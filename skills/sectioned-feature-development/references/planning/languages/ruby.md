# Ruby

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Ruby method/module, IO, extension boundary or package.

Do not select merely because Rails is mentioned but not on the changed path; Ruby is also used for CLI and libraries.

## Decisions before sectioning

- Inspect Ruby/runtime version, gem dependencies and actual loading/entry contract.
- Name block/exception/ensure ownership for IO and cleanup; distinguish returned values from external side effects.
- Resolve hash key conventions, nil/false and mutable shared objects when their meaning crosses an interface.

## Handoff and smallest useful evidence

Exercise the actual public method/command with relevant error/close behavior; select Rails only for framework-owned callbacks/transactions.

## Scope boundary

No blanket metaprogramming removal, actor redesign, Rails migration or unrelated monkey-patch cleanup. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Ruby IO](https://ruby-doc.org/3.4.1/IO.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
