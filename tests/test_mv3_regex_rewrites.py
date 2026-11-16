import re
import unittest

from scripts.convert import AdGuardOptimizer


class MV3RegexRewriteTests(unittest.TestCase):
    def setUp(self):
        self.optimizer = AdGuardOptimizer()

    def test_digit_triplet_positive_lookahead_is_rewritten_equivalently(self):
        rule = (
            r"/^https?:\/\/[^\/]*pay(?=[^\/]*\d[^\/]*\d[^\/]*\d)"
            r"[^\/]*\.com(?:[/?#]|$)/"
        )
        converted = self.optimizer.optimize_line(rule)
        self.assertNotIn("(?=", converted)
        original_pattern = re.compile(rule[1:-1])
        converted_pattern = re.compile(converted[1:-1])
        for host in ("pay", "pay1", "pay12", "pay123", "pay1234", "xpay"):
            for delimiter in ("", "/", "?", "#"):
                for suffix in ("", "1", "12", "123", "1234", "a1b2c3", "1/23"):
                    url = "https://" + host + ".com" + delimiter + suffix
                    with self.subTest(url=url):
                        self.assertEqual(
                            bool(original_pattern.search(url)),
                            bool(converted_pattern.search(url)),
                        )
        self.assertTrue(converted_pattern.search("https://pay.com?123"))
        self.assertTrue(converted_pattern.search("https://pay1.com#23"))
        self.assertFalse(converted_pattern.search("https://pay.com/123"))

    def test_unrelated_positive_lookahead_remains_unsupported(self):
        rule = r"/pay(?=ment)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [MV3未対応の正規表現] " + rule,
        )

    def test_negative_lookahead_remains_unsupported(self):
        rule = r"/^https?:\/\/(?!www\.)[^\/]+\.example(?:\/|$)/$document"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [MV3未対応の正規表現] " + rule,
        )


if __name__ == "__main__":
    unittest.main()
