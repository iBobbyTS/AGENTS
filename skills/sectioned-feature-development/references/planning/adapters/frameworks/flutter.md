# Flutter

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Flutter widgets, navigation, model binding or plugin boundary.

Do not select merely because Dart code exists or a mobile target is mentioned.

## Decisions before sectioning

- Name data owner versus widget-local draft and navigation/lifecycle identity.
- Trace Future/Stream completion into the correct mounted/current state; specify cancellation and error presentation where changed.
- For plugin work preserve the actual Dart/native contract and relevant target support, not all platforms.

## Handoff and smallest useful evidence

Use the existing widget/integration tests through changed interaction and plugin adapter; mock limitations remain explicit.

## Scope boundary

No mandatory MVVM/state-library migration, plugin rewrite or expansion of supported devices. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Flutter architecture guide](https://docs.flutter.dev/app-architecture/guide); [Dart concurrency](https://dart.dev/language/concurrency). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
