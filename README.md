# Prototype

[![Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml)

[![Sync AdGuard filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml)

[![Build uBOL Filter - Red Frame X](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml)

Chrome・ChromeOS・Android向けの設定、コンテンツブロックフィルタ、UserScript、ChMate用正規表現、更新・変換ツール、技術メモをまとめた個人用リポジトリです。

> [!IMPORTANT]
> 学習・検証結果の記録とバックアップを目的としています。ChatGPTで推敲・整理した内容や環境依存の情報を含むため、正確性・完全性は保証しません。
>
> フィルタ、スクリプト、設定、技術メモは自分の環境で確認したもので、一般向けの手順書・配布物を想定していません。

## リポジトリ案内

主要なディレクトリ、原本、生成物、関連資料への導線をまとめています。

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| AdGuard Custom Rules | AdGuard向けの個人用コンテンツブロックルール、DNSルール、関連CHANGELOG | [README](./AdGuard%20Custom%20Rules/README.md) / [コンテンツブロックフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [DNSフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [ChangeLog](./AdGuard%20Custom%20Rules/ChangeLog/) |
| uBOL Filter Converter | AdGuard用ルールをuBlock Origin Lite向けに変換する処理、テスト、自動生成物、変換レポート | [README](./uBOL%20Filter%20Converter/README.md) / [ディレクトリ](./uBOL%20Filter%20Converter/) / [生成フィルタ](./uBOL%20Filter%20Converter/dist/uBOL%20Filter%20-%20Red%20Frame%20X.txt) / [ChangeLog](./uBOL%20Filter%20Converter/upstream/ubol-CHANGELOG.source.md) |
| uB-filter-by-kdroidwin (AdGuard Optimized) | 上流フィルタをAdGuard向けに変換した自動生成物 | [README](./dist/README.md) / [生成フィルタ](./dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt) |
| UserScript | 𝕏・YouTubeなどの表示や挙動を調整する個人用UserScript | [README](./UserScript/README.md) / [ディレクトリ](./UserScript/) |
| NG Word Regex for ChMate | ChMateで使用するJava正規表現 | [README](./NG%20Word%20Regex%20for%20ChMate/README.md) / [正規表現](./NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |
| Markdown Notes | ChromeOS、Android、GitHub、コンテンツブロックなどの学習・調査メモ | [README](./Markdown%20Notes/README.md) / [ディレクトリ](./Markdown%20Notes/) |
| config / upstream | 変換能力の定義、上流情報の追跡・ミラー | [config](./config/) / [upstream](./upstream/) |
| scripts / tests | フィルタ変換・更新処理、整合性検査、回帰テスト | [scripts](./scripts/) / [tests](./tests/) / [uBOL tests](./uBOL%20Filter%20Converter/tests/) |
| GitHub Actions | 品質確認、同期、変換、CHANGELOG追跡などのWorkflow | [Actions](../../actions) |
| License | リポジトリ全体のライセンス情報 | [LICENSE](./LICENSE) / [LICENSES.md](./LICENSES.md) |

> [!NOTE]
> `uBOL Filter Converter/dist/`およびルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換スクリプトを修正して再生成します。

## 編集・更新の原則

- `AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt`はuBOL変換の原本です。これ、または`AdGuard Custom Rules/AdGuard DNS Custom Rules - Red Frame X.txt`のルール変更時は、変更したファイルの`! Version:`をJSTの現在時刻（`YYYYMMDDHHMM`）へ同じコミット内で更新し、品質チェック後に反映します。
- `uBOL Filter Converter/dist/`とルートの`dist/`は自動生成物のため、原則として直接編集しません。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`は上流情報の追跡・ミラー用です。更新は取得スクリプトや追跡設定から行います。
- `Markdown Notes/`の更新時は、可能な限り公式資料・公開ソース・対象バージョンを再確認します。
- ChatGPTで推敲した内容も、重要な技術情報は一次情報と実環境で再確認します。

## 自動更新と品質確認

GitHub Actionsで、個人用フィルタや変換処理の更新・整合性確認を自動化しています。

- フィルタ・コードの整合性、回帰テスト、構文・Lintを自動検査
- 対象ファイル更新時に`! Version:`を日付・現在時刻へ自動更新し、AdGuard原本2ファイルではルール変更とVersion更新が同じコミットに含まれることもCIで検証
- GitHub Actions失敗時の原因確認・修正と再発防止
- `uB-filter-by-kdroidwin (AdGuard Optimized)`を定期同期・変換
- `uBOL Filter - Red Frame X`を再生成し、変換レポートを更新
- AdGuard・uBO Lite公式CHANGELOGを定期確認

ローカルで主要な検査を実行する場合：

```bash
npm ci
python -m pip install -r requirements-ci.txt
python scripts/check_adguard_filter_integrity.py
python scripts/check_adguard_user_rule_edit.py
python -m unittest discover -s tests -v
python -m unittest discover -s "uBOL Filter Converter/tests" -v
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
