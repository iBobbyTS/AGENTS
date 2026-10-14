# Bounded code review request

Review `{BASE..HEAD}` in `{repository}` for `{business parent contract / acceptance criteria}`.

- Boundary: `{allowed owners, inspect-only impact cone, exclusions, relevant constraints}`.
- Checks already available: `{exact head/environment, results and gaps}`; do not rerun unchanged evidence solely because this is a new context.
- Scope: `{INITIAL_BOUNDED | REPAIR_DELTA | FINAL_BOUNDED}`. For REPAIR_DELTA give `{repair range, frozen finding IDs and invalidated coverage}`; inspect only that cone. For FINAL_BOUNDED inspect the complete bounded final diff and its highest-risk changed path once.
- Report: write the full review to `{dispatched report path}` (your only writable `.agent-work` location) — verdict signal, reviewed range, source evidence, covered paths, gaps and batched root causes. Final answer: signal, report path and one-line status.

Inspection outside the named cone needs a concrete causal edge; it does not authorize editing a new owner.
