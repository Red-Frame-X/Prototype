# Repositoryの編集・更新・品質管理方針

この文書は、ルート [README](../README.md) に記載されていた編集・更新・品質管理方針を移行したものです。関連する詳細手順は [AGENTS.md](../AGENTS.md)、[CONTRIBUTING.md](../CONTRIBUTING.md)、[PRのCommit日本語化と自動マージ](./COMMIT_JA_AUTOMATION.md) を参照してください。
## 基本方針

- このRepositoryは、個人の学習記録、検証ログ、設定バックアップとして維持します。
- 技術情報を確認する際は、対象プロジェクトの公式ドキュメント、公式Repository、公開ソース、変更履歴、Issuesなどの一次情報を優先します。
- 互換性を推測だけで拡張せず、必要な検証や回帰テストを行ってから変換処理・設定を変更します。
- 誤ブロック、互換性、視認性、性能、保守性、プライバシーなどのトレードオフを考慮します。
- 製品のUI名や機能名を記載する場合は、可能な限り対象バージョンの公式表記に合わせます。

## 編集・更新の原則

- `AdGuard Custom Rules` / `AdGuard DNS Custom Rules`の変更時は、変更したファイルの`! Version:`をJSTの現在時刻（`YYYYMMDDHHMM`）へ同じCommit内で更新します。
- ルートの`dist/`は自動生成物のため、直接編集せず、原本または変換処理を修正して再生成します。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`は上流情報の追跡・ミラー用で、取得Scriptや追跡設定から更新します。
- `Markdown Notes/`やChatGPTで推敲した内容は、重要な技術情報を可能な限り一次情報・公開ソース・対象バージョン・実環境で再確認します。
- 自動生成物は原則として直接編集せず、原本または変換処理を修正して再生成します。

## 自動更新・生成処理

GitHub Actionsで、更新処理・変換・品質確認を自動化しています。

- 対象ディレクトリの変更をmainへpushします。
- push後、コメントだけの編集も含め、`AdGuard Custom Rules`、`Markdown Notes`、`NG Word Regex for ChMate`、`UserScript`の対応するVersion MetadataをGitHub ActionsでJSTの現在時刻へ同期します。
- push時に同期が起動しなかった場合に備え、品質チェック完了後の実行、15分おきの定期実行、手動実行でも最新mainの未同期の変更を確認します。Versionだけを更新済みのファイルは再更新しません。
- uB-filter-by-kdroidwin (AdGuard Optimized)の定期同期・変換を行います。
- AdGuard公式の変更履歴を定期確認します。

## 品質管理・検証

- フィルタ・コードの整合性、回帰テスト、構文・Lintを自動検査します。
- GitHub Actions Workflowの安全性・構文、UserScriptのJavaScript構文、大量の内容消失も品質検査で確認します。
- AdGuard Custom Rules / AdGuard DNS Custom Rulesでは、Pull Request内の各Commitを検査し、ルール変更と! Version:の更新が同じCommitに含まれていることをCIで検証します。
- Workflow失敗時は原因を確認して修正し、必要に応じて再発防止策を反映します。

ローカルで主要な検査を実行する場合：

```bash
npm ci
python -m pip install -r requirements-ci.txt
python scripts/check_adguard_filter_integrity.py
python scripts/check_workflow_safety.py
python scripts/check_repository_terminology.py
bash scripts/check_workflow_syntax.sh
python scripts/check_adguard_user_rule_edit.py
python -m unittest discover -s tests -v
npm run lint:markdown
npm run lint:adguard
```

Markdownの行末にスペース1つが残ると、CIのMD009検査が失敗します。改行を表すスペース2つは保持してください。`npm run lint:markdown:fix` で自動修正し、差分を確認してからステージします。

Commit前にも同じ検査を行う場合は、`npm ci` の後に `npm run hooks:install` を実行します。この設定は、このクローンの `core.hooksPath` を `.githooks` に変更するため、独自のフックがある場合は先に統合してください。フックはステージ済みの内容を一時ディレクトリへ取り出して検査し、未ステージの修正で問題が隠れることを防ぎます。GitHubのWeb編集などローカルフックを通らない変更も、既存のCIで検査します。

## Commit・Pull Requestの運用

英語のCommit messageやPull Requestのtitle / bodyの一般説明は、ローカルで動作するオープンソース翻訳ライブラリ [Argos Translate](https://github.com/argosopentech/argos-translate) の固定英日モデルを使い、GitHub ActionsのRunner内で日本語化します。この翻訳処理はOpenAI APIを使用せず、失敗時もAPIへ切り替えません。

- `japanese-commits.yml`は5分ごとの定期実行、品質検査完了、手動実行でPRを確認します。同じRepository内でmainを対象とし、作成者に書き込み権限がある通常のPRが対象で、Fork・Draft・Bot作成のPRは対象外です。日本語化が不要なPRを新たに自動マージの対象には加えません。
- `scripts/automate_japanese_commits.py`と`scripts/argos_commit_translation.py`が翻訳・検証を行います。モデルのSHA256・Metadataや、正式表記・URL・コードなどの保持を確認し、取得・翻訳・検証に失敗した場合は停止します。
- 翻訳前後を確認した書き込み権限者の承認、最新SHAのCodex Review完了・指摘なし、専用の品質検査と他のCheck・Statusの成功などを確認してSquash mergeします。未解決のReview thread・変更要求・競合がある場合はマージしません。mainの既存履歴は書き換えません。
- `argos-translation-test.yml`は翻訳関連ファイルを変更したPRで固定モデルの実翻訳・表記保護・翻訳開始後の通信禁止を検証し、PR更新やマージは行いません。

依存関係は`requirements-translation.txt`、モデル情報は`.github/argos-model.json`で管理します。翻訳承認、手動実行のテストモード、停止設定、Workflow実行承認待ちなどの詳細は [PRのCommit日本語化と自動マージ](./COMMIT_JA_AUTOMATION.md) を参照してください。

## 表記・文書作成の方針

本文の説明は、読みやすさを優先して原則として日本語で記述します。

一方、IT・ソフトウェア開発・GitHub・コンテンツブロック等の分野で英語表記が一般的な用語、製品名、機能名、プロジェクト名、ディレクトリ名、ファイル名、コード識別子については、無理に日本語化せず原則として英語表記を優先します。

特に以下の名称は正式な英語表記を維持します。

- AdGuard Custom Rules
- uB-filter-by-kdroidwin (AdGuard Optimized)
- UserScript
- NG Word Regex for ChMate
- Markdown Notes
- GitHub Actions
- Workflow
- Commit
- Pull Request
- Issue
- Branch
- CI
- Lint
- Script
- Test

Commit messageおよびPull Requestのtitleとbodyでは、日本語の説明文と英語の正式名称を組み合わせることを必須とします。[AGENTS.md](../AGENTS.md)と[CONTRIBUTING.md](../CONTRIBUTING.md)に従い、新しく作成する一般説明は日本語にします。既存の自動検査が英語titleを通過させる場合も、この作成方針への適合を保証するものではありません。

例：

`Markdown Notes のVersion自動更新処理を修正`

`AdGuard Custom Rules の生成処理を修正`

以下の英語例は以前の方針の記録として保持します。新しく作成するCommit titleには使わず、`Markdown Notes のVersionを更新`のように日本語で説明します。

`Update Markdown Notes Version`

製品名、コード識別子、コマンド、設定キー、Metadata key、URL、ファイル名、ディレクトリ名、購読先Pathなどは、互換性と参照の一貫性を保つため原表記を維持します。

公式文書・公式UI・Upstreamで正式な表記が存在する場合は、その表記を優先します。`品質検査`、`自動更新`、`変更履歴`、`生成処理`、`構文検査`、`回帰テスト`、`設定`、`説明`、`注意事項`など、自然な日本語として読みやすい一般説明まで機械的に英語化しません。

ライセンス原文、公式変更履歴の原文ミラー、検証用の原文引用も保持します。UserScriptの日本語表示名には`@name:ja`を使い、更新時の識別に必要な既存の`@name`と`@namespace`は維持します。

## 関連ドキュメント

- [AGENTS.md](../AGENTS.md)：既存内容の保持と編集時の保護方針
- [CONTRIBUTING.md](../CONTRIBUTING.md)：変更・貢献時の手順
- [PRのCommit日本語化と自動マージ](./COMMIT_JA_AUTOMATION.md)：翻訳、承認、Review、マージ条件の詳細
