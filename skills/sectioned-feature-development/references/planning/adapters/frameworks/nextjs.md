# Next.js

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Next.js routing, Server/Client Components, mutation or caching path.

Do not select merely because a React app exists; inspect App/Pages Router and installed version.

## Decisions before sectioning

- Mark server/client boundary, serialized props and secret-bearing server-only code.
- Name actual request/data-cache invalidation and post-mutation reader behavior.
- Show client→action/route→data→render examples; do not apply one release's cache defaults to another.

## Handoff and smallest useful evidence

Use actual router/consumer tests and one hydration/cache/failure trajectory for the changed behavior.

## Scope boundary

No router migration, server-action conversion or global cache invalidation. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Next.js server/client components](https://nextjs.org/docs/app/getting-started/server-and-client-components). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
