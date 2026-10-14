# Async, concurrency and process lifecycle planning

Select for changed ordering, retries, cancellation, stale results, tasks/processes, shared resources or partial side effects. This file adds a failure trajectory to the actual stack, not a generic concurrency framework.

## Minimal trajectory

Name the authoritative owner and relevant states, then trace only the affected transitions:

```text
start → in-flight → success | failure | cancel
             → late completion | retry | shutdown/restart (when in scope)
```

For each changed transition: input/event, identity/version, resource/state owner, already-visible side effects, output and who observes completion. Distinguish request accepted, task completed, result consumed and resource released. A timeout may be a stopped wait rather than cancelled work.

Identify lock/transaction/channel scope and blocking points using source. Before permitting a retry, know whether the prior effect occurred and whether the existing contract permits replay. Do not invent idempotency or exactly-once promises. For cancellation, check the actual runtime operation; Swift cooperative cancellation, Python cancellation propagation and Rust dropped futures do not have identical semantics.

## Decompose and verify

Do not split one invariant across independently accepted sections. Internal worker/adapter/state projection can be subsections only with a shared contract and parent reconciliation. When sibling work is parallel, declare shared test DB/ports/cache/process resources as well as files.

A deterministic event fixture or controlled failure at the changed boundary is often enough. Include the stale/late/repeated event that would reveal the defect, not arbitrary sleeps or a new exhaustive scheduler. A compile/test PASS cannot establish an unexercised process-reap or shutdown path; identify required real evidence or record the gap.

## Avoid

No blanket locks, generalized actors, supervisor layers, durable queues, global retry engines, distributed consensus or full failure matrix without a requirement. The agent's own waiting/dispatch lifecycle remains governed by the root Skill, not this product-domain module.

## Sources

[Python tasks](https://docs.python.org/3/library/asyncio-task.html); [Swift concurrency](https://raw.githubusercontent.com/swiftlang/swift-book/main/TSPL.docc/LanguageGuide/Concurrency.md); [Tokio select](https://docs.rs/tokio/latest/tokio/macro.select.html).
