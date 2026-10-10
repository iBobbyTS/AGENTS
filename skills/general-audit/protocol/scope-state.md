# Scope, completion and continuity

## Scope selection

Baseline maps the current system before choosing deep questions; it need not review every line. Routine combines changed causal boundaries, critical outcomes, recurring defects and a neglected area. A focused investigation can stay narrow if its limitations are explicit. Milestone connects current intent to completed integrated behavior; it is not release clearance. Followup verifies named findings rather than silently turning into baseline.

Scoping isn't delegated to a pathname matcher. Churn, directory names, recent subjects and prior reports are hints. Inspect the actual owners and a small counter-sample. For missing/non-ancestor baselines, say the historical delta is uncertain and inspect the present system; don't use a conveniently chosen range as the actual last-audit range.

Keep some exploration outside changed code for baseline/routine/milestone. Rotate **questions and behavior paths**, not alphabetical files. If urgent work displaces this, preserve the debt. Age alone does not prove a defect, but repeated postponement must remain visible.

## State has one owner

Reuse existing compatible records. Otherwise keep `STATE.md` and per-run reports in `.agent-work/general-audit/`. State summarizes pointers, not a second full finding database. General-audit writes coverage and finding dispositions. Steward owns only recommendation/suppression state; preflight owns release-specific evidence and its profile. Never let either imply audit closure.

The state needs:
- last broad scoped run: ID, actual snapshot, date, mode and limits;
- latest targeted runs separately, linked to affected questions;
- scenario coverage with depth, evidence and invalidation assumptions;
- open finding/risk decisions with authority/revisit condition;
- neglected area/next rotation and any displaced objective.

An optional `collection_base` names a real revision used to collect changes, **not full-system coverage**. Keep it distinct from broad-audit completion. A completed focused run can resolve a scenario, but cannot reset last broad audit or erase other changes since it. Partial work adds evidence without advancing completion markers. A user-accepted risk remains visible until its accepted condition or scope changes; the agent cannot accept it itself.

For a legacy `Maintenance-Audit: true` hook, don't emit it if it would falsely reset the user's broad reminder after a tiny followup. Explain the mismatch and propose an explicit mapping separately. Do not modify hooks during an audit.

## Concurrent work and evidence reuse

Record target/environment before and after relevant probes. If changes occurred, invalidate the dependent conclusions, not every untouched check. Do not freeze the user's project by force or overwrite another run's state. On conflict, retain your uniquely named report and reconcile the shared summary; a report saved alone is better than lost evidence.

A report may be completed with open findings. Essential promised checks missing are partial even if no defect was found. Finding status and run status are separate axes. No percentages of overall safety, no N-clean termination, no silent erasure of failed/skipped evidence.
