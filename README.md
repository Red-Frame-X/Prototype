# Prototype

## 連絡先
𝕏：[@Red_Frame_X](https://x.com/Red_Frame_X)

mond：[@Red_Frame_X](https://mond.how/Red_Frame_X)

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
| PR運用 | [PRのCommit日本語化とレビュー後の自動マージ](https://github.com/Red-Frame-X/Prototype/actions/workflows/japanese-commits.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/japanese-commits.yml?branch=main&event=schedule&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |
| 翻訳検証 | [Argos英日モデルの実物検証](https://github.com/Red-Frame-X/Prototype/actions/workflows/argos-translation-test.yml) | ![Workflowの状態](https://img.shields.io/github/actions/workflow/status/Red-Frame-X/Prototype/argos-translation-test.yml?event=pull_request&style=for-the-badge&label=%E7%8A%B6%E6%85%8B&labelColor=555&color=brightgreen) |

## Repository案内

主要なディレクトリ、原本、生成物、関連資料への導線をまとめています。

| 項目 | 主な内容 | 参照先 |
| --- | --- | --- |
| AdGuard Custom Rules | AdGuard向けの個人用コンテンツブロックルール、DNSルール、関連する変更履歴 | [README](./AdGuard%20Custom%20Rules/README.md) / [コンテンツブロックフィルタ](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [DNSフィルタ](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/AdGuard%20Custom%20Rules/AdGuard%20DNS%20Custom%20Rules%20-%20Red%20Frame%20X.txt) / [変更履歴](./AdGuard%20Custom%20Rules/ChangeLog/) |
| uB-filter-by-kdroidwin (AdGuard Optimized) | 上流フィルタをAdGuard向けに変換した自動生成物 | [README](./dist/README.md) / [生成フィルタ](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/dist/uB-filter-by-kdroidwin%20%28AdGuard%20Optimized%29.txt) |
| UserScript | 𝕏・YouTube・GIGAZINEなどの表示や挙動を調整する個人用UserScript | [README](./UserScript/README.md) / [ディレクトリ](./UserScript/) |
| NG Word Regex for ChMate | ChMateで使用するJava正規表現 | [README](./NG%20Word%20Regex%20for%20ChMate/README.md) / [正規表現](https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/NG%20Word%20Regex%20for%20ChMate/NG%20Word%20Regex%20for%20ChMate.txt) |
| Markdown Notes | ChromeOS、Android、Linux / Linux Mint、Googlebook、GitHub、コンテンツブロック、DNSなどの学習・調査メモ | [README](./Markdown%20Notes/README.md) / [ディレクトリ](./Markdown%20Notes/) |
| config / upstream | 変換能力の定義、上流情報の追跡・ミラー | [config](./config/) / [upstream](./upstream/) |
| scripts / tests | フィルタ変換・更新処理、整合性検査、回帰テスト | [scripts](./scripts/) / [tests](./tests/) |
| GitHub Actions | 品質確認、同期、変換、変更履歴の追跡などのWorkflow | [Actions](https://github.com/Red-Frame-X/Prototype/actions) |
| License | Repository全体のライセンス情報 | [LICENSE](./LICENSE) / [LICENSES.md](./LICENSES.md) |

フィルタ、UserScript、NG Word Regex for ChMateなど、ソフトウェアへの購読・登録・コピーに使うファイルのリンクはRaw URLに統一しています。

> [!NOTE]
> ルートの`dist/`にあるフィルタは自動生成物です。生成物を直接編集せず、元ルールまたは変換Scriptを修正して再生成します。

### [ChromeOS・Androidの最適化ガイド](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md)

- ChromeOS・Androidで使うブラウザ拡張機能やアプリの選び方、AdGuard・DNSによるコンテンツブロック、プライバシー・セキュリティの設定をまとめた個人用のガイドです。
- ChatGPT・Codexの活用方法やプロンプト例、利用中のサービスで起きた不具合と対処の記録も掲載しています。

### [Android アプリ ReVanced・Morphe・UPM・Reseam（Android）](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md#android-アプリ-revancedmorpheupmreseamandroid)

- AndroidアプリにPatchを適用して機能や表示を調整する各プロジェクトと、適用に使うManagerの違いを説明しています。
- 公式の入手先、対応APK・Patchの確認、導入・更新・バックアップ、不具合の調べ方をまとめています。
- 旧URVからUPMへの移行、設定JSONとは別に保存する署名用Keystore、Runtime Pluginの要件、Morpheの動画再生設定も扱っています。

### [Android アプリ ChMate（ChromeOS・Android）](./Markdown%20Notes/ChromeOS%20%26%20Android%20Optimization%20Guide.md#android-アプリ-chmatechromeosandroid)

- 掲示板アプリChMateの公式配布元と対応環境、板の登録、ログの保存・バックアップ、NG設定、操作・表示、プライバシー・広告について説明しています。
- 関連ツールのIOMateとHaiagaru-Morpheは、ChMate本体と区別して用途・対応Version・導入方法を案内し、Haiagaru-Morpheの更新・データ移行・不具合の検証手順もまとめています。
- ChromeOSでの動作保証がない点も明記しています。
- Chromebook上でChMateを操作するだけであれば、スマートフォン ハブを使うのがお手軽です。

## 編集・更新・品質管理方針

詳細は [Repositoryの編集・更新・品質管理方針](./.github/REPOSITORY_GUIDELINES.md) を参照してください。
