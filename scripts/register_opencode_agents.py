#!/usr/bin/env python3
"""Opt-in project-local OpenCode adapters, without installing or starting a host.

Uses the existing Office transactional writer and path checks. Run only against
a trusted, quiescent project directory; this is not a hostile filesystem sandbox.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path
import re
import sys

from register_codex_agents import (Blocked, SECTORS, apply, checked_path, digest,
                                   read_optional, text)

STATE = 'office-registration.json'
GENERATOR = 'the-office-opencode-v1'


def json_object(data):
    try:
        value = json.loads(text(data))
        if not isinstance(value, dict):
            raise ValueError
        return value
    except (ValueError, TypeError):
        raise Blocked('invalid JSON object; existing configuration preserved') from None


def render(bundle, source_snapshots=None):
    source_snapshots = source_snapshots if source_snapshots is not None else {}

    def source_bytes(path):
        data = read_optional(path)
        if path in source_snapshots and source_snapshots[path] != data:
            raise Blocked('canonical source changed during plan')
        source_snapshots[path] = data
        return data

    files = {}
    for sector in SECTORS:
        contract = source_bytes(bundle / 'agents' / sector / 'AGENT.md')
        if contract is None:
            raise Blocked('canonical agent contract missing')
        match = re.search(r'## Responsibility\s*\n(.*?)(?=\n## |\Z)', text(contract), re.S)
        if not match or not match[1].strip():
            raise Blocked('canonical agent responsibility missing')
        name = 'office_' + sector.replace('-', '_')
        description = ' '.join(match[1].split())
        mode = 'primary' if sector == 'orchestrator' else 'subagent'
        permissions = {'graphiti_clear_graph': 'deny', 'graphiti_delete_episode': 'deny',
                       'graphiti_delete_entity_edge': 'deny'}
        if sector == 'orchestrator':
            permissions['edit'] = 'deny'
        body = (
            f'---\ndescription: {json.dumps(description, ensure_ascii=False)}\n'
            f'mode: {mode}\npermission: {json.dumps(permissions)}\n---\n\n'
            f'Canonical bundle root: `{bundle.as_posix()}`. Client code remains in '
            'the current workspace. Do not resolve bundle paths from the client.\n\n'
            f'Read `{bundle.as_posix()}/AGENTS.md`, its V2 execution policy and '
            f'`agents/{sector}/AGENT.md` fully before work. Run the canonical '
            f'`scripts/office.py plan {sector}` with necessary capability IDs; '
            'read selected canonical SKILL.md files and mandatory references, '
            'retaining reference_base. Do not load all available skills. '
            'For engineering tasks inherit the approved Task, revision, source and '
            'allowed paths. Return actual skill and execution receipts. '
            'An agent profile or plan never proves execution. '
            'Keep host permissions and existing merge/deploy gates. '
            'Do not invent another owner\'s approval. '
            'Only the primary office_orchestrator coordinates needed office_* subagents; '
            'do not recursively instantiate another orchestrator.\n\n'
            'Graphiti is optional supplemental memory; load required Task sources '
            'first and retain Potpie/local fallback. Do not connect the raw Graphiti '
            'reference MCP or grant graphiti_* permissions implicitly. Tool-name '
            'denials here reduce accidental calls but do not implement server auth '
            'or restrict equivalent network/bash access.\n'
        )
        files[f'agents/{name}.md'] = body.encode()
    registry_data = source_bytes(bundle / 'library/indexes/skill-routes.json')
    if registry_data is None:
        raise Blocked('canonical skill routes missing')
    registry = json_object(registry_data)
    entries = registry.get('skills')
    if not isinstance(entries, list) or not entries:
        raise Blocked('canonical skill routes empty or invalid')
    seen = set()
    for entry in entries:
        sid = entry.get('id') if isinstance(entry, dict) else None
        if not isinstance(sid, str) or not re.fullmatch('[a-z0-9]+(?:-[a-z0-9]+)*', sid) or sid in seen:
            raise Blocked('invalid or duplicate canonical skill ID')
        seen.add(sid)
        source = bundle / 'skills' / sid / 'SKILL.md'
        expected = f'skills/{sid}/SKILL.md'
        if entry.get('path') != expected:
            raise Blocked('noncanonical skill path in route')
        skill = source_bytes(source)
        if skill is None:
            raise Blocked('routed skill missing')
        content = text(skill)
        match = re.match(r'^---\n(.*?)\n---(?:\n|$)', content, re.S)
        if not match or not re.search(r'^name:\s*' + re.escape(sid) + r'\s*$', match[1], re.M):
            raise Blocked('routed skill frontmatter mismatch')
        # Preserve discovery metadata, not a second manually maintained procedure.
        wrapper = (
            content[:match.end()] + '\n'
            f'Canonical skill: `{source.as_posix()}`. Source SHA-256: `{digest(skill)}`.\n\n'
            f'Read that complete canonical SKILL.md and its required core and active '
            f'references before acting. Resolve all repository-relative paths from '
            f'`{bundle.as_posix()}`, retaining the canonical reference_base. '
            'This discovery adapter is not an execution receipt or a replacement '
            'for the source. If the source is absent, unavailable or changed from '
            'this digest, run registration check/update before using it.\n'
        )
        files[f'skills/{sid}/SKILL.md'] = wrapper.encode()
    return files


def plan(bundle_root, project_root):
    bundle, project = checked_path(bundle_root), checked_path(project_root)
    if not bundle.is_dir() or not project.is_dir():
        raise Blocked('existing absolute bundle and project directories required')
    if any(c in bundle.as_posix() for c in '\n\r`'):
        raise Blocked('unsupported bundle path characters')
    source_snapshots = {}
    for prerequisite in ('AGENTS.md', 'docs/operations/v2-execution-policy.md', 'scripts/office.py'):
        path = bundle / prerequisite
        source_snapshots[path] = read_optional(path)
        if source_snapshots[path] is None:
            raise Blocked('canonical bundle prerequisite missing')
    home = checked_path(project / '.opencode')
    if home.exists() and not home.is_dir():
        raise Blocked('.opencode must be a directory')
    # JSONC is intentionally not rewritten or guessed by this stdlib adapter.
    jsonc = read_optional(project / 'opencode.jsonc')
    if (jsonc or b'').strip():
        raise Blocked('opencode.jsonc requires manual collision review')
    config_data = read_optional(project / 'opencode.json')
    config = json_object(config_data) if config_data is not None else {}
    configured_agents = config.get('agent', {})
    if not isinstance(configured_agents, dict):
        raise Blocked('invalid host agent configuration')
    names = {'office_' + sector.replace('-', '_') for sector in SECTORS}
    if names.intersection(configured_agents):
        raise Blocked('office agent override in host config; reconcile manually')
    generated = render(bundle, source_snapshots)
    state_bytes = read_optional(home / STATE)
    old = {}
    if state_bytes is not None:
        state = json_object(state_bytes)
        if (set(state) != {'schema_version', 'generator', 'files'} or
                state['schema_version'] != 1 or state['generator'] != GENERATOR or
                not isinstance(state['files'], dict)):
            raise Blocked('invalid registration state')
        old = state['files']
        if set(old) - set(generated):
            raise Blocked('managed source removed; review stale adapters before updating')
        if any(not isinstance(v, str) or not re.fullmatch('[0-9a-f]{64}', v) for v in old.values()):
            raise Blocked('invalid registration digest')
    snapshots, desired = dict(source_snapshots), {}
    for relative, data in generated.items():
        path = home / relative
        previous = read_optional(path)
        if relative in old:
            if previous is None or digest(previous) != old[relative]:
                raise Blocked('managed adapter changed or missing; reconcile manually')
        elif previous is not None:
            raise Blocked('unmanaged adapter collision; existing file preserved')
        snapshots[path], desired[path] = previous, data
    state = {'schema_version': 1, 'generator': GENERATOR,
             'files': {relative: digest(data) for relative, data in generated.items()}}
    state_path = home / STATE
    snapshots[state_path] = state_bytes
    desired[state_path] = (json.dumps(state, indent=2, sort_keys=True) + '\n').encode()
    # These safety inputs participate in the writer's concurrent-change check.
    snapshots[project / 'opencode.json'] = config_data
    snapshots[project / 'opencode.jsonc'] = jsonc
    changes = {p: data for p, data in desired.items() if snapshots[p] != data}
    return home, snapshots, changes


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('plan', 'check', 'apply'))
    parser.add_argument('--bundle-root', type=Path, required=True)
    parser.add_argument('--project-root', type=Path, required=True)
    args = parser.parse_args(argv)
    try:
        home, snapshots, changes = plan(args.bundle_root, args.project_root)
        backup = apply(home, snapshots, changes) if args.command == 'apply' else None
        status = ('APPLIED' if changes else 'CONFIGURED') if args.command == 'apply' else (
            'CHANGES_REQUIRED' if changes else 'CONFIGURED')
        result = {'status': status, 'profiles': len(SECTORS),
                  'changed_paths': [p.relative_to(home).as_posix() for p in changes],
                  'backup': backup, 'host_schema_baseline': 'OpenCode v1.19.4',
                  'host_execution': 'NOT_VALIDATED', 'memory_connection': 'NOT_CONFIGURED'}
        code = 1 if args.command == 'check' and changes else 0
    except (Blocked, OSError):
        error = sys.exc_info()[1]
        result = {'status': 'BLOCKED', 'reason': str(error) if isinstance(error, Blocked) else 'filesystem operation failed'}
        code = 2
    print(json.dumps(result, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
