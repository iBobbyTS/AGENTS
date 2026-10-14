# Rust

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Rust crate, binary, trait/serde contract or FFI owner.

Do not select merely because Cargo or a Rust-based utility is installed; Rust alone does not imply Tokio.

## Decisions before sectioning

- Confirm edition/MSRV, Cargo features and target used by the deliverable.
- Identify ownership/drop/error/panic boundaries and typed/wire representation through real consumers.
- For asynchronous/process behavior select the actual runtime adapter; memory safety does not prove cancellation, protocol framing or shutdown.

## Handoff and smallest useful evidence

Keep one state/protocol invariant in its parent. Test exported entry paths and the relevant feature/target build; add the concrete failure/EOF/reaping trajectory when lifecycle changes.

## Scope boundary

No blanket Arc<Mutex<_>>, actor framework, runtime replacement, universal no-panic policy or all-features Cartesian gate. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Rust ownership](https://doc.rust-lang.org/book/ch04-00-understanding-ownership.html); [Cargo features](https://doc.rust-lang.org/cargo/reference/features.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
