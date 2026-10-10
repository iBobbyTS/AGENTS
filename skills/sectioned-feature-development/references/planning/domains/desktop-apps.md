# Desktop applications

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

A requested feature changes window/document/editor/device/helper workflows in a desktop application.

Do not select merely because the developer is on a desktop machine; CLI services are separate domains.

## Decisions before sectioning

- Name application/window/document lifetime and the source of truth for draft versus persisted state.
- Trace UI command→background/IPC/device result→state update including close/reopen or late response only when changed.
- Identify actual native/web UI toolkit and OS delivery boundary separately; desktop is not Swift/macOS by default.

## Handoff and smallest useful evidence

Use actual event/controller and existing UI/IPC fixtures; packaging checks only when helper/resources/launch change. Keep cross-process invariants in a single parent.

## Scope boundary

No toolkit rewrite, architecture pattern migration, new privileges or deployment pipeline by default. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Apple SwiftUI model data](https://developer.apple.com/documentation/SwiftUI/Model-data); [Apple Developer ID distribution](https://developer.apple.com/developer-id/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
