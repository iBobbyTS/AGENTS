# Go

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Go package, executable or concurrency contract.

Do not select merely because Go is installed as tooling; a Go binary can be CLI, service or SDK.

## Decisions before sectioning

- Inspect go.mod/toolchain, package surface and dependency direction.
- Name goroutine/channel owner, context propagation, termination and cancellation effects.
- Distinguish zero/nil/interface values, error wrapping and JSON representation when observable.

## Handoff and smallest useful evidence

Exercise the real package/handler and cancellation/timeout only for changed lifetimes. Existing race tests help when the touched path is shared; no new test matrix merely because goroutines exist.

## Scope boundary

No automatic microservice split, goroutine pool, channel framework or context parameter churn across unrelated code. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Go context](https://go.dev/blog/context). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
