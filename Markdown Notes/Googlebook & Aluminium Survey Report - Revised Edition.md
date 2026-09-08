# Googlebook / Aluminium 調査レポート

Googleが2026年5月に発表した「Googlebook」と、発表前に報道された開発コードネーム「Aluminium」を整理します。将来の端末選定や仕様比較で再確認できるよう、公式発表・報道・未確認事項を分けて残している調査記録です。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260908 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

> [!IMPORTANT]
> Googlebookは発売前です。公式発表、報道、推測を区別し、仕様を確定情報として先取りしないでください。

## 要約

Googlebookは、Googleが2026年5月12日に正式発表した新しいノートPCカテゴリです。GoogleはGemini Intelligenceを中核に据え、Androidスマートフォンとの連携を重視した製品として紹介しています。2026年秋の投入予定で、Googleはハードウェアパートナーとして **Acer、ASUS、Dell、HP、Lenovo** を公表しています。一方、2026年9月8日時点でも、個別モデルの価格、全対応地域、CPU、最低RAM、Linux実行方式、既存Chromebookの移行対象など、未発表の仕様があります。

「Aluminium」は求人情報などを根拠に報道されたAndroidベースPCプロジェクトのコードネームです。Googleの正式な製品発表では「Googlebook」を使用しており、「Aluminium OS」または「ALOS」を正式な製品名としていません。したがって、バックアップ目的でAluminiumに関する過去の報道・予測を残す場合も、Google公式の確定情報とは区別します。

## 確認できる情報

Google公式発表で確認できる主な内容は次のとおりです。

- Googlebookは、Gemini Intelligence向けに設計された新しいノートPCカテゴリ。
- Geminiの文脈提案をカーソルから呼び出す「Magic Pointer」。
- 指示からダッシュボードを作る「Create your Widget」。
- Androidスマートフォン上のアプリやファイルとの連携。
- Acer、ASUS、Dell、HP、Lenovoなどのハードウェアパートナー。
- 2026年秋の投入予定。

GoogleのAndroid関連発表では、GooglebookをAndroidエコシステムの新しいノートPCカテゴリとして扱っています。公式発表の範囲を超えて「Aluminium OS搭載」や特定のAndroidバージョン、仮想化方式を確定事項として扱わないようにします。

## 未確認・未発表の事項

- ベースとなるAndroidのバージョン番号。
- Androidアプリの実行方式と互換性の範囲。
- Linux環境の有無、AVFや仮想化方式。
- 最低RAM、ストレージ、CPUなどの要件。
- 既存Chromebookへの移行またはバックポートの対象。
- ChromeOS製品全体の終了時期。
- Gemini機能ごとの端末内処理、クラウド処理、データ保持条件。

## 期待できる点とリスク

| 観点 | 期待できる点 | リスク・未解決点 |
| :--- | :--- | :--- |
| アプリ | Android / Google Playのアプリ資産との連携が期待できる | 大画面、キーボード、マウスへの最適化や具体的な互換性はアプリ・実装ごとに確認が必要 |
| AI | OS全体で文脈に応じた支援を利用できる | 処理場所、送信データ、保持期間を機能ごとに確認する必要がある |
| 端末連携 | スマートフォンのアプリやファイルへアクセスできる | 対応端末、権限、企業管理の要件は未発表部分がある |
| 移行 | AndroidとChromeOSで培われた技術や利用体験が活用される可能性 | 既存端末・周辺機器・業務フローの互換性や移行対象は未確認 |

## 広告ブロックとプライバシー

発売前の段階で特定アプリの組み合わせを「最適構成」と断定することはできません。次の順序で判断します。

1. ブラウザがChrome拡張機能をどの範囲でサポートするか確認する。
2. AndroidのVPN API、プライベートDNS、HTTPS証明書、アプリ単位VPNの実装を確認する。
3. AdGuard for Android、personalDNSfilterなどがGooglebookを正式対応環境に含めるか確認する。
4. ブラウザ内フィルタとDNS・VPNフィルタを重ねる場合は、誤ブロック、二重処理、電池消費、ログの分散を実機で比較する。

AdGuardのフィルタ構文については、製品予測から切り離し、[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)を参照してください。

## 今後確認する項目

- Googleおよび各メーカーの仕様ページ、発売地域、価格。
- 自動更新期限と企業・教育機関向け管理。
- Androidアプリ、Linuxツール、周辺機器の互換性。
- VPN、DNS、証明書、拡張機能に関する制約。
- Geminiのプライバシー説明と管理者向け設定。

## 情報源

### 公式

- [Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)
- [The Android Show: I/O Edition 2026（Google Japan）](https://blog.google/intl/ja-jp/products/android-chrome-play/android-show-io-edition-2026/)
- [Google AI announcements from May 2026](https://blog.google/innovation-and-ai/technology/ai/google-ai-updates-may-2026/)
- [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)

### 報道・背景資料

以下は公式製品仕様ではなく、発表前後のコードネームや移行予測を追うための背景資料として保存します。

- [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
- [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
