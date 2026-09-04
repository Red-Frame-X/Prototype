# GitHub CI Failure 確認メモ

GitHubのステータスチェックが失敗したときに、自分が原因を切り分けて記録するための個人用メモです。

> [!NOTE]
> この文書は自分のリポジトリ運用時の備忘録であり、一般向けのCI運用ガイドやサポート手順を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。GitHubの仕様は変更される可能性があるため、実際の操作時は公式ドキュメントと対象Workflowのログを再確認します。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

## ステータスチェックと署名検証の整理

GitHubでは、Pull RequestやコミットにChecks APIまたはCommit Status APIから状態が報告されます。Checks APIには `failure`、`timed_out`、`cancelled`、`action_required` などの結論があり、Commit Status APIには `error` と `failure` があります。

`Verified` / `Unverified` はコミット署名の検証状態であり、CIのステータスチェックとは別の仕組みです。署名を必須とするリポジトリルールによってマージ可否に影響する場合はありますが、`Unverified` 自体をCI失敗とみなすのは不正確です。

## 自分が失敗時に確認する順序

1. 対象コミットまたはPull Requestで失敗したチェックを開く。
2. GitHub Actionsの場合は該当Workflow runとJobのログを確認する。
3. 最初に失敗したStep、終了コード、エラーメッセージを確認する。
4. コード・テスト・依存関係・Workflow設定・権限・Secretなど、ログが示す原因を切り分ける。
5. 修正後に新しいコミットまたは再実行で検証する。

CI失敗の原因を「コードの不具合」と「Workflowの構成不備」の2種類だけに限定しません。外部サービス障害、runner環境、依存関係、権限、Secretなども原因になり得るため、ログと再現結果を優先して記録します。

## 自分がIssues / Pull Requestsへ記録するとき

原因を後から追えるよう、最低限次の情報を残します。

- 対象コミットSHAまたはPR番号
- 失敗したWorkflow / Job / Step名
- Workflow runへのリンク
- エラーログの該当部分
- 再現条件または再実行結果
- 原因を推測する場合は、確認済みの事実と分けて記載

自分のPull Requestで発生した失敗は、まずそのPull Requestの文脈で記録します。既存のmainブランチや共通Workflow自体の問題と確認できた場合は、そのリポジトリのCONTRIBUTINGやIssuesテンプレートも確認します。

## 参照するGitHub公式ドキュメント

- [About status checks](https://docs.github.com/pull-requests/collaborating-with-pull-requests/collaborating-on-repositories-with-code-quality-features/about-status-checks)
- [REST API endpoints for commit statuses](https://docs.github.com/rest/commits/statuses)
- [REST API endpoints for check runs](https://docs.github.com/rest/checks/runs)
- [About commit signature verification](https://docs.github.com/authentication/managing-commit-signature-verification/about-commit-signature-verification)
