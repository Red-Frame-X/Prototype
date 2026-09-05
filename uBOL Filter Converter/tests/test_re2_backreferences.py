import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "converter_impl.py"
SPEC = importlib.util.spec_from_file_location("ubol_converter_backreference_tests", MODULE_PATH)
converter = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = converter
SPEC.loader.exec_module(converter)


class Re2BackreferenceTests(unittest.TestCase):
    def assert_excluded(self, rule: str) -> None:
        result = converter.convert_line(rule)
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "non-re2-regex")

    def test_numeric_backreference_is_excluded(self):
        self.assert_excluded(r"/(tracker)\1/")

    def test_g_number_backreference_is_excluded(self):
        self.assert_excluded(r"/(tracker)\g1/")

    def test_g_braced_backreference_is_excluded(self):
        self.assert_excluded(r"/(tracker)\g{1}/")

    def test_g_named_backreference_is_excluded(self):
        self.assert_excluded(r"/(?P<id>tracker)\g{id}/")

    def test_k_angle_named_backreference_is_excluded(self):
        self.assert_excluded(r"/(?P<id>tracker)\k<id>/")

    def test_k_quoted_named_backreference_is_excluded(self):
        self.assert_excluded(r"/(?P<id>tracker)\k'id'/")

    def test_escaped_backslash_before_k_is_preserved(self):
        rule = r"/tracker\\k<id>/"
        result = converter.convert_line(rule)
        self.assertEqual(result.output, rule)
        self.assertEqual(result.status, "preserved")

    def test_escaped_backslash_before_g_is_preserved(self):
        rule = r"/tracker\\g{name}/"
        result = converter.convert_line(rule)
        self.assertEqual(result.output, rule)
        self.assertEqual(result.status, "preserved")


if __name__ == "__main__":
    unittest.main()
