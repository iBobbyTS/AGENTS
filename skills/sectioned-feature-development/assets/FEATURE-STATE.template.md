# Feature state — <feature-id>

- Status: PLANNED / HANDOFF_PENDING / EXECUTING / BLOCKED / COMPLETED
- Installed home:
- Dispatch profile (installed):
- Task intent: IMPLEMENT / PLAN_HANDOFF / REVIEW_ONLY
- Execution policy: EXECUTE_WITH_COMMIT (all SFD executions, including one unit)
- Repository / branch / feature base / current candidate / explicit base authority:
- Invocation source and first-plan approval when automatic:
- Requirements / active PLAN or archived PLAN-FULL path:
- PLAN Clean A / Clean B / actual results / admitted findings / pending delta:
- Current parent/child and logical impl tier / resolved route:
- Active actors: actual transport + raw ID + role + workspace + outstanding result:
- Main identity: runtime, native session/task ID, model/effort source or UNKNOWN:
- Subagent usage: requested and observed identities, physical attempts, logical lineage:
- Last closed prerequisite / next permissible action / explicit parallel exception:
- Parent native-side/checkpoint/reconciliation coverage, Clean A / Clean B and open finding IDs:
- Parent repair waves / recovery used / invalidated evidence:
- Accepted parent head → integrated head / implementation-repair-integration commits:
- Final checks / final head / readiness / unresolved limitations:
- Advisor hold and actual human adoption when applicable:
- Efficiency log (one line per checkpoint, per efficiency-checkpoints.md): baseline / per-section / anomaly / closeout
- Closure head/date / archived PLAN-FULL / transient-plan cleanup inventory:

Record facts at real transitions, not every poll; efficiency-log lines are appended at the checkpoints themselves, never reconstructed afterwards. COMPLETED closes product work; archive PLAN-FULL immediately and report the efficiency log with the completion handoff. A later request reads the archive as context, not an open plan or reusable CLEAN. Unknown model/identity stays UNKNOWN.
