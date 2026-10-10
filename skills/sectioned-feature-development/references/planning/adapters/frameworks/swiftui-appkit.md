# SwiftUI / AppKit

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed SwiftUI views/model binding or AppKit delegate/bridge behavior.

Do not select merely because Swift is used on a server or macOS hosts an unrelated service.

## Decisions before sectioning

- Use the existing single source of truth; distinguish view state, binding and persisted model, and avoid a duplicate model just to force refresh.
- Name window/view/delegate/task lifetime, callback ownership and actual main-thread/actor constraints.
- For bridges specify which instance may apply a late result and how selection/identity survives permitted state changes.

## Handoff and smallest useful evidence

Use current XCTest/Swift Testing/UI fixtures and actual scheme. Test the changed state/gesture, not merely model mutation. Platform signing/entitlements are separate and only enter if delivered behavior changes.

SwiftUI and AppKit are not interchangeable: apply AppKit/delegate/NSView bridging advice only to an actual macOS AppKit path; SwiftUI mobile views use their real scene/platform adapter instead.

## Scope boundary

No MVVM/coordinator rewrite, blanket MainActor/unchecked Sendable, Observation migration or new entitlement. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Apple SwiftUI model data](https://developer.apple.com/documentation/SwiftUI/Model-data); [Swift book concurrency source](https://raw.githubusercontent.com/swiftlang/swift-book/main/TSPL.docc/LanguageGuide/Concurrency.md). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
