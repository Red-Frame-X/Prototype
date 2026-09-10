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
        expected = (
            r"/^https?:\/\/[^\/]*pay[^\/]*\d[^\/]*\d[^\/]*\d"
            r"[^\/]*\.com(?:[\/?#]|$)/"
        )
        self.assertEqual(self.optimizer.optimize_line(rule), expected)

    def test_unrelated_positive_lookahead_remains_unsupported(self):
        rule = r"/pay(?=ment)/"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_negative_lookahead_remains_unsupported(self):
        rule = r"/^https?:\/\/(?!www\.)[^\/]+\.example(?:\/|$)/$document"
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )


if __name__ == "__main__":
    unittest.main()
