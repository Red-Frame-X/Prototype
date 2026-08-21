# ChromeOSを安全に手動更新する方法
ChromeOSの更新は、Googleが案内する設定画面から実行します。Croshの内部・診断用コマンドは、一般利用者向けの正式な更新手順としては案内されていません。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260804 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## 公式の実行手順

1. ChromebookをWi-Fiに接続します。
2. 画面右下の時刻を選択し、**設定**を開きます。
3. 左下の**ChromeOSについて**を選択します。
4. **アップデートを確認**を選択します。更新が見つかると自動的にダウンロードされます。
5. ダウンロード完了後、表示された場合は**再起動**を選択します。

`autest`は一般利用者向けの公式ヘルプに記載された更新方法ではないため、本書では推奨しません。更新できない場合は、端末の自動更新期限（AUE）、管理対象端末の更新ポリシー、空き容量、ネットワークを確認します。

## 参照

* [Chromebookを更新する（Chromebookヘルプ）](https://support.google.com/chromebook/answer/15468740?hl=ja)
* [Chromebookの更新スケジュールを確認する（Chromebookヘルプ）](https://support.google.com/chromebook/answer/9367166?hl=ja)
