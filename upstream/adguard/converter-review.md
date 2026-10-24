# AdGuard変換処理の互換性確認

このファイルは自動生成されます。以下は最新安定版のリリースノートから抽出した確認候補の原文であり、ルール構文の対応を証明するものではありません。

## AdGuard Browser Extension 5.5.3.3

- In this release we’ve added AdGuard’s Manifest V3 (MV3) Browser Extension to Microsoft Edge.
- But this doesn’t mean AdGuard is leaving the store. This is where our MV3 version comes in.
- ## What changes with MV3
- With MV2, the extension sees each network request in real time and decides what to block. This changes with MV3: the browser receives a prebuilt ruleset and applies it itself.
- This means the number of active rules is limited in MV3, some traditional filtering rules cannot be converted exactly, and most filter updates now ship with the extension itself, so updates can take longer.
- This will allow the MV3 extension to work as intended.
- * Added AdGuard MV3 Extension to Microsoft Edge
- - Updated [@adguard/dnr-converter] to v2.0.0.
- - Updated [@adguard/dnr-rulesets] to v6.0.0.
- ### How to install MV3 stable:
- ### How to install MV3 beta:
- * [Chrome](https://chromewebstore.google.com/detail/adguard-adblocker-mv3-bet/apjcbfpjihpedihablmalmbbhjpklbdf)

## AdGuard for Android 4.15.1

- 最新安定版のリリースノートに、変換処理に関係するキーワードはありませんでした。

## 変換処理を変更する前に必要な確認

1. AdGuardフィルタリングの公式文書、CoreLibs・Scriptletsのソース、または関連する上流の課題で動作を確認します。
2. 正常系・異常系・誤検出の回帰テストを追加します。
3. レビュー済みのプルリクエストで`config/adguard-converter-capabilities.json`を更新します。
4. 生成フィルターを再ビルドし、AGLintと単体テストを実行します。
