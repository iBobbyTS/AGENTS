# Async and Concurrency Debugging

Load this playbook for races, nondeterministic ordering, deadlocks, livelocks, starvation, cancellation bugs, duplicate work, retry interactions, queue/backpressure failures, or shutdown/resource-lifecycle problems.

## Classify the mechanism

Do not use “race condition” as a generic label. Distinguish:

- **data race:** unsynchronized conflicting memory access;
- **logical race:** individually synchronized operations produce wrong order/state;
- **lost update / check-then-act:** state changes between observation and mutation;
- **deadlock:** tasks wait in a cycle with no progress;
- **livelock:** tasks run/retry but make no progress;
- **starvation:** one task/resource cannot obtain service;
- **cancellation leak:** cancelled work leaves resource/state or later commits;
- **duplicate delivery/execution:** retries or at-least-once delivery repeat side effects;
- **backpressure failure:** producer outpaces bounded consumer/resource;
- **shutdown race:** teardown overlaps in-flight work.

Write the expected ordering and ownership contract before selecting a fix.

## Capture a concurrency timeline

Use monotonic timestamps and stable task/request/job IDs. Record:

```text
time, task/thread/actor/queue, operation,
state version, lock/resource, wait/acquire/release,
cancellation/deadline, attempt, outcome
```

Wall-clock timestamps alone can misorder events. Include sequence/version numbers around shared state where possible.

Create a timeline for one failing execution and one passing control. Identify the first forbidden interleaving.

## Discriminating experiments

Useful controls include:

- run with one worker/thread/process versus the original parallelism;
- repeat with a preserved seed and event order;
- insert a **diagnostic** barrier or delay at one boundary to widen/narrow a suspected window;
- force cancellation or timeout at specific lifecycle points;
- apply load while holding input/data constant;
- replace an external dependency with a deterministic barrier-capable fake;
- check duplicate delivery using idempotency keys and unique operation IDs;
- capture all task/thread stacks during a hang.

Artificial sleeps, serialization, or a global lock may establish timing dependence but are not automatically acceptable repairs.

## Tooling

### Thread and memory sanitizers

Use a platform/runtime-supported sanitizer in a controlled build:

- ThreadSanitizer for conflicting memory accesses and lock-order clues;
- AddressSanitizer for use-after-free, buffer errors, and related corruption;
- UndefinedBehaviorSanitizer where applicable.

A sanitizer only observes exercised paths. Preserve the exact workload and do not conclude “no race” from one clean run. Sanitizer builds alter timing and memory layout; combine with a causal timeline.

### Go

Run the relevant tests or workload with the race detector:

```bash
go test -race ./path/...
go run -race ./cmd/app
```

Keep the failing concurrency path exercised; detector silence on an unexecuted path is not evidence.

### Python asyncio

Use asyncio debug mode to surface never-awaited coroutines, slow callbacks, wrong-thread loop calls, pending tasks, and unclosed transports. Inspect cancellation propagation and `finally` cleanup.

### Node.js

Measure event-loop delay, open handles, timers, promise/task lifecycles, worker messages, and abort-signal propagation. Blocking the event loop can mimic a network timeout or deadlock.

### Swift

Load [swift-macos-native.md](swift-macos-native.md) for actors, `Sendable`, strict concurrency checking, MainActor, continuations, Task cancellation, and Xcode Thread Sanitizer.

## Repair patterns—only after proof

Select the mechanism matching the contract:

- atomic compare-and-swap/version check for lost updates;
- transaction or unique constraint for cross-process invariants;
- consistent lock ordering and minimal critical sections;
- actor/queue ownership for mutable state;
- idempotency key and durable deduplication for repeated delivery;
- structured concurrency and explicit cancellation cleanup;
- bounded queue/semaphore with defined backpressure behavior;
- condition-based waiting rather than fixed sleep;
- immutable snapshots/message passing where shared mutation is unnecessary.

Do not silence detector warnings with unsafe annotations, broad lock scopes, or disabled checks without demonstrating the intended ownership model.

## Deadlock investigation

- Capture all thread/task/process stacks at the same time.
- Record held and awaited resources.
- Build a wait-for graph.
- Include database locks, file locks, IPC/XPC calls, dispatch queues, semaphores, and synchronous callbacks—not only language mutexes.
- Verify whether a timeout breaks the cycle or merely abandons work while locks remain.

## Cancellation and timeout investigation

Trace deadline ownership end to end:

```text
client timeout → proxy timeout → service context → DB/external call → cleanup/commit
```

Ask:

- Does cancellation stop work, or only stop waiting?
- Can work commit after the caller retries?
- Are resources released in every cancellation path?
- Is cancellation converted into a generic error and retried incorrectly?
- Is partial state externally visible?

## Completion evidence

- one explicit forbidden interleaving or wait-for cycle;
- a deterministic/stress regression that exercises the mechanism;
- detector/timeline/control evidence where applicable;
- verification under original parallelism, cancellation, load, and retry conditions;
- no arbitrary sleep or retry increase presented as root-cause repair.
