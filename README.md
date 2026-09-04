# Prototype

[![Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml)

[![Sync AdGuard filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml)

[![Build uBOL Filter - Red Frame X](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml)

Chrome・ChromeOS・Android環境で試した設定、コンテンツブロックフィルタ、UserScript、ChMate用正規表現、変換・自動更新ツール、技術メモなどを保存している個人用リポジトリです。主な目的は、学習・検証の記録と、自分の環境で再利用する設定・スクリプト類のバックアップです。

> [!IMPORTANT]
> このリポジトリは個人利用を前提とした記録・バックアップです。内容の多くは、自分で作成した下書きをChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証できません。記述や設定には誤り、古い情報、環境依存の内容が含まれる可能性があります。
>
> フィルタ、スクリプト、設定、技術メモなどは、自分の環境での確認結果を残すことを目的としており、一般向けの手順書や配布物としての利用を想定していません。

## リポジトリ案内

主要なディレクトリ、原本、生成物、関連資料への導線をまとめています。

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| AdGuard Custom Rules | AdGuard向けの個人用コンテンツブロックルール、DNSルール、関連CHANGELOG | [README](./AdGuard%20Custom%20Rules/README.md) / [コンテンツブロックフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [DNSフィルタ](./AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [ChangeLog](./AdGuard%20Custom%20Rules/ChangeLog/) |
| uBOL Filter Converter | AdGuard用ルールをuBlock Origin Lite向けに変換する処理、テスト、自動生成物、変換レポート | [README](./uBOL%20Filter%20Converter/README.md) / [ディレクトリ](./uBOL%20Filter%20Converter/) / [生成フィルタ](./uBOL%20Filter%20Converter/dist/uBOL%20Filter%20-%20Red%20Frame%20X.txt) |
| uB-filter-by-kdroidwin (AdGuard Optimized) | 上流フィルタをAdGuard向けに変換した自動生成物 | [README](./dist/README.md) / [生成フィルタ](./dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt) |
| UserScript | 𝕏・YouTubeなどの表示や挙動を調整する個人用UserScript | [README](./UserScript/README.md) / [ディレクトリ](./UserScript/) |
| NG Word Regex for ChMate | ChMateで使用するJava正規表現 | [README](./NG%20Word%20Regex%20for%20ChMate/README.md) / [正規表現](./NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |
| Markdown Notes | ChromeOS、Android、GitHub、コンテンツブロックなどの学習・調査メモ | [README](./Markdown%20Notes/README.md) / [ディレクトリ](./Markdown%20Notes/) |
| scripts / tests | フィルタ変換・更新処理、整合性検査、回帰テスト | [scripts](./scripts/) / [tests](./tests/) / [uBOL tests](./uBOL%20Filter%20Converter/tests/) |
| config / upstream | 変換能力の定義、上流情報の追跡・ミラー | [config](./config/) / [upstream](./upstream/) |
| GitHub Actions | 品質確認、同期、変換、CHANGELOG追跡などのWorkflow | [Actions](../../actions) |

> [!NOTE]
> `uBOL Filter Converter/dist/`およびルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換スクリプトを修正して再生成します。

## 編集・更新の原則

- `AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt`はuBOL変換の原本でもあるため、ルール追加・削除時は`! Version:`も更新し、品質チェックを通してから反映します。
- `uBOL Filter Converter/dist/`とルートの`dist/`はGitHub Actionsによる生成物のため、原則として直接編集しません。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`には上流プロジェクトの追跡・ミラー情報が含まれるため、取得スクリプトまたは追跡設定を修正します。
- `Markdown Notes/`は学習・調査時点の記録を含みます。更新時には、可能な限り公式資料、公開ソース、対象バージョンを再確認します。
- ChatGPTによる推敲後の文章も、そのまま正しいとはみなさず、重要な技術情報は一次情報と実環境で再確認します。

## 自動更新と品質確認

GitHub Actionsで、個人用フィルタや変換処理の更新・整合性確認を自動化しています。

- AdGuard原本フィルタのメタデータ・行数・ルール数などの整合性検査
- AdGuardルール編集時の重複、改行、空白、大量削除などの事前検査
- Pythonの回帰テスト、UserScript構文検査、Markdownlint、AGLint
- `uB-filter-by-kdroidwin (AdGuard Optimized)`の定期同期と変換
- `uBOL Filter - Red Frame X`の再生成と変換レポートの更新
- AdGuardおよびuBO Liteの公式CHANGELOGの定期確認

ローカルで主要な検査を実行する場合：

```bash
npm ci
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
