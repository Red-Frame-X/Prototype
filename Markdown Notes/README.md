# Markdown Notes

ChromeOS、Android、コンテンツブロック、GitHub運用に関する調査メモと手順書です。個人の学習記録・検証ログ・設定バックアップとして後から再利用できるよう、一般的な解説、手順、比較情報もできるだけ削らずに残しています。仕様やUIが変わりやすい分野を含むため、各文書の更新日と参照先の公式情報を併せて確認します。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 202609201601 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## ドキュメント案内

### 端末・OS

| ドキュメント | 主な内容 |
| --- | --- |
| [`ChromeOS & Android Optimization Guide.md`](ChromeOS%20%26%20Android%20Optimization%20Guide.md) | ChromeOS・Androidの設定、アプリ、拡張機能、プライバシー対策、実機トラブル対応をまとめた総合ガイド兼設定バックアップ |
| [`Linux Mint Guide.md`](Linux%20Mint%20Guide.md) | Linux Mintの導入、設定、ソフトウェア管理、バックアップ、復旧、Kernel Panic、AdGuard for Linux、セキュリティなどをまとめたガイド |
| [`Android Advanced Flow Guide.md`](Android%20Advanced%20Flow%20Guide.md) | 未確認デベロッパー製AndroidアプリをインストールするAdvanced Flowの概要、公式要件、手順、注意点の確認記録 |
| [`Googlebook & Aluminium Survey Report - Revised Edition.md`](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md) | Googlebookの公式発表と、開発コードネームAluminiumに関する報道・未確認事項・査読結果を区別して整理した調査レポート |
| [`ChromeOS Manual Update and Troubleshooting.md`](ChromeOS%20Manual%20Update%20and%20Troubleshooting.md) | ChromeOSの手動更新手順と、更新失敗時の原因切り分け・再試行・復旧方法の記録 |

### コンテンツブロック

| ドキュメント | 主な内容 |
| --- | --- |
| [`Content Blocking FAQ 2026.md`](Content%20Blocking%20FAQ%202026.md) | uBlock Origin、uBlock Origin Lite、AdGuard MV3、Brave、Vivaldi、DNS併用、フィルタ設計を一次情報中心に整理したFAQ |
| [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md) | AdGuard ブラウザ拡張機能 MV3対応版とAdGuard for Androidでカスタムルールを設計・検証するための指針と学習メモ |
| [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md) | AdGuardの主要フィルタ構文、MV3/DNRとCoreLibsの差異、用途・注意点を確認する補助リファレンス |
| [`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md) | DNSブロックリストの主要形式、選び方、ブラウザ用コンテンツブロッカーとの役割分担・切り分けを整理したガイド |
| [`Strict Blocking Exceptions Test.md`](Strict%20Blocking%20Exceptions%20Test.md) | My docomoを対象に、AdGuardのStrict blockingと`$document`例外ルールの挙動を実機検証した記録 |

### コンテンツブロック資料の使い分け

- [`Content Blocking FAQ 2026.md`](Content%20Blocking%20FAQ%202026.md)：**製品選択・MV3・フィルタ併用の考え方を確認する**
- [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md)：**AdGuardユーザールールの設計方法を学ぶ**
- [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)：**個別のAdGuard構文を確認する**
- [`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md)：**DNSレイヤーのブロックリストとブラウザブロッカーの違いを確認する**
- [`Strict Blocking Exceptions Test.md`](Strict%20Blocking%20Exceptions%20Test.md)：**Strict blockingと例外ルールの実機挙動を確認する**

ブラウザ用コンテンツブロッカーを複数重ねることと、ブラウザブロッカーにDNSブロックを組み合わせることは区別します。uBlock Origin公式は他のブラウザ用コンテンツブロッカーとの併用を非推奨としていますが、DNSブロックは別レイヤーです。DNS併用時は、誤ブロック発生時に各レイヤーを切り離して検証できる構成にします。

Chromium系ではManifest V3の影響を受けるため、フル版uBlock Origin、uBlock Origin Lite、AdGuard Browser Extension MV3を同じ機能の製品として扱わず、DNRへの変換可否、サイト権限、フィルタリングモード、更新方式の差を確認します。

### GitHub・テンプレート

| ドキュメント | 主な内容 |
| --- | --- |
| [`Distributing Filters and UserScripts with GitHub Gist.md`](Distributing%20Filters%20and%20UserScripts%20with%20GitHub%20Gist.md) | GitHub Gistを使ったコンテンツブロックフィルタ／UserScriptの配布・更新方法とメタデータテンプレート |
| [`Handling and Reporting GitHub CI Failures (✕).md`](Handling%20and%20Reporting%20GitHub%20CI%20Failures%20%28%E2%9C%95%29.md) | GitHub Actions / CI失敗時の確認、原因切り分け、ログ確認、報告手順 |
| [`Header Template.md`](Header%20Template.md) | Markdown Notesで共通利用するメタデータ、ライセンス案内、Version表記のヘッダーテンプレート |
| [`Collapse Comments on GitHub Issues and Pull Requests.md`](Collapse%20Comments%20on%20GitHub%20Issues%20and%20Pull%20Requests.md) | GitHub Issues / Pull Requestで長文や補足情報を`<details>`で折りたたむためのスニペット |

## 情報の扱い

各文書では、対象製品・プロジェクトの公式ドキュメント、公式リポジトリ、公開ソースコード、CHANGELOG、Issuesなどの一次情報を優先します。公式資料だけで確認できない事項は、信頼できる複数の情報源や実機検証を補助的に用い、事実・観測結果・推測を区別します。

実機検証やユーザー報告は、それ自体を一般仕様として扱いません。根拠を確認できない原因推測や将来予測は断定せず、仕様変更によって古くなった記述は参照元を再確認したうえで更新または削除します。

日付付きの「2026年○月○日時点」という表現は、更新履歴として必要な場合を除き固定せず、本文のメタデータ `Version` と参照先の一次情報を優先します。将来の査読時に、本文だけが古い基準日のまま残ることを避けます。

文章の下書きや整理にChatGPTを利用することがありますが、生成・推敲された文章をそのまま正しいとはみなさず、重要な技術情報は一次情報や実環境で再確認します。

コマンド、設定変更、フィルタルールなどを実行する場合は、対象バージョンと適用範囲を確認し、可能な場合は元に戻せる状態で少数ずつ検証します。

文書のライセンス、第三者コンテンツの扱いおよび無保証については、共通の[`LICENSES.md`](../LICENSES.md)を参照します。

## 関連情報

- [リポジトリのルートREADME](../README.md)
- [Markdown Notesディレクトリ](./)
