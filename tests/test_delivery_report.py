"""Actual offline reporting, evidence drift and safe portal preparation tests."""
import copy
import hashlib
import importlib.util
import json
from pathlib import Path
import subprocess
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location('delivery_report', ROOT/'scripts/delivery_report.py')
delivery = importlib.util.module_from_spec(spec); spec.loader.exec_module(delivery)
spec2 = importlib.util.spec_from_file_location('delivery_office', ROOT/'scripts/office.py')
office = importlib.util.module_from_spec(spec2); spec2.loader.exec_module(office)


class DeliveryReportTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.source = self.file('plan.md', 'Synthetic fixture, not a real project approval.')
        docs = {'status': 'NOT_APPLICABLE', 'reason': 'Fixture has no product behavior',
                'evidence': [self.source]}
        self.snapshot = {'schema_version': 1, 'project': 'Fixture', 'baseline_revision': '1',
                         'baseline_source': self.source,
                         'stages': [{'id': 'build', 'title': 'Build'}, {'id': 'verify', 'title': 'Verify'}],
                         'tasks': [{'id': 'T1', 'title': 'Fixture Task', 'contract_revision': '1',
                                    'source': self.source,
                                    'issue_url': 'https://github.com/example/fixture/issues/1',
                                    'documentation': {'technical': copy.deepcopy(docs), 'user': copy.deepcopy(docs)}}],
                         'items': [{'id': 'C1', 'task_id': 'T1', 'stage_id': 'build',
                                    'status': 'ACCEPTED', 'evidence': [self.source]},
                                   {'id': 'C2', 'task_id': 'T1', 'stage_id': 'verify',
                                    'status': 'PLANNED', 'evidence': []}]}

    def file(self, path, text):
        target = self.root/path; target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(text)
        return {'path': path, 'sha256': hashlib.sha256(target.read_bytes()).hexdigest()}

    def report(self):
        return delivery.summarize(self.snapshot, self.root)

    def test_unstarted_work_stays_in_denominator(self):
        report = self.report()
        self.assertEqual(report['total']['percent'], 50)
        self.assertEqual([s['percent'] for s in report['stages']], [100, 0])
        self.assertFalse(report['tasks'][0]['closure_ready'])
        self.assertIsNone(report['telemetry']['input_tokens'])

    def test_blocked_rework_and_unverified_never_earn_credit(self):
        for state in ['BLOCKED', 'REWORK', 'NOT_VALIDATED', 'IN_PROGRESS']:
            self.snapshot['items'][1]['status'] = state
            self.assertEqual(self.report()['total']['percent'], 50)

    def test_weighted_metric_and_no_empty_project_claim(self):
        self.snapshot['items'][1]['weight'] = 3
        self.assertEqual(self.report()['total']['percent'], 25)
        self.snapshot['items'] = []
        self.assertIsNone(self.report()['total']['percent'])
        self.assertFalse(self.report()['tasks'][0]['closure_ready'])

    def test_pending_docs_blocks_closure_even_with_accepted_code(self):
        self.snapshot['items'][1].update(status='ACCEPTED', evidence=[self.source])
        self.assertTrue(self.report()['tasks'][0]['closure_ready'])
        self.snapshot['tasks'][0]['documentation']['user'] = {
            'status': 'PENDING', 'reason': 'Tutorial not yet written', 'evidence': []}
        report = self.report()
        self.assertFalse(report['tasks'][0]['closure_ready'])
        self.assertEqual(report['tasks'][0]['canonical_done'], 'NOT_VERIFIED')

    def test_accepted_requires_evidence_and_resolved_docs_require_reason(self):
        self.snapshot['items'][0]['evidence'] = []
        with self.assertRaises(ValueError): self.report()
        self.snapshot['items'][0]['evidence'] = [self.source]
        self.snapshot['tasks'][0]['documentation']['technical']['reason'] = ''
        with self.assertRaises(ValueError): self.report()

    def test_source_changes_fail_closed(self):
        (self.root/'plan.md').write_text('Changed scope')
        with self.assertRaisesRegex(ValueError, 'stale evidence'): self.report()

    def test_path_escape_symlink_and_secret_refs_rejected(self):
        for path in ['../outside', '/etc/passwd', '.env', 'runtime-state/key.json', '.git/config', 'key.pem']:
            with self.assertRaises(ValueError):
                delivery.check_source(self.root, {'path': path, 'sha256': '0'*64})
        (self.root/'linked.md').symlink_to(self.root/'plan.md')
        with self.assertRaises(ValueError):
            delivery.check_source(self.root, {'path': 'linked.md', 'sha256': self.source['sha256']})

    def test_invalid_ids_states_urls_and_weights_rejected(self):
        original = copy.deepcopy(self.snapshot)
        for key, value in [('task_id', 'absent'), ('stage_id', 'absent'), ('status', 'DONE'),
                           ('weight', -1), ('weight', True), ('weight', float('nan')),
                           ('weight', float('inf'))]:
            self.snapshot = copy.deepcopy(original)
            self.snapshot['items'][0][key] = value
            with self.assertRaises(ValueError): self.report()
        self.snapshot = original
        self.snapshot['tasks'][0]['issue_url'] = 'https://evil.test/1'
        with self.assertRaises(ValueError): self.report()

    def test_duplicate_ids_and_json_keys_rejected(self):
        self.snapshot['items'].append(self.snapshot['items'][0])
        with self.assertRaises(ValueError): self.report()
        path = self.root/'duplicate.json'; path.write_text('{"a":1,"a":2}')
        with self.assertRaises(ValueError): delivery.load_snapshot(path)
        path.write_text('{"a":NaN}')
        with self.assertRaises(ValueError): delivery.load_snapshot(path)

    def test_portal_payload_compatible_allowlist_without_internal_sources(self):
        payload = delivery.portal_payload(self.report())
        row = payload['task_payloads'][0]
        self.assertEqual(set(row), {'issueNumber','issueUrl','title','description','stage','status','progress'})
        self.assertEqual(row['progress'], 50)
        self.assertEqual(row['status'], 'in_progress')
        self.assertNotIn('plan.md', json.dumps(payload))
        self.snapshot['items'][1].update(status='ACCEPTED', evidence=[self.source])
        self.assertEqual(delivery.portal_payload(self.report())['task_payloads'][0]['status'], 'in_progress')

    def test_portal_backlog_blocked_and_missing_issue(self):
        self.snapshot['items'][0].update(status='PLANNED', evidence=[])
        self.assertEqual(delivery.portal_payload(self.report())['task_payloads'][0]['status'], 'backlog')
        self.snapshot['items'][0]['status'] = 'BLOCKED'
        self.assertEqual(delivery.portal_payload(self.report())['task_payloads'][0]['status'], 'blocked')
        self.snapshot['tasks'][0]['issue_url'] = None
        self.assertEqual(delivery.portal_payload(self.report())['omitted_tasks'], ['T1'])

    def test_duplicate_issue_mapping_rejected(self):
        second = copy.deepcopy(self.snapshot['tasks'][0]); second['id'] = 'T2'
        self.snapshot['tasks'].append(second)
        with self.assertRaisesRegex(ValueError, 'duplicate canonical Issue'):
            self.report()

    def test_portal_export_rejects_mixed_customer_repositories(self):
        second = copy.deepcopy(self.snapshot['tasks'][0]); second['id'] = 'T2'
        second['issue_url'] = 'https://github.com/example/another-client/issues/2'
        self.snapshot['tasks'].append(second)
        with self.assertRaisesRegex(ValueError, 'one configured GitHub repository'):
            delivery.portal_payload(self.report())

    def test_cli_runs_formats_without_changing_input(self):
        path = self.root/'snapshot.json'; path.write_text(json.dumps(self.snapshot))
        original = path.read_bytes()
        for mode in ['json', 'markdown', 'portal']:
            result = subprocess.run(['python', str(ROOT/'scripts/delivery_report.py'), str(path),
                                     '--root', str(self.root), '--format', mode], capture_output=True,
                                    text=True, timeout=10)
            self.assertEqual(result.returncode, 0, result.stderr)
            self.assertTrue(result.stdout.strip())
        self.assertEqual(path.read_bytes(), original)

    def test_governance_alias_and_documentation_closure_routes(self):
        for sector in ['governance', 'orchestrator']:
            ids = [s['id'] for s in office.select_skills(ROOT, sector, ['delivery-metrics'])['skills']]
            self.assertEqual(ids, ['global-core', 'orchestrator-core', 'delivery-metrics'])
        docs = office.select_skills(ROOT, 'documentation')
        self.assertTrue(docs['selection_complete'])
        self.assertEqual([s['id'] for s in docs['skills']], ['global-core', 'documentation-core'])

    def test_upstream_writer_provenance(self):
        base = ROOT/'library/documentation-templates/upstream/awesome-copilot'
        provenance = json.loads((base/'provenance.json').read_text())
        for name, digest in provenance['files'].items():
            self.assertEqual(hashlib.sha256((base/name).read_bytes()).hexdigest(), digest)


if __name__ == '__main__': unittest.main()
