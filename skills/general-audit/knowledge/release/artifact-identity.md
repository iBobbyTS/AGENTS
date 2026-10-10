# Source, artifact and recipient identity

**Trigger:** installation/distribution/startup claims, generated packages/images, multiple worktrees/channels, or evidence reused from a different build.

**Hypothesis:** reviewed source is not the bytes consumed; packaging omits a required file or includes sensitive/unintended material; the wrong target/channel is selected; a mutable tag hides what was tested. Source-only tests can miss packaging and entry-point errors.

**Distinguish:** bind source/dirty state → build inputs/process → concrete artifact → actual install/import/launch entry → intended recipients/environment. Inspect real package contents and consumer entry where safe. For a source-only early preflight, state which artifact assertions remain unverified. Exact identity may use a digest, immutable version or another project-appropriate locator; no mandatory provenance service.

**Counterevidence:** a statically copied single file need not have a container pipeline or signed attestation. An intentional rebuild is legitimate if the relevant inputs/identity and supporting evidence are reconciled. Provenance can establish origin without proving semantic correctness.

**Expansion:** inspect the implicated packaging/distribution path, not every build-system feature. Use [supply chain](../mechanisms/supply-chain.md) for trust/adversarial dependency questions, [population](../evidence/population.md) for executed coverage and [release/shell](../technology/release-shell.md) for argument/hook semantics. Do not publish a package to validate a preflight.

**Closure:** observations refer to the actual candidate and intended recipient, with clear missing artifact evidence and invalidation conditions.
