# Subsections — implementation granularity, not acceptance multiplication

## Contents
1. [Two levels](#two-levels)
2. [When to decompose](#when-to-decompose)
3. [Plan contract](#plan-contract)
4. [Checkpoint execution and review](#checkpoint-execution-and-review)
5. [Parent acceptance](#parent-acceptance)
6. [Budget and change control](#budget-and-change-control)
7. [Git, scheduling and continuity](#git-scheduling-and-continuity)
8. [Migration and checkpoints](#migration-and-checkpoints)

## Two levels

A **section** is the externally consumed acceptance/integration boundary: one approved behavior contract, shared invariants, assurance, original repair lineage and downstream dependency identity.

A **subsection** is a bounded product implementation plus its tests and scoped review checkpoint **inside** that boundary. It can introduce a real internal helper/domain before the public adapter, provided the parent names its concrete consumer and the intermediate code is safe. It is not independently releaseable/accepted and does not unlock another section.

An ordinary work step (write cases, implement a rule, run tests) does not need a subsection. A row in a case matrix is not automatically a subsection. A dotted historical ID is not a hierarchy: `S04.1.2` remains a section if it was accepted as one. Explicit metadata, not punctuation, defines parenthood.

Maximum nesting: section → subsection. No sub-subsections, independent child PLAN gates, child assurance choices, new child repair budgets or recursively recreated recovery lineages.

## When to decompose

Use subsections prospectively when all three hold:
- the parent contains at least two distinguishable **real product increments** or different reasoning loads;
- an earlier increment can be meaningfully exercised/reviewed before expensive dependent code is written;
- a shared external contract, state machine, transaction or final consumer still requires one joint acceptance.

Examples: simulation primitives→event composition; exact representation/identity→atomic producer transaction; analysis candidate→frozen publication/delivery; worker/current-state→historical reconstruction. Two or three checkpoints are often enough, but this is not a quota.

Keep an atomic section when dividing it would separate two sides of the same rule, create a duplicate validator/parser/state owner, require a fake success path, or save no meaningful context. Status×body-failure priority is one matrix; splitting “timeout” from “non-2xx” does not establish two independent contracts. Validator and extractor must consume the same parsed representation, not become independently approved owners.

Split boundaries follow **invariant bundles**, not module charts. An invariant bundle is a set of cross-state invariants whose violations are visible only in combination — each path alone stays green; dividing through a bundle severs it and every later repair pays for the cut. Independently falsifiable invariants (a command family where every path is testable alone) may be re-divided freely. This is the same visibility test that selects impl_large in [model-routing.md](model-routing.md): what cannot be split cannot be demoted either. Coarser children on a higher tier are not a defect; granularity itself is not the quality variable.

Use a separate full section instead if another section must depend on an increment early, or it truly has an independent product/release/ownership contract. Do not export an unaccepted child by bypassing the parent gate.

LOC is diagnostic, never a stop/split/compact-code trigger. A known larger but coherent increment is allowed. New dependencies or inseparable rule interactions, not crossing 300/650/700 lines, justify revisiting granularity.

## Plan contract

Keep the existing `sections` DAG. Only decomposed parents add `delivery_mode=SUBSECTIONS`, explicit `lineage_id`, `shared_invariants`, `joint_oracles`, and a serial ordered `subsections` list. Each child supplies ID/parent, scope subset, concrete outcome, planned consumer, safe intermediate state, same-parent predecessors, model, check IDs and its scoped oracle.

The parent retains original requirements, resource limits, exemptions, write envelope, consumers, assurance and budget. No child may weaken these or create an unsupported guarantee. Child tests are written beside the changed behavior; don't create an evidence-only product node or a framework to make the schedule prettier.

Model profiles may differ only at meaningful interfaces. A cost-motivated split is legitimate exactly when the interface it splits on already carries an independently falsifiable oracle before implementation starts — a frozen cross table (input × state × outcome), a frozen fixture set (input frame → expected event/output sequence), or a pattern precedent frozen from a prior accepted unit. A bare signature or type declaration is not a freeze. An interface that only slices the task, with no oracle of its own, is manufacturing regardless of the stated motive. The parent review sees the complete shared contract from the first checkpoint, including which behavior is intentionally not implemented yet.

Three ordering rules keep the children honest. (1) **Producer-first**: when children form a framework→family shape, the producer child is implemented and checkpoint-verified first, and each consumer packet carries the producer's actual exported surface as returned — never the planned signature ([boundary-handoff](planning/boundary-handoff.md)). (2) **Deferral is a cross-child contract**: every deferred-to-later item appears as an explicit contract line in the receiving unit's packet and is owned by that unit's acceptance; a “breaks unless re-homed” cross-unit dependency must enter the receiver's acceptance criteria or be repaired now — residence in a NIT ledger is not closure. (3) **An acceptance harness that is itself a deliverable** (an environment/driver-mode script, a probe suite) and shares no invariant with surrounding retirement work is its own bounded unit, not an ingredient of a closing “everything else” section.

## Checkpoint execution and review

1. Reserve **one parent-slot full review** at the first checkpoint; its scope is incrementally inspected, not yet CLEAN for the parent. Resolve that provider from the embedded dispatch profile; the embedded profile supplies the two independent slots, not a provider alternation counter.
2. Implement one child on the existing parent worktree/branch; add targeted behavior tests and make a coherent commit. Don't announce the still-incomplete public feature as supported.
3. Freeze the checkpoint SHA. Send `SUBSECTION_DELTA` under `DELEGATED_PASS` to the parent-slot reviewer: predecessor reviewed head→candidate, child scope, parent invariants, pending behaviors, exact checks. New construction is reviewed, not only repair code; “delta” refers to range, not reduced rigor.
4. Wait for the actual checkpoint reviewer result before main admission. Repair and verify on that reviewer, with the **shared parent lineage**. No next same-parent child, even if otherwise independent, while a checkpoint reviewer/delta is live, a finding is admitted and open, or an invariant is invalidated. Stop/cancel is not CHECKPOINT_VERIFIED.
5. Record `CHECKPOINT_VERIFIED` with base/head, checks and review artifact; not `ACCEPTED`. Continue the next child. Do not create another PLAN.md/state/report hierarchy; one current task packet and one parent ledger are enough.
6. If a later change invalidates earlier code, record the exact prior checkpoint/paths/invariant, review that delta and rerun affected joint cases. Do not reopen all historical lines or clear old evidence because of a new child number.

One parent-slot reviewer session is preferred across children, preserving coverage. Where provider/harness cannot resume a terminal session, use the existing explicit same-provider delta-with-gap policy or stop under strict continuity. Different actual agents are never falsely reported as one session. Every real invocation, including checkpoint reviews, counts in cost telemetry even when it does not advance the full-pass index.

## Parent acceptance

After the last child, the parent-slot reviewer performs **PARENT_RECONCILIATION** on the final parent candidate: reconcile cumulative diff coverage, all admitted closures, intentionally deferred behavior, cross-child interactions, real consumer and the complete parent invariant/oracle matrix. This is completion of the parent-slot pass, not another automatic full rediscovery pass.

A set of locally green child tests is insufficient. Parent-specific joint oracles execute on the final candidate (or demonstrably identical relevant input/environment); parent-slot coverage must explicitly account for every child and any later invalidation. If evidence cannot establish cumulative coverage, conduct the missing bounded review; do not label it clean from a checklist.

Parent acceptance always closes with the independent coverage pair ([reviewer-orchestration.md](reviewer-orchestration.md)): complete parent-slot reconciliation establishes Clean A; the profile's independent closing round on the final parent candidate supplies Clean B.

- That closing reviewer sees original parent base→final diff, the whole contract and joint evidence; it is distinct from all writers and parent-slot instances, and need not trust checkpoint narratives.
- Slot validity, invalidation and silent-slot retirement follow [reviewer-orchestration.md](reviewer-orchestration.md).

No closing pair per child. Closing-round findings return to that reviewer for bounded delta closure and consume the same parent repair budget. Parent acceptance/integration is the only event that unblocks external dependents.

## Budget and change control

Count **attempted admitted repair waves**, not successful closure only. All child checkpoint, parent reconciliation and closing-pair repairs share the original parent lineage's five ordinary waves. A compatible batch may contain multiple finding IDs, but retries after failed closure remain attempts and count. Initial implementation refinement before independent/admitted finding is logged but is not retroactively counted as repair.

Adding/reordering a child, changing a model, a new run, parent rename or provider fallback never replenishes the budget; recovery cannot reset a child budget. A child/model/run change grants no additional wave. Bounded recovery allows one named extra attempt after a non-structural diagnosis, or a genuinely replaced acceptance boundary under one structural recovery. Record the original lineage and recovery_used; a new child is never a replacement boundary. A replacement that exhausts its inherited recovery allowance reaches the external Advisor, not another automatic reset. See recovery-and-migration.md.

When only internal remaining decomposition changes, preserve existing implementation and review evidence; freeze at a safe boundary and obtain one bounded PLAN delta if interfaces/acceptance/dependencies change. No full PLAN re-review merely because a child list grew. An already completed feature stays closed under the existing follow-up rule.

## Git, scheduling and continuity

One parent branch/worktree by default; serial children, no concurrent sibling child writers in the current workflow. Independent **parents** may still run in isolated worktrees under the existing path/contract/resource checks. Parent write/resource reservations remain conservative throughout; don't release a shared Cargo.lock reservation merely because child1 finished without an approved scope revision.

EXECUTE_WITH_COMMIT covers every unit, including one atomic parent or one child; SKILL.md owns the branch authority. Partial child commits stay on the parent branch until parent acceptance unless a separately approved independent section is extracted.

Main chooses the next serial child from the readable plan and actual checkpoint results, then verifies Git, tests and real actors. There is no next-unit or acceptance-check CLI. Structural validation only catches malformed IDs/dependencies/profiles, never verifies acceptance.

## Migration and checkpoints

The authoritative schedule is Markdown with parent/child headings, explicit logical implementation tiers and dependency IDs. Do not reinterpret accepted dotted IDs or rewrite old counters. For an active atomic section, finish its existing review/candidate boundary before adding a decomposition; never reset a live writer or require retroactive child evidence.

Parent acceptance stays distinct from checkpoint verification. Record parent/child/lineage, logical review ID, real reviewer ID, checkpoint base/head, inherited counter before/after and invalidated checkpoints in the parent ledger; the per-section efficiency checkpoint judges a decomposition against flat sections by accepted outcome, not by child pass rate.

## Profile freeze

Before PLAN review, each parent AND each child declares its own implementation profile and task-based reason. No implicit child inheritance. Model changes during execution require a bounded plan revision, unchanged original lineage, and task regeneration before dispatch. Parent repair outside a child uses the parent's explicit profile; child-scoped repair uses that child's profile.

## Checkpoint placement

Every returned implementation gets main's bounded contract/diff/test handoff check before a consumer runs. Invoke or continue the parent's primary reviewer at a consequential producer/consumer, state-machine or scope handoff, not automatically after every tool call or every same-owner repair reply. Preserve the existing SUBSECTION_DELTA/PARENT_RECONCILIATION policy; it is not a second complete A/B loop per child. Final acceptance remains parent A plus full current bounded B, and the parent repair budget does not reset on a child, new context or integration label.
