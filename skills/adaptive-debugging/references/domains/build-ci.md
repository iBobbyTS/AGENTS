# Build and CI Debugging

Load this playbook for compiler/linker/bundler/dependency failures, local-versus-CI differences, GitHub Actions failures, packaging issues, release-only behavior, or non-reproducible build artifacts.

## Identify the exact build

Record:

- commit SHA and whether the working tree differs;
- event type, ref, base/head SHA and merge commit behavior;
- workflow/job/step/matrix values and runner image/architecture;
- shell, working directory, environment and permissions;
- toolchain/compiler/runtime/package-manager versions;
- lockfile, dependency cache key and restored cache identity;
- build flags/configuration/feature flags;
- generated files, artifacts, image/package digest;
- first failing command and its full exit status/output.

Do not debug “the latest branch” when CI executed a specific SHA or synthetic merge commit.

## Reproduce the command, then the environment

1. Run the exact failing command from the same directory with the same build mode.
2. Match toolchain and lockfile behavior.
3. Match environment variables by presence/version, not secret value.
4. Match OS, architecture, filesystem case sensitivity, locale/timezone, shell and permissions.
5. Match service dependencies and network restrictions.
6. If local reproduction still passes, use the runner/container/VM image or collect boundary evidence in CI.

Avoid upgrading dependencies or regenerating all lockfiles before isolating the first failure.

## GitHub Actions workflow

Correlate:

```text
workflow run → job/matrix → step → shell command → artifact/log
```

Check:

- trigger/event filters and conditional `if` expressions;
- checkout ref, fetch depth, submodules and LFS;
- `permissions` and token behavior, especially forked pull requests;
- secrets availability and environment protection;
- matrix include/exclude and fail-fast behavior;
- job/step outputs, quoting, multiline values and environment files;
- working directory and shell differences;
- service container readiness;
- cache key, restore keys and stale generated output;
- artifact upload/download names and paths;
- concurrency cancellation of older runs.

Enable runner/step debug logging only for a controlled rerun and review logs for secrets. Preserve the failing run before rerunning.

A rerun usually uses the same commit/ref context; verify the run metadata rather than assuming current branch changes are included.

## Compiler and linker localization

- Preserve the **first** diagnostic in dependency order; later errors may cascade.
- Confirm the actual source file, generated code and include/module search paths.
- Inspect architecture/ABI, deployment target, language mode, feature flags and conditional compilation.
- Compare debug/release, incremental/clean and local/CI builds as controlled variables.
- For link failures, identify which object/library should define the missing/duplicate symbol and inspect the linked artifact set.
- For native dependencies, confirm platform slice and runtime library availability.

A clean build can establish stale incremental state, but deleting all caches is not a permanent repair. Identify the missing dependency declaration or invalidation rule.

## Dependency resolution

Check:

- lockfile committed and honored in frozen/immutable mode;
- registry/proxy/authentication and package availability;
- platform-conditional optional/native dependencies;
- duplicate major versions or peer constraints;
- toolchain version expected by the lockfile;
- checksum/integrity or supply-chain policy;
- generated code/schema version compatibility.

Record the exact resolution graph/diff. “Install again” without explaining why resolution differed is not completion.

## Cache diagnosis

Use a no-cache build/rerun as a comparison only. If it passes:

- identify the cache content that should have been invalidated;
- inspect key inputs such as lockfile, compiler version, architecture, build flags and source hashes;
- separate dependency cache from build output cache;
- verify restore fallback does not load incompatible artifacts;
- repair keying/dependency declarations rather than disabling all caching.

## Release, package, and artifact parity

Test the exact produced artifact, not a rebuilt local approximation. Preserve:

- binary/package/image digest;
- manifest/metadata;
- source maps/dSYMs/debug symbols;
- signatures/entitlements/notarization logs where applicable;
- deployment configuration and migration bundle.

For macOS/Xcode distribution load [macos-signing-sandbox.md](macos-signing-sandbox.md) and [swift-macos-native.md](swift-macos-native.md).

## Common causal chains

```text
CI tests synthetic merge SHA → local branch lacks merge conflict → local passes
cache key omits toolchain version → incompatible object reused → linker fails intermittently by runner image
fork PR lacks secret/permission → integration step returns auth error → mistaken application regression
case-insensitive local filesystem → import casing passes locally → Linux runner fails
release optimizer exposes undefined behavior/race → debug tests pass → packaged binary crashes
stale generated client/schema → build succeeds → runtime contract fails
```

## Completion evidence

- exact SHA/job/step/command and first causal diagnostic;
- local or controlled CI reproduction with one changed variable;
- cache/dependency/toolchain cause demonstrated, not merely cleared;
- exact artifact retested under the original environment/distribution path;
- debug logging disabled and sensitive artifacts cleaned up.
