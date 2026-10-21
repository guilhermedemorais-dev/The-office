#!/usr/bin/env python3
"""Read-only evidence snapshot validation and delivery reporting. Never publish."""
from __future__ import annotations
import argparse
from collections import Counter
import hashlib
import json
import math
from pathlib import Path
import re
import sys

STATES = {'PLANNED', 'IN_PROGRESS', 'BLOCKED', 'REWORK', 'NOT_VALIDATED', 'ACCEPTED'}
DOC_STATES = {'UPDATED', 'UNCHANGED', 'NOT_APPLICABLE', 'PENDING'}


def require(condition, message):
    if not condition:
        raise ValueError(message)


def nonempty(value):
    return isinstance(value, str) and bool(value.strip())


def unique(entries, label):
    require(isinstance(entries, list), f'{label}: list required')
    result = {}
    for entry in entries:
        require(isinstance(entry, dict) and nonempty(entry.get('id')), f'{label}: id required')
        require(entry['id'] not in result, f'{label}: duplicate id')
        result[entry['id']] = entry
    return result


def check_source(root, source):
    require(isinstance(source, dict), 'source object required')
    raw, digest = source.get('path'), source.get('sha256')
    require(nonempty(raw) and not Path(raw).is_absolute() and '\\' not in raw,
            'source needs project-relative path')
    parts = Path(raw).parts
    require(not any(p in {'.git', '..', 'runtime-state'} or p.startswith('.env') for p in parts),
            'private or escaping source path')
    require(Path(raw).suffix.lower() not in {'.key', '.pem', '.p12', '.pfx'}, 'secret source path')
    target = root / raw
    require(target.resolve().is_relative_to(root.resolve()), 'source escapes project')
    require(not any(p.is_symlink() for p in [target, *target.parents] if p.is_relative_to(root)),
            'symlink source forbidden')
    require(target.is_file(), f'missing evidence: {raw}')
    require(isinstance(digest, str) and re.fullmatch('[a-f0-9]{64}', digest), 'sha256 required')
    require(hashlib.sha256(target.read_bytes()).hexdigest() == digest, f'stale evidence: {raw}')


def check_evidence(root, evidence, required=False):
    require(isinstance(evidence, list), 'evidence list required')
    require(not required or bool(evidence), 'accepted work or resolved documentation needs evidence')
    for source in evidence:
        check_source(root, source)


def percentage(accepted, total):
    return round(100 * accepted / total, 2) if total else None


def summarize(snapshot, root):
    require(isinstance(snapshot, dict) and snapshot.get('schema_version') == 1,
            'snapshot schema_version must be 1')
    require(nonempty(snapshot.get('project')) and nonempty(snapshot.get('baseline_revision')),
            'project and baseline_revision required')
    check_source(root, snapshot.get('baseline_source'))
    stages = unique(snapshot.get('stages'), 'stages')
    tasks = unique(snapshot.get('tasks'), 'tasks')
    items = unique(snapshot.get('items'), 'items')
    issue_urls = [task.get('issue_url') for task in tasks.values() if task.get('issue_url')]
    require(len(issue_urls) == len(set(issue_urls)), 'duplicate canonical Issue mapping')
    for stage in stages.values():
        require(nonempty(stage.get('title')), 'stage title required')
    for task in tasks.values():
        require(nonempty(task.get('title')) and nonempty(task.get('contract_revision')),
                'task title and contract_revision required')
        check_source(root, task.get('source'))
        url = task.get('issue_url')
        require(url is None or isinstance(url, str) and re.fullmatch(
            r'https://github\.com/[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+/issues/[1-9][0-9]*', url),
            'invalid canonical Issue URL')
        docs = task.get('documentation')
        require(isinstance(docs, dict) and set(docs) == {'technical', 'user'},
                'separate technical/user documentation required')
        for assessment in docs.values():
            require(isinstance(assessment, dict) and assessment.get('status') in DOC_STATES
                    and nonempty(assessment.get('reason')), 'documentation status/reason required')
            check_evidence(root, assessment.get('evidence'), assessment['status'] != 'PENDING')
    for item in items.values():
        require(item.get('task_id') in tasks and item.get('stage_id') in stages,
                'item references unknown task/stage')
        require(item.get('status') in STATES, 'unknown item state')
        weight = item.get('weight', 1)
        require(type(weight) in (int, float) and math.isfinite(weight) and 0 < weight <= 1e9,
                'finite positive weight required (maximum 1e9)')
        check_evidence(root, item.get('evidence'), item['status'] == 'ACCEPTED')
    def aggregate(selected):
        total = sum(i.get('weight', 1) for i in selected)
        accepted = sum(i.get('weight', 1) for i in selected if i['status'] == 'ACCEPTED')
        return {'accepted_weight': accepted, 'total_weight': total,
                'percent': percentage(accepted, total),
                'counts': dict(Counter(i['status'] for i in selected))}
    rows = []
    for task_id, task in tasks.items():
        selected = [i for i in items.values() if i['task_id'] == task_id]
        metric = aggregate(selected)
        ready = bool(selected) and all(i['status'] == 'ACCEPTED' for i in selected) and all(
            a['status'] != 'PENDING' for a in task['documentation'].values())
        rows.append({'id': task_id, 'title': task['title'], 'contract_revision': task['contract_revision'],
                     'issue_url': task.get('issue_url'), **metric,
                     'documentation': {k: v['status'] for k, v in task['documentation'].items()},
                     'closure_ready': ready, 'canonical_done': 'NOT_VERIFIED',
                     'current_stage': next((i['stage_id'] for i in selected if i['status'] != 'ACCEPTED'),
                                           selected[-1]['stage_id'] if selected else None)})
    return {'schema_version': 1, 'project': snapshot['project'],
            'baseline_revision': snapshot['baseline_revision'],
            'formula': '100 * accepted baseline weight / all baseline weight',
            'metric_kind': 'approved scope units, not effort or time',
            'total': aggregate(list(items.values())),
            'stages': [{'id': key, 'title': stage['title'], **aggregate(
                [i for i in items.values() if i['stage_id'] == key])} for key, stage in stages.items()],
            'tasks': rows, 'publication': 'PREPARED_NOT_PUBLISHED',
            'validation': 'LOCAL_REFERENCES_CHECKED_NOT_SEMANTIC_APPROVAL',
            'telemetry': {'input_tokens': None, 'output_tokens': None, 'cached_tokens': None,
                          'effort_hours': None, 'elapsed_seconds': None},
            'limitations': ['Snapshot completeness and owner acceptance need semantic reconciliation.',
                            'Remote Issue/contract freshness is not checked by this offline calculator.',
                            'Canonical Done, merge, deploy and portal synchronization are not attested.']}


