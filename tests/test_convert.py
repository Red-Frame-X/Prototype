import json
import os
import tempfile
import unittest
from unittest.mock import MagicMock, patch
from urllib.error import URLError

from scripts.convert import (
    AdGuardOptimizer,
    CANDIDATE_URLS,
    CAPABILITY_FILE,
    CAPABILITY_TARGET,
    FILTER_NAME,
    OUTPUT_FILE,
)


class GeneratedFilterNamingTests(unittest.TestCase):
    def test_filter_name_is_canonical(self):
        self.assertEqual(FILTER_NAME, "uB-filter-by-kdroidwin (AdGuard Optimized)")

    def test_output_filename_matches_filter_name(self):
        self.assertTrue(OUTPUT_FILE.endswith(f"dist/{FILTER_NAME}.txt"))


class CapabilityProfileTests(unittest.TestCase):
    def test_repository_capability_profile_drives_optimizer_settings(self):
        with open(CAPABILITY_FILE, "r", encoding="utf-8") as f:
            profile = json.load(f)

        settings = profile["targets"][CAPABILITY_TARGET]["converter_settings"]
        optimizer = AdGuardOptimizer()

        self.assertEqual(optimizer.adg_supported_ext_css, settings["adguard_extended_css"])
        self.assertEqual(
            optimizer.ubo_unsupported_ext_css,
            settings["unsupported_ubo_extended_css"],
        )
        self.assertEqual(
            optimizer.compatible_scriptlets,
            settings["compatible_scriptlets"],
        )
        self.assertEqual(
            optimizer.incompatible_scriptlets,
            settings["incompatible_scriptlets"],
        )
        self.assertEqual(
            optimizer.modifier_replacements,
            settings["modifier_replacements"],
        )

    def test_adguard_compatible_scriptlets_are_not_marked_incompatible(self):
        with open(CAPABILITY_FILE, "r", encoding="utf-8") as f:
            profile = json.load(f)

        incompatible = profile["targets"][CAPABILITY_TARGET]["converter_settings"][
            "incompatible_scriptlets"
        ]
        for scriptlet in ("acis", "spoof-css", "m3u-prune", "json-prune"):
            with self.subTest(scriptlet=scriptlet):
                self.assertNotIn(scriptlet, incompatible)

    def test_trusted_scriptlets_are_not_assumed_cross_blocker_compatible(self):
        with open(CAPABILITY_FILE, "r", encoding="utf-8") as f:
            profile = json.load(f)

        target = profile["targets"][CAPABILITY_TARGET]
        policy = target["scriptlet_policy"]
        incompatible = target["converter_settings"]["incompatible_scriptlets"]

        self.assertEqual(policy["source_syntax"], "uBlock Origin")
        self.assertEqual(policy["target_syntax"], "AdGuard")
        self.assertIn("not assumed compatible", policy["trusted_scriptlets"])
        for scriptlet in (
            "trusted-replace-argument",
            "trusted-set-cookie",
            "trusted-click-element",
        ):
            with self.subTest(scriptlet=scriptlet):
                self.assertIn(scriptlet, incompatible)

    def test_custom_capability_profile_changes_converter_behavior(self):
        profile = {
            "targets": {
                CAPABILITY_TARGET: {
                    "converter_settings": {
                        "adguard_extended_css": [":custom-ext("],
                        "unsupported_ubo_extended_css": [":unsupported-ext("],
                        "compatible_scriptlets": ["compatible-scriptlet"],
                        "incompatible_scriptlets": ["custom-scriptlet"],
                        "modifier_replacements": {"custommod": "translatedmod"},
                    }
                }
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            capability_path = os.path.join(temp_dir, "capabilities.json")
            with open(capability_path, "w", encoding="utf-8") as f:
                json.dump(profile, f)

            optimizer = AdGuardOptimizer(capability_path)

        self.assertEqual(
            optimizer.optimize_line("example.com##div:custom-ext(value)"),
            "example.com#?#div:custom-ext(value)",
        )
        self.assertEqual(
            optimizer.optimize_line("example.com##div:unsupported-ext(value)"),
            "! [Unsupported Extended CSS] example.com##div:unsupported-ext(value)",
        )
        self.assertEqual(
            optimizer.optimize_line("example.com##+js(custom-scriptlet)"),
            "! [Incompatible Scriptlet] example.com##+js(custom-scriptlet)",
        )
        self.assertEqual(
            optimizer.optimize_line("||example.com^$custommod"),
            "||example.com^$translatedmod",
        )

    def test_invalid_capability_profile_fails_fast(self):
        profile = {
            "targets": {
                CAPABILITY_TARGET: {
                    "converter_settings": {
                        "adguard_extended_css": [],
                        "unsupported_ubo_extended_css": [":unsupported("],
                        "incompatible_scriptlets": ["custom-scriptlet"],
                        "modifier_replacements": {"custommod": "translatedmod"},
                    }
                }
            }
        }

        with tempfile.TemporaryDirectory() as temp_dir:
            capability_path = os.path.join(temp_dir, "capabilities.json")
            with open(capability_path, "w", encoding="utf-8") as f:
                json.dump(profile, f)

            with self.assertRaises(ValueError):
                AdGuardOptimizer(capability_path)


class SourceFallbackTests(unittest.TestCase):
    def test_candidate_urls_are_unique(self):
        self.assertEqual(len(CANDIDATE_URLS), len(set(CANDIDATE_URLS)))

    def test_candidate_urls_target_current_source_repository(self):
        for url in CANDIDATE_URLS:
            self.assertIn("/Kdroidwin/uB-filter-by-kdroidwin", url)
            self.assertNotIn("uBlacklist-filter-by-kdroidwin", url)

    @patch("scripts.convert.urllib.request.urlopen")
    def test_fetch_source_falls_back_to_second_candidate(self, mock_urlopen):
        successful_response = MagicMock()
        successful_response.__enter__.return_value.read.return_value = b"rule-one\nrule-two\n"
        mock_urlopen.side_effect = [URLError("primary unavailable"), successful_response]

        source = AdGuardOptimizer().fetch_source()

        self.assertEqual(source, ["rule-one", "rule-two"])
        self.assertEqual(mock_urlopen.call_count, 2)
        requested_urls = [call.args[0].full_url for call in mock_urlopen.call_args_list]
        self.assertEqual(requested_urls, CANDIDATE_URLS)


class ModifierConversionTests(unittest.TestCase):
    def setUp(self):
        self.optimizer = AdGuardOptimizer()

    def test_redirect_rule_with_value_is_commented_out(self):
        rule = "||example.com/ad.js$script,redirect-rule=noopjs"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Modifier: redirect-rule] " + rule,
        )

    def test_redirect_rule_exception_is_commented_out(self):
        rule = "@@||example.com/ad.js$redirect-rule=noopjs"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Modifier: redirect-rule] " + rule,
        )

    def test_bare_redirect_rule_is_commented_out(self):
        rule = "||example.com/ad.js$script,redirect-rule"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Modifier: redirect-rule] " + rule,
        )

    def test_other_modifier_replacements_still_work(self):
        rule = "||example.com^$3p,queryprune=utm_source"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "||example.com^$third-party,removeparam=utm_source",
        )

    def test_to_modifier_is_preserved_for_chrome_mv3(self):
        rule = "||example.com^$document,to=target.example|~excluded.example"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_negated_to_value_is_preserved_for_chrome_mv3(self):
        rule = "||example.com^$document,to=~excluded.example"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_incompatible_scriptlet_name_matches_exactly(self):
        rule = "example.com##+js(trusted-replace-argument)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Incompatible Scriptlet] " + rule,
        )

    def test_incompatible_scriptlet_with_arguments_matches_exactly(self):
        rule = "example.com##+js(trusted-set-cookie, consent, true)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Incompatible Scriptlet] " + rule,
        )

    def test_adguard_compatible_scriptlets_are_preserved(self):
        rules = (
            "example.com##+js(acis)",
            "example.com##+js(spoof-css, display, block)",
            "example.com##+js(m3u-prune, /ad/)",
            "example.com##+js(json-prune, payload.ad)",
        )
        for rule in rules:
            with self.subTest(rule=rule):
                self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_unverified_scriptlet_is_commented_out(self):
        rule = "example.com##+js(json-prune-fetch-response)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unverified Scriptlet] " + rule,
        )

    def test_unescaped_slash_in_regex_character_class_is_escaped(self):
        rule = r"/^https?:\/\/[^/]*pay(?:[/?#]|$)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            r"/^https?:\/\/[^\/]*pay(?:[\/?#]|$)/",
        )

    def test_end_anchor_in_regex_is_preserved(self):
        rule = r"/tracker$/"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_positive_lookahead_regex_is_commented_out(self):
        rule = r"/pay(?=ment)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_negative_lookahead_regex_is_commented_out(self):
        rule = r"/tracker(?!safe)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_positive_lookbehind_regex_is_commented_out(self):
        rule = r"/(?<=pay)ment/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_negative_lookbehind_regex_is_commented_out(self):
        rule = r"/(?<!safe)tracker/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_numeric_backreference_regex_is_commented_out(self):
        rule = r"/(pay)\1/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_named_backreference_regex_is_commented_out(self):
        rule = r"/(?P<name>pay)\g<name>/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_escaped_backslash_before_digit_is_not_treated_as_backreference(self):
        rule = r"/pay\\1/"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_supported_cosmetic_scope_with_path_is_converted_to_url_modifier(self):
        rule = "example.com/path##.ad"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "[$url=||example.com/path*]##.ad",
        )

    def test_mixed_cosmetic_url_scope_is_commented_out(self):
        rule = "example.com/path,other.example##.ad"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported Mixed Cosmetic URL Scope] " + rule,
        )

    def test_html_filter_is_commented_out(self):
        rule = "example.com##^script:has-text(ad)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported HTML Filter] " + rule,
        )

    def test_cname_rule_is_commented_out(self):
        rule = "||example.com^$cname"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Modifier: cname] " + rule,
        )

    def test_cname_exception_is_commented_out(self):
        rule = "@@||example.com^$cname=tracker.example"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Modifier: cname] " + rule,
        )


if __name__ == "__main__":
    unittest.main()
