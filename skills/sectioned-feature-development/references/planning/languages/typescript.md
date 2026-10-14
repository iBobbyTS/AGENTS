# TypeScript

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed .ts/.tsx source or a public declaration/generic contract.

Do not select merely because the repository only contains a TypeScript-based dependency; TypeScript alone does not imply React, browser or Node.

## Decisions before sectioning

- Inspect target, module resolution, strictness and declaration consumers actually used in the build.
- Distinguish compile-time narrowing/assertions from runtime validation of decoded input.
- Preserve missing/null/union exhaustiveness and public type compatibility only where the feature crosses them.

## Concrete planning example

A response asserted as Group[] still needs the actual decoder/consumer to handle global versus visible groups.

## Handoff and smallest useful evidence

Use actual consumer code plus the existing type check and runtime fixture; a cast or duplicated interface is not evidence that a wire value is valid.

## Scope boundary

No strict-mode migration, schema generator, package-wide any removal or framework assumption. No route creates a product requirement, extra review or new test framework.

## Sources and status

[TypeScript narrowing](https://www.typescriptlang.org/docs/handbook/2/narrowing.html); [MDN promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
