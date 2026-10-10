#!/usr/bin/env python3
"""Bounded local Git observations, NOT quality classification. Python stdlib only.

No source scripts, shell commands, network, checkout, index or durable-state writes.
Output includes filenames/commit subjects, not file bodies; review before sharing.
Exit 0 = complete observation, 2 = useful but incomplete, 1 = cannot identify repo.
"""
from __future__ import annotations
import argparse
import hashlib
import json
import os
from pathlib import Path
import stat
import subprocess
import tempfile
import time
from typing import Any


class ObservationError(Exception):
    pass


class Git:
    def __init__(self, root: Path, timeout: float = 5.0, cap: int = 262144):
        self.root, self.timeout, self.cap = root, timeout, cap

    def run(self, *args: str) -> tuple[int, bytes]:
        env = os.environ.copy()
        # Do not accidentally observe the caller's different checkout/index.
        for k in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_COMMON_DIR",
                  "GIT_OBJECT_DIRECTORY", "GIT_ALTERNATE_OBJECT_DIRECTORIES"):
            env.pop(k, None)
        env.update(GIT_OPTIONAL_LOCKS="0", GIT_TERMINAL_PROMPT="0",
                   GIT_NO_LAZY_FETCH="1", GIT_PAGER="cat")
        cmd = ["git", "--no-pager", "-c", "core.fsmonitor=false", "-c",
               "core.untrackedCache=false", "-C", str(self.root), *args]
        with tempfile.TemporaryFile() as out, tempfile.TemporaryFile() as err:
            try:
                proc = subprocess.Popen(cmd, stdout=out, stderr=err, env=env,
                                        stdin=subprocess.DEVNULL, shell=False)
            except OSError as exc:
                raise ObservationError("git unavailable: " + type(exc).__name__) from exc
            deadline = time.monotonic() + self.timeout
            failure = None
            while proc.poll() is None:
                if time.monotonic() > deadline:
                    failure = "git observation timed out"
                    break
                if os.fstat(out.fileno()).st_size + os.fstat(err.fileno()).st_size > self.cap:
                    failure = "git observation exceeded output limit"
                    break
                time.sleep(.01)
            if failure:
                proc.kill()
            proc.wait()
            out.seek(0)
            data = out.read(self.cap + 1)
            if failure or len(data) > self.cap or os.fstat(err.fileno()).st_size > self.cap:
                raise ObservationError(failure or "git observation exceeded output limit")
            return proc.returncode, data

    def require(self, *args: str) -> bytes:
        code, data = self.run(*args)
        if code:
            # Avoid dumping credentials or attacker-controlled stderr into reports.
            raise ObservationError("git command failed: " + args[0])
        return data


def text(data: bytes) -> str:
    return data.decode("utf-8", "surrogateescape")


def parse_status(raw: bytes) -> list[dict[str, str]]:
    """Parse porcelain v1 -z, including rename destination/origin, without shell splitting."""
    fields = raw.split(b"\0")
    if fields[-1] != b"":
        raise ObservationError("incomplete status record")
    fields.pop()
    results = []
    i = 0
    while i < len(fields):
        item = fields[i]; i += 1
        if len(item) < 4 or item[2:3] != b" ":
            raise ObservationError("invalid status record")
        code = text(item[:2])
        record = {"status": code, "path": text(item[3:])}
        if "R" in code or "C" in code:
            if i >= len(fields):
                raise ObservationError("missing rename source")
            record["original_path"] = text(fields[i]); i += 1
        results.append(record)
    return results


