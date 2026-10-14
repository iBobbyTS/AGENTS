# Host Configuration (quality-skills Project-Level)

This document describes the project-level runtime environment and **is not installed into the host alongside the `skills/` directory**. Model selection, default triggers and schedules, multi-project aggregation, and calibration methods are maintained exclusively here. Since v1.1.0, the skills themselves contain only runtime workflows and decision logic.

## Models

- On this machine, **quality-steward triage always runs on a Flash-tier model, with no escalation path**. Semantic issues that cannot be resolved in a single invocation must return NEEDS_EVIDENCE or RECOMMEND_AUDIT according to the skill rules, rather than pretending that a more capable review has been performed.
- Cost control comes from **doing less work, not writing longer instructions**: delegate Git calculations and identity verification to `collect.py`; use small evidence packets, four explicit states, no item-by-item checklists, line-number bookkeeping, or generated scores; allow one targeted query and a concise handoff. Evidence locations are not required for every passing item.
- Tool permissions and requirements for actual observation are not relaxed based on model capability.
- Provider capabilities (such as whether thinking can be disabled) depend on the actual host and version. This package has not undergone real-world model accuracy benchmarking.

## Triggers and Scheduling

The following table provides recommended starting points for this user's multi-project workload, **not empirically optimized thresholds**. Installing the skills does not install timers, modify Git hooks, or authorize deep audits.

| Trigger | Action | Attention Strategy |
|---|---|---|
| Existing ~100-commit reminder | Run bounded steward triage rather than a mandatory audit; modify hooks only with user approval | At most one new or changed recommendation per repository |
| Weekly check of registered active repositories | Read low-cost observations and due events/decisions; no broad source-code scanning | Produce one consolidated summary only for actionable differences |
| Milestone or major supported-boundary change | Use a user event or existing development handoff; no additional report required | Triage promptly at a safe task boundary |
| Incident or recurring escaped defect | After authorized immediate response, triage the investigation and recurrence risk | Do not delay major active risks for a scheduled summary |
| User indicates readiness to release/deploy | Route to user-triggered deployment-preflight | No automatic release/deployment; GA is not a mandatory prerequisite |
| Quiet but still used/exposed project | Recheck known risks, support status, and dependency evidence on an appropriate local calendar | No commits does not mean no risk |
| Paused and unused project | Skip routine model invocations until reactivation or an explicit event | Git inactivity alone does not establish that a project is unused |

- **Before enabling automation for the first time:** Register only explicitly named repository roots; confirm the existing runner, time budget, and notification destination. Audits always require human approval. A project may initially use only the existing 100-commit hook; weekly aggregation is optional.
- **Default startup behavior:** The skill's `scan_repos.py` reads `~/.agent-work/quality-steward/repos.jsonl` (each line containing `repo_path` and `last_commit`), records new commits in `inspections/YYYYMMDD.md`, updates observation cursors, and then triages repositories sequentially in registration order. When the user explicitly requests a single-repository check, the registration scan is skipped. The registry file must already exist; installation neither registers repositories nor runs scans.
- **Manual registration:** The user creates the registry file manually; neither the installer nor the skill creates it automatically. The initial `last_commit` should preferably be the latest commit covered by the most recent broad audit. If no audit history exists, use the HEAD at registration time; subsequent commits will be counted from the first scan onward. This field is an **observation cursor**, not an audit baseline or completion marker.
- **Same-day scans:** Append to the same inspection file. Records contain only the repository, commit range, and commit count. Pending-work packets and audit/preflight reports are stored separately. Advancing an observation cursor does not mean triage has been completed; after an interruption, resume unfinished ranges using that day's inspection file.
- **Audit necessity:** Decisions must consider both the most recent **broad audit** and accumulated changes/coverage. Audit debt must not be reset after every scan.
- **Snoozed or rejected recommendations:** Record the affected scope, reason, and conditions for re-evaluation. Do not endlessly repeat identical recommendations, but do not treat a single rejection as permanent risk acceptance. Critical or neglected areas subject to prolonged deferral must resurface when their review becomes due.
- **Per-repository failures:** A failure in one repository produces NEEDS_EVIDENCE for that repository only. Processing continues normally for all other entries.

## Multi-Project Aggregation

- This package provides a registered-repository scanning script, not a portfolio daemon. An existing authorized runner may invoke the skill, which processes scan results sequentially. Scheduling and model invocation remain the responsibility of the host.
- Consolidate non-urgent changes across projects into a single summary. A failed or inaccessible repository must neither obscure other repositories nor be reported as healthy.
- Deep audits are not run concurrently by default. Follow the user's existing runner policy.

## Calibration and Regression Testing

After changing the model, host harness, or prompts, rerun comparisons against **the same set** of representative repositories and event packets. The current configuration uses a single Flash model with no escalation group.

- **Test coverage:** Include negative cases requiring no action, significant positive cases, missing or truncated observations, dirty worktrees, projects without CI, repeated failures, and adversarial repository text. Cases must represent distinct scenarios. Randomized runs may resample cases, but repeated samples do not count as independent projects.
- **Evaluation criteria:** Evaluate decisions together with transcripts and actual tool effects, rather than judging response quality based on wording alone.
- **Metrics:** Record missed major audit needs, unnecessary audit initiations or recommendations, false NO_ACTION decisions under missing facts, incorrect targets, permission violations, valid-packet completion rate, and total cost (queries, retries, and manual remediation).
- **Shadow-mode validation:** Initially compare the system's decisions against those the user is already making. Until local evidence supports routine suppression, significant ambiguous cases must be surfaced rather than declared safe.
- **Regression handling:** When regressions occur, narrow the handling of the affected scenario or adjust the configuration. There is no requirement to rerun every unrelated expensive test for each new version.
- **Conservative policies:** User-approved conservative policies may prohibit automatic NO_ACTION decisions for specified high-consequence unknowns.
