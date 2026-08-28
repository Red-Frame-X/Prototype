# Prototype

[![Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml)

[![Sync AdGuard filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml)

[![Build uBOL Filter - Red Frame X](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml)

ChromeOS・Android環境での個人利用を中心に、AdGuard・uBlock Origin Lite向けのコンテンツブロックフィルタ、UserScript、ChMate用正規表現、変換・自動更新ツール、技術メモをまとめたリポジトリです。

> [!IMPORTANT]
> 個人環境で検証した内容を含み、すべての端末・ブラウザ・サイトでの動作を保証するものではありません。フィルタやスクリプトは少数ずつ導入し、誤ブロック、表示崩れ、機能不全がないことを確認してください。

## 目的から選ぶ

| 目的 | 推奨コンテンツ | 主な対象 |
| --- | --- | --- |
| AdGuardで個人用ルールを使う | [AdGuard Custom Rules](AdGuard%20Custom%20Rules/) | AdGuard ブラウザ拡張機能／AdGuard for Android／DNSフィルタリング |
| AdGuard用ルールをuBO Liteで使う | [uBOL Filter - Red Frame X](uBOL%20Filter%20Converter/) | uBlock Origin Lite 2026.621.1813以降 |
| uB-filter-by-kdroidwinをAdGuardで使う | [uB-filter-by-kdroidwin (AdGuard Optimized)](dist/) | 主にAdGuard ブラウザ拡張機能 MV3対応版 |
| 𝕏・YouTubeの表示を調整する | [UserScript](UserScript/) | Violentmonkey／Tampermonkeyなど |
| ChMateでNGワードを設定する | [NG Word Regex for ChMate](NG%20Word%20Regex%20for%20ChMate/) | ChMate |
| ChromeOS・Android等の手順を読む | [Markdown Notes](Markdown%20Notes/) | 技術メモ／調査資料 |
| Chromeのタブ配色を変更する | [Royal Desert Sand Dark Tabs](royal_desert_sand_dark_tabs.zip) | Chrome／ChromeOS |

## Royal Desert Sand Dark Tabs

[royal_desert_sand_dark_tabs.zip](royal_desert_sand_dark_tabs.zip) は、Royal Desert Sand系の配色をベースに、バックグラウンドタブをより明確に見分けられるよう濃いブルー系に調整したChromeテーマです。新しいタブページの背景はグレー系とし、アクティブタブと非アクティブタブの視認性を重視しています。

ZIPを展開し、Chromeの「拡張機能」ページでデベロッパーモードを有効にして、展開したテーマフォルダを「パッケージ化されていない拡張機能を読み込む」から指定して利用します。

## リポジトリ構成

| パス | 内容 |
| --- | --- |
| `AdGuard Custom Rules/` | コンテンツブロックフィルタ、DNSフィルタ、AdGuard CHANGELOGミラー |
| `uBOL Filter Converter/` | uBO Lite向け変換処理、テスト、生成物、変換レポート |
| `dist/` | uB-filter-by-kdroidwinのAdGuard向け生成物 |
| `UserScript/` | 𝕏・YouTube向けUserScript |
| `NG Word Regex for ChMate/` | ChMate向けJava正規表現 |
| `Markdown Notes/` | ChromeOS、Android、コンテンツブロック、GitHub関連資料 |
| `royal_desert_sand_dark_tabs.zip` | Chrome向けカスタムテーマ「Royal Desert Sand Dark Tabs」 |
| `scripts/`、`tests/` | AdGuard向け変換・更新処理と回帰テスト |
| `config/`、`upstream/` | 変換能力の定義と上流情報の追跡データ |

## 自動更新と品質確認

GitHub Actionsで次を自動化しています。

- Pythonの回帰テスト、UserScript構文検査、Markdownlint、AGLint
- `uB-filter-by-kdroidwin (AdGuard Optimized)`の定期同期と変換
- `uBOL Filter - Red Frame X`の再生成と変換レポートの更新
- AdGuardおよびuBO Liteの公式CHANGELOGの定期確認

ローカルで主要な検査を実行する場合：

```bash
npm ci
python -m unittest discover -s tests -v
python -m unittest discover -s "uBOL Filter Converter/tests" -v
npm run lint:markdown
npm run lint:adguard
```

## 方針

- 対象プロジェクトの公式ドキュメント、公式リポジトリ、公開ソース、CHANGELOG、Issuesなどの一次情報を優先します。
- 互換性を推測だけで拡張せず、必要な回帰テストを追加してから変換処理を変更します。
- 誤ブロック、互換性、性能、保守性、プライバシーのトレードオフを考慮します。
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
