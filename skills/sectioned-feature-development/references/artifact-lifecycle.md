# Artifact lifecycle

## One authority per concern

Main owns requirements, PLAN-FULL and readable FEATURE-STATE; real actors, tests and reviewer results justify acceptance. No STATE.json, scheduler registry, approval digest or machine gate.

```text
.agent-work/REQUIREMENTS.md
.agent-work/PLAN-FULL.md
.agent-work/FEATURE-STATE.md
.agent-work/sections/S01-TASK.md
.agent-work/sections/S01-HANDOFF.md
.agent-work/reviews/PLAN-REVIEW.md
.agent-work/reviews/S01-REVIEW.md
```

PLAN ([template](../assets/PLAN.template.md)) and section contract ([template](../assets/SECTION-CONTRACT.template.md)) extracts are disposable views of PLAN-FULL, not independently maintained authorities. One parent task/handoff/ledger carries its children's checkpoints. Record actual actor IDs and evidence references once, not a new hierarchy for each child.

## Bootstrap and planning

Read the embedded dispatch profile in [model-routing.md](model-routing.md) first — the only execution route on this host; a role it cannot invoke is a capability blocker, not a substitution. Target/home/version live in `installation.json`.

Read [efficiency-checkpoints.md](efficiency-checkpoints.md) once at entry; feature/run scope and the efficiency log live in FEATURE-STATE. Preserve unrelated work and exclude .agent-work locally; already tracked workflow files need a separate index-cleanup decision. Save confirmed requirements, original examples and superseded corrections. Native agents receive self-contained role prompts and curated task constraints, not AGENTS.md inheritance.

Write a complete PLAN-FULL with outcomes, non-goals, current owners, dependencies, write scope, logical implementation tiers with task-based reasons, profile-resolved routes and checks. Read planning/router.md and matching guides; integrate concrete boundary examples and named consumer ownership into this same plan. Basic validation checks IDs/dependencies/tiers only. Automatic activation pauses for first-plan approval; explicit execution skips only that pause. All SFD plans record EXECUTE_WITH_COMMIT. PLAN_HANDOFF / REVIEW_ONLY are task intents, not alternative execution modes and do not themselves authorize product writes or commits.

## Review and dispatch

For each executable unit, verify the dispatch handoff in this order and record the conclusion at real transitions, not at every poll:

1. **PLAN is closed for execution:** every selected PLAN pass has returned, its report is read/saved, ordinary corrections are finished and any required PLAN_DELTA is complete — both independent coverage slots ([reviewer-orchestration.md](reviewer-orchestration.md)) valid on the final executable plan. "User approved", "review submitted", a still-running reviewer or an early CLEAN comment cannot authorize S01. Ordinary plan corrections need no matching-hash approval; material changes revalidate only affected coverage. Do not spawn an idle implementer early; that is already an implementation dispatch.
2. **The actual prerequisite is closed:** in serial execution the current parent is accepted under both clean rounds and required checks, and dependents additionally require its integration; within one parent the previous child must be CHECKPOINT_VERIFIED with no open admitted checkpoint defect. Merely completed code, an INITIAL clean, BLOCKED/ABANDONED state or a cancelled reviewer does not release a dependency.
3. **The right actor is used:** the planned profile-resolved impl route for writing, reviewers through the profile's declared route. Log route + returned ID, not a guessed identity.
4. **No conflicting actor is live:** current-candidate review prohibits a writer; independent parents overlap only under [parallel-execution.md](parallel-execution.md) limits. If a prerequisite reviewer is live, wait on it; if it failed without usable evidence, apply the bounded retry/block policy, not fake acceptance.

Example handoff: "PLAN result read and admitted; S01 accepted at <head>, integrated at <head>; no conflicting actor; dispatch S02 to its planned profile-resolved impl." During review: "S01 closing-round reviewer <route/id> still running; next action is wait, not S02 implementation."

A review report is an observation; only main admission plus required coverage/checks closes a boundary. A current-unit repair is a permitted writer handoff only after the originating reviewer has returned and main has frozen admitted findings; it does not require current-parent acceptance and does not authorize work on the next parent.

Main does not implement or repair product/test code. Main makes the narrow implementation/repair commit from the worker's finished patch after checks, without editing the patch itself; this is mechanical Git work. Never ask a worker to escape its sandbox to commit.

Freeze product/test head before review. No conflicting writer remains live. Main admits only bounded material findings; writers repair the admitted scope, and reviewers verify deltas. Both independent clean coverages must cover the final candidate ([reviewer-orchestration.md](reviewer-orchestration.md)). Children are checkpoints, not independent two-round acceptance nodes. Follow the original five-wave parent repair lineage; an actor failure does not replenish it. Evidence unaffected by a repair is reused. Keep safe intermediate states and explicit independent-parent parallel permissions.

## Completion and archive

Once required implementation commits, checks, both clean rounds and integration are complete, stop/close all owned actors and mark PLAN-FULL COMPLETED with final product head, integration outcome and remaining limitations. Do not finish while a requested subagent is still working: wait or cancel per host rules. Complete/blocked status reflects real results, not desired metadata; Advisor-triggered work stays stopped until external result plus human adoption. Do not claim completion for blocked work, a plan-only handoff, a pending required reviewer or an uncommitted implementation.

Archiving is part of this skill's own completion flow, not an optional extra: it runs at product completion. Create one timestamped directory and consolidate lasting decisions and completion references into PLAN-FULL before the move:

```text
.agent-work/archive/{YYYYMMDD-HHMM_feature-id}/
```

Move into it:

- the completed `PLAN-FULL.md`;
- real evidence that cannot be rebuilt from PLAN-FULL: original `REQUIREMENTS.md`, final `FEATURE-STATE.md` (including the efficiency log), reviewer reports under `reviews/`, worker HANDOFF files.

Delete the rebuildable dispatch views generated during the run: `PLAN.md`, section PLAN/CONTRACT extracts, and the TASK/review request packets split out of PLAN-FULL for subagents. They are derived views, not evidence.

Before any move or deletion, make a read-only inventory (path, kind, bytes, task, references). This skill's completion instruction authorizes this archive step and the removal of only its owned, unreferenced generated views. Do not recursively move/delete the whole task tree, delete live references, touch unrelated files, or remove an existing archive. Use the optional archive_plan.py helper with explicit keep/view paths and --apply; it defaults to inventory-only. A task with unresolved live references remains a cleanup blocker, not a reason to delete those references.

Leave a small current-state pointer to the archive; it is not another plan. Later requests may read archived PLAN-FULL for context but are assessed as new work unless the user explicitly requests reopening. Never append new work to a completed archived plan silently.
