---
name: quality-steward
description: Lightweight repository quality triage using repository observations, available check results, incidents and general-audit coverage. Decide whether to recommend a general audit, request specific evidence, or remain quiet. Use at a commit/calendar/event trigger or on request. It never performs a deep audit, installs automation, fixes code or starts deployment. Audit proposals follow general-audit's intake.
---

# Quality steward

Spend little attention to decide **whether investigation is worthwhile**, not whether software is correct. General-audit owns the [handoff contract](../general-audit/protocol/intake.md); read it when handing off. It works without this steward.

## Startup: select repositories

Unless the user explicitly asks to check only one repository, run [scan_repos.py](scripts/scan_repos.py) first; read its [runtime contract](references/repo-scan.md) before first use. It reads `~/.agent-work/quality-steward/repos.jsonl`, records new commit ranges in `~/.agent-work/quality-steward/inspections/YYYYMMDD.md`, advances observation cursors and returns an ordered queue. Then perform steps 1–3 below **sequentially for each changed repository**, using the returned pre-scan base and captured HEAD. Surface failed entries as NEEDS_EVIDENCE and continue with usable entries. Supplied incidents/due revisits still apply to zero-count repositories. If the user limits the invocation to one repository, skip the registry scan and apply steps 1–3 directly to that repository.

## 1. Observe a small, trustworthy packet

Each repository receives one bounded decision for its scope and available trigger/evidence; a trigger is not permission to spawn unapproved agents or spend outside the authorized budget. Read the project's existing guidance, general-audit coverage, previous pending recommendation, user events and available result summaries. Don't create a second quality/finding ledger or infer a deployed state from local activity. The scan log and cursor track observations only; they do not reset accumulated audit scope.

For Git, optionally run [collect.py](scripts/collect.py) on an explicitly supplied local repo and a verified collection base. Read the [collector limitations](references/collector.md) before first use. It performs only bounded local observations, with no project scripts, network or repository modifications. It is not a risk detector. A non-Git project can supply equivalent identity/change evidence manually. Explicit user-provided incidents outrank an empty Git diff.

Check identity, ancestry, dirty state, completeness and observation stability before interpreting "no change." Preserve unknowns/truncation/errors. Read the last broad coverage as well as recent focused checks; a targeted clean does not erase broad review debt. Check whether evidence is current and from the right runtime/artifact. Absent CI is simply absent CI; don't install tests/scanners to fill a template. An inaccessible repo is NEEDS_EVIDENCE for that repo, never a healthy NO_ACTION.

## 2. Make one bounded triage decision

Look for changed trust/state/consumer boundaries, repeated repair or escaped-defect patterns, test-system changes, known due risk decisions, a completed capability, or a neglected critical area. Documentation-only changes are not automatically low risk: changed install/recovery commands, compatibility promises or agent instructions can change real consumer behavior. Use general-audit's [documentation integrity](../general-audit/knowledge/mechanisms/documentation-integrity.md) only when that signal needs investigation; harmless copyediting alone does not require an audit. Path and commit-word heuristics are leads, never proof. Use one small targeted source/configuration look when needed to disambiguate a material signal. Stop if the next step would be a real audit.

Return one of:
- **NO_ACTION**: no new worthwhile action supported by the available, sufficiently complete triage evidence. Not a health certificate.
- **RECOMMEND_AUDIT**: a short general-audit request with evidence-linked questions.
- **USE_EXISTING_WORKFLOW**: surface a known failing check, incident-response need or user-requested preflight through its existing workflow, without inventing a deep audit or executing that action.
- **NEEDS_EVIDENCE**: name the one missing observation that changes the decision; keep any independently justified audit recommendation visible.

A known isolated failing check may need ordinary development rather than an audit: identify that existing failure as the action, without pretending to diagnose it. An active incident needs the user's existing containment process first; don't wait for a scheduled audit or attempt containment yourself. A release intent routes to **manual deployment-preflight**, not automatic execution and not a redundant general-audit gate.

Use [decision examples](references/decisions.md) only for ambiguous cases. No risk arithmetic, confidence percentage or universal commit/coverage threshold. Extract a few decisive questions, not an enumeration of every potential defect. Missing facts stay missing: never reinterpret them as resolved, never manufacture evidence, and never pretend a deeper review happened. If the packet plus one lookup cannot resolve the decision, return NEEDS_EVIDENCE.

## 3. Handoff or remain quiet

USE_EXISTING_WORKFLOW gets one actionable sentence and its evidence/target; do not disguise it as NO_ACTION. Normal scheduled NO_ACTION stays silent; a direct user request gets one sentence. For a recommendation, show **one sentence** identifying project, reason and priority, with a link to a **short packet** conforming to general-audit intake. Save only that packet when a later/new-context auditor needs it; no long steward report, plan or copied diff. Set Authority to PROPOSED unless actual standing/user authorization exists. Never start deep audit merely because a threshold fired.

Reuse/update one pending action per project and scope. Suppress unchanged reminders using the actual observed revision/dirty fingerprint **plus** event, evidence and revisit conditions. An unresolved critical unknown is not a "no change" success; record it and surface meaningful changes or a due revisit. New consequential facts bypass a snooze. No-source-change does not cancel a runtime incident, exposed dependency concern or scheduled risk revisit.

Keep minimal steward-only state via [state template](templates/STATE.md): last observation, pending packet, notification/snooze and next condition. Do not overwrite general-audit findings or its completion baseline.

Do not install hooks/schedulers, modify products, run deployment, or manufacture actual model/tool evidence. Stop after the decision and lean handoff.
