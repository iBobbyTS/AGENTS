# Authority, authorization and data exposure

**Trigger:** multiple actors/tenants, alternate entry points, cached permissions, shared state, tool execution or sensitive output. Authentication alone does not establish ownership authorization.

**Hypothesis:** the decision is checked by one entry point but not at the effect owner; identity changes between validation and use; data escapes through a read/export/log/cache path despite write-side controls.

**Distinguish:** pick a concrete operation and actor/resource relationship. Trace principal, resource identity and permissions through the real path. Use authorized local fixtures to compare permitted, denied and stale/revoked cases; inspect actual side effects and reads. Verify alternate entry points and indirect objects where they share the same resource. Search exposure paths for the specific secret/data class rather than dumping all secrets into evidence.

**Counterevidence:** a genuinely enforced common boundary or trusted internal call contract can make repeated local checks unnecessary. “Internal” must have a real trust boundary, not just a comment. A single-user local tool does not automatically require tenancy, enterprise roles or internet threat assumptions.

**Expansion:** follow shared authorization helpers, resource loaders, caches and export surfaces. Report reachable harm with the actual attacker/actor capability. A source-derived defect can be confirmed without exploiting production. An uncertain high-impact path remains a risk/evidence gap, not suppressed noise and not a demonstrated breach.

**Do not add by default:** a new permissions framework, compliance standard, centralized policy engine or extra approval workflow. Establish the minimal guard at the correct owner first.
