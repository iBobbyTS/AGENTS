#!/usr/bin/env python3
"""Inventory, then archive a completed task and discard explicit generated dispatch views.

Archive layout: .agent-work/archive/{YYYYMMDD-HHMM_feature-id}/ holding the completed
PLAN-FULL plus caller-verified evidence (requirements, final state, review reports,
handoffs); rebuildable dispatch views (PLAN/section extracts, TASK packets) are discarded.

This helper does not schedule agents or prove completion. The caller must have verified real
completion, stopped owned actors and checked references before declaring a view unreferenced.
"""
from __future__ import annotations

import argparse
import json
import os
from pathlib import Path
import re
import tempfile
import time


class ArchiveError(ValueError):
    pass


def plain_path(path: Path) -> None:
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise ArchiveError(f'SYMLINK_NOT_ALLOWED: {candidate}')


GENERATED_VIEW = re.compile(r'PLAN\.md|sections/S[0-9]+(?:\.[A-Z]+)?-(?:PLAN|CONTRACT|TASK)\.md')
FEATURE_ID = re.compile(r'[a-z0-9][a-z0-9-]{0,63}')


def collect_entries(work: Path, values: list[str], kind: str, pattern: re.Pattern | None = None) -> list[Path]:
    selected: list[Path] = []
    for value in values:
        rel = Path(value)
        # No general-purpose cleanup mechanism. Views are conventional generated plan dispatch files.
        if pattern is not None and not pattern.fullmatch(rel.as_posix()):
            raise ArchiveError(f'NOT_A_GENERATED_PLAN_VIEW: {value}')
        candidate = work / rel
        plain_path(candidate)
        if candidate in selected:
            raise ArchiveError(f'DUPLICATE_ENTRY: {value}')
        if not candidate.exists():
            raise ArchiveError(f'{kind}_MISSING: {value}')
        selected.append(candidate)
    return selected


def prepare(repo: Path, feature_id: str, keeps: list[str], views: list[str]):
    if not FEATURE_ID.fullmatch(feature_id):
        raise ArchiveError('FEATURE_ID_REQUIRED: lowercase letters, digits and hyphens')
    repo = Path(os.path.abspath(repo.expanduser()))
    work = repo / '.agent-work'
    full = work / 'PLAN-FULL.md'
    destination = work / 'archive' / f"{time.strftime('%Y%m%d-%H%M')}_{feature_id}"
    for path in (work, full, destination, work / 'tmp'):
        plain_path(path)
    if not full.is_file():
        raise ArchiveError('ACTIVE_PLAN_FULL_REQUIRED')
    if destination.exists():
        raise ArchiveError('ARCHIVE_ALREADY_EXISTS: never overwrite a completed task')
    if not re.search(r'^- Status:\s*COMPLETED\s*$', full.read_text(), re.M):
        raise ArchiveError('COMPLETED_PLAN_REQUIRED: not a plan-only handoff or blocked task')
    keep_paths = collect_entries(work, keeps, 'KEEP')
    view_paths = collect_entries(work, views, 'VIEW', GENERATED_VIEW)
    inventory = []
    for path, action, status in (
        *[(full, 'archive_authority', 'CALLER_VERIFIED_CLOSED')],
        *[(p, 'archive_evidence', 'CALLER_VERIFIED_EVIDENCE') for p in keep_paths],
        *[(p, 'discard_generated_view', 'CALLER_DECLARED_UNREFERENCED') for p in view_paths],
    ):
        inventory.append({'path': str(path), 'type': 'dir' if path.is_dir() else 'file',
                          'bytes': None if path.is_dir() else path.stat().st_size,
                          'task': feature_id, 'reference_status': status, 'action': action})
    return full, destination, keep_paths, view_paths, inventory


def prune_empty(destination: Path) -> None:
    for child in sorted(destination.rglob('*'), reverse=True):
        if child.is_dir():
            child.rmdir()  # raises on non-empty: intended, partial archives stay visible
    destination.rmdir()


def archive(repo: Path, feature_id: str, keeps: list[str], views: list[str], apply: bool = False) -> dict:
    full, destination, keep_paths, view_paths, inventory = prepare(repo, feature_id, keeps, views)
    result = {'applied': False, 'archive': str(destination), 'inventory': inventory,
              'reference_validation': 'CALLER_RESPONSIBILITY_NOT_PROVEN_BY_THIS_HELPER'}
    if not apply:
        return result
    work = full.parent
    (work / 'tmp').mkdir(exist_ok=True)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.mkdir()  # refuses a concurrent existing leaf rather than overwriting it
    placed: list[Path] = []
    try:
        with tempfile.TemporaryDirectory(prefix=f'archive-{feature_id}-', dir=work / 'tmp') as temporary:
            held: list[tuple[Path, Path]] = []
            try:
                for view in view_paths:
                    stash = Path(temporary) / f'view-{len(held)}-{view.name}'
                    os.replace(view, stash)
                    held.append((stash, view))
                for path in [full, *keep_paths]:
                    target = destination / path.relative_to(work)
                    target.parent.mkdir(parents=True, exist_ok=True)
                    os.replace(path, target)
                    placed.append(path)
            except Exception:
                for stash, original in reversed(held):
                    os.replace(stash, original)
                raise
            # Successful close of this temporary directory removes only the explicit views.
    except Exception:
        for path in reversed(placed):
            target = destination / path.relative_to(work)
            os.replace(target, path)
        prune_empty(destination)
        raise
    result['applied'] = True
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--repo', type=Path, required=True)
    parser.add_argument('--feature-id', required=True)
    parser.add_argument('--keep', action='append', default=[],
                        help='file or directory under .agent-work to move into the archive; caller verifies it is real evidence')
    parser.add_argument('--view', action='append', default=[],
                        help='generated dispatch view relative to .agent-work to discard; caller must verify ownership and no live references')
    parser.add_argument('--apply', action='store_true', help='after reviewing inventory, create the timestamped archive, move keeps and discard the declared views')
    args = parser.parse_args(argv)
    try:
        print(json.dumps(archive(args.repo, args.feature_id, args.keep, args.view, args.apply),
                         ensure_ascii=False, indent=2))
        return 0
    except (ArchiveError, OSError) as exc:
        print(json.dumps({'applied': False, 'error': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
