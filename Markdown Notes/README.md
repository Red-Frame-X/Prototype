# Markdown Notes

ChromeOS、Android、コンテンツブロック、GitHub運用に関する調査メモと手順書です。仕様が変わりやすい分野は、本文の日付とリンク先の情報を併せて確認してください。

## 端末・OS

- [`ChromeOS & Android Optimization Guide.md`](ChromeOS%20%26%20Android%20Optimization%20Guide.md)：設定、アプリ、拡張機能、プライバシー対策の総合ガイド
- [`Android Advanced Flow Guide.md`](Android%20Advanced%20Flow%20Guide.md)：未確認デベロッパー製アプリ向けAdvanced Flowの概要
- [`Aluminium OS（ALOS）Survey Report - Revised Edition.md`](Aluminium%20OS%EF%BC%88ALOS%EF%BC%89Survey%20Report%20-%20Revised%20Edition.md)：Googlebookと開発コードネームAluminiumの調査
- [`Forced Updates via Crosh (Chrome OS Developer Shell).md`](Forced%20Updates%20via%20Crosh%20%28Chrome%20OS%20Developer%20Shell%29.md)：ChromeOSの更新手順とCrosh利用上の注意

## コンテンツブロック

- [`Designing AdGuard Custom Rules.md`](Designing%20AdGuard%20Custom%20Rules.md)：AdGuardルールの設計・検証指針
- [`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)：AdGuard構文と実用例の補助リファレンス
- [`DNS Blocklist Guide.md`](DNS%20Blocklist%20Guide.md)：DNSブロックリストの形式、選択、運用
- [`Strict Blocking Exceptions Test.md`](Strict%20Blocking%20Exceptions%20Test.md)：Strict blockingと例外ルールの実機検証記録

## GitHub・テンプレート

- [`How to Use Gists.md`](How%20to%20Use%20Gists.md)：GistをフィルタやUserScriptの配布に利用する際の注意点
- [`Handling and Reporting GitHub CI Failures (✕).md`](Handling%20and%20Reporting%20GitHub%20CI%20Failures%20%28%E2%9C%95%29.md)：CI失敗の確認、切り分け、報告
- [`Header Template.md`](Header%20Template.md)：文書ヘッダーのひな形
- [`Collapse Comments on this Issues.md`](Collapse%20Comments%20on%20this%20Issues.md)：GitHub Issue / PRで長文を折りたたむためのスニペット

## 情報の扱い

各文書では公式ドキュメントやプロジェクト自身の公開資料を優先します。公式資料だけで確認できない場合でも、Web検索によって信頼できる一次資料・公開ソース・Issue・複数の独立した情報源などから十分な裏付けを得られる内容は残します。

実機検証やユーザー報告は、それ自体を仕様として一般化せず、観測結果・報告として区別します。Web検索を行っても正確な根拠を得られない原因推測や断定は削除対象とし、同じ説明の反復や過剰な用語解説は意味を保ったまま整理します。

文書のライセンス、第三者コンテンツの扱いおよび無保証については、共通の[`LICENSES.md`](../LICENSES.md)を参照してください。
