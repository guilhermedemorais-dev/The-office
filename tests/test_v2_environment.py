"""V2 platform and REA plans; mocked discovery never claims native validation."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]


def load(name, path):
    spec = importlib.util.spec_from_file_location(name, ROOT / path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


platform_catalog = load("v2platform", "environment/shared/platform_catalog.py")
rea = load("v2rea", "integrations/reverse-engineering/adapter.py")


class PlatformSelectionTests(unittest.TestCase):
    def test_platform_detection(self):
        detect = platform_catalog.detect_platform
        self.assertEqual(detect("Linux", "5.15-microsoft-WSL2", ""), "linux")
        self.assertEqual(detect("Windows", "10", "10.0.19045"), "windows/win10")
        self.assertEqual(detect("Windows", "10", "10.0.22631"), "windows/win11")
        self.assertEqual(detect("Windows", "11", ""), "windows/win11")
        self.assertEqual(detect("Darwin", "", ""), "macos")
        with self.assertRaises(ValueError):
            detect("Windows", "10", "unknown")
        with self.assertRaises(ValueError):
            detect("Plan9", "", "")

    def test_platforms_reference_same_canonical_scripts(self):
        paths = []
        for platform_id in ("linux", "windows/win10", "windows/win11", "macos"):
            catalog = platform_catalog.load_catalog(platform_id)
            paths.append([tool["path"] for tool in catalog["tools"]])
            self.assertTrue(all((ROOT / p).is_file() for p in paths[-1]))
        self.assertTrue(all(p == paths[0] for p in paths))

    def test_win11_never_inherits_win10_certification(self):
        win10 = platform_catalog.load_catalog("windows/win10")
        win11 = platform_catalog.load_catalog("windows/win11")
        self.assertEqual(win10["tools"][0]["support_state"], "SUPPORTED")
        self.assertEqual(win11["tools"][0]["support_state"], "NOT_VALIDATED")
        self.assertTrue(all(t["native_v2_validation"] == "NOT_VALIDATED" for t in win10["tools"]))
        self.assertEqual(win11["tools"][1]["support_state"], "UNSUPPORTED")

    def test_runtime_presence_never_proves_operational_status(self):
        with patch.object(platform_catalog, "detect_platform", return_value="linux"):
            report = platform_catalog.inspect_tool("environment", "linux", which=lambda _: "/mock/python")
        self.assertTrue(report["runtime_discovered"])
        self.assertTrue(report["eligible_for_verification"])
        for state in ("AVAILABLE", "INSTALLED", "CONFIGURED", "AUTHENTICATED", "VERIFIED"):
            self.assertIsNone(report["states"][state])

    def test_missing_tool_and_foreign_platform(self):
        with patch.object(platform_catalog, "detect_platform", return_value="linux"):
            missing = platform_catalog.inspect_tool("environment", "linux", which=lambda _: None)
            foreign = platform_catalog.inspect_tool("environment", "windows/win10", which=lambda _: self.fail("foreign runtime probed"))
        self.assertFalse(missing["eligible_for_verification"])
        self.assertIsNone(foreign["runtime_discovered"])
        with self.assertRaises(ValueError):
            platform_catalog.inspect_tool("unknown", "linux")

    def test_source_and_overlay_changes_invalidate_fingerprint(self):
        with tempfile.TemporaryDirectory() as folder:
            root = Path(folder)
            (root / "environment/linux").mkdir(parents=True)
            overlay = root / "environment/linux/catalog.json"
            source = root / "catalog.json"
            overlay.write_text(json.dumps({"canonical_catalog": "catalog.json", "inherit_suite_evidence": True}))
            source.write_text(json.dumps({"tools": []}))
            old = platform_catalog.load_catalog("linux", root)["catalog_fingerprint"]
            source.write_text(json.dumps({"tools": [], "revision": 2}))
            changed = platform_catalog.load_catalog("linux", root)["catalog_fingerprint"]
            self.assertNotEqual(old, changed)
            overlay.write_text(json.dumps({"canonical_catalog": "../outside.json", "inherit_suite_evidence": True}))
            with self.assertRaises(ValueError):
                platform_catalog.load_catalog("linux", root)


class ReverseIntegrationTests(unittest.TestCase):
    def test_original_engine_is_pinned_and_distributed(self):
        result = rea.inventory()
        self.assertEqual(result["version"], "4.1.0")
        self.assertEqual(result["license"], "MIT")
        self.assertTrue(result["tarball_present"])
        self.assertEqual(len(result["tarball_sha256"]), 64)
        self.assertEqual(result["provider_validation"], "NOT_VALIDATED")
        self.assertTrue((ROOT / result["gateway"]).is_file())

    def test_all_routes_exist_in_original_catalog(self):
        for kind in rea.ROUTES:
            result = rea.route(kind)
            self.assertFalse(result["execution_performed"])
            self.assertEqual(result["status"], "PLAN_ONLY")
            self.assertEqual(result["mode"], "static_first")
        self.assertEqual(rea.route("apk")["family"], "android")
        self.assertEqual(rea.route("managed")["family"], "managed")

    def test_runtime_is_separate_and_unknown_routes_fail(self):
        self.assertEqual(rea.route("browser", runtime_observation=True)["mode"], "runtime_observation")
        self.assertEqual(rea.route("electron", runtime_observation=True)["family"], "javascript_runtime")
        with self.assertRaises(ValueError):
            rea.route("native", runtime_observation=True)
        with self.assertRaises(ValueError):
            rea.route("unknown")


if __name__ == "__main__":
    unittest.main()
