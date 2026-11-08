# PRのCommit日本語化と自動マージ

同じRepository内のPRで英語のCommit messageやPR説明を検出した場合に、Argos Translateで日本語へ翻訳し、翻訳内容の確認・Codex Review・品質検査の成功後に日本語のCommit messageでSquash mergeするWorkflowです。

mainに記録済みのCommitは書き換えません。PR作成後からマージまでを自動化します。Branchへのpushだけで新しいPRを作成する機能はありません。既存の自動更新Workflowによるmainへの直接pushも変更しません。

## 初回設定

1. WorkflowはCPU版`torch==2.9.1+cpu`と`requirements-translation.txt`のArgos TranslateをRunnerへ導入します。外部の有料翻訳APIは不要です。既存のSecret `OPENAI_API_KEY`は削除しません。
2. Settings → Actions → Generalで、ActionsによるPRへの書き込みを許可します。Workflowは`contents: write`、`pull-requests: write`、`actions: write`、`checks: read`、`statuses: read`を使用します。RepositoryやOrganizationの上位ポリシーで禁止されている場合は、その設定も確認してください。
3. CodexのGitHub連携で、このRepositoryのCode Reviewを有効にします。`@codex review`への応答と利用枠が必要です。このWorkflow自体はCodexの接続・契約・利用枠を設定できません。
4. GitHubでSquash mergeを許可します。GitHubのAuto-merge機能の有効化は不要です。Workflowが条件を確認して、期待するSHAを指定したMerge APIを呼び出します。Branch保護・Rulesetは変更も回避もしません。

翻訳ライブラリは`argostranslate==1.11.0`、モデルは公式Indexの英語（`en`）→日本語（`ja`）Version `1.1`です。モデルの要求Argos Versionは`1.1`です。`COMMIT_TRANSLATION_MODEL`は使用しません。公式配布URLから取得し、固定SHA256と言語・Versionを照合してからインストールします。中間言語への自動切替は行いません。

**移行の未確認事項：現在は有効化できません。** モデル配布先への通信が作業環境で拒否されたため、実物・SHA256・実翻訳の動作は未確認です。`.github/argos-model.json`の`sha256`は`null`、`license_verified`は`false`とし、取得前に安全停止します。これらを推測で埋めないでください。GitHub-hosted runnerと同じPython 3.12環境で、モデル取得・実翻訳・保存表記を確認する必要があります。

