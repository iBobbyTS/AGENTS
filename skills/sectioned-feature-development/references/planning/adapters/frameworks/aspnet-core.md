# ASP.NET Core

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed ASP.NET Core endpoint, middleware, DI service or background lifecycle.

Do not select merely because C# source exists; .NET desktop/game/library code is not ASP.NET.

## Decisions before sectioning

- Trace middleware/auth→bound input→service→serialized result and the configured error envelope.
- Identify singleton/scoped/transient resource lifetime and request cancellation ownership.
- For background tasks do not capture request-scoped services beyond their lifetime without the project's existing scope mechanism.

## Handoff and smallest useful evidence

Use actual host/endpoint integration and scoped disposal/cancellation case where changed; re-use existing test host.

## Scope boundary

No DI replacement, architecture layering campaign, host rewrite or new scheduler. No route creates a product requirement, extra review or new test framework.

## Sources and status

[ASP.NET Core DI](https://learn.microsoft.com/en-us/aspnet/core/fundamentals/dependency-injection); [C# asynchronous programming](https://learn.microsoft.com/en-us/dotnet/csharp/asynchronous-programming/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
