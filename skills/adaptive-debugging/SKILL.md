---
name: adaptive-debugging
description: Evidence-driven root-cause debugging for second-pass or initially complex failures. Invoke when a previous attempted fix did not resolve the issue, or when the failure is intermittent, cross-layer, environment-specific, concurrent, performance-related, a crash/hang/data-integrity problem, CI/container/network/database related, or a Swift/macOS native runtime, signing, notarization, or sandbox issue. Do not invoke for an obvious deterministic first-pass typo, syntax error, missing import, or isolated low-risk configuration mistake with one direct fix and immediate verification.
---

# Adaptive Debugging

Use this skill to replace patch guessing with a bounded, evidence-led investigation. It is deliberately **not** the default ceremony for every trivial first-pass bug.

## Operating contract

1. **Bypass this skill for a genuinely simple first pass.** Handle the issue directly only when all conditions in [routing-and-complexity.md](references/core/routing-and-complexity.md) are satisfied.
2. **Enter this skill before a second repair attempt.** A proposed or applied fix that did not remove the original failure is a hard trigger.
3. **Enter immediately for an initially complex or high-risk failure.** Do not spend a speculative patch to prove complexity.
4. **Investigate before repairing.** Do not change production behavior until the failure contract, relevant evidence, and a testable root-cause hypothesis exist. Temporary diagnostic instrumentation is allowed when isolated and later removed.
5. **Load only relevant playbooks.** Read the core process, then one or more domain references selected by the observed failure boundaries.
6. **Keep the process proportional.** A localized second-pass issue may need a short evidence ledger and one experiment; a cross-system intermittent failure may need persistent notes and several playbooks.
7. **Finish by re-running the original failure contract.** Passing a nearby unit test is not sufficient if the original symptom was not reproduced and verified.

## Phase 0 — Preserve state and prior attempts

Before making another change:

- Inspect the working tree, recent commits, configuration changes, dependency changes, and environment differences relevant to the failure.
- Identify every prior attempted fix and its observed result. Distinguish “not tested,” “changed the symptom,” and “did not fix.”
- Preserve user work. Do not reset, discard, or overwrite unrelated uncommitted changes.
- Revert or isolate a failed experimental patch when safe. Do not stack a new guess on top of an unproven fix.
- Preserve transient evidence such as CI logs, crash reports, traces, failing seeds, request IDs, timestamps, exact binaries, and dSYMs.

For long, intermittent, multi-run, or multi-agent investigations, create persistent notes with:

```bash
python scripts/debug_session.py init --root . --slug <short-issue-name> --title "<failure summary>"
```

For a small localized investigation, keep the same fields in the working response instead of creating files.

## Phase 1 — Establish the failure contract

Write a compact contract before diagnosis:

```text
Expected:
Observed:
Exact reproduction or observation procedure:
Environment/build/version/commit:
Frequency and earliest known occurrence:
Scope and impact:
Prior attempts and outcomes:
```

Rules:

- Use exact error text, status codes, stack frames, signals, timestamps, inputs, and environment identifiers when available.
- Separate symptoms from interpretations. “Request returns 500” is an observation; “database is broken” is a hypothesis.
- If deterministic reproduction is unavailable, define an observation strategy that can distinguish success, failure, and absence of evidence.
- Ask the user only for evidence or product semantics that cannot be obtained from the repository, runtime, logs, or available tools.

## Phase 2 — Classify complexity and route domains

Read [routing-and-complexity.md](references/core/routing-and-complexity.md).

Select every domain that intersects the causal path; do not label a cross-layer failure by the layer where the user first noticed it.

| Failure boundary | Load |
|---|---|
| Browser, DOM, rendering, cache, service worker, Svelte/SvelteKit, Playwright | [browser-frontend.md](references/domains/browser-frontend.md) |
| HTTP handler, service logic, Node.js, Python, external API, observability | [backend-api.md](references/domains/backend-api.md) |
| Persistent data, SQL, transaction, lock, query plan, PostgreSQL | [database-postgresql.md](references/domains/database-postgresql.md) |
| Race, ordering, cancellation, deadlock, duplicate work, backpressure | [async-concurrency.md](references/domains/async-concurrency.md) |
| DNS, TCP, TLS, proxy, HTTP transport, CORS, packet path | [network.md](references/domains/network.md) |
| Process, OS, filesystem, permissions, resources, signals, runtime environment | [system-runtime.md](references/domains/system-runtime.md) |
| Image, container process, Compose, volume, container network, health check | [docker-containers.md](references/domains/docker-containers.md) |
| Compiler, dependency resolution, bundler, GitHub Actions, build/release CI | [build-ci.md](references/domains/build-ci.md) |
| Intermittent or order-dependent automated tests | [test-flakiness.md](references/domains/test-flakiness.md) |
| Latency, CPU, memory, I/O, throughput, responsiveness | [performance.md](references/domains/performance.md) |
| Swift, AppKit, SwiftUI, Xcode, LLDB, crash, hang, memory, actor isolation | [swift-macos-native.md](references/domains/swift-macos-native.md) |
| macOS code signing, hardened runtime, notarization, Gatekeeper, sandbox, entitlements | [macos-signing-sandbox.md](references/domains/macos-signing-sandbox.md) |

A browser action that produces a backend 500 and then a PostgreSQL lock wait requires browser, backend, and database evidence. Load those three references, not every reference.

