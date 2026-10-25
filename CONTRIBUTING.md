# Commit messageの運用

Commit messageとPull Requestのtitleおよびbodyは、変更対象と内容が分かる簡潔で自然な日本語を原則とします。
ChatGPT Chat / Work / Codexでの必須方針と確認手順は[AGENTS.md](AGENTS.md)に従ってください。
英語の技術用語・製品名・ファイル名・コード識別子は維持します。
正式名称や識別子だけで構成され、日本語化する一般説明がない場合を除き、変更内容は日本語で説明します。
`Update Markdown Notes Version`のような英語のみの定型メッセージは採用しません。
既存履歴を書き換えたり、Force Pushしたりして日本語化しません。

例：

- `Markdown Notes のリンク表記を修正`
- `AdGuard Custom Rules に非表示ルールを追加`
- `GitHub Actions のWorkflowを修正`
- `Linux Mint Guide の参考リンクを更新`
- `UserScript のVersion自動更新処理を修正`
- `Markdown Notes のVersionを更新`

## 編集経路ごとの入力方法

| 編集経路 | 作成前の対応 | 制約 |
| --- | --- | --- |
| GitHub Web UI | Commit changesのtitle欄を確認し、日本語で入力する | Repository内の指示やHookで既定の英語titleを自動翻訳できない |
| Git CLI | `git commit -m 'Markdown Notes のリンク表記を修正'`などで指定する | Hookはクローンごとの導入が必要で、回避も可能 |
| GitHub Desktop等 | CommitのSummary欄へ入力する | Hookの対応とPython実行環境はクライアントごとに確認する |
| GitHub API | 呼出側の`message`へ日本語titleを指定する | Repository側からAPI利用者の入力は変更できない |
| ChatGPT・Codex等 | AGENTS.mdを読み、変更内容に合う日本語titleを指定する | すべてのAIや編集ツールが指示ファイルを読む保証はない |
| PRのMerge | PR titleと、Merge確定画面のCommit titleを確認・編集する | Squashは最終titleを確認する。Rebaseは元のCommit titleを引き継ぐ |

通常のMergeでGitHubが生成する`Merge pull request ...`やRevertのtitleは、
既存の自動検査では日本語がないという理由だけで拒否しません。
これは英語の一般説明をそのまま採用してよいという意味ではなく、編集可能なtitleとbodyは日本語にします。
PR titleだけではMerge時の最終messageは保証されないため、確定前にtitleとbodyを確認します。
Squashでは最終bodyも、自分のBranchのCommitが残る方式では各Commit messageも確認します。
mainへの反映まで依頼された場合は、反映後の実際のCommit messageを取得して確認します。

## 検証と修正

既存の`.githooks/commit-msg`と品質検査Workflowで同じ
`scripts/check_commit_titles.py`を使用します。
ローカルでは`npm ci`後に`npm run hooks:install`で有効にできます。
独自Hookがある場合は先に統合してください。設定はクローンごとに必要です。

```sh
python scripts/check_commit_titles.py --message-file .git/COMMIT_EDITMSG
python scripts/check_commit_titles.py --base-ref origin/main --head-ref HEAD
```

検査は空title、固定名称の誤表記、`update`・`fix`・`修正`など対象のない定型titleを失敗にします。
既存の検査は日本語の有無だけでは判定せず、明確な英語titleも通過します。
bodyやPull Requestの文面はこの検査の対象外であり、検査成功だけでは言語方針への準拠を保証しません。
日本語が含まれていても適切とは限らず、意味の正確さと日本語の優先は人が確認します。
定型語以外の曖昧なtitleや不適切な英語をすべて自動検出する仕組みではありません。

PRではベースにないCommitを検査し、mainへのPushではbeforeからheadまでを検査します。
手動実行やゼロSHAの場合はheadのみを検査します。古い履歴全体を再判定しません。
検査失敗は`continue-on-error`や`|| true`で隠しません。他の品質検査も継続します。

失敗した場合、作成前なら入力欄・`-m`・APIの`message`を修正します。
共有済みCommitは書き換えず、PRをSquashする場合は管理者と検査条件を確認し、
最終titleを修正します。Squash予定でもPR内の不適切なCommitの検査は成功に変わりません。
mainに記録済みなら履歴を保持し、次回から改善します。

Actionsは翻訳・生成・Pushの事前阻止を行いません。
必須チェックとして保護されていない場合、失敗してもMergeは阻止できません。
また、`GITHUB_TOKEN`によるPushは通常、新たなPush Workflowを起動しません。
既存の自動更新Workflowの生成元でも適切なmessageを維持してください。

## Rulesetsと保護設定

2026年10月25日のAPI確認では、この公開RepositoryのRulesets一覧は0件でした。
連携ではRepositoryのadmin権限が表示されましたが、Branch protectionの読取は
`Resource not accessible by integration`（403）で、既存の必須チェックは未確認です。
契約プランとCommit metadata restrictionsの利用可否は確認できていません。
Rulesets・Branch protection・Merge方式の設定は変更していません。

日本語必須の正規表現は正当な英語titleやGitHub生成titleを誤拒否するため採用しません。
Commit metadata restrictionsは意味を理解した言語判定や自動翻訳ではありません。
導入を検討する場合は、SettingsのRulesetsで契約・管理権限・評価モードの利用可否を確認し、
mainを対象に、Web直接編集、各Merge方式、許容する英語を検証してから有効化してください。
利用可否が不明な状態で「導入済み」「評価済み」と扱いません。

仕様を確認する際の公式資料：

- [Rulesetsについて](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets)
- [Rulesetsで利用できるルール](https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/available-rules-for-rulesets)
- [Workflowからのイベント発火](https://docs.github.com/en/actions/how-tos/writing-workflows/choosing-when-your-workflow-runs/triggering-a-workflow)
