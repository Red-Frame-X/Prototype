# GitHub Gistでフィルタ・UserScriptを扱うための個人メモ

GitHub Gistを利用して、自分のコンテンツブロックフィルタやUserScriptを保存・参照・更新するときに確認する仕様とメタデータをまとめた個人用メモです。

> [!NOTE]
> この文書は自分の運用を再現するための備忘録であり、一般向けの配布ガイドや推奨テンプレートを目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。実際に公開・更新するときは、GitHub、AdGuard、UserScriptマネージャーの公式資料を再確認します。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

## Gistとリポジトリの使い分けメモ

Gistは少数のコード・テキストファイルを公開・共有する用途に向いており、各Gist自体がGitリポジトリとして履歴を持ちます。一方、通常のGitHubリポジトリはIssues、Pull Requests、GitHub Actionsなどを組み合わせた継続的な開発・保守に向いています。

自分がフィルタやUserScriptを長期運用し、lint・テスト・Issues管理まで行う場合は、通常のリポジトリの方が管理機能を利用しやすいと判断しています。

## Raw URLの扱いメモ

1. Gistで対象ファイルの **Raw** を開く。
2. 表示されたRaw URLを必要な設定先で使う。
3. 特定のrevisionを固定したい場合は、そのrevisionを指すURLを使う。
4. 最新版を追従させる用途では、実際に利用するURLが更新後の内容を返すことを確認する。

以前の版では「URLからコミットハッシュを削除すれば常にHEADを参照する」「Raw URLは数分間キャッシュされる」と具体的に断定していました。GitHub公式ドキュメントでこれらの配信挙動を安定した契約仕様として確認できなかったため、その断定は削除しました。

## AdGuardで使う場合の自分用メモ

AdGuard Browser Extensionは、URLまたはローカルファイルからカスタムフィルタを追加できます。自分がGistを参照元にする場合も、最終的にはAdGuardが取得できるRaw URLを指定します。

フィルタの更新間隔やメタデータの解釈はGitHub GistではなくAdGuard側の仕様です。`! Version:`だけを更新検知の仕組みとみなさず、使用中のAdGuard製品の公式仕様を確認します。

### コンテンツブロックフィルタ用メタデータの控え

AdGuardの公開フィルタとFilters Registryでは、フィルタ名、説明、ホームページ、更新間隔、バージョンなどのメタデータが管理されています。自分のフィルタでも、後から内容・由来・版を追いやすいよう、必要なメタデータを先頭にまとめています。

自分用のひな形：

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

各項目の位置付けを自分用に整理すると次のとおりです。

| 項目 | 自分の扱い | 用途 |
| :--- | :--- | :--- |
| `! Title:` | 基本的に記載 | フィルタ名を識別する |
| `! Description:` | 基本的に記載 | 対象・目的を簡潔に残す |
| `! Homepage:` | 必要に応じて記載 | 元リポジトリや関連メモを示す |
| `! License:` | ライセンスがある場合に記載 | 再利用・改変条件を確認する |
| `! Version:` | 基本的に記載 | 保存している版を識別する |
| `! TimeUpdated:` | 必要な場合に記載 | 最終更新日時を残す |
| `! Expires:` | 自動更新を使う場合に確認 | フィルタ側が希望する更新間隔を示す |

`! Expires:`は更新間隔のメタデータとしてAdGuardのフィルタ基盤でも使用されていますが、実際の再取得タイミングは利用するAdGuard製品や設定にも依存します。`! Version:`や`! TimeUpdated:`も、単独で「この値を変えれば必ず更新される」という意味ではありません。

第三者フィルタとの互換性を考える場合は、独自メタデータを増やしすぎず、名称、説明、由来、ライセンス、版、更新間隔などの基本情報に絞る方が自分でも追跡しやすくなります。

## UserScriptで使う場合の自分用メモ

TampermonkeyなどのUserScriptマネージャーでGistを利用する場合、インストール・自動更新の条件は各マネージャーの仕様に従います。`@version`、`@updateURL`、`@downloadURL`などの扱いも、使用中のマネージャーの公式ドキュメントを確認します。

### UserScript用メタデータの控え

TampermonkeyとViolentmonkeyはいずれも、UserScriptの先頭に `// ==UserScript==` から `// ==/UserScript==` までのメタデータブロックを置く形式を採用しています。

自分用の最小ひな形：

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

Gistなどから自動更新させる場合に確認する項目：

```javascript
// @updateURL    https://example.com/script.meta.js
// @downloadURL  https://example.com/script.user.js
```

主な項目を自分用に整理すると次のとおりです。

| 項目 | 自分の扱い | 用途 |
| :--- | :--- | :--- |
| `@name` | 必須相当 | スクリプト名。各UserScriptマネージャーで識別・表示に使われる |
| `@namespace` | 原則記載 | `@name` と組み合わせてスクリプトを識別する |
| `@version` | 更新管理時に必須 | 更新版の比較に使われる。更新時に増加させる |
| `@description` | 原則記載 | スクリプトの目的を残す |
| `@author` | 任意 | 作者情報を示す |
| `@homepageURL` | 必要に応じて記載 | リポジトリや説明ページを示す |
| `@supportURL` | 必要に応じて記載 | Issuesなど関連先を示す |
| `@match` | 原則記載 | 実行対象URLを必要な範囲に限定する |
| `@grant` | 明示する | 使用するGM APIなどの権限を列挙し、不要なら `none` を明示する |
| `@updateURL` | 必要な場合のみ | 更新確認に使うURLを指定する |
| `@downloadURL` | 必要な場合のみ | 更新版スクリプトの取得URLを指定する |

自分のスクリプトでは実行範囲を必要以上に広げず、`@match https://*/*`や全サイト相当の指定は、その必要性を説明できる場合だけ使います。また、GM APIを使う場合は必要な権限だけを`@grant`に列挙します。

`@version`はTampermonkeyでは更新判定に利用され、Violentmonkeyでも未指定の場合は自動更新されないと明記されています。そのため、自分が継続更新するUserScriptでは版番号を管理します。

## 参照する公式資料

- [GitHub Docs — Creating gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/creating-gists)
- [GitHub Docs — Forking and cloning gists](https://docs.github.com/en/get-started/writing-on-github/editing-and-sharing-content-with-gists/forking-and-cloning-gists)
- [AdGuard Browser Extension — Filters](https://adguard.com/kb/adguard-browser-extension/features/filters/)
- [AdGuard — How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [AdGuard Filters Registry](https://github.com/AdguardTeam/FiltersRegistry)
- [Tampermonkey Documentation — Userscript Header](https://www.tampermonkey.net/documentation.php)
- [Violentmonkey — Metadata Block](https://violentmonkey.github.io/api/metadata-block/)
