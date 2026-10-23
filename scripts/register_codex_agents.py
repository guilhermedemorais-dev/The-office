#!/usr/bin/env python3
"""Opt-in local Codex profile registration; never invokes agents or a network.

This is an Office adapter, not a host permission boundary. Run against a trusted,
quiescent, user-owned CODEX_HOME. Rechecks detect ordinary concurrent changes;
stdlib path checks cannot eliminate hostile filesystem races on every platform.
"""
from __future__ import annotations

import argparse
import copy
import hashlib
import json
import os
from pathlib import Path
import re
import stat
import sys
import tempfile
import tomllib
import uuid


SECTORS = (
    'architecture', 'backend', 'data', 'devops', 'documentation', 'environment',
    'frontend', 'governance', 'librarian', 'orchestrator', 'product', 'qa', 'sdd',
    'security', 'ux-design',
)
BEGIN = '<!-- THE-OFFICE-GLOBAL-AGENTS BEGIN '
END = '<!-- THE-OFFICE-GLOBAL-AGENTS END -->'
PROFILE_BEGIN = b'# THE-OFFICE-CODEX-PROFILE v1 sha256='
PROFILE_STATE = '.office-agent-profiles.json'


class Blocked(Exception):
    """An intentionally sanitized diagnostic, containing no host file content."""


def digest(data):
    return hashlib.sha256(data).hexdigest()


def checked_path(path):
    """Check before resolve: links, junctions and regular-file hardlinks fail closed."""
    path = Path(path)
    if not path.is_absolute() or '..' in path.parts:
        raise Blocked('absolute paths without parent traversal required')
    for item in reversed((path, *path.parents)):
        try:
            info = item.lstat()
        except FileNotFoundError:
            continue
        if stat.S_ISLNK(info.st_mode) or getattr(info, 'st_file_attributes', 0) & 0x400:
            raise Blocked('symlink or reparse path rejected')
        if item != path and not stat.S_ISDIR(info.st_mode):
            raise Blocked('non-directory ancestor rejected')
        if stat.S_ISREG(info.st_mode) and info.st_nlink != 1:
            raise Blocked('hardlinked file rejected')
        if not (stat.S_ISREG(info.st_mode) or stat.S_ISDIR(info.st_mode)):
            raise Blocked('non-regular filesystem entry rejected')
    return path


def read_optional(path):
    checked_path(path)
    if not path.exists():
        return None
    if not path.is_file():
        raise Blocked('file target is not a regular file')
    return path.read_bytes()


def text(data):
    try:
        return data.decode('utf-8-sig')
    except UnicodeError:
        raise Blocked('UTF-8 source required') from None


def parse_toml(data):
    try:
        return tomllib.loads(text(data))
    except tomllib.TOMLDecodeError:
        raise Blocked('invalid TOML; existing configuration preserved') from None


def render_profiles(bundle):
    profiles = {}
    for sector in SECTORS:
        source = read_optional(bundle / 'agents' / sector / 'AGENT.md')
        if source is None:
            raise Blocked('canonical agent contract missing')
        contract = text(source)
        match = re.search(r'## Responsibility\s*\n(.*?)(?=\n## |\Z)', contract, re.S)
        if not match or not match.group(1).strip():
            raise Blocked('canonical agent responsibility missing')
        name = 'office_' + sector.replace('-', '_')
        description = ' '.join(match.group(1).split())
        instructions = (
            f'You are the The Office V2 {sector} specialist. Canonical bundle root: '
            f'{bundle.as_posix()}.\nBefore work, read this root\'s AGENTS.md and '
            f'docs/operations/v2-execution-policy.md, then agents/{sector}/AGENT.md in full. '
            'Resolve repository-relative paths against this bundle, never the client workspace. '
            f'Run scripts/office.py plan {sector} with applicable --capability selections; '
            'read selected V2 skills and their mandatory references fully, retaining reference_base. '
            'Use the compatible installed Python. Inherit the parent approved scope, task/revision, '
            'model, permissions, MCPs and safety controls. Do not invent approvals or execution. '
            'Do not create another orchestrator or unrelated agents. Return your own '
            'SKILL_RECEIPT and EXECUTION_RECEIPT with actual checks and limitations. '
            'Registration never grants merge, deploy, remote writes or spending authority.\n\n'
            + contract
        )
        values = {'name': name, 'description': description,
                  'developer_instructions': instructions}
        payload = ''.join(
            f'{key} = {json.dumps(value, ensure_ascii=False)}\n'
            for key, value in values.items()).encode('utf-8')
        profiles[name] = (description, PROFILE_BEGIN + digest(payload).encode() + b'\n' + payload)
    return profiles


