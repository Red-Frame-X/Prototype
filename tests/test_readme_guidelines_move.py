"""READMEから独立文書への安全な移行検証。"""
import importlib.util
from pathlib import Path
import unittest
from unittest.mock import patch

SCRIPT = Path(__file__).resolve().parents[1] / "scripts" / "check_large_content_loss.py"
spec = importlib.util.spec_from_file_location("content_loss_guard", SCRIPT)
guard = importlib.util.module_from_spec(spec)
spec.loader.exec_module(guard)

HEADING = "## 編集・更新の原則\n"
BODY = (
    HEADING
    + "既存の説明です。\n"
    + "[AGENTS.md](AGENTS.md)\n"
    + "[CONTRIBUTING.md](CONTRIBUTING.md)\n"
    + "(./.github/COMMIT_JA_AUTOMATION.md)\n"
    + "\n## 自動更新と品質確認\n\n```bash\necho ok\n```\n"
    + "\n## 方針\n\n維持します。\n"
    + "\n## 表記の方針\n\n名称を保持します。\n"
)
PREFIX = "# README\n\n変更しない内容。\n\n"
LINK = (
    "## 編集・更新・品質管理方針\n\n"
    "詳細は [Repositoryの編集・更新・品質管理方針]"
    "(./.github/REPOSITORY_GUIDELINES.md) を参照してください。\n"
)
GUIDE_BODY = (
    BODY.replace("[AGENTS.md](AGENTS.md)", "[AGENTS.md](../AGENTS.md)")
    .replace("[CONTRIBUTING.md](CONTRIBUTING.md)", "[CONTRIBUTING.md](../CONTRIBUTING.md)")
    .replace("(./.github/COMMIT_JA_AUTOMATION.md)", "(./COMMIT_JA_AUTOMATION.md)")
)


class VerifiedMoveTest(unittest.TestCase):
    def check(self, readme=PREFIX + LINK, guide="文書の説明\n" + GUIDE_BODY):
        contents = {
            "base:README.md": PREFIX + BODY,
            "HEAD:README.md": readme,
            "HEAD:.github/REPOSITORY_GUIDELINES.md": guide,
        }

        def show(*args):
            return contents[args[1]]

        with patch.object(guard, "run_git", side_effect=show), patch.object(
            guard, "line_count", return_value=None
        ):
            return guard.verified_readme_guidelines_move("base")

    def test_complete_move(self):
        self.assertTrue(self.check())

    def test_missing_line(self):
        self.assertFalse(self.check(guide=GUIDE_BODY.replace("既存の説明です。\n", "")))

    def test_missing_code_block(self):
        self.assertFalse(self.check(guide=GUIDE_BODY.replace("```bash\necho ok\n```\n", "")))

    def test_broken_link(self):
        self.assertFalse(self.check(guide=GUIDE_BODY.replace("../AGENTS.md", "./AGENTS.md")))

    def test_unrelated_readme_edit(self):
        self.assertFalse(self.check(readme=(PREFIX + LINK).replace("変更しない内容。", "変更した内容。")))

    def test_duplicate_move(self):
        self.assertFalse(self.check(guide=GUIDE_BODY + GUIDE_BODY))


if __name__ == "__main__":
    unittest.main()
