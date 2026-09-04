import importlib.util
import sys
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "converter_impl.py"
SPEC = importlib.util.spec_from_file_location("ubol_converter_regex_tests", MODULE_PATH)
converter = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = converter
SPEC.loader.exec_module(converter)


class RegexModifierParsingTests(unittest.TestCase):
    def test_non_re2_regex_with_end_anchor_is_excluded(self):
        result = converter.convert_line(r"/(?<=ad)tracker$/")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "non-re2-regex")

    def test_non_re2_backreference_with_end_anchor_is_excluded(self):
        result = converter.convert_line(r"/(tracker)\1$/")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "non-re2-regex")

    def test_positive_lookahead_regex_is_excluded(self):
        result = converter.convert_line(r"/pay(?=ment)/")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "non-re2-regex")

    def test_negative_lookahead_regex_is_excluded(self):
        result = converter.convert_line(r"/tracker(?!safe)/")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "non-re2-regex")

    def test_re2_regex_end_anchor_is_not_treated_as_modifier_separator(self):
        rule = r"/tracker$/"
        result = converter.convert_line(rule)
        self.assertEqual(result.output, rule)
        self.assertEqual(result.status, "preserved")

    def test_regex_modifier_after_closing_delimiter_is_converted(self):
        result = converter.convert_line(r"/tracker$/$xhr,third-party")
        self.assertEqual(result.output, r"/tracker$/$xmlhttprequest,third-party")
        self.assertEqual(result.status, "converted")

    def test_exception_regex_modifier_after_closing_delimiter_is_converted(self):
        result = converter.convert_line(r"@@/tracker$/$xhr")
        self.assertEqual(result.output, r"@@/tracker$/$xmlhttprequest")
        self.assertEqual(result.status, "converted")

    def test_escaped_slash_does_not_close_regex_early(self):
        result = converter.convert_line(r"/path\/tracker$/$xhr")
        self.assertEqual(result.output, r"/path\/tracker$/$xmlhttprequest")
        self.assertEqual(result.status, "converted")


if __name__ == "__main__":
    unittest.main()
