# What was actually examined?

**Trigger:** scanner/test reports, audit packs, delegated summaries, truncated output, missing history or impressive percentages/counts.

**Hypothesis:** the run succeeded but excluded the relevant file, test variant, failure invocation or consumer. Duplicate events inflated a count, a skipped probe became a pass, or requested agent identity became observed identity.

**Distinguish:** identify the population appropriate to the claim: actual files/rules/targets, test cases/configuration, invocation IDs or produced records. Check selection rules, skips, output truncation and available raw evidence. Sample both included items and a relevant expected item that could be omitted. When a completeness claim matters, reconcile its denominator; when only a narrow claim matters, do not demand an exhaustive data warehouse.

For an audit pack, compare material findings and execution claims with raw IDs/results when supplied. Preserve failures and nonblocking issues. Do not double-count repeated references to one invocation or assume cached-input usage is disjoint from total input. Never infer billing/quota without the provider's actual definition.

**Counterevidence:** declared exclusions and sampling can be appropriate. The finding is not “didn't read everything”; it is an unsupported assurance claim or a consequential omitted case. Missing raw evidence limits confidence but is not proof of falsification.

**Expansion:** if one selection mechanism is broken, inspect other outputs using it. If the relevant file was never scanned, repair the claim and investigation before treating the scanner's clean result as evidence. Report absent subagent/tool access honestly.

No mandatory telemetry subsystem is introduced.
