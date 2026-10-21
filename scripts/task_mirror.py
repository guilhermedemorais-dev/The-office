#!/usr/bin/env python3
"""Render/check the approved THEOFFICE-V2-001 Human Task mirror.

A formatting utility, not a Task store or runtime state system. --check is
read-only and compares all canonical contract fields plus the complete rendered
card. Remote Issue equality still requires reading the actual Issue body.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
DEFAULT_CONTRACT = ROOT / 'docs/execution/THEOFFICE-V2-001.json'
DEFAULT_MIRROR = ROOT / 'docs/tasks/THEOFFICE-V2-001.md'


def _render_value(value, contract, depth=0):
    pref = '  ' * depth
    inherited = {
        'allowed_paths': 'Same approved allowed_paths as the global allowed_paths section above (all entries inherited). ',
        'protected_paths': 'Same protected_paths as the global protected_paths section above (all entries inherited). ',
        'stop_conditions': 'All global stop_conditions above apply unchanged. ',
    }
    if depth > 1:
        for field, text in inherited.items():
            if value == contract[field]:
                return pref + text
    if isinstance(value, dict):
        return '\n'.join(
            pref + '- **' + key + '**:' + (
                '\n' + render_value(child, contract, depth + 1)
                if isinstance(child, (dict, list)) else ' ' + str(child)
            )
            for key, child in value.items()
        )
    if isinstance(value, list) and all(not isinstance(child, (dict, list)) for child in value):
        return pref + '; '.join(str(child) for child in value) if value else pref + 'None.'
    if isinstance(value, list):
        return '\n'.join(
            pref + '- ' + (
                '\n' + render_value(child, contract, depth + 1)
                if isinstance(child, (dict, list)) else str(child)
            )
            for child in value
        ) or pref + '- None.'
    return pref + str(value)


def render_value(value, contract, depth=0):
    return '\n'.join(line.rstrip() for line in _render_value(value, contract, depth).splitlines())


def render_task(contract):
    """Render the approved Task without changing its normative contract."""
    if contract.get('task_id') != 'THEOFFICE-V2-001' or contract.get('schema_version') != 2:
        raise ValueError('renderer is scoped to approved THEOFFICE-V2-001 v2 contract')
    revision = str(contract['contract_revision'])
    link = '../execution/THEOFFICE-V2-001.json'
    body = '# THEOFFICE-V2-001: Restructure Dev-workflow as The Office V2\n\n'
    body += '> **Resumo:** ' + contract['summary'] + '\n\n'
    body += 'contract_revision: ' + revision + '. Complexity: COMPLEX. Branch: `feat/the-office-v2`. Issue: ' + contract['human_task']['issue_url'] + '.\n\n'
    body += 'Normative instructions below mirror the single [Execution Contract](' + link + '). Runtime status and evidence belong in Issue comments/receipts, not JSON. User approved PRD and construction/push; merge and deploy are excluded.\n'
    for key, value in contract.items():
        body += '\n<!-- contract-field: ' + key + ' -->\n## ' + key + '\n\n'
        body += render_value(value, contract) + '\n\n<!-- /contract-field: ' + key + ' -->\n'
    body += '\n## Execution list prompts\n\n'
    for microtask in contract['microtasks']:
        body += '### ' + microtask['id'] + ': ' + microtask['title'] + '\n\n'
        body += 'Execute [JSON da Task](' + link + '), `list_id=' + microtask['id'] + '/checklist`, `contract_revision=' + revision + '`, owner `' + microtask['owner_skill'] + '`. Inherit global constraints, verify current Harness equivalence/dependency receipts and read selected skills/references completely.\n\n'
        body += 'Checklist: see this list in normative **execution_lists** above; track completion in owner evidence.\n'
    body += '\n## Evidence and change ledger\n\nAll checkboxes remain unverified until owner receipts are linked. Current execution evidence is maintained in Issue comments and migration reports. No checkbox, plan or source reading attests runtime PASS.\n\n| Revision | Change | Reason | Impact | Authorization |\n| --- | --- | --- | --- | --- |\n| 1 | Approved PRD rendered as concrete contract; additive compatibility overlay selected | Preserve source paths and rules while enabling selective routing | V1 plugin entrypoints remain compatibility mode; root V2 path is explicit | User PRD and execution command, 2026-10-16 |\n'
    return body


def check_fields(contract, actual):
    """Compare each marked field with the full canonical structured value."""
    keys = re.findall(r'^<!-- contract-field: ([^\n]+) -->$', actual, re.M)
    failures = []
    if keys != list(contract):
        failures.append('missing, duplicate, unexpected or reordered contract field markers')
    for key, value in contract.items():
        start = '<!-- contract-field: ' + key + ' -->\n## ' + key + '\n\n'
        end = '\n\n<!-- /contract-field: ' + key + ' -->'
        if actual.count(start) != 1 or actual.count(end) != 1:
            failures.append('invalid marker: ' + key)
            continue
        observed = actual.split(start, 1)[1].split(end, 1)[0]
        if observed != render_value(value, contract):
            failures.append('normative field divergence: ' + key)
    return failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--contract', type=Path, default=DEFAULT_CONTRACT)
    parser.add_argument('--mirror', type=Path, default=DEFAULT_MIRROR)
    mode = parser.add_mutually_exclusive_group(required=True)
    mode.add_argument('--check', action='store_true', help='read-only exact field/body comparison')
    mode.add_argument('--write', action='store_true', help='write deterministic local mirror; never publish remotely')
    args = parser.parse_args(argv)
    try:
        contract = json.loads(args.contract.read_text(encoding='utf-8'))
        expected = render_task(contract)
        if args.write:
            args.mirror.write_text(expected, encoding='utf-8')
        actual = args.mirror.read_text(encoding='utf-8')
        failures = check_fields(contract, actual)
        if actual != expected:
            failures.append('complete deterministic rendering differs')
        result = {
            'task_id': contract['task_id'],
            'contract_revision': contract['contract_revision'],
            'result': 'DIVERGENT' if failures else 'LOCAL_MIRROR_MATCH',
            'fields_compared': len(contract),
            'characters': len(actual),
            'utf8_bytes': len(actual.encode('utf-8')),
            'mirror_sha256': hashlib.sha256(actual.encode('utf-8')).hexdigest(),
            'contract_sha256': hashlib.sha256(args.contract.read_bytes()).hexdigest(),
            'failures': failures,
            'remote_issue_comparison': 'NOT_PERFORMED',
            'limitation': 'Deterministic representation equality is not independent semantic review or remote publication evidence.',
        }
        print(json.dumps(result, ensure_ascii=False, indent=2))
        return 1 if failures else 0
    except (OSError, ValueError, KeyError, TypeError) as exc:
        print(json.dumps({'result': 'BLOCKED', 'error': str(exc)}), file=sys.stderr)
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
