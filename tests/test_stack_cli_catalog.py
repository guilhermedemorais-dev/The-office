"""Exercise catalog lookup and ensure metadata rebuilds without tool execution."""
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import sys
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('cli_catalog_build',ROOT/'scripts/build_library.py')
builder=importlib.util.module_from_spec(spec)
spec.loader.exec_module(builder)

class StackCliCatalogTests(unittest.TestCase):
 def test_actual_lookup_reuses_documented_catalog(self):
  for query in ['nextjs','nestjs','react-vite-create','vue-create-vue','python-pip','nx-cli','opentofu-cli']:
   result=subprocess.run([sys.executable,str(ROOT/'scripts/office.py'),'search',query],capture_output=True,text=True,check=True)
   data=json.loads(result.stdout)
   self.assertIn('library/tools/stack-clis.json',[x['path'] for x in data['results']],query)
   self.assertFalse(data['external_search_required'])
   self.assertEqual(data['external_search'],'NOT_EXECUTED')

 def test_metadata_rebuild_tracks_catalog_and_policy(self):
  resources={x['path']:x for x in builder.build(ROOT)['resources']}
  for path in ['library/tools/stack-clis.json','library/tools/stack-cli-policy.md']:
   self.assertEqual(resources[path]['sha256'],hashlib.sha256((ROOT/path).read_bytes()).hexdigest())
   self.assertEqual(resources[path]['status'],'CATALOGED_NOT_EXECUTED')
  saved=json.loads((ROOT/'library/indexes/resources.json').read_text())
  self.assertEqual(saved,builder.build(ROOT))

if __name__=='__main__':unittest.main()
