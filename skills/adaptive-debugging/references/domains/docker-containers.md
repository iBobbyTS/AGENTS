# Docker and Container Debugging

Load this playbook for image/build problems, containers that exit or become unhealthy, Compose discrepancies, volume/permission issues, container networking, architecture/platform mismatch, or resource-limit behavior.

## Identify the exact artifact and runtime

Record:

- image name, immutable digest, platform/architecture, build source commit;
- container ID, created/start/finish time, restart count;
- entrypoint, command, working directory, user;
- environment key names and non-secret configuration versions;
- mounts/volumes and network attachments;
- published ports and health-check definition;
- exit code, signal, OOMKilled state, health output;
- Docker Engine/Compose version and host OS.

Tags such as `latest` are not evidence of identical images. Compare digests.

## Inspect before restarting or deleting

```bash
docker ps -a --no-trunc
docker inspect <container>
docker logs --timestamps <container>
docker image inspect <image-or-digest>
docker stats --no-stream <container>
```

For Compose:

```bash
docker compose config
docker compose ps
docker compose logs --timestamps <service>
```

`docker inspect` contains environment and labels that may include secrets. Redact artifacts.

Preserve health-check output, exit state, and logs before a restart. Do not begin with `docker system prune`, image deletion, or volume removal.

## Container process and startup

Check:

- whether PID 1 is the intended process and forwards signals/reaps children;
- shell-form versus exec-form entrypoint behavior;
- actual working directory and file paths;
- executable architecture and dynamic libraries;
- effective user and write permissions;
- startup dependency readiness versus mere process existence;
- whether the container exits successfully because the foreground process ended;
- whether restart policy hides a crash loop.

Reproduce the exact entrypoint/command, not an interactive shell with different environment and user.

## Health checks

Inspect the recent health log and compare the health command with real traffic:

- Is it executed inside the container namespace?
- Does it use `localhost` while users enter through a proxy or published port?
- Does it validate dependencies or only process liveness?
- Are timeout, interval, start period, and retries appropriate to the measured startup contract?
- Does the health command itself exist and have the right permissions?

A healthy check does not prove external reachability or full application correctness.

## Networking

Map each namespace boundary:

```text
client/host
→ published host port
→ container network/IP
→ listening address/port
→ downstream service name/network
```

Check:

- process listens on `0.0.0.0`/intended interface rather than only container loopback;
- service-name DNS from the calling container;
- both containers share the intended Compose network;
- exposed versus published ports;
- host networking differences on Linux versus Docker Desktop;
- proxy/NO_PROXY and certificate trust inside the image;
- IPv4/IPv6 and MTU/VPN behavior.

Use [network.md](network.md) for protocol evidence.

## Mounts, volumes, and permissions

Inspect source/destination, type, read-only flag, propagation, ownership, SELinux/AppArmor labels where applicable, and host path existence.

Common traps:

- bind mount hides files copied into the image;
- host UID/GID differs from image user;
- named volume contains schema/config from an older version;
- relative Compose path resolves from a different project directory;
- Docker Desktop file-sharing/permissions differ from Linux;
- read-only root filesystem needs explicit writable paths.

Do not delete a volume to make the symptom disappear before identifying and preserving its data/state.

## Build and image differences

Use a controlled rebuild and inspect build output:

```bash
docker build --progress=plain --no-cache -t debug-image .
```

`--no-cache` is a diagnostic comparison, not a permanent routine fix. Compare:

- build context and `.dockerignore`;
- multi-stage source/target stage;
- build args versus runtime env;
- lockfile and package-manager mode;
- platform/architecture and native dependencies;
- file ownership/mode copied into image;
- base image digest and repository availability;
- secret mounts versus leaked build arguments/layers.

If a clean build passes and cached build fails, localize the invalid cache dependency rather than always disabling cache.

## Resource constraints

Compare host metrics with effective container limits:

- memory limit and OOM state;
- CPU quota/throttling;
- process/file descriptor limits;
- disk/overlay storage and inode availability;
- shared-memory size;
- health/startup time under constrained resources.

Load system/performance playbooks for deeper evidence.

## Common causal chains

```text
bind mount hides packaged config → interactive image test passes → Compose startup fails
image tag reused across hosts → different digest → environment-specific behavior
process listens on 127.0.0.1 → internal health passes → published port fails
container CA store missing intermediate/root → TLS fails only in image
old named volume schema → new application starts then crashes → deleting volume masks migration defect
CPU quota throttling → health timeout → restart loop under load
```

## Completion evidence

- immutable image digest and exact container configuration;
- first failing boundary inside image/process/network/mount/resource path;
- verification from a clean container using original Compose/deployment semantics;
- persistent data preserved and migration path tested;
- no prune, volume deletion, broad root privileges, or cache disablement used as the unproven final fix.
