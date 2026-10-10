# Vue / Nuxt

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Vue components/reactivity or a confirmed Nuxt server/render path.

Do not select merely because a JS/TS project exists; Nuxt-specific API behavior requires actual Nuxt evidence.

## Decisions before sectioning

- Name reactive source versus computed display, stable key identity and local draft lifetime.
- For SSR keep request-owned state separate from shared module state and define hydration inputs.
- Inspect actual Nuxt data fetch/cache lifecycle only when used; do not infer it from Vue alone.

## Handoff and smallest useful evidence

Use real component/SSR fixtures and a changed navigation/late-response case where relevant.

## Scope boundary

No Vue/Nuxt migration, global store adoption or mandatory SSR. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Vue SSR](https://vuejs.org/guide/scaling-up/ssr.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