def profile_payload(data):
    """Validate the profile envelope; the separate local state establishes provenance."""
    header, separator, payload = data.partition(b'\n')
    if (not separator or not header.startswith(PROFILE_BEGIN)
            or header[len(PROFILE_BEGIN):] != digest(payload).encode()):
        raise Blocked('invalid or customized managed profile envelope; reconcile manually')
    return payload


def load_profile_state(data, names):
    if data is None:
        return None
    try:
        state = json.loads(text(data))
        if (not isinstance(state, dict)
                or set(state) != {'schema_version', 'generator', 'profiles'}
                or type(state['schema_version']) is not int or state['schema_version'] != 1
                or state['generator'] != 'the-office-codex-agents'
                or not isinstance(state['profiles'], dict)
                or set(state['profiles']) != set(names)):
            raise ValueError
        for record in state['profiles'].values():
            if (not isinstance(record, dict)
                    or set(record) != {'sha256', 'description', 'config_file'}
                    or not all(isinstance(value, str) for value in record.values())
                    or not re.fullmatch('[0-9a-f]{64}', record['sha256'])):
                raise ValueError
    except (ValueError, TypeError, KeyError):
        raise Blocked('invalid managed profile state; restore backup or reconcile manually') from None
    return state['profiles']


def refresh_description(config_bytes, name, old, new):
    """Edit only the literal generated description line; other layouts fail closed."""
    if old == new:
        return config_bytes
    pattern = (rb'(?m)^(\[agents\.' + re.escape(name.encode()) + rb'\]\r?\n)'
               + re.escape(('description = ' + json.dumps(old, ensure_ascii=False)).encode())
               + rb'(\r?\n)')
    matches = list(re.finditer(pattern, config_bytes))
    if len(matches) != 1:
        raise Blocked(f'custom registration layout: {name}; reconcile manually')
    match = matches[0]
    replacement = (match[1] + ('description = ' + json.dumps(new, ensure_ascii=False)).encode()
                   + match[2])
    return config_bytes[:match.start()] + replacement + config_bytes[match.end():]


def routing_block(bundle):
    body = (
        '# Global sector agents: The Office V2\n\n'
        f'Canonical bundle root: {bundle.as_posix()}\n'
        'For engineering work, execute each activated sector through its registered '
        'office_* host subagent. The main agent coordinates and consolidates; it must '
        'not impersonate sector owners or invent invocations, independent reviews or receipts. '
        'Read the canonical agent contract, select relevant capabilities with office.py plan, '
        'then read selected skills and mandatory references before executing. '
        'A skill read or a plan does not execute an agent.\n\n'
        + '\n'.join(f'- {s}: office_{s.replace("-", "_")}' for s in SECTORS)
        + '\n\nDiscover actual host availability and use only necessary sectors, respecting '
        'concurrency limits, file ownership, contracts and human gates. Do not create a '
        'second orchestrator to duplicate coordination. If a profile or tool is unavailable, '
        'report that sector as not executed. Registration permits reuse across projects; '
        'it does not keep agents running or prove that existing chats reloaded instructions. '
        'Do not claim another sector approval. Common conversation does not require an '
        'engineering pipeline. No automatic merge or deploy.\n'
    ).encode('utf-8')
    return (BEGIN + digest(body) + ' -->\n').encode() + body + END.encode() + b'\n'


def merge_instructions(original, block):
    original = original or b''
    # Decode only for validation; preserve all original bytes outside the managed block.
    text(original)
    begin, end = BEGIN.encode(), END.encode()
    if begin not in original and end not in original:
        separator = b'' if not original or original.endswith(b'\n') else b'\n'
        return original + separator + block
    if original.count(begin) != 1 or original.count(end) != 1:
        raise Blocked('invalid managed instruction boundaries')
    start = original.index(begin)
    match = re.match(rb'<!-- THE-OFFICE-GLOBAL-AGENTS BEGIN ([0-9a-f]{64}) -->\n', original[start:])
    if not match:
        raise Blocked('invalid managed instruction header')
    stop = original.index(end)
    body_start = start + match.end()
    if stop < body_start or digest(original[body_start:stop]).encode() != match[1]:
        raise Blocked('customized managed instructions; manual reconciliation required')
    finish = stop + len(end)
    if original[finish:finish + 1] == b'\n':
        finish += 1
    return original[:start] + block + original[finish:]


