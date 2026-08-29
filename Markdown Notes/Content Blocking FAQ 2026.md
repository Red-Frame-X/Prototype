# Content Blocking FAQ 2026

コンテンツブロックFAQ（2026年版）

---

本書は、[Yuki2718/adblock2 Wiki「よくある質問」](https://github.com/Yuki2718/adblock2/wiki/%E3%82%88%E3%81%8F%E3%81%82%E3%82%8B%E8%B3%AA%E5%95%8F)で扱われている論点を、2026年8月29日時点の公式ドキュメント・公開ソースコードに照らして再整理した補助資料です。元Wikiは最終更新が2024年4月13日で、一部の製品状況・Manifest V3（MV3）・フィルタ構文に関する説明は現在の状況と一致しません。

本文は第三者Wikiの転載ではなく、現在も有効な設計原則と更新が必要な点を一次情報から再構成しています。

| <div align="center">メタデータ</div> | <div align="center">情報</div> |
| :--- | :--- |
| **Homepage** | [Red-Frame-X/Prototype](https://github.com/Red-Frame-X/Prototype) |
| **License** | CC0-1.0 |
| **Version** | 20260829 |
| **基準日** | 2026-08-29 |

ライセンス、第三者コンテンツの扱いおよび無保証については[`LICENSES.md`](../LICENSES.md)を参照してください。

---

## 1. 2026年時点の結論

### Chromium系ブラウザでは「uBlock Origin」と「uBO Lite」を同一視しない

フル版の **uBlock Origin（uBO）** と、Manifest V3向けの **uBlock Origin Lite（uBOL）** は別実装です。

uBO公式READMEでは、Chromium向けuBOについてChrome Web Storeからの削除日が **2026年8月31日** と明記されています。一方、uBOLはMV3 APIを前提とした独立プロジェクトとして継続されています。

uBOLは宣言的に動作し、ブラウザ側がネットワークルールとCSS/JavaScript注入を処理します。通常のブロック中に常駐プロセスを必要としない設計ですが、uBOと同一の機能セットではありません。サイト権限とフィルタリングモードによって、コスメティックフィルタやスクリプトレットの適用範囲も変わります。

**参照**

- [gorhill/uBlock README](https://github.com/gorhill/uBlock/blob/master/README.md)
- [uBlockOrigin/uBOL-home](https://github.com/uBlockOrigin/uBOL-home)
- [uBO Lite Troubleshooting](https://github.com/uBlockOrigin/uBOL-home/wiki/Troubleshooting)

### Firefoxではフル版uBOが最も機能を利用しやすい

uBO公式はFirefox版について「works best on Firefox」と案内しています。Firefox版ではCNAME uncloaking、IPアドレスに基づくフィルタリング、HTML filteringなど、Chromium系では利用できないか制限される機能があります。

ただし「Firefoxなら常に誤ブロックが少ない」という意味ではありません。高機能であるほど、追加リスト、例外ルール、DNS・プロキシとの組み合わせによって環境差が生じるため、問題発生時はLoggerで原因を切り分けます。

**参照**

- [uBlock Origin works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox)

### AdGuard Browser Extension MV3はDNR固有の制限を持つ

AdGuard Browser ExtensionのMV3版では、DNRの制約によりMV2版と動作が異なります。公式ドキュメントでは、静的・動的・正規表現ルール数の制限、同時に有効化できるフィルタ数の制限、フィルタリングログの精度制約などが明示されています。

また、MV3版ではフィルタ更新の扱いが従来と異なります。DNR形式に組み込まれるルールは、従来のMV2版のように任意のタイミングで完全更新できるとは限りません。カスタムフィルタ・ユーザールールは「構文として正しいか」だけでなく、「DNRへ変換可能か」を確認する必要があります。

**参照**

- [AdGuard ブラウザ拡張機能 MV3対応版](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)

---

## 2. ブロッカーの選択

### Q. ブラウザ内蔵ブロッカーだけで十分か

用途によります。

Brave ShieldsやVivaldiの内蔵ブロッカーは、MV3拡張機能とは別のブラウザ組み込み機能として動作するため、Chromiumの拡張機能API変更だけで停止するものではありません。ただし、uBO・AdGuardと完全に同一の構文・スクリプトレット・デバッグ機能を持つわけではありません。

BraveはShieldsでサードパーティ広告・トラッカー遮断、リソース置換、CNAME uncloaking等を提供しています。Vivaldiも独自のTracker and Ad Blockerを継続して開発しており、2026年にも広告ブロッカー関連の修正が続いています。

したがって、内蔵ブロッカーは「簡易版だから無価値」でも「uBOの完全代替」でもなく、必要な構文互換性・ログ・カスタムルール・保守性で選びます。

**参照**

- [Brave Shields](https://brave.com/shields/)
- [Vivaldi: Manifest v3 update](https://vivaldi.com/blog/manifest-v3-update-vivaldi-is-future-proofed-with-its-built-in-functionality/)
- [Vivaldi Desktop Releases](https://vivaldi.com/blog/desktop/releases/)

### Q. uBOと別のブラウザ用コンテンツブロッカーを同時に使うべきか

原則として避けます。

uBO公式READMEは、uBOを他のコンテンツブロッカーと併用しないよう明示しています。複数のブラウザ拡張型ブロッカーが同じリクエスト、リダイレクト、スクリプトレット、要素隠蔽を別々に処理すると、ブロック結果を増やすよりも、例外処理の無効化、アンチ広告ブロックの誘発、誤ブロックの原因特定困難化につながる場合があります。

**推奨**：ブラウザ内では原則1つの主要コンテンツブロッカーに集約し、必要ならフィルタリストを追加します。

**参照**

- [gorhill/uBlock README](https://github.com/gorhill/uBlock/blob/master/README.md)

### Q. ブラウザブロッカーとDNSブロックを併用してよいか

可能ですが、役割を分離して運用します。

DNSブロックはドメイン名解決の段階で遮断するため、URLパス、DOM要素、スクリプトレット、特定リソース種別などは扱えません。ブラウザブロッカーはページ文脈を使った細かな制御ができます。

そのため、ブラウザブロッカーとDNSブロックの併用は「同じ機能を二重化する」のではなく、異なるレイヤーを組み合わせる構成です。一方、DNS側で先に遮断されるとブラウザ側Loggerに通信が現れず、誤ブロックの原因特定が難しくなることがあります。

トラブルシューティング時は、まずブラウザブロッカー単体またはDNSブロック単体まで構成を簡略化し、問題がどのレイヤーで発生しているか確認します。

**参照**

- [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)

---

## 3. フィルタリストの選択と過剰購読

### Q. フィルタ数が多いほど強力か

単純な件数比較には意味がありません。

uBOでは重複フィルタが除去され、純粋なホスト名フィルタは特に効率よく処理されます。一方で、パターンベースのフィルタ、複数ワイルドカード、正規表現、procedural cosmetic filterなどは設計次第でコストが変わります。

重要なのはルール数ではなく、以下です。

1. 必要な対象へ十分に絞り込まれているか
2. ネットワークフィルタがtokenize可能か
3. 不要な正規表現や複数ワイルドカードを使っていないか
4. procedural filterの評価対象ノードを狭くできているか
5. 既存フィルタとの重複・競合がないか

uBO公式も、追加フィルタリストが増えるほどページ破損の可能性は高まると案内しています。

**参照**

- [uBO Filter Performance](https://github.com/gorhill/uBlock/wiki/Filter-Performance)
- [uBO Dashboard: Filter lists](https://github.com/gorhill/uBlock/wiki/Dashboard%3A-Filter-lists)
- [uBO Procedural cosmetic filters](https://github.com/gorhill/uBlock/wiki/Procedural-cosmetic-filters)

### Q. ホスト名だけのルールは古い・遅いのか

いいえ。用途が合えば最も効率的な部類です。

uBOでは純粋なホスト名フィルタがメモリ・CPUの両面で最適化されています。AdGuard DNSでも、ドメイン遮断はDNSレイヤーの基本です。

ただし、広告やトラッカーがファーストパーティと同一ドメインから配信される場合、ドメイン単位の遮断では正常コンテンツまで巻き込みます。その場合はURL、リソース種別、ドメイン条件、DOM条件など、より狭いブラウザ側ルールを使います。

---

## 4. フィルタ構文の互換性

### Q. uBO用ルールをAdGuardへそのまま貼ってよいか

互換性のある構文も多い一方、完全互換ではありません。

uBO自身もEasyList/ABP構文を基礎にしつつ独自拡張を持ち、AdGuardも独自拡張を持っています。フィルタ作者向けには、対象エンジンの公式リファレンスを基準に確認する必要があります。

特に注意するもの：

- scriptlet名・引数
- redirect resource
- HTML filtering
- procedural cosmetic filter
- action operator（`:style()`, `:remove()`等）
- modifierの対応差
- MV3/DNR変換可否

別エンジン向けルールを移植するときは「見た目が似ている構文」ではなく、同じ副作用と例外処理になるかまで検証します。

**参照**

- [uBO Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [AdGuard Rules syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)

---

## 5. CNAME・DNS・HTTPSフィルタリング

### Q. CNAME uncloakingはすべてのブラウザで同じか

同じではありません。

uBOのCNAME uncloakingは、ブラウザのDNS APIを利用できるFirefoxで提供されています。uBO公式Wikiでは現在もFirefox固有機能として説明されています。

AdGuard for Androidではブラウザ拡張機能とは異なり、OS全体のローカルVPN・DNS保護・HTTPSフィルタリングを組み合わせられるため、比較時は「製品名」ではなく「どのレイヤーで何を処理しているか」を区別します。

**参照**

- [uBlock Origin works best on Firefox](https://github.com/gorhill/uBlock/wiki/uBlock-Origin-works-best-on-Firefox)
- [AdGuard for Android: DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard for Android: Settings / HTTPS filtering](https://adguard.com/kb/adguard-for-android/features/settings/)

---

## 6. アンチ広告ブロックへの対処

### 固定の「万能ルール集」より、再現・報告・最小修正を優先する

アンチ広告ブロック実装は頻繁に変更されます。数年前の特定スクリプト名・DOM構造・タイマー名を前提とした固定ルールは、無効化されるだけでなくサイト破損を生むことがあります。

推奨手順：

1. ブロッカーを複数併用していないことを確認する
2. 追加したサードパーティリストを一時的に減らす
3. Logger / Filtering logで発火ルールを確認する
4. 既存の公式・主要フィルタで対応済みか確認する
5. 未対応なら、対象フィルタのIssue受付先へURL・再現手順・スクリーンショットを添えて報告する
6. 応急処置が必要な場合のみ、サイト限定の最小ルールを作成する

スクリプトレットやHTML filteringは強力ですが、サイト内部実装への依存度が高いため、汎用ルール化は慎重に行います。

---

## 7. 2024年版FAQから明確に更新すべきポイント

| 論点 | 2026年8月29日時点の扱い |
| :--- | :--- |
| Chromium MV3 | 将来予測ではなく現行運用上の制約。uBOとuBOLを明確に分ける |
| Chrome版uBO | 公式READMEでChrome Web Store削除予定日が2026-08-31と明記 |
| uBO Lite | MV3専用の別実装。宣言的処理、権限・モード差を考慮 |
| Brave/Vivaldi | 内蔵ブロッカーは継続開発中。古い2021～2022年時点の能力評価を固定化しない |
| フィルタ性能 | 「数が多い＝重い」ではないが、「何件でも無関係」とも単純化しない。構文・tokenization・対象範囲が重要 |
| `:has()` | 主要ブラウザでネイティブ対応が進み、uBO公式はネイティブ`:has()`を`:upward()`やprocedural `:has()`より効率的と説明 |
| CNAME uncloaking | uBOでは現在もFirefox固有機能として扱う |
| ブロッカー併用 | uBO公式は他のコンテンツブロッカーとの併用を非推奨 |
| DNS併用 | ブラウザブロッカーとは別レイヤー。可否ではなく役割分担と切り分けが重要 |
| アンチ広告ブロック | 固定の古いスクリプトレット例より、最新フィルタ・ログ・最小修正・報告を優先 |

---

## 8. 推奨構成の考え方

### Firefox

- フル版uBOを中心にする
- まず標準フィルタを維持する
- 必要な地域・用途別リストだけ追加する
- DNSブロックを併用する場合は、誤ブロック時に切り離して検証できる構成にする

### Chromium / ChromeOS

- MV3前提でuBO LiteまたはAdGuard Browser Extension MV3等を選ぶ
- uBO Liteではフィルタリングモードとサイト権限を確認する
- AdGuard MV3ではDNR変換・ルール枠・更新方式の制約を意識する
- 「MV2版で使えたルールがMV3でも必ず同じ結果になる」と仮定しない

### Android

- ブラウザだけならFirefox + uBOも有力
- アプリを含む端末全体を対象にするならAdGuard for Android等のシステムレベル製品を検討する
- DNS protectionとHTTPS filteringは別機能として切り分ける

---

## 9. 一次情報

- [gorhill/uBlock](https://github.com/gorhill/uBlock)
- [uBlockOrigin/uBOL-home](https://github.com/uBlockOrigin/uBOL-home)
- [uBO Static filter syntax](https://github.com/gorhill/uBlock/wiki/Static-filter-syntax)
- [uBO Filter Performance](https://github.com/gorhill/uBlock/wiki/Filter-Performance)
- [uBO Dashboard: Filter lists](https://github.com/gorhill/uBlock/wiki/Dashboard%3A-Filter-lists)
- [AdGuard filter syntax](https://adguard.com/kb/general/ad-filtering/create-own-filters/)
- [AdGuard Browser Extension MV3](https://adguard.com/kb/ja/adguard-browser-extension/mv3-version/)
- [AdGuard for Android DNS protection](https://adguard.com/kb/adguard-for-android/features/protection/dns-protection/)
- [AdGuard DNS filtering rules syntax](https://github.com/AdguardTeam/KnowledgeBaseDNS/blob/master/docs/general/dns-filtering-syntax.md)
- [Brave Shields](https://brave.com/shields/)
- [Vivaldi Manifest V3 update](https://vivaldi.com/blog/manifest-v3-update-vivaldi-is-future-proofed-with-its-built-in-functionality/)
