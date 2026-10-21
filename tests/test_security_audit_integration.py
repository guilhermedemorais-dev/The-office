"""Exercise provenance and actual capability routing, without running an audit."""
import hashlib
import importlib.util
import json
from pathlib import Path
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('audit_office',ROOT/'scripts/office.py')
office=importlib.util.module_from_spec(spec)
spec.loader.exec_module(office)

class SecurityAuditIntegrationTests(unittest.TestCase):
 def test_upstream_files_preserved_and_pinned(self):
  record=json.loads((ROOT/'library/skills/external-skills.json').read_text())['skills'][0]
  self.assertEqual(record['revision'],'c1c8a8c1471069fb0e188eeaff69b8e8db6564a8')
  base=ROOT/record['upstream_directory']
  self.assertEqual(set(record['upstream_sha256']),{str(p.relative_to(base)) for p in base.rglob('*') if p.is_file()})
  for rel,digest in record['upstream_sha256'].items():
   self.assertEqual(hashlib.sha256((base/rel).read_bytes()).hexdigest(),digest,rel)
  self.assertIn('Cloudflare',(base/'LICENSE').read_text())

 def test_security_selects_audit_with_core_only_when_requested(self):
  selected=office.select_skills(ROOT,'security',['security-audit'])
  self.assertEqual([s['id'] for s in selected['skills']],['global-core','security-core','security-audit'])
  self.assertNotIn('security-audit',[s['id'] for s in office.select_skills(ROOT,'security')['skills']])
  self.assertNotIn('security-audit',[s['id'] for s in office.select_skills(ROOT,'ux')['skills']])
  with self.assertRaises(ValueError):office.select_skills(ROOT,'ux',['security-audit'])

 def test_companion_links_are_local_and_resolve(self):
  import re
  base=ROOT/'skills/security-audit/upstream'
  for file in base.glob('*.md'):
   for link in re.findall(r'\]\(([^)]+)\)',file.read_text()):
    if '://' not in link and not link.startswith('#'):
     self.assertTrue((base/link.split('#')[0]).is_file(),f'{file.name}: {link}')

 def test_central_catalog_is_searchable(self):
  index=json.loads((ROOT/'library/indexes/resources.json').read_text())
  entry=next(x for x in index['resources'] if x['path']=='library/skills/external-skills.json')
  self.assertIn('security-audit',entry['keywords'])
  self.assertEqual(entry['sha256'],hashlib.sha256((ROOT/entry['path']).read_bytes()).hexdigest())

if __name__=='__main__':unittest.main()
