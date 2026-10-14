# React

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed React components/hooks or React-owned state.

Do not select merely because JS/TS code exists or a component library is installed.

## Decisions before sectioning

- Name source versus derived state; avoid effects that merely mirror render-derived values.
- For async effects/events, identify cleanup, stale-result and component identity boundaries.
- Give the consumer the actual API/action result, and separate optimistic UI from confirmed persistence.

## Handoff and smallest useful evidence

Use existing component/browser fixtures for the changed gesture and failure, not just a helper or mount check.

## Scope boundary

No state-library migration, effect wrapper framework or Next.js assumption. No route creates a product requirement, extra review or new test framework.

## Sources and status

[React effects](https://react.dev/learn/you-might-not-need-an-effect). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
