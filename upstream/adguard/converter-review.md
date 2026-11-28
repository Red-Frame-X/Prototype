# AdGuard変換処理の互換性確認

このファイルは自動生成されます。以下は最新安定版のリリースノートから抽出した確認候補の原文であり、ルール構文の対応を証明するものではありません。

## AdGuard Browser Extension 5.6.2

- ![Chrome MV3](https://img.shields.io/badge/Chrome%20MV3%3A%20Published%205%25-purple)
- ![Edge MV3](https://img.shields.io/badge/Edge%20MV3%3A%20In%20review-yellow)
- > In the Manifest V3 extension, *Block fingerprinting* requires an extra browser permission. To use this feature, enable the *Allow user scripts* toggle in your AdGuard browser settings.
- * **Manifest V2 only:** This feature applies specifically to the MV2 extension. (In Manifest V3, language-specific filters are automatically handled based on your browser’s preferred language settings).
- Managing custom filtering rules is now significantly more convenient. You can now add new rules directly in the user rules list: using the *Create rule* button without switching to the editor view and pasting multi-line text from the clipboard automatically splits it into separate lines. In addition, existing rules and comment blocks can now be edited right in the list, making quick adjustments faster and easier.
- * Added support for exception rules with the new `$stealth=fingerprinting` modifier to disable fingerprinting protection on specific websites
- * Improved MV3 startup performance: only rulesets for enabled filters are prepared at launch (with the rest processed in the background), eliminating redundant filter preparation on subsequent starts
- * Added partial support for `$csp` exception rules in MV3 [#2965](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2965)
- * `$badfilter` rules cancelled other rules regardless of modifier values (`$removeparam`, `$csp`, `$header`, `$method`, `$to`, etc.), causing valid rules with different values to silently stop applying. In addition, rules that only appeared identical after parsing cancelled each other, and case-sensitive `$domain` regexps incorrectly lost their case (e.g. `$domain=/A/` cancelled `$domain=/a/`)
- * In MV3, filters without an available ruleset were displayed on the options page, where toggles reverted without an explanation
- * In MV3, a custom filter whose patch files became unavailable could stay outdated after a manual update [#3560](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3560)
- * Cosmetic rules with multiple domains in the `$domain` modifier did not apply on permitted domains [#3605](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3605)
- * Cosmetic rule matches were duplicated for overlapping domain restrictions [#3605](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3605)
- * Named `$removeparam` rules failed to remove the first query parameter before MV3 requests [#3615](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3615)
- * `$badfilter` rules with the `$permissions` modifier disabled all `$permissions` rules regardless of their modifier values [#2961](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/2961)
- * Domain-scoped cosmetic and JavaScript rules were not applied on hosts with labels ending in an underscore (e.g. `lorenne_.wehype.app`)
- * In MV3, the warning about reaching the active built-in rules limit showed the built-in filters message instead of the rules message
- * In MV3, the rule limits warning did not appear when session rules exceeded the browser quota
- ### TSUrlFilter (AdGuard Browser Extension filtering engine)
- ### Scriptlets (JavaScript enhancement for filtering rules)
- * Updated [@adguard/scriptlets](https://github.com/AdguardTeam/scriptlets) to v2.6.0
- ### How to install MV3 stable:
- ### How to install MV3 beta:
- * [Chrome](https://chromewebstore.google.com/detail/adguard-adblocker-mv3-bet/apjcbfpjihpedihablmalmbbhjpklbdf)

## AdGuard for Android 4.16.1

- 最新安定版のリリースノートに、変換処理に関係するキーワードはありませんでした。

## 変換処理を変更する前に必要な確認

1. AdGuardフィルタリングの公式文書、CoreLibs・Scriptletsのソース、または関連するUpstreamのIssueで動作を確認します。
2. 正常系・異常系・誤検出の回帰テストを追加します。
3. Review済みのPull Requestで`config/adguard-converter-capabilities.json`を更新します。
4. 生成Filterを再Buildし、AGLintと単体テストを実行します。
