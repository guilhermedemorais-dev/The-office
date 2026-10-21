"""Preservation after approved canonical evolution and live V2 routing integrity."""
import hashlib
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def module(name,path):
 spec=importlib.util.spec_from_file_location(name,ROOT/path)
 value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value);return value
preserve=module('studio_preserve','scripts/verify_preservation.py')
office=module('studio_office','scripts/office.py')

class StudioEvolutionTests(unittest.TestCase):
 def setUp(self):
  self.tmp=tempfile.TemporaryDirectory();self.addCleanup(self.tmp.cleanup)
  self.root=Path(self.tmp.name)
  self.path='plugins/studio-prd/skills/studio-prd/SKILL.md'
  self.archive=preserve.ADAPTED[self.path]
  self.original=(ROOT/self.archive).read_bytes()
  inv={'source_commit':'original-fixture','files':[{'path':self.path,'sha256':hashlib.sha256(self.original).hexdigest()}]}
  (self.root/'docs/migration').mkdir(parents=True)
  (self.root/'docs/migration/v1-inventory.json').write_text(json.dumps(inv))
  target=self.root/self.archive;target.parent.mkdir(parents=True);target.write_bytes(self.original)
  live=self.root/self.path;live.parent.mkdir(parents=True);live.write_text('current evolved fixture')

 def test_archived_baseline_is_not_replaced_by_live_hash(self):
  self.assertEqual(preserve.verify(self.root)['failures'],[])
  (self.root/self.archive).write_bytes(b'corrupt archive')
  self.assertEqual(preserve.verify(self.root)['failures'],[self.path])

 def test_missing_archive_cannot_fall_back_to_original_looking_live_file(self):
  (self.root/self.archive).unlink();(self.root/self.path).write_bytes(self.original)
  self.assertEqual(preserve.verify(self.root)['failures'],[self.path])

 def test_all_studio_archive_mappings_keep_original_inventory_hashes(self):
  inventory=json.loads((ROOT/'docs/migration/v1-inventory.json').read_text())
  hashes={i['path']:i['sha256'] for i in inventory['files']}
  for path,destination in preserve.ADAPTED.items():
   if 'studio-prd' in path:
    self.assertEqual(hashlib.sha256((ROOT/destination).read_bytes()).hexdigest(),hashes[path])

 def test_product_routes_use_one_live_source_not_archived_or_competing_owner(self):
  registry=json.loads((ROOT/'library/indexes/skill-routes.json').read_text())
  product=[s for s in registry['skills'] if s['sector']=='product']
  self.assertEqual({s['source'] for s in product},{'studio-prd'})
  self.assertEqual({s['id'] for s in product},{'product-core','product-discovery','product-planning'})
  route=office.select_skills(ROOT,'product',['product-discovery'])
  self.assertEqual([s['id'] for s in route['skills']],['global-core','product-core','product-discovery'])
  for s in route['skills']:self.assertNotIn('v1-frozen',s['path'])

if __name__=='__main__':unittest.main()
