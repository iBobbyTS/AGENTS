#!/usr/bin/env python3
"""Install bundled skills and native agents for Codex or ZCode (Python 3.11+).

Dry-run by default. Replacements are backed up and publication rolls back on failure.
Global configuration is never edited; AGENTS.md is opt-in. Do not run concurrently.
"""
from __future__ import annotations

import argparse
from contextlib import ExitStack
import json
import os
from pathlib import Path
import re
import shutil
import sys
import tempfile
import time
import tomllib

ROOT = Path(__file__).resolve().parents[1]
SKILL_NAME = 'sectioned-feature-development'


def external_data_dir() -> Path:
    """external-subagent's per-user data directory: the product's macOS layout, XDG elsewhere."""
    if sys.platform == 'darwin':
        return Path('~/Library/Application Support/external-subagent').expanduser()
    base = os.environ.get('XDG_DATA_HOME')
    base = Path(base).expanduser() if base else Path('~/.local/share').expanduser()
    return base / 'external-subagent'
PROFILE_SUBAGENTS = ('zcode', 'dsh', 'codex', 'agy')
PROFILE_MODES = ('build', 'edit', 'plan', 'yolo')
CLOSED_EFFORTS = {'codex': ('low', 'medium', 'high', 'xhigh', 'max'), 'agy': ('low', 'medium', 'high', 'max')}
LEGACY_CODEX_AGENTS = ('implementer_1', 'implementer_2', 'implementer_3', 'implementer_4',
                       'advisor', 'impl_nano', 'impl_mini', 'impl_std')


def no_symlinks(path: Path) -> None:
    """Check lexical ancestors before resolve(), including dangling symlinks."""
    for candidate in (path, *path.parents):
        if candidate.is_symlink():
            raise ValueError(f'refusing symlink path: {candidate}')


def check_tree(path: Path) -> None:
    no_symlinks(path)
    if path.is_dir():
        for item in path.rglob('*'):
            if item.is_symlink():
                raise ValueError(f'refusing symlink in installation tree: {item}')


def configuration(target: str, home: Path) -> dict:
    check_tree(ROOT / 'skills' / SKILL_NAME / 'VERSION')
    return {
        'installation_target': target, 'home': str(home),
        'default_dispatch_profile': target, 'available_profiles': [target],
        'version': (ROOT / 'skills' / SKILL_NAME / 'VERSION').read_text().strip(),
    }


def dedicated_profile_files(target: str) -> list[Path]:
    """This host's own spawn-profile sources; the shared folder is not a dispatch route."""
    directory = ROOT / 'agents' / target / 'external'
    no_symlinks(directory)
    return sorted(directory.glob('*.json'))


def external_profile_files(target: str) -> list[Path]:
    """Everything the installer offers for this host: dedicated profiles plus the shared folder."""
    no_symlinks(ROOT / 'agents' / 'external')
    return dedicated_profile_files(target) + sorted((ROOT / 'agents' / 'external').glob('*.json'))


def all_spawn_profile_files() -> list[Path]:
    """Union across hosts; validates shared-directory name uniqueness."""
    no_symlinks(ROOT / 'agents' / 'external')
    files = []
    for target in ('codex', 'zcode'):
        files += dedicated_profile_files(target)
    return files + sorted((ROOT / 'agents' / 'external').glob('*.json'))


