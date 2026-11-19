"""取得済みのGit履歴で、Squash mergeの反映先と変更内容を確認する。"""

import subprocess
import sys


def git(*args):
    return subprocess.check_output(["git", *args])


def changes(base, head):
    return git("diff", "--raw", "--no-renames", "--no-abbrev", "-z", base, head)


def verify(base, head, merged, main):
    base, head, merged, main = [
        git("rev-parse", "--verify", "--end-of-options", ref + "^{commit}").decode().strip()
        for ref in (base, head, merged, main)
    ]
    git("merge-base", "--is-ancestor", merged, main)
    parents = git("show", "-s", "--format=%P", merged).decode().split()
    if len(parents) != 1:
        raise ValueError("マージCommitの親が1件ではありません。")
    git("merge-base", "--is-ancestor", base, head)
    git("merge-base", "--is-ancestor", base, parents[0])
    expected = changes(base, head)
    if not expected or expected != changes(parents[0], merged):
        raise ValueError("PRとマージCommitの差分を個別に確認してください。")


if __name__ == "__main__":
    if len(sys.argv) != 5:
        sys.exit("引数にPRの比較元、先端、マージCommit、取得済みmainを指定してください。")
    try:
        verify(*sys.argv[1:])
    except (ValueError, subprocess.CalledProcessError) as error:
        sys.exit(str(error))
    print("mainへの到達と変更ファイルのGitオブジェクト・モードの一致を確認しました。")
