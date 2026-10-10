# Long-horizon development — a complete roadmap, a small executable horizon

## Contents

1. [When to load this reference](#when-to-load-this-reference)
2. [Authority and scope](#authority-and-scope)
3. [Three planning scales](#three-planning-scales)
4. [Reviewable section boundaries](#reviewable-section-boundaries)
5. [Prove the production path early](#prove-the-production-path-early)
6. [Rolling detail without rolling requirements](#rolling-detail-without-rolling-requirements)
7. [Existing PLAN review, not another committee](#existing-plan-review-not-another-committee)
8. [Implementation and review packets](#implementation-and-review-packets)
9. [Composition checkpoints](#composition-checkpoints)
10. [Existing owners, tests and cross-language rewrites](#existing-owners-tests-and-cross-language-rewrites)
11. [Replanning an active program](#replanning-an-active-program)
12. [Resuming across sessions](#resuming-across-sessions)
13. [Advisor and efficiency](#advisor-and-efficiency)
14. [Counterexamples and cost limits](#counterexamples-and-cost-limits)

## When to load this reference

Default: **do not load for ordinary SFD work**. A long chat, many tokens, many files, or a single difficult repair is not sufficient.

Load when the user explicitly requests multi-session program/rewrite planning; otherwise load only when **both** are true:

1. The request replaces a substantial subsystem or creates a multi-capability product, and is expected to span several implementation sessions.
2. At least one concrete planning signal is present: roughly eight or more distinct behavior outcomes; three or more interacting production boundaries; the first useful assembled path is postponed behind several independently implemented layers; or repeated external corrections show that local completion has diverged from the original outcome.

These are routing aids, not LOC/section quotas or runtime gates. State the evidence briefly in existing PLAN. A three-section task can qualify if its sections hide three large subsystems; twelve mechanical edits need not qualify. Classify by actual work, not by the author's initial headings.

First resolve the four planning axes via [planning/index.md](planning/index.md) and use matched domain/language/adapter/concern guides as usual. This reference adds a **time-horizon lens**, not a fifth technology taxonomy and not a substitute for matching guides. Universal remains a fallback for genuinely uncovered knowledge.

## Authority and scope

Keep one feature outcome and its explicit exclusions authoritative. A milestone, test plan, reviewer or Advisor cannot add product promises. Record changes in authority and superseded requirements, not just changes in implementation.

A rewrite may be developed incrementally yet deployed by one authorized clean cutover. Long-horizon planning does **not** authorize dual writes, historical migration, backward-compatibility layers, online rollback, new service boundaries or a generic orchestration platform. Choose those only when the user/repository actually requires them.

Preserve the ordinary SFD contracts: saved artifacts, actual implementer delegation, native/external reviewer separation, review completion barriers, explicit implementation profiles, commit/branch authority, parent repair lineages, bounded scope, required checks, external human Advisor. No JSON scheduler, actor-receipt validator, approval-hash gate or extra runtime script is introduced.

## Three planning scales

Use existing PLAN-FULL, TASK, HANDOFF, REVIEW and FEATURE-STATE. Keep these scales conceptually distinct; do not create three copies of the plan.

| Scale | Contents | What it does not mean |
|---|---|---|
| Product roadmap | Original outcomes, source baseline, exclusions, complete obligation-to-section coverage, final deployment/retirement condition | A checkbox count is not overall completion |
| Outcome checkpoints | A few observable assembled journeys and the sections that make them possible | These are not implementation agents, independent repair budgets or evidence-only sections |
| Executable sections/subsections | One coherent behavior boundary with an owner, direct consumers, prerequisites, a falsifiable oracle, planned implementation role and bounded acceptance | A subsystem name is not automatically one reviewable section |

PLAN-FULL contains **all known remaining outcomes**, not only the next few tickets. Every listed section/subsection has an explicit profile-resolved impl route and dependency from the beginning. The near-term detail is richer; the far-term private implementation is intentionally provisional.

An inventory row needs only: obligation or endpoint/command family, actual source/consumer reference, implementing section, and status/evidence reference. For a rewrite, include routes, background jobs, CLI/shell entry points, state/units/time, data paths, recovery and deployment. Do not enumerate every theoretical input combination or copy all source code into the inventory.

Group endpoint families only when they share an actual owner and acceptance path. A broad obligation such as “all APIs” must be expanded into the repository's finite supported surface before claiming whole-product coverage. Counts are a reconciliation aid, not an acceptance oracle.

## Reviewable section boundaries

Before dispatch, a section must answer:

- What supported behavior becomes real at its end, and through which public or production entry?
- What state/transaction/lifecycle invariant must be reviewed together?
- Which already accepted inputs does it consume? Who consumes its output next?
- Which example would distinguish a working implementation from a stub, cosmetic extraction or wrong fixture?
- Can one reviewer understand the changed behavior and its direct regression cone without rediscovering several unrelated subsystems?

If a section contains independently failing configuration, probing, scheduling, installation and upgrade state machines, keep them as roadmap outcomes and split the executable work by **coherent behavior**, not by a six-heading preference.

If one indivisible transaction/lifecycle spans multiple owners, preserve one parent and use serial subsections for real internal increments/model capability boundaries. Do not split it merely to obtain more repair budgets. Children require local tests/checkpoint review; their parent still owns the joint invariant and final acceptance.

Do not create one task per private helper, import, test command or reviewer comment. A work packet includes a real implementation increment **and its tests**. Conversely, do not use one catch-all “platform foundation” section to absorb every missing consumer discovered later.

File count is not semantic size. Model assignment follows examples, ambiguity, coupling, existing patterns and oracle strength. Do not downgrade simply because a difficult shared-state patch is short, or upgrade because a mechanical translation is long.

## Prove the production path early

Before multiplying analogous implementation, establish the smallest **representative production-path slice**. This is existing product work, not a separately billed smoke framework.

Examples:

- Runtime adapter: public CLI/MCP → real service → real store/driver with controlled upstream → result → close/reap. A fake Unix server can prove CLI serialization, but not service delivery or recovery.
- Backend rewrite: an actual request → private database transaction → stored state → actual reader. A helper returning a response-shaped object does not prove routing, parsing or rollback.
- Numerical pipeline: normalized configuration → production calculation → fixed wire → receiving service → persisted materialization → query consumer. A toy formula asserted against itself is not a reference oracle.
- Installed service: use the built/installed artifact and ordinary environment/config. A source-tree launch with hand-injected environment is not install acceptance.

Run the path's decisive dependency early: real private DB/extension for database semantics, actual process protocol for lifecycle, actual consumer decoder for wire contracts. Missing environment must be identified before extensive dependent implementation; it is not discovered for the first time in the closing review rounds.

Prepare only the relevant validation environment, using existing scripts/runner conventions. Reuse source/lock/cache/network identity and private data ownership. Do not create a new Compose project per repair, constantly clean build caches, or reset a user's actual data to make tests run.

When environment setup reaches compilation and finds a source error, it has served its purpose: fix the source. Do not require a clean build before allowing code fixes, and do not call a compiler error an environment blocker.

## Rolling detail without rolling requirements

Keep the **working horizon normally at the next two or three ready/dependent parents**, adjusted for a genuine indivisible seam. This is a context-management default, not an approval gate or a reason to suspend progress.

For the near horizon, specify current source paths, exact supported behavior, direct consumers, failure/rollback examples, candidate tests and resource ownership. For later sections, specify the outcome, known invariant, dependencies, assigned impl role, source/consumer family and oracle type; defer private signatures, exact fixture filenames and implementation choreography until their prerequisites exist.

Before a later section enters the working horizon, main reconciles its card against actual integrated code and updates the TASK. Existing PLAN_DELTA rules determine whether an independent delta review is necessary. Ordinary elaboration under the same contract needs no new full review or human approval. A changed boundary, authority, dependency or semantic implementation assignment follows the existing bounded correction rules.

Do not “roll” away an inconvenient required behavior. If a requirement is dropped, weakened, or replaced by an approximation, the ordinary owner-decision rules still apply. Never move an open finding to a later section just to accept the current public surface.

If a new independently accepted section is genuinely needed, give it a unique next sequential ID and explain its scope/lineage. Do not renumber accepted history every time the roadmap changes. A user-authorized wholesale replan may use S01 onward with an explicit old-to-new map; renumbering cannot reset repair budgets or review-provider history.

## Existing PLAN review, not another committee

The authorized PLAN pass checks two levels **in the same review**:

1. Whole roadmap: every required outcome has an owner; dependencies/consumer links resolve; the first representative slice is early; final deployment and deletion are owned; milestones are not disguised mega-sections.
2. Working horizon: current source, actual environment, decisive examples and reviewable packets are sufficient for real implementation.

Far-future private API or probe schema details are not blockers when no existing consumer requires them. A test file assigned to a future implementation naturally does not exist yet. Block only a material omission, wrong authority, impossible intermediate state or unresolved high-impact decision.

The independent reviewer may inspect any relevant roadmap edge, but must not expand every future card to the same detailed level or rerun whole-plan discovery at each horizon advance. The embedded profile's external final PLAN round uses this same lens; it does not add another review beyond existing policy.

The public “no more review requested” or other explicit owner override remains an authority question to resolve from the user's exact scope; a Skill is not permission to erase explicit user decisions.

## Implementation and review packets

Every active TASK carries the relevant source reference, incoming/outgoing contract, decisive positive and negative example, required checks and explicit non-goals. Reuse source-to-contract references; do not replace them with “implement S17 faithfully.”

Handoff must distinguish:

- code exists / compile succeeded;
- targeted behavior executed;
- real assembled production path executed;
- remaining mandatory work versus optional optimization.

Known incomplete required work returns to the implementer; it is not a completed implementation to send through a new full discovery pass. A read-only review may still diagnose a specific uncertainty, but cannot promote that partial work to acceptance. Do not turn every partial reply into a new recovery allocation, new section or Advisor request.

Give reviewers direct, valid paths to the frozen TASK, contract, current finding ledger, changed code/diff, and actual check result. When the external provider cannot run shell/diff commands, prepare a bounded read-only packet from the real Git candidate; do not ask it to guess filenames or reconstruct unseen evidence. Full independent review should not inherit the previous reviewer's persuasive verdict, but it does need the governing contract and objective test evidence.

## Composition checkpoints

At a planned outcome checkpoint, the main agent uses the already required parent reconciliation/final checks to answer:

1. Does the named journey run through the real components already delivered?
2. Which part is still fake, bypassed, manual, source-tree-only or not connected?
3. Did a shared contract change, and are the next cards still valid?

Record the answer in the existing HANDOFF/FEATURE-STATE. Reuse exact-candidate checks where valid. Only a concrete `unproven_composition` justifies additional integration work/review; do not repeat accepted local review or the entire suite by calendar.

Perform this at actual composition boundaries or after a material shared-contract correction — never on a fixed timer, and not after every section solely because the feature is long. No routine external Advisor, new checker agent, recurring automation or mandatory all-repository audit is added.

Milestone progress means a tested journey, not a percentage of headings. An installed-entry proof can remain unproved while code is locally accepted; report both without relabeling unfinished obligations “done.” Conversely, unchanged code/test evidence does not expire merely because a documentation or test-only commit advances HEAD; reuse follows the existing impact rules.

## Existing owners, tests and cross-language rewrites

### Shared owners are not untouchable ancestors

“Accepted” freezes a proven behavior, not a permanent file-write ban. If the current diff necessarily requires a correction/extraction in an existing shared owner, main admits the smallest enabling change, records the consumer chain and runs affected regressions. Do not force duplication, a second transaction, pool, cursor or scheduler to avoid touching the right owner. Do not reopen unrelated accepted behavior.

### Separate behavior from language accidents

Keep the current source baseline and approved bounded-compatibility profiles authoritative. Distinguish:

- required user-visible values, units, precision, response/error priority, transaction effects, actual parser identity and lifecycle;
- internal representation, permitted PRNG differences or approved bounded parser alternatives;
- incidental/unreachable historical language behavior not required by the contract.

No blanket “Python behavior is out of scope,” no mandatory Python RNG/ORM emulation, and no global loosening from an exception granted to one route. Existing supported defaults/config controls must actually affect the production path. A control retained in a schema but ignored in computation is not equivalent.

### Fix the oracle before guessing the product

Use valid source-shaped fixtures, actual schema/state representations and the relevant public/production path. Label pure/source-kernel, controlled-provider, real DB and installed/live evidence separately. A test that exits early without a required DB, executes zero filtered cases, only compares a helper with itself, or drives a fake replacement for the very owner being claimed does not establish that behavior.

A malformed fixture is not automatically a product bug. Keep a tiny source-derived truth table where the same invariant has produced repeated contradictory reviews; freeze root-cause criteria and use delta closure rather than repeatedly polling fresh full reviewers for a different answer.

## Replanning an active program

Read actual Git/worktree, current code, relevant accepted handoffs and adopted Advisor decisions before writing the replacement plan. Priority for present state: actual candidate + latest valid acceptance facts; old plans and chronological summaries are provenance, not new facts.

List accepted baseline, partial-but-valid work, still-open findings and genuinely unimplemented outcomes separately. Preserve current branch, dirty work, test results, provider cursor, original repair lineage and scoped Advisor grants. No cleanup/reset, rebase, replay of accepted predecessors or automatic source deletion is implied.

Replace only active planning artifacts under user authority, archiving the previous plan and current-state note locally. A simple mapping row can relate an old parent/child to the new section and preserved evidence. Missing old counts stay UNKNOWN; do not manufacture zero. A real source change in an allegedly completed unit is handled through its affected invariant, not through a whole-feature restart.

Before resuming, stop/check actual old writers/reviewers; metadata edits do not stop processes. Verify dirty files against the handoff snapshot and preserve newer correct edits. Run basic PLAN structure validation once, then the necessary bounded independent review of the new remaining roadmap/horizon. This is not a requirement to re-review every accepted predecessor.

## Resuming across sessions

Keep one short current-state header with actual base/candidate, accepted prerequisites, active unit, next concrete action, live actors, real blocker and the efficiency-log pointer. Older notes belong below an explicit history marker or in the archive; do not accumulate contradictory “current” declarations.

On takeover, read current state + roadmap overview + active card/TASK + decisive evidence. Use an explicit artifact locator; do not reread a 2,000-line plan and every historical report at every dispatch. If state disagrees with code, reconcile only that discrepancy before dispatch, not the whole history.

A completed product's later request remains new work by default.

## Advisor and efficiency

The existing rare external-human ADV gates remain unchanged. Repeated external correction should first be classified: missed product obligation, wrong source baseline, invalid oracle, overly broad section, overly narrow shared-owner scope, stale packet/state, or genuine unresolved architecture/semantics. Do not use periodic Advisor as the ordinary missing integrator.

Preserve every adopted decision and its exact local scope. A prior special grant is not a global new repair budget; an already resolved decision need not be asked again. Capacity, agent-thread-limit and other upstream transport failures are infrastructure events, not planning defects, failed product repairs or evidence that a section needs architectural replacement.

The efficiency checkpoints apply unchanged across sessions, not as a new report suite: each interim handoff keeps the log current, the baseline may be revised at a real milestone with the reason recorded, and the closeout summary covers the whole program, not the last session.

## Counterexamples and cost limits

- **Six large headings:** valid as six outcome groups; invalid as six bounded execution packets if one hides migration, queueing, permissions, recovery, installation and their consumers.
- **Thirty-nine headings:** no guarantee of reviewability if the first parent combines DB DDL drift, retention metadata, config mutation and multiple HTTP encodings before any real DB run.
- **Every helper gets a child:** too fine; repeated setup/context and empty “partial complete” handoffs grow without delivering behavior.
- **All future implementation frozen now:** too rigid; later actual interfaces change, creating arbitrary PLAN blockers.
- **Only next task planned:** too weak; required consumers/commands/cutover disappear until an external audit.
- **Shared accepted owner inspect-only forever:** forces patches around the correct abstraction; use bounded causal owner correction instead.
- **Fresh full review after every fix:** not permitted by long-horizon mode; ordinary delta/assurance and parent repair budget remain in force.
- **Twelve-hour obligatory Advisor or composition check:** not introduced — the named historical design this chapter rejects. Composition checks fire at actual boundaries; source-grounded local evidence resolves routine direction before external adjudication.

These are planning practices, not validated model-performance claims. Evaluate on future real tasks; the lightweight basic section validator checks syntax/DAG only and cannot certify scope, model identity or semantic completion.
