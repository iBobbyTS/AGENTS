# Android

Axis: `adapter/platform`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Android lifecycle/component, permission, data or packaged behavior.

Do not select merely because Java/Kotlin/Dart source exists; the language does not prove Android.

## Decisions before sectioning

- Identify Activity/Fragment/Compose/navigation owner and state that survives relevant recreation or process loss.
- Separate screen-local state, durable data and background worker lifetime.
- Confirm actual SDK/target, manifest/permission path and plugin boundary.

## Handoff and smallest useful evidence

Use existing component/instrumented fixtures for the changed lifecycle scenario; declare emulator/device limits and avoid inventing users or privileges.

## Scope boundary

No architecture/Compose migration, universal offline support or new background service without requirement authority. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Android app architecture](https://developer.android.com/topic/architecture). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
