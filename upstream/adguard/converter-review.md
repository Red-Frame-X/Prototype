# AdGuard変換処理の互換性確認

このファイルは自動生成されます。以下は最新安定版のリリースノートから抽出した確認候補の原文であり、ルール構文の対応を証明するものではありません。

## AdGuard Browser Extension 5.5.4

- ### How to install MV3 stable:
- ### How to install MV3 beta:
- * [Chrome](https://chromewebstore.google.com/detail/adguard-adblocker-mv3-bet/apjcbfpjihpedihablmalmbbhjpklbdf)

## AdGuard for Android 4.16

- 最新安定版のリリースノートに、変換処理に関係するキーワードはありませんでした。

## 変換処理を変更する前に必要な確認

1. AdGuardフィルタリングの公式文書、CoreLibs・Scriptletsのソース、または関連するUpstreamのIssueで動作を確認します。
2. 正常系・異常系・誤検出の回帰テストを追加します。
3. Review済みのPull Requestで`config/adguard-converter-capabilities.json`を更新します。
4. 生成Filterを再Buildし、AGLintと単体テストを実行します。
