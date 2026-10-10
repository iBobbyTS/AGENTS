# iOS / iPadOS

Axis: `adapter/platform`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Apple mobile scenes, app lifecycle, permission, storage or delivery path.

Do not select merely because Swift/Dart/JS is present; confirm the actual Apple target.

## Decisions before sectioning

- Identify scene/application lifetime and data that must survive only the lifecycle events required by the task.
- Separate foreground UI from permitted background work, system interruptions and denied permissions.
- For native/plugin interfaces use actual deployment target, schema and delivered resource path.

## Handoff and smallest useful evidence

Test the changed scene/navigation/permission trajectory using existing simulator/device tools; mark device-only behavior unverified when unavailable.

## Scope boundary

No assumption of arbitrary background execution, new entitlement, app-wide state migration or mandatory device matrix. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Apple UIKit scenes](https://developer.apple.com/documentation/uikit/scenes). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
