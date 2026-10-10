# Codex dispatch profile

| Logical role | Routing type | Subagent |
|---|---|---|
| code explore | native | [@code_explorer](subagent://code_explorer) |
| impl_std | [@External Subagent](plugin://external-subagent@personal) | `external_subagent_spawn(profile="sfd-dsh-impl-std")` |
| impl_large | native | [@impl_large](subagent://impl_large) |
| PLAN review (native) | native | [@plan_reviewer](subagent://plan_reviewer) |
| PLAN review (external) | [@External Subagent](plugin://external-subagent@personal) | `external_subagent_spawn(profile="sfd-zcode-plan-review")` |
| code review (native) | native | [@code_reviewer](subagent://code_reviewer) |
| code review (external) | [@External Subagent](plugin://external-subagent@personal) | `external_subagent_spawn(profile="sfd-zcode-code-review")` |

Each external row is a literal call: copy it verbatim, adding only `repository`, `prompt` and the task-bounded `write_manifest` where its route carries one. The named profile — installed by the SFD installer into the per-user external-subagent profiles directory — fixes that route's subagent, model, effort, permission mode and the role's developer instructions; never send those fields alongside `profile`. If `external-subagent profile list` lacks the named profile, the route is a capability blocker: report it and reinstall, never inline-substitute. Main invokes the actual native API for native roles and the external_subagent_* tools directly for external roles; native reviewers are not forwarding wrappers. A native barrier closes only on the actual FINAL_ANSWER event with completed status; progress or early text never opens one. Use fresh native contexts (do not fork parent history), and include only applicable bounded repository constraints in the TASK — never paste AGENTS.md or tell the worker to reload it; configuration is not proof of runtime isolation, so report missing isolation instead of silently claiming it. Do not relabel runtime failures as tier inadequacy. On any external spawn failure or plugin-contract doubt, re-read [external-subagent.md](../external-subagent.md) and the installed `$external-subagent` skill instead of improvising.
