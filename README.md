# Prototype

[![Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml)

[![Sync AdGuard filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml)

[![Build uBOL Filter - Red Frame X](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml)

Chrome・ChromeOS・Android環境での個人利用を中心に、コンテンツブロックフィルタ、UserScript、Chromeテーマ、ChMate用正規表現、変換・自動更新ツール、技術メモなどをまとめたリポジトリです。AdGuardやuBlock Origin Liteをはじめ、ブラウザや端末を使いやすく調整するための設定・ツール・資料を収録しています。

> [!IMPORTANT]
> 個人環境で作成・検証した内容を含み、すべての端末・ブラウザ・サイトでの動作を保証するものではありません。フィルタ、スクリプト、テーマなどは内容を確認したうえで導入し、誤ブロック、表示崩れ、機能不全などがないことを確認してください。

## 目的から選ぶ

| 目的 | 推奨コンテンツ | 主な対象 |
| --- | --- | --- |
| AdGuardで個人用ルールを使う | [AdGuard Custom Rules](AdGuard%20Custom%20Rules/) | AdGuard ブラウザ拡張機能／AdGuard for Android／DNSフィルタリング |
| AdGuard用ルールをuBO Liteで使う | [uBOL Filter - Red Frame X](uBOL%20Filter%20Converter/) | uBlock Origin Lite 2026.621.1813以降 |
| uB-filter-by-kdroidwinをAdGuardで使う | [uB-filter-by-kdroidwin (AdGuard Optimized)](dist/) | 主にAdGuard ブラウザ拡張機能 MV3対応版 |
| 𝕏・YouTubeの表示を調整する | [UserScript](UserScript/) | Violentmonkey／Tampermonkeyなど |
| Chromeのタブ配色を変更する | [Royal Desert Sand Dark Tabs](Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md#chromeos-chrome-%E3%83%86%E3%83%BC%E3%83%9E) | Chrome／ChromeOS |
| ChMateでNGワードを設定する | [NG Word Regex for ChMate](NG%20Word%20Regex%20for%20ChMate/) | ChMate |
| ChromeOS・Android等の手順や技術情報を読む | [Markdown Notes](Markdown%20Notes/) | ChromeOS／Android／GitHub／コンテンツブロック関連資料 |

## 主要コンテンツへの直接リンク

- [AdGuard Custom Rules - Red Frame X](AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：AdGuard向けの個人用コンテンツブロックフィルタ
- [AdGuard DNS Custom Rules - Red Frame X](AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt)：AdGuard向けDNSフィルタ
- [uBOL Filter - Red Frame X](uBOL%20Filter%20Converter/dist/uBOL%20Filter%20-%20Red%20Frame%20X.txt)：uBlock Origin Lite向けに保守的に変換した生成フィルタ
- [uB-filter-by-kdroidwin (AdGuard Optimized)](dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt)：uB-filter-by-kdroidwinをAdGuard向けに変換した非公式生成フィルタ
- [Royal Desert Sand Dark Tabs](royal_desert_sand_dark_tabs.zip)：Chrome／ChromeOS向けのカスタムテーマ
- [ChromeOS & Android Optimization Guide](Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md)：ChromeOS・Androidの設定、アプリ、拡張機能、プライバシー対策をまとめた総合ガイド

> [!NOTE]
> `uBOL Filter Converter/dist/`およびルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換スクリプトを修正して再生成してください。

## リポジトリ構成

| パス | 内容 |
| --- | --- |
| `AdGuard Custom Rules/` | AdGuard向けコンテンツブロックフィルタ、DNSフィルタ、AdGuard CHANGELOGミラー |
| `uBOL Filter Converter/` | AdGuard用ルールのuBO Lite向け変換処理、テスト、自動生成フィルタ、変換レポート |
| `dist/` | uB-filter-by-kdroidwinのAdGuard向け自動生成物 |
| `UserScript/` | 𝕏・YouTubeなどの表示や挙動を調整するUserScript |
| `NG Word Regex for ChMate/` | ChMate向けJava正規表現 |
| `Markdown Notes/` | ChromeOS、Android、コンテンツブロック、GitHubなどの技術メモ・調査資料 |
| `scripts/`、`tests/` | フィルタ変換・更新処理、整合性検査、回帰テスト |
| `config/`、`upstream/` | 変換能力の定義と上流情報の追跡データ |

## 編集・更新の原則

- `AdGuard Custom Rules/AdGuard Custom Rules - Red Frame X.txt`はuBOL変換の原本でもあるため、ルール追加・削除時は`! Version:`も更新し、品質チェックを通してから反映します。
- `uBOL Filter Converter/dist/`とルートの`dist/`はGitHub Actionsによる生成物です。原則として直接編集しません。
- `AdGuard Custom Rules/ChangeLog/`と`upstream/`には上流プロジェクトの追跡・ミラー情報が含まれます。上流情報を根拠なく手動改変せず、取得スクリプトまたは追跡設定を修正します。
- Markdown Notesは仕様変更で古くなりやすいため、更新時には公式資料と対象バージョンを再確認します。

## 自動更新と品質確認

GitHub Actionsで、フィルタや変換ツールを中心とした更新・品質確認を自動化しています。

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

- 対象プロジェクトの公式ドキュメント、公式リポジトリ、公開ソース、CHANGELOG、Issuesなどの一次情報を優先します。
- 互換性を推測だけで拡張せず、必要な検証や回帰テストを行ってから変換処理・設定を変更します。
- 誤ブロック、互換性、視認性、性能、保守性、プライバシーなどのトレードオフを考慮します。
- 自動生成物は原則として直接編集せず、原本または変換処理を修正して再生成します。
- 製品のUI名や機能名を記載する場合は、可能な限り対象バージョンの公式表記に合わせます。

## 主要な公式資料

- [AdGuard ナレッジベース](https://adguard.com/kb/ja/)
- [AdGuard ブラウザ拡張機能 MV3対応版](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuard Browser Extension](https://github.com/AdguardTeam/AdguardBrowserExtension)
- [uBlock Origin / uBO Lite source](https://github.com/gorhill/uBlock)
- [uBlock Origin Lite CHANGELOG](https://github.com/uBlockOrigin/uBOL-home/blob/main/CHANGELOG.md)

各サブディレクトリのREADMEには、その内容に直接関係する上流資料を記載しています。

## Contact

- User Name：Red Frame X
- 𝕏：[@Red_Frame_X](https://x.com/Red_Frame_X)
- mond：[@Red Frame X](https://mond.how/ja/Red_Frame_X)

## License

自身で作成したコンテンツは原則として[CC0 1.0 Universal](LICENSE)で提供します。第三者作品を基にしたファイルには原作品のライセンスが適用されます。対象範囲、GPL-3.0の派生物、例外、無保証については[LICENSES.md](LICENSES.md)を参照してください。
