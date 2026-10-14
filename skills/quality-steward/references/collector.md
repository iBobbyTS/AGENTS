# Optional local collector

`python <quality-steward-dir>/scripts/collect.py /absolute/repo --base <verified-revision>`

Requires Python and a trusted Git executable. No package install, project scripts, checkout, fetch, source-content output or repository-state writes. Stdout is an observation JSON packet, **not** a recommendation. Review paths/subjects before externally sharing. Keep the output outside the inspected worktree or in an already-approved ignored location so it doesn't create self-triggering changes; the collector doesn't alter `.gitignore`.

The caller must choose an actual collection base: for accumulated audit need, use the verified broad-audit range and coverage context, not blindly last week's scan. Last-observation deltas may supplement it, but cannot replace accumulated scope. The collector does not read/parse natural-language audit ledgers or infer risk acceptance.

It handles ancestry, bounded name lists, dirty/untracked files, unusual filenames, renames and combined working-content/staged-blob fingerprints. Output records missing baselines, shallow history, truncation, unreadable/oversized files, unsupported nested state and observed races. Missing facts stay unknown, never zero/safe. Exit 0 means complete **within the collector's declared limits**, 2 useful but incomplete, 1 no usable repository identity. Capture stdout even on exit 2; never use `|| echo safe`.

Default limits: 120 paths per list, 256 KiB Git output per command, five seconds per Git command, 1 MiB per dirty file and 16 MiB total dirty content. Output/time checks are sampled, so a small transient output overshoot is possible. Limits are implementation bounds, not a quality threshold. If a limit leaves a material gap, request the specific missing evidence rather than scan the entire repo.

Files ignored by Git, actual runtime/deployment state, events, dependency advisories, check results and audit coverage are **not collected**. Supply relevant permitted evidence separately. Dirty submodule internals aren't fully fingerprinted. A packet isn't an atomic filesystem snapshot: it detects observed branch/head/status/staged-blob/hash drift but cannot exclude every concurrent change. Recheck relevant evidence before a consequential decision. Huge repos may return incomplete rather than hang.

Paths are passed as subprocess arguments, not through a shell. External diff/text conversion, Git fsmonitor and lazy fetch are disabled for these observations. Only run on explicitly enrolled/trusted local repositories with an installed trusted Git executable. The collector is not a sandbox for malicious Git implementations or a protection boundary against a hostile same-user process.
