# How to Use Gists

GitHub Gistを利用して、カスタムフィルタやUserScriptを配布する際のメモです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260824 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## GistとRepositoryの使い分け

Gistは少数のコード・テキストファイルを公開・共有する用途に向いており、各Gist自体がGit Repositoryとして履歴を持ちます。一方、通常のGitHub RepositoryはIssues、Pull Requests、GitHub Actionsなどを組み合わせた継続的な開発・保守に向いています。

フィルタやUserScriptを長期運用し、lint・テスト・Issue管理まで行う場合は通常のRepositoryの方が管理機能を利用しやすくなります。

## Raw URLを使う

1. Gistで対象ファイルの **Raw** を開きます。
2. 表示されたRaw URLを配布先で利用します。
3. 特定のrevisionを固定したい場合は、そのrevisionを指すURLを使用します。
4. 最新版を追従させる用途では、実際に利用するURLが更新後の内容を返すことを確認します。

以前の版では「URLからコミットハッシュを削除すれば常にHEADを参照する」「Raw URLは数分間キャッシュされる」と具体的に断定していました。GitHub公式ドキュメントでこれらの配信挙動を安定した契約仕様として確認できなかったため、その断定は削除しました。

## AdGuardで利用する場合

AdGuard Browser Extensionは、URLまたはローカルファイルからカスタムフィルタを追加できます。Gistを配布元にする場合も、最終的にはAdGuardが取得できるRaw URLを指定します。

フィルタの更新間隔やメタデータの解釈はGitHub GistではなくAdGuard側の仕様です。`! Version:` だけを更新検知の仕組みとみなさず、利用するAdGuard製品の公式仕様を確認してください。

## UserScriptで利用する場合

TampermonkeyなどのUserScriptマネージャーでGistを利用する場合、インストール・自動更新の条件は各マネージャーの仕様に従います。`@version`、`@updateURL`、`@downloadURL`などの扱いも、利用するマネージャーの公式ドキュメントを確認してください。

## 参照

- [GitHub Docs — Creating gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- [GitHub Docs — Forking and cloning gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/forking-and-cloning-gists)
- [AdGuard Browser Extension — Filters](https://adguard.com/kb/adguard-browser-extension/features/filters/)
