# My docomo Strict blocking 実機検証メモ

AdGuard製品で `||mydocomo.docomo.ne.jp^$document` を適用した際に、自分の環境で確認した挙動を残す個人用の実機検証記録です。

> [!NOTE]
> この文書は特定時点・特定環境での観測を後から追うためのメモであり、一般向けの設定ガイドや推奨ルールを目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。仕様解釈はAdGuard公式資料を優先し、観測結果を全製品・全バージョンへ一般化しません。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

## 検証した環境

- **Desktop**：ChromeOS / Chrome / AdGuard ブラウザ拡張機能 MV3対応版
- **Mobile**：Android / Chrome / AdGuard for Android

## 検証時に確認した公式仕様

AdGuardの `$document` は、ブラウザタブに読み込まれるメインフレームのHTMLドキュメントを対象とします。ブロックルールに明示すると通常のmain-frame bypassを無効化してブロッキングページを表示します。

一方、`@@||example.com^$document` のような `$document` 例外は、AdGuard公式仕様では対象ページのフィルタリング全体を無効化するルールで、`$elemhide`、`$content`、`$urlblock`、`$jsinject`、`$extension` を同時に指定するのと同等です。

したがって、以前の版にあった「`$document` 例外ではExtended CSSやScriptletが引き続き作動し、それがMy docomoのエラー原因になっている可能性が高い」という説明は公式仕様と整合しないため削除しました。

## 自分の環境で観測した挙動

以下は上記環境での観測結果です。

- `||mydocomo.docomo.ne.jp^$document`：AdGuardのブロッキングページが表示され、メインドキュメントが遮断された。
- `@@||mydocomo.docomo.ne.jp^$all`：検証環境ではブロッキングページを回避できなかった。
- `@@||mydocomo.docomo.ne.jp^$document`：メインドキュメントへのアクセスは回復したが、検証時にはサイト側でエラーダイアログが発生することがあった。

最後のエラーダイアログについて、HTTPSフィルタリング、DNS保護、Extended CSS、Scriptletなど特定の機能を原因と断定できる公開情報は確認できませんでした。そのため原因推測は残さず、観測事実だけを記録しています。
