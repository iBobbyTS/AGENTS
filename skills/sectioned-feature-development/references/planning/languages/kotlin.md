# Kotlin

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Kotlin source, coroutine/Flow contract or Java interop.

Do not select merely because a JVM service or Android dependency exists; Android and Spring are optional adapters.

## Decisions before sectioning

- Identify JVM/Android/Native/JS target, nullability/platform types and interop consumers.
- For coroutines name parent scope, cancellation/exception flow and where blocking work runs.
- For collections/serialization name mutability, absent/default values and public contracts actually affected.

## Handoff and smallest useful evidence

Exercise the actual target and public call; test cancelled/late emissions only when changed. Use the installed kotlinx.coroutines/serialization versions.

## Scope boundary

No automatic Android architecture, Flow conversion, multiplatform migration or dispatcher changes throughout the repository. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Kotlin coroutines basics](https://kotlinlang.org/docs/coroutines-basics.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
