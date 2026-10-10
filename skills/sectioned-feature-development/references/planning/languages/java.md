# Java

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Actual Java source, class/module API or Java runtime behavior is changed.

Do not select merely because a backend exists; Kotlin or another JVM language is not Java, and Java does not imply Spring.

## Decisions before sectioning

- Inspect JDK/source/target and actual Maven/Gradle module contract; do not choose a JDK upgrade.
- Define checked/unchecked exception, null/collection, resource close and serializer boundaries for affected callers.
- For changed async work, name executor/request lifetime and cancellation owner; framework interception is inspected in its own adapter.

## Handoff and smallest useful evidence

Use the real exported/entry code with direct callers; test resource/error behavior and build the affected modules. Add Spring only for source-proven Spring paths.

## Scope boundary

No blanket virtual-thread migration, repository-wide DTO generation, event bus, CQRS or framework selection. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Dev.java exceptions](https://dev.java/learn/exceptions/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
