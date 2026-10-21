import importlib.util
from pathlib import Path
import tempfile
import unittest

ROOT=Path(__file__).resolve().parents[1]
def load(name,relative):
    spec=importlib.util.spec_from_file_location(name,ROOT/relative)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module);return module

office=load('office_privacy','scripts/office.py')
library=load('library_privacy','scripts/build_library.py')
class LocalPrivacy(unittest.TestCase):
    def symlink(self,link,target):
        try: link.symlink_to(target)
        except OSError as error: self.skipTest('Symlink unavailable: '+str(error))
    def test_in_root_private_symlink_alias_is_blocked(self):
        with tempfile.TemporaryDirectory() as temp:
            root=Path(temp);(root/'.git').mkdir();(root/'.git/config').write_text('fixture')
            self.symlink(root/'alias.md',root/'.git/config')
            with self.assertRaises(ValueError):office.safe_path(root,'alias.md')
    def test_index_does_not_read_symlink_outside_checkout(self):
        with tempfile.TemporaryDirectory() as temp:
            parent=Path(temp);root=parent/'repo';refs=root/'plugins/demo/skills/demo/references';refs.mkdir(parents=True)
            outside=parent/'private.md';outside.write_text('# PRIVATE FIXTURE')
            self.symlink(refs/'alias.md',outside)
            (refs/'public.md').write_text('# Public fixture')
            result=library.build(root)
            self.assertEqual(len(result['resources']),1)
            self.assertEqual(result['resources'][0]['title'],'Public fixture')
