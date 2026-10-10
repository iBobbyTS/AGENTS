# Async APIs and child processes: verify the actual semantics

**Select only:** runtime cancellation, task lifetime, process lifetime or scheduling decides the finding. Inspect the project's runtime version and actual API; the language alone does not select this card's examples.

In Python asyncio, default gather exception propagation and TaskGroup failure handling have different consequences for sibling work. Cancellation also involves task cooperation and cleanup. Trace what owns outstanding work after an exception or timeout, rather than translating “await failed” to “all effects stopped.” ([Python asyncio docs](https://docs.python.org/3/library/asyncio-task.html))

Tokio select cancellation safety depends on the particular operation being dropped. A loop that restarts a non-cancellation-safe operation can lose progress. Yet losing a partial read during final shutdown may be acceptable. A spawned child process has its own lifetime: Tokio Command's default does not kill it merely because its Child handle is dropped; kill-on-drop also does not by itself certify an entire process tree's cleanup. Inspect platform behavior and wait/reap ownership where relevant. ([Tokio select](https://docs.rs/tokio/latest/tokio/macro.select.html), [Tokio Command](https://docs.rs/tokio/latest/tokio/process/struct.Command.html))

**Distinguish:** use a safe helper task/process with a observable disposable effect. Trigger the actual timeout/cancel/exception path, then check outstanding work, effects and release. Prefer a controlled barrier over an arbitrary sleep. Verify the next operation still works and no stale writer can commit, if that is the contract.

**Counterevidence:** deliberate durable background execution, cancellation-safe APIs, proper ownership or supported lossy shutdown can defeat the hypothesis. Do not recommend a new runtime or a global task framework merely because detached work exists. Never spawn an unbounded process tree or touch production to reproduce a lifetime issue.
