# uB-filter-by-kdroidwin (AdGuard Optimized)

[uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin) を、主に **AdGuard for Chrome MV3** で利用できるように自動変換・最適化した非公式フィルタです。詐欺サイトや悪質なアフィリエイトサイトなどへのアクセスをブロックします。

> [!IMPORTANT]
> このフィルタは上流プロジェクトの公式配布物ではありません。誤ブロックやサイトの表示・動作不良が起きる可能性があります。

## 購読URL

AdGuard のカスタムフィルタ追加画面に、次のURLを登録してください。

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt
```

## 導入方法

### AdGuard for Chrome MV3

1. AdGuard の設定を開きます。
2. **フィルタ** → **カスタムフィルタ** を開きます。
3. **カスタムフィルタを追加** を選択し、上記の購読URLを入力します。
4. 追加したフィルタが有効になっていることを確認します。

### AdGuard for Android

1. AdGuard を開き、**保護** → **広告ブロック** → **フィルタ** を開きます。
2. **カスタムフィルタ** から新しいフィルタを追加します。
3. 上記の購読URLを入力し、追加したフィルタを有効にします。

Android 版でも読み込めますが、AdGuard for Chrome MV3 を優先して変換しているため、CoreLibs 固有機能の保持や Android 向けの完全な最適化は保証されません。

## 更新について

GitHub Actions が上流フィルタを定期的に確認し、変換結果に変更がある場合のみこのファイルを自動更新します。生成物のメタデータでは更新間隔を **12時間** としています。

AdGuard 側で更新がすぐに反映されない場合は、カスタムフィルタの更新を手動で実行してください。

## 変換方針と注意点

- AdGuard for Chrome MV3 と互換性のない一部のルールは、変換時に削除またはコメントアウトされます。
- uBlock Origin と AdGuard の構文・対応機能の違いにより、上流版とブロック結果が完全には一致しません。
- 誤ブロックが発生した場合は、まずこのカスタムフィルタを一時的に無効化して原因を切り分けてください。
- 変換処理の詳細は [`scripts/convert.py`](../scripts/convert.py) を参照してください。

## 原典・ライセンス

- 原典：[Kdroidwin/uB-filter-by-kdroidwin](https://github.com/Kdroidwin/uB-filter-by-kdroidwin)
- 変換版：[uB-filter-by-kdroidwin (AdGuard Optimized).txt](./uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt)
- ライセンス：[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)

この変換版は無保証で提供されます。