ライブラリとIndexの公式説明はMIT / CC0です。モデルについては開発者が同じライセンスと説明した[公式Issue #76](https://github.com/argosopentech/argos-translate/issues/76)がある一方、英日モデル個別のライセンス表記不足は[未解決Issue #507](https://github.com/argosopentech/argos-translate/issues/507)に掲載されています。ライブラリのライセンスだけでモデル個別の確認が済んだとは扱いません。実物のREADME・学習データの出典と公式回答の適用範囲を確認してから、根拠とSHA256を固定してください。

## 処理の流れ

1. 5分ごとの定期実行、品質検査完了、または手動実行で開いているPRを確認します。定期実行の開始時刻はGitHubの混雑で遅れることがあります。
2. 同じRepository内にあり、作成者が書き込み権限を持ち、mainを対象とする通常のPRを選びます。Fork、Draft、Bot作成のPR、main自体は対象外です。
3. PRの全Commit messageとPR title/bodyの英語の一般説明をRunner内のArgos Translateで日本語へ翻訳します。日本語・登録済みの正式な製品名・技術用語・識別子・Version・URL・Issue参照・コードは翻訳器に渡さず保持します。同一区間の日英混在を安全に分離できない場合は停止し、手動での日本語化が必要です。任意の未知の製品名の識別や意味の正確性は保証できないため、適用後の翻訳前後の記録を必ず確認します。本文・差分・Secretを外部の翻訳APIへ送りません。
4. 翻訳対象のSHAと件数、titleの表記、URL・Issue参照・Code spanを照合します。Git objectだけを処理し、PR側のコード・Hook・Artifactを特権Jobで実行しません。
5. 全Commitのtree・著者・日時・親の順序を保持してBranchを更新します。`--force-with-lease`で同時更新を保護します。書き換えたCommitとその後続CommitのSHAは変わり、既存の署名は取り除かれます。翻訳前後とSHA対応はPRのBot Commentへ記録します。
6. 次の実行で最新SHAへの`@codex review`を依頼し、品質検査Workflowを`workflow_dispatch`で起動します。`GITHUB_TOKEN`によるBranch更新でも再検証を省略しません。通常のPR検証と同じ比較範囲で検査します。
7. 最新SHAのCodexの機械可読状態が完了・指摘なしであり、対象PR番号とSHAをrun-nameに含む専用の品質検査が成功し、他のCheck・Statusが成功していることを確認します。同じSHAでも通常の手動実行や別PRの検証結果では代用しません。未解決のReview thread、変更要求、競合、Draftへの変更、SHAやPR説明の変更がある場合はマージしません。
8. 書き込み権限を持つ人が翻訳前後の全文章・情報・意味・正式表記を確認し、Botが提示する`/approve-commit-translation <fingerprint>`だけを単独のCommentに記述します。fingerprintは最新SHA・PR title/bodyに結び付き、更新後の古い承認やBotの承認は認めません。この確認がなければ自動マージしません。既存のCodex Review・CI条件もすべて必要です。
9. 日本語のPR title/bodyを最終Commit messageに指定してSquash mergeします。マージ後の実際のCommit messageを照合し、Version自動同期とmainの品質検査を明示的に起動します。mainの検証にはマージ直前のSHAを渡し、通常のpushと同じ比較範囲とVersion検証条件を適用します。

日本語化が不要なPRを新たに自動マージの対象には加えません。日本語化済みのPRに追加Commitが入った場合は、最新状態から翻訳と検証をやり直します。

## 停止する場合

Repository Variable `COMMIT_JA_AUTOMATION_ENABLED`を`false`にすると、翻訳・レビュー依頼・マージを停止します。再開するには`false`以外に変更します。

特定のPRだけを確認する場合は、Actionsの「PRのCommit日本語化とレビュー後の自動マージ」を手動実行し、`pr_number`にPR番号を指定します。空欄なら開いているPRを確認します。`dry_run`は手動実行では既定で`true`です。このモードでは翻訳前後をJSONでログに表示し、push・PR更新・Comment投稿・Review依頼・CI起動・マージを行いません。モデル未確認時はテストモードも失敗します。定期実行にはこの入力は適用されず、既存の実行経路を維持します。

## 待機・失敗時の扱い

- モデル未確認、モデルの取得・hash・Metadata検証失敗、翻訳処理失敗、翻訳結果の欠落・不正、取得失敗、同時pushの検出はエラーにします。他のPRの確認は継続します。
- 翻訳の対象は1～100 Commit、入力JSONは120,000 bytesまでです。翻訳前後のレビュー記録がCommentの上限に収まらない場合も、省略せず停止します。
- 品質検査やCodex Reviewが未完了の場合は、次回実行で再確認します。CI失敗やCodexの指摘を無視してマージしません。
- Codexの指摘に対して、ファイル内容を自動修正する機能はありません。修正Commitが入ると、新しいSHAで翻訳・レビュー・品質検査をやり直します。
- Codexへの依頼はSHAごとに1回です。利用枠不足や連携の問題を直してもレビューが再開しない場合は、PRで`@codex review`を再依頼してください。Commentの形式が将来変わった場合は、成功扱いにせず待機します。
- 品質検査Workflow自体を変更するPRは、自動マージしません。通常のレビューとマージで確認します。このWorkflowの導入前から開いていたPRも、最新mainの品質検査Workflowを取り込む必要があります。
- 初回設定後の実際のArgos翻訳・Codex Review・CI・マージが完了するまでは、全自動経路の稼働確認は完了していません。Secretの登録や外部サービスの有効化を、Workflowを追加しただけで完了したと判断しないでください。

## 一次資料

- [Argos Translateの導入とPython API](https://github.com/argosopentech/argos-translate)
- [公式Indexの固定Revision](https://github.com/argosopentech/argospm-index/blob/ff90de60728f7c1338ff6b75974e4c89b2442d22/index.json)
- [Argos Translate 1.11.0](https://pypi.org/project/argostranslate/1.11.0/)
- [Codex Code Review](https://developers.openai.com/codex/cloud/code-review)
- [GitHub Actionsによるイベント起動の制限](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [GitHub Pull Request Merge API](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)

## OPENAI_API_KEYの依存関係

移行前の最新mainでは、実行時参照は`japanese-commits.yml`と`automate_japanese_commits.py`だけでした。Repository内の他のWorkflowに参照はありません。説明文はこの文書と`CONTRIBUTING.md`にありました。今回、翻訳処理への注入と参照を取り除きましたが、GitHub Secretsの値・登録状態は変更していません。Repository外のWorkflow、Organizationの共有Secret、動的な参照の依存関係はこの調査では確認できません。
