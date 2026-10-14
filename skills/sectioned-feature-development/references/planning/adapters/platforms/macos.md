# macOS

Axis: `adapter/platform`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed macOS app/window/helper/XPC/device or packaged launch behavior.

Do not select merely because development happens on a Mac; Python/Rust service hosting alone is insufficient.

## Decisions before sectioning

- Confirm deployment target/architectures and actual app/document/settings/helper state owner.
- Trace files/device/XPC connection privileges and lifecycle only where the feature changes them.
- For distribution changes identify existing signed helper/resources, entitlements and launch path; separate debug success from packaged behavior.

## Handoff and smallest useful evidence

Use existing app/IPC fixtures and actual delivered artifact path when packaging changes. Source languages and SwiftUI/AppKit are separate selections.

## Scope boundary

No notarization pipeline, entitlement addition, sandbox disablement or architecture migration just because macOS is selected. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Apple Developer ID distribution](https://developer.apple.com/developer-id/); [Apple SwiftUI model data](https://developer.apple.com/documentation/SwiftUI/Model-data). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
