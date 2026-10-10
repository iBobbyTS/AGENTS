# Fictional minimal profile patterns

These illustrate scope selection, not observations of the user's projects. Do not copy unsupported facts.

## Static documentation site, manual upload, no owned persistent user data

Consumers: supported browsers, existing public URLs and cached pages. Delivery: local build directory manually uploaded to an existing static host; no CI assumed. Preserve important paths, relative assets, cache/version behavior and intended access visibility. Evidence: inspect actual generated output, representative old URLs/new pages and hosting configuration. Recovery: retain prior artifact and a documented manual replacement path; don't claim remote cache invalidation was tested locally. A DB migration section is genuinely inapplicable. Secrets may still leak through generated output.

## CLI/library, manual package publication

Consumers: declared runtime/OS versions and actual import/CLI contract. Delivery: package contents and entry metadata from the real packaging process, version/channel manually selected. Evidence: inspect pack scripts first; consume the actual archive in an authorized disposable location, not merely import the source tree. Support/upgrade promises determine compatibility scope. Recovery: withdrawal/deprecation or corrected next version may be feasible; already-downloaded packages cannot necessarily be recalled. A single “currently deployed SHA” is not the whole baseline.

## Desktop utility, manual binary distribution

Consumers: supported OS/runtime and upgrades from supported installed versions. State: user documents, settings and plugin/cache state whose loss matters. Delivery: binary/installer and signing/permissions model appropriate to actual distribution. Evidence: artifact startup, representative supported upgrade and preservation of meaningful settings/user data in a disposable environment. Recovery: prior binary may not read an upgraded file format; record real downgrade/forward repair limits. No server, CI or database assumed.

A server profile uses the same model with real components, availability expectations, environment/state ownership and reachable version coexistence. Add SQL-specific questions only if that transition actually touches SQL behavior.
