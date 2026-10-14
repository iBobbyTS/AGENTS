# Systems software / daemons / local IPC

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The feature changes a long-lived service, IPC/protocol handler, process lifecycle or resource owner.

Do not select merely because Rust/C++ is present or an app launches unchanged tooling.

## Decisions before sectioning

- Separate process alive, request accepted, work completed, response delivered and resources reaped.
- Name one lifecycle/state owner, correlation identity and cancellation/restart behavior required by the feature.
- Probe a truly unknown external runtime/framing contract before designing against it; determine which clients/jobs survive which failure.

## Handoff and smallest useful evidence

Use an actual bounded protocol/process lifecycle fixture and observed result; distinguish client disconnect from job cancellation and stale status from new work. Review remains a different pass from implementing.

## Scope boundary

No second supervisor, HMAC/journal/evidence framework, hostile same-UID threat model or new durability guarantees without authority. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Node streams](https://nodejs.org/api/stream.html); [Tokio process Command](https://docs.rs/tokio/latest/tokio/process/struct.Command.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
