# AdGuard converter compatibility review

This file is generated. Latest stable release-note matches are review candidates, not proof that a rule syntax is supported.

## AdGuard Browser Extension 5.5.2.3

- * Unanchored $urltransform patterns do not match query strings in MV3 [#3600](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3600)
- * "$removeparam for all query parameters" blocks whole site [#3602](https://github.com/AdguardTeam/AdguardBrowserExtension/issues/3602)
- ### How to install MV3 stable:
- ### How to install MV3 beta:
- * [Chrome](https://chromewebstore.google.com/detail/adguard-adblocker-mv3-bet/apjcbfpjihpedihablmalmbbhjpklbdf)

## AdGuard for Android 4.13.2

- No converter-relevant keywords detected in the latest stable release notes.

## Required verification before converter changes

1. Confirm behavior in official AdGuard filtering documentation, CoreLibs/Scriptlets source, or a linked upstream issue.
2. Add positive, negative, and false-positive regression tests.
3. Update `config/adguard-converter-capabilities.json` in a reviewed pull request.
4. Rebuild generated filters and run AGLint plus unit tests.