def fingerprint(root: Path, records: list[dict[str, str]], limit: int,
                per_file: int = 1048576, total_limit: int = 16777216) -> tuple[str | None, list[str]]:
    """Hash dirty contents to detect edits at unchanged HEAD/status; never follow symlinks."""
    problems: list[str] = []
    if len(records) > limit:
        return None, ["dirty file count exceeds fingerprint limit"]
    digest = hashlib.sha256()
    total = 0
    for rec in records:
        rel = rec["path"]
        digest.update(json.dumps(rec, sort_keys=True, ensure_ascii=True).encode())
        p = root / rel
        try:
            # Resolve only for containment; symlink content itself is not read.
            if p.is_symlink():
                digest.update(b"symlink:" + os.fsencode(os.readlink(p)))
                continue
            if not p.exists():
                digest.update(b"missing")
                continue
            p.resolve().relative_to(root.resolve())
            before = p.lstat()
            if not stat.S_ISREG(before.st_mode):
                problems.append("non-regular dirty entry: " + rel); continue
            if before.st_size > per_file or total + before.st_size > total_limit:
                problems.append("dirty content exceeds fingerprint limit: " + rel); continue
            flags = os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_BINARY", 0)
            fd = os.open(p, flags)
            with os.fdopen(fd, "rb") as f:
                actual = os.fstat(f.fileno())
                if (actual.st_dev, actual.st_ino) != (before.st_dev, before.st_ino):
                    problems.append("dirty file changed while opening: " + rel); continue
                data = f.read(per_file + 1)
                after = os.fstat(f.fileno())
            total += len(data)
            if len(data) > per_file or (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
                problems.append("dirty file changed while hashing: " + rel); continue
            digest.update(hashlib.sha256(data).digest())
        except (OSError, ValueError):
            problems.append("dirty entry unreadable/outside root: " + rel)
    return (None if problems else digest.hexdigest()), problems


def collect(repo: Path, base: str | None = None, max_files: int = 120,
            timeout: float = 5.0, output_cap: int = 262144) -> dict[str, Any]:
    if max_files < 1 or timeout <= 0 or output_cap < 64:
        raise ValueError("positive limits required (output_cap >= 64)")
    g = Git(repo.expanduser().resolve(), timeout, output_cap)
    root = Path(text(g.require("rev-parse", "--show-toplevel")).removesuffix("\n")).resolve()
    g.root = root
    issues: list[str] = []
    packet: dict[str, Any] = {"schema": "quality-observation/1", "repo": str(root),
        "kind": "observations-not-verdict", "issues": issues,
        "observed_at_utc": time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime())}
    head = text(g.require("rev-parse", "--verify", "HEAD^{commit}")).strip()
    packet["head"] = head
    branch_rc, branch = g.run("symbolic-ref", "--quiet", "--short", "HEAD")
    packet["branch"] = text(branch).strip() if branch_rc == 0 else "DETACHED"
    if branch_rc not in (0, 1):
        issues.append("branch identity could not be established")
    shallow = text(g.require("rev-parse", "--is-shallow-repository")).strip() == "true"
    packet["shallow"] = shallow
    packet["history"] = {"base_requested": base, "base": None,
                         "ancestry": "unknown", "commit_count": None, "paths": []}
    if shallow:
        issues.append("shallow history; coverage outside available graph is unknown")
    if base:
        try:
            resolved = text(g.require("rev-parse", "--verify", "--end-of-options", base + "^{commit}")).strip()
            packet["history"]["base"] = resolved
            rc, _ = g.run("merge-base", "--is-ancestor", resolved, head)
            if rc == 0:
                packet["history"]["ancestry"] = "ancestor"
                packet["history"]["commit_count"] = int(text(g.require("rev-list", "--count", resolved + ".." + head)))
                paths = g.require("diff", "--no-ext-diff", "--no-textconv", "--no-renames", "--name-only", "-z", resolved, head, "--")
                names = [text(p) for p in paths.split(b"\0") if p]
                packet["history"]["paths"] = names[:max_files]
                packet["history"]["path_count"] = len(names)
                if len(names) > max_files:
                    issues.append("historical path list truncated")
            elif rc == 1:
                packet["history"]["ancestry"] = "not-ancestor"
                issues.append("base is not an ancestor; no since-audit delta inferred")
            else:
                raise ObservationError("ancestry unavailable")
        except (ObservationError, ValueError) as exc:
            issues.append("history unavailable: " + str(exc))
    else:
        issues.append("no verified baseline supplied; history delta unknown")
    try:
        # Subjects are merely leads; a fixed sample is explicitly not full history.
        packet["recent_subjects_sample"] = text(g.require("log", "-8", "--format=%h %s", head, "--")).splitlines()
        raw = g.require("status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=none")
        records = parse_status(raw)
        staged = g.require("diff", "--cached", "--raw", "--no-abbrev", "-z", "--no-renames",
                           "--no-ext-diff", "--no-textconv", head, "--")
        index_fp = hashlib.sha256(staged).hexdigest()
        packet["index_fingerprint"] = index_fp
        packet["dirty"] = records[:max_files]
        packet["dirty_count"] = len(records)
        if len(records) > max_files:
            issues.append("dirty path list truncated")
        fp, trouble = fingerprint(root, records, max_files)
        issues.extend(trouble)
        packet["dirty_fingerprint"] = hashlib.sha256((fp + index_fp).encode()).hexdigest() if fp else None
        # Check again for mutations during observation, including content-only edits.
        end_head = text(g.require("rev-parse", "--verify", "HEAD^{commit}")).strip()
        end_raw = g.require("status", "--porcelain=v1", "-z", "--untracked-files=all", "--ignore-submodules=none")
        end_fp, trouble = fingerprint(root, parse_status(end_raw), max_files)
        issues.extend(trouble)
        end_staged = g.require("diff", "--cached", "--raw", "--no-abbrev", "-z", "--no-renames",
                               "--no-ext-diff", "--no-textconv", end_head, "--")
        end_rc, end_branch = g.run("symbolic-ref", "--quiet", "--short", "HEAD")
        stable = (head == end_head and raw == end_raw and fp is not None and fp == end_fp
                  and staged == end_staged and branch_rc == end_rc and branch == end_branch)
        packet["stable_during_observation"] = stable
        if not stable:
            issues.append("snapshot changed or stability could not be established")
    except ObservationError as exc:
        issues.append("working snapshot unavailable: " + str(exc))
        packet["stable_during_observation"] = False
    if (root / ".gitmodules").exists():
        issues.append("submodule status is a hint; nested content is not fully fingerprinted")
    packet["observations_complete"] = not issues
    packet["limits"] = {"max_paths_per_list": max_files, "git_command_seconds": timeout,
                         "git_output_bytes": output_cap, "dirty_file_bytes": 1048576,
                         "dirty_total_bytes": 16777216,
                         "not_collected": "ignored files, runtime state, CI results, incidents, external advisories, audit coverage, semantics"}
    return packet


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("repo", type=Path)
    parser.add_argument("--base", help="verified collection/audit revision; no default guess")
    parser.add_argument("--max-files", type=int, default=120)
    parser.add_argument("--timeout", type=float, default=5.0)
    parser.add_argument("--output-cap", type=int, default=262144)
    a = parser.parse_args()
    try:
        packet = collect(a.repo, a.base, a.max_files, a.timeout, a.output_cap)
    except (ObservationError, OSError, ValueError) as exc:
        print(json.dumps({"schema": "quality-observation/1", "repo": str(a.repo),
                          "observations_complete": False, "error": str(exc)}, ensure_ascii=True))
        return 1
    print(json.dumps(packet, ensure_ascii=True, indent=2))
    return 0 if packet["observations_complete"] else 2


if __name__ == "__main__":
    raise SystemExit(main())
