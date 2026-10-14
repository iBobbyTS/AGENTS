# Python

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Python application, library, CLI or job source.

Do not select merely because an unrelated script exists, or the host runs Python; .py does not imply Django, FastAPI, asyncio or free-threading.

## Decisions before sectioning

- Inspect pyproject, environment/interpreter, import/config lifetime and installed entry points.
- Identify canonical normalization for bool/number, missing/null, finite/large values and time/units only where changed.
- For asyncio, trace task cancellation and blocking boundaries; for resource contexts, distinguish cleanup from business rollback.

## Handoff and smallest useful evidence

Keep command/service/result within one parent; hand consumers the same fixture. Test actual imports/entry points, and installed artifact outside source tree only when packaging changes. One-off correction scripts do not imply a migration platform.

## Scope boundary

No new DI/validation framework, event loop, global lock, hostile same-process model or duplicated route/raw-loader predicates. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Python asyncio tasks](https://docs.python.org/3/library/asyncio-task.html); [Python packaging pyproject](https://packaging.python.org/en/latest/guides/writing-pyproject-toml/). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
