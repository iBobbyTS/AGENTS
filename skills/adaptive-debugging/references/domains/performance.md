# Performance and Resource Debugging

Load this playbook for latency, throughput, responsiveness, CPU, memory growth, I/O, database, browser, native-app, or resource-exhaustion problems.

Do not optimize without defining the metric, workload, environment, and baseline.

## Performance contract

Record:

```text
metric and percentile/aggregation:
target or regression threshold:
workload/input/data size/concurrency:
warm-up and measurement window:
hardware/OS/runtime/build mode:
commit/config/dependency versions:
baseline and current result:
user-visible impact:
```

Use release/production-equivalent builds when optimization or compiler behavior matters. Debugger attachment, sanitizers, verbose logging, and debug builds can distort results; record them as experimental conditions.

## Classify the bottleneck

- **CPU:** sustained execution or hot code path;
- **latency/wait:** network, lock, queue, timer, I/O, dependency;
- **memory:** retained heap, native allocation, cache, mapping, fragmentation, child process;
- **disk/filesystem:** throughput, latency, sync, metadata, inode or space pressure;
- **database:** query latency, lock, connection pool, plan/cardinality;
- **browser/UI:** main-thread long tasks, layout/paint, network, hydration, memory retention;
- **native UI:** main-thread/MainActor blocking, rendering, allocation, I/O;
- **capacity/backpressure:** queue depth, pool saturation, throttling, retries.

A high-level metric identifies where to profile; it does not identify the source line.

## Measurement discipline

- Hold input, dataset, concurrency and environment constant for comparisons.
- Separate cold start, warm steady state and cache effects.
- Repeat enough to see variance; compare distributions/percentiles, not one lucky run.
- Measure end-to-end user impact and component submetrics.
- Use monotonic clocks for durations.
- Record profiling overhead and sampling interval.
- Compare a known-good build under the same workload when possible.

## CPU and latency

Use sampling profiles first for broad hot paths, then tracing/instrumentation for a specific transaction.

Look for:

- unexpected call count, recursion or retry loops;
- serialization/deserialization and copying;
- lock/queue wait versus active CPU;
- blocking I/O on an event loop/main thread;
- N+1 database/network calls;
- expensive layout/render cycles;
- work repeated across cache boundaries;
- debug/logging overhead;
- CPU throttling or quota.

Optimize the largest causal contributor, remeasure, and verify behavior.

## Memory

Build a lifecycle experiment:

```text
baseline → perform operation N times → release/leave scope → settle → capture
```

Compare retained objects/allocations and owning paths. Distinguish heap, native, mapped, cache and child-process memory. A stable high-water mark may be expected; monotonic retention after lifecycle completion suggests a leak or unbounded cache.

Do not treat forced garbage collection or app restart as repair.

## Platform tools

### Browser

Use Chrome Performance for main-thread/network/rendering timing and Memory tools for allocation/retaining paths. Load [browser-frontend.md](browser-frontend.md).

### Node.js

Use CPU profiles, event-loop delay/utilization, heap snapshots/allocation profiles and diagnostic reports. Snapshot a safe replica when production pause/memory risk is material.

### Python

Use `cProfile`/profilers for CPU and `tracemalloc` for Python allocation traceback comparisons. Include native-extension and process RSS evidence when Python heap does not explain memory.

### PostgreSQL

Use `pg_stat_statements`, activity/wait evidence and safe plans. Load [database-postgresql.md](database-postgresql.md). Query frequency can dominate even when one execution is fast.

### Linux/system

Use process metrics, `vmstat`, `iostat`, cgroup stats/pressure, and a sampling profiler such as `perf` where permitted. Confirm CPU throttling, I/O wait and memory pressure before changing application code.

### Swift/macOS

Use Instruments Time Profiler, Hangs, Allocations, Leaks, System Trace and signposts around the user operation. Load [swift-macos-native.md](swift-macos-native.md). Profile the intended release configuration and device/architecture.

## Database and network call amplification

Count calls per user operation and correlate IDs. Common sources:

- N+1 query/request loops;
- duplicate retries;
- repeated invalidation/refetch;
- missing batching/pagination;
- cache key mismatch;
- serial dependency chain that could safely overlap;
- response/payload far larger than needed.

Do not parallelize or cache until consistency, ordering, cancellation and error semantics are explicit.

## Common causal chains

```text
blocking file read on main actor → UI hang → watchdog termination
N+1 query introduced by serializer → latency grows with rows → local small data hides regression
unbounded listener/cache retention → memory grows per navigation → eventual OOM
proxy retry + application retry → request amplification → dependency saturation
container CPU quota → event-loop delay → health timeouts → restart loop
missing signposts/correlation → profile samples cannot map to user operation → wrong hot path optimized
```

## Completion evidence

- baseline and target metric under a defined workload;
- profile/trace that identifies the dominant causal contributor;
- source repair with before/after measurements under matched conditions;
- functional and concurrency correctness checks;
- no unexplained regression shifted to another resource or percentile;
- residual variance and untested scale disclosed.
