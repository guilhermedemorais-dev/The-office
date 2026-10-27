#!/usr/bin/env python3
"""Build audited, lossless functional slices from canonical V1 skills.

This is a local migration extension, not an agent executor. No source is modified.
Line offsets are 1-based inclusive; hashes use UTF-8 source text (including LF).
"""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import re
import subprocess

ROOT = Path(__file__).resolve().parents[1]
# Each explicit grouping is a capability, never an arbitrary line-count split.
CONFIG = {
 'dev-workflow-standard': ('orchestrator', {
  'core': ['Preamble','Mission','Harness Contract','Mandatory Entry Gate','Hard Limits (non-negotiable)','Skill Roles (who does what)','Practice Provenance','Task And Execution Context','Change Complexity Gate','Context Budget Rules'],
  'discovery':['Mandatory Flow'],
  'task-governance':['Mandatory Task Governance','Official Kanban Method','Definition of Entry / Exit','Repository Readiness Bootstrap','GitHub-Ready Task Structure','Recommended Task Template'],
  'delegation':['Delegation Rules','When to Trigger Each Specialist','Reference Routing'],
  'review':['Review Rules']}),
 'ui-ux-standard':('ux',{
  'core':['Preamble','Ownership','Non-Negotiables','Registry and MCP Policy','Minimal Workflow','Handoff Output'],
  'components':['Component Intelligence'],
  'design-system':['Default Design Structure'],
  'visual-validation':['Visual Quality Gate','Visual QA Checklist']}),
 'sdd-spec-factory':('sdd',{
  'core':['Preamble','Mission','Vocabulary (non-negotiable)','Mandatory hierarchy','Mandatory separation of concerns','Operating principles','Integration with the other plugins','Definition of done for this skill'],
  'discovery':['Phases','Studio PRD handoff','Fase 0 - Diagnóstico','Fase 1 - Consolidação'],
  'specifications':['Consultative Technical Knowledge Routing','Fase 2 - Geração de Specs'],
  'task-contracts':['Fase 3 - Geração de Task Executável'],
  'review':['Fase 4 - Checklist de PR/QA']}),
 'dev-implementation-standard':('implementation',{
  'core':['Preamble','Mission','Preconditions (do not start without these)','Hard Limits (non-negotiable)','Workflow','Escalation','Interfaces with other skills','Definition of done'],
  'delivery':['Task Status Rules','GitHub Projects Readiness','Recommended Task Template'],
  'frontend':['Frontend design sources']}),
 'dev-environment-standard':('environment',{
  'core':['Preamble','Preparation authority','Scope and security'],
  'bootstrap':['Choose the operation','Bootstrap loop'],
  'platform-state':['Platform routing','Library, ownership and local state','Health and handoff']}),
 'devops-standard':('devops',{
  'core':['Preamble','Responsibility boundaries','Human safety gates','Evidence handoff'],
  'operations':['Operational contract','Progressive domain routing']}),
 'qa-testing-standard':('qa',{
  'core':['Preamble','Context and activation','Execution and ownership','Provenance'],
  'validation':['Modes and phases','Shared tools, not duplicated ownership','Evidence gate']}),
 'security-standard':('security',{
  'core':['Preamble','Scope And Safety','Relationship To The Main Workflow','External Publication Gate','Completion Rules','Handoff To Dev Workflow'],
  'review':['Review Modes','Risk-Adaptive Depth','Security Workflow'],
  'tools-reporting':['Tool Policy','Evidence And Reporting']}),
 'studio-prd':('product',{
  'core':['Preamble','Evidence and continuation'],
  'discovery':['Start from evidence'],
  'planning':['Produce the project artifacts','Plan and hand off under supervision']}),
 'reverse-engineering-standard':('reverse-engineering',{
  'core':['Preamble','Preconditions','Safety and legal boundary','Relationship with other skills'],
  'investigation':['Workflow']}),
 'seo-standard':('seo',{
  'core':['Preamble','Preconditions','Ownership boundaries'],
  'site-analysis':['Workflow','Commercial site standard']}),
 'parceiro-estrategico-global':('global',{
  'core':['Preamble','Papel e responsabilidade','Estilo obrigatório','Formato padrão','Classificação da demanda','Verificação e precisão','Práticas consolidadas antes de extensões locais','Execução','Descoberta e roteamento dinâmico de capacidades','Modos especiais','Missão'],
  'discovery':['Descoberta adaptativa','Comando `SemPerguntas`','Briefing estruturado','Tecnologia e software'],
  'marketing-sales':['Marketing','Vendas']})
}
TRIGGERS = {
 'ux-components':['component','library','template','componente','biblioteca'],
 'ux-design-system':['design system','tokens','catalogue','design guide','sistema de design'],
 'ux-visual-validation':['visual','responsive','responsividade','accessibility','acessibilidade','ui','layout'],
 'implementation-frontend':['frontend','ui','component','design'],
 'implementation-delivery':['implement','backend','api','frontend','fix','corrigir'],
 'orchestrator-discovery':['discovery','prd','new product','produto'],
 'orchestrator-task-governance':['task','issue','governance','governança','contract'],
 'orchestrator-delegation':['delegate','handoff','agent','agente','execution'],
 'orchestrator-review':['review','pr','revisão'],
 'sdd-discovery':['discovery','briefing','prd'],
 'sdd-specifications':['spec','architecture','arquitetura','api','database','module'],
 'sdd-task-contracts':['task','contract','issue','tarefa'],
 'sdd-review':['review','qa','pr'],
}

