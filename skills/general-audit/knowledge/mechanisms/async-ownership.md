# Concurrency, cancellation and ownership

**Trigger:** background tasks, queues, subprocesses, retries, leases, timeouts, shared mutable state or shutdown.

**Hypothesis:** cancellation stops waiting but leaves work running; a stale owner can still commit; repeated delivery repeats the effect; a queue/lock protects admission but not the entire invariant.

**Distinguish:** draw the relevant lifecycle: admitted → owned → effect begun → committed → acknowledged → released. Identify the owner after timeout, disconnect and restart. Inspect exact runtime semantics rather than assuming all async APIs cancel alike. Use a controlled barrier or deterministic sequence where possible; activate a real race window and observe effects, resource release and subsequent progress. Do not rely only on sleep-based timing luck.

**Counterevidence:** deliberate detached work can be correct if durable ownership and results are handled; dropping partially read data may be acceptable during final shutdown. An at-least-once queue is not defective merely for redelivery. Establish which invariant requires cancellation, fencing or idempotence.

**Expansion:** follow shared ownership tokens, cancellation wrappers and acknowledgement logic. A violated invariant may be local to one unsafe cancellation point, not a reason to replace the runtime. If uncertainty depends on OS/process-tree behavior, use actual platform docs/probes and declare limits.

**Closure:** test both the interruption and what happens afterward, including a second legitimate actor or resumed process. “Timeout returned” and “handle dropped” are not sufficient outcome assertions.

The lifecycle sketch is a prompt to investigate actual owners, not a mandatory new state machine.
