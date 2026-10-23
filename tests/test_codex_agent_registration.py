"""Synthetic registration tests; never access the developer's live CODEX_HOME."""
import contextlib
import importlib.util
import io
import json
import os
from pathlib import Path
import tempfile
import tomllib
import unittest
from unittest.mock import patch


ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location('codex_registration', ROOT / 'scripts/register_codex_agents.py')
REG = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(REG)


class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.base = Path(self.temp.name)
        self.bundle = self.base / 'bundle with spaces'
        self.home = self.base / 'synthetic-codex'
        for relative in ('AGENTS.md', 'docs/operations/v2-execution-policy.md', 'scripts/office.py'):
            path = self.bundle / relative
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('fixture', encoding='utf-8')
        for sector in REG.SECTORS:
            path = self.bundle / 'agents' / sector / 'AGENT.md'
            path.parent.mkdir(parents=True)
            path.write_text(f'# {sector} contract\n\n## Responsibility\n\nOwn {sector}.\n\n## Outputs\n\nEvidence.\n', encoding='utf-8')

    def cli(self, command):
        output = io.StringIO()
        with contextlib.redirect_stdout(output):
            code = REG.main([command, '--bundle-root', str(self.bundle), '--codex-home', str(self.home)])
        return code, json.loads(output.getvalue())

    def write(self, name, content):
        path = self.home / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_bytes(content)
        return path

    def files(self):
        return {str(p.relative_to(self.home)): p.read_bytes()
                for p in self.home.rglob('*') if p.is_file()} if self.home.exists() else {}

    def test_plan_check_never_create_missing_home(self):
        self.assertEqual(self.cli('plan')[0], 0)
        self.assertEqual(self.cli('check')[0], 1)
        self.assertFalse(self.home.exists())

    def test_apply_generates_fifteen_profiles_from_contracts_and_is_idempotent(self):
        code, result = self.cli('apply')
        self.assertEqual((code, result['status']), (0, 'APPLIED'))
        config = tomllib.loads((self.home / 'config.toml').read_text(encoding='utf-8'))
        self.assertEqual(len(config['agents']), 15)
        for name, entry in config['agents'].items():
            profile = tomllib.loads(Path(entry['config_file']).read_text(encoding='utf-8'))
            self.assertEqual(profile['name'], name)
            self.assertIn('Evidence.', profile['developer_instructions'])
            self.assertNotIn('model', profile)
            self.assertNotIn('sandbox_mode', profile)
        before = self.files()
        self.assertEqual(self.cli('check')[0], 0)
        self.assertEqual(self.cli('apply')[1]['status'], 'CONFIGURED')
        self.assertEqual(self.files(), before)
        self.assertEqual(len(list((self.home / '.office-agent-backups').iterdir())), 1)
        self.assertEqual(result['agent_execution'], 'NOT_VALIDATED')

    def test_preserves_toml_bytes_bom_crlf_and_unrelated_settings(self):
        original = (b'\xef\xbb\xbf# private comment\r\nmodel = "fixture"\r\n'
                    b'[mcp_servers.synthetic]\r\nurl = "https://example.invalid"\r\n'
                    b'[agents]\r\nmax_threads = 2\r\n')
        self.write('config.toml', original)
        user = b'\xef\xbb\xbfUser instructions\r\n'
        self.write('AGENTS.md', user)
        code, result = self.cli('apply')
        self.assertEqual(code, 0)
        self.assertTrue((self.home / 'config.toml').read_bytes().startswith(original))
        self.assertTrue((self.home / 'AGENTS.md').read_bytes().startswith(user))
        backup = self.home / result['backup']
        records = json.loads((backup / 'manifest.json').read_text())
        config_record = next(x for x in records if x['path'] == 'config.toml')
        self.assertEqual((backup / config_record['backup']).read_bytes(), original)
        self.assertNotIn('fixture', json.dumps(result))

    def test_invalid_toml_is_blocked_without_secret_in_error_or_writes(self):
        self.write('config.toml', b'secret = "DO_NOT_DISCLOSE\n')
        before = self.files()
        for command in ('plan', 'check', 'apply'):
            code, result = self.cli(command)
            self.assertEqual(code, 2)
            self.assertNotIn('DO_NOT_DISCLOSE', json.dumps(result))
            self.assertEqual(before, self.files())

    def test_registration_collision_and_custom_profile_block(self):
        self.write('config.toml', b'[agents.office_sdd]\nconfig_file="custom.toml"\n')
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)
        (self.home / 'config.toml').unlink()
        self.write('agents/office_sdd.toml', b'developer_instructions="custom"\n')
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)

    def test_modified_managed_body_and_invalid_markers_block(self):
        self.assertEqual(self.cli('apply')[0], 0)
        path = self.home / 'AGENTS.md'
        path.write_bytes(path.read_bytes().replace(b'No automatic merge', b'Allow automatic merge'))
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)
        path.write_bytes(REG.END.encode())
        self.assertEqual(self.cli('plan')[0], 2)

    def test_content_after_managed_block_preserved(self):
        self.assertEqual(self.cli('apply')[0], 0)
        path = self.home / 'AGENTS.md'
        path.write_bytes(path.read_bytes() + b'\nUser suffix\r\n')
        self.assertEqual(self.cli('apply')[1]['status'], 'CONFIGURED')
        self.assertTrue(path.read_bytes().endswith(b'\nUser suffix\r\n'))

    def test_overrides_and_disabled_agents_block_before_writes(self):
        cases = [('AGENTS.override.md', b'ignore other docs'),
                 ('config.toml', b'model_instructions_file="custom.md"\n'),
                 ('config.toml', b'[features]\nmulti_agent=false\n')]
        for name, content in cases:
            with self.subTest(name=name, content=content):
                path = self.write(name, content)
                before = self.files()
                self.assertEqual(self.cli('apply')[0], 2)
                self.assertEqual(self.files(), before)
                path.unlink()

    def test_missing_contract_blocks_before_creating_home(self):
        (self.bundle / 'agents/sdd/AGENT.md').unlink()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertFalse(self.home.exists())

    def test_symlink_target_or_ancestor_rejected(self):
        outside = self.base / 'outside'
        outside.mkdir()
        self.home.mkdir()
        linked = self.home / 'agents'
        try:
            linked.symlink_to(outside, target_is_directory=True)
        except OSError:
            self.skipTest('host does not permit symlink fixture')
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(list(outside.iterdir()), [])

    def test_hardlink_rejected_and_outside_file_unchanged(self):
        outside = self.base / 'outside.toml'
        outside.write_bytes(b'model="keep"\n')
        self.home.mkdir()
        os.link(outside, self.home / 'config.toml')
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(outside.read_bytes(), b'model="keep"\n')

    def test_partial_failure_restores_existing_bytes_and_removes_new_files(self):
        original = b'# preserve on failed apply\nmodel="keep"\n'
        self.write('config.toml', original)
        self.write('AGENTS.md', b'User guidance\n')
        before = self.files()
        real_replace = REG.replace_file
        calls = 0

        def failing_replace(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 17:  # 15 profiles + config written, then AGENTS fails.
                raise OSError('synthetic injected failure with no secret output')
            return real_replace(*args, **kwargs)

        with patch.object(REG, 'replace_file', side_effect=failing_replace):
            code, result = self.cli('apply')
        self.assertEqual(code, 2)
        self.assertIn('rolled back', result['reason'])
        after = {p: data for p, data in self.files().items() if not p.startswith('.office-agent-backups')}
        self.assertEqual(after, before)
        self.assertFalse((self.home / '.office-agents.lock').exists())

    def test_changed_snapshot_blocks_before_backup(self):
        self.write('config.toml', b'model="before"\n')
        home, snapshots, changes = REG.plan(self.bundle, self.home)
        self.write('config.toml', b'model="after"\n')
        with self.assertRaises(REG.Blocked):
            REG.apply(home, snapshots, changes)
        self.assertFalse((home / '.office-agent-backups').exists())

    def test_existing_lock_is_preserved(self):
        self.write('.office-agents.lock', b'other execution')
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)

    def change_contract(self, responsibility=False):
        path = self.bundle / 'agents/sdd/AGENT.md'
        content = path.read_text(encoding='utf-8')
        if responsibility:
            content = content.replace('Own sdd.', 'Own updated sdd responsibilities.')
        path.write_text(content + 'New canonical output.\n', encoding='utf-8')

    def test_managed_upgrade_refreshes_profile_state_and_description_with_backup(self):
        prefix = b'\xef\xbb\xbf# retain exactly\r\nmodel="fixture"\r\n'
        self.write('config.toml', prefix)
        self.assertEqual(self.cli('apply')[0], 0)
        before = self.files()
        previous_config = (self.home / 'config.toml').read_bytes()
        self.change_contract(responsibility=True)
        self.assertEqual(self.cli('plan')[1]['status'], 'CHANGES_REQUIRED')
        self.assertEqual(self.cli('check')[0], 1)
        self.assertEqual(self.files(), before)
        code, result = self.cli('apply')
        self.assertEqual(code, 0)
        self.assertEqual(set(result['changed_paths']), {
            'agents/office_sdd.toml', 'config.toml', REG.PROFILE_STATE})
        updated = (self.home / 'config.toml').read_bytes()
        self.assertEqual(updated, previous_config.replace(
            b'description = "Own sdd."', b'description = "Own updated sdd responsibilities."'))
        profile = (self.home / 'agents/office_sdd.toml').read_bytes()
        self.assertIn('New canonical output.', tomllib.loads(profile.decode())['developer_instructions'])
        state = json.loads((self.home / REG.PROFILE_STATE).read_text())
        self.assertEqual(state['profiles']['office_sdd']['sha256'], REG.digest(profile))
        backup = self.home / result['backup']
        manifest = json.loads((backup / 'manifest.json').read_text())
        for item in manifest:
            self.assertEqual((backup / item['backup']).read_bytes(), before[str(Path(item['path']))])
        self.assertEqual(self.cli('check')[0], 0)
        self.assertEqual(self.cli('apply')[1]['status'], 'CONFIGURED')

    def test_output_only_contract_update_needs_no_config_rewrite(self):
        self.assertEqual(self.cli('apply')[0], 0)
        config = (self.home / 'config.toml').read_bytes()
        self.change_contract()
        code, result = self.cli('apply')
        self.assertEqual(code, 0)
        self.assertEqual(set(result['changed_paths']), {'agents/office_sdd.toml', REG.PROFILE_STATE})
        self.assertEqual((self.home / 'config.toml').read_bytes(), config)

    def test_custom_profile_and_self_rehashed_envelope_cannot_claim_provenance(self):
        self.assertEqual(self.cli('apply')[0], 0)
        path = self.home / 'agents/office_sdd.toml'
        original = path.read_bytes()
        payload = REG.profile_payload(original).replace(b'Own sdd.', b'Customized sdd.')
        variants = [original.replace(b'sha256=', b'unsupported='),
                    original.replace(b'Own sdd.', b'Customized sdd.'),
                    REG.PROFILE_BEGIN + REG.digest(payload).encode() + b'\n' + payload]
        for data in variants:
            with self.subTest(data=data[:40]):
                path.write_bytes(data)
                before = self.files()
                self.assertEqual(self.cli('apply')[0], 2)
                self.assertEqual(self.files(), before)

    def test_wrong_identity_blocked_even_when_profile_and_state_hashes_match(self):
        self.assertEqual(self.cli('apply')[0], 0)
        path = self.home / 'agents/office_sdd.toml'
        payload = REG.profile_payload(path.read_bytes()).replace(
            b'name = "office_sdd"', b'name = "office_backend"')
        data = REG.PROFILE_BEGIN + REG.digest(payload).encode() + b'\n' + payload
        path.write_bytes(data)
        state_path = self.home / REG.PROFILE_STATE
        state = json.loads(state_path.read_text())
        state['profiles']['office_sdd']['sha256'] = REG.digest(data)
        state_path.write_text(json.dumps(state))
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)

    def test_legacy_exact_generation_can_migrate_but_divergence_blocks(self):
        self.assertEqual(self.cli('apply')[0], 0)
        (self.home / REG.PROFILE_STATE).unlink()
        profile = self.home / 'agents/office_sdd.toml'
        profile.write_bytes(REG.profile_payload(profile.read_bytes()))
        self.assertEqual(self.cli('apply')[0], 0)
        self.assertTrue((self.home / REG.PROFILE_STATE).exists())
        (self.home / REG.PROFILE_STATE).unlink()
        self.change_contract()
        before = self.files()
        code, result = self.cli('apply')
        self.assertEqual(code, 2)
        self.assertIn('back up and reconcile manually', result['reason'])
        self.assertEqual(self.files(), before)

    def test_invalid_state_and_custom_registration_preserved(self):
        self.assertEqual(self.cli('apply')[0], 0)
        state = self.home / REG.PROFILE_STATE
        original = state.read_bytes()
        for invalid in (b'not-json', b'[]', b'{"schema_version":1}', b'{"secret":"DO_NOT_DISCLOSE"}'):
            state.write_bytes(invalid)
            before = self.files()
            code, result = self.cli('apply')
            self.assertEqual(code, 2)
            self.assertNotIn('DO_NOT_DISCLOSE', json.dumps(result))
            self.assertEqual(self.files(), before)
        state.write_bytes(original)
        config = self.home / 'config.toml'
        config.write_bytes(config.read_bytes().replace(b'description = "Own sdd."', b'description = "custom"'))
        self.change_contract(responsibility=True)
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)

    def test_upgrade_partial_failure_restores_profile_config_and_state(self):
        self.assertEqual(self.cli('apply')[0], 0)
        self.change_contract(responsibility=True)
        before = self.files()
        real_replace = REG.replace_file
        calls = 0

        def failing_replace(*args, **kwargs):
            nonlocal calls
            calls += 1
            if calls == 3:  # profile and config changed; fail writing provenance state.
                raise OSError('synthetic state replacement failure')
            return real_replace(*args, **kwargs)

        with patch.object(REG, 'replace_file', side_effect=failing_replace):
            self.assertEqual(self.cli('apply')[0], 2)
        after = self.files()
        for name, data in before.items():
            self.assertEqual(after[name], data)
        self.assertEqual(self.cli('check')[0], 1)

    def test_managed_state_hardlink_blocks_without_external_mutation(self):
        self.assertEqual(self.cli('apply')[0], 0)
        external = self.base / 'external-state.json'
        state = self.home / REG.PROFILE_STATE
        os.link(state, external)
        original = external.read_bytes()
        self.change_contract()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(external.read_bytes(), original)

    def test_custom_table_layout_with_table_text_inside_user_string_is_not_rewritten(self):
        self.assertEqual(self.cli('apply')[0], 0)
        config = self.home / 'config.toml'
        original = config.read_bytes()
        custom = original.replace(b'[agents.office_sdd]', b'[agents."office_sdd"]')
        user = b'custom_text = """\n[agents.office_sdd]\ndescription = "Own sdd."\n"""\n'
        config.write_bytes(user + custom)
        self.change_contract(responsibility=True)
        before = self.files()
        self.assertEqual(self.cli('apply')[0], 2)
        self.assertEqual(self.files(), before)


if __name__ == '__main__':
    unittest.main()
