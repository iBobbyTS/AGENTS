# System and Runtime Debugging

Load this playbook for process startup/exit, permissions, filesystem, environment, resource exhaustion, signals, service managers, host-specific behavior, or OS/runtime discrepancies.

## Capture the execution identity

Record the actual:

- OS/kernel and architecture;
- process binary/script path and version/hash;
- command line, working directory, user/group, umask;
- environment variables and PATH without secrets;
- locale, timezone, system clock;
- open files/sockets, resource limits, service-manager unit;
- container/cgroup limits if applicable;
- filesystem/mount type and permissions.

Interactive shell success does not prove the service manager, CI runner, launch agent, or container has the same identity or environment.

## Process lifecycle

For an unexpected exit capture:

- exit code or terminating signal;
- stderr/stdout and service-manager logs;
- core/crash/diagnostic report availability;
- restart policy and whether repeated restarts hide the first failure;
- last successful startup and recent binary/config/dependency changes.

For a hang capture all relevant stacks and wait states before restarting when safe. A restart restores service but usually destroys root-cause evidence.

## Linux observation checklist

Use the smallest relevant set; commands may require permissions.

```bash
ps -ef
ps -o pid,ppid,user,stat,etime,%cpu,%mem,rss,vsz,cmd -p <pid>
top -H -p <pid>
free -h
vmstat 1
iostat -xz 1
df -h
df -i
lsof -p <pid>
ss -lntup
cat /proc/<pid>/limits
cat /proc/<pid>/status
```

For systemd-managed services:

```bash
systemctl status <unit> --no-pager
journalctl -u <unit> --since "<time>" --until "<time>" --no-pager
systemctl show <unit>
```

Preserve timestamps and the first error. Broad journal or environment dumps may contain secrets.

Kernel/OOM evidence may appear in journal or `dmesg`; accessing it can require privilege. Correlate OOM events with cgroup/container limits rather than only host free memory.

## CPU and scheduling

Distinguish:

- sustained application CPU;
- busy retry/spin/livelock;
- blocked process with low CPU;
- scheduler pressure or CPU quota throttling;
- child process or thread consuming CPU;
- debug/logging overhead.

Capture a profile or stacks before optimizing. Load [performance.md](performance.md).

## Memory

Separate:

- application heap growth;
- native allocations;
- file/page cache;
- mapped files;
- child processes;
- container/cgroup accounting;
- leak versus legitimate retained working set;
- virtual address space versus resident memory.

Use runtime-specific heap/allocation tools where possible. Host RSS alone cannot identify the retaining object.

## Filesystem and permissions

Check the exact effective user and path components:

```bash
namei -l /path/to/file
ls -ld /path /path/to /path/to/file
stat /path/to/file
```

Inspect mount options, read-only state, case sensitivity, network filesystem behavior, symlinks, file ownership, ACLs, sandbox/container boundaries, available bytes and inodes.

Do not broadly apply `chmod 777`, change ownership recursively, or run as root as a repair. Identify the minimum intended access contract.

## Descriptors and sockets

For “too many open files,” connection leaks, or shutdown hangs:

- compare process descriptor count and limit;
- group descriptors by type/target;
- inspect socket states and peer endpoints;
- identify lifecycle that allocates without closing;
- verify whether pooled resources are bounded and released on exceptions/cancellation.

Raising limits may be operational mitigation, not proof that the leak is fixed.

## Environment and dynamic loading

Compare passing and failing executions for:

- PATH and interpreter/runtime selected;
- library search paths and loaded binary versions;
- architecture/ABI;
- config discovery and working directory;
- proxy and certificate environment;
- locale/encoding/timezone;
- feature flags and secrets presence (record presence/version, not values).

Use runtime loader diagnostics only in a controlled environment because output can be large and sensitive.

## cgroups and pressure

In containers or managed services inspect the effective cgroup, CPU/memory limits, throttling, OOM events, and pressure stall information. Host-level capacity can look healthy while a process is constrained by its cgroup.

## macOS host evidence

For native macOS applications, load [swift-macos-native.md](swift-macos-native.md). Useful system evidence may include:

- Console/unified logs;
- `log show`/`log stream` with a narrow predicate;
- Activity Monitor samples;
- `sample`, `spindump`, `vmmap`, `leaks`, and crash reports;
- launchd/SMAppService/XPC context;
- code-signing/sandbox logs.

Do not delete DerivedData, preferences, containers, or user data before preserving evidence and demonstrating that stale state is causal.

## Common causal chains

```text
service manager has different cwd → relative config path fails only as service
cgroup memory limit reached → kernel kills process while host still has free RAM
filesystem inode exhaustion → writes fail despite free bytes
descriptor leak → accept/open fails after long uptime → restart masks lifecycle bug
clock skew → certificates/tokens appear invalid → authentication fails only on one host
recursive permission workaround → service starts but exposes data beyond intended user
```

## Completion evidence

- exact execution identity and environment difference;
- exit/signal/wait/resource evidence at failure time;
- source repair verified under service-manager/container context;
- no broad privilege, permission, cache, or limit workaround substituted for causality.
