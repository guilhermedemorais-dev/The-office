"""Execute actual V2 selection, verify inherited provenance and exercise Plop."""
import hashlib
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('consolidated_office',ROOT/'scripts/office.py')
office=importlib.util.module_from_spec(spec);spec.loader.exec_module(office)

class ConsolidatedV2Tests(unittest.TestCase):
 def test_hig_selection_is_explicit_and_alias_compatible(self):
  for sector in ['ux','ux-design']:
   selected=office.select_skills(ROOT,sector,['apple-hig-designer'])
   self.assertEqual([s['id'] for s in selected['skills']],['global-core','ux-core','apple-hig-designer'])
   self.assertNotIn('apple-hig-designer',[s['id'] for s in office.select_skills(ROOT,sector)['skills']])
  with self.assertRaises(ValueError):office.select_skills(ROOT,'backend',['apple-hig-designer'])

 def test_hig_upstream_exact_bytes(self):
  records=json.loads((ROOT/'library/skills/external-skills.json').read_text())['skills']
  item=next(x for x in records if x['id']=='apple-hig-designer')
  base=ROOT/item['upstream_directory']
  for path,digest in item['upstream_sha256'].items():
   self.assertEqual(hashlib.sha256((base/path).read_bytes()).hexdigest(),digest,path)
  provenance=json.loads((base/'provenance.json').read_text())
  for file in provenance['files']:
   self.assertEqual(hashlib.sha256((base/file['destination']).read_bytes()).hexdigest(),file['sha256'])

 def test_selected_cli_records_preserve_javascript_and_optional_pipeline(self):
  tools={t['id']:t for t in json.loads((ROOT/'library/tools/stack-clis.json').read_text())['tools']}
  self.assertEqual(tools['react-vite-create']['install_argv_template'][-1],'REACT_TEMPLATE')
  for id in ['tailwind-vite','tailwind-cli','plop-cli','compose-scope']:
   self.assertIn(id,tools)
   self.assertEqual(tools[id]['verification'],'NOT_VALIDATED')

 @unittest.skipUnless(os.environ.get('OFFICE_PLOP_BINARY'),'optional actual Plop runtime not supplied')
 def test_real_plop_generates_once_and_rejects_traversal(self):
  cli=os.environ['OFFICE_PLOP_BINARY']
  source=str(ROOT/'library/templates/codegen/react-js/plopfile.cjs')
  with tempfile.TemporaryDirectory() as folder:
   argv=[cli,'--plopfile',source,'react-component','--','--name']
   result=subprocess.run(argv+['CustomerCard'],cwd=folder,capture_output=True,text=True,timeout=30)
   dest=Path(folder)/'src/components/CustomerCard/CustomerCard.jsx'
   self.assertTrue(dest.exists(),result.stdout+result.stderr)
   original=dest.read_bytes();self.assertIn(b'export function CustomerCard',original)
   again=subprocess.run(argv+['CustomerCard'],cwd=folder,capture_output=True,text=True,timeout=30)
   self.assertIn('already exists',again.stdout+again.stderr);self.assertEqual(dest.read_bytes(),original)
   invalid=subprocess.run(argv+['../../Escape'],cwd=folder,capture_output=True,text=True,timeout=30)
   self.assertIn('PascalCase',invalid.stdout+invalid.stderr)
   self.assertEqual([p.name for p in Path(folder).rglob('*.jsx')],['CustomerCard.jsx'])

if __name__=='__main__':unittest.main()
