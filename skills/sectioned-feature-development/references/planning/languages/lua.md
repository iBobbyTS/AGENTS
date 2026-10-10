# Lua

Axis: `language`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

Changed Lua code or a Lua embedding boundary.

Do not select merely because a game engine includes Lua internally; inspect version and host APIs (including LuaJIT/Luau differences).

## Decisions before sectioning

- Identify number/integer behavior, table identity/indexing and nil semantics actually relied upon.
- Name coroutine/host callback lifetime, registry references and error propagation across the embedding API.
- Define ownership and yield/close behavior for host resources rather than assuming garbage collection closes everything in time.

## Handoff and smallest useful evidence

Run the real host or its existing fixture with representative table/argument values and one error/yield lifecycle example.

## Scope boundary

No engine rewrite, universal sandbox promise, Lua version migration or automatic game-domain assumption. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Lua 5.4 manual](https://www.lua.org/manual/5.4/manual.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
