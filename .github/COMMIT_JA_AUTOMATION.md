# PRのCommit日本語化と自動マージ

同じRepository内のPRで英語のCommit messageやPR説明を検出した場合に、Argos Translateで日本語へ翻訳し、翻訳内容の確認・Codex Review・品質検査の成功後に日本語のCommit messageでSquash mergeするWorkflowです。

mainに記録済みのCommitは書き換えません。PR作成後からマージまでを自動化します。Branchへのpushだけで新しいPRを作成する機能はありません。既存の自動更新Workflowによるmainへの直接pushも変更しません。

翻訳内容の承認に加え、GitHub側のWorkflow実行承認やCodex Reviewの再依頼が必要になる場合があります。完全無人でのマージを保証するものではありません。

## 初回設定

1. WorkflowはCPU版`torch==2.9.1+cpu`と`requirements-translation.txt`のArgos TranslateをRunnerへ導入します。外部の有料翻訳APIは不要です。既存のSecret `OPENAI_API_KEY`は削除しません。
2. Settings → Actions → Generalで、ActionsによるPRへの書き込みを許可します。Workflowは`contents: write`、`pull-requests: write`、`actions: write`、`checks: read`、`statuses: read`を使用します。RepositoryやOrganizationの上位ポリシーで禁止されている場合は、その設定も確認してください。
3. CodexのGitHub連携で、このRepositoryのCode Reviewを有効にします。`@codex review`への応答と利用枠が必要です。このWorkflow自体はCodexの接続・契約・利用枠を設定できません。
4. GitHubでSquash mergeを許可します。GitHubのAuto-merge機能の有効化は不要です。Workflowが条件を確認して、期待するSHAを指定したMerge APIを呼び出します。Branch保護・Rulesetは変更も回避もしません。

翻訳ライブラリは`argostranslate==1.11.0`、モデルは公式Indexの英語（`en`）→日本語（`ja`）Version `1.1`です。モデルの要求Argos Versionは`1.1`です。`COMMIT_TRANSLATION_MODEL`は使用しません。公式配布URLから取得し、固定SHA256と言語・Versionを照合してからインストールします。中間言語への自動切替は行いません。

公式配布URLの取得にはUser-Agentを明示します。GitHub-hosted runner上で配布物のMetadata・README・SHA256を確認し、`.github/argos-model.json`に固定しました。SHA256は`16300cc4eaa85320520cabcf433b63d01be40ef6966251de72043a083408f716`です。取得失敗や不一致を別モデルへの切替やOpenAI APIで補わず、停止します。

