"""Offline tests for the token-free update checker."""
import importlib.util
import unittest
from pathlib import Path
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("office_update", ROOT / "scripts/office_update.py")
office = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(office)


class UpdateCheckerTests(unittest.TestCase):
    def test_default_branch_from_origin(self):
        with patch.object(office, "git", return_value="origin/main"):
            self.assertEqual(office.default_branch(), "main")

    def test_check_detects_fast_forward(self):
        def fake_git(*args, **kwargs):
            if args[:2] == ("rev-parse", "--show-toplevel"):
                return str(ROOT.resolve())
            if args[:2] == ("remote", "get-url"):
                return "https://github.com/test/repo"
            if args[0] == "symbolic-ref" and args[-1] == "refs/remotes/origin/HEAD":
                return "origin/main"
            if args[0] == "symbolic-ref":
                return "main"
            if args[0] == "rev-parse" and args[1] == "HEAD":
                return "old"
            if args[0] == "rev-parse":
                return "new"
            if args[0] == "status":
                return ""
            if args[0] == "rev-list":
                return "2" if args[-1] == "old..new" else "0"
            return ""
        with patch.object(office, "git", side_effect=fake_git):
            result = office.check(fetch=False)
        self.assertTrue(result["update_available"])
        self.assertEqual(result["behind"], 2)

    def test_apply_refuses_dirty_checkout(self):
        with patch.object(office, "check", return_value={
            "update_available": True, "dirty": True, "local_branch": "main", "branch": "main"}):
            with self.assertRaises(office.UpdateError):
                office.apply()

    def test_apply_refuses_feature_branch(self):
        with patch.object(office, "check", return_value={
            "update_available": True, "dirty": False,
            "local_branch": "feat/work", "branch": "main"}):
            with self.assertRaises(office.UpdateError):
                office.apply()


if __name__ == "__main__":
    unittest.main()
