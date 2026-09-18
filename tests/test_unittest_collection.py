from __future__ import annotations

import ast
import unittest
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
TEST_DIRS = (ROOT / "tests",)


class UnittestCollectionContractTests(unittest.TestCase):
    def test_no_pytest_style_top_level_test_functions(self) -> None:
        """Keep every test discoverable by the repository's unittest command."""
        undiscoverable: list[str] = []
        for test_dir in TEST_DIRS:
            for path in sorted(test_dir.glob("test_*.py")):
                tree = ast.parse(path.read_text(encoding="utf-8"), filename=str(path))
                for node in tree.body:
                    if isinstance(node, (ast.FunctionDef, ast.AsyncFunctionDef)):
                        if node.name.startswith("test"):
                            undiscoverable.append(f"{path.relative_to(ROOT)}:{node.lineno}")

        self.assertEqual(
            undiscoverable,
            [],
            "Top-level test functions are not collected by unittest discover: "
            + ", ".join(undiscoverable),
        )


if __name__ == "__main__":
    unittest.main()
