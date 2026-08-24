# Distributing Filters and UserScripts with GitHub Gist

GitHub Gistを利用して、コンテンツブロックフィルタやUserScriptを配布・更新する際の手順と、推奨メタデータをまとめたメモです。

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

### コンテンツブロックフィルタ用メタデータのテンプレート

AdGuardの公開フィルタとFilters Registryでは、フィルタ名、説明、ホームページ、更新間隔、バージョンなどのメタデータが管理されています。自作フィルタをURL配布する場合も、利用者が内容・配布元・更新頻度を判断できるよう、先頭にメタデータをまとめておくと管理しやすくなります。

以下は、AdGuard系フィルタで一般的に使いやすいテンプレートです。

```adblock
! Title: Example Filter
! Description: Short description of this filter.
! Homepage: https://example.com/
! License: CC0-1.0
! Version: 1.0.0
! TimeUpdated: 2026-08-24T00:00:00+09:00
! Expires: 1 day

! Filtering rules start below.
```

各項目の位置付けは次のとおりです。

| 項目 | 位置付け | 用途 |
| :--- | :--- | :--- |
| `! Title:` | 推奨 | フィルタ名を明示する |
| `! Description:` | 推奨 | 対象・目的を簡潔に説明する |
| `! Homepage:` | 推奨 | 配布元、README、Repositoryなどを示す |
| `! License:` | 推奨 | 再配布・改変条件を明示する |
| `! Version:` | 推奨 | 配布物の版を識別する |
| `! TimeUpdated:` | 任意 | 最終更新日時を明示する |
| `! Expires:` | 推奨 | フィルタ側が希望する更新間隔を示す |

`! Expires:` は更新間隔のメタデータとしてAdGuardのフィルタ基盤でも使用されていますが、実際の再取得タイミングは利用するAdGuard製品や設定にも依存します。`! Version:` や `! TimeUpdated:` も、単独で「この値を変えれば必ず更新される」という意味ではありません。

第三者フィルタとの互換性も考える場合は、独自メタデータを増やしすぎず、名称、説明、配布元、ライセンス、版、更新間隔などの基本情報に絞る方が扱いやすくなります。

## UserScriptで利用する場合

TampermonkeyなどのUserScriptマネージャーでGistを利用する場合、インストール・自動更新の条件は各マネージャーの仕様に従います。`@version`、`@updateURL`、`@downloadURL`などの扱いも、利用するマネージャーの公式ドキュメントを確認してください。

### UserScript用メタデータのテンプレート

TampermonkeyとViolentmonkeyはいずれも、UserScriptの先頭に `// ==UserScript==` から `// ==/UserScript==` までのメタデータブロックを置く形式を採用しています。

汎用的な最小テンプレートは次のとおりです。

```javascript
// ==UserScript==
// @name         Example UserScript
// @namespace    https://example.com/userscripts
// @version      1.0.0
// @description  Short description of this userscript.
// @author       Your Name
// @homepageURL  https://example.com/
// @supportURL   https://example.com/issues
// @match        https://example.com/*
// @grant        none
// ==/UserScript==
```

Gistなどから自動更新させる場合は、必要に応じて次の項目を追加します。

```javascript
// @updateURL    https://example.com/script.meta.js
// @downloadURL  https://example.com/script.user.js
```

主な項目の考え方は次のとおりです。

| 項目 | 位置付け | 用途 |
| :--- | :--- | :--- |
| `@name` | 必須相当 | スクリプト名。各UserScriptマネージャーで識別・表示に使われる |
| `@namespace` | 強く推奨 | `@name` と組み合わせてスクリプトを識別する。Violentmonkeyはこの組み合わせを一意識別子として説明している |
| `@version` | 自動更新する場合は必須 | 更新版の比較に使われる。更新のたびに増加させる |
| `@description` | 推奨 | スクリプトの目的を説明する |
| `@author` | 任意 | 作者を示す |
| `@homepageURL` | 推奨 | Repositoryや説明ページを示す |
| `@supportURL` | 任意 | Issue trackerなど問い合わせ先を示す |
| `@match` | 強く推奨 | 実行対象URLを必要な範囲に限定する |
| `@grant` | 明示推奨 | 使用するGM APIなどの権限を列挙する。不要なら `none` を明示する |
| `@updateURL` | 任意 | 更新確認に使うURLを指定する |
| `@downloadURL` | 任意 | 更新版スクリプトの取得URLを指定する |

実行範囲は必要以上に広げず、`@match https://*/*` や全サイト相当の指定は、その必要性が明確な場合だけ使用します。また、GM APIを使う場合は必要な権限だけを `@grant` に列挙します。

`@version` はTampermonkeyでは更新判定に利用され、Violentmonkeyでも未指定の場合は自動更新されないと明記されています。そのため、継続配布するUserScriptでは版番号を必ず管理するのが適切です。

## 参照

- [GitHub Docs — Creating gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- [GitHub Docs — Forking and cloning gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/forking-and-cloning-gists)
- [AdGuard Browser Extension — Filters](https://adguard.com/kb/adguard-browser-extension/features/filters/)
- [AdGuard — How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [AdGuard Filters Registry](https://github.com/AdguardTeam/FiltersRegistry)
- [Tampermonkey Documentation — Userscript Header](https://www.tampermonkey.net/documentation.php)
- [Violentmonkey — Metadata Block](https://violentmonkey.github.io/api/metadata-block/)
