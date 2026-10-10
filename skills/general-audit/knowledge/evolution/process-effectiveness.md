# Development-process effectiveness — optional lens

**Trigger:** repeated review escapes, excessive handoffs/retries, routine artifact work dominating features, conflicting model/tool claims, or a user-requested cross-feature retrospective. Not a mandatory extra audit for every project/run.

**Hypothesis:** process steps measure paperwork rather than failure reduction; multiple reviewers share one oracle; telemetry gaps hide physical attempts; a broad ceremony duplicates already-valid local evidence. A process may also look expensive because it catches real high-consequence failures.

**Distinguish:** sample actual completed work and contemporaneous evidence. Separate application defects, plan/requirements drift, reviewer judgment, harness/lifecycle faults and measurement gaps. For **SFD**, its audit object is SFD execution: actual requirements/corrections, accepted candidate, physical vs logical attempts, targeted checks, evidence loss and workflow cost. It is not a substitute code-audit stage. Use actual exports/receipts, not self-reconstructed logs or requested model names as observed identities.

**Counterevidence:** justified boundary/acceptance checks and evidence captured only during execution cannot safely be postponed. Slow tests can be necessary; less ceremony is not automatically safer. A repeated experiment is not a new independent case; missing usage is unknown, not zero.

**Expansion:** compare representative successful and failed features before recommending removal of a gate. Preserve useful observations at source and move only retrospective synthesis when warranted. Do not reopen completed product work, alter SFD gates, re-run calls for a cleaner cost log, or read unauthorized raw sessions.

**Closure:** a concrete keep/remove/defer recommendation tied to observed failure prevention and cost, with migration dependencies and counterexamples. New workflow adoption needs separate authority and coordinated producer/consumer changes. Incident learning should target a recurring mechanism, not punish an agent or add a universal gate for one case.
