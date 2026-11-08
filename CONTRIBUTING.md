# Commit messageの運用

Commit messageとPull Requestのtitleおよびbodyは、変更対象と内容が分かる簡潔で自然な日本語を必須とします。
ChatGPT Chat / Work / Codexでの必須方針と確認手順は [AGENTS.md](AGENTS.md) に従ってください。
英語の技術用語・製品名・ファイル名・コード識別子は維持します。
MV3対応のAdGuardブラウザ拡張機能は、本文・見出し・リンクの表示名を`AdGuard Browser Extension MV3`に統一します。公式原文の引用、URL、互換性に関わる識別子は保持します。
Chat / Work / Codexを経由した編集のCommit titleとbodyは、必ず日本語で変更内容を説明します。英語のみのCommit titleは許可しません。
例：`Markdown Notes のVersionを更新`、`uB-filter-by-kdroidwin (AdGuard Optimized) を更新`、`AGLint の設定を修正`。
ツールが英語を生成しやすいことだけを理由に、英語の定型メッセージを採用しません。
既存履歴の書き換えやForce Pushによる日本語化は、ユーザーが明示的に許可した範囲に限ります。

英語のCommit messageを含むPRについては、[PRのCommit日本語化と自動マージ](.github/COMMIT_JA_AUTOMATION.md)で、PR内の日本語化・Codex Review・品質検査・Squash mergeを自動化できます。この自動化によるPR内のCommit書き換えは承認済みの対象範囲です。mainに記録済みの履歴は書き換えません。Argosモデルの取得・整合性・ライセンスの確認とCodexのGitHub連携が必要です。固定モデルの確認根拠と翻訳承認・テストモードはリンク先を参照してください。既存の`OPENAI_API_KEY`は削除しません。

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
| ChatGPT・Codex等 | AGENTS.md を読み、変更内容に合う日本語titleを指定する | すべてのAIや編集ツールが指示ファイルを読む保証はない |
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

## Haiagaruガイド編集時の事前検査

`Markdown Notes/ChromeOS & Android Optimization Guide.md`のHaiagaru説明を編集する場合は、Commit前に次を実行してください。Pythonの標準ライブラリだけで動作し、`npm ci`は不要です。

```sh
npm run check:haiagaru
```

- 対応APK一覧、固定検証環境、準備手順、報告テンプレートのVersion・versionCodeを照合します。
- Versionごとの解説を整理する場合も、検証環境との照合に必要な対応APK一覧は保持してください。対応状況を変更する際は公式情報を確認し、関連する記載をそろえます。
- 見出しや一覧の書式を変更した場合は、欠落・不一致を検出するTestを保持したまま対応書式を更新してください。検査の無効化や削除で通過させないでください。
- 「導入・更新方法」以降を保持する依頼では、変更前後の該当範囲が完全一致することも確認します。この整合性検査だけで、本文全体の保持や技術的な正確さを保証するものではありません。

CIでも依存パッケージ導入前に同じ整合性検査を実行します。全Python Test・Markdownlint・内容消失防止検査も引き続き実行します。

## Rulesetsと保護設定

### 現在の連携で行うマージ前の確認

現在のGitHub連携は管理権限を取得しないため、Branch protection詳細API
`GET /repos/{owner}/{repo}/branches/{branch}/protection` の取得を通常運用の必須項目から外します。
この403を解消するための追加権限やPATの導入は、通常のWorkflow検証・マージの完了条件にしません。
以下の手順は日常のマージ判断を代替するもので、保護設定の詳細取得や変更と同等の機能ではありません。

1. 通常のBranch API `GET /repos/{owner}/{repo}/branches/{branch}` で対象Branchの
   `protected` を確認します。取得失敗・項目欠落・判定不能を `false` とみなさず、判定できるまでマージを保留します。
   Rulesets一覧を取得できた場合も併せて確認しますが、一覧が空という理由だけで保護なしと判断しません。
2. `protected=true` で必要な条件を確認できない場合は、GitHubのSettingsやPR画面で確認します。
   確認できるまではマージを保留します。保護設定を変える作業は、権限と設定内容を別途確認します。
3. 保護の有無にかかわらず、最新のPR先端SHAに対するCI・Lint・Test、Codex Review、未解決の指摘、
   必要な承認、Draft状態、競合、変更差分を確認します。既存の自動マージで必要な翻訳の承認も維持します。
   `mergeable=true` や `mergeable_state=clean` だけでは、すべての条件を満たしたと判断しません。
4. 確認した先端SHAを指定して通常のMerge APIを使用します。管理者による回避・強制マージは行いません。
   SHAの変更、保護条件による拒否、権限不足等で受け付けられない場合は停止し、保護設定を弱めて再試行しません。
5. マージ後のCommit、差分、mainのCIと関連Workflowを確認します。

2026年11月8日の確認では、通常のBranch APIは `main.protected=false`、Rulesets一覧は0件でした。
これは確認時点の状態であり、将来も保護なしであることを保証しません。既存の自動マージScriptは
Branch protection詳細APIに依存していないため、検査や停止条件を削除する実装修正は不要です。
ここでのBranch情報とSettingsの確認は作業者が行う運用手順であり、Scriptに新しい自動検査を追加したものではありません。
下記の過去の403・保護設定に関する記録は履歴として保持します。

