#!/usr/bin/env python3
"""The Office V2: read-only capability planning and shared metadata lookup.

This CLI produces plans, never invokes agents, installs tools, or attests PASS.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SECTOR_ALIASES = {'ui_ux': 'ux-design', 'database': 'data', 'harness': 'orchestrator', 'observability': 'devops'}


def read_json(path):
    return json.loads(Path(path).read_text(encoding='utf-8'))


def safe_path(root, relative):
    if not isinstance(relative, str) or not relative or Path(relative).is_absolute():
        raise ValueError('repository-relative path required')
    result = (root / relative.split('#', 1)[0]).resolve()
    if not result.is_relative_to(root.resolve()):
        raise ValueError('path escapes root')
    if any(part in {'.git', 'runtime-state'} for part in result.relative_to(root.resolve()).parts):
        raise ValueError('private runtime path forbidden')
    if result.name.startswith('.env') or result.suffix.lower() in {'.key', '.pem', '.p12', '.pfx'}:
        raise ValueError('secret path forbidden')
    return result


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def select_skills(root, sector, capabilities=()):
    registry = read_json(root / 'library/indexes/skill-routes.json')
    sector = SECTOR_ALIASES.get(sector, sector)
    if sector not in registry['sectors']:
        raise ValueError(f'unknown sector: {sector}')
    entries = {item['id']: item for item in registry['skills']}
    requested = list(capabilities)
    # Selecting no capability returns only invariant core and asks for a bounded choice.
    selected = list(registry.get('global_required', [])) + list(registry['sectors'][sector]['core'])
    candidates = registry['sectors'][sector]['capabilities']
    for value in requested:
        if value not in candidates:
            raise ValueError(f'capability {value} is not owned by {sector}')
        selected.append(value)
    ordered, visiting = [], set()
    def visit(key):
        if key in ordered:
            return
        if key in visiting or key not in entries:
            raise ValueError('invalid skill dependency graph')
        visiting.add(key)
        for dep in entries[key].get('requires', []):
            visit(dep)
        visiting.remove(key)
        ordered.append(key)
    for key in selected:
        visit(key)
    result = []
    for key in ordered:
        item = entries[key]
        path = safe_path(root, item['path'])
        if not path.is_file():
            raise ValueError(f'mandatory_reference_missing: {item["path"]}')
        result.append({'id': key, 'path': item['path'], 'sha256': sha(path), 'bytes': path.stat().st_size,
                       'read': 'FULL_SKILL_REQUIRED', 'reference_base': item.get('reference_base')})
    return {'sector': sector, 'skills': result, 'candidate_capabilities': candidates,
            'decision': 'PLANNED_NOT_EXECUTED', 'selection_complete': bool(requested) or not candidates,
            'instruction': 'Select applicable capabilities; read selected skills fully and all active mandatory references. Legacy entrypoints remain separate compatibility mode.'}


def validate_anchor(path, anchor):
    if not anchor:
        return
    anchor = anchor.lstrip('#')
    raw = path.read_text(encoding='utf-8')
    lines, fence = [], None
    for line in raw.splitlines():
        marker = re.match(r'^ {0,3}(`{3,}|~{3,})(.*)$', line)
        if marker:
            token, tail = marker.groups()
            if fence is None:
                fence = token
            elif token[0] == fence[0] and len(token) >= len(fence) and not tail.strip():
                fence = None
            continue
        if fence is None:
            lines.append(line)
    text = '\n'.join(lines)
    explicit = set(re.findall(r'(?:id|name)=[\"\']([^\"\']+)[\"\']', text))
    headings, counts = set(), {}
    for title in re.findall(r'^#{1,6}\s+(.+?)\s*#*$', text, re.M):
        title = re.sub(r'[^\w\- ]', '', title.lower()).replace(' ', '-')
        count = counts.get(title, 0)
        headings.add(title + (f'-{count}' if count else ''))
        counts[title] = count + 1
    if anchor not in headings | explicit:
        raise ValueError(f'mandatory_reference_missing: anchor #{anchor}')


def validate_checklist(items):
    if not isinstance(items, list) or not items:
        raise ValueError('nonempty checklist required')
    for item in items:
        if not isinstance(item, dict) or not isinstance(item.get('instruction'), str) or not item['instruction'].strip():
            raise ValueError('checklist instruction required')
        if 'children' in item:
            validate_checklist(item['children'])


def validate_contract(contract):
    if contract.get('schema_version') != 2:
        raise ValueError('legacy contract: normalize through canonical Harness before routing')
    for field in ('task_id', 'contract_revision', 'human_task', 'goal', 'scope', 'out_of_scope',
                  'allowed_paths', 'sectors', 'microtasks', 'references', 'required_tests',
                  'acceptance_criteria', 'stop_conditions', 'execution_lists'):
        if field not in contract:
            raise ValueError(f'missing contract field: {field}')
    for collection, key in (('execution_lists','list_id'),('microtasks','id'),('references','id'),('required_tests','id'),('acceptance_criteria','id')):
        ids = [x[key] for x in contract[collection]]
        if len(ids) != len(set(ids)):
            raise ValueError(f'duplicate identifiers: {collection}')
    microtasks = {x['id']: x for x in contract['microtasks']}
    references = {x['id'] for x in contract['references']}
    tests = {x['id'] for x in contract['required_tests']}
    criteria = {x['id'] for x in contract['acceptance_criteria']}
    lists = {x['list_id']: x for x in contract['execution_lists']}
    done, active = set(), set()
    def visit_microtask(key):
        if key not in microtasks or key in active:
            raise ValueError('unknown or cyclic microtask dependency')
        if key in done:
            return
        active.add(key)
        for dep in microtasks[key].get('depends_on', []):
            visit_microtask(dep)
        active.remove(key)
        done.add(key)
    for key in microtasks:
        visit_microtask(key)
    for item in lists.values():
        if item.get('phase') not in {'planning', 'implementation', 'validation'}:
            raise ValueError('invalid list phase')
        validate_checklist(item.get('checklist'))
        if not set(item.get('depends_on', [])) <= set(microtasks):
            raise ValueError('unknown list microtask dependency')
        if not item.get('owner_skill') or not item.get('microtask_ids'):
            raise ValueError('list owner and microtasks required')
        for key in item['microtask_ids']:
            if key not in microtasks or microtasks[key].get('owner_skill') != item['owner_skill']:
                raise ValueError('microtask owner mismatch or missing microtask')
        if not set(item.get('references', [])) <= references:
            raise ValueError('unknown list reference')
        if not set(item.get('required_tests', [])) <= tests or not set(item.get('acceptance_criteria', [])) <= criteria:
            raise ValueError('unknown list test or acceptance criterion')
    sectors = contract['sectors']
    for phase_key in ('depends_on', 'planning_depends_on'):
        done, active = set(), set()
        def visit(key):
            if key not in sectors or key in active:
                raise ValueError('unknown or cyclic sector dependency')
            if key in done:
                return
            active.add(key)
            for dep in sectors[key].get(phase_key, []):
                if dep not in sectors or sectors[dep]['applicability'] != 'REQUIRED':
                    raise ValueError('dependency must be REQUIRED')
                visit(dep)
            active.remove(key)
            done.add(key)
        for key, item in sectors.items():
            if item.get('applicability') not in {'REQUIRED', 'N/A'} or not item.get('owner'):
                raise ValueError('invalid sector applicability or owner')
            if item['applicability'] == 'N/A' and not item.get('reason'):
                raise ValueError('N/A requires reason')
            visit(key)
    required = {key for key, value in sectors.items() if value['applicability'] == 'REQUIRED'}
    if 'harness' not in required or not required - {'harness'} <= set(sectors['harness']['depends_on']):
        raise ValueError('harness must reconcile all REQUIRED sectors')
    return contract


def handoff(root, contract_path, list_id, sector, revision):
    path = safe_path(root, contract_path)
    contract = validate_contract(read_json(path))
    if str(contract['contract_revision']) != str(revision):
        raise ValueError('stale contract revision')
    if sector not in contract['sectors'] or contract['sectors'][sector]['applicability'] != 'REQUIRED':
        raise ValueError('sector is not REQUIRED')
    lists = [item for item in contract['execution_lists'] if item['list_id'] == list_id]
    if len(lists) != 1:
        raise ValueError('unknown or duplicate list ID')
    item, routed = lists[0], contract['sectors'][sector]
    if item['owner_skill'] != routed['owner']:
        raise ValueError('wrong list owner')
    microtasks = {m['id']:m for m in contract['microtasks']}
    if not set(item['microtask_ids']) <= set(routed['microtasks']):
        raise ValueError('list microtasks outside sector')
    refs = {r['id']:r for r in contract['references']}
    selected = list(dict.fromkeys(routed['required_sources'] + item.get('references', [])))
    for key in item['microtask_ids']:
        if key not in microtasks:
            raise ValueError('unknown microtask')
        selected.extend(x for x in microtasks[key].get('references', []) if x not in selected)
    sources = []
    for key in selected:
        if key not in refs:
            raise ValueError('unknown reference ID')
        ref = refs[key]
        if not ref.get('purpose'):
            raise ValueError('source purpose required')
        target = safe_path(root, ref['project_path'])
        if not target.is_file():
            raise ValueError(f'mandatory_reference_missing: {key}')
        validate_anchor(target, ref['project_path'].partition('#')[2])
        validate_anchor(target, ref.get('section', ''))
        sources.append(ref)
    conditional = routed.get('conditional_sources', [])
    if any(x.get('reference_id') not in refs or not x.get('condition') for x in conditional):
        raise ValueError('invalid conditional source')
    return {'task_id': contract['task_id'], 'contract_revision': str(revision),
            'execution_contract_path': contract_path, 'list_id': list_id, 'sector': sector,
            'phase': item['phase'], 'owner': item['owner_skill'], 'required_sources': sources,
            'conditional_sources': conditional, 'optional_sources': routed.get('optional_sources', []),
            'depends_on': routed.get('planning_depends_on', []) if item['phase'] == 'planning' else routed['depends_on'],
            'global_constraints': {k:contract.get(k) for k in ('goal','scope','allowed_paths','protected_paths','out_of_scope','stop_conditions','acceptance_criteria','required_tests')},
            'list': item, 'decision': 'PLANNED_NOT_EXECUTED',
            'execution_blockers': ['current Human Task/JSON equivalence receipt required', 'current dependency and skill receipts required'],
            'instruction': 'A handoff plan does not authorize execution or complete a gate. Resolve current canonical receipts and active conditional sources first.'}


def search(root, query, layers=(), limit=8):
    """Metadata-only lookup; priority is Task, project, local, distributed.

    No external network/installation/skill execution is performed. Each content
    access validates its digest; stale records become explicit misses.
    """
    indexes = [Path(p) for p in layers] + [root/'library/indexes/resources.json']
    terms = set(re.findall(r'[\w-]+', query.casefold()))
    seen, results, warnings = set(), [], []
    for rank, index in enumerate(indexes):
        data = read_json(index)
        for record in data['resources']:
            identity = record['id']
            if identity in seen:
                continue
            text = ' '.join(str(record.get(k,'')) for k in ('id','title','category','keywords')).casefold()
            score = sum(t in text for t in terms)
            if not score:
                continue
            target = safe_path(root, record['path'])
            if not target.is_file() or sha(target) != record['sha256']:
                warnings.append(f'stale_or_missing:{identity}')
                continue
            seen.add(identity)
            results.append(dict(record, layer=rank, score=score))
    results.sort(key=lambda x:(x['layer'], -x['score'], x['id']))
    return {'query':query,'results':results[:max(1,min(limit,50))], 'warnings':warnings,
            'external_search_required':not bool(results), 'external_search':'NOT_EXECUTED',
            'instruction':'Reuse selected Task resource, then project/local/distributed metadata. On a gap use available canonical research tools with official sources and permission gates. Read only selected bodies.'}


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--root',type=Path,default=ROOT)
    sub=parser.add_subparsers(dest='command',required=True)
    p=sub.add_parser('plan'); p.add_argument('sector'); p.add_argument('--capability',action='append',default=[])
    p=sub.add_parser('search'); p.add_argument('query'); p.add_argument('--index',action='append',default=[]); p.add_argument('--limit',type=int,default=8)
    p=sub.add_parser('read'); p.add_argument('resource_id')
    p=sub.add_parser('handoff'); p.add_argument('contract'); p.add_argument('--list',required=True); p.add_argument('--sector',required=True); p.add_argument('--revision',required=True)
    args=parser.parse_args(argv); root=args.root.resolve()
    try:
        if args.command=='plan': result=select_skills(root,args.sector,args.capability)
        elif args.command=='search': result=search(root,args.query,args.index,args.limit)
        elif args.command=='handoff': result=handoff(root,args.contract,args.list,args.sector,args.revision)
        else:
            records=read_json(root/'library/indexes/resources.json')['resources']
            found=[x for x in records if x['id']==args.resource_id]
            if len(found)!=1: raise ValueError('unknown resource ID')
            entry=found[0]; target=safe_path(root,entry['path'])
            if sha(target)!=entry['sha256']: raise ValueError('stale resource: rebuild index')
            result={'resource':entry,'content':target.read_text(encoding='utf-8')}
        print(json.dumps(result,ensure_ascii=False,indent=2)); return 0
    except (ValueError,OSError,KeyError,TypeError) as exc:
        print(json.dumps({'error':str(exc),'state':'BLOCKED'}),file=sys.stderr); return 2

if __name__=='__main__': raise SystemExit(main())
