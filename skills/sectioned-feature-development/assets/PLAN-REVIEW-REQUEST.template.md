# PLAN review request

Review `{plan path}` at `{candidate reference}` against `{original requirements and repository constraints}`.

- Scope / exclusions: `{business outcome, owners, supported environment}`.
- Evidence: `{source base, selected boundary examples, relevant guide links}`. Inspect source to falsify suspected defects; do not reread all catalogs or prescribe new requirements.
- For a delta only: `{previous candidate → current, admitted IDs, changed owners and invalidated conclusions}`. Do not reopen unchanged scope.
- Report: write the full review to `{dispatched report path}` (your only writable `.agent-work` location) — signal, candidate reference, covered boundaries, gaps and batched root causes; separate PLAN_BLOCKER / OWNER_DECISION from PLAN_SCOPE_EXPANSION / PLAN_NIT; do not invent private helper names as requirements. Final answer: signal, report path and one-line status.

State missing evidence rather than manufacturing a completed check.