公式仕様：[Branch情報の取得](https://docs.github.com/en/rest/branches/branches#get-a-branch)、
[Pull Requestのマージ](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)。

### 内容消失の再発防止と必須チェック

2026年11月2日の再確認では、Rulesets一覧は0件、Branch protectionの読取は
`Resource not accessible by integration`（403）でした。現在の連携には保護設定の
変更用ツールがなく、設定の強制化は未実施です。CIの成功だけで、失敗したPRの
マージやmainへの直接Pushまで禁止できているとは判断しないでください。

- 内容消失防止検査は、PRでは共通祖先から、mainへのPushではイベントの
  `before`からHEADまでを比較します。比較元が取得できないPushは失敗にし、
  最後のCommitだけの比較へ縮小しません。Force Pushでも実際のPush前後を比較します。
- 保護対象の`.md`・`.txt`・`.js`・`.json`では、従来の純減120行以上に加え、
  純減20行以上かつ元の行数の25%以上の減少もレビュー対象です。
  承認済みの削除だけ、既存の`--allow-deletion-in`で正確なパスを指定します。
  保持行数が元の25%未満になる変更は、この承認でも許可しません。
- 出力の省略表示は、本文中・引用行・箇条書きでも検出します。
  Code span内の引用例は保持します。省略表示のない欠落、未知の省略形式、
  閾値未満の削除や同じ行数の不正な置換は、差分の意味も確認してください。
  この検査は`scripts/`・`tests/`・`.github/`を保護対象から除外しています。

管理権限のある接続で強制化する場合は、次の順序で確認します。

1. SettingsのRulesetsまたはBranch protectionで、mainの既存設定と自動更新の
   書き込み主体を確認します。既存設定を上書きせず、品質検査の実際のCheck名
   `quality`を必須チェックに追加し、最新のmainに対する検査を要求します。
2. 既存の自動更新Workflowはmainへ直接Pushするため、必須チェックやPR必須化との
   整合性を先に確認します。必要なら自動更新もPR経由に移すか、利用できる例外を
   書き込み主体と用途に限定して検証します。通常の編集まで無条件に回避できる
   広い例外は設けません。
3. 内容保護に失敗する検証用PRがマージ不可になること、成功したPRがマージ可能に
   なること、自動更新が継続することを確認します。設定の保存とAPIでの再取得、
   この動作確認まで終えてから「強制化済み」と報告します。

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

## AdGuardのVersion更新漏れの防止

ルール変更時は、日本標準時の `! Version: YYYYMMDDHHMM` を同じCommitで更新します。
`npm run hooks:install` で有効になる `pre-commit` Hookが、HEADとステージ済み内容を比較します。
作業ファイルだけVersionを更新しても、`git add` していなければCommitを拒否します。
手動実行は `python scripts/check_adguard_version_timestamp.py --staged` です。

GitHub Web UIやGitHub APIではHookが動きません。ルールとVersionを同じ書き込みに含め、
PR作成前にCommitの差分を確認してください。PRの `AdGuardのVersion日時検査` は引き続き必須の確認です。
後続CommitによるVersion更新では、先行Commitの更新漏れは解消しません。

## NG Word Regex for ChMateのVersion同期

対象は `NG Word Regex for ChMate/NG Word Regex for ChMate.txt` です。
Chat / Work / Codexも本文変更と現在のJSTのVersionを同じCommitに含めます。
ローカルでは `datetime.now(ZoneInfo("Asia/Tokyo")).strftime("%Y%m%d%H%M")`
または `TZ=Asia/Tokyo date +%Y%m%d%H%M` で取得します。内容変更がなければ更新しません。

品質検査はPRの各Commitとmainへのpushを検査します。Version行の欠落・重複・形式不正、
存在しない日時、更新漏れ、不要なVersionのみの更新、Commit日時をJSTへ変換した値との
ずれを検出します。処理からCommitまで5分未満を許容し、同じ分の編集は同値を許容します。
数値だけの日時から元のタイムゾーンや実際の処理時刻を証明することはできません。
Commit日時との照合でUTC等の9時間のずれを検出しますが、Commit日時の偽装までは防げません。
Squash mergeで日時が変わった場合は、GitHub APIのマージ済みPRとMerge SHA、
変更前後のTXTの一致を確認してから、元PRの全CommitのVersionと編集日時を再検査します。
API取得や履歴取得に失敗した場合はCIを失敗させます。
自動同期の例外にはBotのCommitter情報と、同じCommit内の内容チェックポイントも必要です。
Commit titleだけでは例外を許可しません。

既存の共通Workflow `update-version-timestamps.yml` はmainへのpush、品質検査完了、
定期実行、手動実行で内容ハッシュとチェックポイントを比較し、未同期の編集を実行時のJSTで補完します。
ChMate専用の手動Workflowも同じScriptを使い、同じconcurrency groupで直列化します。
push競合時は最新mainから再生成し、3回失敗した場合はCIを失敗させます。
欠落・重複・不正なVersion行は推測で修復せず、明確なエラーで停止します。

| 編集経路 | 対応と制約 |
| --- | --- |
| Chat / Work / Codex | AGENTS.mdで同時更新を指示。指示を読まないツールもあるため、指示だけでは保証しない |
| Git CLI | 導入済みHookでindexを検査。Hookは回避でき、全環境への自動導入はできない |
| GitHub上の直接編集 | mainへのpush後に検査・補完。元のCommitに遡って追記はできない |
| Pull Request | 各Commitの更新漏れを検出してCIを失敗させる。外部PRへ権限付きで自動書き込みしない |
| GitHub Actions / API | 編集主体に関係なくハッシュで検出。GITHUB_TOKENのpushでWorkflowが起動しない場合は定期実行で回収 |

mainの補完は別Commitとなり、チェックポイントも同時に記録します。同じ内容への再実行はCommitを作りません。
Versionだけの手動変更はハッシュを変えないため自動同期の対象外であり、品質検査で検出します。
Actions停止、権限不足、Branch保護、定期実行の遅延時は即時反映を保証できません。
失敗したPRのマージを禁止するには品質検査を必須チェックにする保護設定が別途必要です。
補完成功で過去の失敗したRunの結果が書き換わることもありません。
