import unittest

from scripts.convert import AdGuardOptimizer, CANDIDATE_URLS


class SourceFallbackTests(unittest.TestCase):
    def test_candidate_urls_are_unique(self):
        self.assertEqual(len(CANDIDATE_URLS), len(set(CANDIDATE_URLS)))


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