def portal_payload(report):
    repositories = {task['issue_url'].split('/issues/', 1)[0]
                    for task in report['tasks'] if task['issue_url']}
    require(len(repositories) <= 1, 'portal export requires one configured GitHub repository')
    payloads, omitted = [], []
    for task in report['tasks']:
        if not task['issue_url'] or not task['current_stage']:
            omitted.append(task['id'])
            continue
        counts = task['counts']
        status = 'blocked' if counts.get('BLOCKED') or counts.get('REWORK') else (
            'backlog' if counts.get('PLANNED', 0) == sum(counts.values()) else 'in_progress')
        # Ready for review is not canonical Done. This tool never publishes done.
        payloads.append({'issueNumber': int(task['issue_url'].rsplit('/', 1)[1]),
                         'issueUrl': task['issue_url'], 'title': task['title'],
                         'description': 'Scope criteria progress; final acceptance remains separate.',
                         'stage': task['current_stage'], 'status': status,
                         'progress': min(100, int(task['percent'] or 0))})
    return {'publication': 'PREPARED_NOT_PUBLISHED', 'task_payloads': payloads, 'omitted_tasks': omitted,
            'review_required': 'Review titles/stages and project membership before sending.',
            'metric_gap': 'Portal dashboard done/eligible excludes backlog; it is not whole-baseline progress.'}


def markdown(report):
    def cell(value):
        return str(value).replace('|', '\\|').replace('\n', ' ').replace('\r', ' ')
    lines = [f'# {cell(report["project"])}', '',
             f'Baseline: {cell(report["baseline_revision"])}. Prepared, not published.', '',
             f'Accepted scope: {report["total"]["percent"] if report["total"]["percent"] is not None else "NOT_AVAILABLE"}%.',
             'This measures approved scope units, not effort, duration or production readiness.', '',
             '| Phase | Accepted / total weight | Percent |', '| --- | --- | --- |']
    for stage in report['stages']:
        lines.append(f'| {cell(stage["title"])} | {stage["accepted_weight"]} / {stage["total_weight"]} | {stage["percent"] if stage["percent"] is not None else "NOT_AVAILABLE"} |')
    lines += ['', '| Task | Documentation technical / user | Closure ready |', '| --- | --- | --- |']
    for task in report['tasks']:
        lines.append(f'| {cell(task["id"])} | {task["documentation"]["technical"]} / {task["documentation"]["user"]} | {task["closure_ready"]} |')
    lines += ['', 'Blockers/unverified items: ' + str(report['total']['counts']), '',
              'Tokens, effort and elapsed time: NOT_AVAILABLE. Canonical Done and portal sync: NOT_VERIFIED.']
    return '\n'.join(lines) + '\n'


def load_snapshot(path):
    def pairs(entries):
        result = {}
        for key, value in entries:
            require(key not in result, 'duplicate JSON key')
            result[key] = value
        return result
    def constant(value):
        raise ValueError(f'nonfinite JSON value: {value}')
    return json.loads(Path(path).read_text(encoding='utf-8'), object_pairs_hook=pairs,
                      parse_constant=constant)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('snapshot')
    parser.add_argument('--root', type=Path, required=True, help='Actual client project root')
    parser.add_argument('--format', choices=['json', 'markdown', 'portal'], default='json')
    args = parser.parse_args()
    try:
        report = summarize(load_snapshot(args.snapshot), args.root.resolve())
        print(markdown(report) if args.format == 'markdown' else json.dumps(
            portal_payload(report) if args.format == 'portal' else report, ensure_ascii=False, indent=2))
    except (ValueError, OSError, TypeError, KeyError, OverflowError) as error:
        parser.exit(1, f'Report not generated: {error}\n')


if __name__ == '__main__':
    main()
