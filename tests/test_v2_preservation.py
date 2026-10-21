import importlib.util
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
spec=importlib.util.spec_from_file_location('preserve',ROOT/'scripts/verify_preservation.py')
preserve=importlib.util.module_from_spec(spec);spec.loader.exec_module(preserve)
class FrozenV1(unittest.TestCase):
    def test_all_canonical_sources_and_archives_match_inventory(self):
        result=preserve.verify(ROOT)
        self.assertGreater(result['files'],300)
        self.assertEqual(result['failures'],[])
