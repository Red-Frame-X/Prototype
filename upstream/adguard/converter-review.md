# AdGuard converter compatibility review

This file is generated. Latest stable release-note matches are review candidates, not proof that a rule syntax is supported.

## AdGuard Browser Extension 5.5.3.3

- In this release we’ve added AdGuard’s Manifest V3 (MV3) Browser Extension to Microsoft Edge.
- But this doesn’t mean AdGuard is leaving the store. This is where our MV3 version comes in.
- ## What changes with MV3
- With MV2, the extension sees each network request in real time and decides what to block. This changes with MV3: the browser receives a prebuilt ruleset and applies it itself.
- This means the number of active rules is limited in MV3, some traditional filtering rules cannot be converted exactly, and most filter updates now ship with the extension itself, so updates can take longer.
- This will allow the MV3 extension to work as intended.
- * Added AdGuard MV3 Extension to Microsoft Edge
- - Updated [@adguard/dnr-converter] to v2.0.0.
- - Updated [@adguard/dnr-rulesets] to v6.0.0.
- ### How to install MV3 stable:
- ### How to install MV3 beta:
- * [Chrome](https://chromewebstore.google.com/detail/adguard-adblocker-mv3-bet/apjcbfpjihpedihablmalmbbhjpklbdf)

## AdGuard for Android 4.14.2

- No converter-relevant keywords detected in the latest stable release notes.

## Required verification before converter changes

1. Confirm behavior in official AdGuard filtering documentation, CoreLibs/Scriptlets source, or a linked upstream issue.
2. Add positive, negative, and false-positive regression tests.
3. Update `config/adguard-converter-capabilities.json` in a reviewed pull request.
4. Rebuild generated filters and run AGLint plus unit tests.
