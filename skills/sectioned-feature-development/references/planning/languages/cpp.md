# C++

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed C++ objects/templates, ownership, concurrency or binary interface.

Do not select merely because a build tool uses C++; C and C++ are not interchangeable planning modes.

## Decisions before sectioning

- Confirm standard/library/compiler/ABI and exception/RTTI settings in affected targets.
- State RAII/resource owner, borrowing/lifetime and exception-safety guarantee actually required.
- For callbacks/tasks, trace captures, synchronization and destruction; for public types, identify binary/source consumers.

## Handoff and smallest useful evidence

Exercise the real interface at success and one relevant exception/cancel/destruction boundary. Compile existing supported targets, using available diagnostic tooling only where useful.

## Scope boundary

No blanket smart-pointer conversion, new framework, language-standard migration or universal strong-exception guarantee. No route creates a product requirement, extra review or new test framework.

## Sources and status

[C++ Core Guidelines](https://isocpp.github.io/CppCoreGuidelines/CppCoreGuidelines). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
