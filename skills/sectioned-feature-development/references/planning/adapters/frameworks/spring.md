# Spring

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Spring-managed controller/service/transaction/lifecycle path.

Do not select merely because Java/Kotlin source exists; unknown JVM frameworks use universal fallback.

## Decisions before sectioning

- Name the real proxied production call; default proxy transaction interception does not cover self-invocation.
- Inspect configured rollback rules, exception type, transaction propagation and actual commit boundary.
- Trace DTO/null/default/error envelope and lazy data serialization through actual consumer; do not infer atomicity from an annotation alone.

## Handoff and smallest useful evidence

Use the existing integration fixture where interception/DB behavior matters. A mocked repository is not transaction evidence. SvelteKit adapter→Java/Kotlin endpoint remains two explicit transformations if both exist.

For a cross-stack change, trace the actual DTO/handler and real client decoder; SvelteKit action encoding does not automatically apply to a separate Java HTTP endpoint. A mocked repository alone does not prove transaction interception or database rollback.

## Scope boundary

No new AOP, blanket rollback policy, CQRS, DTO generator or framework/JDK upgrade. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Spring declarative transactions](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/annotations.html); [Spring rollback rules](https://docs.spring.io/spring-framework/reference/data-access/transaction/declarative/rolling-back.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
