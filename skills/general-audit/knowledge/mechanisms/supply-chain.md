# Build, dependency and release trust

**Trigger:** external packages/actions, install scripts, generated artifacts, publish credentials, downloaded tools or build/release changes.

**Hypothesis:** the reviewed source is not the artifact users run; an untrusted input reaches a privileged build step; a lockfile or vulnerability scanner is mistaken for proof that the executed dependency graph is safe.

**Distinguish:** trace source and dependency resolution → build inputs → artifact → distribution/launch. Check the actual installed/resolved versions and reachable vulnerable functionality against current primary advisories when relevant. Inspect permissions, secret scope, untrusted pull-request/input handling, artifact provenance and mutable references at the precise trust boundary. Prefer existing metadata and local artifact inspection before any network execution.

**Counterevidence:** a scanner alert may be unreachable, development-only or mitigated; explain rather than automatically downgrade it. Conversely, lack of a known advisory is not assurance. Floating dependencies can be an explicit policy; determine the actual consequence instead of declaring every unpinned tool Critical.

**Expansion:** follow shared release templates, inherited permissions and artifacts consumed downstream. Do not execute arbitrary install/build scripts, exfiltrate packages, add a security scanner or upgrade dependencies without appropriate authorization.

**Closure:** verify the artifact and privilege boundary implicated in the finding, not merely a changed manifest. A deterministic build proves reproducibility under its stated inputs, not correctness of those inputs.

This card is not a complete compliance or licensing review; inspect legal/distribution constraints only when explicitly applicable and use authoritative sources.
