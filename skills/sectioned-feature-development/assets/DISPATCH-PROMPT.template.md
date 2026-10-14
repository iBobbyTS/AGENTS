# Dispatch prompt — <role / S{id}>

<!-- Coordinator template: replace the placeholders, drop this comment, send.
     The prompt carries task facts only — role law, report conventions, git
     prohibitions and scheduling metadata never enter it; the worker's
     developer instruction (assets/ROLE-INSTRUCTIONS.md) already binds those. -->

Repository/workspace: `{absolute repository path}`

TASK: read `{.agent-work/sections/{feature}/{id}-TASK.md}` and execute it.

Report: write your full report to `{.agent-work/handoffs/{feature}/{id}-HANDOFF.md}`.

<!-- Reviewer variant: replace the TASK line with the bounded request built
     from SECTION-REVIEW-REQUEST.template.md (plus the exact `{BASE..HEAD}`
     diff range) or PLAN-REVIEW-REQUEST.template.md (plus the plan path and
     candidate reference), and point Report at the review report path. -->
