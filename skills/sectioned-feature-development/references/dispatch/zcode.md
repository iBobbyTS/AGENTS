# ZCode dispatch profile

Use `@subagent_name` for native rows. A route substitution at call time follows the substitution rule in model-routing.md.

| Logical role | Routing type | Subagent |
|---|---|---|
| code explore | native | @Explore |
| impl_std | native | @impl_std (if user requested an override, @impl_std can still be used as the fallback) |
| impl_large | [@external-subagent](plugin://external-subagent@inline) | `external_subagent_spawn(profile="sfd-codex-impl-large")` |
| PLAN review A | native | @plan_review |
| PLAN review B | [@external-subagent](plugin://external-subagent@inline) | `external_subagent_spawn(profile="sfd-codex-plan-review")` |
| code review A | native | @code_review |
| code review B | [@external-subagent](plugin://external-subagent@inline) | `external_subagent_spawn(profile="sfd-codex-code-review")` |

Each external row is a literal call: copy it verbatim and add repository and prompt. The named profile — installed by the SFD installer into the per-user external-subagent profiles directory — fixes that route's subagent, model, effort, permission mode and the role's developer instructions; never send those fields alongside `profile`. If `external-subagent profile list` lacks the named profile, the route is a capability blocker: report it and reinstall, never inline-substitute. No route in this profile takes a write_manifest. A prompt boundary is not sandbox enforcement. If hard path restriction is required, block rather than imply that yolo is read-only or silently weaken it. The callable in ZCode is `mcp__plugin_external-subagent_external_subagent__external_subagent_spawn`.

Use built-in @Explore, never shadow it. @impl_std is this host's write-capable native implementation role; the TASK's owned write paths are prompt constraints, and ZCode subagent tool access is not sandbox enforcement. Custom @impl_std, @plan_review and @code_review have injectAgentsMd=false and self-contained prompts; they do not inherit main's reasoning. Use the actual ZCode invocation mechanism and completed result, not invented Codex event names. On plugin-contract doubt re-read [external-subagent.md](../external-subagent.md) and the installed `$external-subagent` skill.