def validate_spawn_profiles(files: list[Path]) -> dict[str, Path]:
    """Shape-check spawn-profile sources once; returns profile name -> source path."""
    profiles: dict[str, Path] = {}
    for path in files:
        check_tree(path)
        try:
            data = json.loads(path.read_text())
        except (json.JSONDecodeError, OSError) as exc:
            raise ValueError(f'invalid spawn profile JSON: {path}: {exc}')
        if not isinstance(data, dict):
            raise ValueError(f'spawn profile must be an object: {path}')
        name, subagent = data.get('name'), data.get('subagent')
        if not isinstance(name, str) or not name.startswith('sfd-') or name != path.stem:
            raise ValueError(f'spawn profile name must be the sfd- prefixed file stem: {path}')
        if subagent not in PROFILE_SUBAGENTS:
            raise ValueError(f'spawn profile names an unknown subagent: {path}')
        if data.get('permission_mode') not in PROFILE_MODES:
            raise ValueError(f'spawn profile names an unknown permission_mode: {path}')
        effort = data.get('effort')
        if not isinstance(effort, str) or not re.fullmatch(r'[a-z0-9_]{1,24}', effort):
            raise ValueError(f'spawn profile has a malformed effort token: {path}')
        if subagent in CLOSED_EFFORTS and effort not in CLOSED_EFFORTS[subagent]:
            raise ValueError(f"spawn profile effort is outside {subagent}'s closed set: {path}")
        model = data.get('model')
        if subagent == 'zcode' and model is not None:
            raise ValueError(f'the zcode subagent rejects an explicit spawn model: {path}')
        if subagent == 'dsh' and (not isinstance(model, str) or ':' not in model):
            raise ValueError(f'the dsh subagent wants a provider:model token: {path}')
        if subagent in ('codex', 'agy') and (not isinstance(model, str) or ':' in model or '/' in model):
            raise ValueError(f'the {subagent} subagent wants a bare model slug: {path}')
        if not str(data.get('developer_instructions') or '').strip():
            raise ValueError(f'spawn profile is missing developer_instructions: {path}')
        if name in profiles:
            raise ValueError(f'duplicate spawn profile name: {name}')
        profiles[name] = path
    return profiles


def profile_subagents(target: str) -> str:
    """External selectors this host's dedicated spawn profiles actually name; warning text only."""
    profiles = validate_spawn_profiles(dedicated_profile_files(target))
    names = {json.loads(path.read_text())['subagent'] for path in profiles.values()}
    return ', '.join(sorted(names)) or 'none'


def check_external_subagent(target: str, home: Path) -> None:
    """Warn-only static existence check: no CLI execution, daemon contact or writes."""
    routes = profile_subagents(target)
    data_dir = external_data_dir()
    binding = home / ('config.toml' if target == 'codex' else 'v2/setting.json')
    if shutil.which('external-subagent') is None and not data_dir.is_dir():
        print(f"WARNING: external-subagent not found (PATH, {data_dir}). External dispatch routes "
              f"({routes}) will be capability blockers until it is installed; SFD installation continues.")
        return
    try:
        bound = binding.exists() and 'external-subagent' in binding.read_text()
    except OSError:
        print(f"external-subagent installed; binding unknown ({binding} unreadable); SFD installation continues.")
        return
    if bound:
        print(f"external-subagent: installed; referenced by {binding} (static check only, runtime readiness unverified).")
    else:
        print(f"WARNING: external-subagent installed but not referenced by {binding}. Bind it to this host or "
              f"external dispatch routes ({routes}) will be capability blockers; SFD installation continues.")


