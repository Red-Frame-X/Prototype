# uB-filter-by-kdroidwin (AdGuard Optimized)

[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)を、自分のAdGuard環境で検証するために自動変換・最適化している非公式生成フィルタです。上流フィルタの目的をできるだけ維持しつつ、uBlock OriginとAdGuardの構文・機能差を考慮して変換しています。

> [!IMPORTANT]
> このディレクトリは個人の学習・検証・設定バックアップ用です。一般向けの配布、導入ガイド、推奨構成を目的としていません。説明の下書きはChatGPTで推敲・整理する場合があるため、専門性・正確性・完全性を保証しません。
>
> この生成物は上流プロジェクトおよびAdGuardの公式配布物ではありません。上流版とブロック結果が完全に一致することは保証されず、誤ブロックやサイトの表示・動作不良が起きる可能性があります。

## 自分の環境での登録先メモ

自分の検証環境では、必要な場合にAdGuardのカスタムフィルタとして次のRaw URLを登録しています。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt
```

### AdGuard ブラウザ拡張機能 MV3対応版

自分の再設定時は、次の順序で上記URLを登録します。

**AdGuard アイコン → ⚙ → フィルタ → カスタムフィルタ → カスタムフィルタを追加する**

登録後は、必要な権限やUser Scripts APIの状態を、使用中バージョンのUIと公式資料で確認します。

AdGuard ブラウザ拡張機能 v5.2以降では、MV3でカスタムフィルタを扱うためにUser Scripts APIが使用されています。仕様確認用としてAdGuard公式の[User Scripts API](https://adguard.com/kb/ja/adguard-browser-extension/user-scripts-api/)を参照します。

### AdGuard for Android

Android側で試す場合は、次の順序で上記URLを登録します。

**ボトムバーの ⚙ → フィルタリング → フィルタ → カスタムフィルタ → ＋ カスタムフィルタを追加する**

ただし、この生成物は主にAdGuard ブラウザ拡張機能 MV3対応版との互換性を確認する目的で変換しており、CoreLibs固有機能の保持やAndroid向けの完全な最適化は前提としていません。

## 更新記録

GitHub Actionsで上流フィルタを定期的に確認し、変換結果に変更がある場合だけ生成物を更新します。生成物のメタデータでは更新間隔を12時間としています。

AdGuard ブラウザ拡張機能では、v5.4.1系でMV3のカスタムフィルタを拡張機能本体とは独立して更新する機能が追加されています。実際の取得時刻は通信状況、配布元の応答、AdGuard側の更新処理などにより前後するため、保存している説明だけで更新状態を判断しません。

## 変換方針と検証メモ

- AdGuard ブラウザ拡張機能 MV3対応版で安全に対応付けられない一部のルールは、変換時に削除またはコメントアウトします。
- uBlock OriginとAdGuardの構文・対応機能は同一ではないため、上流版とブロック結果が完全には一致しません。
- 変換できることと、元ルールの意味を完全に維持できることは同義ではありません。意味を安全に維持できない場合は保守的に除外します。
- 誤ブロックを疑う場合は、この生成フィルタを一時的に無効化して自分の環境で原因を切り分けます。
- 正規表現の構文検査対策として`$document`を自動追加しません。AGLint 3.0.2が正規表現内の終端アンカーを修飾子と誤認する場合だけ、該当行の`invalid-modifiers`診断をコメントで抑制します。その他の検査は維持します。
- 変換処理の詳細は[`scripts/convert.py`](../scripts/convert.py)に残しています。

## 参照している公式資料

- [AdGuard ブラウザ拡張機能](https://adguard.com/kb/ja/adguard-browser-extension/)
- [AdGuard ブラウザ拡張機能 MV3対応版](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuardフィルタリングルール構文](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard Browser Extension Releases](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)

## 原典・ライセンス

- 原典：[Kdroidwin/uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)
- 変換版：[uB-filter-by-kdroidwin (AdGuard Optimized).txt](./uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt)
- ライセンス：[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

第三者由来ファイルのライセンスと、このリポジトリ内の独自部分の扱いは[`LICENSES.md`](../LICENSES.md)に記録しています。
