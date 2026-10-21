"""Independent QA: hostile inputs at read-only V2 routing boundaries.

Fixtures are synthetic contracts, not owner/dependency approval evidence.
"""
import copy
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('office_qa', ROOT / 'scripts/office.py')
office = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(office)


class HandoffBoundaryTests(unittest.TestCase):
    def setUp(self):
        self.folder = tempfile.TemporaryDirectory()
        self.addCleanup(self.folder.cleanup)
        self.root = Path(self.folder.name)
        self.contract = copy.deepcopy(office.read_json(ROOT / 'docs/execution/THEOFFICE-V2-001.json'))
        for ref in self.contract['references']:
            ref['project_path'] = 'source.md'
            ref['section'] = ''
        (self.root / 'source.md').write_text('# Source\n\n## Existing anchor\n\nVerified fixture.\n', encoding='utf-8')
        self.path = self.root / 'contract.json'
        self.execution_list = next(x for x in self.contract['execution_lists'] if x['list_id'] == 'MT-10/checklist')

    def handoff(self):
        self.path.write_text(json.dumps(self.contract), encoding='utf-8')
        return office.handoff(self.root, 'contract.json', 'MT-10/checklist', 'qa', '1')

    def test_valid_handoff_remains_blocked_from_execution_without_receipts(self):
        plan = self.handoff()
        self.assertEqual(plan['decision'], 'PLANNED_NOT_EXECUTED')
        self.assertTrue(plan['execution_blockers'])
        self.assertEqual(plan['depends_on'], ['backend', 'documentation'])

    def test_unknown_phase_cannot_be_routed_as_validation(self):
        self.execution_list['phase'] = 'approve-and-deploy'
        with self.assertRaises(ValueError):
            self.handoff()

    def test_missing_checklist_cannot_form_executable_list(self):
        del self.execution_list['checklist']
        with self.assertRaises(ValueError):
            self.handoff()

    def test_changed_microtask_owner_cannot_inherit_qa_list_authority(self):
        item = next(x for x in self.contract['microtasks'] if x['id'] == 'MT-10')
        item['owner_skill'] = 'security-standard'
        with self.assertRaises(ValueError):
            self.handoff()

    def test_missing_required_path_anchor_blocks_handoff(self):
        self.contract['references'][0]['project_path'] = 'source.md#absent-anchor'
        with self.assertRaises(ValueError):
            self.handoff()

    def test_missing_required_section_field_anchor_blocks_handoff(self):
        self.contract['references'][0]['section'] = '#absent-anchor'
        with self.assertRaises(ValueError):
            self.handoff()

    def test_fenced_example_heading_is_not_a_required_anchor(self):
        (self.root / 'source.md').write_text('# Source\n\n```md\n## Example only\n```\n', encoding='utf-8')
        self.contract['references'][0]['project_path'] = 'source.md#example-only'
        with self.assertRaises(ValueError):
            self.handoff()

    def test_known_required_anchor_remains_usable(self):
        self.contract['references'][0]['project_path'] = 'source.md#existing-anchor'
        self.assertEqual(self.handoff()['decision'], 'PLANNED_NOT_EXECUTED')

    def test_missing_required_file_blocks_handoff(self):
        (self.root / 'source.md').unlink()
        with self.assertRaises(ValueError):
            self.handoff()

    def test_duplicate_microtask_identifier_blocks_resolution(self):
        self.contract['microtasks'].append(copy.deepcopy(self.contract['microtasks'][0]))
        with self.assertRaises(ValueError):
            self.handoff()

    def test_unknown_dependency_microtask_blocks_resolution(self):
        self.execution_list['depends_on'] = ['MT-NOT-EXISTING']
        with self.assertRaises(ValueError):
            self.handoff()

    def test_narrowed_list_does_not_omit_global_protected_paths(self):
        plan = self.handoff()
        self.assertEqual(plan['global_constraints']['protected_paths'], self.contract['protected_paths'])


class LibraryAndSkillBoundaryTests(unittest.TestCase):
    def test_symlink_escape_is_rejected(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'outside').mkdir()
            (root / 'repo').mkdir()
            (root / 'repo/link').symlink_to(root / 'outside', target_is_directory=True)
            with self.assertRaises(ValueError):
                office.safe_path(root / 'repo', 'link/secret.txt')

    def test_missing_capability_body_blocks_selection(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'library/indexes').mkdir(parents=True)
            registry = {'global_required': [], 'sectors': {'qa': {'core': [], 'capabilities': ['qa-validation']}},
                        'skills': [{'id': 'qa-validation', 'path': 'missing/SKILL.md', 'requires': []}]}
            (root / 'library/indexes/skill-routes.json').write_text(json.dumps(registry))
            with self.assertRaises(ValueError):
                office.select_skills(root, 'qa', ['qa-validation'])

    def test_cyclic_capability_dependencies_block_selection(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / 'library/indexes').mkdir(parents=True)
            registry = {'global_required': [], 'sectors': {'qa': {'core': [], 'capabilities': ['a']}},
                        'skills': [{'id': 'a', 'path': 'a.md', 'requires': ['b']},
                                   {'id': 'b', 'path': 'b.md', 'requires': ['a']}]}
            (root / 'library/indexes/skill-routes.json').write_text(json.dumps(registry))
            with self.assertRaises(ValueError):
                office.select_skills(root, 'qa', ['a'])

    def test_library_miss_requests_research_without_claiming_execution(self):
        result = office.search(ROOT, 'qa_nonexistent_resource_763196')
        self.assertEqual(result['results'], [])
        self.assertTrue(result['external_search_required'])
        self.assertEqual(result['external_search'], 'NOT_EXECUTED')


if __name__ == '__main__':
    unittest.main()
