import unittest

from scripts.convert import AdGuardOptimizer


class ModifierConversionTests(unittest.TestCase):
    def setUp(self):
        self.optimizer = AdGuardOptimizer()

    def test_redirect_rule_with_value_is_converted(self):
        rule = "||example.com/ad.js$script,redirect-rule=noopjs"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "||example.com/ad.js$script,redirect=noopjs",
        )

    def test_redirect_rule_exception_is_converted(self):
        rule = "@@||example.com/ad.js$redirect-rule=noopjs"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "@@||example.com/ad.js$redirect=noopjs",
        )

    def test_other_modifier_replacements_still_work(self):
        rule = "||example.com^$3p,queryprune=utm_source"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "||example.com^$third-party,removeparam=utm_source",
        )


if __name__ == "__main__":
    unittest.main()
