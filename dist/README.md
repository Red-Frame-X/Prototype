# uB-filter-by-kdroidwin (AdGuard Optimized)

[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)を、主に**AdGuard ブラウザ拡張機能 MV3対応版**で利用するために自動変換・最適化した非公式フィルタです。上流フィルタの目的を維持しつつ、uBlock OriginとAdGuardの構文・機能差を考慮して変換します。

> [!IMPORTANT]
> このフィルタは上流プロジェクトおよびAdGuardの公式配布物ではありません。上流版とブロック結果が完全に一致することは保証されず、誤ブロックやサイトの表示・動作不良が起きる可能性があります。

## 購読URL

AdGuardの「カスタムフィルタ」に次のURLを登録してください。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt
```

## 導入方法

### AdGuard ブラウザ拡張機能 MV3対応版

1. AdGuardの設定から「フィルタ」を開きます。
2. 「カスタムフィルタ」から「カスタムフィルタを追加する」を選択します。
3. 上記の購読URLを入力し、追加したフィルタを有効にします。
4. ChromeからUser Scripts APIの許可を求められた場合は、AdGuardの案内に従って必要な権限を有効にします。

AdGuard ブラウザ拡張機能 v5.2以降では、MV3でカスタムフィルタを利用するためにUser Scripts APIが使用されています。詳細はAdGuard公式の[User Scripts API](https://adguard.com/kb/ja/adguard-browser-extension/user-scripts-api/)を参照してください。

### AdGuard for Android

1. AdGuardの「広告ブロック」設定で「フィルタ」を開きます。
2. 「カスタムフィルタ」からカスタムフィルタを追加します。
3. 上記の購読URLを入力し、追加したフィルタを有効にします。

Android版でも購読できますが、この生成物はAdGuard ブラウザ拡張機能 MV3対応版との互換性を主眼に変換しています。CoreLibs固有機能の保持やAndroid向けの完全な最適化は保証しません。

## 更新について

GitHub Actionsが上流フィルタを定期的に確認し、変換結果に変更がある場合のみ生成物を更新します。生成物のメタデータでは更新間隔を**12時間**としています。

AdGuard ブラウザ拡張機能では、v5.4.1系でMV3のカスタムフィルタを拡張機能本体とは独立して更新する機能が追加されています。実際の取得時刻は通信状況、配布元の応答、AdGuard側の更新処理などにより前後します。

## 変換方針と注意点

- AdGuard ブラウザ拡張機能 MV3対応版で安全に対応付けられない一部のルールは、変換時に削除またはコメントアウトします。
- uBlock OriginとAdGuardの構文・対応機能は同一ではないため、上流版とブロック結果が完全には一致しません。
- 変換できることと、元ルールの意味を完全に維持できることは同義ではありません。意味を安全に維持できない場合は保守的に除外します。
- 誤ブロックが発生した場合は、まずこのカスタムフィルタを一時的に無効化して原因を切り分けてください。
- 変換処理の詳細は[`scripts/convert.py`](../scripts/convert.py)を参照してください。

## 参考資料

- [AdGuard ブラウザ拡張機能](https://adguard.com/kb/ja/adguard-browser-extension/)
- [AdGuard ブラウザ拡張機能 MV3対応版](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuardフィルタリングルール構文](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard Browser Extension Releases](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)

## 原典・ライセンス

- 原典：[Kdroidwin/uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)
- 変換版：[uB-filter-by-kdroidwin (AdGuard Optimized).txt](./uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt)
- ライセンス：[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

第三者由来ファイルのライセンスとこのリポジトリ内の独自部分の扱いは、[`LICENSES.md`](../LICENSES.md)も参照してください。この変換版は無保証で提供されます。
