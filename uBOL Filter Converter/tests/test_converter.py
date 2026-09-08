import importlib.util
import json
import sys
import tempfile
import unittest
from pathlib import Path


MODULE_PATH = Path(__file__).resolve().parents[1] / "converter_impl.py"
if not MODULE_PATH.exists():
    MODULE_PATH = Path(__file__).resolve().parents[2] / "scripts" / "convert_adguard_to_ubol.py"
SPEC = importlib.util.spec_from_file_location("ubol_converter", MODULE_PATH)
converter = importlib.util.module_from_spec(SPEC)
assert SPEC and SPEC.loader
sys.modules[SPEC.name] = converter
SPEC.loader.exec_module(converter)


class LineConversionTests(unittest.TestCase):
    def test_non_basic_modifier_is_excluded_and_reported(self):
        rule = "[$app=com.example.app]##.ad"
        self.assertEqual(converter.convert_line(rule).reason, "non-basic-modifier")
        output, excluded = converter.convert(["! App-only hiding", rule])
        self.assertEqual(output, [])
        self.assertEqual(excluded[0]["line"], 2)

    def test_list_header_is_preserved(self):
        self.assertEqual(converter.convert_line("[Adblock Plus 2.0]").output, "[Adblock Plus 2.0]")

    def test_plain_cosmetic_rule_is_preserved(self):
        self.assertEqual(converter.convert_line("example.com##.ad").output, "example.com##.ad")

    def test_native_has_rule_is_preserved(self):
        rule = "example.com##section:has(> .promo)"
        self.assertEqual(converter.convert_line(rule).output, rule)

    def test_adguard_extended_separator_becomes_ubo_separator(self):
        result = converter.convert_line("example.com#?#div:has(.promo)")
        self.assertEqual(result.output, "example.com##div:has(.promo)")
        self.assertEqual(result.status, "converted")

    def test_contains_rule_is_converted_to_has_text(self):
        result = converter.convert_line("example.com#?#div:contains(Promo)")
        self.assertEqual(result.output, "example.com##div:has-text(Promo)")
        self.assertEqual(result.status, "converted")

    def test_nested_contains_rule_is_converted_to_has_text(self):
        result = converter.convert_line(
            "example.com#?#aside:has(h3:contains(Promo)):has(button.close)"
        )
        self.assertEqual(
            result.output,
            "example.com##aside:has(h3:has-text(Promo)):has(button.close)",
        )

    def test_upward_rule_is_preserved_for_ubol(self):
        result = converter.convert_line(
            "example.com#?#span:contains(Promo):upward(div.card)"
        )
        self.assertEqual(
            result.output,
            "example.com##span:has-text(Promo):upward(div.card)",
        )

    def test_style_rule_is_preserved_for_ubol(self):
        rule = "example.com##.title:style(font-size: 1.2rem !important;)"
        result = converter.convert_line(rule)
        self.assertEqual(result.output, rule)
        self.assertEqual(result.status, "preserved")

    def test_adguard_nth_ancestor_becomes_upward(self):
        result = converter.convert_line(
            "example.com#?#span:contains(Promo):nth-ancestor(2)"
        )
        self.assertEqual(
            result.output,
            "example.com##span:has-text(Promo):upward(2)",
        )

    def test_adguard_matches_property_becomes_matches_prop(self):
        result = converter.convert_line(
            "example.com#?#img:matches-property(naturalWidth=160)"
        )
        self.assertEqual(
            result.output,
            "example.com##img:matches-prop(naturalWidth=160)",
        )

    def test_ubo_procedural_operators_are_preserved(self):
        rules = (
            'example.com##button:matches-attr(class="/[a-z]{7}/")',
            "example.com##div:matches-css(position: absolute)",
            "example.com##div:matches-css-before(content: Promo)",
            "example.com##div:matches-css-after(content: Promo)",
            'example.com##:xpath(//div[@data-ad="true"])',
        )
        for rule in rules:
            with self.subTest(rule=rule):
                self.assertEqual(converter.convert_line(rule).output, rule)

    def test_remove_action_is_preserved(self):
        rule = "example.com##.ad:remove()"
        result = converter.convert_line(rule)
        self.assertEqual(result.output, rule)
        self.assertEqual(result.status, "preserved")

    def test_adguard_extended_remove_action_is_converted(self):
        result = converter.convert_line("example.com#?#.ad:remove()")
        self.assertEqual(result.output, "example.com##.ad:remove()")
        self.assertEqual(result.status, "converted")

    def test_html_filter_is_excluded(self):
        self.assertEqual(converter.convert_line('example.com$$div[id="ad"]').reason, "html-filtering")

    def test_scriptlet_is_excluded(self):
        self.assertEqual(converter.convert_line("example.com#%#//scriptlet('set-cookie')").reason, "scriptlet")

    def test_app_modifier_is_excluded(self):
        result = converter.convert_line("@@||example.com^$app=com.example.app")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "modifier:app")

    def test_xhr_alias_is_converted(self):
        result = converter.convert_line("||example.com^$xhr,third-party")
        self.assertEqual(result.output, "||example.com^$xmlhttprequest,third-party")

    def test_unsupported_modifier_is_excluded(self):
        result = converter.convert_line("||example.com^$script,replace=/a/b/")
        self.assertIsNone(result.output)
        self.assertEqual(result.reason, "modifier:replace")

    def test_non_re2_regex_is_excluded(self):
        self.assertEqual(converter.convert_line(r"/(?<=ad)tracker/").reason, "non-re2-regex")

    def test_report_keeps_source_line_number(self):
        output, excluded = converter.convert(["! comment", "example.com##.ad", "@@||api^$app=x"])
        self.assertEqual(output, ["! comment", "example.com##.ad"])
        self.assertEqual(excluded[0]["line"], 3)

    def test_excluded_rule_removes_domain_and_description_comments(self):
        output, excluded = converter.convert([
            "! ads-x.com",
            "! App compatibility exception",
            "@@||static.ads-x.com^$app=example.app",
        ])
        self.assertEqual(output, [])
        self.assertEqual(excluded[0]["line"], 3)

    def test_mixed_domain_keeps_only_comments_for_surviving_rules(self):
        output, _ = converter.convert([
            "! example.com",
            "! Removed app-only rule",
            "@@||api.example.com^$app=example.app",
            "! Visible ad container",
            "example.com##.ad",
        ])
        self.assertEqual(output, ["! example.com", "! Visible ad container", "example.com##.ad"])

    def test_standalone_section_comment_is_preserved(self):
        output, _ = converter.convert(["! Global"])
        self.assertEqual(output, ["! Global"])

    def test_multi_domain_heading_keeps_converted_and_standard_rules(self):
        output, _ = converter.convert([
            "! one.example,two.example",
            "! Converted procedural rule",
            "one.example,two.example#?#div:contains(Ad)",
            "! Surviving standard rule",
            "one.example,two.example##.ad",
        ])
        self.assertEqual(output, [
            "! one.example,two.example",
            "! Converted procedural rule",
            "one.example,two.example##div:has-text(Ad)",
            "! Surviving standard rule",
            "one.example,two.example##.ad",
        ])


