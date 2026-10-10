# PLAN review request

Review `{plan path}` at `{candidate reference}` against `{original requirements and repository constraints}`.

- Scope / exclusions: `{business outcome, owners, supported environment}`.
- Evidence: `{source base, selected boundary examples, relevant guide links}`. Inspect source to falsify suspected defects; do not reread all catalogs or prescribe new requirements.
- For a delta only: `{previous candidate → current, admitted IDs, changed owners and invalidated conclusions}`. Do not reopen unchanged scope.
- Return: `CLEAN | MATERIAL_CANDIDATES | INSUFFICIENT_EVIDENCE`, candidate reference, covered boundaries, gaps and batched root causes. Separate PLAN_BLOCKER / OWNER_DECISION from PLAN_SCOPE_EXPANSION / PLAN_NIT. Do not invent private helper names as requirements.

State missing evidence rather than manufacturing a completed check.
