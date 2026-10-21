#!/usr/bin/env python3
"""Verify every frozen V1 resource against the recorded source inventory."""
import hashlib
import json
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
ADAPTED={'README.md':'docs/migration-v1-readme.md','AGENTS.md':'docs/migration/v1-AGENTS.md','LICENSE':'docs/migration/V1-LICENSE'}

def verify(root=ROOT):
    inventory=json.loads((root/'docs/migration/v1-inventory.json').read_text(encoding='utf-8'))
    failures=[]
    for item in inventory['files']:
        relative=item['path']
        destination=('docs/migration/v1-bytecode/'+relative) if relative.endswith('.pyc') else ADAPTED.get(relative,relative)
        path=root/destination
        if not path.is_file() or hashlib.sha256(path.read_bytes()).hexdigest()!=item['sha256']:
            failures.append(item['path'])
    return {'source_commit':inventory['source_commit'],'files':len(inventory['files']),'failures':failures,
            'result':'PASS' if not failures else 'FAIL'}

if __name__=='__main__':
    result=verify();print(json.dumps(result,indent=2));raise SystemExit(bool(result['failures']))
