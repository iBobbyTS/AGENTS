# Failure detection, containment and usable recovery

**Trigger:** meaningful failure detection, restore promises, ownership transition, operational incidents or critical background work. For exact release identity, environment and version ordering use the canonical [artifact](../release/artifact-identity.md), [environment](../release/environment.md) and [transition](../release/transition.md) cards rather than duplicating them here.

**Hypothesis:** code works in the author's environment, but the deployed entry point uses a different artifact/configuration; backups cannot restore a usable system; a runbook invokes an obsolete owner; monitoring reports process health while useful progress stopped.

**Distinguish:** trace build artifact → launch/configuration → state location → health signal → recovery command. Inspect the real command path, permissions and dependencies. Where authorized, use a disposable restore or startup/refusal test and verify usable data/application state. Sample an actual failure signal against what an operator would observe and do. Check source/deployment version mismatches before concluding from either.

**Counterevidence:** a small stateless tool need not have an on-call program, multi-region deployment or backups. A known unfinished migration stage can legitimately retain the old owner; inspect the active/accepted ownership decision. Operational objectives must come from real usage or explicit commitments, not a generic uptime ideal.

**Expansion:** follow the failed recovery chain or deployment assumption; do not run production chaos tests to prove a code finding. If credentials, infrastructure or hardware are absent, name exactly which restoration/operational claim remains unverified and continue static tracing.

**Closure:** runnable recovery/startup behavior under the supported configuration, or a precisely bounded source conclusion. Documentation edits alone do not prove recovery. A backup's existence/hash does not establish restored business correctness.
