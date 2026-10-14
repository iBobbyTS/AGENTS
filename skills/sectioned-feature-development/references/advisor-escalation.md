# External advisor escalation — human handoff for non-converging work

## Two advisor kinds, both external and human-mediated

- **PLAN advisor**: a PLAN-stage trigger below, or PLAN repair budget/diagnosis that cannot converge.
- **CODE advisor**: a section lineage's repair budget and its one automatic recovery cannot close, or a code-stage trigger below.

Both live outside the current host runtime; the human obtains the decision and returns it. There is no model-level advisor route: never spawn a subagent as an advisor, never select an advisor provider/model, and never let a second reviewer substitute for one. This mechanism is independent of the efficiency checkpoints.

## Triggers

1. `ADV-01 SECOND_CONVERGENCE_FAILURE` (code): an original section lineage consumed its one automatic hard-cap recovery; the replacement reaches another hard cap or requires a sixth independent material repair wave.
2. `ADV-02 HIGH_IMPACT_REVIEWER_CONFLICT` (plan/code): the two independently dispatched reviewers independently recommend mutually exclusive architecture, trust/persistence/public-compatibility boundary, scope authority or merge verdict, and one bounded probe/test cannot resolve it.
3. `ADV-03 LARGE_VALIDATED_WORK_DISCARD` (code): restart-from-base or major-owner rebound would discard roughly 20% or more of validated feature implementation; the cause is not an ordinary local bug.
4. `ADV-04 UNRESOLVED_TRUST_OR_CONSISTENCY_MODEL` (plan/code): two materially different security, credential, durability or concurrency models remain plausible; both over- and under-design have serious consequences; repository/user authority does not choose one.
5. `ADV-05 RELEASE_EVIDENCE_CONTRADICTION` (code): source/Git, deterministic checks and independent reviewers disagree about final-HEAD release readiness, and one same-environment deterministic rerun cannot reconcile it.
6. `ADV-06 EXTERNAL_SYSTEM_SHAPE_UNRESOLVED` (plan): after one bounded real probe, external protocol/agent/harness shape is still unknown and continuing would lock in a costly or irreversible architecture.

## Non-triggers

No escalation for a normal bug, first finding, first hard cap, one advisor-package exclusion, missing credential/environment, simple merge conflict, pre-existing baseline failure, a product decision directly answerable by the user, low-cost local refactor, or one model's preference. Diagnostics alone do not create a system-level decision. Ask the owner directly for ordinary business semantics.

## Freeze and package

1. Stop writers/reviewers using actual lifecycle tools; do not merely clear their IDs. Record final partial results, and freeze HEAD, dirty patch, requirements, PLAN-FULL, contracts and the ledger; these execution records are always required.
2. Create `.agent-work/advisor/{YYYYMMDD-HHMM_feature-id}/request/` and the sibling `response/` directory. Save a filled copy of `assets/ADVISOR-REQUEST.template.md` — the adjudication note — as `request/ADVISOR-REQUEST.md`.
3. Run the `advisor_pack.py` export helper. It packs one zip into `request/`: the user requirements, the complete current source tree plus Git evidence, and what the two flows require — PLAN advisor: PLAN-FULL, plan review reports and the bounded diagnosis; CODE advisor: section contract, findings ledger, repair-wave history and the hard-cap diagnosis. The helper excludes detected secret-like content at any file size, recording omissions without blocking the remaining package. It applies the same filter to generated Git evidence; binary patches are omitted. Raw `.git` metadata and other `.agent-work` content are excluded by default; `--include-git` and `--include-agent-work` opt in (this request's own `request/` output directory stays out), `--exclude` drops additional in-repo paths and `--include` recovers untracked build/cache directories — all recorded in the manifest, and none of them can bypass content filtering. A portable bundle is included only when its reachable, decompressed history passes the same full-content checks at any object size; otherwise the current source snapshot and the recorded history gap remain. Symlinks are preserved without following them. Filtering is best effort, not a guarantee that the archive contains no secrets; the user reviews the package before forwarding. The helper prints every archived file above 2 MB (at most 50) plus an `AGENT_INSTRUCTION` line to verify necessity or include/exclude policy, and the final zip size; act on that instruction — tighten `--include`/`--exclude` and re-export — before handing the zip over. Do not mutate Git, reset, clean or upload.
4. Before the request snapshot, allow active actors to stop and persist their final partial work; if HEAD changes afterwards, packaging blocks and the request must be explicitly refreshed rather than silently using a stale decision packet.
5. Main records ADVISOR_REQUIRED and sets WAITING_EXTERNAL only after real actors stop and the export verifies. No workflow approval script is used. Respond only with the paused state, the request path/hash, and the handoff prompt asking the user to deliver the zip to the external advisor manually. Do not continue normal development while waiting.

```bash
# Create the request/response directories and save the completed note here first:
# .agent-work/advisor/20260922-1430_quota-switch/request/ADVISOR-REQUEST.md
python {skill-dir}/scripts/advisor_pack.py --repo /abs/repo \
  --request 20260922-1430_quota-switch --trigger ADV-04
```

## Human handoff

```text
请将附件交给外部 Advisor，只读检查完整仓库、Git、已确认需求、PLAN、review 和测试证据。
当前触发：<TRIGGER_ID>；冻结 HEAD：<HEAD>。
需要裁决的唯一问题：<EXACT_DECISION>。
请返回 DECISION、关键证据、最小安全边界、否决方案及理由、保留的有效工作、后续顺序、停止/再次升级条件和不确定性。
不要直接改代码、扩大产品需求或代替 human owner 接受业务/风险/破坏性操作。
```

The skill need only know that an external advisor exists; no model name is embedded in routing.

## Result intake

Save the returned result verbatim as `response/ADVISOR-RESULT.md`; main records the actual provenance. Record provenance/model only when actually provided. Receiving advice keeps the feature blocked at `WAITING_HUMAN_DECISION`.

The human explicitly accepts, rejects, or requests clarification. Save the actual human message and its decision/provenance with the request. Main applies only that authorized disposition. A model-authored approval is not human authority; no receipt schema or adopt CLI is required.

Apply only the accepted bounded action; preserve accepted sections, history and original repair counters. Do not restart a clean streak, reset a budget, silently reopen a completed PLAN or infer merge/reset/push authority. A technical recommendation needing a plan revision still follows the existing bounded PLAN delta process.

## Records

Capture the trigger facts, request path/hash, frozen code identity, recorded exclusions, raw returned result, human adoption, applied action and resumed outcome in the advisor request/response directories; the anomaly checkpoint of [efficiency-checkpoints.md](efficiency-checkpoints.md) gets one line when an advisor fires.
