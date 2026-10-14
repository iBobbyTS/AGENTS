# Backend, API, and Service Debugging

Load this playbook for HTTP handlers, service logic, external integrations, Node.js or Python runtimes, request failures, wrong payloads, timeouts, or missing observability.

## Establish the request contract

Capture one exact failing transaction:

```text
client/request ID:
method + normalized URL:
request headers/body shape:
authentication/authorization context:
expected status/body/side effect:
observed status/body/side effect:
service version/commit/config:
upstream/downstream dependencies:
```

Redact credentials and personal data. Preserve enough shape, length, hashes, IDs, and schema/version information to compare failing and passing requests.

## Trace boundaries, not just stack frames

Follow the same correlation ID through:

```text
edge/proxy
→ router/middleware
→ validation/auth
→ handler/service
→ cache/queue/database/external API
→ response serialization
```

At each boundary record input, output/status, latency, retry/attempt number, and error type. If trace context is lost, repair propagation or add a temporary correlation field before guessing which service failed.

Distinguish:

- request never reached service;
- service rejected it intentionally;
- service crashed or returned an unexpected error;
- downstream timed out or returned malformed data;
- side effect succeeded but response failed;
- retry duplicated a non-idempotent side effect.

Load network, database, or concurrency playbooks when the first divergence enters those domains.

## HTTP and API checks

- Confirm the exact deployed route, method, content type, body encoding, query normalization, and proxy prefix.
- Compare raw request/response with generated client or UI interpretation.
- Preserve status code, error code, headers, and structured error body; do not collapse all errors into a generic 500.
- Check timeout ownership at every layer. The shortest timeout may abort a request while downstream work continues.
- Trace redirects and authentication refresh independently from application retries.
- Verify idempotency keys, deduplication, and transaction boundaries for retried mutations.
- Confirm schema/version compatibility between clients and services.
- Treat validation, authorization, not-found, conflict, rate-limit, dependency, and internal failures as distinct contracts.

## Structured observability

Use stable fields rather than concatenated prose:

```text
timestamp, severity, service, version, environment,
trace_id, span_id, request_id, operation,
attempt, status, latency_ms, error_type
```

Correlate logs with traces where available. Add spans around meaningful service and dependency boundaries, not every helper function. Record exceptions with stack and causal context, but avoid duplicate logging at every layer.

Do not log passwords, cookies, authorization headers, raw access tokens, full payment/personal records, or unrestricted request bodies.

## Node.js workflow

### Inspector and breakpoints

Use the inspector on a controlled local/staging process:

```bash
node --inspect-brk path/to/app.js
# or the project's normal command with NODE_OPTIONS=--inspect-brk
```

Break at the first wrong state transition, not only the final throw. Inspect async call stacks, closures, request IDs, and active promise/task state.

Do not expose the inspector port publicly or attach it to production without explicit authorization.

### Diagnostic reports

For crashes, fatal errors, signals, or hard-to-observe runtime state, use Node diagnostic reports in a safe environment or configure a controlled production capture. A report can include process, stack, libuv handles, environment, and resource details; treat it as sensitive.

Examples:

```js
const path = process.report.writeReport();
console.error(`diagnostic report: ${path}`);
```

Use `--report-on-fatalerror`, `--report-on-signal`, or related flags only after checking storage, privacy, and signal behavior for the deployed version.

### Event loop, CPU, and memory

- For latency with low external wait, measure event-loop delay and capture a CPU profile.
- For memory growth, compare heap snapshots/allocation profiles around a controlled lifecycle and identify retaining paths.
- Heap snapshots can pause the process and require substantial memory; prefer a replica or disposable worker.
- Inspect open handles, timers, sockets, listeners, and unresolved promises when shutdown hangs.
- Use `diagnostics_channel` or existing instrumentation for low-overhead boundary events when supported by the application.

Avoid “fixing” event-loop stalls by increasing timeouts or worker counts before identifying the blocking work.

## Python workflow

### Interactive localization

Use `breakpoint()`/`pdb` at the first divergence in a controlled run. Inspect locals, call stack, exceptions, and the exact input that selects the failing path.

For unhandled faults or deadlocks where normal logging is incomplete:

```bash
python -X faulthandler -m your_module
```

or enable `faulthandler` programmatically. Preserve all thread stacks when a process hangs.

### Asyncio

Enable debug mode in a development/test reproduction:

```bash
PYTHONASYNCIODEBUG=1 python -X dev -m your_module
```

Inspect never-awaited coroutines, slow callbacks, wrong-thread event-loop calls, pending tasks, cancellation paths, and unclosed transports. Debug mode changes overhead; use it as evidence, not as the production fix.

### Memory

Use `tracemalloc` snapshots to compare allocations before/after the smallest lifecycle. Filter framework noise, group by traceback, and verify retained application objects rather than relying only on RSS.

## External dependency failures

For each dependency record:

- endpoint/version/region;
- request ID or provider correlation ID;
- timeout and retry policy at each layer;
- raw status/error shape;
- rate-limit headers;
- whether the operation is idempotent;
- whether the dependency may return stale/eventually consistent data.

Reproduce with a safe direct client only when it preserves authentication and transport semantics. A mocked success does not rule out network, TLS, proxy, or provider behavior.

## Common causal chains

```text
proxy timeout < service timeout → client receives 504 → service commits mutation → retry duplicates mutation
lost trace context → downstream error cannot be joined → wrong service patched
exception swallowed and converted to empty result → cache stores empty response → persistent user-visible stale state
blocking CPU work on Node event loop → health checks time out → orchestrator restarts healthy process
async task cancelled after response timeout → cleanup skipped → resource leak
client/server schema skew → valid new field rejected by old deployment → environment-only 4xx
```

## Completion evidence

- one correlated failing request and passing control;
- first failing service/dependency boundary;
- regression test at the contract level plus relevant unit/integration checks;
- verification under the original proxy/timeouts/retry/environment conditions;
- no sensitive diagnostic artifacts left in source control or logs.