ライセンスは、Argosの開発者による[公式Issue #76の回答](https://github.com/argosopentech/argos-translate/issues/76)に基づき、Argosプロジェクトのモデル学習成果についてMIT / CC0として確認しました。配布物のREADMEにはOPUS、Wiktionary / Wiktextract、Stanzaと学習データの出典が記載されています。英日モデル個別のライセンス表記不足を扱う[未解決Issue #507](https://github.com/argosopentech/argos-translate/issues/507)は残っており、READMEにライセンスが明記されたとは説明しません。学習データや同梱物の権利まで一律にMIT / CC0とする判断ではありません。配布物の再配布は行わず、Runnerが公式配布先から取得します。

Version 1.1に同梱されたStanzaの重みは、現在のStanzaとの互換性に問題があります。重みを書き換えたり、最新版の別モデルを暗黙に取得したりせず、文分割にはspaCyの`blank('en')`とルールによる`sentencizer`を使います。翻訳の学習済みモデルは固定したArgosの英日モデルだけです。翻訳開始後に外部通信を行わないことを専用CIでも検査します。推論・文分割に使うCTranslate2、SentencePiece、spaCyのVersionも`requirements-translation.txt`で固定しています。

モデル実物の確認記録は[公式配布物の検証Run](https://github.com/Red-Frame-X/Prototype/actions/runs/42447418170)、文脈・表記保護・通信禁止・PR title/bodyとCommitの実翻訳確認は[実モデル検証Run](https://github.com/Red-Frame-X/Prototype/actions/runs/42448065454)で参照できます。`Update README.md`→`README.mdの更新`、`Fix GitHub Actions configuration`→`GitHub Actionsの設定を修正`、`Do not remove existing tests.`→`既存のテストを削除しないでください。`を確認しました。これらの代表例の成功で、任意の文章の意味の正確性まで証明されたとは扱いません。マージ前の翻訳内容の確認は引き続き必須です。

## マージを行わない実モデル検証

`Argos英日モデルの実物検証`は、翻訳関連ファイルを変更したPRでGitHub-hosted runner / Python 3.12上に起動します。権限は`contents: read`だけで、checkoutの認証情報も保持しません。公式モデルの取得・SHA256・Metadata・README、実翻訳の代表例、表記保護、既存日本語、日英混在、PR title/bodyとCommitの翻訳結果の検査を行います。PR・Commitの更新、Review依頼、マージは行いません。

ローカルで同じ検証を行う場合は、CPU版torchと`requirements-translation.txt`を導入し、空の専用ディレクトリを`ARGOS_PACKAGES_DIR`へ設定して`python scripts/test_argos_model.py`を実行します。公式配布先へのHTTPS通信が必要です。`ARGOS_MODEL_PROVIDER=OPENNMT`、`ARGOS_CHUNK_TYPE=STANZA`、`ARGOS_DEVICE_TYPE=cpu`はWorkflowと同じ値を使います。`STANZA`はArgosの初期化経路を固定する指定で、実際の文分割は上記のルールへ置き換えます。

## 処理の流れ

1. 5分ごとの定期実行、品質検査完了、または手動実行で開いているPRを確認します。定期実行の開始時刻はGitHubの混雑で遅れることがあります。
2. 同じRepository内にあり、作成者が書き込み権限を持ち、mainを対象とする通常のPRを選びます。Fork、Draft、Bot作成のPR、main自体は対象外です。
3. PRの全Commit messageとPR title/bodyの英語の一般説明をRunner内のArgos Translateで日本語へ翻訳します。日本語、登録済みの正式な製品名・技術用語、固有名詞とみられる表記、識別子、Version、URL、Issue参照、コードを一時識別子に置き換え、文全体の文脈を保ったまま翻訳してから原表記を復元します。識別子の欠落・重複・変更、未翻訳の一般説明、未完結のコードブロックは停止条件です。Markdownの行構造・引用とConventional Commitsのprefixも保持します。未知の名前の判別や全文章の意味の正確性を機械検査だけでは保証できないため、適用後の翻訳前後の記録を確認します。判別しづらい製品名・識別子はCode spanにしてください。本文・差分・Secretを外部の翻訳APIへ送りません。
4. Markdownのコード範囲はVersionを固定した`markdown-it-py`のCommonMarkパーサーで判定します。リスト内のフェンスと、リスト外の字下げ付きコードを区別し、Task listの`[x]` / `[X]` / `[ ]`も原表記のまま保持します。翻訳対象のSHAと件数、titleの表記、URL・Issue参照・Code spanを照合します。Git objectだけを処理し、PR側のコード・Hook・Artifactを特権Jobで実行しません。
5. 全Commitのtree・著者・日時・親の順序を保持してBranchを更新します。`--force-with-lease`で同時更新を保護します。書き換えたCommitとその後続CommitのSHAは変わり、既存の署名は取り除かれます。翻訳前後とSHA対応はPRのBot Commentへ記録します。
6. 次の実行で最新SHAへの`@codex review`を依頼し、品質検査Workflowを`workflow_dispatch`で起動します。`GITHUB_TOKEN`によるBranch更新でも再検証を省略しません。通常のPR検証と同じ比較範囲で検査します。
7. 最新SHAのCodexの機械可読状態が完了・指摘なしであり、対象PR番号とSHAをrun-nameに含む専用の品質検査が成功し、他のCheck・Statusが成功していることを確認します。同じSHAでも通常の手動実行や別PRの検証結果では代用しません。未解決のReview thread、変更要求、競合、Draftへの変更、SHAやPR説明の変更がある場合はマージしません。
8. 書き込み権限を持つ人が翻訳前後の全文章・情報・意味・正式表記を確認し、Botが提示する`/approve-commit-translation <fingerprint>`だけを単独のCommentに記述します。fingerprintは最新SHA・PR title/bodyに結び付き、更新後の古い承認やBotの承認は認めません。この確認がなければ自動マージしません。既存のCodex Review・CI条件もすべて必要です。
9. 日本語のPR title/bodyを最終Commit messageに指定してSquash mergeします。マージ後の実際のCommit messageを照合し、Version自動同期とmainの品質検査を明示的に起動します。mainの検証にはマージ直前のSHAを渡し、通常のpushと同じ比較範囲とVersion検証条件を適用します。

日本語化が不要なPRを新たに自動マージの対象には加えません。日本語化済みのPRに追加Commitが入った場合は、最新状態から翻訳と検証をやり直します。

## 停止する場合

Repository Variable `COMMIT_JA_AUTOMATION_ENABLED`を`false`にすると、翻訳・レビュー依頼・マージを停止します。再開するには`false`以外に変更します。

特定のPRだけを確認する場合は、Actionsの「PRのCommit日本語化とレビュー後の自動マージ」を手動実行し、`pr_number`にPR番号を指定します。空欄なら開いているPRを確認します。`dry_run`は手動実行では既定で`true`です。このモードでは翻訳前後をJSONでログに表示し、push・PR更新・Comment投稿・Review依頼・CI起動・マージを行いません。取得・整合性・翻訳検査が失敗した場合はテストモードも停止します。定期実行にはこの入力は適用されず、既存の実行経路を維持します。

## 待機・失敗時の扱い

`GITHUB_TOKEN`でCommitを書き換えた後、`pull_request`の`opened`・`synchronize`・`reopened`によるWorkflowは、GitHub側の実行承認待ちになる場合があります。Runの`action_required`と、PR画面の「Approve workflows to run」を確認してください。書き込み権限者が差分を確認して実行を承認し、必要な検査を完了させます。これは翻訳内容を承認するCommentとは別の操作で、専用の`workflow_dispatch`品質検査が成功しても、その承認を代行したことにはなりません。マージ状態が`clean`でなければ、既存のWorkflowは保留します。

Botが`@codex review`を投稿しても、最新SHAのReviewが開始されず、要約に以前のSHAだけが残る場合があります。通常のユーザー権限で`@codex review`を再依頼し、最新SHAの完了・指摘なしを確認してください。古いSHAのReviewや通常の手動検査を、専用の最新SHA検証の代わりに使いません。

これらの外部連携による待機を、CI・Reviewの省略、マージ条件の緩和、無条件の成功扱いで回避しません。画面操作やReviewの再依頼ができない場合は、確認できた段階までを部分検証として報告します。

- モデル未確認、モデルの取得・hash・Metadata検証失敗、翻訳処理失敗、翻訳結果の欠落・不正、取得失敗、同時pushの検出はエラーにします。他のPRの確認は継続します。
- 翻訳の対象は1～100 Commit、入力JSONは120,000 bytesまでです。翻訳前後のレビュー記録がCommentの上限に収まらない場合も、省略せず停止します。
- 品質検査やCodex Reviewが未完了の場合は、次回実行で再確認します。CI失敗やCodexの指摘を無視してマージしません。
- Codexの指摘に対して、ファイル内容を自動修正する機能はありません。修正Commitが入ると、新しいSHAで翻訳・レビュー・品質検査をやり直します。
- Codexへの依頼はSHAごとに1回です。利用枠不足や連携の問題を直してもレビューが再開しない場合は、PRで`@codex review`を再依頼してください。Commentの形式が将来変わった場合は、成功扱いにせず待機します。
- 品質検査Workflow自体を変更するPRは、自動マージしません。通常のレビューとマージで確認します。このWorkflowの導入前から開いていたPRも、最新mainの品質検査Workflowを取り込む必要があります。
- 初回設定後の実際のArgos翻訳・Codex Review・CI・マージが完了するまでは、全自動経路の稼働確認は完了していません。Secretの登録や外部サービスの有効化を、Workflowを追加しただけで完了したと判断しないでください。

## PR #261の翻訳誤停止と回帰検証

Run [42530138140](https://github.com/Red-Frame-X/Prototype/actions/runs/42530138140)は、
PR #261が開いていた時点で既定Branchの`ddd87c10`を取得し、翻訳直後の検証で停止しました。
PRのtitle・body・Commit messageは日本語でしたが、日本語に隣接する`README.md`を
Unicodeの単語境界では完全に保護できず、拡張子`.md`がArgosへ渡っていました。
固定英日モデルによる再現では日本語を含まない結果が返り、空・不正・未翻訳の検証条件に該当しました。
元Runには入力・訳文の記録がないため、当時の訳文そのものを確認できたという意味ではありません。

PathをASCIIの境界・文字集合で先に保護し、未登録の固有名詞の境界もASCIIで判定します。
本文中のRunner・Secret・cache・bodyと
検証用コマンドの表記も保護対象へ追加しました。日本語が含まれるという理由だけで行全体を
翻訳対象外にはせず、残った英語の一般説明は従来どおり翻訳・検証します。
失敗時は本文や訳文を出さず、title・body・Commit messageのどの項目で停止したかを記録します。

実入力は`tests/fixtures/pr261-japanese-translation.json`で保持し、Unit Testと
固定実モデルの検証で原文の完全保持を確認します。英語説明、部分翻訳、参照破損、
モデル失敗の既存Testを維持し、終了済みPR・処理中の終了・重複実行のTestも追加しています。

## Git trailerの保護漏れと継続検証

2026年11月9日の調査では、`Co-authored-by: Alice Example <alice@example.com>`と
`Signed-off-by`のキー・メールアドレスが部分的に分割され、翻訳器へ渡ることを再現しました。
分類は保護対象の取りこぼしと翻訳処理の停止です。実際の過去Runでこの問題が
発生したことや、当時の日本語訳は確認していません。再現Testの入力を実障害の訳文として扱いません。

Git公式の基本構文に従い、空行に続く末尾の`key: value`と継続行をブロック全体で
保護します。ただし、`Note: ...`等の一般説明を未翻訳のまま残さないよう、
`Co-authored-by`のようにハイフン付きのkeyを含むブロックに限定します。
コードブロックの判定を優先し、本文の説明まで一括で保護しません。
翻訳後の検証でも元のtrailer末尾との完全一致を要求し、キー・著者・メールアドレス・
重複・改行を保持します。ハイフンのないkeyだけのブロック、独自の区切り文字や
Git設定によるtrailer構文の拡張は対象外です。

回帰Testは日本語本文の無変更、英語説明の翻訳、複数・重複trailer、日本語の名前、
継続行、CRLF、trailerの改変・欠落・追加の拒否を検証します。
`scripts/test_argos_model.py`にも英語Commitとtrailerの組み合わせを追加し、
既存の固定モデルCIで実翻訳と原文保持を確認します。モデル・辞書・依存Versionは変更しません。

調査した経路は次のとおりです。

- `japanese-commits.yml`は既定BranchのScriptと固定Argos依存を導入します。
  `automate_japanese_commits.py`がPR title・body・各Commit messageを取得し、
  `argos_commit_translation.py`でMarkdown・技術表記・日本語を保護して行単位に翻訳し、
  保護識別子の一致と未翻訳を検証して復元します。最終検証後、変更のあるPRにだけ適用します。
- 翻訳の承認、最新SHAのCodex Review、品質検査、他のCheck、競合・未解決指摘の確認後に
  PR title・bodyをSquash messageとして明示指定し、マージ後の実messageを照合します。
  手動マージにはこのScriptの検証が自動適用されないため、確定前の確認が必要です。
- Workflowのname・run-name・Step表示と、自動更新のCommitは各Workflowに日本語を
  直接指定しています。Job ID・Step ID・式を翻訳する別の処理はありません。
  Chat / Work / Codexの作成方針は`AGENTS.md`、HookとCIのtitle検査は
  `scripts/check_commit_titles.py`です。これらはArgos翻訳器とは役割が異なります。

今後の不具合は、原文・実際の結果・RunとSHA・分類・原因・公式根拠・対応Testを
この文書と回帰Testへ追記します。一般説明の意味保持は識別子の一致だけでは保証できないため、
翻訳前後の比較と人による承認を維持します。

## 一次資料

- [Argos Translateの導入とPython API](https://github.com/argosopentech/argos-translate)
- [公式Indexの固定Revision](https://github.com/argosopentech/argospm-index/blob/ff90de60728f7c1338ff6b75974e4c89b2442d22/index.json)
- [spaCyのルールによる文分割](https://spacy.io/api/sentencizer)
- [Argos Translate 1.11.0](https://pypi.org/project/argostranslate/1.11.0/)
- [Codex Code Review](https://developers.openai.com/codex/cloud/code-review)
- [GitHub Actionsによるイベント起動の制限](https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow)
- [GitHub Pull Request Merge API](https://docs.github.com/en/rest/pulls/pulls#merge-a-pull-request)
- [Git trailerの構文](https://git-scm.com/docs/git-interpret-trailers)

## OPENAI_API_KEYの依存関係

移行前の最新mainでは、実行時参照は`japanese-commits.yml`と`automate_japanese_commits.py`だけでした。Repository内の他のWorkflowに参照はありません。説明文はこの文書と`CONTRIBUTING.md`にありました。今回、翻訳処理への注入と参照を取り除きましたが、GitHub Secretsの値・登録状態は変更していません。Repository外のWorkflow、Organizationの共有Secret、動的な参照の依存関係はこの調査では確認できません。
