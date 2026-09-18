# Prototype

## 概要

Chrome・ChromeOS・Android向けの設定、コンテンツブロックフィルタ、UserScript、ChMate用正規表現、更新・変換ツール、技術メモをまとめた個人用リポジトリです。

> [!IMPORTANT]
> 学習・検証結果の記録とバックアップを目的としています。ChatGPTで推敲・整理した内容や環境依存の情報を含むため、正確性・完全性は保証しません。
>
> フィルタ、スクリプト、設定、技術メモは自分の環境で確認したもので、一般向けの手順書・配布物を想定していません。

## Workflow

| Category | Workflow | Status |
| --- | --- | --- |
| Quality | [Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/quality.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |
| Build / Sync | [Sync and Convert uB-filter-by-kdroidwin (AdGuard Optimized)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/sync.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |
| Version | [Check AdGuard Version Timestamp](https://github.com/Red-Frame-X/Prototype/actions/workflows/check-adguard-version.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/check-adguard-version.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |
| Version | [Update Version Timestamps (JST)](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-version-timestamps.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-version-timestamps.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |
| Maintenance | [Update AdGuard Changelogs](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-adguard-changelogs.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-adguard-changelogs.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |
| Maintenance | [Update ChMate NG Version](https://github.com/Red-Frame-X/Prototype/actions/workflows/update-chmate-ng-version.yml) | ![STATUS PASSING](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/update-chmate-ng-version.yml?style=for-the-badge&label=STATUS&labelColor=555&color=brightgreen) |

## リポジトリ案内

主要なディレクトリ、原本、生成物、関連資料への導線をまとめています。

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| AdGuard Custom Rules | AdGuard向けの個人用コンテンツブロックルール、DNSルール、関連CHANGELOG | [README](./AdGuard%20Custom%20Rules/README.md) / [コンテンツブロックフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [DNSフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [ChangeLog](./AdGuard%20Custom%20Rules/ChangeLog/) |
| uB-filter-by-kdroidwin (AdGuard Optimized) | 上流フィルタをAdGuard向けに変換した自動生成物 | [README](./dist/README.md) / [生成フィルタ](./dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt) |
| UserScript | 𝕏・YouTubeなどの表示や挙動を調整する個人用UserScript | [README](./UserScript/README.md) / [ディレクトリ](./UserScript/) |
| NG Word Regex for ChMate | ChMateで使用するJava正規表現 | [README](./NG%20Word%20Regex%20for%20ChMate/README.md) / [正規表現](./NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |
| Markdown Notes | ChromeOS、Android、GitHub、コンテンツブロックなどの学習・調査メモ | [README](./Markdown%20Notes/README.md) / [ディレクトリ](./Markdown%20Notes/) |
| config / upstream | 変換能力の定義、上流情報の追跡・ミラー | [config](./config/) / [upstream](./upstream/) |
| scripts / tests | フィルタ変換・更新処理、整合性検査、回帰テスト | [scripts](./scripts/) / [tests](./tests/) |
| GitHub Actions | 品質確認、同期、変換、CHANGELOG追跡などのWorkflow | [Actions](../../actions) |
| License | リポジトリ全体のライセンス情報 | [LICENSE](./LICENSE) / [LICENSES.md](./LICENSES.md) |

> [!NOTE]
> ルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換スクリプトを修正して再生成します。

## 編集・更新の原則

- `AdGuard Custom Rules` / `AdGuard DNS Custom Rules`の変更時は、変更したファイルの`! Version:`をJSTの現在時刻（`YYYYMMDDHHMM`）へ同じコミット内で更新します。
- ルートの`dist/`は自動生成物のため、直接編集せず、原本または変換処理を修正して再生成します。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`は上流情報の追跡・ミラー用で、取得スクリプトや追跡設定から更新します。
- `Markdown Notes/`やChatGPTで推敲した内容は、重要な技術情報を可能な限り一次情報・公開ソース・対象バージョン・実環境で再確認します。

## 自動更新と品質確認

GitHub Actionsで、更新処理・変換・品質確認を自動化しています。

- フィルタ・コードの整合性、回帰テスト、構文・Lintを自動検査
- 対象ディレクトリの変更をmainへpushした後、対応するVersionメタデータをGitHub ActionsでJSTの現在時刻へ同期します。`AdGuard Custom Rules` / `AdGuard DNS Custom Rules`では、Pull Request時にルール変更と`! Version:`更新が同じコミットに含まれることもCIで検証します
- Workflow失敗時は原因を確認して修正し、必要に応じて再発防止策を反映
- `uB-filter-by-kdroidwin (AdGuard Optimized)`の定期同期・変換
- AdGuard公式CHANGELOGを定期確認

ローカルで主要な検査を実行する場合：

```bash
npm ci
python -m pip install -r requirements-ci.txt
python scripts/check_adguard_filter_integrity.py
python scripts/check_adguard_user_rule_edit.py
python -m unittest discover -s tests -v
npm run lint:markdown
npm run lint:adguard
```

## 方針

- このリポジトリは、個人の学習記録、検証ログ、設定バックアップとして維持します。
- 技術情報を確認する際は、対象プロジェクトの公式ドキュメント、公式リポジトリ、公開ソース、CHANGELOG、Issuesなどの一次情報を優先します。
- 互換性を推測だけで拡張せず、必要な検証や回帰テストを行ってから変換処理・設定を変更します。
- 誤ブロック、互換性、視認性、性能、保守性、プライバシーなどのトレードオフを考慮します。
- 自動生成物は原則として直接編集せず、原本または変換処理を修正して再生成します。
- 製品のUI名や機能名を記載する場合は、可能な限り対象バージョンの公式表記に合わせます。
