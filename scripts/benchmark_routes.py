#!/usr/bin/env python3
"""Reproducible routing microbenchmark; not end-to-end LLM performance."""
import json
from pathlib import Path
from time import perf_counter
from office import ROOT, read_json, select_skills, search, validate_contract
import importlib.util

def execute():
    registry=read_json(ROOT/'library/indexes/skill-routes.json')
    entries={x['id']:x for x in registry['skills']}
    source_paths={x['id']:x['path'] for x in registry['sources']}
    cases=[('A-trivial-ui',[('ux-design',['ux-visual-validation'])]),
           ('B-backend',[('backend',['implementation-delivery'])]),
           ('C-new-module',[('product',['product-discovery','product-planning']),('architecture',[]),
             ('sdd',['sdd-specifications','sdd-task-contracts']),('backend',['implementation-delivery']),
             ('ux-design',['ux-components','ux-design-system','ux-visual-validation']),
             ('qa',['qa-validation']),('security',['security-review','security-tools-reporting']),('documentation',[]),
             ('orchestrator',['orchestrator-task-governance','orchestrator-delegation','orchestrator-review'])])]
    results=[]
    for name,routes in cases:
        start=perf_counter(); ids=set()
        for sector,caps in routes:
            plan=select_skills(ROOT,sector,caps)
            assert plan['selection_complete']
            ids.update(x['id'] for x in plan['skills'])
        v2=sum((ROOT/entries[i]['path']).stat().st_size for i in ids)
        originals={entries[i]['source'] for i in ids if entries[i]['source']}
        v1=sum((ROOT/source_paths[i]).stat().st_size for i in originals)
        results.append({'scenario':name,'selected_skills':sorted(ids),'v1_canonical_skill_bytes':v1,
                        'v2_selected_skill_bytes':v2,'planner_elapsed_ms':round((perf_counter()-start)*1000,3),
                        'result':'PASS','scope':'source bodies and generated wrappers only; excludes mandatory references, Task, tool outputs and actual LLM execution'})
    start=perf_counter(); first=search(ROOT,'backend payments'); again=search(ROOT,'backend payments')
    assert first==again and first['results'] and first['external_search']=='NOT_EXECUTED'
    results.append({'scenario':'D-library-reuse','result':'PASS','same_results':True,'external_calls':0,
                    'elapsed_ms':round((perf_counter()-start)*1000,3)})
    spec=importlib.util.spec_from_file_location('platform_catalog',ROOT/'environment/shared/platform_catalog.py')
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    missing=module.inspect_tool('environment',which=lambda command:None)
    assert missing['runtime_discovered'] is False and missing['states']['VERIFIED'] is None
    results.append({'scenario':'E-missing-tool','result':'PASS','fixture':'runtime lookup returns None','operational_verified':None,'preparation_executed':False})
    contract=read_json(ROOT/'docs/execution/THEOFFICE-V2-001.json');validate_contract(contract)
    from office import handoff
    rejected=False
    try: handoff(ROOT,'docs/execution/THEOFFICE-V2-001.json','MT-10/checklist','qa','stale')
    except ValueError: rejected=True
    assert rejected
    results.append({'scenario':'F-contract-change','result':'PASS','stale_revision_blocked':True,
                    'scope':'revision mismatch only; Issue edit/equivalence and scope approval remain canonical workflow gates'})
    return {'type':'routing-microbenchmark','measurement_source':'Python perf_counter and filesystem byte counts',
            'input_tokens':'NOT_AVAILABLE','output_tokens':'NOT_AVAILABLE','cached_tokens':'NOT_AVAILABLE',
            'llm_latency':'NOT_MEASURED','end_to_end_quality':'NOT_VALIDATED',
            'results':results,'interpretation':'Do not translate bytes into tokens or claim full workflow parity/savings. References and wrappers can dominate. Repeated metadata query is deterministic reuse, not a remote-cache benchmark.'}

if __name__=='__main__': print(json.dumps(execute(),indent=2))
