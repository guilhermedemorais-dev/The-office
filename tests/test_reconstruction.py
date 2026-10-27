"""Negative coverage cases from reviewed Replica behavior; no external services."""
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
from pathlib import Path
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


coverage = load('reconstruction_coverage', 'library/reconstruction/coverage.py')
generator = load('reconstruction_routes', 'scripts/build_skill_routes.py')


class CoverageTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name)
        (self.root / 'run.txt').write_text('Executed positive and negative fixture checks.\n')
        self.contract = {
            'schema_version': 2, 'task_id': 'TEST-MODULE', 'contract_revision': '3',
            'acceptance_criteria': [{'id': 'AC-1', 'validation': 'TEST-1'}],
            'required_tests': [{'id': 'TEST-1'}],
        }
        (self.root / 'task.json').write_text(json.dumps(self.contract))
        self.digest = coverage.sha256(self.root / 'task.json')
        self.case = {'test_id': 'TEST-1', 'status': 'PASS', 'source_revision': 'artifact-1',
                     'path': 'run.txt', 'sha256': coverage.sha256(self.root / 'run.txt')}
        self.ledger = {
            'task_id': 'TEST-MODULE', 'contract_revision': '3',
            'contract_sha256': self.digest, 'source_revision': 'artifact-1',
            'criteria': [{'id': 'AC-1', 'declared_state': 'IMPLEMENTED',
                          'cases': [copy.deepcopy(self.case)]}],
        }

    def check(self):
        return coverage.check(self.contract, self.ledger, self.root, 'artifact-1', self.digest)

    def test_current_evidence_is_present_but_never_release_authorization(self):
        report = self.check()
        self.assertEqual(report['status'], 'EVIDENCE_PRESENT')
        self.assertFalse(report['release_authorized'])

    def test_missing_critical_cannot_be_hidden_by_many_completed_criteria(self):
        for n in range(2, 12):
            self.contract['acceptance_criteria'].append({'id': f'AC-{n}'})
            self.ledger['criteria'].append({'id': f'AC-{n}', 'declared_state': 'IMPLEMENTED',
                                            'cases': [copy.deepcopy(self.case)]})
        self.ledger['criteria'][0]['cases'] = []
        self.assertEqual(self.check()['status'], 'INCOMPLETE')

    def test_skip_partial_and_declaration_only_do_not_verify(self):
        for state in ('SKIP', 'PARTIAL', 'PLANNED', 'UNKNOWN'):
            with self.subTest(state=state):
                self.ledger['criteria'][0]['declared_state'] = state
                self.assertEqual(self.check()['status'], 'INCOMPLETE')

    def test_empty_ledger_is_incomplete_not_success(self):
        self.ledger['criteria'] = []
        self.assertEqual(self.check()['status'], 'INCOMPLETE')

    def test_failed_not_run_and_stale_case_block(self):
        for status in ('FAIL', 'NOT_RUN'):
            self.ledger['criteria'][0]['cases'][0]['status'] = status
            self.assertEqual(self.check()['status'], 'INCOMPLETE')
        self.ledger['criteria'][0]['cases'][0]['status'] = 'PASS'
        self.ledger['criteria'][0]['cases'][0]['source_revision'] = 'old-artifact'
        self.assertEqual(self.check()['status'], 'INCOMPLETE')

    def test_stale_ledger_blocks_even_when_case_is_current(self):
        self.ledger['source_revision'] = 'old-artifact'
        report = self.check()
        self.assertEqual(report['status'], 'INCOMPLETE')
        self.assertEqual(report['criteria_with_evidence'], [])

    def test_changed_or_empty_evidence_blocks(self):
        for text in ('changed', ''):
            (self.root / 'run.txt').write_text(text)
            self.assertEqual(self.check()['status'], 'INCOMPLETE')

    def test_wrong_task_revision_contract_bytes_and_unknown_ids_rejected(self):
        for key, value in [('task_id', 'other'), ('contract_revision', '2'),
                           ('contract_sha256', '0' * 64)]:
            with self.subTest(key=key):
                old = self.ledger[key]
                self.ledger[key] = value
                with self.assertRaises(ValueError):
                    self.check()
                self.ledger[key] = old
        self.ledger['criteria'][0]['id'] = 'made-up'
        with self.assertRaises(ValueError):
            self.check()

    def test_duplicate_criteria_and_unknown_tests_rejected(self):
        self.ledger['criteria'].append(copy.deepcopy(self.ledger['criteria'][0]))
        with self.assertRaises(ValueError):
            self.check()
        self.ledger['criteria'].pop()
        self.ledger['criteria'][0]['cases'][0]['test_id'] = 'made-up'
        with self.assertRaises(ValueError):
            self.check()

    def test_canonical_test_mapping_and_all_required_tests_are_enforced(self):
        self.contract['required_tests'].append({'id': 'TEST-2'})
        self.assertEqual(self.check()['status'], 'INCOMPLETE')
        self.ledger['criteria'][0]['cases'][0]['test_id'] = 'TEST-2'
        self.ledger['criteria'].append({'id': 'AC-2', 'declared_state': 'IMPLEMENTED',
                                        'cases': [copy.deepcopy(self.case)]})
        self.contract['acceptance_criteria'].append({'id': 'AC-2'})
        report = self.check()
        self.assertEqual(report['status'], 'INCOMPLETE')
        self.assertTrue(any('canonical criterion validation' in g for g in report['gaps']))

    def test_external_absolute_traversal_symlink_and_missing_evidence_rejected(self):
        for path in ('/etc/passwd', '../outside', 'missing.txt'):
            self.ledger['criteria'][0]['cases'][0]['path'] = path
            with self.assertRaises(ValueError):
                self.check()
        (self.root / 'link.txt').symlink_to(self.root / 'run.txt')
        self.ledger['criteria'][0]['cases'][0]['path'] = 'link.txt'
        with self.assertRaises(ValueError):
            self.check()

    def test_cli_exit_codes(self):
        args = ['--project-root', str(self.root), '--contract', 'task.json',
                '--ledger', 'ledger.json', '--source-revision', 'artifact-1']
        with contextlib.redirect_stdout(io.StringIO()), contextlib.redirect_stderr(io.StringIO()):
            (self.root / 'ledger.json').write_text(json.dumps(self.ledger))
            self.assertEqual(coverage.main(args), 0)
            self.ledger['criteria'][0]['declared_state'] = 'SKIP'
            (self.root / 'ledger.json').write_text(json.dumps(self.ledger))
            self.assertEqual(coverage.main(args), 1)
            (self.root / 'ledger.json').write_text('[]')
            self.assertEqual(coverage.main(args), 2)


