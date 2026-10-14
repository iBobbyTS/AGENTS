# Recovery and Workflow Migration

## Contents

1. [What the hard cap measures](#what-the-hard-cap-measures)
2. [Hard-cap evidence packet](#hard-cap-evidence-packet)
3. [Recovery classifications](#recovery-classifications)
4. [Preservation rules](#preservation-rules)
5. [Automatic recovery limit](#automatic-recovery-limit)
6. [Adopting or activating mid-feature](#adopting-or-activating-mid-feature)
7. [Branch-base authority](#branch-base-authority)

## What the hard cap measures

The cap measures **repair waves**, not reviewer calls.

One repair wave is:

1. one or more compatible admitted root-cause classes;
2. one coherent repair;
3. targeted validation;
4. delta review closing or reopening those IDs.

Reviewer invocations, repeated comments, rejected scope proposals, plan formatting corrections, and tool retries do not count. Any admitted repair arising from initial, delta, final, checkpoint, or integration review does count toward the applicable cumulative budget.

The fifth wave is allowed to complete. The counter does not reset when entering the closing clean pair or choosing a non-structural recovery. Recovery begins only before a sixth wave or when the current wave proves the section architecture/contract cannot close locally.

## Hard-cap evidence packet

Use [HARD-CAP-DIAGNOSIS.template.md](../assets/HARD-CAP-DIAGNOSIS.template.md). Before invoking the main orchestrator (plan author), collect:

- feature outcome and non-goals;
- original section lineage and whether its one automatic recovery event is already used;
- section goal, base, head, frozen scope manifest, and direct impact cone;
- current diff summary;
- five repair waves and stable finding IDs;
- which findings were closed and what recurred;
- current open blocker;
- tests and environment gaps;
- new mechanisms introduced and their requirement anchors;
- rejected scope proposals in a non-authoritative appendix;
- current branch/worktree and backup ref.

Do not send rejected proposals intermixed with admitted requirements.

## Recovery classifications

### `CONTINUE_CURRENT`

Use when architecture/ownership is sound and one named local root cause remains. Authorize exactly one recovery repair wave against current code, then go directly to `FINAL_BOUNDED`. It does not create another general five-wave cycle.

### `SIMPLIFY_CURRENT`

Use when review-created mechanisms, stronger threat models, generalized tooling, or excessive proof infrastructure dominate. Delete/simplify unanchored mechanisms in one named recovery wave, preserve requirement-aligned fixes, then go directly to `FINAL_BOUNDED`.

### `SPLIT_REMAINING`

Use when unresolved behavior genuinely contains two independent product increments. Preserve completed correct code and split only remaining work into at most two active descendants.

### `REBOUND_OWNER`

Use when the unresolved behavior belongs to another existing owner or section. Move the responsibility and update only affected dependencies.

### `REPAIR_EVIDENCE`

Use when product behavior appears correct but one acceptance-criterion-anchored oracle/environment is broken. Fix that evidence in one named recovery wave; do not create an evidence-only descendant.

### `RESTART_FROM_BASE`

Use only when the implementation direction, state owner, or threat model is demonstrably wrong and in-place simplification would retain most of the wrong design. State:

- wrong assumptions;
- code/mechanisms to discard;
- why reversion/simplification is insufficient;
- exact restart base;
- valid fixes/evidence that can still be reused conceptually.

## Preservation rules

- Create a dedicated recovery ref such as `refs/backup/<lineage-id>` for the current state, not an active development requirement.
- Keep current correct commits by default.
- Do not require a pristine ancestry for tests/reviews.
- Do not replay accepted predecessors unless changed product code invalidated their contract.
- Do not copy rejected scope proposals into new contracts.
- Do not rewrite the full plan when only one section/dependency changes.
- Do not add a descendant solely for a test, checkpoint, review format, or provenance record.
- If all unresolved items are reviewer-created tooling, generalized oracles, or process artifacts without an exact acceptance anchor, structural recovery is forbidden; simplify/delete them or stop.

## Automatic recovery limit

One automatic hard-cap recovery event is allowed per original section lineage, regardless of classification.

- Non-structural recovery (`CONTINUE_CURRENT`, `SIMPLIFY_CURRENT`, `REPAIR_EVIDENCE`) authorizes exactly one named recovery wave followed by `FINAL_BOUNDED`. Another independent blocker stops the lineage; do not diagnose/recover again automatically.
- Structural recovery (`SPLIT_REMAINING`, `REBOUND_OWNER`, `RESTART_FROM_BASE`) may establish a genuinely new boundary with a fresh five-wave budget, but the replacement inherits `automatic_recovery_used = yes`. If it reaches another hard cap, stop rather than recursively growing `S03.1.1.1...`.

This limit prevents technical recovery from becoming a new feature graph or a hidden sequence of five-wave cycles.

## Adopting or activating mid-feature

A skill update is a workflow change, not a product change. An initially local task may also activate this workflow late when its actual owners, diff, or semantic boundary cross the trigger.

When adopting/activating mid-feature:

1. Stop product/test edits at a safe point and record `adoption_head`, changed owners, current validation, open work, and invocation timing `MID_FEATURE`.
2. Preserve correct code, accepted sections, tests, closed findings, and applicable review coverage; do not rewrite history or restart from base merely for workflow purity.
3. Resolve branch transition before continuing:
   - on `main` with uncommitted work, create/switch to the feature branch and carry the worktree changes;
   - on an unrelated non-`main` branch, ask the user to choose a base: `main`, the current branch, or `main` after an explicitly authorized merge; continuing an already authorized feature branch needs no repeat choice;
   - when feature commits already exist on local `main`, create a safety branch at current HEAD and ask before restoring/rewriting `main`.
4. Build/review a prospective plan only for active unaccepted and remaining work. If activation was automatic, stop before plan review for user approval.
5. Continue with delta review when a repair is already in progress; otherwise use one bounded full re-review if prior coverage cannot be reconstructed economically.
6. Sanitize only the active, unaccepted contract: trace every guarantee/oracle/structural allowance to user intent, repository rules, or established behavior; downgrade unanchored reviewer-authored items to `SCOPE_PROPOSAL`.
7. Add only the minimum fields needed for future continuation. Do not create migration sections, plan-review loops, legacy admission copies, evidence rehabilitation, or clean-lineage worktrees.
8. Assign distinct delegated implementer/reviewer roles for all remaining work; prior main-thread code remains valid evidence but the main agent does not continue product coding after activation.

If an old plan lacks new optional headings, note them in current state and continue. Do not run a strict validator that retroactively fails accepted work.

## Branch-base authority

In `EXECUTE_WITH_COMMIT`, creating an isolated feature branch/worktree from `main` requires no additional approval. When the current branch is not `main`, do not silently inherit it. Ask the user to choose exactly one:

1. branch from `main`;
2. branch from the current branch;
3. first merge the current branch into `main`, then branch from updated `main`.

Record the starting branch, selected base, explicit authority, and any late-adoption head in `FEATURE-STATE.md`. Preserve uncommitted work. If the repository has no clear `main` equivalent, ask rather than guessing. This branch-base choice does not authorize merge, push, cleanup, or deletion of the source branch.


## Lifetime budget projection

`waves_used` and the parent's repair count are lifetime attempt counters. Do not lower them for a child or a replacement. A genuine structural replacement records exactly one `structural_recovery` on the original lineage with classification, `boundary_changed=true`, original lineage ID, replacement parent section ID, generation, `waves_at_boundary_change`, and a hashed diagnosis/admission artifact. The new five-wave window is an offset from that lifetime counter, not a reset. A model/child change cannot create that record.

One non-structural extra attempt references one named request/decision artifact and its hash. After that (or exhaustion of the structural window), ordinary automation stops. Further action needs the external Advisor or explicit owner decision under the existing escalation policy, not a new automatically fabricated allowance. Main checks the projection against these records; no script enforces it.

## Local state continuation

Use readable FEATURE-STATE.md and real review/check references. Agent-managed scope decisions and the retained repair/recovery quotas remain binding; changing format or model never replenishes them.
