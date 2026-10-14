# FastAPI

Axis: `adapter/framework`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed FastAPI route/dependency/serialization or lifespan behavior.

Do not select merely because Python, ASGI or Pydantic exists elsewhere; inspect actual route and dependency graph.

## Decisions before sectioning

- Trace actual input model, dependency-provided identity/resource and response encoding.
- Separate framework-managed sync work from awaited async calls and blocking work inside them.
- Name startup/shutdown and request dependency lifetime; background work returning success is not evidence it completed.

## Handoff and smallest useful evidence

Use real ASGI/route clients and activated resource/error paths with existing fixtures; verify actual payload models, not a lookalike dict.

## Scope boundary

No async rewrite, task queue, new validation package or unrestricted request strictness. No route creates a product requirement, extra review or new test framework.

## Sources and status

[FastAPI async](https://fastapi.tiangolo.com/async/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
