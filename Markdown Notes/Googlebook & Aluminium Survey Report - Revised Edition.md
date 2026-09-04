# Googlebook / Aluminium 調査メモ

Googleが2026年5月に発表した「Googlebook」と、発表前に報道された開発コードネーム「Aluminium」について、自分が確認した情報を後から追えるよう整理した個人用の調査記録です。

> [!NOTE]
> この文書は購入判断や将来の再確認に使う個人メモであり、一般向けの製品ガイドや購入推奨を目的としていません。下書きはChatGPTで推敲・整理しているため、専門性・正確性・完全性を保証しません。発売前情報は特に変化しやすいため、使用時点のGoogle公式発表と製品ページを再確認します。

| メタデータ | 情報 |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260904 |

ライセンス、第三者コンテンツの扱いおよび無保証は[`LICENSES.md`](../LICENSES.md)に記録しています。

> [!IMPORTANT]
> Googlebookは発売前です。自分のメモ内でも公式発表、報道、推測を区別し、仕様を確定情報として先取りしません。

## 現時点の整理

Googlebookは、Androidのアプリ基盤とChromeOSのブラウザ体験を組み合わせ、Gemini Intelligenceを中核に据えた新しいノートPCカテゴリです。Googleは2026年秋の投入を予告していますが、2026年8月22日時点の公式紹介では、個別メーカー、価格、対応地域、CPU、最低RAM、Linux実行方式、既存Chromebookの移行対象を公表していません。

「Aluminium」は求人情報などから報道されたAndroidベースPCプロジェクトのコードネームです。Googleの製品発表は「Googlebook」を使用しており、「Aluminium OS」または「ALOS」を正式な製品名としていません。

## 確認できた情報

Google公式発表で確認できる主な内容を記録します。

- AndroidとChromeOSの長所を取り入れた新しいノートPCカテゴリ。
- Geminiの文脈提案をカーソルから呼び出す「Magic Pointer」。
- 指示からダッシュボードを作る「Create your Widget」。
- Androidスマートフォン上のアプリやファイルとの連携。
- 主要パートナーによるプレミアムハードウェアと、2026年秋の投入予定。

## 未確認・未発表として残している事項

- ベースとなるAndroidのバージョン番号。
- Androidアプリの実行方式と互換性の範囲。
- Linux環境の有無、AVFや仮想化方式。
- 最低RAM、ストレージ、CPUなどの要件。
- 既存Chromebookへの移行またはバックポートの対象。
- ChromeOS製品の終了時期。
- Gemini機能ごとの端末内処理、クラウド処理、データ保持条件。

## 自分の判断材料としての利点とリスク

| 観点 | 期待できる点 | リスク・未解決点 |
| :--- | :--- | :--- |
| アプリ | Google Playのアプリ資産を活用できる | 大画面、キーボード、マウスへの最適化はアプリごとに異なる |
| AI | OS全体で文脈に応じた支援を利用できる | 処理場所、送信データ、保持期間を機能ごとに確認する必要がある |
| 端末連携 | スマートフォンのアプリやファイルへアクセスできる | 対応端末、権限、企業管理の要件は未発表 |
| 移行 | AndroidとChromeOSの資産を統合できる可能性 | 既存端末・周辺機器・業務フローの互換性は未確認 |

## 広告ブロックとプライバシーの確認メモ

発売前の段階で特定アプリの組み合わせを「最適構成」と断定しません。自分が実機を検討するときは、次の順序で確認します。

1. ブラウザがChrome拡張機能をどの範囲でサポートするか確認する。
2. AndroidのVPN API、プライベートDNS、HTTPS証明書、アプリ単位VPNの実装を確認する。
3. AdGuard for Android、personalDNSfilterなどがGooglebookを正式対応環境に含めるか確認する。
4. ブラウザ内フィルタとDNS・VPNフィルタを重ねる場合は、誤ブロック、二重処理、電池消費、ログの分散を実機で比較する。

AdGuardのフィルタ構文については、製品予測から切り離し、[`AdGuard Custom Rules Reference.md`](AdGuard%20Custom%20Rules%20Reference.md)に記録しています。

## 今後自分で確認する項目

- Googleおよび各メーカーの仕様ページ、発売地域、価格。
- 自動更新期限と企業・教育機関向け管理。
- Androidアプリ、Linuxツール、周辺機器の互換性。
- VPN、DNS、証明書、拡張機能に関する制約。
- Geminiのプライバシー説明と管理者向け設定。

## 参照した情報源

### 公式

- [Introducing Googlebook, designed for Gemini Intelligence](https://blog.google/products-and-platforms/platforms/android/meet-googlebook/)
- [The Android Show: I/O Edition 2026（Google Japan）](https://blog.google/intl/ja-jp/products/android-chrome-play/android-show-io-edition-2026/)
- [Chromebookの自動更新ポリシー](https://support.google.com/chrome/a/answer/6220366?hl=ja)

### 報道・背景資料

- [Google listing says Android PC OS, ‘Aluminium,’ will have ‘AI at the core’](https://9to5google.com/2025/11/24/google-android-pc-aluminium-os/)
- [For Aluminium OS to succeed, Google needs to avoid Android's earliest mistakes](https://www.androidauthority.com/google-aluminium-os-avoid-android-early-mistakes-3663293/)
