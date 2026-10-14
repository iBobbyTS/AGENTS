# Mobile applications

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The change targets a mobile user workflow or its platform lifecycle/data behavior.

Do not select merely because Kotlin, Swift, Dart or a mobile SDK appears in unrelated code.

## Decisions before sectioning

- Name visible flow and durable versus screen-local state; define only the relevant interruption/recreation behavior.
- For network work distinguish offline/error/retry from confirmed save, and prevent stale responses overwriting newer intent.
- Identify native/cross-platform plugin and permission/OS boundary from actual target evidence.

## Handoff and smallest useful evidence

Use existing app/widget/instrumented fixtures for the requested lifecycle transition. Unknown device/system behavior is an environment gap, not proof from unit mocks.

## Scope boundary

No universal offline sync, new analytics/auth/background service, framework migration or all-device matrix. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Android app architecture](https://developer.android.com/topic/architecture); [Apple UIKit scenes](https://developer.apple.com/documentation/uikit/scenes); [Flutter architecture guide](https://docs.flutter.dev/app-architecture/guide). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
