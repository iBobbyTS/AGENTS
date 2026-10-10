# Angular

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Angular component, service, router or dependency lifetime.

Do not select merely because TypeScript code exists without Angular owners.

## Decisions before sectioning

- Name component/input/service state owner and actual initialization/destruction path.
- Identify observable/subscription and request lifetime in the installed Angular/RxJS conventions.
- Determine which changed action updates rendered state, including navigation/cancel and form error cases.

## Handoff and smallest useful evidence

Use existing component/router/service tests through real bindings; subscriptions need closure only where lifecycle changed.

## Scope boundary

No zone/signal/standalone migration, global DI changes or new state framework. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Angular lifecycle](https://angular.dev/guide/components/lifecycle). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
