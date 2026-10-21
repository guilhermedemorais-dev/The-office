#!/usr/bin/env python3
"""Build a metadata cache over canonical resources; never copy their contents."""
from pathlib import Path
import hashlib
import json
import re

ROOT = Path(__file__).resolve().parents[1]

def build(root=ROOT):
    paths = set(root.glob('plugins/*/skills/*/references/*'))
    paths.update(root.glob('library/skills/*.json'))
    paths.update(root.glob('library/tools/*'))
    paths.update(root.glob('plugins/*/skills/*/library/**/*'))
    paths.update(root.glob('library/documentation-templates/**/*'))
    paths.update(root.glob('plugins/*/templates/*'))
    resources=[]
    for path in sorted(paths):
        if not path.resolve().is_relative_to(root.resolve()) or path.is_symlink(): continue
        if any(part in {'.git','runtime-state'} for part in path.resolve().relative_to(root.resolve()).parts): continue
        if not path.is_file() or path.suffix not in {'.json','.md','.yaml','.yml'}: continue
        relative=path.relative_to(root).as_posix()
        text=path.read_text(encoding='utf-8')
        headings=re.findall(r'^#{1,3}\s+(.+)',text,re.M)
        category='tools' if 'tool' in path.name or 'mcp' in path.name else 'references'
        if 'component' in path.name: category='components'
        if 'template' in relative: category='documentation-templates'
        if 'architecture' in path.name: category='architecture'
        metadata=[]
        if path.suffix=='.json':
            def extract(value):
                if isinstance(value,dict):
                    for k,v in value.items():
                        if k in {'id','name','title','description','category','capability','official_repository'} and isinstance(v,str): metadata.append(v)
                        elif isinstance(v,(dict,list)): extract(v)
                elif isinstance(value,list):
                    for v in value: extract(v)
            extract(json.loads(text))
        else:
            metadata.extend(re.findall(r'\[([^]\n]+)\]\(https?://[^)]+\)',text))
            metadata.extend(line.split('|')[1].strip(' `') for line in text.splitlines() if line.startswith('|') and len(line.split('|'))>2)
        resources.append({'id':relative,'path':relative,'title':headings[0] if headings else path.stem,
                          'category':category,'keywords':headings[:30]+metadata[:250]+re.split(r'[-_/ .]',relative),
                          'sha256':hashlib.sha256(path.read_bytes()).hexdigest(),
                          'provenance':{'type':'canonical-versioned-file','license':'See source record and repository LICENSE; no external dependency relicensing',
                                        'version':'content-sha256','source':relative},
                          'status':'CATALOGED_NOT_EXECUTED'})
    return {'schema_version':1,'cache_policy':'Content-addressed metadata; reject changed/missing content, rebuild with scripts/build_library.py',
            'resources':resources}

if __name__=='__main__':
    output=ROOT/'library/indexes/resources.json'; output.parent.mkdir(parents=True,exist_ok=True)
    output.write_text(json.dumps(build(),ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
