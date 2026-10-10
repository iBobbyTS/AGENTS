# Efficiency checkpoints

Main judges its own scheduling and process efficiency at four fixed points, records one line per point in the FEATURE-STATE efficiency log, and reports the log with the completion handoff. This is self-observation, not a deliverable: no scripts, schemas, ZIP or extra model calls, and it never opens or closes a barrier.

## The four checkpoints

1. **Baseline — once, after both PLAN coverages close and before S01 dispatch.** Record the expected shape: section count and granularity, the implementation tier chosen per section, planned serial/parallel order, and expected review rounds per section. Later checkpoints judge waste against this line; revise it only at a real milestone, with the reason recorded.
2. **Per-section — at each section acceptance.** Compare actual dispatches against the plan: physical attempts versus planned (failed, retried or cancelled calls), repair waves used, reviewer signal-to-noise from the ledger's per-round admitted / rejected / duplicate counts, and whether exploration results were actually consumed. Where waste occurred, record what it was and the concrete adjustment — apply the streak-based silent-slot retirement as soon as it triggers, change tier, merge sections, parallelize.
3. **Anomaly — immediately on trigger, not at a scheduled point.** Triggers: a PLAN's second material repair wave or its budget-stop diagnosis, a parent's third repair wave (over half the five-wave budget), the second occurrence of the same root-cause family, or a second failed/retried dispatch of the same task. Name the layer — decomposition, routing, serialization or duplicated review — and record the adjustment taken.
4. **Closeout — once, after integration and before archiving.** Summarize totals: physical dispatches versus logical rounds, whether planned parallelism was actually used, admitted-versus-rejected finding totals across the run, and the waste points by layer. Report this summary with the completion handoff.

## Record and report

The efficiency log is one field in FEATURE-STATE: a line per checkpoint (checkpoint, observation, adjustment), appended at the checkpoint itself, never reconstructed afterwards. It archives with FEATURE-STATE and has no separate lifecycle. The per-round admitted / rejected / duplicate counts live in the review ledger and are referenced, not duplicated, here.

Never rerun a check, dispatch a model call or delay product work to fill the log; missing data is recorded as unknown. The log observes the process — it does not change admission, coverage or repair budgets. Cross-feature process retrospective belongs to general-audit.
