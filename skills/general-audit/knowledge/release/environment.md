# Environment, configuration and effective privilege

**Trigger:** first install/start, new runtime requirements, config/secret interface changes, permission changes, optional dependencies or environment-specific packaging.

**Hypothesis:** a successful developer run depends on an implicit tool/path/config/cache/account privilege unavailable to supported users; the actual environment silently selects different behavior; unsupported defaults expose data or disable required controls.

**Distinguish:** inspect the real launch/install/consumer entry, declared minimum runtime and effective config/permission requirements. Compare supported target facts with tested facts, including working directory, paths, architecture and optional services only where they affect behavior. Check required configuration presence/meaning without printing secret values. Prefer a representative clean disposable consumer environment over the author's already-populated checkout when possible.

**Counterevidence:** one explicitly supported platform is enough when the product doesn't promise portability. A required external service may be a legitimate prerequisite. Absence of CI, containers or a secret-management platform isn't itself a defect.

**Expansion:** follow the specific implicit dependency and user-visible failure. Do not install system software, fetch dependencies, query live secrets or elevate privileges to fill missing evidence. Changed runtime/signing/permissions can invalidate a profile even if module architecture is unchanged.

**Closure:** the real entry can operate or fail safely with the stated supported environment, or the required target fact remains explicit. Operational detection/recovery is owned by [recovery](../mechanisms/recovery.md), not a second checklist here.
