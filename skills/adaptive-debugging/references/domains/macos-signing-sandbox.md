# macOS Signing, Notarization, Gatekeeper, and Sandbox Debugging

Load this playbook when a macOS app/helper/XPC service works from Xcode but fails after archive/export/download/install, is blocked or damaged according to Gatekeeper, fails notarization, has invalid signatures, loses permissions under hardened runtime or App Sandbox, or has entitlement/team/bundle-ID mismatches.

These are distinct layers. Do not treat “signed,” “notarized,” “Gatekeeper accepted,” and “sandbox access allowed” as synonyms.

## Preserve the exact distribution chain

Capture the actual artifact and every transformation:

```text
archive/build
→ export
→ nested code signing
→ outer app/package signing
→ notarization submission/result
→ stapling
→ DMG/PKG/ZIP packaging
→ upload/download or installer
→ quarantine/Gatekeeper assessment
→ launch/runtime sandbox behavior
```

Record:

- Xcode/toolchain and build configuration;
- app version/build, bundle ID and Team ID;
- signing identities/certificate chain and provisioning profile if used;
- hardened runtime and actual entitlements for app plus every nested executable;
- artifact hash before/after packaging;
- notarization submission ID and log;
- quarantine attribute and how the user obtained the artifact;
- macOS version/architecture and clean-machine/user result.

Do not rebuild, re-sign, strip, modify, or repackage the failed artifact before preserving it. Any post-sign mutation can invalidate the signature; re-signing after notarization/stapling changes what was assessed.

## Verify signatures and metadata

Inspect the top-level app:

```bash
codesign --verify --strict --verbose=4 "MyApp.app"
codesign -dv --verbose=4 "MyApp.app"
codesign -d --entitlements :- "MyApp.app"
codesign -dr - "MyApp.app"
```

Enumerate and inspect every nested code object independently:

- `Contents/Frameworks`;
- `Contents/XPCServices`;
- `Contents/PlugIns`;
- helper/login-item executables;
- nested apps, frameworks, dylibs and command tools.

Use recursive/deep verification only as supplementary evidence. Do **not** use `codesign --deep` as a signing strategy: it can apply or preserve the wrong options/entitlements and obscure which nested component is incorrect. Sign nested code inside-out according to its own contract, then sign the containing app.

Check:

- designated requirement, TeamIdentifier, bundle identifier;
- timestamp and hardened-runtime flags;
- architecture slices and nested-code placement;
- entitlements actually embedded in the signature, not only the `.entitlements` source file;
- `get-task-allow`, library validation exceptions and other debug-only entitlements;
- whether a tool modified executable resources after signing.

## Notarization

Preserve and read the notarization log rather than submitting repeatedly:

```bash
xcrun notarytool info <submission-id> --keychain-profile <profile>
xcrun notarytool log <submission-id> --keychain-profile <profile>
xcrun stapler validate "MyApp.app"
```

When a controlled resubmission is necessary:

```bash
xcrun notarytool submit "MyApp.zip" --keychain-profile <profile> --wait
```

Verify the submitted container contains the same signed artifact later distributed. Notarization acceptance does not prove the final package was unchanged, stapled correctly, quarantined, or accepted by Gatekeeper on the target system.

Do not weaken hardened runtime or remove problematic nested code blindly to obtain an “Accepted” result; diagnose the logged path and signing/runtime contract.

## Gatekeeper and quarantine

Inspect the actual downloaded artifact:

```bash
xattr -p com.apple.quarantine "MyApp.app" 2>/dev/null
xattr -lr "MyApp.app"
spctl --assess --type execute --verbose=4 "MyApp.app"
```

Treat `spctl` as supplementary diagnostic information, not a complete simulation of user launch policy. Test the real distribution path on a clean supported macOS account/machine with quarantine present.

Do not remove `com.apple.quarantine` as the product fix. Removing quarantine only bypasses the policy path you need to validate.

Correlate Gatekeeper messages with unified logs around the attempted launch. Distinguish:

