import importlib.util
import json
import os
from pathlib import Path
import sys
import tempfile
import unittest

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / 'scripts'))
spec = importlib.util.spec_from_file_location('office_opencode', ROOT / 'scripts/register_opencode_agents.py')
registration = importlib.util.module_from_spec(spec)
spec.loader.exec_module(registration)


class OpenCodeRegistration(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.root = Path(self.temp.name)
        self.bundle = self.root / 'bundle'
        self.project = self.root / 'client'
        self.project.mkdir()
        for name in ('AGENTS.md', 'docs/operations/v2-execution-policy.md', 'scripts/office.py'):
            path = self.bundle / name
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text('fixture\n')
        for sector in registration.SECTORS:
            path = self.bundle / 'agents' / sector / 'AGENT.md'
            path.parent.mkdir(parents=True)
            path.write_text(f'# {sector}\n\n## Responsibility\nOwn {sector}.\n\n## Other\nfixture\n')
        self.skill = self.bundle / 'skills/global-core/SKILL.md'
        self.skill.parent.mkdir(parents=True)
        self.skill.write_text('---\nname: global-core\ndescription: "Core fixture"\n---\n\nRead fixture.\n')
        registry = self.bundle / 'library/indexes/skill-routes.json'
        registry.parent.mkdir(parents=True)
        registry.write_text(json.dumps({'skills': [{'id': 'global-core', 'path': 'skills/global-core/SKILL.md'}]}))

    def tearDown(self):
        self.temp.cleanup()

    def plan(self):
        return registration.plan(self.bundle, self.project)

    def apply(self):
        home, snapshots, changes = self.plan()
        return registration.apply(home, snapshots, changes)

    def test_plan_is_read_only_and_profiles_are_native(self):
        home, _, changes = self.plan()
        self.assertFalse(home.exists())
        primary = changes[home / 'agents/office_orchestrator.md'].decode()
        specialist = changes[home / 'agents/office_sdd.md'].decode()
        self.assertIn('mode: primary', primary)
        self.assertIn('mode: subagent', specialist)
        self.assertIn('"edit": "deny"', primary)
        self.assertNotIn('model:', specialist)

    def test_apply_is_idempotent_and_does_not_touch_host_config(self):
        config = self.project / 'opencode.json'
        original = b'{"model":"custom/model","mcp":{"existing":{"type":"remote","url":"https://example.test"}}}'
        config.write_bytes(original)
        first = self.apply()
        self.assertIsNotNone(first)
        self.assertEqual(config.read_bytes(), original)
        self.assertEqual(self.plan()[2], {})
        self.assertIsNone(self.apply())
        self.assertEqual(len(list((self.project / '.opencode/.office-agent-backups').iterdir())), 1)

    def test_skill_discovery_points_to_canonical_source_and_hash(self):
        home, _, changes = self.plan()
        wrapper = changes[home / 'skills/global-core/SKILL.md'].decode()
        self.assertIn('name: global-core', wrapper)
        self.assertIn(self.skill.as_posix(), wrapper)
        self.assertIn(registration.digest(self.skill.read_bytes()), wrapper)
        self.assertIn('complete canonical SKILL.md', wrapper)

    def test_update_intact_adapters_after_source_changes(self):
        self.apply()
        self.skill.write_text(self.skill.read_text() + 'New source rule.\n')
        self.assertTrue(self.plan()[2])
        self.apply()
        self.assertEqual(self.plan()[2], {})

    def test_user_edits_block_update(self):
        self.apply()
        path = self.project / '.opencode/agents/office_sdd.md'
        path.write_text(path.read_text() + 'User customization.\n')
        with self.assertRaisesRegex(registration.Blocked, 'managed adapter changed'):
            self.plan()
        self.assertIn('User customization', path.read_text())

    def test_unmanaged_collision_blocks_without_writes(self):
        path = self.project / '.opencode/agents/office_sdd.md'
        path.parent.mkdir(parents=True)
        path.write_text('private customized agent')
        with self.assertRaisesRegex(registration.Blocked, 'unmanaged adapter collision'):
            self.plan()
        self.assertEqual(path.read_text(), 'private customized agent')
        self.assertFalse((path.parent / 'office_qa.md').exists())

    def test_host_agent_override_blocks(self):
        (self.project / 'opencode.json').write_text('{"agent":{"office_sdd":{"model":"other/model"}}}')
        with self.assertRaisesRegex(registration.Blocked, 'override'):
            self.plan()

    def test_jsonc_requires_review_without_rewriting(self):
        path = self.project / 'opencode.jsonc'
        path.write_text('// custom settings\n{}')
        with self.assertRaisesRegex(registration.Blocked, 'jsonc'):
            self.plan()
        self.assertFalse((self.project / '.opencode').exists())

    def test_config_change_after_plan_blocks_apply(self):
        home, snapshots, changes = self.plan()
        (self.project / 'opencode.json').write_text('{"model":"new/model"}')
        with self.assertRaisesRegex(registration.Blocked, 'concurrent changes'):
            registration.apply(home, snapshots, changes)
        self.assertFalse(home.exists())

    def test_canonical_source_change_after_plan_blocks_apply(self):
        home, snapshots, changes = self.plan()
        self.skill.write_text(self.skill.read_text() + 'Concurrent source change.\n')
        with self.assertRaisesRegex(registration.Blocked, 'concurrent changes'):
            registration.apply(home, snapshots, changes)
        self.assertFalse(home.exists())

    @unittest.skipUnless(hasattr(os, 'symlink'), 'requires symlink support')
    def test_symlink_target_is_rejected(self):
        outside = self.root / 'outside'
        outside.mkdir()
        (self.project / '.opencode').symlink_to(outside, target_is_directory=True)
        with self.assertRaises(registration.Blocked):
            self.plan()
        self.assertEqual(list(outside.iterdir()), [])

    def test_corrupt_state_blocks(self):
        self.apply()
        (self.project / '.opencode/office-registration.json').write_text('{"schema_version":1}')
        with self.assertRaisesRegex(registration.Blocked, 'registration state'):
            self.plan()

    def test_noncanonical_route_is_rejected(self):
        path = self.bundle / 'library/indexes/skill-routes.json'
        path.write_text('{"skills":[{"id":"global-core","path":"../../secret"}]}')
        with self.assertRaisesRegex(registration.Blocked, 'noncanonical'):
            self.plan()

    def test_install_and_update_prompts_remain_separate(self):
        install = (ROOT / 'docs/operations/installation-prompt.md').read_text()
        update = (ROOT / 'docs/operations/update-prompt.md').read_text()
        self.assertIn('instalação inicial', install.lower())
        self.assertIn('prompt de atualização', install.lower())
        self.assertIn('já estiver instalado ou registrado', update.lower())
        self.assertIn('prompt de instalação inicial', update.lower())
        self.assertNotEqual(install, update)


if __name__ == '__main__':
    unittest.main()