# Additive V2 behavior; the imported V1 skill bodies remain byte-for-byte intact.
V2_OVERLAYS = {
 'product-discovery': {
  'id': 'evidence-led-product-reconstruction',
  'summary': 'Map reference behavior and real feedback into proposed requirements without replacing approved scope.',
  'text': '''## Reference products and user feedback

When the request uses a reference app, screenshots, an existing workflow or user reviews, read the repository-root [reconstruction procedure](library/reconstruction/README.md). Reuse approved discoveries; map observed behavior separately from proposed and approved requirements. Review evidence-backed complaints before fixing scope when differentiation matters. Keyword themes are research candidates, never proof of sentiment or a validated market trend. Do not activate a competing eleven-stage pipeline or impose a new stack.'''
 },
 'reverse-engineering-investigation': {
  'id': 'behavioral-reconstruction-handoff',
  'summary': 'Add stable screen/flow/evidence links while preserving the existing REA gateway and authorized inspection.',
  'text': '''## Behavioral reconstruction handoff

For authorized feature reconstruction, read the repository-root [reconstruction procedure](library/reconstruction/README.md) and use its linked inventory template only where it adds information. Preserve the REA gateway and existing evidence ledger. Link stable screen/flow IDs to observed states, source revisions, evidence and unknowns; an inferred backend is not an observed implementation. Hand findings to the existing SDD owner. This overlay does not restrict separately authorized REA investigations to screenshots or authorize access to third-party private systems.'''
 },
 'sdd-specifications': {
  'id': 'evidence-to-spec-traceability',
  'summary': 'Link reference behavior to existing specifications, requirements, acceptance and planned tests.',
  'text': '''## Evidence to technical specifications

When deriving behavior from a reference product, process or reconstruction findings, read the repository-root [reconstruction procedure](library/reconstruction/README.md). Extend existing module/page/component/API/database specs and canonical Task IDs. Record evidence -> approved requirement -> rule/state -> acceptance criterion -> planned test. Keep OBSERVED, INFERRED and UNKNOWN separate from scope approval and implementation status. Specify actors, permissions, preconditions, transitions, persistence, errors and applicable concurrency/idempotency constraints; resolve material unknowns before readiness. A screenshot does not establish backend rules. No duplicate architecture document, automatic MVP, stack default or Task per screen is introduced.'''
 },
 'qa-validation': {
  'id': 'evidence-bound-reconstruction-coverage',
  'summary': 'Validate every canonical acceptance criterion with revision-bound evidence; never use weighted parity as release approval.',
  'text': '''## Reconstruction and specification coverage

For reconstructed behavior or evidence-to-spec coverage, read the repository-root [reconstruction procedure](library/reconstruction/README.md). Compare the canonical acceptance/test IDs with actual current-revision evidence, including negative cases. Implementation declarations and visual similarity do not prove functional equivalence. Missing mandatory criteria, unapproved skips, stale evidence and incomplete tests block coverage regardless of any average. Use the optional coverage checker only as a structural/integrity check; it cannot run tests, certify independent QA or authorize release. Preserve existing QA, UX, Security and human gates.'''
 },
 'orchestrator-delegation': {
  'id': 'optional-project-memory-routing',
  'summary': 'Retrieve scoped Graphiti memory only when selected, then verify against canonical project sources.',
  'text': '''## Optional project memory

When persistent project memory is selected for the task, read the repository-root [memory integration](integrations/memory/README.md). Retrieve only the authorized project/module slice; verify recalled decisions and evidence against current versioned sources before routing them. Memory is supporting context, never an approval, credential store, canonical Task or proof that a sector executed. If unavailable, continue from current project sources and record the limitation. Do not preload all memories or create one memory service per sector.'''
 },
 'environment-bootstrap': {
  'id': 'opencode-host-preparation',
  'summary': 'Route explicitly selected OpenCode setup through the existing Environment owner.',
  'text': '''## OpenCode host preparation

When the requested host is OpenCode, read the repository-root [OpenCode operation guide](docs/operations/opencode.md). Reuse the existing Environment/provider/tool-state workflow and explicit target paths. Keep generated configuration, host availability and a successful bounded operation as separate evidence. Do not overwrite global settings, install every catalog tool, start persistent services or treat generated profiles as executed agents.'''
 },
 'global-core': {
  'id': 'curated-catalog-before-external-research',
  'summary': 'Search task and project sources, proactively map needs to The Office catalog capabilities, then verify external gaps with official sources.',
  'text': '''## Curated catalog before external research

For technical, product, API, repository, library or tool research, consult current task and project sources first, then search The Office shared catalog before using the web, GitHub search or code-search services. In a The Office checkout, use:

```bash
python scripts/office.py search "<specific need>" --index library/indexes/resources.json --limit 8
```

Read the relevant matched resource files, not only search metadata and not the entire catalog. In an installed bundle, resolve the command and index from that active bundle; do not guess sibling cache paths. If the catalog is inaccessible, state that and continue with the sources actually available. Never claim a search was performed when it was not.

For MCP discovery, search by the needed capability and the term `MCP` (for example, `MCP public-code-search`), then read the matched `mcp-library.json` record and its handoff/configuration fields. Check runtime/host availability separately; the shared JSON is descriptive metadata, not a live connection registry.

Use catalog entries as curated starting points. For current API behavior, official provider documentation, price, quotas, legal terms and availability, verify the relevant claims with the provider after the internal search. A catalog candidate is enough to keep PRD discovery moving: record it as a candidate and leave unsupported facts UNKNOWN or NOT VALIDATED; do not block the PRD by asserting that a paid API or new provider is required before checking the catalog.

## Proactive capability routing and readiness

At the start of a project or a materially new task, translate the outcome into required capabilities (for example: repository/issues, official SDK docs, browser QA, design context, API discovery, public-code examples, cloud/account operations). Search The Office capability/MCP catalog for each material need, then inspect the current host to distinguish AVAILABLE, CONFIGURED, AUTHENTICATED and OPERATION_VERIFIED. A catalog entry is a recommendation candidate, never evidence that the host has it.

Tell the user when a catalog capability would materially improve the task. Name the capability/MCP, the concrete project problem it addresses, why it is better than the available fallback, its provider/source, prerequisites, required access or token, scope, cost if known, and the exact next setup step. Offer a supported installation/connection path; do not silently skip it and do not silently install/connect it. For MCPs marked CORE, interpret CORE as a reusable high-priority catalog capability, not a universal install requirement: select it only when the current task needs that capability. Basic plugin operation has no universal third-party MCP prerequisite.

If no catalog capability fits, say which need remains uncovered, then do bounded external discovery (official provider docs/registry first; GitHub or grep.app for code examples when useful). Compare vetted options and return the source, compatibility, auth, scope, and limitations. Do not install a CLI/MCP or acquire credentials as part of discovery. Use the host's secure auth flow; never ask for or write a token in chat or versioned files. If setup requires user action, provide the exact official URL, host setting/file and field names supported by current documentation, and report USER_ACTION_REQUIRED until the user completes it.

Never report “ready” based only on plugin installation, a catalog match, or a config entry. Report separate evidence for PLUGIN_RECOGNIZED, REQUIRED_TOOLS_AVAILABLE, MCP_CONFIGURED, AUTHENTICATED, and OPERATION_VERIFIED; mark unobserved states UNKNOWN and say what blocks the task. “Task ready” requires all capabilities actually required by that task to be available and verified to the level the work needs. Optional capabilities can remain not requested without blocking unrelated work.

Use public-code search such as the cataloged Grep MCP only when repository examples would materially help. Confirm the capability is actually available in the current host; if it is not, use the grep.app site through approved browsing when available, or recommend connecting the cataloged MCP if repeated code search is valuable. Treat snippets as examples, not proof of provider support, current API behavior, license compatibility or production suitability.'''
 },
}

