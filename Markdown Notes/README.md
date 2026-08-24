# Markdown Notes

ChromeOS、Android、コンテンツブロック、GitHub運用に関する調査メモと手順書です。仕様やUIが変わりやすい分野を含むため、各文書の更新日と参照先の公式情報を併せて確認してください。

## 端末・OS

- [`ChromeOS & Android Optimization Guide.md`](ChromeOS%20%26%20Android%20Optimization%20Guide.md)：設定、アプリ、拡張機能、プライバシー対策の総合ガイド
- [`Android Advanced Flow Guide.md`](Android%20Advanced%20Flow%20Guide.md)：未確認デベロッパー製アプリ向けAdvanced Flowの概要
- [`Googlebook & Aluminium Survey Report - Revised Edition.md`](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md)：Googlebookと開発コードネームAluminiumの調査
- [`ChromeOS Manual Update and Troubleshooting.md`](ChromeOS%20Manual%20Update%20and%20Troubleshooting.md)：ChromeOSの手動更新と更新エラー時のトラブルシューティング

## コンテンツブロック

- [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md)：AdGuardルールの設計・検証指針
- [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)：AdGuard構文と実用例の補助リファレンス
- [`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md)：DNSブロックリストの形式、選択、運用
- [`Strict Blocking Exceptions Test.md`](Strict%20Blocking%20Exceptions%20Test.md)：Strict blockingと例外ルールの実機検証記録

## GitHub・テンプレート

- [`Distributing Filters and UserScripts with GitHub Gist.md`](Distributing%20Filters%20and%20UserScripts%20with%20GitHub%20Gist.md)：GitHub Gistを使ったコンテンツブロックフィルタ／UserScriptの配布・更新方法とメタデータテンプレート
- [`Handling and Reporting GitHub CI Failures (✕).md`](Handling%20and%20Reporting%20GitHub%20CI%20Failures%20%28%E2%9C%95%29.md)：CI失敗の確認、切り分け、報告
- [`Header Template.md`](Header%20Template.md)：文書ヘッダーのひな形
- [`Collapse Comments on GitHub Issues and Pull Requests.md`](Collapse%20Comments%20on%20GitHub%20Issues%20and%20Pull%20Requests.md)：GitHub Issues / Pull Requestで長文を折りたたむためのスニペット

## 情報の扱い

各文書では、対象製品・プロジェクトの公式ドキュメント、公式リポジトリ、公開ソースコード、CHANGELOG、Issuesなどの一次情報を優先します。公式資料だけで確認できない事項は、信頼できる複数の情報源や実機検証を補助的に用い、事実・観測結果・推測を区別します。

実機検証やユーザー報告は、それ自体を一般仕様として扱いません。根拠を確認できない原因推測や将来予測は断定せず、仕様変更によって古くなった記述は参照元を再確認したうえで更新または削除します。

コマンド、設定変更、フィルタルールなどを実行する場合は、対象バージョンと適用範囲を確認し、可能な場合は元に戻せる状態で少数ずつ検証してください。

文書のライセンス、第三者コンテンツの扱いおよび無保証については、共通の[`LICENSES.md`](../LICENSES.md)を参照してください。
