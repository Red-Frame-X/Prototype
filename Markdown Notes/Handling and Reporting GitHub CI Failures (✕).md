# Handling and Reporting GitHub CI Failures (✕)

GitHubのステータスチェック失敗を確認・報告するためのメモです。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260825 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

## ステータスチェックと署名検証

GitHubでは、Pull RequestやコミットにChecks APIまたはCommit Status APIから状態が報告されます。Checks APIには `failure`、`timed_out`、`cancelled`、`action_required` などの結論があり、Commit Status APIには `error` と `failure` があります。

`Verified` / `Unverified` はコミット署名の検証状態であり、CIのステータスチェックとは別の仕組みです。署名を必須とするリポジトリルールによってマージ可否に影響する場合はありますが、`Unverified` 自体をCI失敗とみなすのは不正確です。

## 失敗時の確認手順

1. 対象コミットまたはPull Requestで失敗したチェックを開きます。
2. GitHub Actionsの場合は該当Workflow runとJobのログを確認します。
3. 最初に失敗したStep、終了コード、エラーメッセージを確認します。
4. コード・テスト・依存関係・Workflow設定・権限・Secretなど、ログが示す原因を切り分けます。
5. 修正後に新しいコミットまたは再実行で検証します。

CI失敗の原因を「コードの不具合」と「Workflowの構成不備」の2種類だけに限定することはできません。外部サービス障害、runner環境、依存関係、権限、Secretなども原因になり得るため、以前の版にあった二分類は統合しました。

## Issues / Pull Requestsで報告する場合

最低限、次の情報を添えると原因を追いやすくなります。

- 対象コミットSHAまたはPR番号
- 失敗したWorkflow / Job / Step名
- Workflow runへのリンク
- エラーログの該当部分
- 再現条件または再実行結果
- 原因を推測する場合は、確認済みの事実と分けて記載

自分のPull Requestで発生した失敗は、まずそのPull Requestの文脈で共有します。既存のmainブランチや共通Workflow自体の問題と確認できた場合は、リポジトリのCONTRIBUTINGやIssuesテンプレートに従って報告します。

## 公式ドキュメント

- [About status checks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
- [REST API endpoints for commit statuses](https://docs.github.com/rest/commits/statuses)
- [REST API endpoints for check runs](https://docs.github.com/rest/checks/runs)
- [About commit signature verification](https://docs.github.com/authentication/managing-commit-signature-verification/about-commit-signature-verification)