def plan(bundle_root, codex_home):
    bundle, home = checked_path(bundle_root), checked_path(codex_home)
    if not bundle.is_dir():
        raise Blocked('bundle root missing')
    for required in ('AGENTS.md', 'docs/operations/v2-execution-policy.md', 'scripts/office.py'):
        if read_optional(bundle / required) is None:
            raise Blocked('bundle prerequisite missing')
    if home.exists() and not home.is_dir():
        raise Blocked('CODEX_HOME must be a directory')
    # Check auxiliary mutation boundaries during read-only preflight as well.
    checked_path(home / '.office-agents.lock')
    backup_parent = checked_path(home / '.office-agent-backups')
    if backup_parent.exists():
        if not backup_parent.is_dir():
            raise Blocked('backup parent must be a directory')
        if os.name != 'nt' and stat.S_IMODE(backup_parent.stat().st_mode) & 0o077:
            raise Blocked('backup parent is not private')
    override_bytes = read_optional(home / 'AGENTS.override.md')
    if (override_bytes or b'').strip():
        raise Blocked('global AGENTS.override.md may suppress routing; reconcile manually')
    original = read_optional(home / 'config.toml')
    config = parse_toml(original or b'')
    expected_config = copy.deepcopy(config)
    if any(config.get(key) for key in ('instructions', 'developer_instructions',
                                     'model_instructions_file', 'experimental_instructions_file')):
        raise Blocked('custom global instruction override requires manual reconciliation')
    features = config.get('features', {})
    if isinstance(features, dict) and features.get('multi_agent') is False:
        raise Blocked('multi_agent explicitly disabled; settings preserved')
    agents = config.get('agents', {})
    if not isinstance(agents, dict):
        raise Blocked('agents configuration is not a table')
    snapshots, desired = {}, {}

    def target(relative, content, previous):
        path = home / relative
        checked_path(path)
        if not path.is_relative_to(home):
            raise Blocked('target outside CODEX_HOME')
        if read_optional(path) != previous:
            raise Blocked('concurrent target changes during plan')
        snapshots[path] = previous
        desired[path] = content

    profiles = render_profiles(bundle)
    state_path = home / PROFILE_STATE
    state_bytes = read_optional(state_path)
    old_state = load_profile_state(state_bytes, profiles)
    new_state = {'schema_version': 1, 'generator': 'the-office-codex-agents', 'profiles': {}}
    amended = original or b''
    append = ''
    for name, (description, profile) in profiles.items():
        relative = f'agents/{name}.toml'
        expected = {'description': description, 'config_file': (home / relative).as_posix()}
        expected_config.setdefault('agents', {})[name] = expected
        existing = read_optional(home / relative)
        prior = old_state[name] if old_state is not None else None
        previous_expected = ({'description': prior['description'], 'config_file': prior['config_file']}
                             if prior is not None else expected)
        if name in agents and agents[name] != previous_expected:
            raise Blocked(f'agent registration conflict: {name}')
        if prior is not None and prior['config_file'] != expected['config_file']:
            raise Blocked(f'managed profile path conflict: {name}')
        if existing is not None:
            values = parse_toml(existing)
            if prior is not None:
                if (digest(existing) != prior['sha256']
                        or set(values) != {'name', 'description', 'developer_instructions'}
                        or values.get('name') != name
                        or values.get('description') != prior['description']):
                    raise Blocked(f'customized agent profile: {name}; restore backup or reconcile manually')
                profile_payload(existing)
            elif existing not in (profile, profile_payload(profile)):
                # Legacy bytes may be recognized only by exact equality to current generation.
                raise Blocked(f'profile without matching managed provenance: {name}; back up and reconcile manually')
        elif prior is not None:
            raise Blocked(f'managed profile missing: {name}; restore backup or reconcile manually')
        target(relative, profile, existing)
        new_state['profiles'][name] = {'sha256': digest(profile), **expected}
        if name in agents and prior is not None:
            amended = refresh_description(amended, name, prior['description'], description)
        if name not in agents:
            append += f'\n[agents.{name}]\n' + ''.join(
                f'{key} = {json.dumps(value, ensure_ascii=False)}\n'
                for key, value in expected.items())
    if append:
        newline = b'\r\n' if b'\r\n' in amended else b'\n'
        if amended and not amended.endswith(b'\n'):
            amended += newline
        amended += append.encode('utf-8').replace(b'\n', newline)
    if parse_toml(amended) != expected_config:
        raise Blocked('registration amendment would change unrelated configuration; reconcile manually')
    target('config.toml', amended, original)
    instructions = read_optional(home / 'AGENTS.md')
    target('AGENTS.md', merge_instructions(instructions, routing_block(bundle)), instructions)
    target(PROFILE_STATE, (json.dumps(new_state, indent=2, ensure_ascii=False) + '\n').encode(), state_bytes)
    # Also recheck non-written safety inputs immediately before applying.
    snapshots[home / 'AGENTS.override.md'] = override_bytes
    changes = {p: data for p, data in desired.items() if snapshots[p] != data}
    return home, snapshots, changes


