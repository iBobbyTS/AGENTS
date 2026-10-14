# C#

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed C# logic or .NET-facing public types.

Do not select merely because the feature is web, desktop or a game; those are independent domain choices.

## Decisions before sectioning

- Confirm target framework/language level and nullable annotations in real consumers.
- Name Task ownership, CancellationToken propagation, exception observation and disposable resource lifetime.
- Trace async return versus fire-and-forget effects and actual serialized enum/nullable/date/numeric fields.

## Handoff and smallest useful evidence

Exercise the actual public API and cancellation/error trajectory if changed; use an affected target/framework configuration, not every .NET runtime.

## Scope boundary

No DI container change, blanket async rewrite or ASP.NET/Unity assumption. No route creates a product requirement, extra review or new test framework.

## Sources and status

[C# asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
