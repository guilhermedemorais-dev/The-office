"""Lossless coverage, generation drift and prerequisite safety for skill migration."""
import importlib.util
import json
from pathlib import Path
import re
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('build_skill_routes',ROOT/'scripts/build_skill_routes.py')
generator=importlib.util.module_from_spec(spec)
spec.loader.exec_module(generator)

class SkillRoutesTests(unittest.TestCase):
 @classmethod
 def setUpClass(cls):
  cls.registry=json.loads((ROOT/'library/indexes/skill-routes.json').read_text())
  cls.skills={s['id']:s for s in cls.registry['skills']}

 def test_all_canonical_skills_are_covered_without_vendor_rewrite(self):
  sources={s['path'] for s in self.registry['sources']}
  canonical={str(p.relative_to(ROOT)) for p in ROOT.glob('plugins/*/skills/*/SKILL.md')}
  self.assertEqual(sources,canonical)
  self.assertEqual(len(sources),13)
  self.assertIn("plugins/ui-ux-standard/skills/cinematic-web-standard/SKILL.md",sources)

 def test_exact_source_and_destination_section_equivalence(self):
  for source in self.registry['sources']:
   text=(ROOT/source['path']).read_text(encoding='utf-8')
   self.assertEqual(generator.digest(text),source['sha256'])
   lines=text.splitlines(keepends=True)
   cursor=source['body_start_line']
   reconstructed=[]
   for section in source['sections']:
    self.assertEqual(section['start_line'],cursor,section['id'])
    chunk=''.join(lines[section['start_line']-1:section['end_line']])
    self.assertEqual(generator.digest(chunk),section['sha256'])
    dest=(ROOT/self.skills[section['skill_id']]['path']).read_text(encoding='utf-8')
    marker=f'<!-- source-section:{section["id"]} sha256:{section["sha256"]} -->\n'
    self.assertEqual(dest.count(marker),1)
    self.assertIn(marker+chunk,dest)
    reconstructed.append(chunk)
    cursor=section['end_line']+1
   self.assertEqual(cursor,len(lines)+1)
   self.assertEqual(''.join(reconstructed),''.join(lines[source['body_start_line']-1:]))

 def test_no_generation_drift(self):
  _,outputs=generator.build()
  for path,content in outputs.items():
   self.assertEqual((ROOT/path).read_text(encoding='utf-8'),content,path)

 def test_dependencies_exist_are_acyclic_and_include_own_core(self):
  def visit(sid,ancestors):
   self.assertNotIn(sid,ancestors)
   for dependency in self.skills[sid]['requires']:
    self.assertIn(dependency,self.skills)
    visit(dependency,ancestors|{sid})
  for sid,skill in self.skills.items():
   visit(sid,set())
   if skill['role']=='capability':
    self.assertIn(skill['sector']+'-core',skill['requires'])
   self.assertTrue((ROOT/skill['path']).is_file())
   self.assertTrue((ROOT/skill['reference_base']).is_dir())

 def test_direct_host_activation_preserves_global_governance(self):
  self.assertEqual(self.skills['global-core']['requires'],[])
  for sid,skill in self.skills.items():
   if sid=='global-core':
    continue
   self.assertIn('global-core',skill['requires'],sid)
   text=(ROOT/skill['path']).read_text(encoding='utf-8')
   for dependency in skill['requires']:
    self.assertIn(f'`skills/{dependency}/SKILL.md`',text,sid)

 def test_new_sectors_have_concrete_procedures_and_resolvable_references(self):
  for sector in ['architecture','data','documentation','librarian']:
   sid=sector+'-core'
   self.assertEqual(self.registry['sectors'][sector]['core'],[sid])
   text=(ROOT/self.skills[sid]['path']).read_text()
   self.assertIn('SKILL_RECEIPT',text)
   for ref in self.skills[sid].get('references',[]):
    self.assertTrue((ROOT/ref).is_file(),ref)

 def test_fences_do_not_create_fake_sections(self):
  text='---\nname: demo\n---\n\n# Demo\n\n```md\n## Not a section\n```\n\n## Actual\nContent\n'
  _,sections=generator.sections(text,'demo')
  self.assertEqual([s['heading'] for s in sections],['Preamble','Actual'])

 def test_implementation_safety_workflow_is_always_in_core(self):
  text=(ROOT/self.skills['implementation-core']['path']).read_text()
  self.assertIn('## Workflow',text)
  self.assertIn('MINIMAL_CODE_GATE',text)
  self.assertIn('REUSE_INVENTORY',text)

 def test_trivial_ui_does_not_require_full_component_catalog(self):
  selected=['global-core','ux-core','ux-visual-validation']
  self.assertNotIn('ux-components',selected)
  self.assertNotIn('sdd-core',selected)
  for sid in selected:
   for required in self.skills[sid]['requires']:
    self.assertIn(required,selected)
  combined=''.join((ROOT/self.skills[sid]['path']).read_text() for sid in selected)
  self.assertIn('## Visual QA Checklist',combined)
  self.assertNotIn('## Component Intelligence',combined)

if __name__=='__main__':
 unittest.main()
