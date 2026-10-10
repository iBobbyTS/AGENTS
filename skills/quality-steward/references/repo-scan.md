# Registered repository scan

Run `python <quality-steward-dir>/scripts/scan_repos.py` at startup unless the user explicitly limits this invocation to one repository. Requires Python, Git and a POSIX host. It reads `~/.agent-work/quality-steward/repos.jsonl`; each nonblank line is an object with these required fields (additional fields are preserved):

```json
{"repo_path":"/absolute/worktree/root","last_commit":"<previously observed commit hash>"}
```

`repo_path` may start with `~/`. Repositories must already be enrolled; do not discover/register repositories or invent a first baseline. Missing/malformed registry is an evidence gap, not permission to create it. `--state-dir /absolute/directory` overrides the state directory for isolated runs.

For each entry, the script captures HEAD and counts commits in `last_commit..HEAD`, excluding the old commit. Positive counts append a heading and range/count to `inspections/YYYYMMDD.md` using the host's local date. Same-day runs append rather than overwrite. Successfully observed entries advance `last_commit` to that captured HEAD, including zero-count entries. This is an **observation cursor**, not completed triage or an audit baseline. Missing commits, divergent/shallow history, inaccessible repositories and observed HEAD races leave that entry's cursor unchanged; other entries continue. Git commands have the collector's time/output limits and do not fetch or modify repositories.

Stdout is JSON with `inspection_file` and ordered `repos`. Each entry contains `repo_path`, old `last_commit`, `status` (`changed`, `unchanged`, `error`); successful entries also contain `current_commit` and `commit_count`. Exit 0 means all entries observed, 2 means per-repository errors with usable results, 1 means a registry/write/concurrent-scan failure. Capture stdout on exit 2 and surface each error as NEEDS_EVIDENCE. Exit 1 stops this batch; do not treat it as no changes.

Use returned old/new revisions for this invocation even though the registry has advanced. Process `changed` entries sequentially in registry order through the normal observation, decision and handoff steps. Zero-count entries need no commit-triggered triage, but explicit incidents, due revisits and other supplied events still apply. The daily file preserves scanned ranges if triage is interrupted: resume unfinished ranges from it; a second scan's zero count does not prove the previous triage completed. Do not replace broad-audit coverage with this cursor or infer clean dirty/runtime state from the count.

Writes are restricted to the steward state directory. Concurrent script runs use a nonblocking lock; the registry is replaced atomically after the daily record is flushed. A failed registry write can leave a duplicate range when retried; deduplicate it by repository and old/new hashes.