def plan_spawn_profiles(target: str, override: Path | None, replace: bool) -> dict | None:
    """Resolve the per-user profiles directory and stage this host's spawn profiles.

    The directory is shared across hosts; SFD writes only sfd-*.json files there and never
    touches anything else. Returns None with a warning when external-subagent is not
    installed; raises on invalid sources, or when an existing sfd-* file differs and
    --replace was not given. Stale cleanup compares against the union of all hosts'
    sources so one host's install never retires another host's profiles.
    """
    data_dir = external_data_dir()
    if override is None:
        no_symlinks(data_dir)
    if override is None and not data_dir.is_dir():
        print(f"WARNING: spawn profiles skipped: external-subagent data directory not found ({data_dir}). "
              f"External dispatch rows need their named profiles; SFD installation continues.")
        return None
    directory = override if override is not None else data_dir / 'profiles'
    no_symlinks(directory)
    validate_spawn_profiles(all_spawn_profile_files())
    own = validate_spawn_profiles(external_profile_files(target))
    install: list[tuple[Path, Path]] = []
    identical: list[str] = []
    occupied: list[tuple[Path, Path]] = []
    for name, src in own.items():
        dst = directory / f'{name}.json'
        check_tree(dst)
        if not dst.exists():
            install.append((src, dst))
        elif dst.read_bytes() == src.read_bytes():
            identical.append(name)
        else:
            occupied.append((src, dst))
    if occupied and not replace:
        names = ', '.join(sorted(dst.stem for _, dst in occupied))
        raise ValueError(f'spawn profiles exist with different content ({names}); '
                         f'review dry-run, then use --replace to back them up')
    stale: list[Path] = []
    if replace and directory.is_dir():
        union = set(validate_spawn_profiles(all_spawn_profile_files()))
        stale = sorted(path for path in directory.glob('sfd-*.json') if path.stem not in union)
        for path in stale:
            check_tree(path)
    return {'directory': directory, 'install': install, 'identical': identical,
            'occupied': occupied, 'stale': stale}


def agent_files(target: str) -> list[Path]:
    no_symlinks(ROOT / 'agents' / target)
    suffix = '*.toml' if target == 'codex' else '*.md'
    files = sorted((ROOT / 'agents' / target).glob(suffix))
    if not files:
        raise ValueError(f'missing agent definitions for {target}')
    for path in files:
        check_tree(path)
        if target == 'codex':
            data = tomllib.loads(path.read_text())
            if data.get('name') != path.stem or not all(data.get(k) for k in (
                'description', 'model', 'model_reasoning_effort', 'developer_instructions', 'sandbox_mode'
            )) or data.get('project_doc_max_bytes') != 0:
                raise ValueError(f'invalid Codex agent definition: {path}')
        else:
            # The supplied template has a deliberately small frontmatter vocabulary.
            # Do not introduce a YAML dependency just to install already-bundled Markdown.
            text = path.read_text()
            if not text.startswith('---\n') or '\ninjectAgentsMd: false\n' not in text.split('---', 2)[1] + '\n':
                raise ValueError(f'invalid ZCode agent definition: {path}')
    return files


def targets(home: Path, target: str, only: str = 'all',
            include_agents_md: bool = False) -> list[tuple[Path, Path]]:
    root = ROOT / 'skills'
    no_symlinks(root)
    names = ['code-review'] if only == 'code-review' else sorted(
        path.name for path in root.iterdir() if path.is_dir() or path.is_symlink())
    if 'code-audit' in names:
        raise ValueError('legacy code-audit must not be bundled alongside its replacements')
    items = [(root / name, home / 'skills' / name) for name in names]
    if only == 'all':
        items += [(path, home / 'agents' / path.name) for path in agent_files(target)]
    if include_agents_md:
        items.append((ROOT / 'AGENTS.md', home / 'AGENTS.md'))
    for src, dst in items:
        check_tree(src)
        check_tree(dst)
        if not src.exists() or (src.is_dir() and not (src / 'SKILL.md').is_file()):
            raise ValueError(f'missing bundled content: {src}')
    return items


def host_doc(stage: Path, folder: str, profile: str) -> str:
    """A per-host document body: strip the H1, keep links resolving from references/."""
    path = stage / 'references' / folder / f'{profile}.md'
    body = '\n'.join(path.read_text().split('\n')[1:]).lstrip('\n')
    return body.replace('](../', '](')


def embed(stage: Path, rel: str, label: str, body: str) -> None:
    """Replace one marker-bounded placeholder block in a staged document."""
    path = stage / rel
    text = path.read_text()
    markers = re.search(rf'<!-- installer: begin {label} embed -->\n.*?'
                        rf'<!-- installer: end {label} embed -->\n?', text, re.S)
    if markers is None:
        raise ValueError(f'{rel} is missing {label} embed markers')
    path.write_text(text[:markers.start()] + body.rstrip('\n') + '\n\n' + text[markers.end():])


