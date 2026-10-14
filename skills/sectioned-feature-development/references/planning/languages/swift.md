# Swift

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Swift source, actor/task, value/reference or public module boundary.

Do not select merely because the host is a Mac; server-side Swift is not a macOS UI project.

## Decisions before sectioning

- Inspect Swift language mode, deployment/toolchain constraints and actual concurrency checking.
- Name value/reference ownership, optional/error representation and callback lifetime across boundaries.
- For task changes, name actor isolation, cooperative cancellation and who may apply a late result; isolation alone does not enforce request freshness.

## Handoff and smallest useful evidence

Use the actual module/API and relevant cancellation/error test. Load SwiftUI/AppKit or Apple platform adapters only if their code and lifecycle are touched.

## Scope boundary

No blanket MainActor, unchecked Sendable, Observation migration or Apple UI assumption. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Swift book concurrency source](https://raw.githubusercontent.com/swiftlang/swift-book/main/TSPL.docc/LanguageGuide/Concurrency.md). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
