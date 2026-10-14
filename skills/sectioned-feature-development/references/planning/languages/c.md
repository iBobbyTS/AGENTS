# C

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed C translation units, headers or a C ABI boundary.

Do not select merely because a C++ source or a native dependency exists without changes to C code.

## Decisions before sectioning

- Confirm C standard/dialect, target data model, ABI and compiler options actually shipped.
- Name allocation/free ownership, buffer length/termination, alignment, signedness and error convention across callers.
- Identify invalidated pointer lifetime and synchronization rules where mutable memory or interrupts are involved.

## Handoff and smallest useful evidence

Use a boundary-sized/truncated input and a failure cleanup example through the actual entry. Existing compiler warnings/sanitizer targets can support evidence but do not prove all behavior or require new infrastructure.

## Scope boundary

No whole-repo rewrite to another language, universal hardening parser, new allocator or blanket sanitizer gate. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Clang UndefinedBehaviorSanitizer](https://clang.llvm.org/docs/UndefinedBehaviorSanitizer.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
