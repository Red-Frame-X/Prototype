# My docomoにおけるStrict blockingの挙動と例外ルール検証

AdGuard製品で `||mydocomo.docomo.ne.jp^$document` を適用した際の実機検証メモです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260825 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 動作環境

- **Desktop**：ChromeOS / Chrome / AdGuard ブラウザ拡張機能 MV3対応版
- **Mobile**：Android / Chrome / AdGuard for Android

## 公式仕様

AdGuardの `$document` は、ブラウザタブに読み込まれるメインフレームのHTMLドキュメントを対象とします。ブロックルールに明示すると通常のmain-frame bypassを無効化してブロッキングページを表示します。

一方、`@@||example.com^$document` のような `$document` 例外は、AdGuard公式仕様では対象ページのフィルタリング全体を無効化するルールで、`$elemhide`、`$content`、`$urlblock`、`$jsinject`、`$extension` を同時に指定するのと同等です。

したがって、以前の版にあった「`$document` 例外ではExtended CSSやScriptletが引き続き作動し、それがMy docomoのエラー原因になっている可能性が高い」という説明は公式仕様と整合しないため削除しました。

## 実機で確認した挙動

以下は上記環境での観測結果であり、AdGuard全製品・全バージョンに一般化するものではありません。

- `||mydocomo.docomo.ne.jp^$document`：AdGuardのブロッキングページが表示され、メインドキュメントが遮断される。
- `@@||mydocomo.docomo.ne.jp^$all`：検証環境ではブロッキングページを回避できなかった。
- `@@||mydocomo.docomo.ne.jp^$document`：メインドキュメントへのアクセスは回復したが、検証時にはサイト側でエラーダイアログが発生することがあった。

最後のエラーダイアログについて、HTTPSフィルタリング、DNS保護、Extended CSS、Scriptletなど特定の機能を原因と断定できる公開情報は確認できませんでした。そのため原因推測は削除し、観測事実だけを残します。

## 解釈上の注意

AdGuardとuBlock Originは似たフィルタ構文を持ちますが、同じ修飾子名でも意味や例外処理が完全に同一とは限りません。クロスエンジン向けルールでは、それぞれの公式構文を個別に確認してください。

## 参照

- [AdGuard — How to create your own ad filters](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [uBlock Origin Wiki — Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [uBlock Origin Wiki — Strict blocking](https://github.com/gorhill/uBlock/wiki/Strict-blocking)
