import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('office',ROOT/'scripts/office.py')
office=importlib.util.module_from_spec(spec); spec.loader.exec_module(office)

class OfficeTests(unittest.TestCase):
    def test_private_and_escape_paths_rejected(self):
        for path in ('../outside','/etc/passwd','.env.local','runtime-state/anything','.git/config','secret.pem'):
            with self.assertRaises(ValueError,msg=path): office.safe_path(ROOT,path)
    def test_metadata_search_reuses_without_network(self):
        result=office.search(ROOT,'backend',limit=3)
        self.assertTrue(result['results'])
        self.assertEqual(result['external_search'],'NOT_EXECUTED')
        self.assertNotIn('content',result['results'][0])
    def test_stale_cache_rejected_and_lower_priority_fallback(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp); (root/'library/indexes').mkdir(parents=True)
            (root/'ref.md').write_text('safe',encoding='utf-8')
            valid={'id':'resource','title':'payment','path':'ref.md','sha256':office.sha(root/'ref.md')}
            index={'resources':[valid]}; (root/'library/indexes/resources.json').write_text(json.dumps(index))
            bad=dict(valid,sha256='outdated'); (root/'task.json').write_text(json.dumps({'resources':[bad]}))
            result=office.search(root,'payment',[root/'task.json'])
            self.assertEqual(result['results'][0]['layer'],1)
            self.assertTrue(result['warnings'])
            (root/'ref.md').write_text('changed')
            self.assertTrue(office.search(root,'payment')['external_search_required'])
    def test_task_index_priority(self):
        with tempfile.TemporaryDirectory() as temp:
            path=Path(temp)/'index.json'
            resource=dict(office.search(ROOT,'backend')['results'][0]); resource.pop('layer');resource.pop('score')
            path.write_text(json.dumps({'resources':[resource]}))
            hits=office.search(ROOT,'backend',[path])['results']
            self.assertEqual(hits[0]['layer'],0)
            self.assertEqual(sum(x['id']==resource['id'] for x in hits),1)
    def test_unknown_sector_or_cross_sector_capability(self):
        with self.assertRaises(ValueError): office.select_skills(ROOT,'unknown')
        with self.assertRaises(ValueError): office.select_skills(ROOT,'backend',['unknown'])
    def test_plan_is_not_execution_and_core_only_is_incomplete(self):
        registry=office.read_json(ROOT/'library/indexes/skill-routes.json')
        sector=next(k for k,v in registry['sectors'].items() if v['capabilities'])
        result=office.select_skills(ROOT,sector)
        self.assertEqual(result['decision'],'PLANNED_NOT_EXECUTED')
        self.assertFalse(result['selection_complete'])
        self.assertTrue(all(x['read']=='FULL_SKILL_REQUIRED' for x in result['skills']))
    def contract(self):
        return office.read_json(ROOT/'docs/execution/THEOFFICE-V2-001.json')
    def test_real_contract_and_handoff_reject_stale_revision(self):
        contract=self.contract(); office.validate_contract(contract)
        with self.assertRaisesRegex(ValueError,'stale'):
            office.handoff(ROOT,'docs/execution/THEOFFICE-V2-001.json','invalid','harness','invalid')
    def test_invalid_dependency_and_duplicate_list_fail_closed(self):
        contract=self.contract(); contract['sectors']['harness']['depends_on'].append('harness')
        with self.assertRaises(ValueError): office.validate_contract(contract)
        contract=self.contract(); contract['execution_lists'].append(contract['execution_lists'][0])
        with self.assertRaises(ValueError): office.validate_contract(contract)

if __name__=='__main__': unittest.main()