class MainOutputTests(unittest.TestCase):
    def test_filter_name_and_output_basename_are_canonical(self):
        self.assertEqual(converter.FILTER_TITLE, "uBOL Filter - Red Frame X")
        self.assertEqual(converter.FILTER_BASENAME, "uBOL Filter - Red Frame X")

    def test_report_is_deterministic_and_contains_no_runtime_timestamp(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.txt"
            output = root / "output.txt"
            report = root / "report.json"
            source.write_text(
                "! Version: 202608221705\n"
                "! example.com\n! Ad container\nexample.com##.ad\n",
                encoding="utf-8",
            )
            args = [
                "--input", str(source),
                "--output", str(output),
                "--report", str(report),
            ]

            self.assertEqual(converter.main(args), 0)
            first_output = output.read_bytes()
            first_report = report.read_bytes()
            self.assertEqual(converter.main(args), 0)

            self.assertEqual(output.read_bytes(), first_output)
            self.assertEqual(report.read_bytes(), first_report)
            self.assertNotIn("generated", json.loads(first_report))
            expected_header = (
                "! Title: uBOL Filter - Red Frame X\n"
                "! Description: Customize uBOL filters for personal use.\n"
                "! Version: 202608221705\n"
                "! Syntax: uBOL\n"
                "! Expires: 1 day\n"
                "! Homepage: https://github.com/Red-Frame-X/Prototype\n"
                "! License: CC0-1.0\n"
                "! Note: Combination of Japan’s community-driven rules and my own rules.\n"
            ).encode()
            self.assertTrue(first_output.startswith(expected_header))

    def test_missing_source_version_is_rejected(self):
        with tempfile.TemporaryDirectory() as directory:
            root = Path(directory)
            source = root / "source.txt"
            source.write_text("example.com##.ad\n", encoding="utf-8")
            self.assertEqual(converter.main(["--input", str(source)]), 1)


if __name__ == "__main__":
    unittest.main()
