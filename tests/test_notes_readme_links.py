"""Check the percent-encoded local links in the Markdown Notes index."""
import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit


class NotesReadmeLinkTests(unittest.TestCase):
    def test_local_link_targets_exist(self):
        readme = Path(__file__).resolve().parents[1] / "Markdown Notes/README.md"
        targets = re.findall(r"\[[^\]\n]+\]\(([^\s)]+)\)", readme.read_text(encoding="utf-8"))
        self.assertTrue(targets, "No index links were collected")
        for target in targets:
            url = urlsplit(target)
            if url.scheme or url.netloc or not url.path:
                continue
            with self.subTest(target=target):
                self.assertTrue(
                    (readme.parent / unquote(url.path)).exists(),
                    f"Missing local link target: {target}",
                )
