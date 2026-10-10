# Profile lifecycle

Use a stable Markdown release/deployment model, preferably in the project's existing docs (suggested `docs/quality/RELEASE-PROFILE.md`). The [template](../templates/PROFILE.md) is a prompt for facts, not a form requiring every subsection. Link existing deploy/runbook/config documentation rather than copying it. Commands are references, not automatically executable instructions.

On first use, inspect actual package/config/build/install/launch sources, current usage commitments and user permissions. Mark facts observed, user-confirmed or unknown; associate consequential claims with a file/record that can be rechecked. Draft local evidence during preflight; committing or changing the project profile follows the project's edit authority. No production access is implied by initializing a profile.

Stable: product type, supported consumer/environment families, topology and ownership, release method, persistent/user data, coexistence promises, observation/recovery model, relevant permissions and evidence locations.
Dynamic: current deployed/candidate revision, exact artifacts/checksums, migration/change set, environment readings, current check results, actual backup freshness, this release's accepted risks and manual sequence. Keep these in the run, not the profile. Historical known risk should point to the authoritative GA/incident record, not grow a copied risk database.

Every run performs a small drift check against changed manifests/config/deploy files and actual target evidence. Changed runtime minima, permissions, distribution channels, certificates/signing requirements or new local persistence matter even without an architectural overhaul. Verify affected facts and propose a minimal patch; don't blindly trust an old “no state” assertion, and don't rewrite unaffected sections.

Profile changes do not invalidate every previous check. Invalidate conclusions depending on changed facts. An unresolved material topology/consumer/target mismatch prevents the relevant readiness claim; a corrected pathname need not block other checks. User business requirements outrank a stale profile; expose conflicting evidence rather than silently picking a convenient version.

Three starting examples are provided in [examples](../templates/EXAMPLES.md). They are fictional patterns, not discovered facts about the user's repositories and not mandatory architecture recommendations.