def digest(text):
 return hashlib.sha256(text.encode('utf-8')).hexdigest()

def sections(text, source_id):
 lines=text.splitlines(keepends=True)
 if lines[0].strip() != '---':
  raise ValueError('Missing source frontmatter')
 body=next(i+1 for i in range(1,len(lines)) if lines[i].strip()=='---')
 starts=[(body,'Preamble')]
 fenced=False
 for i in range(body,len(lines)):
  if re.match(r'^\s*(```|~~~)',lines[i]):
   fenced=not fenced
  if not fenced:
   match=re.match(r'^(#{2,3}) (.+?)\s*$',lines[i])
   if match and (len(match[1])==2 or source_id=='sdd-spec-factory'):
    starts.append((i,match[2]))
 out=[]
 for n,(start,heading) in enumerate(starts):
  end=starts[n+1][0] if n+1<len(starts) else len(lines)
  chunk=''.join(lines[start:end])
  out.append({'id':f'{source_id}:{n:03d}','heading':heading,'start_line':start+1,'end_line':end,'sha256':digest(chunk),'text':chunk})
 return body+1,out

def build(root=ROOT):
 registry={'schema_version':1,'sources':[],'skills':[],'sectors':{}}
 existing=root/'library/indexes/skill-routes.json'
 if existing.exists():
  registry['source_commit']=json.loads(existing.read_text()).get('source_commit','UNKNOWN')
 else:
  try:
   registry['source_commit']=subprocess.check_output(['git','-C',str(root.parent/'v1'),'rev-parse','HEAD'],text=True).strip()
  except (OSError,subprocess.CalledProcessError):
   registry['source_commit']='UNKNOWN'
 outputs={}
 for source_id,(sector,groups) in CONFIG.items():
  rel=f'plugins/{source_id}/skills/{source_id}/SKILL.md'
  text=(root/rel).read_text(encoding='utf-8')
  body_start,spans=sections(text,source_id)
  expected=[h for headings in groups.values() for h in headings]
  actual=[s['heading'] for s in spans]
  if len(set(expected)) != len(expected) or set(expected)!=set(actual):
   raise ValueError(f'{source_id}: unreviewed/missing headings: {set(expected)^set(actual)}')
  source={'id':source_id,'path':rel,'sha256':digest(text),'body_start_line':body_start,'sections':[]}
  if source_id=='studio-prd':
   source['evolution']={'authorization':'STUDIO-PRD-002',
    'original_archive':'docs/migration/v1-frozen/'+rel,
    'note':'Current canonical content evolved after the recorded V1 baseline; original bytes remain archived.'}
  for group,headings in groups.items():
   sid=f'{sector}-{group}'
   chunks=[s for s in spans if s['heading'] in headings]
   path=f'skills/{sid}/SKILL.md'
   required=[] if group=='core' else [f'{sector}-core']
   if sid!='global-core':
    required.insert(0,'global-core')
   triggers=TRIGGERS.get(sid,[group.replace('-',' '),sector])
   entry={'id':sid,'sector':sector,'path':path,'source':source_id,'role':'core' if group=='core' else 'capability','requires':required,'triggers':triggers,'source_sections':[s['id'] for s in chunks],'reference_base':str(Path(rel).parent),'reference_fallback':f'plugins/{source_id}'}
   if sid in V2_OVERLAYS:
    entry['v2_overlays']=[V2_OVERLAYS[sid]['id']]
   reference_map=[]
   routed_text=''.join(item['text'] for item in chunks)
   if sid in V2_OVERLAYS:
    routed_text+='\n'+V2_OVERLAYS[sid]['text']
   for target in dict.fromkeys(re.findall(r'\]\(([^)]+)\)', routed_text)):
    if '://' in target or target.startswith('#'):
     continue
    local=target.split('#',1)[0]
    candidates=[root/Path(rel).parent/local,root/f'plugins/{source_id}'/local,root/local]
    found=next((candidate.resolve() for candidate in candidates if candidate.is_file()),None)
    reference_map.append({'original':target,'resolved':str(found.relative_to(root.resolve())) if found and found.is_relative_to(root.resolve()) else None,'status':'RESOLVED' if found and found.is_relative_to(root.resolve()) else 'NOT_VALIDATED'})
   entry['reference_map']=reference_map
   registry['skills'].append(entry)
   bucket=registry['sectors'].setdefault(sector,{'core':[],'capabilities':[]})
   bucket['core' if group=='core' else 'capabilities'].append(sid)
   description=f"Use for {sector} {group.replace('-', ' ')}: "+'; '.join(headings)+'. Load required core skills first.'
   wrapper=f'---\nname: {sid}\ndescription: {json.dumps(description,ensure_ascii=False)}\n---\n\n# The Office V2: {sid}\n\n'
   wrapper+=f'Source: `{rel}`. Read this selected skill in full and emit SKILL_RECEIPT.\n'
   wrapper+=f'Required skill IDs: {", ".join(required) or "none (global core)"}.\n'
   for dependency in required:
    wrapper+=f'Before acting, read repository-root `skills/{dependency}/SKILL.md` fully and include it in SKILL_RECEIPT.\n'
   wrapper+='The exact source sections follow unchanged. In those sections, “this SKILL”\nmeans this selected V2 skill plus its required core, not the entire V1 control plane.\n'
   wrapper+=f'Resolve original relative references and backticked resource paths from repository root `{Path(rel).parent}/`;\nfor plugin templates/scripts absent there, use repository root `plugins/{source_id}/`.\n'
   wrapper+='Never resolve inherited relative paths against this generated directory.\n'
   wrapper+='Load only the references whose conditions hold; retain all explicit mandatory gates.\n\n'
   if sid in V2_OVERLAYS:
    wrapper+=V2_OVERLAYS[sid]['text']+'\n\n'
   if reference_map:
    wrapper+='Canonical link resolution (repository-relative paths, not skill-directory-relative):\n'
    for ref in reference_map:
     wrapper+=f'- `{ref["original"]}`: `{ref["resolved"] or "NOT_VALIDATED; resolve active owner before use"}`\n'
    wrapper+='\n'
   for s in chunks:
    wrapper+=f'<!-- source-section:{s["id"]} sha256:{s["sha256"]} -->\n'+s['text']
   wrapper+='<!-- end of selected V2 skill -->\n'
   wrapper=wrapper.replace('# The Office V2:', 'V2 execution precedence: read repository-root `docs/operations/v2-execution-policy.md` before applying inherited governance; its bounded TRIVIAL exception is explicit.\n\n# The Office V2:', 1)
   outputs[path]=wrapper
   for s in chunks:
    source['sections'].append({k:v for k,v in s.items() if k!='text'}|{'skill_id':sid})
  source['sections'].sort(key=lambda x:x['start_line'])
  registry['sources'].append(source)
 registry['global_required']=['global-core']
 # Logical sectors reuse canonical implementation responsibilities without copies.
 for alias,target in {'frontend':'implementation','backend':'implementation','data':'implementation','ux-design':'ux','governance':'orchestrator'}.items():
  registry['sectors'][alias]=dict(registry['sectors'][target])
 # New bounded procedures fill V1 ownership gaps; these are explicit local additions.
 extras={
 'architecture-core':('architecture','Review and design software architecture under approved product scope.',
  'Inspect approved PRD, actual source topology, deployment constraints and dependency boundaries. Compare the smallest viable alternatives against measured scale, consistency, cost, recovery and security needs. Record chosen alternative, rejected options, trade-offs and validation in project ADRs. Do not change approved public contracts without a Task revision and authorization. Produce only diagrams useful to the decision. Hand approved constraints to SDD and require independent sector evidence.',
  ['plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-architecture.md']),
 'data-core':('data','Design or validate data models, migrations, queries and concurrency constraints.',
  'Inspect actual schemas, migrations, database/runtime versions and existing transactions before changes. Identify invariants, uniqueness, ownership, isolation and concurrency boundaries. Reuse repository migration and query conventions. Plan negative cases, rollback and recovery; route product implementation through the selected executor. A production migration or destructive operation requires its explicit target-specific gate. Return schema/query evidence and executed validation, never infer data integrity from lint success.',
  ['plugins/sdd-spec-factory/skills/sdd-spec-factory/references/technical-data-concurrency.md']),
 'documentation-core':('documentation','Document technical changes and user tutorials; assess documentation at every Task closure.',
  'Read approved Task and the actual current code or executable behavior being documented. Ask the shared Librarian for only the required documentation template. Trace each described screen, field, permission, error and outcome to its source revision or executed observation. Distinguish code-observed, runtime-tested and NOT_VALIDATED behavior. Use synthetic data in real captures; never fabricate screenshots. Keep help articles versioned in the product project and reuse them as the source for an optional Help Center. An absent UI or capture capability is a documented limitation, not permission to invent it. Preserve applicable Issue/contract/report gates.',
  ['docs/operations/documentation.md', 'library/documentation-templates/README.md']),
 'librarian-core':('librarian','Retrieve selected reusable resources by metadata and preserve provenance.',
  'Search Task-selected resources, project indexes, distributed catalog, inherited V1 catalogs, available host capabilities, then bounded official sources for an actual gap. Return stable resource ID, path, origin, version or UNKNOWN, license, purpose and compatibility evidence. Load only selected bodies. Reuse prior compatible results and invalidate on source or query drift. Separate distributed knowledge, private project/user extensions and runtime observations. Never publish local knowledge globally or store credentials. Evaluate external skill code, instructions, dependencies, license and permissions before recommending adoption; installation is a separate authorized operation. A catalog listing never proves availability, authentication or validation.',
  ['plugins/dev-workflow-standard/skills/dev-workflow-standard/references/capability-registry.md'])
 }
 for sid,(sector,description,procedure,refs) in extras.items():
  path=f'skills/{sid}/SKILL.md'
  outputs[path]=f'---\nname: {sid}\ndescription: {json.dumps(description)}\n---\n\n# {sid}\n\nLocal V2 capability addition. Before acting, read repository-root `skills/global-core/SKILL.md` fully and include it in SKILL_RECEIPT. Read the routed JSON, required sources with purpose and current revision before work; return SKILL_RECEIPT and your own evidence.\n\n{procedure}\n\nLoad these canonical references only when their domain is active:\n'+''.join(f'- `{ref}`\n' for ref in refs)
  registry['skills'].append({'id':sid,'sector':sector,'path':path,'source':None,'role':'core','requires':['global-core'],'triggers':[sector],'source_sections':[],'reference_base':'.','references':refs})
  registry['sectors'][sector]={'core':[sid],'capabilities':[]}
 # Explicit, inspected external integrations are capabilities, never mandatory core.
 external=root/'library/skills/external-skills.json'
 if external.exists():
  for item in json.loads(external.read_text(encoding='utf-8'))['skills']:
   if item['id'] in {entry['id'] for entry in registry['skills']}:
    raise ValueError('duplicate external capability ID')
   if item['sector'] not in registry['sectors'] or item['role']!='capability':
    raise ValueError('external capability must have an existing sector')
   registry['skills'].append(item)
   registry['sectors'][item['sector']]['capabilities'].append(item['id'])
 for alias,target in {'ux-design':'ux'}.items():
  registry['sectors'][alias]['capabilities']=list(registry['sectors'][target]['capabilities'])
 # Local capabilities have their own registry; do not mislabel them as upstream skills.
 local=root/'library/skills/local-skills.json'
 if local.exists():
  for item in json.loads(local.read_text(encoding='utf-8'))['skills']:
   if item['id'] in {entry['id'] for entry in registry['skills']}:
    raise ValueError('duplicate local capability ID')
   registry['skills'].append(item)
   registry['sectors'][item['sector']]['capabilities'].append(item['id'])
 registry['sectors']['governance']['capabilities']=list(registry['sectors']['orchestrator']['capabilities'])
 outputs['library/indexes/skill-routes.json']=json.dumps(registry,ensure_ascii=False,indent=2)+'\n'
 rows=['# Lossless V1 to V2 skill migration','',
 'This is a local functional migration, not a replacement execution engine. Original V1 resources remain preserved at canonical paths or explicit byte-identical archives. Studio PRD evolves under approved STUDIO-PRD-002 / ADR 006; its current slices cover the evolved canonical source, while the original remains in docs/migration/v1-frozen/. The vendored REA skill stays with its upstream runtime; it is not split or rewritten.','',
 'Each V1 body section is assigned once. Registry offsets are 1-based inclusive and SHA-256 hashes cover exact UTF-8 text. Frontmatter remains in the canonical source and is covered by the full source hash. Generated skills contain source text verbatim after an explicit reference-base adapter. Additive V2-only overlays are recorded in `library/indexes/skill-routes.json` and do not modify imported V1 files. Regenerate with `python scripts/build_skill_routes.py`; validate with `python scripts/build_skill_routes.py --check`.','',
 '## Additive V2 overlays','',
 *[f'- `{sid}` / `{overlay["id"]}`: {overlay["summary"]} Imported V1 content remains unchanged.' for sid,overlay in V2_OVERLAYS.items()],'',
 'Select global core, relevant sector core, and only capabilities required by the Task. A selected capability depends on its core. Explicit IDs take priority over lexical trigger hints; ambiguous matching must be resolved from Task scope, not treated as authorization. Shared executor aliases do not create duplicate skills.','',
 'Full behavioral parity across arbitrary agent hosts is NOT VALIDATED. Exact text coverage proves no section was dropped; it does not prove all models follow the instructions, nor tokens saved. SDD task-contract generation and implementation workflow remain deliberately cohesive and relatively large to preserve coupled gates. Legacy bundles continue loading their original monolithic SKILL.md, so selective-loading gains require the V2 router.','',
 '| V1 source | Section and original lines | V2 skill |','| --- | --- | --- |']
 for source in registry['sources']:
  for section in source['sections']:
   rows.append(f'| `{source["id"]}` | {section["heading"]} ({section["start_line"]}–{section["end_line"]}) | `{section["skill_id"]}` |')
 outputs['docs/migration/v1-to-v2.md']='\n'.join(rows)+'\n'
 return registry,outputs

def main():
 parser=argparse.ArgumentParser(description=__doc__)
 parser.add_argument('--check',action='store_true')
 args=parser.parse_args()
 _,outputs=build()
 drift=[]
 for rel,content in outputs.items():
  path=ROOT/rel
  if args.check:
   if not path.exists() or path.read_text(encoding='utf-8')!=content:
    drift.append(rel)
  else:
   path.parent.mkdir(parents=True,exist_ok=True)
   path.write_text(content,encoding='utf-8')
 if drift:
  parser.exit(1,'Generated skill drift: '+', '.join(drift)+'\n')
 print(f'{"Checked" if args.check else "Generated"} {len(outputs)-2} generated skills; external capabilities registered separately')

if __name__=='__main__':
 main()
