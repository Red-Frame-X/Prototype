import unittest

from scripts.convert import AdGuardOptimizer


class Re2BackreferenceTests(unittest.TestCase):
    def setUp(self):
        self.optimizer = AdGuardOptimizer()

    def assert_unsupported(self, rule: str) -> None:
        self.assertEqual(
            self.optimizer.optimize_line(rule),
            "! [Unsupported MV3 Regex] " + rule,
        )

    def test_numeric_backreference_is_rejected(self):
        self.assert_unsupported(r"/(tracker)\1/")

    def test_g_number_backreference_is_rejected(self):
        self.assert_unsupported(r"/(tracker)\g1/")

    def test_g_braced_backreference_is_rejected(self):
        self.assert_unsupported(r"/(tracker)\g{1}/")

    def test_g_named_backreference_is_rejected(self):
        self.assert_unsupported(r"/(?P<id>tracker)\g{id}/")

    def test_k_angle_named_backreference_is_rejected(self):
        self.assert_unsupported(r"/(?P<id>tracker)\k<id>/")

    def test_k_quoted_named_backreference_is_rejected(self):
        self.assert_unsupported(r"/(?P<id>tracker)\k'id'/")

    def test_escaped_backslash_before_k_is_not_misclassified(self):
        rule = r"/tracker\\k<id>/"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)

    def test_escaped_backslash_before_g_is_not_misclassified(self):
        rule = r"/tracker\\g{name}/"
        self.assertEqual(self.optimizer.optimize_line(rule), rule)


if __name__ == "__main__":
    unittest.main()
