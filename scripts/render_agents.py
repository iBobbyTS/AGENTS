#!/usr/bin/env python3
"""Render subagent role instructions from agents/instructions.md into every
native agent definition and external spawn profile.

agents/instructions.md is the single hand-edited source; the instruction bodies
inside agents/zcode/*.md, agents/codex/*.toml and agents/*/external/*.json are
generated. Host-specific metadata (frontmatter, model, tools, sandbox, preset
fields) is not touched. Default mode rewrites drifted files; --check exits
non-zero on drift without writing.
"""
from __future__ import annotations
import argparse
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
INSTRUCTIONS = ROOT / 'agents' / 'instructions.md'
SECTION = re.compile(r'^## ([a-z][a-z0-9_]*)$\n?', re.M)

# Generated definition -> its role section in instructions.md.
NATIVE_ROLES = {
    'agents/zcode/impl_std.md': 'implementer',
    'agents/zcode/plan_review.md': 'plan_review',
    'agents/zcode/code_review.md': 'code_review',
    'agents/codex/impl_large.toml': 'implementer',
    'agents/codex/plan_reviewer.toml': 'plan_review',
    'agents/codex/code_reviewer.toml': 'code_review',
    'agents/codex/code_explorer.toml': 'code_explorer',
}
EXTERNAL_ROLES = {
    'agents/zcode/external/sfd-codex-impl-large.json': 'implementer',
    'agents/zcode/external/sfd-codex-plan-review.json': 'plan_review',
    'agents/zcode/external/sfd-codex-code-review.json': 'code_review',
    'agents/codex/external/sfd-dsh-impl-std.json': 'implementer',
    'agents/codex/external/sfd-zcode-plan-review.json': 'plan_review',
    'agents/codex/external/sfd-zcode-code-review.json': 'code_review',
    'agents/external/sfd-agy-impl-std.json': 'implementer',
}
TOML_BLOCK = re.compile(r'(developer_instructions = """).*?(""")', re.S)
# Runtime copy main reads before dispatching: all roles in one installed asset.
SKILL_ASSET = ROOT / 'skills/sectioned-feature-development/assets/ROLE-INSTRUCTIONS.md'


def role_texts() -> dict[str, str]:
    parts = SECTION.split(INSTRUCTIONS.read_text(encoding='utf-8'))
    if len(parts) < 3:
        raise ValueError(f'{INSTRUCTIONS} has no role sections')
    roles: dict[str, str] = {}
    for key, body in zip(parts[1::2], parts[2::2]):
        if key in roles:
            raise ValueError(f'duplicate role section: {key}')
        roles[key] = body.strip()
    return roles


def rendered(path: str, role: str, roles: dict[str, str]) -> str:
    """The full file content this definition should carry."""
    target = ROOT / path
    text = target.read_text(encoding='utf-8')
    if path.endswith('.md'):
        _, front, _ = text.split('---', 2)
        return '---' + front + '---' + '\n\n' + roles[role] + '\n'
    if path.endswith('.toml'):
        updated, count = TOML_BLOCK.subn(lambda m: m.group(1) + '\n' + roles[role] + '\n' + m.group(2), text, count=1)
        if count != 1:
            raise ValueError(f'{path} has no developer_instructions block')
        return updated
    data = json.loads(text)
    data['developer_instructions'] = roles[role]
    return json.dumps(data, indent=2, ensure_ascii=False) + '\n'


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, allow_abbrev=False)
    parser.add_argument('--check', action='store_true', help='verify only; exit 1 on drift')
    args = parser.parse_args(argv)
    try:
        roles = role_texts()
        known = set(roles)
        for mapping in (NATIVE_ROLES, EXTERNAL_ROLES):
            for role in mapping.values():
                if role not in known:
                    raise ValueError(f'definition names unknown role section: {role}')
        drifted = []
        want_asset = INSTRUCTIONS.read_text(encoding='utf-8')
        if not SKILL_ASSET.exists() or SKILL_ASSET.read_text(encoding='utf-8') != want_asset:
            drifted.append(SKILL_ASSET.relative_to(ROOT).as_posix())
            if not args.check:
                SKILL_ASSET.write_text(want_asset, encoding='utf-8')
                print(f'rendered: {SKILL_ASSET.relative_to(ROOT)}')
        for mapping in (NATIVE_ROLES, EXTERNAL_ROLES):
            for rel, role in sorted(mapping.items()):
                target = ROOT / rel
                want = rendered(rel, role, roles)
                if target.read_text(encoding='utf-8') != want:
                    drifted.append(rel)
                    if not args.check:
                        target.write_text(want, encoding='utf-8')
                        print(f'rendered: {rel}')
    except (ValueError, OSError, json.JSONDecodeError) as exc:
        print(f'ERROR: {exc}', file=sys.stderr)
        return 2
    if args.check:
        for rel in drifted:
            print(f'DRIFT: {rel}')
        if drifted:
            print('run scripts/render_agents.py to regenerate', file=sys.stderr)
            return 1
        print('all generated definitions match agents/instructions.md')
    elif not drifted:
        print('all generated definitions match agents/instructions.md')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())
