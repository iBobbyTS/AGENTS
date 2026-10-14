# Feature Integration Review Request

Review the integrated feature candidate `{feature base..head}` in `{repository}` against `{original feature acceptance criteria}` — one round of an `INTEGRATION` review proving what local section reviews could not.

- Execution target:
- No product writer/reviewer is active: `yes`
- Frozen feature product/test head:
- Feature ID / plan:
- Accepted section summary:
- Repository-required gates:
- Required end-to-end checks:
- Dispatched report path (your only writable `.agent-work` location):

Review only what local section reviews could not prove:

- original feature outcome and non-goals;
- emergent cross-section API/schema/state/permission/ordering/error behavior;
- required migration, compatibility, rollout, rollback, cleanup, and observability;
- representative end-to-end paths;
- branch-scope integrity.

Use the same classes and blocking proof as section review: admit only feature-diff-caused composition defects, a necessary merge-blocking dependency on a real feature acceptance path, or an evidence gap tied to an existing feature acceptance criterion or repository-required gate. Composition creates no authority to add stronger product/security/durability/compatibility/observability/rollout promises, routes, analyzers, governance, or browser flows; do not repeat local section review, audit unrelated repository code, or reopen an accepted section without concrete combined-behavior evidence. Write the full report to the dispatched report path; the final answer carries only the signal, that path and one line of status. A missing actual report file means INSUFFICIENT_EVIDENCE, never an implicit clean.