- unsigned/invalid signature;
- unnotarized or unstapled/offline-ticket behavior;
- damaged/modified after signing;
- blocked nested code/library;
- revoked/expired certificate trust issue;
- unsupported architecture or launch failure misreported as policy failure.

## Hardened runtime and library loading

For launch/crash only in hardened release builds inspect:

- code-signing status of every loaded framework/dylib/plugin;
- library validation and Team ID compatibility;
- JIT, unsigned executable memory, debugger, DYLD environment and injection-related entitlements;
- plugin/update framework behavior;
- architecture slices and load paths;
- whether debug builds relied on permissions unavailable in signed release.

Do not add broad exceptions such as disabled library validation unless the product architecture truly requires them and the security trade-off is approved.

## App Sandbox

### Prove the denial boundary

Capture unified/Console logs around the operation and look for sandbox denial records. Correlate process, path/resource, operation and entitlement.

Compare:

- actual signed entitlements;
- requested resource and resolved path/endpoint;
- app container and group container;
- user-selected file/folder flow;
- security-scoped bookmark creation, persistence, resolution and access lifetime;
- network client/server entitlement;
- automation/Apple Events, camera/microphone/photos or other privacy permission;
- XPC/helper entitlement and Team ID relationship.

A POSIX “permission denied” can originate from filesystem ACLs, TCC privacy, App Sandbox, hardened runtime, or container path—not one generic permission system.

### File access and security-scoped bookmarks

Trace:

```text
user grants access
→ URL/bookmark created
→ bookmark persisted
→ resolved on later launch
→ startAccessingSecurityScopedResource
→ operation
→ stopAccessingSecurityScopedResource
```

Check stale bookmarks, moved volumes/files, app-group storage, access balancing, and whether a helper/XPC process receives an authorization it is allowed to use. Do not replace user-granted access with a broad filesystem entitlement.

### Entitlement discipline

- Inspect entitlements in the signed artifact for every executable.
- Add only the minimum capability required by the product contract.
- Keep bundle IDs, application groups, keychain groups and Team ID prefixes consistent.
- Do not disable the sandbox or add temporary broad entitlements as the permanent repair.
- Re-test a clean install/user because existing consent and container state can hide missing setup.

## XPC services, helpers, login items, and launch agents

Verify:

- nested location and bundle structure;
- signature/Team ID/designated requirement of both client and service;
- actual version registered/installed versus bundled version;
- sandbox and mach service/application-group entitlements;
- protocol compatibility and interruption/invalidation logs;
- launchd/SMAppService registration state;
- helper update/replacement path and authorization.

A stale helper may survive app replacement. Preserve its path, hash, signature and logs before unregistering or deleting it.

## Packaging and post-processing

Compare hashes/signatures before and after:

- ZIP creation/extraction;
- DMG construction;
- PKG scripts/installation;
- auto-update framework packaging;
- CDN/server transformation;
- antivirus or enterprise tooling;
- user copy/move/translocation behavior.

Ensure packaging preserves symlinks, permissions, extended attributes as intended and does not mutate signed resources. Test the exact upload/download artifact.

## Common causal chains

```text
nested helper signed with wrong Team ID → outer app verifies locally → helper rejected at launch
artifact modified after notarization → notary result remains Accepted → downloaded app signature is invalid
source entitlements file is correct → export step signs different entitlements → sandbox denial only in release
security-scoped bookmark not persisted/resolved correctly → first session works → relaunch loses file access
stale installed login item → new app talks to old protocol → Xcode run passes but installed app fails
quarantine removed during testing → Gatekeeper path never exercised → users see blocked/damaged message
```

## Completion evidence

- exact distributed artifact hash and transformation chain;
- signature and entitlements for app and every relevant nested executable;
- notarization log/ticket evidence and real quarantined launch test;
- sandbox denial or access trace at the first failing resource boundary;
- clean-machine/user verification with intended hardened runtime and sandbox intact;
- no `codesign --deep` signing, quarantine removal, broad entitlement, disabled validation, or sandbox removal presented as the repair.
