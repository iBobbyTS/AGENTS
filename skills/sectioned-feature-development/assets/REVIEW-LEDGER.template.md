# `<ID>` Review Ledger

## Scope and identities

- Feature ID:
- Section base:
- Current head:
- Contract:
- Original section lineage:
- Main/orchestrator task/session ID:
- Live reviewer(s) in flight (slot, candidate head; cleared on terminal result):
- Plan reviewer task/session ID:
- Implementer task/session ID:
- Repairer task/session ID(s):
- Coverage slot reviewer task/session IDs (actual routes):
- Closing-round (Clean B) reviewer task/session ID:
- Planned provider / actual native-or-external dispatch tool and raw ID / override authority:
- Role-separation check: `pass | fail | unknown`
- Sequence-barrier check: `pass | violation-recorded | unknown`; actual result/admission before successor dispatch:
- Frozen reviewed product/test head:
- Allowed-to-edit owners/files/symbols/routes:
- Inspect-only dependency paths/direct impact cone:
- Explicitly excluded owners/mechanisms:
- Supported environment/non-goals:
- Cumulative repair waves used:
- Automatic recovery used:
- Review intensity:
- Exact product/test head covered by evidence:

## Initial bounded coverage

- Reviewer task/session ID and mode:
- Range:
- Changed files/symbols reviewed:
- Critical changed paths traced:
- Contracts/invariants reviewed:
- Risk lenses triggered:
- Checks/experiments:
- Explicit gaps:
- Causal inspection expansions beyond named cone:
- Round counts: findings admitted / rejected (non-blocking) / duplicate (cross-validated): N / M / K

## Findings

| ID | Class | Family | Severity | Causality/path | Trigger | Authority / AC ID | Consequence | Allowed repair owner | Smallest bounded repair | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| REV-001 | DIFF_CAUSED |  | Must Fix |  |  |  |  |  |  | open |

Family is the root-cause family of the clustering rule; a defect reported by both slots in one window is one cross-validated row. Every review round records its admitted / rejected (non-blocking) / duplicate counts in its own section below; these counts are the reviewer signal-to-noise input for efficiency-checkpoints.md.

## Repair waves

### Wave 1

- Origin phase: `INITIAL_BOUNDED | REPAIR_DELTA | FINAL_BOUNDED | CHECKPOINT | INTEGRATION | RECOVERY`
- Finding IDs:
- Repairer task/session ID:
- Frozen repair owners:
- Repair range:
- Targeted checks:
- Delta reviewer task/session ID and result:
- Delta counts: admitted / rejected / duplicate: N / M / K
- Coverage invalidated/re-established:

## Clean A — closure evidence

- All admitted findings closed: `yes/no`
- Required targeted/section checks pass: `yes/no`
- Remaining evidence gaps:

## Closing round (Clean B)

- Closing-round (Clean B) reviewer task/session ID and mode:
- Reviewer is distinct from plan reviewer, writers, and all earlier reviewers: `yes/no/unknown`
- Range / frozen head:
- Highest-risk changed path:
- Result: `clean | findings | insufficient-evidence`
- New admissible findings, if any:
- Closing counts: admitted / rejected / duplicate: N / M / K
- Scope/mechanism drift check:

## Silent-slot retirement

- Retired slot and its two clean round references:
- Replacement closing coverage (productive slot's final-boundary clean):

## Clean evidence and acceptance

- Required evidence under `two clean rounds`:
- Clean reviewer outcome(s) satisfied: `yes/no`
- Clean B satisfied: `yes/no`
- Section status: `ACCEPTED | NOT_ACCEPTED | BLOCKED`
- Residual risk:

## Non-blocking notes

- PREEXISTING_OUT_OF_SCOPE:
- SCOPE_PROPOSAL:
- DEFERRED_OWNER:
- NIT_DEBT:
