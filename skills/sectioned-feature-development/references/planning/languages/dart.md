# Dart

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Dart library, async stream/future or isolate boundary.

Do not select merely because Flutter is present in another package; Dart does not imply mobile or Flutter.

## Decisions before sectioning

- Confirm SDK, sound-null-safety contract and actual native/web target.
- Name Future/Stream subscription ownership, error propagation and cancellation after navigation/shutdown where relevant.
- For isolate work, define transferred data and ownership rather than assuming shared-memory execution.

## Handoff and smallest useful evidence

Test actual public consumer, serialization and subscription cancellation if changed; add Flutter for widget/lifecycle semantics only.

## Scope boundary

No isolate conversion, new state management library, all-platform test matrix or mandatory Flutter architecture. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Dart concurrency](https://dart.dev/language/concurrency). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
