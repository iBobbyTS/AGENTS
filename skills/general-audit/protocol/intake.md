# General-audit intake v1

Owned by general-audit. A human request is valid without this format. A producer such as quality-steward supplies a **proposal**, not authority or a verdict. The auditor may change questions after inspecting reality. No JSON handshake, approval hash or dispatcher API is required.

For a handoff crossing sessions, save this short Markdown block (usually 100–200 words, a target not a validation limit). In the same context it may be inline. Reference existing evidence; don't paste a diff or long report.

```text
General audit request v1
Target: <absolute repository/worktree; branch; observed revision; dirty/unknown>
Mode: <baseline | routine | focused | milestone | followup>
Why now: <1–3 observed signals, each with a usable evidence locator>
Questions: <1–3 open questions, not assumed defects; advisory, not exhaustive>
Evidence: <observation packet, previous report/coverage, relevant local logs>
Bounds: <user constraints; priority area; other work not yet assessed>
Unknowns: <material missing facts, or none known within this triage>
Authority: PROPOSED — user has not authorized deep audit / <actual user authority>
```

Missing reference/revision is explicitly unknown, never guessed. A revision is the **observed** target; general-audit must re-establish reality before using it. New runtime incidents can justify investigation without source changes. No CI is not itself a finding or a reason to demand infrastructure.

A release request belongs to deployment-preflight. A failing cheap check may need an ordinary fix rather than an audit: report the existing failure and its evidence, don't inflate every lint/test failure into a whole-system investigation. Active incidents need authorized containment first; general-audit is a later investigation, not emergency automation.
