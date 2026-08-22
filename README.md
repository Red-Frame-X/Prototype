# Prototype

[![Repository Quality Checks](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/quality.yml)
[![Sync AdGuard filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/sync.yml)
[![Build uBO Lite filter](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml/badge.svg)](https://github.com/Red-Frame-X/Prototype/actions/workflows/build-ubol.yml)

ChromeOS・Android・コンテンツブロックに関する、個人利用向けのフィルタ、
UserScript、正規表現、技術メモをまとめたリポジトリです。

> [!IMPORTANT]
> 個人環境で検証した内容であり、すべての端末・サイトでの動作は保証しません。
> フィルタやスクリプトは、少数ずつ導入して誤ブロックや表示崩れを確認してください。

## 目的から選ぶ

| 目的 | 推奨コンテンツ | 対象 |
| --- | --- | --- |
| AdGuardで個人用ルールを使う | [AdGuard Custom Rules](AdGuard%20Custom%20Rules/) | AdGuard Browser Extension／Android／DNS |
| AdGuard用ルールをuBO Liteで使う | [uBOL Filter - Red Frame X](uBOL%20Filter%20Converter/) | uBlock Origin Lite 2026.621.1813以降 |
| kdroidwinフィルタをAdGuard MV3で使う | [uB-filter-by-kdroidwin (AdGuard Optimized)](dist/) | 主にAdGuard Browser Extension MV3 |
| 𝕏・YouTubeの表示を調整する | [UserScript](UserScript/) | Tampermonkeyなど |
| ChMateでNGワードを設定する | [NG Word Regex for ChMate](NG%20Word%20Regex%20for%20ChMate/) | ChMate |
| ChromeOS・Android等の手順を読む | [Markdown Notes](Markdown%20Notes/) | 技術メモ／調査資料 |

## フィルタを購読する

### AdGuard Custom Rules - Red Frame X

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt
```

### uBOL Filter - Red Frame X

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/uBOL%20Filter%20Converter/dist/uBOL%20Filter%20-%20Red%20Frame%20X.txt
```

### uB-filter-by-kdroidwin (AdGuard Optimized)

```text
https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt
```

各フィルタの対応機能、導入手順、変換で除外されるルールは、リンク先のREADMEを
確認してください。uBO Lite用生成版とAdGuard用生成版は、元フィルタと完全に同じ
動作にはなりません。互換性を安全に判断できないルールは、誤変換を避けるため除外
またはコメントアウトしています。

## リポジトリ構成

| パス | 内容 |
| --- | --- |
| `AdGuard Custom Rules/` | Webフィルタ、DNSルール、AdGuard CHANGELOGミラー |
| `uBOL Filter Converter/` | uBO Lite向け変換処理、テスト、生成物、変換レポート |
| `dist/` | kdroidwinフィルタのAdGuard向け生成物 |
| `UserScript/` | 𝕏・YouTube向けUserScript |
| `NG Word Regex for ChMate/` | ChMate向けJava正規表現 |
| `Markdown Notes/` | ChromeOS、Android、広告ブロック、GitHub関連資料 |
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

- 上流の仕様、公開ソース、CHANGELOGを優先して確認します。
- 互換性を推測だけで拡張せず、回帰テストを追加してから変換処理を変更します。
- 誤ブロック、互換性、性能、保守性のバランスを重視します。
- 自動生成物は直接編集せず、原本または変換処理を修正します。

## Contact

- User Name: Red Frame X
- 𝕏: [@Red_Frame_X](https://x.com/Red_Frame_X)
- mond: [Red Frame X](https://mond.how/ja/Red_Frame_X)

## License

自身で作成したコンテンツは原則として[CC0 1.0 Universal](LICENSE)で提供します。
第三者作品を基にしたファイルには原作品のライセンスが適用されます。対象範囲、
GPL-3.0の派生物、例外、無保証については[LICENSES.md](LICENSES.md)を参照してください。