class ReconstructionRoutingTests(unittest.TestCase):
    def test_overlay_references_are_registered_not_only_rendered(self):
        registry, outputs = generator.build()
        routes = {row['id']: row for row in registry['skills']}
        expected = {
            'product-discovery': 'library/reconstruction/README.md',
            'reverse-engineering-investigation': 'library/reconstruction/README.md',
            'sdd-specifications': 'library/reconstruction/README.md',
            'qa-validation': 'library/reconstruction/README.md',
            'orchestrator-delegation': 'integrations/memory/README.md',
            'environment-bootstrap': 'docs/operations/opencode.md',
        }
        for skill_id, ref in expected.items():
            with self.subTest(skill=skill_id):
                route = routes[skill_id]
                self.assertIn(generator.V2_OVERLAYS[skill_id]['id'], route['v2_overlays'])
                self.assertIn(ref, outputs[route['path']])
                refs = {item['original']: item for item in route['reference_map']}
                self.assertIn(ref, refs)
                if (ROOT / ref).exists():
                    self.assertEqual(refs[ref]['resolved'], ref)
                    self.assertEqual(refs[ref]['status'], 'RESOLVED')

    def test_generated_skills_keep_original_sections_byte_exact(self):
        registry, outputs = generator.build()
        routes = {row['id']: row for row in registry['skills']}
        for source in registry['sources']:
            lines = (ROOT / source['path']).read_text().splitlines(keepends=True)
            for section in source['sections']:
                if section['skill_id'] not in generator.V2_OVERLAYS:
                    continue
                original = ''.join(lines[section['start_line'] - 1:section['end_line']])
                self.assertEqual(hashlib.sha256(original.encode()).hexdigest(), section['sha256'])
                self.assertIn(original, outputs[routes[section['skill_id']]['path']])


if __name__ == '__main__':
    unittest.main()