def exclusive_write(path, data):
    checked_path(path)
    with path.open('xb') as stream:
        os.chmod(path, 0o600)
        stream.write(data)
        stream.flush()
        os.fsync(stream.fileno())


def replace_file(path, data, mode=0o600):
    checked_path(path)
    fd, temporary = tempfile.mkstemp(prefix='.office-agents-', dir=path.parent)
    temporary = Path(temporary)
    try:
        with os.fdopen(fd, 'wb') as stream:
            stream.write(data)
            stream.flush()
            os.fsync(stream.fileno())
        os.chmod(temporary, mode)
        checked_path(path)
        os.replace(temporary, path)
    finally:
        if temporary.exists():
            temporary.unlink()


def apply(home, snapshots, changes):
    if not changes:
        return None
    for path, previous in snapshots.items():
        if read_optional(path) != previous:
            raise Blocked('concurrent changes detected before apply')
    # All configuration/profile/path conflicts have been checked before mkdir/write.
    checked_path(home)
    home.mkdir(parents=True, exist_ok=True, mode=0o700)
    lock = home / '.office-agents.lock'
    checked_path(lock)
    try:
        lock_fd = os.open(lock, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
    except FileExistsError:
        raise Blocked('registration lock exists; inspect before retry') from None
    os.close(lock_fd)
    backup = None
    applied, modes = [], {}
    try:
        for path, previous in snapshots.items():
            if read_optional(path) != previous:
                raise Blocked('concurrent changes detected under registration lock')
        backup_parent = checked_path(home / '.office-agent-backups')
        backup_parent.mkdir(mode=0o700, exist_ok=True)
        if os.name != 'nt' and stat.S_IMODE(backup_parent.stat().st_mode) & 0o077:
            raise Blocked('backup parent is not private')
        backup = backup_parent / uuid.uuid4().hex
        backup.mkdir(mode=0o700)
        manifest = []
        for index, path in enumerate(changes):
            previous = snapshots[path]
            modes[path] = stat.S_IMODE(path.stat().st_mode) if previous is not None else 0o600
            manifest.append({'path': path.relative_to(home).as_posix(),
                             'existed': previous is not None, 'backup': f'{index}.bin'})
            if previous is not None:
                exclusive_write(backup / f'{index}.bin', previous)
        exclusive_write(backup / 'manifest.json', json.dumps(manifest, indent=2).encode())
        for path, data in changes.items():
            checked_path(path.parent)
            path.parent.mkdir(mode=0o700, parents=True, exist_ok=True)
            if read_optional(path) != snapshots[path]:
                raise Blocked('concurrent target changes detected')
            replace_file(path, data, modes[path])
            applied.append(path)
        return backup.relative_to(home).as_posix()
    except (OSError, Blocked):
        rollback_failed = False
        for path in reversed(applied):
            try:
                if read_optional(path) != changes[path]:
                    raise Blocked('concurrent rollback conflict')
                if snapshots[path] is None:
                    path.unlink()
                else:
                    replace_file(path, snapshots[path], modes[path])
            except (OSError, Blocked):
                rollback_failed = True
        outcome = 'rollback incomplete; inspect private backup' if rollback_failed else 'changed files rolled back'
        raise Blocked('apply failed; ' + outcome) from None
    finally:
        lock.unlink()


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('command', choices=('plan', 'check', 'apply'))
    parser.add_argument('--bundle-root', required=True, type=Path)
    parser.add_argument('--codex-home', required=True, type=Path)
    args = parser.parse_args(argv)
    try:
        home, snapshots, changes = plan(args.bundle_root, args.codex_home)
        backup = apply(home, snapshots, changes) if args.command == 'apply' else None
        status = ('APPLIED' if changes else 'CONFIGURED') if args.command == 'apply' else (
            'CHANGES_REQUIRED' if changes else 'CONFIGURED')
        result = {'status': status, 'profiles': len(SECTORS),
                  'changed_paths': [p.relative_to(home).as_posix() for p in changes],
                  'backup': backup, 'agent_execution': 'NOT_VALIDATED',
                  'existing_chat_reload': 'NOT_VALIDATED'}
        code = 1 if args.command == 'check' and changes else 0
    except (Blocked, OSError):
        # Never emit raw OS/TOML diagnostics or host file contents.
        error = sys.exc_info()[1]
        reason = str(error) if isinstance(error, Blocked) else 'filesystem operation failed'
        result, code = {'status': 'BLOCKED', 'reason': reason}, 2
    print(json.dumps(result, indent=2))
    return code


if __name__ == '__main__':
    raise SystemExit(main())
