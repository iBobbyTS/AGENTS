# Handoff — <feature / parent / child>

- Actual writer ID, requested role/model/effort; observed metadata or UNKNOWN:
- Task/PLAN references, repository/branch, base → candidate:
- Actual behavior and changed paths:
- Changed boundary, when applicable: actual redacted request/response fixture or exact source/test reference; encoding, subset/global, failure/late-result meaning; named consumers:
- Planned example changes and why; unobserved output explicitly marked, not claimed as captured evidence:
- Tests/checks you ran: command, relevant input/head/environment, exit status and key lines inline (long raw output is collected by main under `.agent-work/evidence/{feature}/`, never written by you):
- Remaining parent behavior, joint-oracle needs, no-future-scope statement:
- Risks/owner decisions/gaps:

The worker writes this file itself at the dispatched path; its final answer carries only the path, signal and one-line status. Main reads the file for admission and may append Git verification, never rewriting failed or unknown results into success.
