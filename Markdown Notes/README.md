# Markdown Notes

ChromeOS、Android、コンテンツブロック、GitHub運用に関して自分で調べた内容や検証結果を残している個人用メモです。主な目的は、学習記録、後から参照するための調査ログ、自分の環境を再構成する際の備忘録です。

> [!IMPORTANT]
> このディレクトリは一般向けの手順書・解説書として作成しているものではありません。文章は自分で作成した下書きをChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証できません。誤り、古い情報、環境依存の記述、推測が含まれる可能性があります。
>
> 仕様やUIが変わりやすい分野を含むため、重要な内容は対象製品の公式ドキュメント、公開ソース、CHANGELOG、Issues、実機の挙動などで再確認します。

## 端末・OS

- [`ChromeOS & Android Optimization Guide.md`](ChromeOS%20%26%20Android%20Optimization%20Guide.md)：自分の環境で試した設定、アプリ、拡張機能、プライバシー対策などの記録
- [`Android Advanced Flow Guide.md`](Android%20Advanced%20Flow%20Guide.md)：未確認デベロッパー製アプリ向けAdvanced Flowについて調べた内容
- [`Googlebook & Aluminium Survey Report - Revised Edition.md`](Googlebook%20%26%20Aluminium%20Survey%20Report%20-%20Revised%20Edition.md)：Googlebookと開発コードネームAluminiumの調査記録
- [`ChromeOS Manual Update and Troubleshooting.md`](ChromeOS%20Manual%20Update%20and%20Troubleshooting.md)：ChromeOSの手動更新と更新エラー時に確認した内容

## コンテンツブロック

- [`Content Blocking FAQ 2026.md`](Content%20Blocking%20FAQ%202026.md)：2026年時点のuBlock Origin / uBO Lite / AdGuard MV3 / Brave / Vivaldi / DNS併用などを整理した学習メモ
- [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md)：AdGuardルールの設計・検証についての学習記録
- [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)：AdGuard構文と実用例を自分用に整理した補助リファレンス
- [`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md)：DNSブロックリストの形式、選択、ブラウザ用コンテンツブロッカーとの役割分担についての調査メモ
- [`Strict Blocking Exceptions Test.md`](Strict%20Blocking%20Exceptions%20Test.md)：Strict blockingと例外ルールの実機検証記録

これらの文書は役割が重なる部分がありますが、後から自分の調査経緯を追えるよう、完全には統合せず残しています。

## GitHub・テンプレート

- [`Distributing Filters and UserScripts with GitHub Gist.md`](Distributing%20Filters%20and%20UserScripts%20with%20GitHub%20Gist.md)：GitHub GistでフィルタやUserScriptを扱う方法について調べた記録
- [`Handling and Reporting GitHub CI Failures (✕).md`](Handling%20and%20Reporting%20GitHub%20CI%20Failures%20%28%E2%9C%95%29.md)：CI失敗の確認、切り分け、記録方法
- [`Header Template.md`](Header%20Template.md)：個人メモ用ヘッダーのひな形
- [`Collapse Comments on GitHub Issues and Pull Requests.md`](Collapse%20Comments%20on%20GitHub%20Issues%20and%20Pull%20Requests.md)：GitHub Issues / Pull Requestで長文を折りたたむために保存しているスニペット

## 情報の扱い

- 対象製品・プロジェクトの公式ドキュメント、公式リポジトリ、公開ソースコード、CHANGELOG、Issuesなどの一次情報を優先します。
- 公式資料だけで確認できない事項は、信頼できる複数の情報源や実機検証を補助的に使い、事実・観測結果・推測をできる限り区別します。
- 実機検証やユーザー報告は、そのまま一般仕様として扱いません。
- 根拠を確認できない原因推測や将来予測は断定せず、仕様変更によって古くなった記述は参照元を再確認したうえで更新または削除します。
- ChatGPTで推敲した文章も正しいとは限らないため、重要な技術情報は必ず一次情報や実環境で再確認します。

コマンド、設定変更、フィルタルールなどは、自分の環境で変更履歴や影響範囲を把握できる状態で少数ずつ検証します。

文書のライセンス、第三者コンテンツの扱いおよび無保証については、共通の[`LICENSES.md`](../LICENSES.md)を参照します。
