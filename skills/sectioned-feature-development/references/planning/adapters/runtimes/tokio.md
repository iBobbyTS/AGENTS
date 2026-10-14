# Tokio

Axis: `adapter/runtime`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Tokio select/task/channel/process path in real Rust source.

Do not select merely because Rust or async syntax exists without Tokio.

## Decisions before sectioning

- Identify which select branch can be dropped and whether the exact awaited operation preserves partial progress.
- Name cancellation, lock/channel ownership, backpressure and shutdown obligations.
- For child processes inspect kill_on_drop/configuration and explicit wait/reap; handle drop alone is not business completion.

## Handoff and smallest useful evidence

Use existing runtime tests for the concrete failure/write/EOF/cancel trajectory. Compilation does not prove shutdown or cancellation safety.

Child termination on drop is configurable; inspect the actual setting rather than assuming the handle owns process completion. A failed-write/cancel/EOF trajectory must check only the operation-specific partial effect, not enumerate every schedule.

## Scope boundary

No runtime replacement, generic actor/supervisor or exhaustive scheduler matrix. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Tokio select](https://docs.rs/tokio/latest/tokio/macro.select.html); [Tokio process Command](https://docs.rs/tokio/latest/tokio/process/struct.Command.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