## Phase 3 — Build the evidence plan

Read [root-cause-and-evidence.md](references/core/root-cause-and-evidence.md), then produce:

1. **Causal path:** the components and boundaries between input and failure.
2. **Unknowns:** facts that materially separate plausible causes.
3. **Observations:** the cheapest safe evidence to collect at each relevant boundary.
4. **Predictions:** what each leading hypothesis expects those observations to show.
5. **Experiment order:** highest information gain and lowest risk first.

Prefer evidence that discriminates between hypotheses over large undirected log dumps.

At each boundary, capture both sides when possible:

```text
input received → transformation/state → output emitted
```

Correlate observations with stable identifiers such as request ID, trace ID, job ID, transaction ID, task ID, test seed, process ID, build SHA, or crash UUID.

## Phase 4 — Reproduce and localize

- Reproduce under the smallest environment that preserves the failure.
- Compare a failing case with the nearest passing control.
- Find the **first boundary where expected and observed state diverge**, not merely the last place an exception surfaces.
- Trace incorrect values, state, or timing backward to their source.
- For intermittent failures, classify the dependence: timing, order, shared state, environment, load, resource pressure, clock, randomness, or external service.
- Use recent-change inspection or bisection when the failure window is bounded and the experiment is cheaper than manual speculation.
- Record negative evidence. A hypothesis that predicts X and repeatedly produces not-X should lose priority.

Do not repair while localization still has several equally plausible causes unless the proposed change is itself a reversible diagnostic experiment with an explicit prediction.

## Phase 5 — Test explicit hypotheses

Maintain a short hypothesis ledger:

| Hypothesis | Supporting evidence | Contradicting evidence | Unique prediction | Discriminating test | Status |
|---|---|---|---|---|---|

Rules:

- Test one causal claim at a time.
- State the prediction before running the experiment.
- Change one independent variable where feasible.
- Prefer a counterfactual: when the suspected cause is present the failure appears; when it is removed or controlled, the failure disappears.
- Do not treat correlation, a plausible code smell, or “the test passes once” as proof.
- Do not promote a workaround that masks the symptom into the root-cause slot.

## Phase 6 — Prove root cause

A root-cause claim is ready for repair when it explains:

- the original symptom;
- the relevant environment, timing, state, or input dependence;
- why prior attempts failed or changed the symptom;
- the observed evidence at the first failing boundary; and
- a passing control or counterfactual result.

If evidence supports multiple independent causes, list them separately and repair the minimum set required by the failure contract.

## Phase 7 — Repair the source

- Create a regression test or deterministic reproduction before the repair when feasible.
- Make the smallest coherent change at the causal source.
- Preserve intended external behavior and existing contracts unless the user has approved a semantic change.
- Avoid drive-by refactors, dependency upgrades, cache deletion, retry inflation, broad exception swallowing, global locks, arbitrary sleeps, and “reset everything” repairs.
- Add defense in depth only after the source fix, and only where it prevents recurrence or improves diagnosis without hiding errors.
- Keep temporary probes clearly marked; remove them or convert them into intentional observability before completion.

## Phase 8 — Verify the repair

Verification must include:

1. The exact original reproduction or observation procedure.
2. The regression test or targeted check that would fail without the repair.
3. Relevant neighboring tests and static checks.
4. The same build mode, environment, data shape, concurrency, packaging, or distribution path that originally mattered.
5. A diff review for accidental scope growth, hidden behavior changes, leftover instrumentation, secret leakage, and ignored errors.
6. For intermittent failures, repeated or stress execution sufficient to exercise the original trigger, plus disclosure of residual uncertainty.

A changed error message, lower frequency, or a passing unrelated test is not completion.

## Failed repair and escalation policy

When a repair fails verification:

- Mark it failed; do not silently reinterpret the original success criterion.
- Revert or isolate it when safe.
- Add the result to the evidence ledger.
- Return to localization and update hypotheses.

After **two independent repair attempts within this skill fail**, stop making additional speculative changes. Re-evaluate:

- whether the failure contract is wrong or incomplete;
- whether the first failing boundary was misidentified;
- whether hidden shared state or environment drift exists;
- whether the problem is architectural, contractual, or actually contains multiple defects.

Use specialist subagents only when domains can collect independent evidence in parallel. The parent agent must define each subagent’s boundary and synthesize one causal chain. Do not create a default debugging swarm.

## Safety and evidence hygiene

- Do not mutate production data, run destructive database commands, delete Docker volumes, prune caches/images, rotate credentials, disable TLS verification, weaken signing/sandbox entitlements, or remove user data without explicit authorization.
- Treat `EXPLAIN ANALYZE` as statement execution. Do not run it casually against production writes.
- Heap snapshots, packet traces, crash reports, CI logs, environment dumps, and curl traces can contain secrets or personal data. Redact before persisting or reporting.
- Prefer staging, a replica, a copied artifact, a read-only query, or a controlled rollback-capable experiment for risky evidence collection.
- Do not use `sudo`, kill processes, attach debuggers to production, or enable globally verbose logging without checking impact and authorization.

## Completion report

Use [final-report-template.md](references/core/final-report-template.md). Report:

- failure contract;
- root cause and causal chain;
- decisive evidence;
- repair and why it addresses the source;
- exact verification performed;
- remaining uncertainty or follow-up, if any.

Do not claim resolution unless the original failure contract passed.
