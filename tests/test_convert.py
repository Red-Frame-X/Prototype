import unittest
from unittest.mock import MagicMock, patch
from urllib.error import URLError

from scripts.convert import AdGuardOptimizer, CANDIDATE_URLS


class SourceFallbackTests(unittest.TestCase):
    def test_candidate_urls_are_unique(self):
        self.assertEqual(len(CANDIDATE_URLS), len(set(CANDIDATE_URLS)))

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
        rule = "example.com##+js(acis)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Incompatible Scriptlet] " + rule,
        )

    def test_incompatible_scriptlet_with_arguments_matches_exactly(self):
        rule = "example.com##+js(json-prune, payload.ad)"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Incompatible Scriptlet] " + rule,
        )

    def test_scriptlet_with_longer_name_is_not_a_prefix_match(self):
        rule = "example.com##+js(json-prune-fetch-response)"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_unescaped_slash_in_regex_character_class_is_escaped(self):
        rule = r"/^https?:\/\/[^/]*pay(?:[/?#]|$)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            r"/^https?:\/\/[^\/]*pay(?:[\/?#]|\$)/",
        )

    def test_unescaped_slash_outside_character_class_remains_delimiter(self):
        rule = r"/^https?:\/\/example\.com\//$document"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_cosmetic_rule_with_url_path_uses_url_modifier(self):
        rule = "www.example.com/specific-path##.advertisement"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "[$url=||www.example.com/specific-path*]##.advertisement",
        )

    def test_cosmetic_rule_with_domain_scope_is_preserved(self):
        rule = "www.example.com##.advertisement"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)


if __name__ == "__main__":
    unittest.main()
