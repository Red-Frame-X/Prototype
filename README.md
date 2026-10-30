# Prototype

## 概要

ChromeOS・Android・Linux向けの設定、コンテンツブロックフィルタ、UserScript、ChMate用正規表現、GitHub運用、更新・変換ツール、技術メモをまとめた個人用の試作Repository

> [!IMPORTANT]
> 学習・検証結果の記録とバックアップを目的としています。ChatGPTで推敲・整理した内容や環境依存の情報を含むため、正確性・完全性は保証しません。
>
> フィルタ、Script、設定、技術メモは自分の環境で確認したもので、一般向けの手順書・配布物を想定していません。

## Workflow

| 分類 | Workflow | 状態 |
| --- | --- | --- |
| 品質検査 | [Repositoryの品質検査](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/quality.yml?branch=main&event=push&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| 生成・同期 | [uB-filter-by-kdroidwinの同期・AdGuard向け変換](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/sync.yml?branch=main&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| バージョン | [AdGuardのVersion日時検査](https://github.com/Red-Frame-X/Prototype/actions/workflows/check-adguard-version.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/check-adguard-version.yml?branch=main&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| バージョン | [Version日時の更新（日本標準時）](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-version-timestamps.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-version-timestamps.yml?branch=main&event=schedule&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| 保守 | [AdGuard変更履歴の更新](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-adguard-changelogs.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-adguard-changelogs.yml?branch=main&event=schedule&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| 保守 | [NG Word Regex for ChMate のVersion更新](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-chmate-ng-version.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-chmate-ng-version.yml?branch=main&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |

## Repository案内

主要なディレクトリ、原本、生成物、関連資料への導線をまとめています。

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| AdGuard Custom Rules | AdGuard向けの個人用コンテンツブロックルール、DNSルール、関連する変更履歴 | [README](./AdGuard%20Custom%20Rules/README.md) / [コンテンツブロックフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [DNSフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [変更履歴](./AdGuard%20Custom%20Rules/ChangeLog/) |
| uB-filter-by-kdroidwin (AdGuard Optimized) | 上流フィルタをAdGuard向けに変換した自動生成物 | [README](./dist/README.md) / [生成フィルタ](./dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt) |
| UserScript | 𝕏・YouTube・GIGAZINEなどの表示や挙動を調整する個人用UserScript | [README](./UserScript/README.md) / [ディレクトリ](./UserScript/) |
| NG Word Regex for ChMate | ChMateで使用するJava正規表現 | [README](./NG%20Word%20Regex%20for%20ChMate/README.md) / [正規表現](./NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |
| Markdown Notes | ChromeOS、Android、Linux / Linux Mint、Googlebook、GitHub、コンテンツブロック、DNSなどの学習・調査メモ | [README](./Markdown%20Notes/README.md) / [ディレクトリ](./Markdown%20Notes/) |
| config / upstream | 変換能力の定義、上流情報の追跡・ミラー | [config](./config/) / [upstream](./upstream/) |
| scripts / tests | フィルタ変換・更新処理、整合性検査、回帰テスト | [scripts](./scripts/) / [tests](./tests/) |
| GitHub Actions | 品質確認、同期、変換、変更履歴の追跡などのWorkflow | [Actions](https://github.com/Red-Frame-X/Prototype/actions) |
| License | Repository全体のライセンス情報 | [LICENSE](./LICENSE) / [LICENSES.md](./LICENSES.md) |

> [!NOTE]
> ルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換Scriptを修正して再生成します。

[ChromeOS・Androidの最適化ガイド](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md)：ChromeOS・Androidを中心に、ブラウザ、コンテンツブロック、プライバシー、セキュリティの設定・運用方法をまとめています。

[Android アプリ ReVanced・Morphe・UPM・Reseam（Android）](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md#android-アプリ-revancedmorpheurvreseamandroid)：各プロジェクトの公式情報、機能、導入・更新・バックアップ、互換性、Redditの参照方法をまとめています。Universal Patch Manager（UPM、旧URV）への移行、設定JSONと署名用Keystoreの個別バックアップ、Runtime Pluginの要件も説明しています。

[Android アプリ ChMate（ChromeOS・Android）](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md#android-アプリ-chmatechromeosandroid)：公式の配布元・対応環境、板の登録、バックアップ、NG設定、操作・表示、プライバシー・広告についてまとめています。IOMate・Haiagaru-Morpheの用途や導入・更新・データ移行、ChromeOSでの動作保証に関する注意点も説明しています。

## 編集・更新の原則

- `AdGuard Custom Rules` / `AdGuard DNS Custom Rules`の変更時は、変更したファイルの`! Version:`をJSTの現在時刻（`YYYYMMDDHHMM`）へ同じCommit内で更新します。
- ルートの`dist/`は自動生成物のため、直接編集せず、原本または変換処理を修正して再生成します。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`は上流情報の追跡・ミラー用で、取得Scriptや追跡設定から更新します。
- `Markdown Notes/`やChatGPTで推敲した内容は、重要な技術情報を可能な限り一次情報・公開ソース・対象バージョン・実環境で再確認します。

## 自動更新と品質確認

GitHub Actionsで、更新処理・変換・品質確認を自動化しています。

- フィルタ・コードの整合性、回帰テスト、構文・Lintを自動検査します。
- GitHub Actions Workflowの安全性・構文、UserScriptのJavaScript構文、大量の内容消失も品質検査で確認します。
- 対象ディレクトリの変更をmainへpushします。
- push後、コメントだけの編集も含め、`AdGuard Custom Rules`、`Markdown Notes`、`NG Word Regex for ChMate`、`UserScript`の対応するVersion MetadataをGitHub ActionsでJSTの現在時刻へ同期します。
- push時に同期が起動しなかった場合に備え、品質チェック完了後の実行、15分おきの定期実行、手動実行でも最新mainの未同期の変更を確認します。Versionだけを更新済みのファイルは再更新しません。
- AdGuard Custom Rules / AdGuard DNS Custom Rulesでは、Pull Request内の各Commitを検査し、ルール変更と! Version:の更新が同じCommitに含まれていることをCIで検証します。
- Workflow失敗時は原因を確認して修正し、必要に応じて再発防止策を反映します。
- uB-filter-by-kdroidwin (AdGuard Optimized)の定期同期・変換を行います。
- AdGuard公式の変更履歴を定期確認します。

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

## 方針

- このRepositoryは、個人の学習記録、検証ログ、設定バックアップとして維持します。
- 技術情報を確認する際は、対象プロジェクトの公式ドキュメント、公式Repository、公開ソース、変更履歴、Issuesなどの一次情報を優先します。
- 互換性を推測だけで拡張せず、必要な検証や回帰テストを行ってから変換処理・設定を変更します。
- 誤ブロック、互換性、視認性、性能、保守性、プライバシーなどのトレードオフを考慮します。
- 自動生成物は原則として直接編集せず、原本または変換処理を修正して再生成します。
- 製品のUI名や機能名を記載する場合は、可能な限り対象バージョンの公式表記に合わせます。

## 表記の方針

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

Commit messageおよびPull Requestでは、日本語の説明文と英語の正式名称を組み合わせる形式を基本とします。英語のみのCommit titleも、正式名称と意味が明確であれば使用できます。

例：

`Markdown Notes のVersion自動更新処理を修正`

`AdGuard Custom Rules の生成処理を修正`

`Update Markdown Notes Version`

製品名、コード識別子、コマンド、設定キー、Metadata key、URL、ファイル名、ディレクトリ名、購読先Pathなどは、互換性と参照の一貫性を保つため原表記を維持します。

公式文書・公式UI・Upstreamで正式な表記が存在する場合は、その表記を優先します。`品質検査`、`自動更新`、`変更履歴`、`生成処理`、`構文検査`、`回帰テスト`、`設定`、`説明`、`注意事項`など、自然な日本語として読みやすい一般説明まで機械的に英語化しません。

ライセンス原文、公式変更履歴の原文ミラー、検証用の原文引用も保持します。UserScriptの日本語表示名には`@name:ja`を使い、更新時の識別に必要な既存の`@name`と`@namespace`は維持します。