def render_installation(stage: Path, config: dict) -> None:
    """Render only the main skill; companion and native agents are host-specific inputs.

    Installing embeds this host's dispatch profile into model-routing.md and installs
    this host's own native agents — never a foreign host's runtime agents,
    bridge or second scheduler. The per-host dispatch/ source directory is not
    installed; installation facts live in installation.json.
    """
    (stage / 'installation.json').write_text(json.dumps(config, indent=2, ensure_ascii=False) + '\n')
    profile = config['default_dispatch_profile']
    embed(stage, 'references/model-routing.md', 'dispatch-profile', host_doc(stage, 'dispatch', profile))
    shutil.rmtree(stage / 'references' / 'dispatch')


def publish(items: list[tuple[Path, Path]], retired: list[Path], home: Path,
            config: dict, replace: bool) -> Path | None:
    """Stage everything before publication; backup and rollback include external profiles.

    Temporary siblings keep each rename on its destination filesystem. This transaction
    protects against ordinary I/O failures, not power loss or concurrent installers.
    """
    destinations = [dst for _, dst in items] + retired
    if any(dst == ROOT or dst.is_relative_to(ROOT) or ROOT.is_relative_to(dst) for dst in destinations):
        raise ValueError('installation destinations must not overlap bundled sources')
    if any(a != b and a.is_relative_to(b) for a in destinations for b in destinations):
        raise ValueError('installation destinations must not overlap each other')
    if len(set(destinations)) != len(destinations):
        raise ValueError('duplicate installation destination')
    for path in destinations:
        check_tree(path)
    for src, _ in items:
        check_tree(src)
    occupied = [dst for dst in destinations if dst.exists()]
    if occupied and not replace:
        raise ValueError('targets exist; review dry-run, then use --replace to back them up')
    no_symlinks(home)
    no_symlinks(home / 'sfd-backups')
    backup = None
    with ExitStack() as stack:
        staged = []
        workspaces = {}
        for dst in destinations:
            no_symlinks(dst.parent)
            dst.parent.mkdir(parents=True, exist_ok=True)
            if dst.parent not in workspaces:
                workspaces[dst.parent] = Path(stack.enter_context(tempfile.TemporaryDirectory(
                    prefix='.skills-install-', dir=dst.parent)))
        for index, (src, dst) in enumerate(items):
            candidate = workspaces[dst.parent] / f'candidate-{index}'
            if src.is_dir():
                shutil.copytree(src, candidate, ignore=shutil.ignore_patterns(
                    '__pycache__', '*.pyc', '.DS_Store', 'test_*.py'))
                if src == ROOT / 'skills' / SKILL_NAME:
                    render_installation(candidate, config)
            else:
                shutil.copy2(src, candidate)
            staged.append((candidate, dst))
        if occupied:
            parent = home / 'sfd-backups'
            parent.mkdir(parents=True, exist_ok=True)
            backup = Path(tempfile.mkdtemp(prefix=time.strftime('%Y%m%d-%H%M%S-'), dir=parent))
            manifest = {}
            for index, dst in enumerate(occupied):
                relative = dst.relative_to(home) if dst.is_relative_to(home) else Path('external-profiles') / dst.name
                out = backup / relative
                out.parent.mkdir(parents=True, exist_ok=True)
                if dst.is_dir():
                    shutil.copytree(dst, out)
                else:
                    shutil.copy2(dst, out)
                manifest[str(relative)] = str(dst)
            (backup / 'manifest.json').write_text(json.dumps(manifest, indent=2) + '\n')
        moved = []
        installed = []
        try:
            for index, dst in enumerate(destinations):
                check_tree(dst)
                if dst.exists():
                    old = workspaces[dst.parent] / f'original-{index}'
                    os.replace(dst, old)
                    moved.append((old, dst))
            for candidate, dst in staged:
                no_symlinks(dst)
                os.replace(candidate, dst)
                installed.append(dst)
        except Exception:
            for dst in reversed(installed):
                if dst.is_dir():
                    shutil.rmtree(dst)
                else:
                    dst.unlink()
            for old, dst in reversed(moved):
                os.replace(old, dst)
            raise
    return backup


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--target', '--host', required=True, choices=['codex', 'zcode'])
    parser.add_argument('--home', type=Path, help='target home; defaults to CODEX_HOME/ZCODE_HOME, then ~/.codex or ~/.zcode')
    parser.add_argument('--include-agents-md', action='store_true', help='also install the bundled global AGENTS.md; existing files require --replace')
    parser.add_argument('--apply', action='store_true')
    parser.add_argument('--replace', action='store_true')
    parser.add_argument('--only', choices=['all', 'code-review'], default='all')
    parser.add_argument('--profiles-dir', type=Path,
                        help='spawn-profile destination directory; defaults to the external-subagent data dir')
    parser.add_argument('--retire-legacy-agents', action='store_true', help='back up and retire only the documented old SFD Codex role filenames')
    args = parser.parse_args(argv)
    try:
        raw_home = (args.home or Path(os.environ.get(f'{args.target.upper()}_HOME') or f'~/.{args.target}')).expanduser()
        no_symlinks(raw_home)
        home = Path(os.path.abspath(raw_home))
        if args.profiles_dir is not None:
            no_symlinks(args.profiles_dir.expanduser())
        profiles_dir = Path(os.path.abspath(args.profiles_dir.expanduser())) if args.profiles_dir else None
        no_symlinks(home)
        config = configuration(args.target, home)
        items = targets(home, args.target, args.only, args.include_agents_md)
        if args.retire_legacy_agents and (args.target != 'codex' or args.only != 'all' or not args.replace):
            raise ValueError('--retire-legacy-agents requires --target codex, a full install, and --replace')
        retired = [home / 'agents' / f'{name}.toml' for name in LEGACY_CODEX_AGENTS] if args.retire_legacy_agents else []
        legacy = home / 'skills' / 'code-audit'
        check_tree(legacy)
        if args.only == 'all' and legacy.exists():
            if not args.replace:
                raise ValueError('legacy code-audit exists; use --replace to back up and retire it')
            retired.append(legacy)
        for dst in retired:
            check_tree(dst)
            if dst.exists():
                print(f'RETIRE after backup: {dst}')
        profiles = None
        if args.only == 'all':
            check_external_subagent(args.target, home)
            profiles = plan_spawn_profiles(args.target, profiles_dir, args.replace)
        print(json.dumps(config, indent=2, ensure_ascii=False))
        for src, dst in items:
            print(f'{src.relative_to(ROOT)} -> {dst}' + (' [exists]' if dst.exists() else ''))
        if profiles is not None:
            for src, dst in profiles['install']:
                print(f'{src.relative_to(ROOT)} -> {dst} [profile]')
            for _, dst in profiles['occupied']:
                print(f'{dst} [profile differs; --replace backs it up]')
            for name in profiles['identical']:
                print(f'{profiles["directory"] / f"{name}.json"} [profile already current]')
            for dst in profiles['stale']:
                print(f'RETIRE profile after backup: {dst}')
        if not args.apply:
            print('DRY_RUN: no files changed. --apply installs; --replace backs up existing exact targets.')
            return 0
        if profiles is not None:
            items += profiles['install'] + profiles['occupied']
            retired += profiles['stale']
        backup = publish(items, retired, home, config, args.replace)
        print(f'INSTALLED. Backup: {backup or "none"}. Unrelated skills and agents and global config unchanged; AGENTS.md installed only if requested.')
        print('Live acceptance still required: role discovery, AGENTS isolation, exact model/effort and external runtime readiness.')
        return 0
    except (ValueError, OSError) as exc:
        print(f'ERROR: {exc}')
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
