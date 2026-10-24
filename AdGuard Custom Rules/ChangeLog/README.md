# AdGuardの変更履歴

このディレクトリには、AdGuardの更新内容を確認するための変更履歴ミラーを保存しています。

変更履歴では、バージョンごとの新機能、変更点、修正内容、フィルタリングエンジンや関連コンポーネントの更新などを確認できます。ここに保存されているファイルは、AdGuard公式の一次情報を参照しやすくするために自動取得・生成されています。

## 変更履歴一覧

| 変更履歴 | 対象 | 説明 |
| --- | --- | --- |
| [`adguard-browser-extension-CHANGELOG.source.md`](adguard-browser-extension-CHANGELOG.source.md) | AdGuard Browser Extension | AdGuard Browser Extension公式Repositoryの`CHANGELOG.md`をミラーしたファイルです。バージョンごとの変更点・修正内容・関連コンポーネント更新などを確認できます。 |
| [`adguard-for-android-CHANGELOG.source.md`](adguard-for-android-CHANGELOG.source.md) | AdGuard for Android | AdGuard for Android公式GitHub Releasesから生成した変更履歴ミラーです。リリースごとの公開日時、公式リリースへのリンク、新機能・改善・修正内容などを確認できます。 |

## 更新について

変更履歴は [`scripts/update_adguard_changelogs.py`](../../scripts/update_adguard_changelogs.py) で取得・生成し、GitHub Actionsの [`AdGuard変更履歴の更新`](../../.github/workflows/update-adguard-changelogs.yml) で更新しています。

現在のWorkflowでは、主に次のタイミングで更新処理が実行されます。

- 毎日 04:07 JST（GitHub Actionsのcronでは `7 19 * * *`）
- 関連する更新スクリプト、テスト、依存関係、Workflow自体が `main` にpushされた場合
- GitHub Actionsから手動実行した場合

更新処理では、公式情報を取得したあとにテストを実行し、対象ファイルに実際の変更がある場合だけCommit・pushします。

取得・生成対象は次のとおりです。

- AdGuard Browser Extension：公式Repositoryの`CHANGELOG.md`
- AdGuard for Android：公式GitHub Releases
- 付随するMetadataと互換性レビュー候補：`upstream/adguard/`

> [!NOTE]
> ここに保存する変更履歴は、人が更新内容を確認するための資料です。フィルタ構文や機能対応を保証する実行可能な仕様そのものではありません。新しい構文や挙動を判断する場合は、AdGuard公式ドキュメント、公開ソースコード、関連する課題なども確認してください。

## 関連情報

- [AdGuard Custom Rulesの案内](../README.md)
- [RepositoryのルートREADME](../../README.md)
- [更新スクリプト](../../scripts/update_adguard_changelogs.py)
- [AdGuard変更履歴の更新Workflow](../../.github/workflows/update-adguard-changelogs.yml)

## 公式情報

- [AdGuardブラウザー拡張機能の変更履歴](https://github.com/AdguardTeam/AdguardBrowserExtension/blob/master/CHANGELOG.md)
- [AdGuardブラウザー拡張機能のリリース](https://github.com/AdguardTeam/AdguardBrowserExtension/releases)
- [AdGuard for Androidのリリース](https://github.com/AdguardTeam/AdguardForAndroid/releases)
- [AdGuardフィルタリングルール構文](https://adguard.com/kb/ja/general/ad-filtering/create-own-filters/)
- [AdGuard ブラウザ拡張機能](https://adguard.com/kb/ja/adguard-browser-extension/)
- [AdGuard for Android](https://adguard.com/kb/ja/adguard-for-android/)
