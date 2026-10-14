# Games / real-time interactive media

Axis: `domain`. Use only for the changed path; repository versions and confirmed authority govern.

## Match and exclusions

The feature changes gameplay, simulation/render timing, entity lifecycle or interactive media behavior.

Do not select merely because C#/C++/Lua exists; engine and language are separate.

## Decisions before sectioning

- Name frame/update/physics/audio clocks, authoritative entity state and resource/scene lifetime.
- Separate simulation outcome from visual interpolation/input feedback and persistence/network authority if affected.
- Define a reproducible scene/input trajectory and concrete frame/memory budget only when requested or causally at risk.

## Handoff and smallest useful evidence

Use the actual scene/engine pipeline and representative input/load; do not infer correctness from an isolated math helper or frame screenshot alone.

## Scope boundary

No engine rewrite, netcode/rollback system, ECS migration or performance campaign without requirement authority. No route creates a product requirement, extra review or new test framework.

## Sources and status

[Godot idle/physics processing](https://docs.godotengine.org/en/stable/tutorials/scripting/idle_and_physics_processing.html). Underlying mechanisms are source-based; these planning questions/examples are engineering synthesis, not measured outcomes.
