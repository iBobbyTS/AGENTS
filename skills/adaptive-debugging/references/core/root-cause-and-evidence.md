# Root Cause and Evidence Playbook

## Evidence hierarchy

Prefer, in descending order:

1. A controlled reproduction with a counterfactual or passing control.
2. Runtime state captured at the first failing boundary.
3. Correlated traces, crash reports, packet captures, profiles, or structured logs.
4. Deterministic tests that exercise the causal path.
5. Static code/configuration evidence consistent with runtime behavior.
6. Intuition, common failure patterns, and code smells.

Lower levels generate hypotheses; they do not override contradictory higher-level evidence.

## Build a causal map

Represent the path from trigger to symptom:

```text
user/input/event
  → boundary A input/output
  → state transformation
  → boundary B input/output
  → side effect or persisted state
  → observed failure
```

For each node record:

- owner/component/process;
- relevant identifier and timestamp;
- expected input/state/output;
- observed input/state/output;
- whether evidence is direct, inferred, or missing.

The first divergence is the localization target. A stack frame where the process aborts may be downstream of the source.

## Boundary instrumentation

At a component boundary, prefer a compact structured event:

```text
time, correlation_id, component, operation,
input_shape_or_hash, state_version, result/status,
latency, error_type
```

Do not log full tokens, passwords, personal records, cookies, authorization headers, or unbounded payloads. Hash or summarize sensitive values when equality—not content—is what matters.

Collect both sides of a boundary when possible. If the client says it sent X and the server says it received Y, capture the proxy/network layer before blaming serialization or application state.

## Backward tracing

When a bad value or state appears:

1. Identify where it became observably wrong.
2. Find the immediate producer/caller.
3. Inspect the producer’s inputs and preconditions.
4. Repeat until the value/state first diverges from a valid source.
5. Test that source with a controlled valid/invalid input.

Do not stop at the first function that notices invalid state.

## Classify non-determinism

Use evidence to assign one or more classes:

- **Timing:** delay or relative scheduling changes outcome.
- **Order:** test/request/event sequence changes outcome.
- **Shared state:** another execution leaves state behind.
- **Environment:** version, architecture, locale, timezone, permissions, filesystem, or config differs.
- **Load/resource:** pressure, queue depth, memory, descriptors, CPU, I/O, or network saturation changes outcome.
- **Clock:** wall-clock jumps, expiration, daylight-saving, monotonic-vs-wall time.
- **Randomness:** seed or generated data matters.
- **External dependency:** availability, consistency, response shape, or rate limit changes.

Instrument the suspected dimension; do not label a failure “random.”

## Hypothesis quality

A useful hypothesis has four parts:

```text
Cause: <specific mechanism>
Because: <existing evidence>
Prediction: <observable result unique enough to distinguish it>
Test: <safe experiment that can falsify it>
```

Weak: “There may be a race.”

Strong: “Two handlers update the same version without a compare-and-swap; under parallel execution both read version 14, so logs should show duplicate version-14 writes and serial execution should eliminate the failure.”

## Experiment design

- State the prediction before collecting results.
- Change one independent variable when possible.
- Include a passing control.
- Prefer the smallest experiment that separates the top hypotheses.
- Preserve the exact binary, config, input, seed, and data snapshot for expensive reproductions.
- Separate diagnostic perturbations from repairs. Artificial delay may reveal timing dependence but is not the fix.
- Record commands, environment, result, and interpretation. Do not record only the conclusion.

## Recent changes and bisection

Use history when the failure has a bounded onset:

- inspect relevant commits, lockfiles, migration history, build images, deployment manifests, entitlements, and toolchain versions;
- compare the nearest known-good and known-bad artifact under the same reproduction;
- bisect only when each run has a reliable pass/fail classification and the cost is lower than direct localization;
- do not mistake correlation with a broad commit for the causal line—inspect the changed boundary.

## Expensive or one-shot reproduction

Before consuming the next run:

1. List all plausible failure boundaries.
2. Add low-risk observations that cover those boundaries in one execution.
3. Ensure clocks and correlation IDs can join the evidence.
4. Confirm storage capacity, privacy, and logging overhead.
5. Define what each possible outcome will eliminate or support.
6. Preserve raw artifacts before summarizing them.

Avoid repeated single-probe runs when one carefully instrumented run can distinguish several hypotheses.

## Proving causality

Strong causal evidence commonly uses one or more:

- the failure follows the suspected input/state and disappears with a controlled valid alternative;
- the suspected operation is absent in a passing trace and present at the first divergence in a failing trace;
- a sanitizer/race detector/debugger stops at the violating access;
- the same artifact fails or passes solely according to one environment variable or permission;
- a targeted regression test fails before and passes after the source repair;
- reversing the repair restores the failure.

A workaround can be acceptable operational mitigation, but report it separately from root cause and permanent repair.

## Failed fixes as evidence

For each failed attempt record:

```text
Change:
Hypothesis it was meant to test:
Prediction:
Observed outcome:
What the result rules out or leaves open:
Whether the change was reverted:
```

Do not carry failed changes forward unless they are independently justified.
