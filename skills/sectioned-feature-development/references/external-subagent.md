# external-subagent MCP adapter

Protocol authority is the installed external-subagent skill (`$external-subagent`) plus its live MCP tool descriptions: spawn fields and admission (model, effort, write_manifest), the full lifecycle (spawn/wait/respond/result/close), and observation payloads. This project keeps no second copy. On any spawn, transport or contract doubt, re-read the installed external-subagent skill (`$external-subagent`) or the live tool descriptions instead of improvising; if the skill is absent, the live tool descriptions alone govern.

## SFD client discipline

Do not pre-check the daemon every session: the pinned routes either run or fail loudly. Inspect tools/list and status only after an observed spawn/transport failure, restart or contract change; a documented interface is not evidence that an installed daemon runs that code. This skill is a client, not a daemon installer or second lifecycle manager.

The embedded dispatch profile names one spawn profile per external route; copy the literal `profile=` call and never send subagent, model, effort or permission_mode alongside it — the preset fixes those plus the role's developer instructions. Reviewer jobs never request a nonempty write_manifest; an implementation manifest, only where its route carries one, stays task-bounded to owned write paths. A permission mode or manifest label alone does not prove read-only isolation; reviewer no-write behavior comes from the role instructions and returned evidence, not the mode label. A TASK path boundary is not sandbox enforcement. Terminal-session continuity for a reviewer (same_session=false, the plugin’s terminal-round gap reason) follows the plugin contract.

If a route's exact configuration cannot be established, report MODEL_CONFIGURATION_UNVERIFIED or a capability block before dispatch — never a silent default or invented `model:effort` syntax.

## Named spawn profiles

Each external route names an SFD-owned spawn preset (`sfd-*.json`) that the installer keeps in the per-user profiles directory external-subagent owns; `external-subagent profile list` reports the exact path in use and `profile show <name>` prints one preset. The preset carries the route's subagent, model, effort, permission mode and the role's developer instructions — the same standing role law the corresponding native agent definition carries — while the spawn prompt stays the bounded TASK; do not duplicate the role law into the prompt. If the named profile is missing from `profile list`, the route is a capability blocker: report it and reinstall SFD; never inline-substitute route fields or invent a preset. SFD writes only `sfd-*.json` files there; other files in that directory are not SFD's.
