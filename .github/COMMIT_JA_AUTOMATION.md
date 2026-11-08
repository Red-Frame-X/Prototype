# PRのCommit日本語化と自動マージ

同じRepository内のPRで英語のCommit messageやPR説明を検出した場合に、OpenAI APIで日本語へ翻訳し、Codex Reviewと品質検査の成功後に日本語のCommit messageでSquash mergeするWorkflowです。

mainに記録済みのCommitは書き換えません。PR作成後からマージまでを自動化します。Branchへのpushだけで新しいPRを作成する機能はありません。既存の自動更新Workflowによるmainへの直接pushも変更しません。

## 初回設定

1. RepositoryのSettings → Secrets and variables → Actionsで、Secret `OPENAI_API_KEY`を登録します。APIキーをPRやCommentに貼らないでください。ChatGPTの契約とOpenAI APIの利用料金は別です。
2. Settings → Actions → Generalで、ActionsによるPRへの書き込みを許可します。Workflowは`contents: write`、`pull-requests: write`、`actions: write`、`checks: read`、`statuses: read`を使用します。RepositoryやOrganizationの上位ポリシーで禁止されている場合は、その設定も確認してください。
3. CodexのGitHub連携で、このRepositoryのCode Reviewを有効にします。`@codex review`への応答と利用枠が必要です。このWorkflow自体はCodexの接続・契約・利用枠を設定できません。
4. GitHubでSquash mergeを許可します。GitHubのAuto-merge機能の有効化は不要です。Workflowが条件を確認して、期待するSHAを指定したMerge APIを呼び出します。Branch保護・Rulesetは変更も回避もしません。

翻訳モデルの既定値は`gpt-4.1-mini`です。変更する場合はRepository Variable `COMMIT_TRANSLATION_MODEL`を設定します。Chat Completions APIのJSON modeと`temperature: 0`に対応するモデルを指定してください。

## 処理の流れ

1. 5分ごとの定期実行、品質検査完了、または手動実行で開いているPRを確認します。定期実行の開始時刻はGitHubの混雑で遅れることがあります。
2. 同じRepository内にあり、作成者が書き込み権限を持ち、mainを対象とする通常のPRを選びます。Fork、Draft、Bot作成のPR、main自体は対象外です。
3. PRの全Commit messageとPR title/bodyをOpenAI APIへ送り、英語の一般説明を日本語へ翻訳します。既に日本語の説明、正式な製品名・技術用語・識別子は保持します。APIにはファイルの内容・差分やSecretを送りません。
4. 翻訳対象のSHAと件数、titleの表記、URL・Issue参照・Code spanを照合します。Git objectだけを処理し、PR側のコード・Hook・Artifactを特権Jobで実行しません。
5. 全Commitのtree・著者・日時・親の順序を保持してBranchを更新します。`--force-with-lease`で同時更新を保護します。書き換えたCommitとその後続CommitのSHAは変わり、既存の署名は取り除かれます。翻訳前後とSHA対応はPRのBot Commentへ記録します。
6. 次の実行で最新SHAへの`@codex review`を依頼し、品質検査Workflowを`workflow_dispatch`で起動します。`GITHUB_TOKEN`によるBranch更新でも再検証を省略しません。通常のPR検証と同じ比較範囲で検査します。
7. 最新SHAのCodexの機械可読状態が完了・指摘なしであり、対象PR番号とSHAをrun-nameに含む専用の品質検査が成功し、他のCheck・Statusが成功していることを確認します。同じSHAでも通常の手動実行や別PRの検証結果では代用しません。未解決のReview thread、変更要求、競合、Draftへの変更、SHAやPR説明の変更がある場合はマージしません。
8. 日本語のPR title/bodyを最終Commit messageに指定してSquash mergeします。マージ後の実際のCommit messageを照合し、Version自動同期とmainの品質検査を明示的に起動します。mainの検証にはマージ直前のSHAを渡し、通常のpushと同じ比較範囲とVersion検証条件を適用します。

日本語化が不要なPRを新たに自動マージの対象には加えません。日本語化済みのPRに追加Commitが入った場合は、最新状態から翻訳と検証をやり直します。

## 停止する場合

Repository Variable `COMMIT_JA_AUTOMATION_ENABLED`を`false`にすると、翻訳・レビュー依頼・マージを停止します。再開するには`false`以外に変更します。

特定のPRだけを確認する場合は、Actionsの「PRのCommit日本語化とレビュー後の自動マージ」を手動実行し、`pr_number`にPR番号を指定します。空欄なら開いているPRを確認します。

## 待機・失敗時の扱い

- APIキー未設定、API利用枠切れ、翻訳結果の欠落・不正、取得失敗、同時pushの検出はエラーにします。他のPRの確認は継続します。
- 翻訳の対象は1～100 Commit、入力JSONは120,000 bytesまでです。翻訳前後のレビュー記録がCommentの上限に収まらない場合も、省略せず停止します。
- 品質検査やCodex Reviewが未完了の場合は、次回実行で再確認します。CI失敗やCodexの指摘を無視してマージしません。
- Codexの指摘に対して、ファイル内容を自動修正する機能はありません。修正Commitが入ると、新しいSHAで翻訳・レビュー・品質検査をやり直します。
- Codexへの依頼はSHAごとに1回です。利用枠不足や連携の問題を直してもレビューが再開しない場合は、PRで`@codex review`を再依頼してください。Commentの形式が将来変わった場合は、成功扱いにせず待機します。
- 品質検査Workflow自体を変更するPRは、自動マージしません。通常のレビューとマージで確認します。このWorkflowの導入前から開いていたPRも、最新mainの品質検査Workflowを取り込む必要があります。
- 初回設定後の実際のAPI翻訳・Codex Review・CI・マージが完了するまでは、全自動経路の稼働確認は完了していません。Secretの登録や外部サービスの有効化を、Workflowを追加しただけで完了したと判断しないでください。

## 一次資料

- [OpenAI Chat Completions API](https://platform.openai.com/docs/api-reference/chat/create)
- [Codex Code Review](https://developers.openai.com/codex/cloud/code-review)
- [GitHub Actionsによるイベント起動の制限](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [GitHub Pull Request Merge API](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)
