# Libraries / SDKs / reusable packages

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

A public reusable library/API/package is the deliverable or changes observably.

Do not select merely because a project uses dependencies but only application internals change.

## Decisions before sectioning

- Define actual public surface, caller preconditions, errors, ownership and supported versions/targets.
- Identify the first real consumer and package build/export path; source tests do not prove installed consumption.
- State compatible versus intentional breaking changes using the repository's existing release/versioning policy.

## Handoff and smallest useful evidence

Use the actual consumer/import/link against the produced package when distribution changes; retain exact public types/serialization examples at seams.

## Scope boundary

No unrequested backward-compatibility matrix, public registry release, codegen or plugin ecosystem. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Semantic Versioning 2.0.0](https://semver.org/); [Cargo features](https://doc.rust-lang.org/cargo/reference/features.html); [Python packaging pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
