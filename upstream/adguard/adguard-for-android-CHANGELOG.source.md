# AdGuard for Android changelog mirror

> Source: https://api.github.com/repos/AdguardTeam/AdguardForAndroid/releases?per_page=100
> Generated from official GitHub Releases; newest release first.

## 4.13.1

- Published: 2026-08-03T16:50:17Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13.1

We recently released AdGuard for Android v4.13, and now we’re following up with a quick hotfix to address a couple of bugs.

Please note that for Integration mode to work properly, you need to update both AdGuard and AdGuard VPN to their latest versions.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.13

- Published: 2026-07-28T14:04:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13

Please welcome the much anticipated AdGuard for Android v4.13! We set ambitious goals for this release, and did our best to deliver: a lot of work was done both in terms of big features as well as the usual behind the scenes routine of fixing bugs and oiling gears for a better performance. Let’s see the details below.

With this release, we introduced differential filter updates to AdGuard for Android! To achieve this, we integrated the FiltersListManager library into the app. Now, your filters will load automatically without consuming tons of traffic and overloading servers.

We also added post-quantum cryptography support to DnsLibs. Now AdGuard for Android, like our other full ad-blocking products, keeps your DNS requests protected against future threats.

Another significant change is our adoption of CRLite by Mozilla to verify revoked certificates. Using this instead of the more outdated OCSP (Online Certificate Status Protocol) or letting the app check each certificate against the CRL (Certificate Revocation List) not only speeds up website loading, but also increases your privacy and safety while browsing.

To improve security in Integration mode with AdGuard VPN, we changed the connection protocol, introducing the use of credentials. With the release of AdGuard for Android v4.13, our ad blocker and VPN cooperate seamlessly and securely, with no additional action required on the user’s part for them to synchronize. No third-party apps will be able to spy on your activities, as an added bonus.

In previous versions, in-app instructions for installing HTTPS certificates were added, as the process could differ in regards to your device’s make and model. In AdGuard for Android 4.13, we added support for ColorOS (Oppo) to those instructions.

And last, but not least, we have done a lot of work on our filtering engines and fixed bugs that had accumulated over time. Scriptlets and CoreLibs were updated for better app performance.

You can consult the changelog below to see all the fixes and improvements.

## Changelog


### Improvements
* Added possibility to copy an applied rule in request details in the filtering log [5637](https://github.com/AdguardTeam/AdguardForAndroid/issues/5637)
* Added support for Google Backup [5879](https://github.com/AdguardTeam/AdguardForAndroid/issues/5879)
* Excluded 2ndLine application from filtering by default [5116](https://github.com/AdguardTeam/AdguardForAndroid/issues/5116)
* Displayed information about updated DNS filters in the DNS list [5519](https://github.com/AdguardTeam/AdguardForAndroid/issues/5519)
* Added possibility to copy package_name in request details in the filtering log [5636](https://github.com/AdguardTeam/AdguardForAndroid/issues/5636)
* Improved the *Check for updates* button’s behavior on the update check screen [5923](https://github.com/AdguardTeam/AdguardForAndroid/issues/5923)
* Eliminated the possibility to add an empty user rule through the recent activity tab [5193](https://github.com/AdguardTeam/AdguardForAndroid/issues/5193)
* Added color distinction for updated content on the *Updates* screen [5886](https://github.com/AdguardTeam/AdguardForAndroid/issues/5886)
* Improved voicing of TalkBack voice assistant elements for *Private browser*
* Restructured the inputs/dialogs in *Tracking protection*
* Updated crash reports and app usage data names and dialogs
* Added the option to find requests by applied rules in recent activity
* Added validation to *Mask your IP* address screen
* Added auto-refreshing of the webpage after toggling the *Website protection* switch for it in *Private browser*
* Added authentication for the local proxy
* Added possibility to clear `.hprof` when it’s not needed
* Added an app update error screen for TV
* Improved video playback in the YouTube player in the background and picture-in-picture (PiP) mode

### Fixes
* A blocking rule for the `$network` type is added via the *Add allowing rule* button in request details [5390](https://github.com/AdguardTeam/AdguardForAndroid/issues/5390)
* The *Disable all?* popup appears on the *User rules* screen even if the rules list is empty [5175](https://github.com/AdguardTeam/AdguardForAndroid/issues/5175)
* CA certificate installation instructions are not relevant for ColorOS [5827](https://github.com/AdguardTeam/AdguardForAndroid/issues/5827)
* DNS filters shows `null` instead of the time of the last update [5902](https://github.com/AdguardTeam/AdguardForAndroid/issues/5902)
* Firewall is activated automatically after granting the *Usage access* system permission [5927](https://github.com/AdguardTeam/AdguardForAndroid/issues/5927)
* High battery consumption starting from v4.12 [5893](https://github.com/AdguardTeam/AdguardForAndroid/issues/5893)
* Impossible to block a domain, unblocked in DNS filter, using the filtering log only [5880](https://github.com/AdguardTeam/AdguardForAndroid/issues/5880)
* Incorrect subdomains appear in statistics [5868](https://github.com/AdguardTeam/AdguardForAndroid/issues/5868)
* Many apps stop working when AdGuard is active [5617](https://github.com/AdguardTeam/AdguardForAndroid/issues/5617)
* Recent activity log lags heavily after updating to v4.12.1 [5882](https://github.com/AdguardTeam/AdguardForAndroid/issues/5882)
* Problems while editing extensions in language modes other than English [5914](https://github.com/AdguardTeam/AdguardForAndroid/issues/5914)
* Recent activity log fails to be cleared instantly in AdGuard v4.14 nightly 4 [5908](https://github.com/AdguardTeam/AdguardForAndroid/issues/5908)
* Subdomains duplicate in *Statistics* [5840](https://github.com/AdguardTeam/AdguardForAndroid/issues/5840)
* The custom DNS server disappears after importing settings that were just exported [5892](https://github.com/AdguardTeam/AdguardForAndroid/issues/5892)
* The title of videos doesn’t minimize when clicking the share button while in horizontal mode [5612](https://github.com/AdguardTeam/AdguardForAndroid/issues/5612)
* Turning on AdGuard using tile closes the notification panel [5915](https://github.com/AdguardTeam/AdguardForAndroid/issues/5915)
* Filters update without authorization [5309](https://github.com/AdguardTeam/AdguardForAndroid/issues/5309)
* User regex in *Ad blocking* and *DNS filtering* rules breaks after AdGuard v4.14 nightly 5 [5916](https://github.com/AdguardTeam/AdguardForAndroid/issues/5916)
* When attempting to update a beta version (e.g. RC), the update proceeds to the latest release version [5920](https://github.com/AdguardTeam/AdguardForAndroid/issues/5920)
* Configuration can’t be imported via link, even if the versions are consistent [5912](https://github.com/AdguardTeam/AdguardForAndroid/issues/5912)
* Rules duplicate themselves in the *Applied rules* section
* Failed to move the AdGuard Personal CA to the system store via the *Move* button in the app
* Custom content filter lists disappear after time
* Protection resumes every few seconds with *HTTPS filtering* and *FakeDNS* enabled
* An error snack appears after editing a userscript 
* The switch on the Extensions setting does not respond when tapping the setting name 
* After rebooting the phone, blocked URLs no longer show the reason why they were blocked in the log
* The *Protection may not work properly while the hotspot is active* notification is displayed for Android 10+
* Impossible to add a blocking rule with additional modifiers from *Recent activity*
* Impossible to select a custom DNS server by tapping *Save and select*
* Actual DNS protocol doesn’t match with what is shown on the *DNS server details* screen after settings import
* Empty space below the navigation bar after opening extensions editor
* AdGuard does not start after reboot
* Incorrect display of onboarding for certificate installation when importing settings via a link
* Integration mode dialogue doesn’t open consistently at app’s first launch
* Search query is not displayed on the *Recent activity* screen if the header was not collapsed after returning from request details
* The *Open* button for DNS providers opens the browser but not the website on Xiaomi TV Box
* The *Can’t update license info* snack is not displayed on the *TV license* screen after license check timeout
* Focus reset to default after pressing the *Refresh status* button on the *License* screen on TV
* The *Certificate wasn’t installed* dialog is shown after certificate installation via settings sharing
* Custom filter version is not updated after the filter update
* Text clipping, header overlap, and content being covered by the keyboard in *Rule editor*
* The YouTube button in the AdGuard player restarts video 
* On the *Quick actions* screen firewall notifications are displayed for both blocked and allowed apps when the *Show blocked only* filter is selected
* Scrolling *User rules* overlaps another view
* Scroll focus moves out of viewport during rapid scrolling of *App management* on TV
* Sharing from YouTube Music to AdGuard player doesn’t work
* AdGuard’s notification brings the device’s screen out of sleep mode
* *Private browser* does not open other apps from webpages
* Filter rule editor accepts any non-empty string as valid rule without syntax validation
* Dynamic theme does not apply to the AdGuard app after closing *Private browser*

* With Kazakh or Kyrgyz as system language, AdGuard erroneously displays it as Russian
* The number of blocked requests is displayed incorrectly in notifications in languages ​​that use hieroglyphs

### DnsLibs (DNS filtering engine)
* Updated DnsLibs to v2.8.45 [5961](https://github.com/AdguardTeam/AdguardForAndroid/issues/5961)

#### Improvements
* Added Post-Quantum cryptography support to DnsLibs [245](https://github.com/AdguardTeam/DnsLibs/issues/245)
* Added an option to remove `h3` from the `alpn` parameter of HTTPS RR [257](https://github.com/AdguardTeam/DnsLibs/issues/257)
 * Improved reliability of testing DoT upstream availability [263](https://github.com/AdguardTeam/DnsLibs/issues/263)
* Improved DNS upstream list updates without reloading filters [248](https://github.com/AdguardTeam/DnsLibs/issues/248)

#### Fixes
* DNS unblocking rule does not work
* At times system:// upstream replies failed to be accepted on Android [265](https://github.com/AdguardTeam/DnsLibs/issues/265)
* Missing AdGuard certificate on some websites such as hitomi.la [2055](https://github.com/AdguardTeam/CoreLibs/issues/2055)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.21.38

#### Improvements
* Added support for decoding URLs in `$urltransform` [1915](https://github.com/AdguardTeam/CoreLibs/issues/1915)
* Enabled HTTP/3 filtering by default in beta/nightly builds [2014](https://github.com/AdguardTeam/CoreLibs/issues/2014)
* Added support for example.org/path cosmetic rules [2012](https://github.com/AdguardTeam/CoreLibs/issues/2012)
* Added support for the new `$reason` modifier [1986](https://github.com/AdguardTeam/CoreLibs/issues/1986)
* Improved *Do Not Track* behavior [1982](https://github.com/AdguardTeam/CoreLibs/issues/1982)
* Prevented local.adguard.org DNS leakage after enabling protection [1854](https://github.com/AdguardTeam/CoreLibs/issues/1854)
* Enabled HTTP/3 filtering by default in stable builds [2015](https://github.com/AdguardTeam/CoreLibs/issues/2015)

#### Fixes
* Incorrect certificate serial number marshalling leads to false positive CRLite matches [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* There is no AdGuard certificate if the advanced option *Check websites’ certificate transparency* is enabled [2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* Connection resets on CoreLibs v1.19 
* Localhost is unreachable in manual proxy mode in v1.19 [2019](https://github.com/AdguardTeam/CoreLibs/issues/2019)
* Incorrect destination address is shown in *Request details* when integration with AdGuard VPN is enabled [2021](https://github.com/AdguardTeam/CoreLibs/issues/2021)
* Userscript import failure caused by BOM [2009](https://github.com/AdguardTeam/CoreLibs/issues/2009)
* Broken injections when FakeDNS is used in proxy settings [2017](https://github.com/AdguardTeam/CoreLibs/issues/2017)
* Broken handling of closing script tags with spaces [2042](https://github.com/AdguardTeam/CoreLibs/issues/2042)
* Incorrect `$generichide` behavior for domain-scoped rules [2041](https://github.com/AdguardTeam/CoreLibs/issues/2041)
* High latency in QUIC/HTTP/3 filtering causes protocol fallback to HTTP/2 [2062](https://github.com/AdguardTeam/CoreLibs/issues/2062)

### Scriptlets (JavaScript enhancement for filtering rules)
* Updated Scriptlets to v2.2.16

#### Improvements
* Added new scriptlet — `prevent-innerHTML` [488](https://github.com/AdguardTeam/Scriptlets/issues/488)
* Improved `fingerprintjs2` — support window [541](https://github.com/AdguardTeam/Scriptlets/issues/541)
* Added a parameter to increase duration of the `trusted-click-element` scriptlet’s execution duration [400](https://github.com/AdguardTeam/Scriptlets/issues/400)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12.3

- Published: 2026-02-20T18:11:04Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.3

This is a technical update aimed to increase the app stability and fix minor bugs.

## Changelog

### Fixes
* No internet access when protection is enabled [#5897](https://github.com/AdguardTeam/AdguardForAndroid/issues/5897)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.19.48 [#6011](https://github.com/AdguardTeam/AdguardForAndroid/issues/6011)

### Scriptlets (JavaScript enhancement for filtering rules)

* Updated Scriptlets to v2.2.10

### Improvements
* Improve 'href-sanitizer ' — support uBO arguments [#493](https://github.com/AdguardTeam/Scriptlets/issues/493)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12.2

- Published: 2025-12-12T17:57:02Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.2

This is a technical update aimed to increase the app stability and fix minor bugs.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12.1

- Published: 2025-10-14T09:37:46Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12.1

We found two bugs after the latest update of AdGuard for Android: the app didn’t launch automatically and filters stopped auto-updating for some users. We are now rolling out a quick fix to address these issues and get your ad-blocking back to normal.

## Changelog

### Fixes
* The app stopped launching at system startup
 [#5862](https://github.com/AdguardTeam/AdguardForAndroid/issues/5862)
* Auto-update of filters doesn’t work
 [#5866](https://github.com/AdguardTeam/AdguardForAndroid/issues/5866)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12

- Published: 2025-10-01T18:40:48Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12

With this release, using AdGuard for Android on tablets has become more convenient — thanks to everyone who voted for the landscape mode. We’ve also added the new *Share settings* feature and made improvements to CoreLibs. Read more about the new features below and don’t forget to update to version 4.12!
## Landscape mode
As we always say, your feedback is really important to us, and this time we’ve added one of the most requested features — landscape mode. Using AdGuard on a tablet is now even more convenient.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/tablet_en.png" width="700">
</p>

Some screens still need polishing, but we’re actively working on them!

## Share settings

We’ve also added the Share settings feature. Now you don’t need to reconfigure everything on a new device or spend time describing your settings when reporting a missed ad — just share a link or scan a QR code.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/share_en.png" width="300">
</p>

To share your settings, go to Settings → Menu (⋮) → Share settings. If someone sends you a link, just open it in a browser and tap Import.

## CoreLibs 

The new CoreLibs release includes bug fixes and various improvements. For example, userscripts now work more reliably on [SPA (Single Page Application) websites](https://en.wikipedia.org/wiki/Single-page_application). Check the changelog for full details.

## Changelog

### Improvements
* Disabled “Route traffic through AdGuard” option for com.bKash.customerapp to ensure the app works correctly [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### Fixes
* CA certificate installation instructions are not relevant for Honor [#5779](https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* Impossible to add app-specific HTTPS exclusion [#5290](https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* Custom DNS filter is not shown in the Update section [#5821](https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* Tapping the cross on the snackbar about downloading a new app version doesn’t stop the download [#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* Some images are missing in a banking app due to AdGuard filtering [#5819](https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### Improvements
* Improved the `$app` modifier: added support for wildcards and regexps
[#1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* Added support for ALPS extension [#1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### Fixes
* Wrong tracking protection option shown in the log [#5739](https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* Filtering disabled on some websites due to performance warnings (new.lewd.ninja) [#1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* “Use FakeDNS” option in Proxy Server interrupts the connection of bypassed apps [#5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* Some extensions do not work after update to v2.17 [#1993](https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHR timeout with the `immersivetranslate` userscript [#2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* Content-type modifiers do not work with the `$urltransform` modifier [#1978](https://github.com/AdguardTeam/CoreLibs/issues/1978)
* DNS filters do not apply [#5851](https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### DnsLibs (DNS filtering engine)

* Updated DnsLibs to v2.6.20 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### Scriptlets (JavaScript enhancement for filtering rules)

* Updated Scriptlets to v2.2.9

#### Improvements
* Added a new scriptlet  — 'trusted-replace-argument' [#405](https://github.com/AdguardTeam/Scriptlets/issues/405)

#### Fixes
* 'prevent-element-src-loading' — TrustedScriptURL is not defined in Firefox  [#514](https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — quotes are escaped incorrectly [#517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* Compilation error in Safari 15 due to unsupported regex lookbehind [#519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.11

- Published: 2025-08-26T15:38:16Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.11

This release includes some under-the-hood improvements, a substantial number of bug fixes, and a CoreLibs update. As a result, overall app stability has been significantly improved.

## Changelog

### Fixes
* The Create button overlaps the checkbox on the trial activation screen [#5039](https://github.com/AdguardTeam/AdguardForAndroid/issues/5039)
* AdGuard player doesn’t open when sharing a video from the YouTube app [#5780](https://github.com/AdguardTeam/AdguardForAndroid/issues/5780)
* AdGuard identifies AdGuard VPN as a third-party VPN in Integration mode [#5567](https://github.com/AdguardTeam/AdguardForAndroid/issues/5567)
* Apps excluded by UID are routed through AdGuard [#5731](https://github.com/AdguardTeam/AdguardForAndroid/issues/5731)
* Invalid filter update date format for Japanese, Korean, and Chinese [#5703](https://github.com/AdguardTeam/AdguardForAndroid/issues/5703)
* Missing string for private browser notification [#5741](https://github.com/AdguardTeam/AdguardForAndroid/issues/5741)
* Private browser onboarding is displayed twice [#5752](https://github.com/AdguardTeam/AdguardForAndroid/issues/5752)
* Private browser crashes after tapping browser settings [#5781](https://github.com/AdguardTeam/AdguardForAndroid/issues/5781)
* The “Nothing found” warning is missing on some screens [#5038](https://github.com/AdguardTeam/AdguardForAndroid/issues/5038)
* The “Apps operating through proxy” screen is displayed in gray in Integration mode [#5732](https://github.com/AdguardTeam/AdguardForAndroid/issues/5732)
* The app asks for permission to run in the background even though permission has already been granted [#5560](https://github.com/AdguardTeam/AdguardForAndroid/issues/5560)
* Titles and descriptions of DNS servers, extensions, and filters are translated into the system language if a different language is selected in AdGuard [#5709](https://github.com/AdguardTeam/AdguardForAndroid/issues/5709)
* Two similar graphs can be displayed at the same time [#4915](https://github.com/AdguardTeam/AdguardForAndroid/issues/4915)
* The app icon does not fill the designed area on the Amazon Fire TV Stick 4K Max [#5476](https://github.com/AdguardTeam/AdguardForAndroid/issues/5476)
* `com.carshering` is broken when routed through AdGuard [#5464](https://github.com/AdguardTeam/AdguardForAndroid/issues/5464)
* Rules don’t get removed from the firewall after tapping “Remove rule” [#5613](https://github.com/AdguardTeam/AdguardForAndroid/issues/5613)

### CoreLibs (Filtering engine)

* CoreLibs updated to v1.18.28 [#5792](https://github.com/AdguardTeam/AdguardForAndroid/issues/5792)

#### Improvements

* Added support for ABP’s CSS injection syntax [#1927](https://github.com/AdguardTeam/CoreLibs/issues/1927)
* Added permission to remove content with empty attribute [#1934](https://github.com/AdguardTeam/CoreLibs/issues/1934)
* Improved content script performance by using the browser cache properly [#1929](https://github.com/AdguardTeam/CoreLibs/issues/1929)
* Improved performance of content script loading [#1930](https://github.com/AdguardTeam/CoreLibs/issues/1930)
* Removed complicated logic for the `$domain` modifier [#1875](https://github.com/AdguardTeam/CoreLibs/issues/1875)
* Added encoding support for “zstd” [#1976](https://github.com/AdguardTeam/CoreLibs/issues/1976)

#### Fixes

* `$removeparam` does not work when paired with the `$domain` modifier [#1999](https://github.com/AdguardTeam/CoreLibs/issues/1999)
* Some React-based sites aren’t loaded correctly due to “Minified React error” [#1953](https://github.com/AdguardTeam/CoreLibs/issues/1953)
* `urltransform` combined with `$~3p` doesn’t modify the request URL if it’s opened directly in the address bar [#1931](https://github.com/AdguardTeam/CoreLibs/issues/1931)
* `paramountplus.com` is broken [#1937](https://github.com/AdguardTeam/CoreLibs/issues/1937)
* `dailydot.com` is continually reloading [#1925](https://github.com/AdguardTeam/CoreLibs/issues/1925)
* Content script is not injected in `www.huya.com` [#1897](https://github.com/AdguardTeam/CoreLibs/issues/1897)
* Error in content script when the `$jsinject` exception is applied [#1960](https://github.com/AdguardTeam/CoreLibs/issues/1960)

### Scriptlets (JavaScript enhancement for filtering rules)
* Scriptlets updated to v2.2.8

#### Improvements

* Add more examples to scriptlet docs [#392](https://github.com/AdguardTeam/Scriptlets/issues/392)
* Add new scriptlet — 'trusted-replace-argument' [#405](https://github.com/AdguardTeam/Scriptlets/issues/405)
* Improve 'prevent-fetch' — add ability to set random response content [#416](https://github.com/AdguardTeam/Scriptlets/issues/416)
* Improve 'set-cookie' — add an empty object value [#497](https://github.com/AdguardTeam/Scriptlets/issues/497)
* Update AGTree to v3 [#247](https://github.com/AdguardTeam/AGLint/issues/247)

#### Fixes
* Fix 'inject-css-in-shadow-dom' — scriptlet does not work if adoptedStyleSheets is overridden [#477](https://github.com/AdguardTeam/Scriptlets/issues/477)
* Fix 'json-prune' — handle 'null' values while checking specified key in object [#504](https://github.com/AdguardTeam/Scriptlets/issues/504)
* Fix 'prevent-element-src-loading' —  TrustedScriptURL is not defined in Firefox [#514](https://github.com/AdguardTeam/Scriptlets/issues/514)
* Fix 'spoof-css' — DOMRect is set incorrectly [#498](https://github.com/AdguardTeam/Scriptlets/issues/498)
* Fix 'trusted-replace-node-text' — output literal quotes for escaped quotes [#440](https://github.com/AdguardTeam/Scriptlets/issues/440)
* Fix 'trusted-replace-node-text' — some quotes are incorrectly escaped [#517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* Fix 'trusted-set-cookie-reload' — prevent infinite reload for constantly changing values [#489](https://github.com/AdguardTeam/Scriptlets/issues/489)
* Fix 'trusted-suppress-native-method' — reset 'isMatchingSuspended' when stack is not matched [#496](https://github.com/AdguardTeam/Scriptlets/issues/496)
* Fix scriptlets compilation error in Safari 15 due to unsupported regex lookbehind [#519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.10

- Published: 2025-06-25T17:22:52Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.10

AdGuard for Android v4.10 introduces important improvements to the HTTPS certificate installation process, making it more intuitive and accessible for users. 

When you install AdGuard and launch the app for the first time, you’re prompted to install an HTTPS certificate. This step is essential because the certificate plays a key role in ensuring effective ad filtering in browsers. Without it, filtering quality is significantly reduced. That’s why it’s crucial for all users, beginner or advanced, to be able to complete the installation without difficulty.

We knew there was room for improvement in the whole process — the previous instructions often didn’t reflect the actual settings found on devices from different manufacturers, and there was also a bug that prevented users from returning to the instructions after leaving the app.

To address these issues, we’ve added in-app guides for the most common devices — including Google Pixel, Samsung, Huawei, Xiaomi, and OnePlus — with adjustments based on Android OS version and user locale. We’ve also fixed the bug mentioned above.

## Changelog

### Improvements
* Added HTTPS filtering by default for the Lemur browser [#5577](https://github.com/AdguardTeam/AdguardForAndroid/issues/5577)

### Fixes
* AdGuard gets disabled when WebView is stopped or updated [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)
* After integration with Tor, Tor via Orbot isn’t the default proxy [#4908](https://github.com/AdguardTeam/AdguardForAndroid/issues/4908)
* Updated filters aren’t displayed after the app is restarted [#5638](https://github.com/AdguardTeam/AdguardForAndroid/issues/5638)
* QUIC filtering is disabled for WeChat and AliExpress [#5497](https://github.com/AdguardTeam/AdguardForAndroid/issues/5497)
* WeChat is excluded from HTTPS filtering by default [#5689](https://github.com/AdguardTeam/AdguardForAndroid/issues/5689)
* The app is not fully translated [#5418](https://github.com/AdguardTeam/AdguardForAndroid/issues/5418)
* Filtering status is not saved if it’s changed twice [#5701](https://github.com/AdguardTeam/AdguardForAndroid/issues/5701)
* Recent activity log lags when scrolling slowly [#5369](https://github.com/AdguardTeam/AdguardForAndroid/issues/5369)
* Some parameters are not included in the link when reporting an incorrect blocking [#5520](https://github.com/AdguardTeam/AdguardForAndroid/issues/5520)
* When opening a link in a browser, two AdGuard apps appear in the list of browsers, and one of which does not work as expected [#5592](https://github.com/AdguardTeam/AdguardForAndroid/issues/5592)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.17.157 [#5725](https://github.com/AdguardTeam/AdguardForAndroid/issues/5725)

#### Fixes
* Naver Smartstore cannot be accessed properly [#1971](https://github.com/AdguardTeam/CoreLibs/issues/1971)
* Some React-based websites aren’t loaded correctly due to a `Minified React error` [#1953](https://github.com/AdguardTeam/CoreLibs/issues/1953)
* User rule for domains does not block the request completely [#5539](https://github.com/AdguardTeam/AdguardForAndroid/issues/5539)

### DnsLibs (DNS filtering engine)
* DnsLibs updated to v2.6.6 [#5724](https://github.com/AdguardTeam/AdguardForAndroid/issues/5724)

### Scriptlets (JavaScript enhancement for filtering rules) 
* Scriptlets updated to v2.1.7

#### Improvements
*  ’prevent-addEventListener’ — added ability to match specific element [#480](https://github.com/AdguardTeam/Scriptlets/issues/480)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.9

- Published: 2025-04-03T18:22:43Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9

We’ve added a major feature in AdGuard v4.9 for Android: native support for userstyles. This feature has been available in AdGuard for Windows and AdGuard for Mac for a while, and now we are bringing it to AdGuard for Android!

Userstyles are similar to userscripts in a way, but they only focus on changing the appearance of websites using CSS, without getting into their code. Now customizing websites — like adding a dark theme — becomes an easy task. You can create your own userstyles in the app itself, or install ready-made styles from trusted [online sources](https://userstyles.world/).

![Wikipedia with a userstyle](https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.9/styled_wikipedia.jpg)

To add a userstyle, go to *Settings* → *Filtering* → *Extensions*→ *Add extension* → *Import from file or URL*. To create your own style, tap *Add extension* → *Create userstyle*.

![Install userstyle in app](https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.9/Userstyles_en.jpg)

Also, some users might have recently faced a bug that was increasing statistics to ridiculously huge values. We fixed the issue, and once you install AdGuard v4.9 for Android, you will see normal numbers in the *Statistics* tab. 

> Please note that statistics accumulated earlier than the last 24 hours will be heavily pruned.

Aside from this serious issue, we have also worked on fixing smaller bugs. As always, we’ve updated CoreLibs and Scriptlets for better functionality of the app.

## Changelog

### Improvements
* Added support for MSN browser as default [#5533](https://github.com/AdguardTeam/AdguardForAndroid/issues/5533)
* Added com.irobot.home to routing exclusions [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### Fixes
* Billion values on statistic counters do not convert to abbreviations [#5633](https://github.com/AdguardTeam/AdguardForAndroid/issues/5633)
* Clicking AdGuard's protection status notification leads to mobile view on Amazon Fire TV stick [#5498](https://github.com/AdguardTeam/AdguardForAndroid/issues/5498)
* DNS filters are able to be updated if the DNS filters switch is disabled [#5382](https://github.com/AdguardTeam/AdguardForAndroid/issues/5382)
* Domain with the `$app` modifier fails to be added to HTTPS-filtered website exclusions [#5587](https://github.com/AdguardTeam/AdguardForAndroid/issues/5587)
* Option *Filter secure DNS* changes by itself after rebooting [#5379](https://github.com/AdguardTeam/AdguardForAndroid/issues/5379)
* Statistics bar overlaps the counter description in the *Statistics* tab [#5138](https://github.com/AdguardTeam/AdguardForAndroid/issues/5138)
* Impossible to download the Android system update [#5651](https://github.com/AdguardTeam/AdguardForAndroid/issues/5651)
* Unable to log in to the Adguard Ad Blocker app on Android TV
[#5669](https://github.com/AdguardTeam/AdguardForAndroid/issues/5669)

### CoreLibs (filtering engine)
* CoreLibs updated to v1.17.118 [#5654](https://github.com/AdguardTeam/AdguardForAndroid/issues/5654)

#### Fixes
* Handled ClientHello fragmentation [#1968](https://github.com/AdguardTeam/CoreLibs/issues/1968)
* Corrected long processing time of large HTML [#1886](https://github.com/AdguardTeam/CoreLibs/issues/1886)

### Scriptlets (JavaScript enhancement for filtering rules)
* Scriptlets updated to v2.1.6

#### Fixes
* Fixed `json-prune` — content of array was incorrectly removed [#482](https://github.com/AdguardTeam/Scriptlets/issues/482)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7.2

- Published: 2025-06-26T16:42:05Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7.2

In this update, we’ve fully fixed a problem that slipped through in the previous release: AdGuard protection would shut off whenever WebView was stopped or updated. With this version, Android 7 and 8 users can finally enjoy uninterrupted protection as well.

## Changelog

### Fixes
* AdGuard gets disabled when WebView is stopped or updated [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)

## 4.9 RC 1

- Published: 2025-03-27T17:01:06Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9-rc-1

We’ve added a major feature in this RC: please welcome native support for userstyles. This feature has been available in AdGuard for Windows and AdGuard for Mac for a while, and now we are bringing it to AdGuard for Android!

Userstyles are similar in a way to userscripts, but they only focus on changing the appearance of websites using CSS, without getting into their code. Now customising the websites of your choice — like adding a dark theme — becomes an easy task. You can create your own userstyles in the app itself, or install ready-made styles from trusted [online sources](https://userstyles.world/).

To add a userstyle, go to *Settings* → *Filtering* → *Extensions*→ *Add extension* → *Import from file or URL*. To create your own style, click *Add extension* → *Create userstyle*.

We are continuing to make the app better while fixing bugs on the way and updating CoreLibs.

## Changelog

### CoreLibs

* CoreLibs updated to 1.17.118 [#5673](https://github.com/AdguardTeam/AdguardForAndroid/issues/5673)

#### Fixes

* Fixed ClientHello fragmentation [#1968](https://github.com/AdguardTeam/CoreLibs/issues/1968)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.9 Beta 1

- Published: 2025-03-20T17:35:30Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.9-beta-1

In this beta version, we are continuing our quest on making the app better while fixing bugs and glitches in the UI, and bringing timely updates to our CoreLibs and Scriptlets modules. You will find full details in the сhangelog below.

## Changelog

### Improvements

* Added support for MSN browser as default [#5533](https://github.com/AdguardTeam/AdguardForAndroid/issues/5533)
* Added `com.irobot.home` to route traffic through AdGuard exclusions [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### Fixes

* Billion values on statistic counters do not convert to abbreviations [#5633](https://github.com/AdguardTeam/AdguardForAndroid/issues/5633)
* Clicking AdGuard's protection status notification leads to mobile view on Amazon Fire TV stick [#5498](https://github.com/AdguardTeam/AdguardForAndroid/issues/5498)
* DNS filters are marked as updated if the DNS filter switch is disabled [#5382](https://github.com/AdguardTeam/AdguardForAndroid/issues/5382)
* Domain with `$app` modifier fails to be added to HTTPS-filtered website exclusions [#5587](https://github.com/AdguardTeam/AdguardForAndroid/issues/5587)
* Option "Filter secure DNS" changes by itself after rebooting [#5379](https://github.com/AdguardTeam/AdguardForAndroid/issues/5379)
* Statistics bar overlaps the counter description in Statistics tab [#5138](https://github.com/AdguardTeam/AdguardForAndroid/issues/5138)

### CoreLibs (filtering engine)
* CoreLibs updated to v1.17.108 [#5654](https://github.com/AdguardTeam/AdguardForAndroid/issues/5654)

#### Fixes

* Error in content-script when `$jsinject` exception is applied [#1960](https://github.com/AdguardTeam/CoreLibs/issues/1960)
* Special whitelist exceptions for scriptlets not working correctly [#1959](https://github.com/AdguardTeam/CoreLibs/issues/1959)

#### Other

* CoreLibs 1.17 blocks access to `ota.googlezip.net` [#1963](https://github.com/AdguardTeam/CoreLibs/issues/1963)

### Scriptlets (JavaScript enhancement for filtering rules)
* Scriptlets updated to v1.11.27

#### Fixes

* Fixed `json-prune` — content of array is incorrectly removed [#482](https://github.com/AdguardTeam/Scriptlets/issues/482)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.13 Beta 1

- Published: 2026-07-17T11:41:50Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.13-beta-1

If this beta of AdGuard for Android v4.13 is rolling out after a bit of radio silence, it means that sometimes the goals we set are even bigger in reality than they were in our plans. A lot of work was done across the board to get ready for the next step: the release version.

With this beta, we introduced differential filter updates to AdGuard for Android! To achieve this, we integrated the FiltersListManager library into the app. Now, your filters will load automatically without consuming tons of traffic.

We also added post-quantum cryptography support to DnsLibs. Now AdGuard for Android, like our other full ad-blocking products, keeps your DNS requests protected against future threats.

Another significant change is our: adoption of CRLite by Mozilla to verify revoked certificates. Using this instead of the more outdated OCSP (Online Certificate Status Protocol) or letting the app check each certificate against the CRL (Certificate Revocation List) not only speeds up website loading, but also increases your privacy and safety while browsing.

And last, but not least, we have done a lot of work on our filtering engines and fixed bugs that had accumulated over time. Scriptlets and CoreLibs were updated for better app performance.

You can consult the extensive changelog below to see all the fixes and improvements.

## Changelog


### Improvements
* Added possibility to copy an applied rule in request details in the filtering log [5637](https://github.com/AdguardTeam/AdguardForAndroid/issues/5637)
* Added support for Google Backup [5879](https://github.com/AdguardTeam/AdguardForAndroid/issues/5879)
* Excluded 2ndLine application from filtering by default [5116](https://github.com/AdguardTeam/AdguardForAndroid/issues/5116)
* Displayed information about updated DNS filters in the DNS list [5519](https://github.com/AdguardTeam/AdguardForAndroid/issues/5519)
* Added possibility to copy package_name in request details in the filtering log [5636](https://github.com/AdguardTeam/AdguardForAndroid/issues/5636)
* Improved the update check screen for the *Check for updates* button [5923](https://github.com/AdguardTeam/AdguardForAndroid/issues/5923)
* Eliminated the possibility to add an empty user rule through the recent activity tab [5193](https://github.com/AdguardTeam/AdguardForAndroid/issues/5193)
* Added color distinction for updated content on the *Updates* screen [5886](https://github.com/AdguardTeam/AdguardForAndroid/issues/5886)
* Improved voicing of TalkBack voice assistant elements for *Private browser*
* Restructured the inputs/dialogs in *Tracking protection*
* Updated crash reports and app usage data names and dialogs
* Added the option to find requests by applied rules in recent activity
* Added validation to *Mask your IP* address screen
* Added auto-refreshing of the webpage after toggling the *Website protection* switch for it in *Private browser*
* Added authentication for the local proxy
* Added possibility to clear `.hprof` when it’s not needed
* Added an app update error screen for TV

### Fixes
* A blocking rule for the `$network` type is added via the *Add allowing rule* button in request details [5390](https://github.com/AdguardTeam/AdguardForAndroid/issues/5390)
* The *Disable all?* popup appears on the *User rules* screen even if the rules list is empty [5175](https://github.com/AdguardTeam/AdguardForAndroid/issues/5175)
* CA certificate installation instructions are not relevant for ColorOS [5827](https://github.com/AdguardTeam/AdguardForAndroid/issues/5827)
* DNS filters shows `null` instead of the time of the last update [5902](https://github.com/AdguardTeam/AdguardForAndroid/issues/5902)
* Firewall is activated automatically after granting the *Usage access* system permission [5927](https://github.com/AdguardTeam/AdguardForAndroid/issues/5927)
* High battery consumption starting from v4.12 [5893](https://github.com/AdguardTeam/AdguardForAndroid/issues/5893)
* Impossible to block a domain, unblocked in DNS filter, using the filtering log only [5880](https://github.com/AdguardTeam/AdguardForAndroid/issues/5880)
* Incorrect subdomains appear in statistics [5868](https://github.com/AdguardTeam/AdguardForAndroid/issues/5868)
* Many apps stop working when AdGuard is active [5617](https://github.com/AdguardTeam/AdguardForAndroid/issues/5617)
* Recent activity log lags heavily after updating to v4.12.1 [5882](https://github.com/AdguardTeam/AdguardForAndroid/issues/5882)
* Problems while editing extensions in language modes other than English [5914](https://github.com/AdguardTeam/AdguardForAndroid/issues/5914)
* Recent activity log fails to be cleared instantly in AdGuard v4.14 nightly 4 [5908](https://github.com/AdguardTeam/AdguardForAndroid/issues/5908)
* Subdomains duplicate in *Statistics* [5840](https://github.com/AdguardTeam/AdguardForAndroid/issues/5840)
* The custom DNS server disappears after importing settings that were just exported [5892](https://github.com/AdguardTeam/AdguardForAndroid/issues/5892)
* The title of videos doesn’t minimize when clicking the share button while in horizontal mode [5612](https://github.com/AdguardTeam/AdguardForAndroid/issues/5612)
* Turning on AdGuard using tile closes the notification panel [5915](https://github.com/AdguardTeam/AdguardForAndroid/issues/5915)
* Filters update without authorization [5309](https://github.com/AdguardTeam/AdguardForAndroid/issues/5309)
* User regex in *Ad blocking* and *DNS filtering* rules breaks after AdGuard v4.14 nightly 5 [5916](https://github.com/AdguardTeam/AdguardForAndroid/issues/5916)
* When attempting to update a beta version (e.g. RC), the update proceeds to the latest release version [5920](https://github.com/AdguardTeam/AdguardForAndroid/issues/5920)
* Configuration can’t be imported via link, even if the versions are consistent [5912](https://github.com/AdguardTeam/AdguardForAndroid/issues/5912)
* Rules duplicate themselves in the *Applied rules* section
* Failed to move the AdGuard Personal CA to the system store via the *Move* button in the app
* Custom content filter lists disappear after time
* Protection resumes every few seconds with *HTTPS filtering* and *FakeDNS* enabled
* An error snack appears after editing a userscript 
* The switch on the Extensions setting does not respond when tapping the setting name 
* After rebooting the phone, blocked URLs no longer show the reason why they were blocked in the log
* The *Protection may not work properly while the hotspot is active* notification is displayed for Android 10+
* Impossible to add a blocking rule with additional modifiers from *Recent activity*
* Impossible to select a custom DNS server by tapping *Save and select*
* Actual DNS protocol doesn’t match with what is shown on the *DNS server details* screen after settings import
* Empty space below the navigation bar after opening extensions editor
* AdGuard does not start after reboot
* Incorrect display of onboarding for certificate installation when importing settings via a link
* Integration mode dialogue doesn’t open consistently at app’s first launch
* Search query is not displayed on the *Recent activity* screen if the header was not collapsed after returning from request details
* The *Open* button for DNS providers opens the browser but not the website on Xiaomi TV Box
* The *Can’t update license info* snack is not displayed on the *TV license* screen after license check timeout
* Focus reset to default after pressing the *Refresh status* button on the *License* screen on TV
* The *Certificate wasn’t installed* dialog is shown after certificate installation via settings sharing
* Custom filter version is not updated after the filter update
* Text clipping, header overlap, and content being covered by the keyboard in *Rule editor*
* The YouTube button in the AdGuard player restarts video 
* On the *Quick actions* screen firewall notifications are displayed for both blocked and allowed apps when the *Show blocked only* filter is selected
* Scrolling *User rules* overlaps another view
* Scroll focus moves out of viewport during rapid scrolling of *App management* on TV
* Sharing from YouTube Music to AdGuard player doesn’t work
* AdGuard’s notification brings the device’s screen out of sleep mode
* *Private browser* does not open other apps from webpages
* Filter rule editor accepts any non-empty string as valid rule without syntax validation
* Dynamic theme does not apply to the AdGuard app after closing *Private browser*
* UI layering was corrected in PiP mode for the AdGuard player
* With Kazakh or Kyrgyz as system language, AdGuard erroneously displays it as Russian
* The number of blocked requests is displayed incorrectly in notifications in languages ​​that use hieroglyphs

### DnsLibs (DNS filtering engine)
* Updated DnsLibs to v2.8.45 [5961](https://github.com/AdguardTeam/AdguardForAndroid/issues/5961)

#### Improvements
* Added Post-Quantum cryptography support to DnsLibs [245](https://github.com/AdguardTeam/DnsLibs/issues/245)
* Added an option to remove `h3` from the `alpn` parameter of HTTPS RR [257](https://github.com/AdguardTeam/DnsLibs/issues/257)
 * Improved reliability of testing DoT upstream availability [263](https://github.com/AdguardTeam/DnsLibs/issues/263)
* Improved DNS upstream list updates without reloading filters [248](https://github.com/AdguardTeam/DnsLibs/issues/248)

#### Fixes
* DNS unblocking rule does not work
* At times system:// upstream replies failed to be accepted on Android [265](https://github.com/AdguardTeam/DnsLibs/issues/265)
* Missing AdGuard certificate on some websites such as hitomi.la [2055](https://github.com/AdguardTeam/CoreLibs/issues/2055)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.21.38

#### Improvements
* Added support for decoding URLs in `$urltransform` [1915](https://github.com/AdguardTeam/CoreLibs/issues/1915)
* Enabled HTTP/3 filtering by default in beta/nightly builds [2014](https://github.com/AdguardTeam/CoreLibs/issues/2014)
* Added support for example.org/path cosmetic rules [2012](https://github.com/AdguardTeam/CoreLibs/issues/2012)
* Added support for the new `$reason` modifier [1986](https://github.com/AdguardTeam/CoreLibs/issues/1986)
* Improved *Do Not Track* behavior [1982](https://github.com/AdguardTeam/CoreLibs/issues/1982)
* Prevented local.adguard.org DNS leakage after enabling protection [1854](https://github.com/AdguardTeam/CoreLibs/issues/1854)
* Enabled HTTP/3 filtering by default in stable builds [2015](https://github.com/AdguardTeam/CoreLibs/issues/2015)

#### Fixes
* Incorrect certificate serial number marshalling leads to false positive CRLite matches [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* In the Request details, the *Destination address* is displayed as 127.0.0.1 if integration with AdGuard VPN is enabled
* There is no AdGuard certificate if the advanced option *Check websites’ certificate transparency* is enabled [2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* Connection resets on CoreLibs v1.19 
* Localhost is unreachable in manual proxy mode in v1.19 [2019](https://github.com/AdguardTeam/CoreLibs/issues/2019)
* Incorrect destination address is shown in *Request details* when integration with AdGuard VPN is enabled [2021](https://github.com/AdguardTeam/CoreLibs/issues/2021)
* Userscript import failure caused by BOM [2009](https://github.com/AdguardTeam/CoreLibs/issues/2009)
* Broken injections when FakeDNS is used in proxy settings [2017](https://github.com/AdguardTeam/CoreLibs/issues/2017)
* Broken handling of closing script tags with spaces [2042](https://github.com/AdguardTeam/CoreLibs/issues/2042)
* Incorrect `$generichide` behavior for domain-scoped rules [2041](https://github.com/AdguardTeam/CoreLibs/issues/2041)
* AdGuard certificate absent if the advanced option *Check websites’ certificate transparency* is enabled [2046](https://github.com/AdguardTeam/CoreLibs/issues/2046)
* Incorrect certificate serial number marshalling leads to false positive CRLite matches [5793](https://github.com/AdguardTeam/AdguardForWindows/issues/5793)
* High latency in QUIC/HTTP/3 filtering causes protocol fallback to HTTP/2 [2062](https://github.com/AdguardTeam/CoreLibs/issues/2062)

### Scriptlets (JavaScript enhancement for filtering rules)
* Updated Scriptlets to v2.2.16

#### Improvements
* Added new scriptlet — `prevent-innerHTML` [488](https://github.com/AdguardTeam/Scriptlets/issues/488)
* Improved `fingerprintjs2` — support window [541](https://github.com/AdguardTeam/Scriptlets/issues/541)
* Added a parameter to increase duration of the `trusted-click-element` scriptlet’s execution duration [400](https://github.com/AdguardTeam/Scriptlets/issues/400)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12 RC 1

- Published: 2025-09-30T22:36:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12-rc-1

A release candidate for the upcoming AdGuard for Android v4.12 is now available. For us, launching an RC version is a great way to test new features before their official release. For users, it’s an opportunity to be among the first to try them out. We hope you enjoy it!

## Changelog

### Improvements
* Disabled “Route traffic through AdGuard” option for com.bKash.customerapp to ensure the app works correctly [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### Fixes
* CA certificate installation instructions are not relevant for Honor [#5779](https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* Impossible to add app-specific HTTPS exclusion [#5290](https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* Custom DNS filter is not shown in the Update section [#5821](https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* Tapping the cross on the snackbar about downloading a new app version doesn’t stop the download [#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* Some images are missing in a banking app due to AdGuard filtering [#5819](https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)
* Unable to connect to proxy server [#5794](https://github.com/AdguardTeam/AdguardForAndroid/issues/5794)
* DNS filters do not apply [#5851](https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### Improvements

* Improved the `$app` modifier: added support for wildcards and regexps
[1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* Added support for ALPS extension [1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### Fixes

* Wrong tracking protection option shown in the log [#5739](https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* Filtering disabled on some websites due to performance warnings (new.lewd.ninja) [1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* "Use FakeDNS" option in Proxy Server interrupts the connection of bypassed apps [5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* Some extensions do not work after update to v2.17 [1993](https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHR timeout with the `immersivetranslate` userscript [2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* Content-type modifiers do not work with the `$urltransform` modifier [1978](https://github.com/AdguardTeam/CoreLibs/issues/1978)

### DnsLibs (DNS filtering engine)

* Updated DnsLibs to v2.6.20 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### Scriptlets (JavaScript enhancement for filtering rules)

* Updated Scriptlets to v2.2.9

#### Improvements
* Added a new scriptlet  — 'trusted-replace-argument' [405](https://github.com/AdguardTeam/Scriptlets/issues/405)

#### Fixes
* 'prevent-element-src-loading' — TrustedScriptURL is not defined in Firefox  [514](https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — quotes are escaped incorrectly [517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* Compilation error in Safari 15 due to unsupported regex lookbehind [519](https://github.com/AdguardTeam/Scriptlets/issues/519)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.12 Beta 1

- Published: 2025-09-29T21:42:10Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.12-beta-1

As we always say, your feedback is really important to us, and this time we’ve added one of the most requested features — landscape mode. Using AdGuard on a tablet is now even more convenient.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/tablet_en.png" width="700">
</p>

We’ve also introduced settings import via link. This feature saves you time: no need to reconfigure everything on a new device or spend time describing your setup when reporting missed ads — just share a link.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.12/share_en.png" width="300">
</p>

## Changelog

### Improvements
* Disabled “Route traffic through AdGuard” option for com.bKash.customerapp to ensure the app works correctly [#5788](https://github.com/AdguardTeam/AdguardForAndroid/issues/5788)

### Fixes
* CA certificate installation instructions are not relevant for Honor [#5779](https://github.com/AdguardTeam/AdguardForAndroid/issues/5779)
* Impossible to add app-specific HTTPS exclusion [#5290](https://github.com/AdguardTeam/AdguardForAndroid/issues/5290)
* Custom DNS filter is not shown in the Update section [#5821](https://github.com/AdguardTeam/AdguardForAndroid/issues/5821)
* Tapping the cross on the snackbar about downloading a new app version doesn’t stop the download [#5760](https://github.com/AdguardTeam/AdguardForAndroid/issues/5760)
* Some images are missing in a banking app due to AdGuard filtering [#5819](https://github.com/AdguardTeam/AdguardForAndroid/issues/5819)
* Unable to connect to proxy server [#5794](https://github.com/AdguardTeam/AdguardForAndroid/issues/5794)
* DNS filters do not apply [#5851](https://github.com/AdguardTeam/AdguardForAndroid/issues/5851)

### CoreLibs (Filtering engine)

* Updated CoreLibs to v1.19.28 [#5830](https://github.com/AdguardTeam/AdguardForAndroid/issues/5830)

#### Improvements

* Improved the `$app` modifier: added support for wildcards and regexps
[1906](https://github.com/AdguardTeam/CoreLibs/issues/1906)
* Added support for ALPS extension [1987](https://github.com/AdguardTeam/CoreLibs/issues/1987) 

#### Fixes

* Wrong tracking protection option shown in the log [#5739](https://github.com/AdguardTeam/AdguardForAndroid/issues/5739)
* Filtering disabled on some websites due to performance warnings (new.lewd.ninja) [1994](https://github.com/AdguardTeam/CoreLibs/issues/1994)
* "Use FakeDNS" option in Proxy Server interrupts the connection of bypassed apps [5355](https://github.com/AdguardTeam/AdguardForAndroid/issues/5355)
* Some extensions do not work after update to v2.17 [1993](https://github.com/AdguardTeam/CoreLibs/issues/1993)
* XHR timeout with the `immersivetranslate` userscript [2000](https://github.com/AdguardTeam/CoreLibs/issues/2000)
* Content-type modifiers do not work with the `$urltransform` modifier [1978](https://github.com/AdguardTeam/CoreLibs/issues/1978)

### DnsLibs (DNS filtering engine)

* Updated DnsLibs to v2.6.20 [#5834](https://github.com/AdguardTeam/AdguardForAndroid/issues/5834)

### Scriptlets (JavaScript enhancement for filtering rules)

* Updated Scriptlets to v2.2.9

#### Improvements
* Added a new scriptlet  — 'trusted-replace-argument' [405](https://github.com/AdguardTeam/Scriptlets/issues/405)

#### Fixes
* 'prevent-element-src-loading' — TrustedScriptURL is not defined in Firefox  [514](https://github.com/AdguardTeam/Scriptlets/issues/514)
* 'trusted-replace-node-text' — quotes are escaped incorrectly [517](https://github.com/AdguardTeam/Scriptlets/issues/517)
* Compilation error in Safari 15 due to unsupported regex lookbehind [519](https://github.com/AdguardTeam/Scriptlets/issues/519)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.11 Beta 1

- Published: 2025-08-14T15:04:09Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.11-beta-1

This beta includes some under-the-hood improvements, a substantial number of bug fixes, and a CoreLibs update. As a result, overall app stability has been significantly improved.

## Changelog

### Fixes
* The Create button overlaps the checkbox on the trial activation screen [#5039](https://github.com/AdguardTeam/AdguardForAndroid/issues/5039)
* AdGuard player doesn’t open when sharing a video from the YouTube app [#5780](https://github.com/AdguardTeam/AdguardForAndroid/issues/5780)
* AdGuard identifies AdGuard VPN as a third-party VPN in Integration mode [#5567](https://github.com/AdguardTeam/AdguardForAndroid/issues/5567)
* Apps excluded by UID are routed through AdGuard [#5731](https://github.com/AdguardTeam/AdguardForAndroid/issues/5731)
* Invalid filter update date format for Japanese, Korean, and Chinese [#5703](https://github.com/AdguardTeam/AdguardForAndroid/issues/5703)
* Missing string for private browser notification [#5741](https://github.com/AdguardTeam/AdguardForAndroid/issues/5741)
* Private browser onboarding is displayed twice [#5752](https://github.com/AdguardTeam/AdguardForAndroid/issues/5752)
* Private browser crashes after tapping browser settings [#5781](https://github.com/AdguardTeam/AdguardForAndroid/issues/5781)
* The “Nothing found” warning is missing on some screens [#5038](https://github.com/AdguardTeam/AdguardForAndroid/issues/5038)
* The “Apps operating through proxy” screen is displayed in gray in Integration mode [#5732](https://github.com/AdguardTeam/AdguardForAndroid/issues/5732)
* The app asks for permission to run in the background even though permission has already been granted [#5560](https://github.com/AdguardTeam/AdguardForAndroid/issues/5560)
* Titles and descriptions of DNS servers, extensions, and filters are  translated into the system language if a different language is selected in AdGuard [#5709](https://github.com/AdguardTeam/AdguardForAndroid/issues/5709)
* Two similar graphs can be displayed at the same time [#4915](https://github.com/AdguardTeam/AdguardForAndroid/issues/4915)
* The app icon does not fill the designed area on the Amazon Fire TV Stick 4K Max [#5476](https://github.com/AdguardTeam/AdguardForAndroid/issues/5476)
* `com.carshering` is broken when routed through AdGuard [#5464](https://github.com/AdguardTeam/AdguardForAndroid/issues/5464)
* Rules don’t get removed from the firewall after tapping “Remove rule” [#5613](https://github.com/AdguardTeam/AdguardForAndroid/issues/5613)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.18.28 [#5792](https://github.com/AdguardTeam/AdguardForAndroid/issues/5792)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.10 Beta 1

- Published: 2025-06-17T11:54:02Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.10-beta-1

This beta introduces important improvements to the HTTPS certificate installation process, making it more intuitive and accessible for users. 

When you install AdGuard and launch the app for the first time, you’re prompted to install an HTTPS certificate. This step is essential because the certificate plays a key role in ensuring effective ad filtering in browsers. Without it, filtering quality is significantly reduced. That’s why it’s crucial for all users, beginner or advanced, to be able to complete the installation without difficulty.

We knew there was room for improvement in the whole process — the previous instructions often didn’t reflect the actual settings found on devices from different manufacturers, and there was also a bug that prevented users from returning to the instructions after switching away from the app.

To address these issues, we’ve added in-app video guides for the most common devices — including Google Pixel, Samsung, Huawei, Xiaomi, and OnePlus — with adjustments based on Android OS version and user locale. We’ve also fixed the bug mentioned above.

## Changelog

### Improvements
* Added HTTPS filtering by default for the Lemur browser [#5577](https://github.com/AdguardTeam/AdguardForAndroid/issues/5577)

### Fixes
* AdGuard gets disabled when WebView is stopped or updated [#5537](https://github.com/AdguardTeam/AdguardForAndroid/issues/5537)
* After integration with Tor, Tor via Orbot isn’t the default proxy [#4908](https://github.com/AdguardTeam/AdguardForAndroid/issues/4908)
* Updated filters aren’t displayed after the app is restarted [#5638](https://github.com/AdguardTeam/AdguardForAndroid/issues/5638)
* QUIC filtering is disabled for WeChat and AliExpress [#5497](https://github.com/AdguardTeam/AdguardForAndroid/issues/5497)
* WeChat is excluded from HTTPS filtering by default [#5689](https://github.com/AdguardTeam/AdguardForAndroid/issues/5689)
* The app is not fully translated [#5418](https://github.com/AdguardTeam/AdguardForAndroid/issues/5418)
* Filtering status is not saved if it’s changed twice [#5701](https://github.com/AdguardTeam/AdguardForAndroid/issues/5701)
* Recent activity log lags when scrolling slowly [#5369](https://github.com/AdguardTeam/AdguardForAndroid/issues/5369)
* Some parameters are not included in the link when reporting an incorrect blocking [#5520](https://github.com/AdguardTeam/AdguardForAndroid/issues/5520)
* When opening a link in a browser, two AdGuard apps appear in the list of browsers, and one of which does not work as expected [#5592](https://github.com/AdguardTeam/AdguardForAndroid/issues/5592)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.17.157 [#5725](https://github.com/AdguardTeam/AdguardForAndroid/issues/5725)

#### Fixes
* Naver Smartstore cannot be accessed properly [#1971](https://github.com/AdguardTeam/CoreLibs/issues/1971)
* Some React-based websites aren’t loaded correctly due to a `Minified React error` [#1953](https://github.com/AdguardTeam/CoreLibs/issues/1953)
* User rule for domains does not block the request completely [#5539](https://github.com/AdguardTeam/AdguardForAndroid/issues/5539)

### DnsLibs (DNS filtering engine)
* DnsLibs updated to v2.6.6 [#5724](https://github.com/AdguardTeam/AdguardForAndroid/issues/5724)

### Scriptlets (JavaScript enhancement for filtering rules) 
* Scriptlets updated to v2.1.7

#### Improvements
*  ’prevent-addEventListener’ — added ability to match specific element [#480](https://github.com/AdguardTeam/Scriptlets/issues/480)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.8

- Published: 2025-02-17T17:20:34Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8

We continue to unify the code base of our products, and AdGuard for Android is no exception. Updates will now be more stable and new features will be added faster. Also, in the new version we have accelerated the loading of large amounts of data in Statistics, as well as updated CoreLibs and DnsLibs.

> From this version, AdGuard for Android only supports Android 9 or higher.

## Changelog

### Fixes
* Beeline Wi-Fi calls do not work [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)
* The CPU background value increases drastically after a few series of quitting/starting the app [#5504](https://github.com/AdguardTeam/AdguardForAndroid/issues/5504)
* Custom DNS does not work after importing settings [#5618](https://github.com/AdguardTeam/AdguardForAndroid/issues/5618)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.17.88 [#5620](https://github.com/AdguardTeam/AdguardForAndroid/issues/5620)

### DnsLibs (DNS filtering engine)
* DnsLibs updated to v2.5.63 [#5607](https://github.com/AdguardTeam/AdguardForAndroid/issues/5607)

#### Improvements
* Added `matter._tcp.default.service.arpa` to the list of default exclusions [#230](https://github.com/AdguardTeam/DnsLibs/issues/230)
* Block RFC9462 (_dns.resolver.arpa) queries [#228](https://github.com/AdguardTeam/DnsLibs/issues/228)
* Use `pretty_str()` in errors reported in `DnsRequestProcessedEvent` [#223](https://github.com/AdguardTeam/DnsLibs/issues/223)

#### Fixes
* Long waiting time for response when blocking by DNS [#1887](https://github.com/AdguardTeam/CoreLibs/issues/1887)
* `$dnsrewrite=IPv4` rule does not block IPv6 resolution [#224](https://github.com/AdguardTeam/DnsLibs/issues/224)

### UserscriptsWrapper 

* UserscriptsWrapper updated to v2.0.1

### Scriptlets (JavaScript enhancement for filtering rules) 

* Scriptlets updated to v2.1.4

#### Improvements
* `trusted-click-element` — check for `containsText` of all matched selectors [#468](https://github.com/AdguardTeam/Scriptlets/issues/468)

#### Fixes
* `trusted-click-element` — element was removed and added again before it was clicked [#391](https://github.com/AdguardTeam/Scriptlets/issues/391)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.8 RC 2

- Published: 2025-02-15T11:47:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-rc-2

Ad blocking was compromised, but not for long: we fixed [an annoying bug reported by users](https://github.com/AdguardTeam/AdguardForAndroid/issues/5604) and updated our libraries while we were at it.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.8 RC 1

- Published: 2025-02-11T17:31:57Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-rc-1

We continue to unify the code base of our products, and AdGuard for Android is no exception. Updates will now be more stable and new features will be added faster. Also, in the new version we have accelerated the loading of large amounts of data in Statistics, as well as updated CoreLibs and DnsLibs.

>  From this version, AdGuard for Android only supports Android 9 or higher.

## Changelog

### Fixes
* Beeline Wi-Fi calls do not work [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.17.82 [#5610](https://github.com/AdguardTeam/AdguardForAndroid/issues/5610)

### DnsLibs (DNS filtering engine)
* DnsLibs updated to v2.5.63 [#5607](https://github.com/AdguardTeam/AdguardForAndroid/issues/5607)

#### Improvements
* Added matter._tcp.default.service.arpa to the list of default exclusions [#230](https://github.com/AdguardTeam/DnsLibs/issues/230 )
* Block RFC9462 (_dns.resolver.arpa) queries [#228](https://github.com/AdguardTeam/DnsLibs/issues/228)
* Use `pretty_str()` in errors reported in DnsRequestProcessedEvent [#223](https://github.com/AdguardTeam/DnsLibs/issues/223)

#### Fixes
* Long waiting time for response when blocking by DNS [#1887](https://github.com/AdguardTeam/CoreLibs/issues/1887 )
* Rule `$dnsrewrite=IPv4` does not block IPv6 resolution [#224](https://github.com/AdguardTeam/DnsLibs/issues/224)
## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.8 Beta 1

- Published: 2025-02-07T17:27:43Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.8-beta-1

We continue to unify the code base of our products, and AdGuard for Android is no exception. Updates will now be more stable and new features will be added faster. Also in the new version we have accelerated the loading of large amounts of data in Statistics and updated CoreLibs. 

## Changelog

### Fixes

* Beeline Wi-Fi calls do not work [#5583](https://github.com/AdguardTeam/AdguardForAndroid/issues/5583)

### CoreLibs (Filtering engine)

* CoreLibs updated to v1.16.58 [#5579](https://github.com/AdguardTeam/AdguardForAndroid/issues/5579)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7.1

- Published: 2024-12-11T16:59:44Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7.1

In this update we've improved the stability of the app and fixed some minor bugs.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7

- Published: 2024-12-03T15:41:02Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7

Today’s version is exactly what we love: it introduces a fresh feature we couldn’t wait to see on the app. And it’s no small release – we’re introducing an in-app privacy browser to the app! Let’s take a closer look at what’s new.

> AdGuard v4.7 is the last version that supports Android 7 and 8. Starting with the next release, we will only offer support for Android 9 or higher.

## A private browser, because there’s no such thing as too much privacy

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.7/agpb_en.png" width="300">
</p>

Keeping privacy in mind while browsing has become an essential part of many users’ everyday life. We want our app to be part of that routine, and that’s why we’re rolling out the AdGuard private browser, bringing an extra layer of privacy to your daily web experience.

So, what’s so cool about this browser?

* Ad and tracker blocking (of course!)
* Easy history deletion with a visible, accessible button. Also, your browser history is automatically cleared when you close the browser

To explore this new feature, tap *Try our private browser* on the app's home screen. You can also access the browser through the *Protection* tab, where you can set a default search engine and even create a browser widget.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.7/agmainpb_en.png" width="300">
</p>

Just a heads-up: our private browser is still in the early stages of development and has a few limitations, like the inability to handle multiple sessions at once. In the future, we’ll offer a more comprehensive browsing experience, but for now, we suggest using it as a supplement to your usual browser’s Incognito Mode, rather than a replacement. Sounds good?

## Changelog

### Improvements
* Incorrect translation of Fanboy's Annoyance List description [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### Fixes
* “Allow app usage access” popup does not disappear after enabling the corresponding switch in the system settings on Android 9 [#4906](https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* Almost all apps are no longer logged as filtered [#5426](https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* Cursor barely visible at search bars in the Dark theme [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* Enabling/disabling the switch “Trusted filter” doesn’t make protection restart [#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* Incorrect error message when trying to send a report with an invalid email on the Report a bug screen [#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* Magenta color of AdGuard notification if protection is paused [#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* Routing for problem apps in groups is enabled when you turn on this option for problem-free apps [#4918](https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* TCP keepalive for outgoing sockets screen doesn't scroll [#5415](https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* The user rules are positioned in the middle of the editor [#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Translations are missing for Annoyances blocking notice [#5388](https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)
* The app crashes when Android WebView is unloaded [#5521](https://github.com/AdguardTeam/AdguardForAndroid/issues/5521)

### Other
* `it.labfabrici.hub` does not work when protection is working [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.5

- Published: 2024-11-12T17:10:23Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.5

Minor improvements to the statistics module.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7 RC 2

- Published: 2024-11-30T08:51:08Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-rc-2

One more RC, one step closer to the final release. This time, we focused on improving our private browser by fixing the stats counting and implementing filtering rules. We also worked on a solid boost for the overall app performance. Almost there!

## Changelog

### Improvements
* Incorrect translation of Fanboy's Annoyance List description [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### Fixes
* "Allow app usage access" popup does not disappear after enabling the corresponding switch in the system settings on Android 9 [#4906](https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* AdGuard crashes when Android WebView unloads [#5521](https://github.com/AdguardTeam/AdguardForAndroid/issues/5521)
* Almost all apps are no longer logged as filtered [#5426](https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* Cursor barely visible at search bars in the Dark theme [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* Enabling/disabling the switch “Trusted filter” doesn't make protection restart [#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* Incorrect error message when trying to send a report with an invalid email on the Report a bug screen [#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* Magenta color of AdGuard notification if protection is paused [#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* Routing for problem apps in groups is enabled when you turn on this option for problem-free apps [#4918](https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* TCP keepalive for outgoing sockets screen doesn't scroll [#5415](https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* The user rules are positioned in the middle of the editor [#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Translations are missing for Annoyances blocking notice [#5388](https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### Other
* `it.labfabrici.hub` does not work when protection is working [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7 RC 1

- Published: 2024-11-21T17:36:35Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-rc-1

We’re so close to the release, we can practically hear the champagne cork popping... No new features have been added since the last beta, but we promise we weren’t slacking, just getting all the awesome stuff ready for the final version.

## Changelog

### Improvements
* Incorrect translation of Fanboy's Annoyance List description [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### Fixes
* "Allow app usage access" popup does not disappear after enabling the corresponding switch in the system settings on Android 9 [#4906](https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* Almost all apps are no longer logged as filtered [#5426](https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* Cursor barely visible at search bars in the Dark theme [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* Enabling/disabling the switch “Trusted filter” doesn't make protection restart [#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* Incorrect error message when trying to send a report with an invalid email on the Report a bug screen [#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* Magenta color of AdGuard notification if protection is paused [#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* Routing for problem apps in groups is enabled when you turn on this option for problem-free apps [#4918](https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* TCP keepalive for outgoing sockets screen doesn't scroll [#5415](https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* The user rules are positioned in the middle of the editor [#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Translations are missing for Annoyances blocking notice [#5388](https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### Other
* `it.labfabrici.hub` does not work when protection is working [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### CoreLibs (Filtering engine)

#### CoreLibs updated to to v1.16.53

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.7 Beta 1

- Published: 2024-11-15T15:23:10Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.7-beta-1

Today's beta version is exactly what we love: it introduces a fresh feature we can’t wait to see live in the main release. And it’s no small beta either: we’re introducing a privacy browser to the app! Let’s take a closer look at each of these.

> AdGuard v4.7 is the last version that offers support for Android 7 and 8. From the next release, we will only offer support for Android 9 or superior.

## A private browser, because there’s no such thing as too much privacy

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/privatebrowser2.png" width="300">
</p>

Keeping privacy in mind while browsing has become an essential part of many users’ everyday life. We’re rolling out the AdGuard private browser, bringing an extra layer of privacy to your daily web experience.

So, what’s so cool about this browser?

* Ad and tracker blocking (of course!)
* Easy history deletion with a visible, accessible button. Also, your browser history is automatically cleared when you close a tab
* The option to save a browsing session by creating a bookmark — something regular Incognito Mode doesn’t offer! If you want to pick up right where you left off without re-opening every tab or logging back in, this feature is for you. For this to work, though, we do store cookies and localStorage

To explore this new feature, tap *Try our private browser* on the app's home screen. You can also access the browser through the *Protection* tab, where you can set a default search engine and even create a browser widget.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/privatebrowser1.jpg" width="300">
</p>

Just a heads-up: our private browser is still in the early stages of development and has a few limitations, like the inability to handle multiple sessions at once. In the future, we’ll offer a more comprehensive browsing experience, but for now, we suggest using it as a supplement to your usual browser’s Incognito Mode, rather than a replacement. Sounds good?

## Changelog

### Improvements
* Incorrect translation of Fanboy's Annoyance List description [#5423](https://github.com/AdguardTeam/AdguardForAndroid/issues/5423)

### Fixes
* "Allow app usage access" popup does not disappear after enabling the corresponding switch in the system settings on Android 9 [#4906](https://github.com/AdguardTeam/AdguardForAndroid/issues/4906)
* Almost all apps are no longer logged as filtered [#5426](https://github.com/AdguardTeam/AdguardForAndroid/issues/5426)
* Cursor barely visible at search bars in the Dark theme [#5397](https://github.com/AdguardTeam/AdguardForAndroid/issues/5397)
* Enabling/disabling the switch “Trusted filter” doesn't make protection restart [#5202](https://github.com/AdguardTeam/AdguardForAndroid/issues/5202)
* Incorrect error message when trying to send a report with an invalid email on the Report a bug screen [#5160](https://github.com/AdguardTeam/AdguardForAndroid/issues/5160)
* Magenta color of AdGuard notification if protection is paused [#5449](https://github.com/AdguardTeam/AdguardForAndroid/issues/5449)
* Routing for problem apps in groups is enabled when you turn on this option for problem-free apps [#4918](https://github.com/AdguardTeam/AdguardForAndroid/issues/4918)
* TCP keepalive for outgoing sockets screen doesn't scroll [#5415](https://github.com/AdguardTeam/AdguardForAndroid/issues/5415)
* The user rules are positioned in the middle of the editor [#5422](https://github.com/AdguardTeam/AdguardForAndroid/issues/5422)
* Translations are missing for Annoyances blocking notice [#5388](https://github.com/AdguardTeam/AdguardForAndroid/issues/5388)

### Other
* `it.labfabrici.hub` does not work when protection is working [#5284](https://github.com/AdguardTeam/AdguardForAndroid/issues/5284)

### CoreLibs (Filtering engine)

#### CoreLibs updated to to v1.16.51

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.4 Hotfix 

- Published: 2024-11-05T11:13:36Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4-hotfix

This hotfix update resolves the battery drain issue caused by usage of java.util.Calendar in specific time zones.

## 4.6.4

- Published: 2024-10-31T15:57:15Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4

If this release were a UFC fighter, it would go by the name “The Bugfixer” because it is all about squashing bugs. Let’s break down what we’ve accomplished here.

## DNS bug

We’ve tackled a particularly eye-twitching bug that caused DNS — and, as a result, the Internet — to randomly fail when switching networks. It took some detective work on our part since the issue was unpredictable and only impacted a small number of users. But hey, no one should be left without DNS protection! 

## Battery drain bug

Another irritating bug we discovered during beta testing: incorrect statistics calculations were leading to excessive battery drain. The system code was unable to calculate the date necessary for accurate statistics below a certain value. Thankfully, we’ve managed to work around this odd behavior in the system code, and now the stats are calculated correctly. They also now load faster and take up less RAM.

This issue seemed to affect users on specific versions of Android. If you were using the nightly or beta version of AdGuard and ran into this problem, we recommend updating to the stable release.

## Other fixes

A number of bug fixes and improvements come with the latest version of the CoreLibs, along with improved filtering quality — you can see the details in the changelog below.

## Changelog

### Fixes
* AdGuard fails to export logs and settings due to statistics size [#5458](https://github.com/AdguardTeam/AdguardForAndroid/issues/5458)
* AdGuard crashes when Recent activity log is opened in split screen [#5481](https://github.com/AdguardTeam/AdguardForAndroid/issues/5481)
* AdGuard consumes too much battery since v4.6 [#5460](https://github.com/AdguardTeam/AdguardForAndroid/issues/5460)

### CoreLibs (Filtering engine)
* CoreLibs updated to v1.16.44

#### Improvements
* Enable post-quantum cryptography when it’s used by the filtered app [#1916](https://github.com/AdguardTeam/CoreLibs/issues/1916)
* Support `strict-first-party` and `strict-third-party` modifier of uBO [#1874](https://github.com/AdguardTeam/CoreLibs/issues/1874)
* Added possibility to allowlist scriptlets [#1862](https://github.com/AdguardTeam/CoreLibs/issues/1862)
* Support redirection to the destination without tracking services as middleman [#1557](https://github.com/AdguardTeam/CoreLibs/issues/1557)


#### Fixes
* AdGuard content script is blocked by CSP on `uber.com` [#1903](https://github.com/AdguardTeam/CoreLibs/issues/1903)
* Login is broken in Firefox on `sony.de` [#1867](https://github.com/AdguardTeam/CoreLibs/issues/1867)
* GM_xmlhttpRequest doesn’t support the Referer header [#1899](https://github.com/AdguardTeam/CoreLibs/issues/1899)
*AdGuard overrides User-Agent changes made by the browser, which reduces privacy [#1910](https://github.com/AdguardTeam/CoreLibs/issues/1910)

### Scriptlets (JavaScript enhancement for filtering rules)
* Scriptlets updated to v1.11.27

#### Improvements
* `set-local-storage-item` — added values `allowed` and `denied` [#445](https://github.com/AdguardTeam/Scriptlets/issues/445)
* `abort-on-stack-trace` — support line number for `inlineScript` and `injectedScript` [#439](https://github.com/AdguardTeam/Scriptlets/issues/439)
* `set cookie` — added values `checked` and `unchecked` [#444](https://github.com/AdguardTeam/Scriptlets/issues/444)
* `trusted-click-element` — added `reload` option [#301](https://github.com/AdguardTeam/Scriptlets/issues/301)
* Added new scriptlet `trusted-set-session-storage-item` [#426](https://github.com/AdguardTeam/Scriptlets/issues/426)
* `set-cookie` — added `essential` and `nonessential` to supported values [#436](https://github.com/AdguardTeam/Scriptlets/issues/436)
* `trusted-set-cookie` and `trusted-set-cookie-reload` — added `$currentISODate$` [#435](https://github.com/AdguardTeam/Scriptlets/issues/435)
* `set-cookie` — added more supported values [#433](https://github.com/AdguardTeam/Scriptlets/issues/433)
* `set-local-storage-item` — added more supported values [#429](https://github.com/AdguardTeam/Scriptlets/issues/429)
* Improve logging in scriptlets [#411](https://github.com/AdguardTeam/Scriptlets/issues/411)
* Show cosmetic rules in the filtering log [#180](https://github.com/AdguardTeam/CoreLibs/issues/180)
* Added new scriptlet `trusted-dispatch-event` [#382](https://github.com/AdguardTeam/Scriptlets/issues/382)
* Added new scriptlet `trusted-replace-outbound-text` [#410](https://github.com/AdguardTeam/Scriptlets/issues/410)
* Added ability to validate redirects for AdGuard compatibility without the full rule text [#420](https://github.com/AdguardTeam/Scriptlets/issues/420)
* `trusted-click-element` — added support for closed ShadowRoot [#423](https://github.com/AdguardTeam/Scriptlets/issues/423)
* `trusted-click-element` — added an ability to click an element containing a given text [#409](https://github.com/AdguardTeam/Scriptlets/issues/409)

#### Fixes
* `log-on-stack-trace` — player is broken on `deltabit.co` [#384](https://github.com/AdguardTeam/Scriptlets/issues/384)
* `trusted-create-element` — when using the `cleanupDelayMs` parameter, a removed element is re-added and removed several times [#434](https://github.com/AdguardTeam/Scriptlets/issues/434)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.4 Beta 1

- Published: 2024-10-04T08:08:05Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.4-beta-1

This release is all about good vibes and improved filtering quality — the new version of the CoreLibs does just that. We’ve also optimized the way we handle statistics, so they load faster and use less RAM while the app is running. A few minor bugs were fixed as well.

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.3

- Published: 2024-09-09T16:58:37Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.3

Here’s an additional technical update following the previous one. In it, we’ve fixed bugs and kept working on the app stability.

&nbsp;
### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

### AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.2

- Published: 2024-08-21T15:01:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.2

Have you ever noticed how the app crashes even when you have a freshly updated version? Well, notice no more! This hotfix solves that problem. From now on, just pure ad blocking all the way.

&nbsp;
### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

### AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6.1 

- Published: 2024-07-26T10:36:02Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6.1

Filtering engines have been hit by [enemy bugs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5405), but AdGuard is stronger than that. With this hotfix, updated libraries bring you a cleaner and safer web.

&nbsp;
### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

### AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6

- Published: 2024-07-24T16:16:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6

As Vince Lombardi says, “Perfection is not attainable, but if we chase perfection we can catch excellence.” We do as he says, and try our best to make every update better. Today we are happy to release the new version of AdGuard for Android. Faster, stronger, and more efficient. Let’s take a look at the major changes.

With the updated filtering engine CoreLibs, we have been able to implement many new features that will improve your filtering experience. First of all, we’ve increased HTTPS filtering speed. Second, there are some handy enhancements for our filter developers and advanced users. We’ve added support for [`urltransform`](https://adguard.com/kb/general/ad-filtering/create-own-filters/#urltransform-modifier) and [`xmlprune`](https://adguard.com/kb/general/ad-filtering/create-own-filters/#xmlprune-modifier) modifiers. Now even more distracting elements on a page will be blocked.

We have made some UI improvements to make our app more user friendly. Some Xiaomi users faced difficulties when trying to optimize battery usage. We thought about it and decided to add the guide.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.6/Xiaomi_guide_en.png" width="300">
</p>

 
Our developers didn’t rest on their laurels, so they also updated DnsLibs andUserscriptsWrapper and fixed a lot of bugs to make the app more stable.

## Changelog

### Fixes
* AdGuard YouTube player cannot open YouTube links or play the playlist [#5348](https://github.com/AdguardTeam/AdguardForAndroid/issues/5348)
* App crashes when tapping the protection notification after quitting AdGuard [#5366](https://github.com/AdguardTeam/AdguardForAndroid/issues/5366)
* Translations do not fit in the field [#5324](https://github.com/AdguardTeam/AdguardForAndroid/issues/5324)
* The warning text “Not routed through AdGuard” does not disappear after resetting settings to default [#5340](https://github.com/AdguardTeam/AdguardForAndroid/issues/5340)

### CoreLibs (filtering engine)
* [CoreLibs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5400) updated to v1.15.59

#### Improvements
* Added `$urltransform` (trusted) modifier support [#1364](https://github.com/AdguardTeam/CoreLibs/issues/1364)
* Added `$xmlprune` modifier support [#473](https://github.com/AdguardTeam/CoreLibs/issues/473)
* Added mobile browsers to the list of user agents that support `:has()` natively [#1870](https://github.com/AdguardTeam/CoreLibs/issues/1870)
* Allowed ECDSA ciphers on the local side [#360](https://github.com/AdguardTeam/CoreLibs/issues/360)
* Set up `Sec-Fetch-Dest header: fencedframe` [#1853](https://github.com/AdguardTeam/CoreLibs/issues/1853)
* Support uBO's `/regex/` cosmetic rule format [#1844](https://github.com/AdguardTeam/CoreLibs/issues/1844)

#### Fixes
* Adblock syntax rules with FQDN do not work [#210](https://github.com/AdguardTeam/DnsLibs/issues/210)
* AdGuard and FTP connection error [#1864](https://github.com/AdguardTeam/CoreLibs/issues/1864)
* Userscript XHR error [#1876](https://github.com/AdguardTeam/CoreLibs/issues/1876)
* `$all` modifier does not work with non-domain-like URL part [#1860](https://github.com/AdguardTeam/CoreLibs/issues/1860)
* URL blocking rules do not work correctly with the `$generichide` modifier [#1857](https://github.com/AdguardTeam/CoreLibs/issues/1857)

### DnsLibs (DNS filtering engine)
* [DnsLibs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5357) updated to v2.5.33

### UserscriptsWrapper
* UserscriptsWrapper updated to v1.2.24

#### Fixes
* `vk-metabot.user.js` does not work via AdGuard [#1871](https://github.com/AdguardTeam/CoreLibs/issues/1871)

### ContentScript
* ContentScript updated to v2.0.6

#### Fixes
* Element hiding rules `##` and `#$#` do not apply to the `tv.rambler.ru` [#1865](https://github.com/AdguardTeam/CoreLibs/issues/1865)


&nbsp;
### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

### AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6 RC 1

- Published: 2024-07-19T13:03:42Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.6-rc-1

Just one final tweak before the release. In this version we’ve successfully fixed one major issue. Some users were experiencing a problem when switching between mobile and Wi-Fi connections. The AdGuard protection would stop, so you’d have to start it again manually. We’ve also fixed some other bugs to make the application even more stable. Keep an eye out for more updates — the official release is just around the corner!

## Changelog

### CoreLibs (filtering engine)
* [CoreLibs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5400) updated to v1.15.59


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.6 Beta 1

- Published: 2024-07-11T14:44:07Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/4.6-beta-1

As Vince Lombardi says, “Perfection is not attainable, but if we chase perfection we can catch excellence.” We do as he says, and try our best to make every update better. Today we are happy to release the new beta version of AdGuard for Android. Faster, stronger, and more efficient. Let’s take a look at the major changes.

With the updated filtering engine CoreLibs, we have been able to implement many new features that will improve your filtering experience. First of all, we increased HTTPS filtering speed. Second, we added support for `urltransform` and `xmlprune` modifiers. Now even more distracting elements on a page will be blocked.

Our developers didn't rest on their laurels, so they also updated DnsLibs, UserscriptsWrapper and fixed a lot of bugs to make the application more stable.

## Changelog

### Fixes
* AdGuard YouTube player cannot open YouTube links or play the playlist [#5348](https://github.com/AdguardTeam/AdguardForAndroid/issues/5348)
* App crashes when tapping the protection notification after quitting AdGuard [#5366](https://github.com/AdguardTeam/AdguardForAndroid/issues/5366)
* Translations do not fit in the field [#5324](https://github.com/AdguardTeam/AdguardForAndroid/issues/5324)
* The warning text “Not routed through AdGuard” does not disappear after resetting settings to default [#5340](https://github.com/AdguardTeam/AdguardForAndroid/issues/5340)

### CoreLibs (filtering engine)
* [CoreLibs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5381) updated to v1.15.54

#### Improvements
* Added `$urltransform` (trusted) modifier support [#1364](https://github.com/AdguardTeam/CoreLibs/issues/1364)
* Added `$xmlprune modifier` support [#473](https://github.com/AdguardTeam/CoreLibs/issues/473)
* Added mobile browsers to the list of user agents that support `:has()` natively [#1870](https://github.com/AdguardTeam/CoreLibs/issues/1870)
* Allowed ECDSA ciphers on the local side [#360](https://github.com/AdguardTeam/CoreLibs/issues/360)
* Set up `Sec-Fetch-Dest header: fencedframe` [#1853](https://github.com/AdguardTeam/CoreLibs/issues/1853)
* Support uBO's `/regex/` cosmetic rule format [#1844](https://github.com/AdguardTeam/CoreLibs/issues/1844)

#### Fixes
* Adblock syntax rules with FQDN do not work [#210](https://github.com/AdguardTeam/DnsLibs/issues/210)
* AdGuard and FTP connection error [#1864](https://github.com/AdguardTeam/CoreLibs/issues/1864)
* Userscript XHR error [#1876](https://github.com/AdguardTeam/CoreLibs/issues/1876)
* `$all` modifier does not work with non-domain-like URL part [#1860](https://github.com/AdguardTeam/CoreLibs/issues/1860)
* URL blocking rules do not work correctly with the `$generichide` modifier [#1857](https://github.com/AdguardTeam/CoreLibs/issues/1857)

### DnsLibs (DNS filtering engine)
* [DnsLibs](https://github.com/AdguardTeam/AdguardForAndroid/issues/5357) updated to v2.5.33

### UserscriptsWrapper
* UserscriptsWrapper updated to v1.2.24

#### Fixes
* `vk-metabot.user.js` does not work via AdGuard [#1871](https://github.com/AdguardTeam/CoreLibs/issues/1871)

### ContentScript
* ContentScript updated to v2.0.6

#### Fixes
* Element hiding rules `##` and `#$#` do not apply to the `tv.rambler.ru` [#1865](https://github.com/AdguardTeam/CoreLibs/issues/1865)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.5

- Published: 2024-06-11T12:09:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.5

This update brings our YouTube player’s usability to a whole new level: we added background playback, recommended videos, quality settings, and much more. Not so unskippable now, are you, ads? On top of that, this version includes some nice fixes for overall app performance, including the Android TV version.

## A ton of improvements for AdGuard’s YouTube player

Just look at what’s available now:

* Change video quality, playback speed, and subtitle settings using the gear ⚙ button

![AG player video settings](https://cdn.adtidy.org/blog/new/jdwr7AG-player-video-settings.png)

* Picture-in-picture mode is now supported, which means you can shrink the video to a small window and keep playing it in the background while using other apps. Great for such things as listening to music or podcasts

<p align="center">
<img src="https://cdn.adtidy.org/blog/new/x31y3AG-player-picture-in-picture.png" 
width="300" height="600">

* View recommendations at the end of the video, while paused, or by tapping the lower right corner of the player (availability depends on the video)

![AG player recommended videos](https://cdn.adtidy.org/blog/new/g64dbAG-player-recommended.png)

* Double-tap the right or left side of the screen to skip 10 seconds forward or back correspondingly

> Quick reminder: to launch the AdGuard player, choose any video in the YouTube app, tap *Share* and select AdGuard Player (it’s likely that you will need to scroll right and tap *More* first). 
>
> Note: AdGuard player is based on the internal web browser that opens YouTube and has ad-blocking functionality built in. Therefore, the functioning and availability of its features depends on the web version of YouTube.

## Changelog

### Improvements
* Focus now stays in the same place after opening the left-side menu of AdGuard for Android TV and closing it back [#5271](https://github.com/AdguardTeam/AdguardForAndroid/issues/5271)

### Fixes
* DNS protection settings fail to reset to default [#5322](https://github.com/AdguardTeam/AdguardForAndroid/issues/5322)
* "Show DevTools on the main screen" toggle starts blinking after interacting with other toggles on the same screen [#5332](https://github.com/AdguardTeam/AdguardForAndroid/issues/5332)
* Language-specific filter “Other, Other” [#5232](https://github.com/AdguardTeam/AdguardForAndroid/issues/5232)
* Failed to reset to default  the “Show DevTools on the main screen” option in Low-level settings [#5331](https://github.com/AdguardTeam/AdguardForAndroid/issues/5331)
* AdGuard for Android TV crashes when you try to add a custom DNS server using a link with "adguard:add_dns_server?address=" prefix [#5264](https://github.com/AdguardTeam/AdguardForAndroid/issues/5264)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.4.1

- Published: 2024-05-23T14:08:43Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4.1

This is a technical update aimed to increase the app stability and fix minor bugs.


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.4

- Published: 2024-05-20T12:58:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4

Improved Firewall functionality and on-the-fly DoH filtering are the highlights of AdGuard v4.4 for Android. After extensive testing, we are ready to introduce the new version to you.

## Firewall on fire

We like to think that we make the Internet cleaner and more enjoyable for users. But we are not ashamed to admit that sometimes we can send annoying notifications ourselves. Users have reported that they find using Firewall inconvenient: there are just too many notifications. As a result, people are turning them off for good in the system preferences.

In response, we have improved Firewall functionality. Now you can customize and turn off firewall notifications for all applications or specific ones. 
Don’t want to get notifications about Chrome connections? Open the notification shade, tap a notification about Chrome, and then tap *Mute*. All Firewall notifications for this app will be disabled.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/mute.png" 
width="300" height="600">

Alternatively, you can go to *Protection* → *Firewall* → *Notifications*and toggle off notifications for individual apps.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/settings.png" 
width="300" height="600">

## DoH requests be flying

With the updated filtering engine, CoreLibs, we can implement on-the-fly DNS-over-HTTPS (DoH) connection filtering. Our [desktop apps](https://adguard.com/en/blog/adguard-v2-14-for-mac.html) have already gone this route and it seems to work fine. Why is this feature even necessary?
 
Before, if a user enabled DoH in their browser but not in AdGuard, we had to filter requests directly in the browser and send them to the unencrypted system DNS, which decreased security. Now, with on-the-fly DoH connection filtering, we can filter DNS requests in the browser without sending them to an unencrypted server.

> You can find the new feature in *Settings* → *General* → *Advanced* → *Low-level settings* → *Filter secure DNS*.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/dns_en.png" 
width="300" height="600">

We also fixed some minor bugs and updated UserscriptsWrapper and DnsLibs.

## Changelog

### Improvements
* Enable HTTPS filtering on the Chromite browser for free [#4997](https://github.com/AdguardTeam/AdguardForAndroid/issues/4997)
* Improved Developer Tools section [#5173](https://github.com/AdguardTeam/AdguardForAndroid/issues/5173)
* Add the "Nothing to export" snack when trying to export rules with empty User rules list [#5176](https://github.com/AdguardTeam/AdguardForAndroid/issues/5176)
* Added com.klook app to default HTTPS filtering exclusions [#5143](https://github.com/AdguardTeam/AdguardForAndroid/issues/5143)
* Include com.nekki.shadowfightarena to QUIC bypass packages by default [#5158](https://github.com/AdguardTeam/AdguardForAndroid/issues/5158)

### Fixes
* The license key is not hidden [#4496](https://github.com/AdguardTeam/AdguardForAndroid/issues/4496)
* Fixed the translation on `it` locale [#5180](https://github.com/AdguardTeam/AdguardForAndroid/issues/5180)
* Autorun doesn’t work after rebooting Chromecast and Sony TV [#5156](https://github.com/AdguardTeam/AdguardForAndroid/issues/5156)
* Large battery consumption [#4960](https://github.com/AdguardTeam/AdguardForAndroid/issues/4960)
* Cache size grows quickly [#5125](https://github.com/AdguardTeam/AdguardForAndroid/issues/5125)
* App crashes when making changes on the Userscript state and returning back [#5131](https://github.com/AdguardTeam/AdguardForAndroid/issues/5131)
* App crashes when choosing the Indonesian language [#5236](https://github.com/AdguardTeam/AdguardForAndroid/issues/5236)
* DNS server settings reset after resetting the settings in DNS filters tab [#5142](https://github.com/AdguardTeam/AdguardForAndroid/issues/5142)
* Dialog about the certificate installation failure does not disappear after successful installation [#5194](https://github.com/AdguardTeam/AdguardForAndroid/issues/5194)
* Downloading the application update takes more than 400 mAh of battery capacity [#5259](https://github.com/AdguardTeam/AdguardForAndroid/issues/5259)
* Duplicates can be added to Websites allowlist using case difference [#5037](https://github.com/AdguardTeam/AdguardForAndroid/issues/5037)
* Error while exporting settings [#5069](https://github.com/AdguardTeam/AdguardForAndroid/issues/5069)
* Background images are blocked on com.opera.browser [#5096](https://github.com/AdguardTeam/AdguardForAndroid/issues/5096)
* Meross device pairing error (com.meross.meross) [#4989](https://github.com/AdguardTeam/AdguardForAndroid/issues/4989)
* Recent activity of the selected company with two components is not displayed [#5067](https://github.com/AdguardTeam/AdguardForAndroid/issues/5067)
* Remove (.) character for all DNS entries [#4824](https://github.com/AdguardTeam/AdguardForAndroid/issues/4824)
* Scroll area issue on the Browsing security screen [#5195](https://github.com/AdguardTeam/AdguardForAndroid/issues/5195)
* Scrollbar thumb goes behind the bottom menu in Recent activity [#4901](https://github.com/AdguardTeam/AdguardForAndroid/issues/4901)
* Snacks close due to minimizing the application [#5018](https://github.com/AdguardTeam/AdguardForAndroid/issues/5018)
* Some custom filter properties don’t update properly [#5171](https://github.com/AdguardTeam/AdguardForAndroid/issues/5171)
* Statistic cards on main screen doesn't fill full screen width [#5118](https://github.com/AdguardTeam/AdguardForAndroid/issues/5118)
* The popups are displayed in the system language, while the whole application is in English [#5168](https://github.com/AdguardTeam/AdguardForAndroid/issues/5168)
* The radio button state is not imported for the Bootstrap upstreams option [#5239](https://github.com/AdguardTeam/AdguardForAndroid/issues/5239)
* Update loader is not working correctly [#5028](https://github.com/AdguardTeam/AdguardForAndroid/issues/5028)
* Disabling via the notification shade will auto enable itself upon re-opening the app [#5146](https://github.com/AdguardTeam/AdguardForAndroid/issues/5146)
* With AdGuard protection enabled, the app reports that there is no Internet connection [#5209](https://github.com/AdguardTeam/AdguardForAndroid/issues/5209)
* Santander and Sainsburys Bank apps are breaking with HTTPS filtering on [#5058](https://github.com/AdguardTeam/AdguardForAndroid/issues/5058)
* Update progress bar has wrong colors [#5308](https://github.com/AdguardTeam/AdguardForAndroid/issues/5308)

### CoreLibs (Filtering engine) updated to v1.14.59 [#5316](https://github.com/AdguardTeam/AdguardForAndroid/issues/5316)

#### Improvements
* Added on-the-fly filtering of DoH connections [#198](https://github.com/AdguardTeam/DnsLibs/issues/198)
* Added `GM.xmlhttpRequest` as alias of `GM_xmlhttpRequest` [#1785](https://github.com/AdguardTeam/CoreLibs/issues/1785)
* Indicate that outbound proxy is used in the request processed event [#1385](https://github.com/AdguardTeam/CoreLibs/issues/1385)
* Added support for passing host to outbound proxy [#1386](https://github.com/AdguardTeam/CoreLibs/issues/1386)
* Added Firefox 121.0+ to the list of user agents, that natively support `:has()` [#1840](https://github.com/AdguardTeam/CoreLibs/issues/1840)
* Added ECH parameters from intercepted DNS HTTPS queries [#1794](https://github.com/AdguardTeam/CoreLibs/issues/1794)
* Improved HTML filtering performance [#1855](https://github.com/AdguardTeam/CoreLibs/issues/1855)
* Added an option to use `|` as a separator in `$permissions` [#1850](https://github.com/AdguardTeam/CoreLibs/issues/1850)

#### Fixes
* Apply `$permissions` only to `document` [#1856](https://github.com/AdguardTeam/CoreLibs/issues/1856)
* Cannot parse QUIC ClientHello split into two packets [#1861](https://github.com/AdguardTeam/CoreLibs/issues/1861)
* VOT script doesn’t work in Google chrome [#1665](https://github.com/AdguardTeam/CoreLibs/issues/1665)
* Request with Authorization header is not redirected [#1851](https://github.com/AdguardTeam/CoreLibs/issues/1851)
* Support anti-DPI feature for Korea Telecom [#1789](https://github.com/AdguardTeam/CoreLibs/issues/1789)
* Cookie rules with `[` and `]` in the name are invalid [#1843](https://github.com/AdguardTeam/CoreLibs/issues/1843)
* Cosmetic rules are not applied in some cases when AdGuard works alongside AdGuard VPN browser extension [#1791](https://github.com/AdguardTeam/CoreLibs/issues/1791)
* One of the subdomains is not filtered due to different site certificates [#1839](https://github.com/AdguardTeam/CoreLibs/issues/1839)
* `$all` modifier does not work correctly [#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)
* `mall.sk` content script is not injected [#1834](https://github.com/AdguardTeam/CoreLibs/issues/1834)
* Blocking regex rule that has escaped slash in a character class doesn’t work [#1831](https://github.com/AdguardTeam/CoreLibs/issues/1831)
* Content script is not injected if there is a tag (with embed attribute) before doctype declaration [#1825](https://github.com/AdguardTeam/CoreLibs/issues/1825)
* `$path` modifier doesn’t work with query params [#1817](https://github.com/AdguardTeam/CoreLibs/issues/1817)
* `$removeparam` on url with port redirects to url without port [#1818](https://github.com/AdguardTeam/CoreLibs/issues/1818)
* `android-hilfe.de` brakes website [#1800](https://github.com/AdguardTeam/CoreLibs/issues/1800)
* Cannot connect to wiki.cemu.info securely [#1821](https://github.com/AdguardTeam/CoreLibs/issues/1821)
* AdGuard systematically crashes and freezes [#1880](https://github.com/AdguardTeam/CoreLibs/issues/1880)

### Scriptlets (JavaScript enhancement for filtering rules) updated to v1.10.25

#### Improvements
* Improved google-analytics, added `ga.q` property [#355](https://github.com/AdguardTeam/Scriptlets/issues/355)
* Improved google-ima3, added `OmidVerificationVendor` property [#353](https://github.com/AdguardTeam/Scriptlets/issues/353)
* Added compatibility with uBO's set-cookie scriptlet [#332](https://github.com/AdguardTeam/Scriptlets/issues/332)
* Added new scriptlet `href-sanitizer` [#327](https://github.com/AdguardTeam/Scriptlets/issues/327)
* Added new scriptlet `json-prune-fetch-response` [#361](https://github.com/AdguardTeam/Scriptlets/issues/361)
* Added new scriptlet `json-prune-xhr-response` [#360](https://github.com/AdguardTeam/Scriptlets/issues/360)
* Added new scriptlet `trusted-suppress-native-method` [#383](https://github.com/AdguardTeam/Scriptlets/issues/383)
* Added new scriptlet `no-protected-audience` [#395](https://github.com/AdguardTeam/Scriptlets/issues/395)
* Improved `set-cookie`, increased a possible numeric value [#388](https://github.com/AdguardTeam/Scriptlets/issues/388)
* Improved `trusted-click-element`, added support for finding selectors in shadowRoot [#323](https://github.com/AdguardTeam/Scriptlets/issues/323)
* Use some redirects resources as scriptlets as well [#300](https://github.com/AdguardTeam/Scriptlets/issues/300)
* Added possibility to allowlist scriptlets [#377](https://github.com/AdguardTeam/Scriptlets/issues/377)
* Improved `prevent-fetch`, added `cors` responseType [#394](https://github.com/AdguardTeam/Scriptlets/issues/394)
* Improved `set-cookie`, added `domain` parameter [#389](https://github.com/AdguardTeam/Scriptlets/issues/389)
* Added new scriptlet `call-nothrow.js` [#333](https://github.com/AdguardTeam/Scriptlets/issues/333)
* Added new scriptlet `spoof-css` [#317](https://github.com/AdguardTeam/Scriptlets/issues/317)
* Added new scriptlet `trusted-create-element` [#278](https://github.com/AdguardTeam/Scriptlets/issues/278)
* Improved `set-cookie`, added more supported values [#379](https://github.com/AdguardTeam/Scriptlets/issues/379)
* Added new scriptlet `trusted-set-attr` [#281](https://github.com/AdguardTeam/Scriptlets/issues/281)

#### Fixes
* Fixed `set-constant` — setProxyTrap() [#403](https://github.com/AdguardTeam/Scriptlets/issues/403)
* Fixed `set-cookie`, do not encode a cookie name [#408](https://github.com/AdguardTeam/Scriptlets/issues/408)
* Fixed `set-local-storage-item` conversion, `$remove$` param [#404](https://github.com/AdguardTeam/Scriptlets/issues/404)

### UserscriptsWrapper updated to v1.2.23

### DnsLibs (DNS filtering engine) updated to v2.5.25 [#5306](https://github.com/AdguardTeam/AdguardForAndroid/issues/5306)

#### Improvements
* Allowed specifying tcp-only and udp-only DNS upstreams [#208](https://github.com/AdguardTeam/DnsLibs/issues/208)
* Support passing hostname to outbound proxy instead of bootstrapping [#197](https://github.com/AdguardTeam/DnsLibs/issues/197)
* Improved handling of HTTPS RRType [#215](https://github.com/AdguardTeam/DnsLibs/issues/215)
* Restrict host normalization to DoH only [#219](https://github.com/AdguardTeam/DnsLibs/issues/219)

#### Fixes
* Cannot use DoH DNS server that use HTTP/1.1 after updating to v4.3 [#216](https://github.com/AdguardTeam/DnsLibs/issues/216)
* Use Happy Eyeballs for IPv4/IPv6 in DoH [#217](https://github.com/AdguardTeam/DnsLibs/issues/217)
* Adblock syntax rules with FQDN doesn’t work [#210](https://github.com/AdguardTeam/DnsLibs/issues/210)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.5 Beta 1

- Published: 2024-05-30T15:22:00Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.5-beta-1

This update brings our YouTube player’s usability to a whole new level. This update brings our YouTube player’s usability to a whole new level: we added background playback, recommended videos, quality settings, and much more. Not so unskippable now, are you, ads? On top of that, this version includes some nice fixes for overall app performance, including the Android TV version.

## A ton of improvements for AdGuard’s YouTube player

Just look at what’s available now:

Change video quality, playback speed, and subtitle settings using the gear ⚙ button
Picture-in-Picture mode is now supported, which means you can shrink the video to a small window and keep playing it in the background while using other apps. Great for such things as listening to music or podcasts
View recommended videos at the end of the video or by pausing the video
Double-tap the right or left side of the screen to skip 10 seconds forward or back correspondingly

> Quick reminder: to launch the AdGuard player, choose any video in the YouTube app, tap “Share” and select AdGuard Player (it’s likely that you will need to scroll right and tap “More” first).

## Changelog

### Improvements
* Focus now stays in the same place after opening the left-side menu of AdGuard for Android TV and closing it back [#5271](https://github.com/AdguardTeam/AdguardForAndroid/issues/5271)

### Fixes
* DNS protection settings fail to reset to default [#5322](https://github.com/AdguardTeam/AdguardForAndroid/issues/5322)
* Language-specific filter "Other, Other" [#5232](https://github.com/AdguardTeam/AdguardForAndroid/issues/5232)
* Failed to reset to default  the "Show DevTools on the main screen" option in Low-level settings [#5331](https://github.com/AdguardTeam/AdguardForAndroid/issues/5331)
* AdGuard for Android TV crashes when you try to add a custom DNS server using a link with "adguard:add_dns_server?address=" prefix [#5264](https://github.com/AdguardTeam/AdguardForAndroid/issues/5264)



## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.4 Beta 1

- Published: 2024-04-27T16:57:29Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.4-beta-1

Improved Firewall functionality is the highlight of AdGuard v4.4 for Android beta. We have been testing it for a long time and now we are ready to introduce it to you.

Now you can select the apps you want to be notified about. Don't want to receive notifications about Chrome connections? Open the pull-down menu, tap a notification about Chrome, then tap *Mute*. All Firewall notifications for this app will be disabled.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/mute.png" 
width="300" height="600">
</p>

Alternatively, you can go to *Protection* → *Firewall* → *Notifications*. Select an app and toggle it off.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/v4.4/settings.png" 
width="300" height="600">
</p>

We also fixed some minor bugs and updated UserscriptsWrapper, CoreLibs, and DNsLibs.

## Changelog

### Improvements
* Enable HTTPS filtering on the Chromite browser for free [#4997](https://github.com/AdguardTeam/AdguardForAndroid/issues/4997)
* Improved Developer Tools section [#5173](https://github.com/AdguardTeam/AdguardForAndroid/issues/5173)
* Add the "Nothing to export" snack when trying to export rules with empty User rules list [#5176](https://github.com/AdguardTeam/AdguardForAndroid/issues/5176)
* Added com.klook app to default HTTPS filtering exclusions [#5143](https://github.com/AdguardTeam/AdguardForAndroid/issues/5143)
* Include com.nekki.shadowfightarena to QUIC bypass packages by default [#5158](https://github.com/AdguardTeam/AdguardForAndroid/issues/5158)

### Fixes
* The license key is not hidden [#4496](https://github.com/AdguardTeam/AdguardForAndroid/issues/4496)
* Fixed the translation on `it` locale [#5180](https://github.com/AdguardTeam/AdguardForAndroid/issues/5180)
* Autorun doesn’t work after rebooting Chromecast and Sony TV [#5156](https://github.com/AdguardTeam/AdguardForAndroid/issues/5156)
* Large battery consumption [#4960](https://github.com/AdguardTeam/AdguardForAndroid/issues/4960)
* Cache size grows quickly [#5125](https://github.com/AdguardTeam/AdguardForAndroid/issues/5125)
* App crashes when making changes on the Userscript state and returning back [#5131](https://github.com/AdguardTeam/AdguardForAndroid/issues/5131)
* App crashes when choosing the Indonesian language [#5236](https://github.com/AdguardTeam/AdguardForAndroid/issues/5236)
* DNS server settings reset after resetting the settings in DNS filters tab [#5142](https://github.com/AdguardTeam/AdguardForAndroid/issues/5142)
* Dialog about the certificate installation failure does not disappear after successful installation [#5194](https://github.com/AdguardTeam/AdguardForAndroid/issues/5194)
* Downloading the application update takes more than 400 mAh of battery capacity [#5259](https://github.com/AdguardTeam/AdguardForAndroid/issues/5259)
* Duplicates can be added to Websites allowlist using case difference [#5037](https://github.com/AdguardTeam/AdguardForAndroid/issues/5037)
* Error while exporting settings [#5069](https://github.com/AdguardTeam/AdguardForAndroid/issues/5069)
* Background images are blocked on com.opera.browser [#5096](https://github.com/AdguardTeam/AdguardForAndroid/issues/5096)
* Meross device pairing error (com.meross.meross) [#4989](https://github.com/AdguardTeam/AdguardForAndroid/issues/4989)
* Recent activity of the selected company with two components is not displayed [#5067](https://github.com/AdguardTeam/AdguardForAndroid/issues/5067)
* Remove (.) character for all DNS entries [#4824](https://github.com/AdguardTeam/AdguardForAndroid/issues/4824)
* Scroll area issue on the Browsing security screen [#5195](https://github.com/AdguardTeam/AdguardForAndroid/issues/5195)
* Scrollbar thumb goes behind the bottom menu in Recent activity [#4901](https://github.com/AdguardTeam/AdguardForAndroid/issues/4901)
* Snacks close due to minimizing the application [#5018](https://github.com/AdguardTeam/AdguardForAndroid/issues/5018)
* Some custom filter properties don’t update properly [#5171](https://github.com/AdguardTeam/AdguardForAndroid/issues/5171)
* Statistic cards on main screen doesn't fill full screen width [#5118](https://github.com/AdguardTeam/AdguardForAndroid/issues/5118)
* The popups are displayed in the system language, while the whole application is in English [#5168](https://github.com/AdguardTeam/AdguardForAndroid/issues/5168)
* The radio button state is not imported for the Bootstrap upstreams option [#5239](https://github.com/AdguardTeam/AdguardForAndroid/issues/5239)
* Update loader is not working correctly [#5028](https://github.com/AdguardTeam/AdguardForAndroid/issues/5028)
* Disabling via the notification shade will auto enable itself upon re-opening the app [#5146](https://github.com/AdguardTeam/AdguardForAndroid/issues/5146)
* With AdGuard protection enabled, the app reports that there is no Internet connection [#5209](https://github.com/AdguardTeam/AdguardForAndroid/issues/5209)
* Santander and Sainsburys Bank apps is braking with HTTPS Filtering on [#5058](https://github.com/AdguardTeam/AdguardForAndroid/issues/5058)

### CoreLibs (Filtering engine) updated to v1.14.51 [#5280](https://github.com/AdguardTeam/AdguardForAndroid/issues/5280)

#### Improvements
* Added `GM.xmlhttpRequest` as alias of `GM_xmlhttpRequest` [#1785](https://github.com/AdguardTeam/CoreLibs/issues/1785)
* Indicate that outbound proxy is used in the request processed event [#1385](https://github.com/AdguardTeam/CoreLibs/issues/1385)
* Added support for passing host to outbound proxy [#1386](https://github.com/AdguardTeam/CoreLibs/issues/1386)
* Added Firefox 121.0+ to the list of user agents, that natively support `:has()` [#1840](https://github.com/AdguardTeam/CoreLibs/issues/1840)
* Added ECH parameters from intercepted DNS HTTPS queries [#1794](https://github.com/AdguardTeam/CoreLibs/issues/1794)
* Improved HTML filtering performance [#1855](https://github.com/AdguardTeam/CoreLibs/issues/1855)
* Added an option to use `|` as a separator in `$permissions` [#1850](https://github.com/AdguardTeam/CoreLibs/issues/1850)

#### Fixes
* Apply `$permissions` only to `document` [#1856](https://github.com/AdguardTeam/CoreLibs/issues/1856)
* Cannot parse QUIC ClientHello split into two packets [#1861](https://github.com/AdguardTeam/CoreLibs/issues/1861)
* VOT script doesn’t work in Google chrome [#1665](https://github.com/AdguardTeam/CoreLibs/issues/1665)
* Request with Authorization header is not redirected [#1851](https://github.com/AdguardTeam/CoreLibs/issues/1851)
* Support anti-DPI feature for Korea Telecom [#1789](https://github.com/AdguardTeam/CoreLibs/issues/1789)
* Cookie rules with `[` and `]` in the name are invalid [#1843](https://github.com/AdguardTeam/CoreLibs/issues/1843)
* Cosmetic rules are not applied in some cases when AdGuard works alongside AdGuard VPN browser extension [#1791](https://github.com/AdguardTeam/CoreLibs/issues/1791)
* One of the subdomains is not filtered due to different site certificates [#1839](https://github.com/AdguardTeam/CoreLibs/issues/1839)
* `$all` modifier does not work correctly [#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)
* `mall.sk` content script is not injected [#1834](https://github.com/AdguardTeam/CoreLibs/issues/1834)
* Blocking regex rule that has escaped slash in a character class doesn’t work [#1831](https://github.com/AdguardTeam/CoreLibs/issues/1831)
* Content script is not injected if there is a tag (with embed attribute) before doctype declaration [#1825](https://github.com/AdguardTeam/CoreLibs/issues/1825)
* `$path` modifier doesn’t work with query params [#1817](https://github.com/AdguardTeam/CoreLibs/issues/1817)
* `$removeparam` on url with port redirects to url without port [#1818](https://github.com/AdguardTeam/CoreLibs/issues/1818)
* `android-hilfe.de` brakes website [#1800](https://github.com/AdguardTeam/CoreLibs/issues/1800)
* Cannot connect to wiki.cemu.info securely [#1821](https://github.com/AdguardTeam/CoreLibs/issues/1821)

### Scriptlets (JavaScript enhancement for filtering rules) updated to v1.10.25

#### Improvements
* Improved google-analytics, added `ga.q` property [#355](https://github.com/AdguardTeam/Scriptlets/issues/355)
* Improved google-ima3, added `OmidVerificationVendor` property [#353](https://github.com/AdguardTeam/Scriptlets/issues/353)
* Added compatibility with uBO's set-cookie scriptlet [#332](https://github.com/AdguardTeam/Scriptlets/issues/332)
* Added new scriptlet `href-sanitizer` [#327](https://github.com/AdguardTeam/Scriptlets/issues/327)
* Added new scriptlet `json-prune-fetch-response` [#361](https://github.com/AdguardTeam/Scriptlets/issues/361)
* Added new scriptlet `json-prune-xhr-response` [#360](https://github.com/AdguardTeam/Scriptlets/issues/360)
* Added new scriptlet `trusted-suppress-native-method` [#383](https://github.com/AdguardTeam/Scriptlets/issues/383)
* Added new scriptlet `no-protected-audience` [#395](https://github.com/AdguardTeam/Scriptlets/issues/395)
* Improved `set-cookie`, increased a possible numeric value [#388](https://github.com/AdguardTeam/Scriptlets/issues/388)
* Improved `trusted-click-element`, added support for finding selectors in shadowRoot [#323](https://github.com/AdguardTeam/Scriptlets/issues/323)
* Use some redirects resources as scriptlets as well [#300](https://github.com/AdguardTeam/Scriptlets/issues/300)
* Added possibility to allowlist scriptlets [#377](https://github.com/AdguardTeam/Scriptlets/issues/377)
* Improved `prevent-fetch`, added `cors` responseType [#394](https://github.com/AdguardTeam/Scriptlets/issues/394)
* Improved `set-cookie`, added `domain` parameter [#389](https://github.com/AdguardTeam/Scriptlets/issues/389)
* Added new scriptlet  `call-nothrow.js` [#333](https://github.com/AdguardTeam/Scriptlets/issues/333)
* Added new scriptlet `spoof-css` [#317](https://github.com/AdguardTeam/Scriptlets/issues/317)
* Added new scriptlet `trusted-create-element` [#278](https://github.com/AdguardTeam/Scriptlets/issues/278)
* Improved `set-cookie`, added more supported values [#379](https://github.com/AdguardTeam/Scriptlets/issues/379)
* Added new scriptlet `trusted-set-attr` [#281](https://github.com/AdguardTeam/Scriptlets/issues/281)

#### Fixes
* Fixed `set-constant` — setProxyTrap() [#403](https://github.com/AdguardTeam/Scriptlets/issues/403)
* Fixed `set-cookie`, do not encode a cookie name [#408](https://github.com/AdguardTeam/Scriptlets/issues/408)
* Fixed `set-local-storage-item` conversion, `$remove$` param [#404](https://github.com/AdguardTeam/Scriptlets/issues/404)

### UserscriptsWrapper updated to v1.2.23

### DnsLibs (DNS filtering engine) updated to v2.5.4 [#5237](https://github.com/AdguardTeam/AdguardForAndroid/issues/5237)

#### Improvements
* Allowed specifying tcp-only and udp-only DNS upstreams [#208](https://github.com/AdguardTeam/DnsLibs/issues/208)
* Support passing hostname to outbound proxy instead of bootstrapping [#197](https://github.com/AdguardTeam/DnsLibs/issues/197)
* Improved handling of HTTPS RRType [#215](https://github.com/AdguardTeam/DnsLibs/issues/215)

#### Fixes
* Cannot use DoH DNS server that use HTTP/1.1 after updating to v4.3 [#216](https://github.com/AdguardTeam/DnsLibs/issues/216)
* Use Happy Eyeballs for IPv4/IPv6 in DoH [#217](https://github.com/AdguardTeam/DnsLibs/issues/217)


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.3.1

- Published: 2023-12-27T16:46:42Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3.1

Sometimes a release is so significant and exciting that it’s easy for a bug to slip through. The only thing left to do is to release a new version as quickly as possible. In this hotfix, we’ve fixed a major issue: the app would crash when HTTPS proxy is enabled in a browser. We also made sure that the `$all` modifier now works correctly, updated the CoreLibs and DnsLibs — our beloved filtering engines — and added a few improvements along the way. What else is there to say? Update and see for yourself!

## Changelog

### Fixes 
* AdGuard crashes when HTTPS proxy is set in a browser [#5130](https://github.com/AdguardTeam/AdguardForAndroid/issues/5130)
* “Stay always protected” card re-appears on Xiaomi devices [#5126](https://github.com/AdguardTeam/AdguardForAndroid/issues/5126)

### CoreLibs (Filtering engine) 
* CoreLibs updated to v1.13.115 [#5124](https://github.com/AdguardTeam/AdguardForAndroid/issues/5124) 
* `$all` modifier does not work correctly [#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)

### DnsLibs (DNS filtering engine) 
* DnsLibs updated to v2.4.37 [#5123](https://github.com/AdguardTeam/AdguardForAndroid/issues/5123) 


## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.3.1 Beta 1

- Published: 2023-12-26T14:10:44Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3.1-beta-1

Sometimes a release is so significant and exciting that it’s easy for a bug to slip through. The only thing left to do is to release a new version as quickly as possible. In this beta, we’ve fixed a major issue: the app would crash when HTTPS proxy is enabled in a browser. We also made sure that the `$all` modifier now works correctly, updated the CoreLibs and DnsLibs — our beloved filtering engines — and added a few improvements along the way. What else is there to say? Update and see for yourself!

## Changelog

### Fixes 
* AdGuard crashes when HTTPS proxy is set in browser [#5130](https://github.com/AdguardTeam/AdguardForAndroid/issues/5130)

### CoreLibs (Filtering engine) 
* CoreLibs updated to v1.13.115 [#5124](https://github.com/AdguardTeam/AdguardForAndroid/issues/5124) 
* `$all` modifier does not work correctly [#1842](https://github.com/AdguardTeam/CoreLibs/issues/1842)

### DnsLibs (DNS filtering engine) 
* DnsLibs updated to v2.4.37 [#5123](https://github.com/AdguardTeam/AdguardForAndroid/issues/5123)

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## 4.3

- Published: 2023-12-22T12:54:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3

AdGuard v4.3 for Android brings you something not only special, but unprecedented. It’s the same AdGuard you know and love, but now with a TV-sized twist – and we mean that quite literally: we’re glad to introduce the support for Android TV! Important updates and a new Developer tools section are also here to enhance your user experience with our app.

## Android TV support

![AdGuard for Android TV](https://cdn.adguard.com/content/blog/articles/androidtv_en.png)

To provide full support for Android TV, we’ve developed a version of AdGuard for Android with the most essential features to enhance your browsing experience and content filtering on your TV. The new design, fully adapted for Android TV, includes:

* Adapted onboarding
* Home screen with statistics
* Adapted Protection screen
* Adapted settings
* App management
* DNS protection

DNS protection is a key feature on AdGuard for Android TV. Securing DNS traffic through encryption adds an extra layer of security and privacy to your browsing experience. With this update, you can now benefit from this safety also on the big screen. DNS-over-HTTPS is selected by default, but you can add your own server if a different protocol is needed.

Hold on to your remote, what you are about to experience is a brand new app! You can find the detailed instructions on how to install AdGuard for Android TV [in our blog post](https://adguard.com/en/blog/adguard-for-android-tv.html).

> Note: You’ll need a license to use AdGuard for Android TV. But you can also try it for free — we offer a 7-day trial period.

## Developer tools

<p align="center">
<img src="https://cdn.adguard.com/content/blog/articles/developertools_en.jpg" 
width="300" height="600">
</p>

We invite our advanced users and filter developers who interact very actively with the app to explore our new Developer tools, a specialized section designed for quick navigation and switching between features. There you can quickly enable or disable custom filters, access logs, enable recording of different logs, and more. This feature can be enabled in *Low-level settings*.

## CoreLibs and DnsLibs updates

The recent CoreLibs v1.13 update boosts your browsing experience with improved HTML filtering, while the update of DnsLibs to v2.4 makes your connection more secure with support for HTTP basic authentication. 

## More transparency in HTTPS filtering

To enhance the transparency of HTTPS filtering, AdGuard now offers the option to inspect the original certificate via *Recent Activity*. There you can view details of any web request, examine the encryption used by AdGuard, and inspect the original certificate.

This feature stems from a major concern with HTTPS filtering. AdGuard validates the certificate (and does it well!), but there may be situations where you’d like to inspect the original certificate yourself. You can read more about this issue in our [Knowledge base](https://adguard.com/kb/general/https-filtering/known-issues/).  

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Release channel](https://agrd.io/tvapk)
- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## Changelog

### Features
* Fulguris added to the list of browsers [#4969](https://github.com/AdguardTeam/AdguardForAndroid/issues/4969)
* Added a list of Russian VoWiFi IPs to exclude [#4992](https://github.com/AdguardTeam/AdguardForAndroid/issues/4992)
* Android TV OS support added [#3597](https://github.com/AdguardTeam/AdguardForAndroid/issues/3597)
* Added a button to reset DNS Protection setting [#4735](https://github.com/AdguardTeam/AdguardForAndroid/issues/4735)
* Added support for Macedonian (mk) to AdGuard for Android [#5086](https://github.com/AdguardTeam/AdguardForAndroid/issues/5086)
* HTTPS filtering for com.kantarworldpanel.shoppix disabled by default [#4706](https://github.com/AdguardTeam/AdguardForAndroid/issues/4706)
* Click area for back arrow buttons increased [#4789](https://github.com/AdguardTeam/AdguardForAndroid/issues/4789)
* Sorting order for User rules improved [#4779](https://github.com/AdguardTeam/AdguardForAndroid/issues/4779)
* Parse 'Title' metadata from filter list subscriptions [#4760](https://github.com/AdguardTeam/AdguardForAndroid/issues/4760)
* Operating System name + version sent to ReportsWebApp [#5025](https://github.com/AdguardTeam/AdguardForAndroid/issues/5025)

### Fixes
* "Slow work" notification disappears when enabling debug logging level [#5017](https://github.com/AdguardTeam/AdguardForAndroid/issues/5017)
* Product type and AdGuard version are incorrectly detected in the "Report incorrect blocking" form [#4895](https://github.com/AdguardTeam/AdguardForAndroid/issues/4895)
* Bootstrap upstreams setting doesn't reset after resetting low-level settings [#4907](https://github.com/AdguardTeam/AdguardForAndroid/issues/4907)
* Deleting website from blocklist doesn't work properly [#4902](https://github.com/AdguardTeam/AdguardForAndroid/issues/4902)
* In the free version, the status “Disabled Browsing security” appears as “Updated” when checking for updates [#4844](https://github.com/AdguardTeam/AdguardForAndroid/issues/4844)
* Filters can be found in the search only using English [#5026](https://github.com/AdguardTeam/AdguardForAndroid/issues/5026)
* Firewall works when it's disabled and there is no app usage access [#5012](https://github.com/AdguardTeam/AdguardForAndroid/issues/5012)
* Google Play: `com.gpn.azs` app doesn't work [#4845](https://github.com/AdguardTeam/AdguardForAndroid/issues/4845)
* Google Play: de.dkb.portalapp incorrect blocking [#3734](https://github.com/AdguardTeam/AdguardForAndroid/issues/3734)
* Importing settings with another language doesn't work correctly [#5007](https://github.com/AdguardTeam/AdguardForAndroid/issues/5007)
* Impossible to open and hear vocal messages in "Orange Téléphone" app [#4777](https://github.com/AdguardTeam/AdguardForAndroid/issues/4777)
* In the snack that appears in all settings, "Undo" is not translated into other languages [#4880](https://github.com/AdguardTeam/AdguardForAndroid/issues/4880)
* In tracking protection blinking at functions when pressing the switch [#4879](https://github.com/AdguardTeam/AdguardForAndroid/issues/4879)
* Incorrect tab is highlighted when redirected to the protection section by long tapping the icon [#4860](https://github.com/AdguardTeam/AdguardForAndroid/issues/4860)
* Infinite loader after tap on a snack from the Website allowlist/blocklist [#4843](https://github.com/AdguardTeam/AdguardForAndroid/issues/4843)
* It is possible to make a two-line rule via the clipboard [#5009](https://github.com/AdguardTeam/AdguardForAndroid/issues/5009)
* Keyboard lags and text cannot be entered in the search field after collapsing the top of the screen [#4979](https://github.com/AdguardTeam/AdguardForAndroid/issues/4979)
* License expiry date is displayed incorrectly [#4856](https://github.com/AdguardTeam/AdguardForAndroid/issues/4856)
* Logs upload changes login and password for Proxy server [#4884](https://github.com/AdguardTeam/AdguardForAndroid/issues/4884)
* Long option names do not fit in the rule creation dialog [#4764](https://github.com/AdguardTeam/AdguardForAndroid/issues/4764)
* Non-relevant results are also displayed on the "Language-specific ad blocking" screen [#4891](https://github.com/AdguardTeam/AdguardForAndroid/issues/4891)
* Redirect from the assistant highlights the incorrect tab in the bar [#5001](https://github.com/AdguardTeam/AdguardForAndroid/issues/5001)
* The "Add userscript" popup does not appear when redirected to AdGuard by the userscript link [#4913](https://github.com/AdguardTeam/AdguardForAndroid/issues/4913)
* The cursor position in the search field resets after collapsing the top of the screen [#4892](https://github.com/AdguardTeam/AdguardForAndroid/issues/4892)
* The loader is displayed on the search field on the Recent activity screen [#5035](https://github.com/AdguardTeam/AdguardForAndroid/issues/5035)
* The same icon is used for unrelated purposes [#4737](https://github.com/AdguardTeam/AdguardForAndroid/issues/4737)
* Unable to send a bug report when the checkbox "Send app logs..." is marked [#4894](https://github.com/AdguardTeam/AdguardForAndroid/issues/4894)
* When adding a DNS filter from the system using a file, the input field is grayed out [#4882](https://github.com/AdguardTeam/AdguardForAndroid/issues/4882)
* When adding custom DNS filters or Userscripts, the "Browse" button is grayed out [#4850](https://github.com/AdguardTeam/AdguardForAndroid/issues/4850)
* When changing the setting of the disabled option the protection is restarted [#4762](https://github.com/AdguardTeam/AdguardForAndroid/issues/4762)
* When importing DNS user rules containing empty lines, these lines are added [#4888](https://github.com/AdguardTeam/AdguardForAndroid/issues/4888)
* When quickly switching switches in Firewall rules, the rule list lines glitch [#4885](https://github.com/AdguardTeam/AdguardForAndroid/issues/4885)
* Wi-Fi calling issue on Xiaomi: add com.qualcomm.qti.cne to routing exclusions [#5029](https://github.com/AdguardTeam/AdguardForAndroid/issues/5029)
* Clearing the statistics doesn't clear apps and companies sections only resets their counters to zero [#4748](https://github.com/AdguardTeam/AdguardForAndroid/issues/4748)
* Impossible to log in to the ONECTA-Daikin app with AdGuard enabled [#4775](https://github.com/AdguardTeam/AdguardForAndroid/issues/4775)
​
## DnsLibs (DNS filtering engine)
​
### DnsLibs updated to v2.4.16
* On-the-fly filtering of DoH connections [#198](https://github.com/AdguardTeam/DnsLibs/issues/198)
​
### DnsLibs updated to v2.4.0
​* Basic auth for DoH endpoints [#189](https://github.com/AdguardTeam/DnsLibs/issues/189)
* Possible DoS attack against the local DNS proxy when it’s using a plain DNS upstream [#202](https://github.com/AdguardTeam/DnsLibs/issues/202)
​
### DnsLibs updated to v2.3.4
* `127.0.0.1 local` is incorrectly interpreted as being for all .local address, breaking mDNS [#207](https://github.com/AdguardTeam/DnsLibs/issues/207)
* Allow C# comments in domain name rules [#196](https://github.com/AdguardTeam/DnsLibs/issues/196)
* DoH tries to use stale connection too much time [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* Properly filter type=HTTPS requests [#199](https://github.com/AdguardTeam/DnsLibs/issues/199)
​
## CoreLibs (Filtering engine)

### CoreLibs updated to v1.13.98
* Add `!#else` pre-processor directive support [#1806](https://github.com/AdguardTeam/CoreLibs/issues/1806)
* Add `$extension` modifier disabling specific userscript [#1706](https://github.com/AdguardTeam/CoreLibs/issues/1706)
* Adopt new rule priority scheme [#1768](https://github.com/AdguardTeam/CoreLibs/issues/1768)
* Change sec-ch-ua headers to match user-agent when Stealth Mode is active [#1764](https://github.com/AdguardTeam/CoreLibs/issues/1764)
* Improve HTML filtering performance [#1772](https://github.com/AdguardTeam/CoreLibs/issues/1772)
* Improve HTML filtering rules `$$` -- allow CSS-like selectors [#94](https://github.com/AdguardTeam/CoreLibs/issues/94)
* Support for cap_html_filtering condition [#1758](https://github.com/AdguardTeam/CoreLibs/issues/1758)
* $denyallow does not allow blocking documents [#1809](https://github.com/AdguardTeam/CoreLibs/issues/1809)
* $stealth exceptions do not work on the TCP stack level where we block STUN/TURN [#1737](https://github.com/AdguardTeam/CoreLibs/issues/1737)
* Images are not displayed in Edge Bing Chat [#1744](https://github.com/AdguardTeam/CoreLibs/issues/1744)
* The `网盘直链下载助手` user script is not working with AdGuard [#1780](https://github.com/AdguardTeam/CoreLibs/issues/1780)
* Websites using SXG have no cosmetic filtering when opening from Google search [#1812](https://github.com/AdguardTeam/CoreLibs/issues/1812)
* socks5 proxy not working with AdGuard v4.0 [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* Content script is not injected into elements loaded in `object` tag [#1769](https://github.com/AdguardTeam/CoreLibs/issues/1769)
* Detect website locale based on HTML "lang" attribute and language request HTTP headers [#1736](https://github.com/AdguardTeam/CoreLibs/issues/1736)
* Increase limit for `$replace` rules [#1802](https://github.com/AdguardTeam/CoreLibs/issues/1802)
* Moving certificate is not an option anymore [#277](https://github.com/AdguardTeam/CoreLibs/issues/277)
*  Properly use ECH retry_configs [#1793](https://github.com/AdguardTeam/CoreLibs/issues/1793)
*  Support anti-DPI feature for Korea Telecom [#1789](https://github.com/AdguardTeam/CoreLibs/issues/1789)
*  UDP timeout is too small in TcpIpStack [#1796](https://github.com/AdguardTeam/CoreLibs/issues/1796)

## 4.3 Beta 1

- Published: 2023-12-15T19:07:07Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.3-beta-1

AdGuard v4.3 for Android beta brings you something not only special, but unprecedented. It’s the same AdGuard you know and love, but now with a TV-sized twist – and we mean that quite literally: we’re glad to introduce the support for Android TV! Important updates and a new Developer tools section are also here to enhance your user experience with our app

## Android TV support

To provide full support for Android TV, we’ve developed a simplified version of AdGuard for Android featuring the most essential features to enhance your browsing experience and content filtering on your TV. The new design, fully adapted for Android TV.

Hold on to your remote, what you are about to experience is a brand new app!

> Note: Android TV support is a feature exclusive to users with an AdGuard license.

## Developer tools

We invite our advanced users and filter developers who interact very actively with the app to explore our new Developer tools, a specialized section designed for quick navigation and switching between features. There you can quickly enable or disable custom filters, access logs, enable recording of different logs, and more. This feature can be enabled in *Low-level settings*.

## CoreLibs and DnsLibs updates

The recent CoreLibs v1.13 update boosts your browsing experience with improved HTML filtering, while the update of DnsLibs to v2.4 makes your connection more secure with support for HTTP basic authentication. 

## AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## AdGuard for Android TV direct download links:

- [Beta channel ](https://agrd.io/ag_android_tv_beta)

## Changelog

### Features
* Fulguris browser added to the list of browsers [#4969](https://github.com/AdguardTeam/AdguardForAndroid/issues/4969)
* A list of Russian VoWiFi IPs to exclude [#4992](https://github.com/AdguardTeam/AdguardForAndroid/issues/4992)
* Android TV OS support added [#3597](https://github.com/AdguardTeam/AdguardForAndroid/issues/3597)
* Add a button to reset DNS Protection setting [#4735](https://github.com/AdguardTeam/AdguardForAndroid/issues/4735)
* Add support for Macedonian (mk) to AdGuard for Android [#5086](https://github.com/AdguardTeam/AdguardForAndroid/issues/5086)
* HTTPS filtering for com.kantarworldpanel.shoppix disabled by default [#4706](https://github.com/AdguardTeam/AdguardForAndroid/issues/4706)
* Click area for back arrow buttons increased [#4789](https://github.com/AdguardTeam/AdguardForAndroid/issues/4789)
* Sorting order for User rules improved [#4779](https://github.com/AdguardTeam/AdguardForAndroid/issues/4779)
* Parse 'Title' metadata from filter list subscriptions [#4760](https://github.com/AdguardTeam/AdguardForAndroid/issues/4760)
* Operating System name + version sent to ReportsWebApp [#5025](https://github.com/AdguardTeam/AdguardForAndroid/issues/5025)

### Fixes
* "Slow work" notification disappears when enabling debug logging level [#5017](https://github.com/AdguardTeam/AdguardForAndroid/issues/5017)
* Product type and AdGuard version are incorrectly detected in the "Report incorrect blocking" form [#4895](https://github.com/AdguardTeam/AdguardForAndroid/issues/4895)
* Bootstrap upstreams setting doesn't reset after resetting low-level settings [#4907](https://github.com/AdguardTeam/AdguardForAndroid/issues/4907)
* Deleting website from blocklist doesn't work properly [#4902](https://github.com/AdguardTeam/AdguardForAndroid/issues/4902)
* In the free version, the status “Disabled Browsing security” appears as “Updated” when checking for updates [#4844](https://github.com/AdguardTeam/AdguardForAndroid/issues/4844)
* Filters can be found in the search only using English [#5026](https://github.com/AdguardTeam/AdguardForAndroid/issues/5026)
* Firewall works when it's disabled and there is no app usage access [#5012](https://github.com/AdguardTeam/AdguardForAndroid/issues/5012)
* Google Play: `com.gpn.azs` app doesn't work [#4845](https://github.com/AdguardTeam/AdguardForAndroid/issues/4845)
* Google Play: de.dkb.portalapp incorrect blocking [#3734](https://github.com/AdguardTeam/AdguardForAndroid/issues/3734)
* Importing settings with another language doesn't work correctly [#5007](https://github.com/AdguardTeam/AdguardForAndroid/issues/5007)
* Impossible so open and hear vocal messages in "Orange Téléphone" app [#4777](https://github.com/AdguardTeam/AdguardForAndroid/issues/4777)
* In the snack that appears in all settings, "Undo" is not translated into other languages [#4880](https://github.com/AdguardTeam/AdguardForAndroid/issues/4880)
* In tracking protection blinking at functions when pressing the switch [#4879](https://github.com/AdguardTeam/AdguardForAndroid/issues/4879)
* Incorrect tab is highlighted when redirected to the protection section by long tapping the icon [#4860](https://github.com/AdguardTeam/AdguardForAndroid/issues/4860)
* Infinite loader after tap on a snack from the Website allowlist/blocklist [#4843](https://github.com/AdguardTeam/AdguardForAndroid/issues/4843)
*It is possible to make a two-line rule via the clipboard [#5009](https://github.com/AdguardTeam/AdguardForAndroid/issues/5009)
* Keyboard lags and text cannot be entered in the search field after collapsing the top of the screen [#4979](https://github.com/AdguardTeam/AdguardForAndroid/issues/4979)
* License expiry date displayed incorrectly [#4856](https://github.com/AdguardTeam/AdguardForAndroid/issues/4856)
* Logs upload changes login and password for Proxy server [#4884](https://github.com/AdguardTeam/AdguardForAndroid/issues/4884)
* Long option names do not fit in the rule creation dialog [#4764](https://github.com/AdguardTeam/AdguardForAndroid/issues/4764)
* Non-relevant results are also displayed on the "Language-specific ad blocking" screen [#4891](https://github.com/AdguardTeam/AdguardForAndroid/issues/4891)
* Redirect from the assistant highlights the incorrect tab in the bar [#5001](https://github.com/AdguardTeam/AdguardForAndroid/issues/5001)
* The "Add userscript" popup does not appear when redirected to AdGuard by the userscript link [#4913](https://github.com/AdguardTeam/AdguardForAndroid/issues/4913)
* The cursor position in the search field resets after collapsing the top of the screen [#4892](https://github.com/AdguardTeam/AdguardForAndroid/issues/4892)
* The loader is displayed on the search field on the Recent activity screen [#5035](https://github.com/AdguardTeam/AdguardForAndroid/issues/5035)
* The same icon is used for unrelated purposes [#4737](https://github.com/AdguardTeam/AdguardForAndroid/issues/4737)
* Unable to send a bug report when the checkbox "Send app logs.." is marked [#4894](https://github.com/AdguardTeam/AdguardForAndroid/issues/4894)
* When adding a DNS filter from the system using a file, the input field is grayed out [#4882](https://github.com/AdguardTeam/AdguardForAndroid/issues/4882)
* When adding custom DNS filters or Userscripts, the "Browse" button is grayed out [#4850](https://github.com/AdguardTeam/AdguardForAndroid/issues/4850)
* When changing the setting of the disabled option the protection is restarted [#4762](https://github.com/AdguardTeam/AdguardForAndroid/issues/4762)
* When importing DNS user rules containing empty lines, these lines are added [#4888](https://github.com/AdguardTeam/AdguardForAndroid/issues/4888)
* When quickly switching switches in Firewall rules, the rule list lines glitch [#4885](https://github.com/AdguardTeam/AdguardForAndroid/issues/4885)
* Wi-Fi calling issue on Xiaomi: add com.qualcomm.qti.cne to routing exclusions [#5029](https://github.com/AdguardTeam/AdguardForAndroid/issues/5029)
* Clearing the statistics doesn't clear apps and companies sections only resets their counters to zero [#4748](https://github.com/AdguardTeam/AdguardForAndroid/issues/4748)
* Impossible to log in to the ONECTA-Daikin app with AdGuard enabled [#4775](https://github.com/AdguardTeam/AdguardForAndroid/issues/4775)
​
### DnsLibs updated to v2.4.16
​
* On-the-fly filtering of DoH connections [#198](https://github.com/AdguardTeam/DnsLibs/issues/198)
* Basic auth for DoH endpoints [#189](https://github.com/AdguardTeam/DnsLibs/issues/189)
* Possible DoS attack against the local DNS proxy when it’s using a plain DNS upstream [#202](https://github.com/AdguardTeam/DnsLibs/issues/202)
* `127.0.0.1 local` is incorrectly interpreted as being for all .local address, breaking mDNS [#207](https://github.com/AdguardTeam/DnsLibs/issues/207)
* Allow C# comments in domain name rules [#196](https://github.com/AdguardTeam/DnsLibs/issues/196)
* DoH tries to use stale connection too much time [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* Properly filter type=HTTPS requests [#199](https://github.com/AdguardTeam/DnsLibs/issues/199)
​
### CoreLibs updated to v1.13.98
​
* Add `!#else` pre-processor directive support [#1806](https://github.com/AdguardTeam/CoreLibs/issues/1806)
* Add `$extension` modifier disabling specific userscript [#1706](https://github.com/AdguardTeam/CoreLibs/issues/1706)
* Adopt new rule priority scheme [#1768](https://github.com/AdguardTeam/CoreLibs/issues/1768)
* Change sec-ch-ua headers to match user-agent when Stealth Mode is active [#1764](https://github.com/AdguardTeam/CoreLibs/issues/1764)
* Improve HTML filtering performance [#1772](https://github.com/AdguardTeam/CoreLibs/issues/1772)
* Improve HTML filtering rules `$$` -- allow CSS-like selectors [#94](https://github.com/AdguardTeam/CoreLibs/issues/94)
* Support for cap_html_filtering condition [#1758](https://github.com/AdguardTeam/CoreLibs/issues/1758)
* $denyallow does not allow blocking documents [#1809](https://github.com/AdguardTeam/CoreLibs/issues/1809)
* $stealth exceptions do not work on the TCP stack level where we block STUN/TURN [#1737](https://github.com/AdguardTeam/CoreLibs/issues/1737)
* Websites using SXG have no cosmetic filtering when opening from Google search [#1812](https://github.com/AdguardTeam/CoreLibs/issues/1812)
* socks5 proxy not working with AdGuard v4.0 [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* Content script is not injected into elements loaded in `object` tag [#1769](https://github.com/AdguardTeam/CoreLibs/issues/1769)
* Detect website locale based on HTML "lang" attribute and language request HTTP headers [#1736](https://github.com/AdguardTeam/CoreLibs/issues/1736)
* Increase limit for `$replace` rules [#1802](https://github.com/AdguardTeam/CoreLibs/issues/1802)
* Moving certificate is not an option anymore [#277](https://github.com/AdguardTeam/CoreLibs/issues/277)
*  Properly use ECH retry_configs [#1793](https://github.com/AdguardTeam/CoreLibs/issues/1793)
*  Support anti-DPI feature for Korea Telecom [#1789](https://github.com/AdguardTeam/CoreLibs/issues/1789)
*  UDP timeout is too small in TcpIpStack [#1796](https://github.com/AdguardTeam/CoreLibs/issues/1796)

---

## 4.2

- Published: 2023-10-23T12:02:32Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2

## AdGuard Dynamics

Get ready for a dynamic experience as AdGuard for Android makes its way to your screens with exciting new features! Now our app not only has [dynamic icons](https://github.com/AdguardTeam/AdguardForAndroid/issues/4317), it also has a dynamic theme.

If you enable this option in the settings, the AdGuard app interface and icon will match the color of your smartphone interface.

> Please note that these features are only available on Android devices running version 12 or higher.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/dynamicicon.png?mw=500" 
width="300" height="150">
</p>

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/themes/theme_en.png" 
width="600" height="600">
</p>

## HTTP/3 filtering support [#487](https://github.com/AdguardTeam/CoreLibs/issues/487)

AdGuard now not only filters HTTP/1.1 and HTTP/2 traffic. In this release, we have added **experimental** support for HTTP/3 filtering. The HTTP/3 protocol, powered by the QUIC network protocol, provides better privacy and security, as well as a more stable and faster Internet connection. By enabling HTTP/3 filtering, you can take advantage of the QUIC protocol and effectively block ads and trackers.

To enable HTTP/3 filtering, go to Settings → General → Advanced → Low-level settings → *Filter HTTP/3* and toggle the switch to the right.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/HTTP3filtering_en.png" 
width="300" height="600">
</p>

## Support for two HTTPS certificates

By implementing two HTTPS certificates, we have fixed an issue with HTTPS filtering in Chrome 100 and above on rooted devices. While the certificate in the system store will be responsible for filtering in most apps, the certificate in the user store will allow AdGuard to filter HTTPS traffic in Chromium-based browsers. 

Installing certificates has also become easier: we’ve added step-by-step instructions.

To install the second certificate, go to Settings → Filtering → Network → HTTPS filtering → *Security сertificates* and follow the instructions.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/4.2/HTTP3filtering_en.png" 
width="300" height="600">
</p>

Our filters have become even more powerful and we have also fixed a bunch of bugs to ensure stable performance of the app. Hurry up to update!

## Changelog
​
### Features
* Enabled HTTPS filtering by default for the Opera browser [#4972](https://github.com/AdguardTeam/AdguardForAndroid/issues/4972)
​
### Fixes
* Exclude INETCOM.TV from routing by default [#4723](https://github.com/AdguardTeam/AdguardForAndroid/issues/4723)
* AdGuard cannot start protection due to HTTPS certificate expiration [#4896](https://github.com/AdguardTeam/AdguardForAndroid/issues/4896)
* Auto-update of custom filters doesn't work [#4961](https://github.com/AdguardTeam/AdguardForAndroid/issues/4961)
* AdGuard logs users out of their accounts [#4959](https://github.com/AdguardTeam/AdguardForAndroid/issues/4959)
* AdGuard notifications cause the locked screen to turn on while in sleep mode [#4778](https://github.com/AdguardTeam/AdguardForAndroid/issues/4778)
* HTTPS filtering is disabled for the app after relaunching AdGuard if the certificate has been moved to the system storage [#5008](https://github.com/AdguardTeam/AdguardForAndroid/issues/5008)
* Shadow around the main switch is missing on Android 8 [#4858](https://github.com/AdguardTeam/AdguardForAndroid/issues/4858)
* Some elements are not announced correctly by TalkBack [#4809](https://github.com/AdguardTeam/AdguardForAndroid/issues/4809)
* Switch sometimes disappears for 10-30 seconds, protection restarts for a long time [#4862](https://github.com/AdguardTeam/AdguardForAndroid/issues/4862)
* The space at the bottom of the "How to block ads on YouTube" screen is missing on devices with small screens [#4866](https://github.com/AdguardTeam/AdguardForAndroid/issues/4866)
* If the app is set to Traditional Chinese, the filters are displayed in Simplified Chinese after the update [#4949](https://github.com/AdguardTeam/AdguardForAndroid/issues/4949) 
* Switching between firewall tabs causes AdGuard to crash [#4999](https://github.com/AdguardTeam/AdguardForAndroid/issues/4999)
* Importing settings with a different language does not immediately change the language [#4984](https://github.com/AdguardTeam/AdguardForAndroid/issues/4984)
* License is not imported when importing settings [#4985](https://github.com/AdguardTeam/AdguardForAndroid/issues/4985)
* Non-working button in the snack about disabled notifications [#5002](https://github.com/AdguardTeam/AdguardForAndroid/issues/5002)
* On the ‘Why filter HTTPS traffic’ screen, pressing Next again cancels the previous action [#4993](https://github.com/AdguardTeam/AdguardForAndroid/issues/4993)
* A cross button doesn't remove the text in the search bar on the Language-specific ad blocking screen [#4978](https://github.com/AdguardTeam/AdguardForAndroid/issues/4978)
* The text of imported/exported settings does not fit in the dialog box [#4981](https://github.com/AdguardTeam/AdguardForAndroid/issues/4981)

### CoreLibs (Filtering engine) updated to v1.12.80 [#4966](https://github.com/AdguardTeam/AdguardForAndroid/issues/4966)

#### Improvements
* User Agent stripping Improved [#1345](https://github.com/AdguardTeam/CoreLibs/issues/1345)
* TCP/IP: Added new reject mode - ICMP administratively prohibited [#1774](https://github.com/AdguardTeam/CoreLibs/issues/1774)
* Added support for uBO media queries [#1707](https://github.com/AdguardTeam/CoreLibs/issues/1707)

#### Fixes
* Connection is terminated by timer in have-result state [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180)
* A few seconds delay when using ipTIME home routers [#1756](https://github.com/AdguardTeam/CoreLibs/issues/1756)
* AdGuard slows down web page load time [#1522](https://github.com/AdguardTeam/CoreLibs/issues/1522)
* Hide referrer with "Hide your search queries" option enabled when request is made by click [#1766](https://github.com/AdguardTeam/CoreLibs/issues/1766)
* SOCKS5 proxy does not work with AdGuard 4.0 [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* Enabled ECH GREASE when ECH is enabled [#1781](https://github.com/AdguardTeam/CoreLibs/issues/1781)
* Fixed a bug with removing HTTP headers when decrypting book text [#1750](https://github.com/AdguardTeam/CoreLibs/issues/1750)
* Preparation for XPC [#1675](https://github.com/AdguardTeam/CoreLibs/issues/1675)
* DNS fallback helper sometimes returns 127.0.0.1 instead of provider servers [#1687](https://github.com/AdguardTeam/CoreLibs/issues/1687)
* UDP timeout is too small in TcpIpStack [#1796](https://github.com/AdguardTeam/CoreLibs/issues/1796)
​
### DnsLibs (DNS filtering engine) updated to v2.2.24 [#4953](https://github.com/AdguardTeam/AdguardForAndroid/issues/4953)

#### Fixes
* DoH tries to use stale connection for too long [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* CoreDNS DoQ server cannot be used by DnsLibs [#204](https://github.com/AdguardTeam/DnsLibs/issues/204)
* sdns:// cert pinning is incorrect [#205](https://github.com/AdguardTeam/DnsLibs/issues/205)

### Important for filter maintainers

* Added `$referral-policy` modifier [#135](https://github.com/AdguardTeam/CoreLibs/issues/135)
* Added `$method` modifier for basic rules [#1713](https://github.com/AdguardTeam/CoreLibs/issues/1713)
* Allowed $stealth rules with an empty pattern [#1762](https://github.com/AdguardTeam/CoreLibs/issues/1762)
* Added `$to` modifier [#1714](https://github.com/AdguardTeam/CoreLibs/issues/1714)
* `$jsonprune`, `$replace`, and `$hls` do not work with non-GET/POST HTTP methods [#1743](https://github.com/AdguardTeam/CoreLibs/issues/1743)
* Exception rules interfere with each other [#1749](https://github.com/AdguardTeam/CoreLibs/issues/1749)
* `$path` modifier does not work on path market.yandex.ru [#1726](https://github.com/AdguardTeam/CoreLibs/issues/1726)
* `$jsonprune` modifier should be able to handle quotes for jsonp [#1734](https://github.com/AdguardTeam/CoreLibs/issues/1734)
* Consider `:has()`, `:not()`, and `:is()` as a standard pseudo-class if ExtendedCss usage is not forced by the `#?#` rule marker [#1683](https://github.com/AdguardTeam/CoreLibs/issues/1683)
* Cosmetic rules do not work at mypikpak.com [#1767](https://github.com/AdguardTeam/CoreLibs/issues/1767)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.2 Beta 2

- Published: 2023-10-13T13:10:35Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2-beta-2

Now our app not only has dynamic icons, it also has a dynamic theme. If you enable this option in the settings, the AdGuard app interface will match the color of your smartphone interface. Aside from external changes, we have fixed several bugs for a smoother user experience.

<p align="center">
<img src="https://cdn.adtidy.org/content/github/ad_blocker/android/protectiontheme1.png" width="300" height="600"> <img src="https://cdn.adtidy.org/content/github/ad_blocker/android/protectiontheme2.png" width="300" height="600">
</p>

## Changelog
​​
### Fixes
 
* Switching between firewall tabs causes AdGuard to crash [#4999](https://github.com/AdguardTeam/AdguardForAndroid/issues/4999)
* Importing settings with a different language does not immediately change the language [#4984](https://github.com/AdguardTeam/AdguardForAndroid/issues/4984)
* License is not imported when importing settings [#4985](https://github.com/AdguardTeam/AdguardForAndroid/issues/4985)
* Non-working button in the snack about disabled notifications [#5002](https://github.com/AdguardTeam/AdguardForAndroid/issues/5002)
* On the Why filter HTTPS traffic' screen, pressing Next again cancels the previous action [#4993](https://github.com/AdguardTeam/AdguardForAndroid/issues/4993)
* A cross button doesn't remove the text in the search bar on the Language-specific ad blocking screen [#4978](https://github.com/AdguardTeam/AdguardForAndroid/issues/4978)
* The text of imported/exported settings does not fit in the dialog box [#4981](https://github.com/AdguardTeam/AdguardForAndroid/issues/4981)


### CoreLibs updated to v1.12.80 [#5003](https://github.com/AdguardTeam/AdguardForAndroid/issues/5003)
* Minor stability improvements


---

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.2 Beta 1

- Published: 2023-09-29T16:16:13Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.2-beta-1

## Dynamic icon [#4317](https://github.com/AdguardTeam/AdguardForAndroid/issues/4317)

AdGuard for Android now has a dynamic icon. If you are using themed icons on your smartphone, the AdGuard app will also match the color of your system. 

<p align="center">
<img src="https://cdn.adtidy.org/content/github/ad_blocker/android/dynamicicon.png" 
width="300" height="150">
</p>

## HTTP/3 filtering support [#487](https://github.com/AdguardTeam/CoreLibs/issues/487)

AdGuard now not only filters HTTP/1.1 and HTTP/2 traffic. In this beta we have added experimental support for HTTP/3 filtering. The HTTP/3 protocol, powered by the QUIC network protocol, provides better privacy and security, as well as a more stable and faster Internet connection. By enabling HTTP/3 filtering, you can take advantage of the QUIC protocol and effectively block ads and trackers.

To enable HTTP/3 filtering, go to Settings → General → Advanced → Low-level settings → *Filter HTTP/3* and toggle the switch to the right.

<p align="center">
<img src="https://cdn.adtidy.org/content/github/ad_blocker/android/HTTP3.png" 
width="300" height="600">
</p>

## Support for two HTTPS certificates

By implementing two HTTPS certificates, we have fixed an issue with HTTPS filtering in Chrome version 100 and above on rooted devices. While the certificate in the system store will be responsible for filtering in most apps, the certificate in the user store will allow AdGuard to filter HTTPS traffic in Chromium-based browsers. 

Installing certificates has also become easier: we've added step-by-step instructions.

To install the second certificate, go to Settings → Filtering → Network → HTTPS filtering → *Security сertificates* and follow the instructions.

<p align="center">
<img src="https://cdn.adtidy.org/content/github/ad_blocker/android/2certificates.png" 
width="300" height="600">
</p>

## Changelog
​
### Features
* Enabled HTTPS filtering by default for Opera browser [#4972](https://github.com/AdguardTeam/AdguardForAndroid/issues/4972)
​
### Fixes
* Exclude INETCOM.TV from routing by default [#4723](https://github.com/AdguardTeam/AdguardForAndroid/issues/4723)
* AdGuard cannot start protection due to HTTPS certificate expiration [#4896](https://github.com/AdguardTeam/AdguardForAndroid/issues/4896)
* Auto update of custom filters doesn't work [#4961](https://github.com/AdguardTeam/AdguardForAndroid/issues/4961)
* AdGuard logs out of the account [#4959](https://github.com/AdguardTeam/AdguardForAndroid/issues/4959)
* Shadow around the main switch is missing on Android 8 [#4858](https://github.com/AdguardTeam/AdguardForAndroid/issues/4858)
* Some elements are not announced correctly by TalkBack [#4809](https://github.com/AdguardTeam/AdguardForAndroid/issues/4809)
* Switch sometimes disappears for 10-30 seconds, protection restarts for a long time [#4862](https://github.com/AdguardTeam/AdguardForAndroid/issues/4862)
* The space at the bottom of the "How to block ads on YouTube" screen is missing on devices with small screens [#4866](https://github.com/AdguardTeam/AdguardForAndroid/issues/4866)
* If the app is set to Traditional Chinese, the filters are displayed in Simplified Chinese after the update [#4949](https://github.com/AdguardTeam/AdguardForAndroid/issues/4949)  

### CoreLibs
* CoreLibs updated to v1.12.76 [#4966](https://github.com/AdguardTeam/AdguardForAndroid/issues/4966)
* Connection is terminated by timer in have-result state [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180)
* Improved User Agent stripping [#1345] (https://github.com/AdguardTeam/CoreLibs/issues/1345)
* Added support for uBO media queries [#1707](https://github.com/AdguardTeam/CoreLibs/issues/1707)
* A few seconds delay when using ipTIME home routers [#1756](https://github.com/AdguardTeam/CoreLibs/issues/1756)
* AdGuard slows down web page load time [#1522](https://github.com/AdguardTeam/CoreLibs/issues/1522)
* Hide referrer with "Hide your search queries" option enabled when request is made by click [#1766](https://github.com/AdguardTeam/CoreLibs/issues/1766)
* SOCKS5 proxy does not work with AdGuard 4.0 [#4812](https://github.com/AdguardTeam/AdguardForAndroid/issues/4812)
* Enabled ECH GREASE when ECH is enabled [#1781](https://github.com/AdguardTeam/CoreLibs/issues/1781)
* Fixed a bug with removing HTTP headers when decrypting book text [#1750](https://github.com/AdguardTeam/CoreLibs/issues/1750)
* Preparation for XPC [#1675](https://github.com/AdguardTeam/CoreLibs/issues/1675)
* DNS fallback helper sometimes returns 127.0.0.1 instead of provider servers [#1687](https://github.com/AdguardTeam/CoreLibs/issues/1687)
* TCP/IP: Added new reject mode - ICMP administratively prohibited [#1774](https://github.com/AdguardTeam/CoreLibs/issues/1774)
* UDP timeout is too small in TcpIpStack [#1796](https://github.com/AdguardTeam/CoreLibs/issues/1796)
​
### DnsLibs
* DnsLibs updated to v2.2.24 [#4953](https://github.com/AdguardTeam/AdguardForAndroid/issues/4953)
* DoH tries to use stale connection for too long [#200](https://github.com/AdguardTeam/DnsLibs/issues/200)
* CoreDNS DoQ server cannot be used by DnsLibs [#204](https://github.com/AdguardTeam/DnsLibs/issues/204)
* sdns:// cert pinning is incorrect [#205](https://github.com/AdguardTeam/DnsLibs/issues/205)

### Important for filter maintainers

* Added $referral-policy modifier [#135](https://github.com/AdguardTeam/CoreLibs/issues/135)
* Added $method modifier for basic rules [#1713](https://github.com/AdguardTeam/CoreLibs/issues/1713)
* Allowed $stealth rules with an empty pattern [#1762](https://github.com/AdguardTeam/CoreLibs/issues/1762)
* Added $to modifier [#1714](https://github.com/AdguardTeam/CoreLibs/issues/1714)
* $jsonprune, $replace, and $hls do not work with non-GET-POST HTTP methods [#1743](https://github.com/AdguardTeam/CoreLibs/issues/1743)
* Exception rules interfere with each other [#1749](https://github.com/AdguardTeam/CoreLibs/issues/1749)
* $path modifier does not work on path market.yandex.ru [#1726](https://github.com/AdguardTeam/CoreLibs/issues/1726)
* $jsonprune modifier should be able to handle quotes for jsonp [#1734](https://github.com/AdguardTeam/CoreLibs/issues/1734)
* Consider :has(), :not(), and :is() as a standard pseudo-class if ExtendedCss usage is not forced by the #?# rule marker [#1683](https://github.com/AdguardTeam/CoreLibs/issues/1683)
* Cosmetic rules do not work at mypikpak.com [#1767](https://github.com/AdguardTeam/CoreLibs/issues/1767)

---

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.1

- Published: 2023-07-26T17:14:51Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.1

With this release, we have made a number of improvements to the UI and internal workings of our app. For example, we've reworked the YouTube player to support all video formats, including Live Streams and Shorts. Actually, it's based on the internal web browser that opens YouTube and has ad-blocking functionality built in. Take a look at the Protection section for a detailed description of this feature. We also made it easier for you to access *App management*. It's now just one tap away via the button we've added to the tab bar menu at the bottom.

## Changelog

### Features
* Added `com.homeretailgroup.myargoscard` and related domains to exclusions [#3480](https://github.com/AdguardTeam/AdguardForAndroid/issues/3480)
* Added support for com.quark.browser and com.qihoo.contents [#3673](https://github.com/AdguardTeam/AdguardForAndroid/issues/3673)
* Easier access to App management [#4408](https://github.com/AdguardTeam/AdguardForAndroid/issues/4408)

### Fixes
* AdGuard player does not play a YouTube video when tapping the Share button in a browser [#3932](https://github.com/AdguardTeam/AdguardForAndroid/issues/3932)
* Improved the behavior of bug report and feature request screens to prevent duplicates [#4814](https://github.com/AdguardTeam/AdguardForAndroid/issues/4814)
* *Reset to default* in General settings doesn't work properly [#4719](https://github.com/AdguardTeam/AdguardForAndroid/issues/4719)
* Added `com.apple.movetoios` to exclusions [#3676](https://github.com/AdguardTeam/AdguardForAndroid/issues/3676)
* AdGuard v4.0 for Android frequently restarts protection [#4707](https://github.com/AdguardTeam/AdguardForAndroid/issues/4707)
* When trying to go back after submitting a bug report, an infinite loader is displayed [#4792](https://github.com/AdguardTeam/AdguardForAndroid/issues/4792)
* After updating the filters, the updated filters are displayed in a row [#4790](https://github.com/AdguardTeam/AdguardForAndroid/issues/4790)
* Chrome Remote Desktop does not work unless filtering for the app is turned off [#4036](https://github.com/AdguardTeam/AdguardForAndroid/issues/4036)
* Added `pl.tvn.player` to filtering exclusions [#3646](https://github.com/AdguardTeam/AdguardForAndroid/issues/3646)
* Incorrect transition from the Use license key tab when entering a blocked key [#4562](https://github.com/AdguardTeam/AdguardForAndroid/issues/4562)
* Switching to another tab via snack does not work [#4502](https://github.com/AdguardTeam/AdguardForAndroid/issues/4502)
* On a small display, the buttons overlap the text on the Userscript screen [#4750](https://github.com/AdguardTeam/AdguardForAndroid/issues/4750)
* The com.rapido.passenger app is not working [#3976](https://github.com/AdguardTeam/AdguardForAndroid/issues/3976)
* When checking for updates, the Browsing Security Database should report "Up to date" if no update has been installed [#4725](https://github.com/AdguardTeam/AdguardForAndroid/issues/4725)
* Added `com.inpost.fresh` to filtering exclusions [#3979](https://github.com/AdguardTeam/AdguardForAndroid/issues/3979)

### Design
* Improved the technical info dialog [#4717](https://github.com/AdguardTeam/AdguardForAndroid/issues/4717)
* Improved the app's language screen [#4718](https://github.com/AdguardTeam/AdguardForAndroid/issues/4718)

### Versions
* Upgraded CoreLibs to v1.11.113
* Upgraded DnsLibs to v2.2.14

#### DnsLibs

* Added `lb._dns-sd._udp.*.in-addr.arpa` to the default list of exclusions [#194](https://github.com/AdguardTeam/DnsLibs/issues/194)
* `$denyallow` rules are not validated until additional modifiers are added [#191](https://github.com/AdguardTeam/DnsLibs/issues/191)
* Fallback upstream is not enabled for invalid plain DNS upstream [#4820](https://github.com/AdguardTeam/AdguardForAndroid/issues/4820)
* For IP-based DoT/DoQ connections, IP address is set for SNI [#186](https://github.com/AdguardTeam/DnsLibs/issues/186)
* Overall timeout is bigger when multiple upstreams are added [#105](https://github.com/AdguardTeam/DnsLibs/issues/105)
* Added XPC support [#174](https://github.com/AdguardTeam/DnsLibs/issues/174)
* Added the `dnsproxy_settings::request_timeout setting` instead of the upstream-specific ones [#163](https://github.com/AdguardTeam/DnsLibs/issues/163)
* DNS-over-QUIC upstream does not respect resolved_ip [#185](https://github.com/AdguardTeam/DnsLibs/issues/185)
* Traffic is routed from DNS 127.0.0.1 to an outbound proxy server [#195](https://github.com/AdguardTeam/DnsLibs/issues/195)
* Added SPKI fingerprint verification feature [#172](https://github.com/AdguardTeam/DnsLibs/issues/172)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.1 Beta 1

- Published: 2023-07-21T18:37:51Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.1-beta-1

With this release, we have made a number of improvements to the UI and internal workings of our app. For example, we've redesigned the YouTube player to support all video formats, including live streams, regular videos and shorts. Have a look at the Protection section for a detailed description of this feature. We also made it easier for you to access Apps Management. It's now just one click away via the button we've added to the tab bar menu at the bottom.

## Changelog

### Features
* Added com.homeretailgroup.myargoscard and associated domains to exclusions [#3480](https://github.com/AdguardTeam/AdguardForAndroid/issues/3480 )
* Added support for com.quark.browser and com.qihoo.contents [#3673](https://github.com/AdguardTeam/AdguardForAndroid/issues/3673)
* Easier access to Apps management [#4408](https://github.com/AdguardTeam/AdguardForAndroid/issues/4408)

### Fixes
* Improved the behavior of bug report and feature request screens to prevent duplicates [#4814](https://github.com/AdguardTeam/AdguardForAndroid/issues/4814)
* "Reset to default" in the General settings doesn't work as it should [#4719](https://github.com/AdguardTeam/AdguardForAndroid/issues/4719)
* Added com.apple.movetoios to the exclusions [#3676](https://github.com/AdguardTeam/AdguardForAndroid/issues/3676)
* AdGuard 4 nightly frequently restarts protection [#4707](https://github.com/AdguardTeam/AdguardForAndroid/issues/4707)
* When trying to go back after submitting a bug report, an infinite loader is displayed [#4792](https://github.com/AdguardTeam/AdguardForAndroid/issues/4792)
* After updating the filters, the updated filters are displayed in a row [#4790](https://github.com/AdguardTeam/AdguardForAndroid/issues/4790)
* Chrome Remote Desktop does not work unless filtering for the app is turned off [#4036](https://github.com/AdguardTeam/AdguardForAndroid/issues/4036)
* Added pl.tvn.player to the filtering exclusions [#3646](https://github.com/AdguardTeam/AdguardForAndroid/issues/3646)
* Incorrect transition from the Use license key tab when entering a blocked key [#4562](https://github.com/AdguardTeam/AdguardForAndroid/issues/4562)
* Switching to another tab via snack does not work [#4502](https://github.com/AdguardTeam/AdguardForAndroid/issues/4502)
* On a small display, the buttons overlap the text on the Userscript screen [#4750](https://github.com/AdguardTeam/AdguardForAndroid/issues/4750)
* The com.rapido.passenger app is not working [#3976](https://github.com/AdguardTeam/AdguardForAndroid/issues/3976)
* When checking for updates, the Browsing Security Database should report "Up to date" if no update has been installed [#4725](https://github.com/AdguardTeam/AdguardForAndroid/issues/4725)

* Added com.inpost.fresh to the filtering exclusions [#3979](https://github.com/AdguardTeam/AdguardForAndroid/issues/3979)

### Design
* Improved the technical info dialog [#4717](https://github.com/AdguardTeam/AdguardForAndroid/issues/4717)
* Improved the app's language screen [#4718](https://github.com/AdguardTeam/AdguardForAndroid/issues/4718)

### Versions
* Upgraded CoreLibs to v1.11.113
* Upgraded DnsLibs to v2.2.14

#### DnsLibs

* Added "lb._dns-sd._udp.*.in-addr.arpa" to the default list of exclusions [#194](https://github.com/AdguardTeam/DnsLibs/issues/194)
* The $denyallow rules are not validated until additional modifiers are added [#191](https://github.com/AdguardTeam/DnsLibs/issues/191)
* Fallback upstream not enabled for invalid plain DNS upstream [#4820](https://github.com/AdguardTeam/AdguardForAndroid/issues/4820)
* For IP-based DoT/DoQ connections, IP address is set for SNI [#186](https://github.com/AdguardTeam/DnsLibs/issues/186)
* Overall timeout is bigger when multiple upstreams are added [#105](https://github.com/AdguardTeam/DnsLibs/issues/105)
* Added XPC support [#174](https://github.com/AdguardTeam/DnsLibs/issues/174)
* Added the dnsproxy_settings::request_timeout setting instead of the upstream specific ones [#163](https://github.com/AdguardTeam/DnsLibs/issues/163)
* Dns-over-QUIC upstream does not respect resolved_ip [#185](https://github.com/AdguardTeam/DnsLibs/issues/185)
* Traffic is routed from DNS 127.0.0.1 to an outbound proxy server [#195](https://github.com/AdguardTeam/DnsLibs/issues/195)
* Added SPKI fingerprint verification feature [#172](https://github.com/AdguardTeam/DnsLibs/issues/172)

---

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.0

- Published: 2023-06-13T18:10:45Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0

## Remarkable сhanges in AdGuard v4.0 for Android

Finally, we are ready to reveal the result of titanic efforts! Let’s take a closer look at AdGuard v4.0 for Android and talk about what has changed since version 3.6. 

### Total reengineering

We've overhauled the entire app, meticulously rewriting every line of code from the ground up. This transformative revamp has resulted in an app that's not only faster, but also smoother than ever before. 

### Complete redesign 

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/ca756813-86ae-428b-8302-12a37266900a" width="300" height="600">
</p>


We've reimagined the design to make the app interface simpler and bring core features to the forefront. Now, to turn on Ad blocking, Tracking protection, Annoyance blocking, or DNS protection along with their filters, you can just tap the corresponding icon above the main switch.

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/831280e2-06fc-4beb-b9f5-bb6ff087097a" width="300" height="600">
</p>



We've also added a separate *Protection* section. Accessible by tapping the shield icon at the bottom of the screen, this section gives you even more control. Apart from the above-mentioned “core” features, this section allows you to manage *Firewall*, *Browsing Security*, and even AdGuard VPN. From the Protection screen, you can turn these modules on or off as you wish and access their settings.

### Firewall

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/55680f16-6c0f-4e0b-9c74-becd45d0966c" width="300" height="600">
</p>



We've uncovered an exciting feature from the depths of AdGuard for Android — *Firewall* – and given it a full-fledged, independent status. With it, you are the master of your domain, deciding which apps can indulge in mobile data or Wi-Fi when the screen is off. It is designed to keep you in the know with real-time notifications of app activities, so nothing escapes your attention.

And for those lightning-fast modifications, head over to the *Quick actions* section where updating firewall rules has never been simpler. With *Firewall*, you can also block apps from accessing the Internet while in roaming, saving your precious megabytes abroad.

### Detailed statistics

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/8cc898c9-685b-4afe-b63c-858e56c0d910" width="300" height="1350">
</p>




A dedicated tab offers comprehensive statistics about all apps, companies, and domains. Wondering which company's requests are blocked most often? Which apps are trying to send your data and to whom? You can quickly identify and block anything suspicious.

### Integration with AdGuard VPN 

As we wrote above, Integrated mode with AdGuard VPN was introduced in AdGuard v3.5 for Android. Until then, users had to go through seven circles of hell to get our ad blocker and VPN to work simultaneously. All because normally two different network-filtering apps can’t work alongside each other on Android.

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/e71cca1e-f1a6-4a06-87cb-0bebde89f1ab" width="300" height="600">
</p>



With the release of AdGuard v4.0 for Android, Integrated mode has become more stable than ever. Previously, each time AdGuard or AdGuard VPN was updated or reinstalled, Integrated mode had to be reconfigured. Now, you configure it once and it will withstand updates and reinstalls while maintaining the integration. In addition, more frequent information exchange between AdGuard Ad Blocker and AdGuard VPN enhances the stability of Integrated mode without affecting performance.

> Changes in Integrated mode are synced between AdGuard v4.0 for Android and AdGuard VPN v2.3 for Android. Be sure to update both apps to the latest versions to enjoy their most stable and smooth simultaneous operation in Integrated mode. 

### Selective app proxying

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/5dd58f40-a43b-4814-b62b-6e7169631e31" width="300" height="600">
</p>




Before AdGuard v4.0 for Android, you could route all of your web traffic through a specified proxy server. With the *Apps operating through proxy* feature, located at *Settings → Filtering → Network → Proxy*, you can now choose which apps will work through your proxy. In addition, *Apps operating through proxy* allows you to specify which apps will route their traffic through AdGuard VPN when operating in Integrated mode. 

### Root access perks

For all the tech enthusiasts out there, the term “root” is no stranger to you. Rooting is essentially unlocking your device to gain more privileged control. If your Android device is rooted, AdGuard v4.0 for Android offers you unprecedented capabilities beyond any previous version of AdGuard Ad Blocker.

Traditionally, AdGuard routes network traffic to its CoreLibs filtering engine by establishing a local VPN. But now, with root access, you can switch AdGuard to the *Automatic proxy* mode. Just navigate to *Settings → Filtering → Network → Routing mode* and switch to *Automatic proxy*. This action takes local VPN out of the picture and instead configures iptables to accomplish the same goals. And there are several benefits to this change.

Firstly, AdGuard is now able to apply DNS filtering to IPv6 requests, something that was not possible before. Secondly, we've ironed out a few issues that hampered AdGuard from accurately associating web requests with their respective apps. This fine-tuning will enhance the performance of Firewall, Filtering log, and so forth. For those of you with rooted devices, this AdGuard update takes your control and customization to a whole new level!

### Low-level settings rework

Diving into the realm of Low-level settings? Found under Settings → General → Advanced, these options are designed with the tech-savvy user in mind. It's a powerful playground, but it's also a place where it's all too easy to mess things up if you're not careful. Despite all the warnings we’ve placed, it's human nature to explore and experiment, often without fully understanding the consequences.

<p align="center">
<img src="https://github.com/AdguardTeam/AdguardForAndroid/assets/107266340/723ce5f2-a8f5-474b-962d-67b82d552045" width="300" height="600">
</p>



In response to this, we've made the Low-level settings more user-friendly and intuitive. It's now easier to understand what each setting does, and even if you do make a mistake, we've implemented security measures like validation checks for entered values to protect you from major missteps.

As for the settings themselves, we've added new ones, retired old ones, and have continued to refine this advanced toolset. A [comprehensive guide on Low-level settings is available in our Knowledge base](https://adguard.com/kb/adguard-for-android/solving-problems/low-level-settings/). So get ready for an enhanced, yet safer deep dive into the depths of customization with AdGuard's advanced settings!

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.0 RC 1

- Published: 2023-06-01T16:30:03Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-rc-1

We are excited to present the first release candidate of AdGuard v4.0 for Android! In this update, we have addressed several issues to improve the overall performance and user experience.

## Changelog
### Fixes
* Show a list of companies related to statistics records when tapping "Show all companies" [#4716](https://github.com/AdguardTeam/AdguardForAndroid/issues/4716)
* In Integration mode, with Proxy enabled, the notification falsely reports the use of a proxy server [#4739](https://github.com/AdguardTeam/AdguardForAndroid/issues/4739)
* Incorrect behavior of sorting order for Apps/Companies [#4730](https://github.com/AdguardTeam/AdguardForAndroid/issues/4730)
* Incorrect behavior of AdGuard after enabling a third-party VPN [#4687](https://github.com/AdguardTeam/AdguardForAndroid/issues/4687)
* Incorrect behavior of app switches in HTTPS-filtered apps [#4729](https://github.com/AdguardTeam/AdguardForAndroid/issues/4729)
* Notification language changes after screen rotation [#4661](https://github.com/AdguardTeam/AdguardForAndroid/issues/4661)
* Recent activity is cleared after quitting the app [#4705](https://github.com/AdguardTeam/AdguardForAndroid/issues/4705)
* Remove parallel resolving from the "Add DNS server" dialogue [#4713](https://github.com/AdguardTeam/AdguardForAndroid/issues/4713)
* Show snack or something like that on the "User rules" screen in some cases [#4712](https://github.com/AdguardTeam/AdguardForAndroid/issues/4712)
* Snack blinks in "Apps operating through proxy" [#4728](https://github.com/AdguardTeam/AdguardForAndroid/issues/4728)
* Some translations don't fit in the fields [#4623](https://github.com/AdguardTeam/AdguardForAndroid/issues/4623)
* Technical version is displayed in the "What's new" popup [#4727](https://github.com/AdguardTeam/AdguardForAndroid/issues/4727)
* The last item does not fit in the Proxy settings on compact devices [#4738](https://github.com/AdguardTeam/AdguardForAndroid/issues/4738)
* The license is not reset after removing the device from the list in the AdGuard account [#4710](https://github.com/AdguardTeam/AdguardForAndroid/issues/4710)
* The requests bar bounces when changing the period of statistics [#4720](https://github.com/AdguardTeam/AdguardForAndroid/issues/4720)
* The update channel is not changed until the app is restarted [#4741](https://github.com/AdguardTeam/AdguardForAndroid/issues/4741)
* Truncated list in HTTPS-filtered apps and apps operating through proxy [#4688](https://github.com/AdguardTeam/AdguardForAndroid/issues/4688)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.0 beta 2

- Published: 2023-05-25T14:23:44Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-beta-2

We’re now in the cleanup phase, so the changelog for the second beta of AdGuard v4.0 for Android is almost entirely bug fixes. This is where we need your help: if you find any problems with this version, please report a bug in the [Android repo](https://github.com/AdguardTeam/AdGuardforAndroid/issues) or vote for an existing bugfix.

Not forgetting the improvements: we updated CoreLibs and DnsLibs, added a couple of features, and worked on the stats screen.

## Changelog

### Features

* Added fast scroll feature to the Recent activity screen [#4617](https://github.com/AdguardTeam/AdguardForAndroid/issues/4617)
* Brought back `pref.proxy.disable.reconfigure` [#4636](https://github.com/AdguardTeam/AdguardForAndroid/issues/4636)
* Changed wording of the stats notification [#4630](https://github.com/AdguardTeam/AdguardForAndroid/issues/4630)
* Once AdGuard and AdGuard VPN are running in the *Integrated mode*, tapping the *Apps* section in the *Exclusions* tab in AdGuard VPN opens the *Apps operating through proxy* screen in AdGuard  [#281](https://github.com/AdguardTeam/AdGuardVPNForAndroid/issues/281)
* Tap on the statistics numbers on the main screen leads to the *Statistics* screen [#4684](https://github.com/AdguardTeam/AdguardForAndroid/issues/4684)
* Statistics numbers on the main screen and statistics screen are updated when AdGuard returns to the foreground [#4633](https://github.com/AdguardTeam/AdguardForAndroid/issues/4633)

### Fixes

* The wrong rule is added through the *Add blocking rule* dialog [#4685](https://github.com/AdguardTeam/AdguardForAndroid/issues/4685)
* Clicking *Buy license* closes the *You've already used your trial license* popup  [#4607](https://github.com/AdguardTeam/AdguardForAndroid/issues/4607)
* The license promo is displayed instead of the filter details screen [#4647](https://github.com/AdguardTeam/AdguardForAndroid/issues/4647)
* Adguard Extra does not work after resetting to default [#4602](https://github.com/AdguardTeam/AdguardForAndroid/issues/4602)
* В строке уведомлений всегда указано, что *Прокси работает*, независимо от состояния прокси [#4545](https://github.com/AdguardTeam/AdguardForAndroid/issues/4545)
* Blinking text on the statistics tab [#4714](https://github.com/AdguardTeam/AdguardForAndroid/issues/4714)
* Tapping the *Clear statistics* button does not remove data from the *Recent activity* section [#4715](https://github.com/AdguardTeam/AdguardForAndroid/issues/4715)
* Disabling *Tracking protection* does not disable the corresponding filter lists [#4599](https://github.com/AdguardTeam/AdguardForAndroid/issues/4599)
* Email auto-fill does not work with password managers [#4627](https://github.com/AdguardTeam/AdguardForAndroid/issues/4627)
* Failed to export certificate into the device storage [#4609](https://github.com/AdguardTeam/AdguardForAndroid/issues/4609)
* Green part of the downloading bar is slightly shifted to the left [#4625](https://github.com/AdguardTeam/AdguardForAndroid/issues/4625)
* Logging in and out of a premium account does not restart protection [#4605](https://github.com/AdguardTeam/AdguardForAndroid/issues/4605)
* The notification that protection is enabled can be dismissed [#4612](https://github.com/AdguardTeam/AdguardForAndroid/issues/4612)
* Protection restarts after enabling the proxy switch with no proxy server on the list [#4681](https://github.com/AdguardTeam/AdguardForAndroid/issues/4681)
* Protection status and icons positioning glitch [#4628](https://github.com/AdguardTeam/AdguardForAndroid/issues/4628)
* Proxy hostname string fails to validate a correct domain name [#4603](https://github.com/AdguardTeam/AdguardForAndroid/issues/4603)
* The list of proxy servers is not scrollable [#4654](https://github.com/AdguardTeam/AdguardForAndroid/issues/4654)
* Proxy settings are not disabled when AdGuard works in the *Integration mode* [#4635](https://github.com/AdguardTeam/AdguardForAndroid/issues/4635)
* Samsung Pay compatibility notification is shown not only to Korean users [#4629](https://github.com/AdguardTeam/AdguardForAndroid/issues/4629)
* Scroll position is not saved in some cases when the *Recent activity* log is filtered by the keyword [#4699](https://github.com/AdguardTeam/AdguardForAndroid/issues/4699)
* The search field is in the focus by default on Android 8 [#4618](https://github.com/AdguardTeam/AdguardForAndroid/issues/4618)
* Snack glitch on the "Apps operating through proxy" screen [#4702](https://github.com/AdguardTeam/AdguardForAndroid/issues/4702)
* Snacks in *Tracking protection* don't disappear [#4665](https://github.com/AdguardTeam/AdguardForAndroid/issues/4665)
* AdGuard crashes on startup [#4649](https://github.com/AdguardTeam/AdguardForAndroid/issues/4649)
* Statistics fail to be converted from GB to TB [#4638](https://github.com/AdguardTeam/AdguardForAndroid/issues/4638)
* The statistics screen for a company is blank if no statistics have been registered for that company in the last 24 hours [#4642](https://github.com/AdguardTeam/AdguardForAndroid/issues/4642)
* On small screens, texts overlap on the *Statistics* tab [#4664](https://github.com/AdguardTeam/AdguardForAndroid/issues/4664)
* The summary is missing on the *Apps operating through proxy* screen [#4696](https://github.com/AdguardTeam/AdguardForAndroid/issues/4696)
* The switch on the home screen changes position after loading statistics [#4678](https://github.com/AdguardTeam/AdguardForAndroid/issues/4678)
* The tooltip for the *Recent activity log* is displayed at the wrong moment [#4701](https://github.com/AdguardTeam/AdguardForAndroid/issues/4701)
* Transitive notification on the *Apps operating through proxy* screen in the *Integrated mode* [#4682](https://github.com/AdguardTeam/AdguardForAndroid/issues/4682)
* Update button is hidden behind the tooltip [#4589](https://github.com/AdguardTeam/AdguardForAndroid/issues/4589)
* Version number is shown on the *Updates screen* instead of the version name [#4690](https://github.com/AdguardTeam/AdguardForAndroid/issues/4690)
* When exiting the Recent activity screen and returning back, the scroll position is retained [#4644](https://github.com/AdguardTeam/AdguardForAndroid/issues/4644)
* The text entered in the custom search bar of the *Recent activity* screen remains after deleting when exiting the section and returning back [#4643](https://github.com/AdguardTeam/AdguardForAndroid/issues/4643)
* The icons on the control panel blink when swiping between tabs in the Home tab [#4592](https://github.com/AdguardTeam/AdguardForAndroid/issues/4592)
* Wrong alignment of a down arrow on the statistics screens [#4700](https://github.com/AdguardTeam/AdguardForAndroid/issues/4700)
* Wrong underlying settings for the *Tracking protection* levels [#4632](https://github.com/AdguardTeam/AdguardForAndroid/issues/4632)
* *App language* option disappears for devices with Chinese as the system language [#4666](https://github.com/AdguardTeam/AdguardForAndroid/issues/4666)

### Versions

* Updated CoreLibs to v1.11.106
* Updated DnsLibs to 2.1.41 [#4675](https://github.com/AdguardTeam/AdguardForAndroid/issues/4675)


#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.0 beta 1

- Published: 2023-04-24T15:04:42Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-beta-1

Remember when we talked about [the first Nightly of AdGuard v4.0 for Android](https://adguard.com/blog/adguard-v4-0-for-android-nightly.html)? It was the first version after a long break — with reworked design and texts, rewritten code, and new features.

Thanks to our development, QA, design, and content teams, we’re releasing the first beta version: refreshed, significantly more stable, and available in multiple languages.

Since the release of the first Nightly version, we’ve fixed more than 100 bugs! Though, it doesn't mean there are no more left (known issues are gathered on [GitHub](https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)). If you encounter any, please let us know. Instructions on how to report bugs are below.
## First Nightly updates

If you haven't read the post about Nightly, [take a look](https://adguard.com/blog/adguard-v4-0-for-android-nightly.html). We wrote a lot about the changes compared to v3.6, the last AdGuard version before v4.0. There’s something useful for those who are not very tech-savvy, as well as for those who understand the details and are willing to dig even into low-level settings.

Here’s a brief overview of the improvements:

  * **Complete redesign**. We made the design lighter, more minimalist, and easier to understand, and put the most important features on a separate screen — now it will be much easier to access them.
<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/protection_en.jpg?0" width="300" height="600">
</p>

  * **Firewall**. Now you can control the access to the Internet for all your apps — if you wish, prevent them from using the Internet without your knowledge.

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/firewall_en.jpg" width="300" height="600">
</p>


  * **Statistics**. Now you can view detailed stats for apps, companies, and domains. Complete transparency!

<p align="center">
<img src="https://cdn.adtidy.org/content/release_notes/ad_blocker/android/statistics_en.jpg?0" width="300" height="600">
</p>


  * **Integration with AdGuard VPN**. We’ve greatly enhanced the stability of the Integrated mode.
  * **Selective app proxying**. Now you can exclude apps from your proxy — even from AdGuard VPN!
  * **Root access perks**. On rooted devices, among other things, you can now apply DNS filtering to IPv6 requests — thanks to the *Automatic proxy* mode.
  * **Easier-to-understand low-level settings**. We’ve updated the design and added clear descriptions as well as input validation so you can be sure that everything is working as it should.

## What’s changed since the first Nightly
### Support for multiple languages

Now the app supports more than 15 languages. But we know there’s much to be improved. If you notice that some translations are missing or if the app is not translated into your language, we’ll be thankful for your contributions on Crowdin. Read more about how to translate AdGuard products in our [Knowledge base](https://adguard.com/kb/miscellaneous/contribute/translate/program/).
### Firewall roaming support

Although this feature was already in the first Nightly version, it didn’t actually work — a truly nightly experience. But now you can block access to the Internet for specific apps when roaming. Megabytes, especially valuable when you're traveling abroad, won't be wasted.
### Import and export of user rules, blocklists, and allowlists

In the first Nightly, you could only import settings as a whole. Now you can import user rules separately. It’s useful if you want to share your rules with someone or transfer them to your other AdGuard apps.

## How to download beta

Visit the [beta page](https://adguard.com/beta.html?platform=android), download the APK file of the beta version, and install it. Done! You’re ready to start exploring.

![How to get the beta version](https://cdn.adtidy.org/content/release_notes/ad_blocker/android/beta_en.png)

Alternatively, you can choose the beta channel right in the app. If you’ve used the Nightly channel, go to *Settings* → *General* → *App and filer updates* and switch to Beta.

If you’re using the Release channel, open Settings* → *General* → *Updates* → *Update channel* and select *Beta*.

> To switch back to the Release channel, you’ll need to reinstall the app.

## Report bugs and vote for feature requests

We’ve already talked about that earlier, so here’s a quick reminder:

1. Check out the [Android repo](https://github.com/AdguardTeam/AdGuardforAndroid/issues) to make sure the issue hasn’t been reported yet.
2. If the issue is new, open the [page for creating new issues](https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose) and select *Bug report*.
3. [Describe the problem](https://adguard.com/kb/guides/report-bugs/#how-to-describe-a-problem). If possible, attach screenshots or a screen recording.

If you want to support the implementation of a new feature or bugfix, you can vote for it on GitHub. To vote, just react with some emoji.

> If you use AdGuard VPN and Ad Blocker in the Integrated mode, download the [beta version of AdGuard VPN](https://adguard-vpn.net/beta.html?platform=android&release=beta).

## In conclusion

We're one step closer to the release we hope you'll enjoy. We would like to thank all the beta testers and translators for their dedication — with your help, bugs get fixed and the app gets better.

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 4.0 Nightly 39

- Published: 2023-01-30T16:59:40Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v4.0-nightly-39

We haven't talked about AdGuard's mobile apps for a long time, but now we're ready to let you in on what we've been up to.

The Android app has been improved so that everyone can enjoy its perks. It is now much simpler to use for people without any technical background and more packed with features for those who want complete control over their data.

Moreover, we've completely rewritten the app so that it runs way faster and smoother.

> Disclaimer: this is a Nightly version — so the app contains more bugs than usual (here's the [list of known issues](https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)). If you're not ready to report bugs, better not take the risk and wait for the release — we're actively working on making the app more stable.

## Updates useful for everyone

### Full redesign

<p align="center">
<img src="https://cdn.adtidy.org/blog/new/iqfm6main.jpg" width="300" height="650">
</p>

Originally, AdGuard for Android has a plethora of features — it serves as an all-purpose tool for blocking ads, trackers, and other threats. While redesigning it, we tried to simplify access to the "core" features, so that all of them are available with a single tap. Now, to turn on Ad blocking, Tracking protection, Annoyance blocking, or DNS protection along with their filters, you can just tap the corresponding icon above the main switch.

<p align="center">
<img src="https://cdn.adtidy.org/blog/new/la0mnprotection.jpg" width="300" height="650">
</p>

We've also added the *Protection* section. You can find it by tapping the shield icon at the bottom of the screen. Apart from the above-mentioned "core" features, this section allows you to manage Firewall, Browsing security, and even AdGuard VPN. On the Protection screen, you may turn these modules on or off as well as easily access their settings.

### Detailed statistics

<p align="center">
<img src="https://cdn.adtidy.org/blog/new/qv07vstatistics.jpg" width="300" height="1200">
</p>

This is not news that apps nowadays do whatever they want with your data and leak it all over the place. And it's quite logical that the user wants complete control over their data. With AdGuard, it's already possible — and now we're introducing a feature that would provide even more transparency! Which apps and companies would potentially leak your data?
With Statistics, you'll now be able to track which apps send your data to global corporations — and block or allow some requests on the fly.

### Firewall

<p align="center">
<img src="https://cdn.adtidy.org/blog/new/40jm3firewall.jpg" width="300" height="650">
</p>

The Android app used to have a functionality similar to Firewall earlier, but it was hidden deep inside the app — in the App management section. Now it's become a completely standalone feature with well-defined scope of actions.

Firewall allows you to control the apps' access to the Internet: decide which apps can use mobile data or Wi-Fi with screen off, get real-time notifications on app activity, and update firewall rules in the Quick actions section.

> The Nightly version is filled to the brim with new features, and this is just the beginning. If you are curious to learn more, read the [blog post](https://adguard.com/en/blog/adguard-v4-0-for-android-nightly.html) — there we cover the advanced features in detail and share our plans for the future. 

## Test it yourself

We need your feedback! [Download](https://agrd.io/android_nightly) the Nightly version of AdGuard v4.0 for Android and (if you're using AdGuard VPN) the [Nightly version of AdGuard VPN](https://adguard-vpn.com/en/beta.html?platform=android&release=nightly), report issues, and send feature requests. Here's the info you might need.

### How to report an issue

If you've noticed a bug, please tell us about it by creating a [GitHub issue](https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose). Describe what you've found and share your logs with devteam@adguard.com — this'll make it easier for us to address the problem.

To collect logs, tap *Settings* → *General* → *Advanced* and select *Export logs and system info*.

> There are things we're already working on — they don't need to be reported. Please consult the **[list of known issues](https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Version%3A+AdGuard+v4.0%22+-label%3A%22Status%3A+Resolved%22)** if you're about to send us a bug report.

### Vote for feature requests

![GitHub reactions](https://cdn.adtidy.org/blog/new/go9q3github_reaction.png)

On [GitHub](https://github.com/AdguardTeam/AdguardForAndroid/issues?q=is%3Aopen+label%3A%22Feature+request%22+sort%3Areactions-%2B1-desc), you can leave your reactions on feature requests. That'll help us find out what most people are interested in. To leave your reaction, select the feature request you like and use an emoji to support its implementation.

## In conclusion

We've never devoted this much attention to a single nightly version — and for a reason. They are usually of interest only to a small number of die-hard enthusiasts. But this time is different. This version heralds huge changes that will soon come to AdGuard Ad Blocker for Android for a lot of people, and we want to do it right.

With your help, the help of the community, we will be able to track down every single bug and tweak all the knobs just right, so that once the update ships to release, millions of AdGuard users will find it perfect.

## 3.6.11

- Published: 2023-01-23T13:18:23Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

You must have been missing AdGuard for Android updates. Well, you won't be bored now, because we're breaking into 2023 with a new release of the product, and we'll only gain traction from there. 

The main changes in AdGuard v3.6.11 for Android were made in our core filtering engine – CoreLibs and DNSLibs. As for the rest, we’ve worked to enhance content filtering and made a bunch of minor changes to improve the application performance. 

## Updated DnsLibs to v2.0.75 [#4324](https://github.com/AdguardTeam/AdguardForAndroid/issues/4324)

A significantly updated version of the DNS filtering library consumes less resources and runs faster. The DNS-over-QUIC protocol implementation now supports the [RFC 9250](https://datatracker.ietf.org/doc/rfc9250/) standard, and the experimental status was removed from the DoQ support.

### First step to Encrypted ClientHello support [DL#161](https://github.com/AdguardTeam/DnsLibs/issues/161)

First of all, what is Encrypted ClientHello? Nowadays, almost every internet connection is encrypted and no one can see what's inside this encrypted connection. However, there is still one little issue with it: the very first packet of the connection indicates the name of the server you are connecting to. Say you want to open `www.google.com`, your ISP cannot see what exactly you send and receive from it, but they know what website you are communicating with. ECH (Encrypted ClientHello) is a new technology that is supposed to solve this issue and encrypt that last bit of unencrypted information.

So what would be the first step to supporting it from AdGuard? Surprisingly, it is to suppress ECH! This can be done by switching on both `pref.dns.block.ech` and `pref.https.redirect.doh` flags in the *Low-level settings*.

But fret not: what we want to achieve is to provide you with ECH support globally so that **all** your apps could benefit from ECH, not just your browser. To accomplish this, AdGuard makes your apps establish regular HTTPS connections with it, and then it will establish a ECH-enabled connection on their behalf. This experimental feature is planned for the next update so stay tuned.

## Updated CoreLibs to v1.10.186

### DNS-over-HTTPS filtering

**Added an option to redirect secure DNS requests to the local DNS proxy [#1563](https://github.com/AdguardTeam/CoreLibs/issues/1563)**

Chrome and Firefox DNS queries sometimes could circumvent DNS filtering by using a DNS-over-HTTPS server. Now AdGuard can automatically filter DNS-over-HTTPS as well.

This feature is experimental and can be enabled in *Low-level settings*, its name is `pref.https.redirect.doh`. In the future versions we're planning to enable it by default.

### Improved content filtering

The following new features are important to filter maintainers and provide advanced capabilities for content filtering. 

#### Enhancement

* Added a new [`$jsonprune` basic rule modifier](https://adguard.com/kb/general/ad-filtering/create-own-filters/#jsonprune-modifier). This modifier allows advanced filtering for JSON responses [#1447](https://github.com/AdguardTeam/CoreLibs/issues/1447)
* Added a new [`$hls` basic rule modifier](https://adguard.com/kb/general/ad-filtering/create-own-filters/#hls-modifier). This modifier provides advanced filtering capabilities for modifying HTTP live streaming files which will help with preventing video ads. [#1434](https://github.com/AdguardTeam/CoreLibs/issues/1434)
* Expanded capabilities of the `$stealth` modifier. Filters maintainers can now specify which Stealth Mode features should be disabled for a given URL. Before that change the only option was to completely disable Stealth Mode. [#1224](https://github.com/AdguardTeam/CoreLibs/issues/1224)
* Added support for empty `$path` modifier for non-basic rules. [#1591](https://github.com/AdguardTeam/CoreLibs/issues/1591)
* `$removeparam` can now be applied to POST requests. [#1573](https://github.com/AdguardTeam/CoreLibs/issues/1573)

#### Fixed

* *Hide your Referrer from third-parties* Stealth mode option interferes with the `$third-party` modifier [#1640](https://github.com/AdguardTeam/CoreLibs/issues/1640)
* Cosmetic rules with `:where()` pseudo-class are rejected [#1609](https://github.com/AdguardTeam/CoreLibs/issues/1609)
* Rules with `$third-party` modifier block resources from the site's own subdomain [#1637](https://github.com/AdguardTeam/CoreLibs/issues/1637)
* Rules with the `$all` modifier do not block explicitly visited sites [#1590](https://github.com/AdguardTeam/CoreLibs/issues/1590)

## Other improvements

* Enabled HTTPS filtering by default for Soul Browser [#4202](https://github.com/AdguardTeam/AdguardForAndroid/issues/4202)

## Other fixes

* When confirming 2FA the code entry page disappears in some cases
* AdGuard does not create a local VPN and protection does not start [#4269](https://github.com/AdguardTeam/AdguardForAndroid/issues/4269)
* Internet fails to work when a network is changing from Wi-Fi to mobile data [#4265](https://github.com/AdguardTeam/AdguardForAndroid/issues/4265)
* Compatibility issue with iRobot Home app [#4273](https://github.com/AdguardTeam/AdguardForAndroid/issues/4273)

AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.11 beta 2

- Published: 2023-01-18T16:58:16Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11-beta-2

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

They say that two betas before a release is a good sign. Today we are releasing the second beta of AdGuard v3.6.11 for Android with only one change: updated DnsLibs.

## Changelog


### Enhancement
* Updated DnsLibs to v2.0.75 [#4324](https://github.com/AdguardTeam/AdguardForAndroid/issues/4324)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.11 beta 1

- Published: 2023-01-13T17:12:36Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.11-beta-1

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

You must have been missing AdGuard for Android updates. Well, you won't be bored now, because we're breaking into 2023 with a new beta version of the product, and we'll only gain traction from there. 

The main changes in AdGuard v3.6.11 for Android beta were made in our core filtering engine – CoreLibs and DNSLibs. As for the rest, we’ve worked to enhance content filtering and made a bunch of minor changes to improve the application performance. 

## Updated DnsLibs to v2.0.66

A significantly updated version of the DNS filtering library consumes less resources and runs faster. The DNS-over-QUIC protocol implementation now supports the [RFC 9250](https://datatracker.ietf.org/doc/rfc9250/) standard, and the experimental status was removed from the DoQ support.

### First step to Encrypted ClientHello support [DL#161](https://github.com/AdguardTeam/DnsLibs/issues/161)

First of all, what is Encrypted ClientHello? Nowadays, almost every internet connection is encrypted and no one can see what's inside this encrypted connection. However, there is still one little issue with it: the very first packet of the connection indicates the name of the server you are connecting to. Say you want to open `www.google.com`, your ISP cannot see what exactly you send and receive from it, but they know what website you are communicating with. ECH (Encrypted ClientHello) is a new technology that is supposed to solve this issue and encrypt only the last bit of unencrypted information.

So what would be the first step to supporting it from AdGuard? Surprisingly, it is to suppress it! This can be done by switching both `pref.dns.block.ech` and `pref.https.redirect.doh` flags in the *Low Level Settings*.

But fret not: what we want to achieve is to provide you with ECH support globally so that **all** your apps could benefit from ECH, not just your browser. To accomplish this, AdGuard makes your apps establish regular HTTPS connections with it, and then it will establish a ECH-enabled connection on their behalf. This experimental feature is planned for the next update so stay tuned.

## Updated CoreLibs to v1.10.186

### DNS-over-HTTPS filtering

**Added an option to redirect secure DNS requests to the local DNS proxy [#1563](https://github.com/AdguardTeam/CoreLibs/issues/1563)**

Chrome and Firefox DNS queries sometimes could circumvent DNS filtering by using a DNS-over-HTTPS server. Now AdGuard can automatically filter DNS-over-HTTPS as well.

This feature is experimental and can be enabled in *Low Level Settings*, its name is `pref.https.redirect.doh`. In the future versions we're planning to enable it by default.

### Improved content filtering

The following new features are important to filter maintainers and provide advanced capabilities for content filtering. 

#### Enhancement

* Added a new [`$jsonprune` basic rule modifier](https://adguard.com/kb/general/ad-filtering/create-own-filters/#jsonprune-modifier). This modifier allows advanced filtering for JSON responses [#1447](https://github.com/AdguardTeam/CoreLibs/issues/1447)
* Added a new [`$hls` basic rule modifier](https://adguard.com/kb/general/ad-filtering/create-own-filters/#hls-modifier). This modifier provides advanced filtering capabilities for modifying HTTP live streaming files which will help with preventing video ads. [#1434](https://github.com/AdguardTeam/CoreLibs/issues/1434)
* Expanded capabilities of the `$stealth` modifier. Filters maintainers can now specify which Stealth Mode features should be disabled for a given URL. Before that change the only option was to completely disable Stealth Mode. [#1224](https://github.com/AdguardTeam/CoreLibs/issues/1224)
* Added support for empty `$path` modifier for non-basic rules. [#1591](https://github.com/AdguardTeam/CoreLibs/issues/1591)
* `$removeparam` can now be applied to POST requests. [#1573](https://github.com/AdguardTeam/CoreLibs/issues/1573)

#### Fixed

* *Hide your Referrer from third-parties* Stealth mode option interferes with the `$third-party` modifier [#1640](https://github.com/AdguardTeam/CoreLibs/issues/1640)
* Cosmetic rules with `:where()` pseudo-class are rejected [#1609](https://github.com/AdguardTeam/CoreLibs/issues/1609)
* Rules with `$third-party` modifier block resources from the site's own subdomain [#1637](https://github.com/AdguardTeam/CoreLibs/issues/1637)
* Rules with the `$all` modifier do not block explicitly visited sites [#1590](https://github.com/AdguardTeam/CoreLibs/issues/1590)

## Other improvements

* Enabled HTTPS filtering by default for Soul Browser [#4202](https://github.com/AdguardTeam/AdguardForAndroid/issues/4202)

## Other fixes

* When confirming 2FA the code entry page disappears in some cases
* AdGuard does not create a local VPN and protection does not start [#4269](https://github.com/AdguardTeam/AdguardForAndroid/issues/4269)
* Internet fails to work when a network is changing from Wi-Fi to mobile data [#4265](https://github.com/AdguardTeam/AdguardForAndroid/issues/4265)
* Compatibility issue with iRobot Home app [#4273](https://github.com/AdguardTeam/AdguardForAndroid/issues/4273)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.10

- Published: 2022-08-26T16:36:40Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

In this version we’ve improved connectivity check — now the app determines better whether there is internet connection.

AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.10 Beta 2

- Published: 2022-08-25T18:14:18Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10-beta-2

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

This is a technical beta update aimed to fix minor bugs.

**AdGuard for Android direct download links:**

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.10 Beta 1

- Published: 2022-08-23T14:23:22Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.10-beta-1

>Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

In AdGuard v3.6.10 for Android we’ve improved connectivity check — now the app determines better whether there is internet connection.

**AdGuard for Android direct download links:**

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.9

- Published: 2022-08-02T21:14:15Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.9

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

This is a technical update aimed to increase the app stability and fix minor bugs.

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.9 Beta 1

- Published: 2022-08-01T20:11:15Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.9-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

This is a technical update aimed to increase the app stability and fix minor bugs.

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.8

- Published: 2022-04-28T15:55:31Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.8

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

In this version we've added a new feature — 'Protect from DPI'. In a nutshell, it modifies your outgoing traffic to prevent ISP's Deep Packet Inspection systems from detecting the websites you visit. To make this feature visible and enable it, select 'Custom' in the Stealth Mode tab and scroll down.

Besides, we've fixed extensions settings and enabled HTTPS filtering by default for Naver Whale Browser. Finally, CoreLibs and DnsLibs were updated.

### Changelog

* [Fixed] AdGuard not turning on inside Samsung secure folder, Android 12 [#4073](https://github.com/AdguardTeam/AdguardForAndroid/issues/4073)
* [Fixed] Replace the "Move certificate" with "AdGuard certificate" as a recommended Magisk module [#4126](https://github.com/AdguardTeam/AdguardForAndroid/issues/4126)
* [Fixed] Check "pref.dns.blocking.type" translations, they seem to be outdated [#4133](https://github.com/AdguardTeam/AdguardForAndroid/issues/4133)
* [Fixed] The URL in about wrongly includes the front words (zh-TW) [#3654](https://github.com/AdguardTeam/AdguardForAndroid/issues/3654)
* [Fixed] Make sure that we open proper settings section when installing a certificate on Samsung devices [#4115](https://github.com/AdguardTeam/AdguardForAndroid/issues/4115) 
* [Fixed] Add an DPI-bypass option to AdGuard Stealth Mode [#4131](https://github.com/AdguardTeam/AdguardForAndroid/issues/4131)
* [Other] Update CoreLibs and DnsLibs to their latest versions

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.8 beta 1

- Published: 2022-04-25T15:42:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.8-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

In this beta we've added a new feature — 'Protect from DPI'. In a nutshell, it modifies your outgoing traffic to prevent ISP's Deep Packet Inspection systems from detecting the websites you visit. To make this feature visible and enable it, select 'Custom' in the Stealth Mode tab and scroll down.

Besides, we've fixed extensions settings and enabled HTTPS filtering by default for Naver Whale Browser. Finally, CoreLibs and DnsLibs were updated.

### Changelog

* [Other] Update CoreLibs to 1.9.57 [#4135](https://github.com/AdguardTeam/AdguardForAndroid/issues/4135)
* [Other] Update DnsLibs to 1.7.11 [#4121](https://github.com/AdguardTeam/AdguardForAndroid/issues/4121)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.7

- Published: 2022-02-02T13:37:47Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.7

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

📲  Lately some of our users experienced discomfort — they couldn’t make voice calls in WhatsApp when AdGuard v3.6.6 for Android is enabled. The CoreLibs team managed to combat this problem.
:books: Besides, we’ve made several fixes to [the scriptlets library](https://github.com/AdguardTeam/Scriptlets). To recap, scriptlets are powerful blocking tools. In particular, they carry out a noble mission: to neutralize anti ad blockers. The previous version of AdGuard for Android had a scriptlet library that contained an incorrect fix for rules like `#%#/scriptlet(“abort-current-inline-script”, ...)`, which could break some web pages; now the problem is solved.
Having dealt with all the issues, we’re ready to present a new version. Please meet v3.6.7, we’ve done our best for it to function smoothly. 

### Changelog

* [Fixed] AdGuard breaks calls in WhatsApp [#4080](https://github.com/AdguardTeam/AdguardForAndroid/issues/4080)
* [Enhancement] CoreLibs to v1.8.285 [#4089](https://github.com/AdguardTeam/AdguardForAndroid/issues/4089)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.7 beta 1

- Published: 2022-01-25T12:13:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.7-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

📲  Lately some of our users experienced discomfort — they couldn’t make voice calls in WhatsApp when AdGuard v3.6.6 for Android is enabled. The CoreLibs team managed to combat this problem.
:books: Besides, we’ve made several fixes to [the scriptlets library](https://github.com/AdguardTeam/Scriptlets). To recap, scriptlets are powerful blocking tools. In particular, they carry out a noble mission: to neutralize anti ad blockers. The previous version of AdGuard for Android had a scriptlet library that contained an incorrect fix for rules like `#%#/scriptlet(“abort-current-inline-script”, ...)`, which could break some web pages; now the problem is solved.
Having dealt with all the issues, we’re ready to present a new version. Please meet v3.6.7-beta, we’ve done our best for it to function smoothly. 

### Changelog

* [Fixed] AdGuard breaks calls in WhatsApp [#4080](https://github.com/AdguardTeam/AdguardForAndroid/issues/4080)
* [Enhancement] CoreLibs to v1.8.285 [#4089](https://github.com/AdguardTeam/AdguardForAndroid/issues/4089)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.6

- Published: 2021-12-30T10:55:42Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.6

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

After the last update of AdGuard for Android, some users may have encountered the problem of the app crashing when using earlier versions of the Firefox browser. Well, we decided to close all debts this year and release the patch today. We also did something that no release can do without: we updated CoreLibs. 

### Changelog

* [Fixed] AdGuard crashes while using earlier versions of FireFox browser [#4068](https://github.com/AdguardTeam/AdguardForAndroid/issues/4068)
* [Enhancement] Updated CoreLibs to v1.8.281 [#4076](https://github.com/AdguardTeam/AdguardForAndroid/issues/4076)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.5

- Published: 2021-12-17T11:39:26Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.5

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

It's time to release AdGuard v3.6.5 for Android. The biggest thing about this version is the enhanced Browsing Security module which now blocks requests to malicious and phishing sites better and faster! No less important point is that we’ve updated CoreLibs and DNSLibs to make the app perform more reliably, and fixed various minor bugs. Hope you will enjoy AdGuard v3.6.5 for Android! 

* **[Enhancement] Enhanced Browsing Security module**

With the implementation of new Safe Browsing API v2, Browsing Security module responsible for blocking requests to malicious and phishing sites has become more effective. The upgraded version of this module makes browsing the Internet safer than ever and leaves no chance for the malicious code to be executed.

### Changelog

* [Fixed] Keenetic app compatibility issue with AdGuard [#4035](https://github.com/AdguardTeam/AdguardForAndroid/issues/4035)
* [Fixed] Cosmote Greek carrier VoWiFi blocking [#3821](https://github.com/AdguardTeam/AdguardForAndroid/issues/3821)
* [Enhancement] Add 360 browser to the list of browsers [#4040](https://github.com/AdguardTeam/AdguardForAndroid/issues/4040)
* [Enhancement] Updated CoreLibs to v1.8.274 [#4061](https://github.com/AdguardTeam/AdguardForAndroid/issues/4061)
* [Enhancement] Updated DnsLibs to v1.6.70 [#4051](https://github.com/AdguardTeam/AdguardForAndroid/issues/4051)


#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.5 beta

- Published: 2021-12-02T12:51:50Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.5-beta

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Meet AdGuard v.3.6.5 for Android beta! There aren't many changes in it, but they're all pretty important. The main news is that we've upgraded the Safebrowsing module, so you can now surf the web feeling safer than ever before. What’s more? Of course, we’ve updated CoreLibs and DNSLibs (otherwise it wouldn't be a true release). Hope you’ll enjoy the new version! 

* **[Enhancement] Safebrowsing v2.0**
Safebrowsing, which is responsible for blocking requests to malicious and phishing sites, has been upgraded. The new version of this module makes browsing the Internet safer than ever.

### Changelog

* [Fixed] Keenetic app compatibility issue with AdGuard [#4035](https://github.com/AdguardTeam/AdguardForAndroid/issues/4035)
* [Fixed] Cosmote Greek carrier VoWiFi blocking [#3821](https://github.com/AdguardTeam/AdguardForAndroid/issues/3821)
* [Enhancement] Add 360 browser to the list of browsers [#4040](https://github.com/AdguardTeam/AdguardForAndroid/issues/4040)
* [Enhancement] Updated CoreLibs to v1.8.256 [#1000](https://github.com/AdguardTeam/AdguardForMac/issues/1000)
* [Enhancement] Updated DnsLibs to v1.6.66 [#989](https://github.com/AdguardTeam/AdguardForMac/issues/989)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.4

- Published: 2021-09-17T13:02:29Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.4

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

This quick update fixes a bug that could have happened to our long-term users. If you have been using AdGuard for a few years and your security certificate expired, it could have lead to an HTTPS filtering failure. After this update, you will see a notification on the app’s main screen. Tap on it and follow on-screen instructions to reinstall the certificate and resume HTTPS filtering.

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.3

- Published: 2021-09-08T14:53:39Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.3

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

In this version we focused on updating CoreLibs. Namely, we dealt with the priority of existing modifiers and added several new ones: `$denyallow`, `$redirect-rule`, `$removeheader`, and `$specifichide`. It might be of interest to users who’d like to [create their own ad filters](https://kb.adguard.com/en/general/how-to-create-your-own-ad-filters). Besides, we’ve made userscript exclusions work properly and fixed all issues found.
We know you are waiting for v4.0, so are we. Trust us, it’s worth it.

### Changelog

* [Fixed] Proxy gets disabled after each AdGuard VPN update [#3680](https://github.com/AdguardTeam/AdguardForAndroid/issues/3680)
* [Fixed] Stealth mode settings configured in the setup wizard are not applied [#3747](https://github.com/AdguardTeam/AdguardForAndroid/issues/3747)
* [Fixed] AdGuard doesn't let users of the MEGA app log in [#3837](https://github.com/AdguardTeam/AdguardForAndroid/issues/3837)
* [Fixed] "NetworkCallback was not registered" error when stopping protection [#3870](https://github.com/AdguardTeam/AdguardForAndroid/issues/3870)
* [Fixed] Instagram doesn't work in Local HTTP Proxy mode (root access) [#3879](https://github.com/AdguardTeam/AdguardForAndroid/issues/3879)
* [Fixed] NektoMe doesn't work when AdGuard is enabled [#374](https://github.com/AdguardTeam/AdguardForAndroid/issues/374)
* [Fixed] If a phone has access to an IPv6 connection, AdGuard for Android fails to connect to DNS-over-QUIC servers that are only accessible over IPv4 [#3927](https://github.com/AdguardTeam/AdguardForAndroid/issues/3927)
* [Fixed] The issue with changing the language in the DNS section [#3731](https://github.com/AdguardTeam/AdguardForAndroid/issues/3731)
* [Fixed] Root + Local HTTP proxy slowdown on Android 7 [#3844](https://github.com/AdguardTeam/AdguardForAndroid/issues/3844)
* [Fixed] Check proxy connection status error [#3848](https://github.com/AdguardTeam/AdguardForAndroid/issues/3848)
* [Fixed] TikTok doesn't work when AdGuard is enabled [#3866](https://github.com/AdguardTeam/AdguardForAndroid/issues/3866)
* [Fixed] Wrong exclusions suggested for `$removeparam` rules in the filtering log [#3873](https://github.com/AdguardTeam/AdguardForAndroid/issues/3873)
* [Fixed] Don't pass DNS64 settings to DNSLibs if IPv4 network interface is present [#3886](https://github.com/AdguardTeam/AdguardForAndroid/issues/3886)
* [Fixed] Connection issues on Fujitsu devices
* [Fixed] Issue with an expired security certificate
* [Fixed] Extend public networks list to force IPv4 default route
* [Fixed] `com.android.browser` connection issues on several devices
* [Fixed] Stealth mode screen can't be scrolled
* [Enhancement] Updated DnsLibs to v1.6.29 [#3952](https://github.com/AdguardTeam/AdguardForAndroid/issues/3952)
* [Enhancement] DNS-over-QUIC (Removed "experimental" label) [#3842](https://github.com/AdguardTeam/AdguardForAndroid/issues/3842)
* [Enhancement] Turkey - Turkcell VoWifi new IP address [#3864](https://github.com/AdguardTeam/AdguardForAndroid/issues/3864)
* [Enhancement] Fanboy's Annoyance List's Subscription URL is broken [#3865](https://github.com/AdguardTeam/AdguardForAndroid/issues/3865)
* [Enhancement] Enable HTTPS filtering by default for Edge Dev, Edge Beta, and Styx Browser [#3897](https://github.com/AdguardTeam/AdguardForAndroid/issues/3897)
* [Enhancement] Do not hardcode excluding AdGuard VPN package from filtering [#3923](https://github.com/AdguardTeam/AdguardForAndroid/issues/3923)
* [Enhancement] Added Yandex Browser to the list of browsers [#3951](https://github.com/AdguardTeam/AdguardForAndroid/issues/3951)

### Updated CoreLibs to v1.8.163 [#3945](https://github.com/AdguardTeam/AdguardForAndroid/issues/3945)

* [Fixed] Rule with `$important` modifier should has higher priority than rule with `$all` modifier [#1440](https://github.com/AdguardTeam/CoreLibs/issues/1440)
* [Fixed] Userscript exclusions do not work as they should [#1425](https://github.com/AdguardTeam/CoreLibs/issues/1425)
* [Enhancement] Add `$denyallow` modifier [#1304](https://github.com/AdguardTeam/CoreLibs/issues/1304)
* [Enhancement] Add `$redirect-rule` modifier [#1303](https://github.com/AdguardTeam/CoreLibs/issues/1303)
* [Enhancement] Add `$removeheader` modifier [#1427](https://github.com/AdguardTeam/CoreLibs/issues/1427)
* [Enhancement] Add `$specifichide` modifier [#1166](https://github.com/AdguardTeam/CoreLibs/issues/1166)
* [Enhancement] Add an option to send Global Privacy Control's Do NotSell signal to Stealth Mode [#1451](https://github.com/AdguardTeam/CoreLibs/issues/1451)
* [Enhancement] Improve the way negation works for `$redirect` rules [#1388](https://github.com/AdguardTeam/CoreLibs/issues/1388)
* [Other] Rules with `$extension` modifier unblock blocked requests [#1350](https://github.com/AdguardTeam/CoreLibs/issues/1350)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.3 beta

- Published: 2021-08-31T15:11:34Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.3-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Do you remember the day when we solemnly announced that AdGuard v4.0 for Android is coming? Today, standing at the threshold of a new era and foreseeing bright prospects, we are finally releasing it... v3.6.3 beta. Ba-dum-tss!

### Changelog

* [Fixed] Proxy gets disabled after each AdGuard VPN update [#3680](https://github.com/AdguardTeam/AdguardForAndroid/issues/3680)
* [Fixed] Stealth mode settings configured in the setup wizard are not applied [#3747](https://github.com/AdguardTeam/AdguardForAndroid/issues/3747)
* [Fixed] AdGuard doesn't let users of the MEGA app log in [#3837](https://github.com/AdguardTeam/AdguardForAndroid/issues/3837)
* [Fixed] "NetworkCallback was not registered" error when stopping protection [#3870](https://github.com/AdguardTeam/AdguardForAndroid/issues/3870)
* [Fixed] Instagram doesn't work in Local HTTP Proxy mode (root access) [#3879](https://github.com/AdguardTeam/AdguardForAndroid/issues/3879)
* [Fixed] NektoMe doesn't work when AdGuard is enabled [#374](https://github.com/AdguardTeam/AdguardForAndroid/issues/374)
* [Fixed] If a phone has access to an IPv6 connection, AdGuard for Android fails to connect to DNS-over-QUIC servers that are only accessible over IPv4 [#3927](https://github.com/AdguardTeam/AdguardForAndroid/issues/3927)
* [Fixed] The issue with changing the language in the DNS section [#3731](https://github.com/AdguardTeam/AdguardForAndroid/issues/3731)
* [Fixed] Root + Local HTTP proxy slowdown on Android 7 [#3844](https://github.com/AdguardTeam/AdguardForAndroid/issues/3844)
* [Fixed] Check proxy connection status error [#3848](https://github.com/AdguardTeam/AdguardForAndroid/issues/3848)
* [Fixed] TikTok doesn't work when AdGuard is enabled [#3866](https://github.com/AdguardTeam/AdguardForAndroid/issues/3866)
* [Fixed] Wrong exclusions suggested for $removeparam rules in the filtering log [#3873](https://github.com/AdguardTeam/AdguardForAndroid/issues/3873)
* [Fixed] Don't pass DNS64 settings to DNSLibs if IPv4 network interface is present [#3886](https://github.com/AdguardTeam/AdguardForAndroid/issues/3886)
* [Fixed] Connection issues on Fujitsu devices
* [Fixed] Issue with an expired security certificate
* [Fixed] Extend public networks list to force IPv4 default route
* [Fixed] com.android.browser connection issues on several devices
* [Fixed] Stealth mode screen can't be scrolled
* [Enhancement] Updated CoreLibs to v1.8.163 [#3945](https://github.com/AdguardTeam/AdguardForAndroid/issues/3945)
* [Enhancement] Updated DnsLibs to v1.6.29 [#3952](https://github.com/AdguardTeam/AdguardForAndroid/issues/3952)
* [Enhancement] DNS-over-QUIC (Removed "experimental" label) [#3842](https://github.com/AdguardTeam/AdguardForAndroid/issues/3842)
* [Enhancement] Turkey - Turkcell VoWifi new IP address [#3864](https://github.com/AdguardTeam/AdguardForAndroid/issues/3864)
* [Enhancement] Fanboy's Annoyance List's Subscription URL is broken [#3865](https://github.com/AdguardTeam/AdguardForAndroid/issues/3865)
* [Enhancement] Enable HTTPS filtering by default for Edge Dev, Edge Beta, and Styx Browser [#3897](https://github.com/AdguardTeam/AdguardForAndroid/issues/3897)
* [Enhancement] Do not hardcode excluding AdGuard VPN package from filtering [#3923](https://github.com/AdguardTeam/AdguardForAndroid/issues/3923)
* [Enhancement] Added Yandex Browser to the list of browsers [#3951](https://github.com/AdguardTeam/AdguardForAndroid/issues/3951)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.2

- Published: 2021-05-13T14:29:46Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Well, well, 3.6.2 release arrived. One beta and two RCs have proved successful, we said, “Hooray,” and released the final version right away.

So, what’s inside it? We could write about updated CoreLibs and DnsLibs, improved data collection for reports and minor issues like parsing SDNS links for DoQ servers, but honestly, not many people would understand what the hell it means. Trust us, the app has only gotten better!

P.S. v4.0 is coming. Hopefully, v3.6.2 will be the last way station before the new era.

<img src="https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/Starken.png">

### Changelog

* [Enhancement] Added Microsoft Edge Canary browser to the list of supported browsers [#3808](https://github.com/AdguardTeam/AdguardForAndroid/issues/3808)
* [Enhancement] Added Iceraven Browser to the list of supported browsers [#3797](https://github.com/AdguardTeam/AdguardForAndroid/issues/3797)
* [Enhancement] Added QQ and UC browsers to the list of supported browsers [#3707](https://github.com/AdguardTeam/AdguardForAndroid/issues/3707)
* [Enhancement] Added Privacy Browser to the list of supported browsers [#3677](https://github.com/AdguardTeam/AdguardForAndroid/issues/3677)
* [Enhancement] Added Vivaldi Snapshot to the HTTPS filtering list [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)
* [Enhancement] Added popular Wi-Fi calling servers to the default exclusions list [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Enhancement] Added posteitaliane.posteapp.appbpol to exclusions [#3756](https://github.com/AdguardTeam/AdguardForAndroid/issues/3756)
* [Fixed] Built-in iptables is missing support for “-p dport” [#3782](https://github.com/AdguardTeam/AdguardForAndroid/issues/3782)
* [Fixed] Disable HTTPS filtering for com.google.android.feedback [#3655](https://github.com/AdguardTeam/AdguardForAndroid/issues/3655)
* [Fixed] Unable to get a trial period [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [Fixed] com.tomtom.amigo.huawei app incompatibility [#3767](https://github.com/AdguardTeam/AdguardForAndroid/issues/3767)
* [Fixed] de.avm.android.fritzapp — VoIP/SIP issue [#3810](https://github.com/AdguardTeam/AdguardForAndroid/issues/3810)
* [Fixed] Buffer was exhausted while reading /proc/net/tcp6 [#3832](https://github.com/AdguardTeam/AdguardForAndroid/issues/3832)
* [Other] Added Kurdish localization [#3774](https://github.com/AdguardTeam/AdguardForAndroid/issues/3774)
* [Other] Updated DnsLibs to v1.5.26 [#3829](https://github.com/AdguardTeam/AdguardForAndroid/issues/3829)
* [Other] Added “UniFi Network” to the apps exclusions list
#### Updated CoreLibs to v1.7.211
* [Fixed] CSS rules with ```URL``` shouldn’t be allowed [#1431](https://github.com/AdguardTeam/CoreLibs/issues/1431)
* [Fixed] HTTPS filtering issue at hepsiburada.com [#1406](https://github.com/AdguardTeam/CoreLibs/issues/1406)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.2 RC 2

- Published: 2021-05-11T11:31:40Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-rc-2

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Here comes the second release candidate for AdGuard v3.6.2 for Android. We've made it so that AdGuard will perform better on the devices where multiple proxies are in use. Plus, DnsLibs have been updated one more time.

### Changelog

* [Fixed] Buffer was exhausted while reading /proc/net/tcp6 [#3832](https://github.com/AdguardTeam/AdguardForAndroid/issues/3832)
* [Other] Updated DnsLibs to v1.5.26

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.2 RC 1

- Published: 2021-04-30T13:35:19Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-rc-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Meet the release candidate for AdGuard v3.6.2 for Android. Only two tasks separate it from the final version. Next stop, release.

### Changelog

* [Fixed] HTTPS filtering issue at hepsiburada.com [#1406](https://github.com/AdguardTeam/CoreLibs/issues/1406)
* [Other] Updated DnsLibs to v1.5.24

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.2 beta 1

- Published: 2021-04-27T19:02:59Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.2-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Meet AdGuard v3.6.2 for Android beta! In this version we’ve updated CoreLibs and DnsLibs to v1.7.211 and to v1.5.18 respectively, added a few apps to the list of exclusions, and improved data collection for submitting reports. Besides, we have fixed some other minor issues like parsing SDNS links for DoQ servers. 

### Changelog

* [Enhancement] Added Microsoft Edge Canary browser to the list of supported browsers [#3808](https://github.com/AdguardTeam/AdguardForAndroid/issues/3808)
* [Enhancement] Added Iceraven Browser to the list of supported browsers [#3797](https://github.com/AdguardTeam/AdguardForAndroid/issues/3797)
* [Enhancement] Added QQ and UC browsers to the list of supported browsers [#3707](https://github.com/AdguardTeam/AdguardForAndroid/issues/3707)
* [Enhancement] Added Vivaldi Snapshot to the HTTPS filtering list [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)
* [Enhancement] Privacy Browser Support [#3677](https://github.com/AdguardTeam/AdguardForAndroid/issues/3677)
* [Enhancement] Added popular Wi-Fi calling servers to the default exclusions list [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Enhancement] Added posteitaliane.posteapp.appbpol to exclusions [#3756](https://github.com/AdguardTeam/AdguardForAndroid/issues/3756)
* [Enhancement] Updated CoreLibs to v1.7.180 [#3737](https://github.com/AdguardTeam/AdguardForAndroid/issues/3737)
* [Fixed] Built-in iptables is missing support for “-p dport” [#3782](https://github.com/AdguardTeam/AdguardForAndroid/issues/3782)
* [Fixed] Disable HTTPS filtering for com.google.android.feedback [#3655](https://github.com/AdguardTeam/AdguardForAndroid/issues/3655)
* [Fixed] Unable to get a trial period [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [Fixed] com.tomtom.amigo.huawei app incompatibility [#3767](https://github.com/AdguardTeam/AdguardForAndroid/issues/3767)
* [Fixed] de.avm.android.fritzapp — VoIP/SIP issue [#3810](https://github.com/AdguardTeam/AdguardForAndroid/issues/3810)
* [Other] Added Kurdish localization [#3774](https://github.com/AdguardTeam/AdguardForAndroid/issues/3774)
* [Other] Added “UniFi Network” to the apps exclusions list
* [Other] Updated DnsLibs to v1.5.18 
* [Other] Updated CoreLibs to v1.7.211
* [Fixed] CSS rules with ```URL``` shouldn’t be allowed [#1431](https://github.com/AdguardTeam/CoreLibs/issues/1431)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.1

- Published: 2021-02-19T11:49:04Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Another round of software release life cycle complete! This version of AdGuard for Android has made its way from an unsure of itself alpha to a confident release. We have routinely updated CoreLibs, fixed a couple of bugs and compatibility issues. This time, there are no shocking features like watching YouTube without ads but this release is no less important than the previous one. After all, we are getting better with every update!

### Changelog

* [Enhancement] CoreLibs updated to v1.7.189 [#3749](https://github.com/AdguardTeam/AdguardForAndroid/issues/3749)
* [Fixed] Filtering doesn't work with 4G and IPv6 [#3527](https://github.com/AdguardTeam/AdguardForAndroid/issues/3527)
* [Fixed] An error when trying to get a trial period via the app [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [Fixed] hepsiburada.com - HTTPS filtering issue [#1406](https://github.com/AdguardTeam/CoreLibs/issues/1406)
* [Fixed] blockchain.com is broken [#1411](https://github.com/AdguardTeam/CoreLibs/issues/1411)
* [Fixed] Compatibility issues
* [Other] Several popular Wi-Fi calling servers added to the default exclusions list [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Other] HTTPS filtering for Vivaldi Snapshot browser is enabled by default now [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6.1 beta 1

- Published: 2021-02-15T16:15:08Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6.1-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

This is the first beta on the way towards AdGuard v4.0. We fixed a couple of bugs, did a routine CoreLibs update, and made a few other changes.

### Changelog

* [Enhancement] CoreLibs updated to v1.7.188 [#3743](https://github.com/AdguardTeam/AdguardForAndroid/issues/3743)
* [Fixed] Filtering doesn't work with 4G and IPv6 [#3527](https://github.com/AdguardTeam/AdguardForAndroid/issues/3527)
* [Fixed] An error when trying to get a trial period via the app [#3691](https://github.com/AdguardTeam/AdguardForAndroid/issues/3691)
* [Fixed] Compatibility issues
* [Other] Several popular Wi-Fi calling servers added to the default exclusions list [#3742](https://github.com/AdguardTeam/AdguardForAndroid/issues/3742)
* [Other] HTTPS filtering for Vivaldi Snapshot browser is enabled by default now [#3741](https://github.com/AdguardTeam/AdguardForAndroid/issues/3741)

#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.6

- Published: 2020-12-15T10:43:20Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

AdGuard for Android v3.6 is headlined by two pretty big changes, new features even. It's watching YouTube ad-free inside the app and DNS-over-QUIC protocol support. The first one is easy to grasp, the second one will take some explaining. 
​

**[Enhancement] An option to watch Youtube ad-free [#2994](https://github.com/AdguardTeam/AdguardForAndroid/issues/2994)**
​
Blocking ads in YouTube on Android has been exclusive to browsers for a long time, thanks to the restrictions Android OS imposes on filtering other apps' traffic. However, we found a way for you to avoid ads in YouTube app. Follow these easy steps:
​
<img src="https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/share.gif" style="border: 1px solid #efefef; max-height: 700px; max-width: 350px; padding: 2px;">
​
1. Open the YouTube app and start the video you want to watch.
2. Tap on the Share button and select AdGuard for Android from the list of apps.
3. A new window will pop up where you'll be able to watch the video without being interrupted by ads! 
​

**[Enhancement] DNS-over-QUIC support**
​
DNS-over-QUIC, or simply DoQ, is a DNS encryption protocol. You might have heard about DNS encryption protocols before, the most common ones are DNS-over-HTTPS and DNS-over-TLS (DoH and DoT correspondingly). So what makes DoQ so special? A bunch of things, really: out-of-the-box encryption, reduced connection times, and better performance in cases of lost data packets.
​
<img src="https://cdn.adguard.com/public/Adguard/Blog/Android/3-6/DNS-over-QUIC_en.png" width="300">
​
The feature is still experimental — AdGuard for Android is one of the first open-source implementations of DNS-over-QUIC — but it's perfectly functioning and we encourage you to try it. You'll find it under *DNS Filtering*. Select AdGuard DNS and choose DoQ from among the available encryption protocols.
​
### Changelog

* [Enhanced] HTTPS filtering for the Firefox Fenix browser is enabled forcibly [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [Enhanced] The "What's new" dialog is updated [#3638](https://github.com/AdguardTeam/AdguardForAndroid/issues/3638) 
* [Fixed] Shadowsocks proxy gets removed automatically [#3641](https://github.com/AdguardTeam/AdguardForAndroid/issues/3641) 
​
#### DnsLibs updated to v1.4.14

* [Enhanced] DoQ/DoH/DoT queries are retried before using the fallback [#86](https://github.com/AdguardTeam/DnsLibs/issues/86) 
* [Other] DoQ support is added to DNS stamps [#84](https://github.com/AdguardTeam/DnsLibs/issues/84) 
​
#### AdGuard for Android direct download links:

- [Release channel](https://agrd.io/apk)
- [Beta channel](https://agrd.io/apkb)
- [Nightly channel](https://agrd.io/android_nightly)

## 3.5.2

- Published: 2020-11-20T14:16:26Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.2

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Today we are launching a small but still very important hotfix. Namely, the compatibility with the new Chrome 87 was improved and the CoreLibs was updated.

**[Other] ERR_HTTP2_PROTOCOL_ERROR on some websites #1374**

This week Chrome 87 was released, which has a compatibility problem with AdGuard when using the HTTP/2 filtering protocol - some sites may experience regular hangs and download errors. In this update we have improved HTTP/2 filtering compatibility with Chrome 87, it is recommended to upgrade to the new stable version as soon as possible. :)

### Changelog

- [Enhancement] Add com.huawei.browser to the list of browsers #3495
- [Enhancement] Enable forcibly HTTPs filtering for the Firefox Fenix browser #3617
- [Other] Compatibility issues

#### Upgraded CoreLibs to v1.7.150

- [Enhancement] Improve socket connect with hostname provided (for Proxy mode) #123
- [Enhancement] Indicate libraries versions #1150
- [Fixed] `$badfilter` rules are sensitive to domain lists #1331
- [Other] $generichide rule causes that assistant is showing that AdGuard is disabled #7
- [Other] Connection error after waking computer from sleep mode #3412

#### AdGuard for Android direct download links:

[Release channel](https://agrd.io/apk)
[Beta channel](https://agrd.io/apkb)
[Nightly channel](https://agrd.io/android_nightly)

## 3.5.1

- Published: 2020-10-02T11:20:59Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.1

> Disclaimer AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Meet the release version 3.5.1 of AdGuard for Android. We’ve been working on improving its integration with AdGuard VPN, and now it seems we’ve maintained their seamless cooperation. Besides, we’ve updated CoreLibs and Dnslibs. 

## Changelog

* [Enhancement] Add Fennec F-Droid to the list of browsers  [#3587](https://github.com/AdguardTeam/AdguardForAndroid/issues/3587)
* [Enhancement] Add com.huawei.browser to the list of browsers  [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
* [Enhancement] Enable forcibly HTTPs filtering for the Firefox Fenix browser  [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [Fixed] Make the AdGuard application update work on Android 11  [#3564](https://github.com/AdguardTeam/AdguardForAndroid/issues/3564)
* [Fixed] Thai Ads Filters always enabled if the Language Filters group is enabled  [#3520](https://github.com/AdguardTeam/AdguardForAndroid/issues/3520)
* [Other] Update DnsLibs to the 1.3.24 version  [#3578](https://github.com/AdguardTeam/AdguardForAndroid/issues/3578)
* [Other] ru.sogaz.tm - app is not working  [#3573](https://github.com/AdguardTeam/AdguardForAndroid/issues/3573)

## Upgraded CoreLibs to v1.7.114

* [Enhancement] Add $ping content type  [#1258](https://github.com/AdguardTeam/CoreLibs/issues/1258)
* [Enhancement] Check that trusted-types CSP does not break the content script  [#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320)
* [Fixed] AGFDVSocket doesn't return original peer address in case of outbound proxy set  [#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)
* [Fixed] AdGuard doesn't filter domains when HTTPS filtering is disabled  [#1343](https://github.com/AdguardTeam/CoreLibs/issues/1343)
* [Fixed] AdGuard doesn't work with Youtube in Safari macOS Big Sur (infinity circle loader)  [#727](https://github.com/AdguardTeam/AdguardForMac/issues/727)
* [Fixed] Exclusion with $elemhide,jsinject,extension disable HTML filtering rules  [#1337](https://github.com/AdguardTeam/CoreLibs/issues/1337)
* [Fixed] Filtering log doesn't show information about cookies  [#3406](https://github.com/AdguardTeam/AdguardForWindows/issues/3406)
* [Fixed] Problematic userscripts  [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [Fixed] Redundant errors when local.adguard.org accessed from non-HTTPS-filtered processes  [#1056](https://github.com/AdguardTeam/CoreLibs/issues/1056)
* [Fixed] Regexp rule doesn't match URL  [#1311](https://github.com/AdguardTeam/CoreLibs/issues/1311)
* [Fixed] The foreign requests get into filtering log with enabled DNS module  [#3411](https://github.com/AdguardTeam/AdguardForWindows/issues/3411)
* [Fixed] URL contains extra slash while matching against filters and some rules are not applied  [#1338](https://github.com/AdguardTeam/CoreLibs/issues/1338)
* [Fixed] Wrong filter is shown in Filtering log  [#1312](https://github.com/AdguardTeam/CoreLibs/issues/1312)
* [Fixed] &#96;$badfilter&#96; rules are sensitive to domain lists  [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331)
* [Fixed] hkclubs.samsung.com  [#1340](https://github.com/AdguardTeam/CoreLibs/issues/1340)
* [Other] AdGuard for Mac doesn't start protection without internet connection  [#1323](https://github.com/AdguardTeam/CoreLibs/issues/1323)
* [Other] Fix errors encoding under Windows  [#79](https://github.com/AdguardTeam/DnsLibs/issues/79)
* [Other] HTML is not detected on some sites  [#1308](https://github.com/AdguardTeam/CoreLibs/issues/1308)
* [Other] local.adguard.org certificate is not re-issued when it expires [#1348](https://github.com/AdguardTeam/CoreLibs/issues/1348)

### **AdGuard for Android direct download links:**

**[Release channel](https://agrd.io/apk)**

**[Beta channel](https://agrd.io/apkb)**

**[Nightly channel](https://agrd.io/android_nightly)**

## 3.5.1 beta 1

- Published: 2020-09-28T16:25:59Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5.1-beta-1

This is an unscheduled update of AdGuard v3.5.1 for Android. Who would have thought that we’d do so, but double-checking doesn’t hurt, right? In this beta we fixed a few nasty bugs, updated CoreLibs and Dnslibs. Now it’s almost ready to be released.

## Changelog

* [Enhancement] Add Fennec F-Droid to the list of browsers  [#3587](https://github.com/AdguardTeam/AdguardForAndroid/issues/3587)
* [Fixed] Thai Ads Filters are always enabled if the group is enabled  [#3520](https://github.com/AdguardTeam/AdguardForAndroid/issues/3520)
* [Other] Updated CoreLibs to 1.7.114  [#3596](https://github.com/AdguardTeam/AdguardForAndroid/issues/3596) 
* [Other] Updated DnsLibs to the 1.3.24 version  [#3578](https://github.com/AdguardTeam/AdguardForAndroid/issues/3578) 

## CoreLibs

### Upgraded CoreLibs to v1.7.114

* [Enhancement] Add $ping content type  [#1258](https://github.com/AdguardTeam/CoreLibs/issues/1258) 
* [Enhancement] Check that trusted-types CSP does not break the content script  [#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320) 
* [Fixed] AGFDVSocket doesn't return original peer address in case of outbound proxy set  [#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330) 
* [Fixed] AdGuard doesn't filter domains when HTTPS filtering is disabled  [#1343](https://github.com/AdguardTeam/CoreLibs/issues/1343) 
* [Fixed] AdGuard doesn't work with Youtube in Safari macOS Big Sur (infinity circle loader)  [#727](https://github.com/AdguardTeam/AdguardForMac/issues/727) 
* [Fixed] Exclusion with $elemhide, jsinject, extension disable HTML filtering rules  [#1337](https://github.com/AdguardTeam/CoreLibs/issues/1337) 
* [Fixed] Filtering log doesn't show information about cookies  [#3406](https://github.com/AdguardTeam/AdguardForWindows/issues/3406) 
* [Fixed] Redundant errors when local.adguard.org is accessed from non-HTTPS-filtered processes  [#1056](https://github.com/AdguardTeam/CoreLibs/issues/1056) 
* [Fixed] Problematic userscripts  [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273) 
* [Fixed] Regexp rule doesn't match URL  [#1311](https://github.com/AdguardTeam/CoreLibs/issues/1311) 
* [Fixed] URL contains extra slash while matching against filters and some rules are not applied [#1338](https://github.com/AdguardTeam/CoreLibs/issues/1338) 
* [Fixed] The foreign requests get into filtering log with enabled DNS module  [#3411](https://github.com/AdguardTeam/AdguardForWindows/issues/3411) 
* [Fixed] &#96;$badfilter&#96; rules are sensitive to domain lists  [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331) 
* [Fixed] hkclubs.samsung.com  [#1340](https://github.com/AdguardTeam/CoreLibs/issues/1340) 
* [Other] HTML is not detected on some sites [#1308](https://github.com/AdguardTeam/CoreLibs/issues/1308) 
* [Other] local.adguard.org certificate is not re-issued when it expires  [#1348](https://github.com/AdguardTeam/CoreLibs/issues/1348)

## 3.5 

- Published: 2020-09-08T13:12:00Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5

It's time to release AdGuard v3.5 for Android. We took our time with this one: tested two betas and expanded the changelog. What's in there? Introduced compatibility mode with AdGuard VPN for Android, updated CoreLibs and a load-truck of fixed bugs.

**[Enhancement] Compatibility Mode with AdGuard VPN for Android app #3441**

Since AdGuard VPN for Android was first introduced, there was already a way to make it work along with AdGuard ad blocker. But to make the two apps coexist in peace, you were required to jump through some hoops. Anyone who went ahead and did the thing 100% has been waiting for a proper integration ever since — and we oblige.

The best kind of compatibility is when you install two apps and they just start working together. We did exactly that. Presuming you already have AdGuard ad blocker installed, just download AdGuard VPN from Google Play Store (you can get there right from the ad blocker app, there's a new item in General Settings menu).

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/settings.gif" width="300">

Both apps will detect each other and do everything that's needed for smooth joint work. All that will be left for you is to enjoy both ad-free Internet and all the benefits of a VPN. By the way, it works the other way around just as well: install AdGuard ad blocker on top of an already-running AdGuard VPN and you're good.

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/compatibility.gif" width="300">

If you'd like to disable Compatibility Mode for any reason, it's very simple to do so from AdGuard ad blocker settings, just toggle the switch. Additionally, you can add AdGuard ad blocker and AdGuard VPN tiles to your device's notification bar and toggle them in one tap at your own will — thanks to Compatibility Mode the configuration will change immediately and silently.

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/tiles.png" width="300">

## Changelog

- [Enhancement] Adaptive icons for app shortcuts [#2656](https://github.com/AdguardTeam/AdguardForAndroid/issues/2656)
- [Enhancement] Firefox Fenix browser added to the list of default browsers [#2861](https://github.com/AdguardTeam/AdguardForAndroid/issues/2861)
- [Enhancement] New rules are now added to the top of User filter [#2962](https://github.com/AdguardTeam/AdguardForAndroid/issues/2962)
- [Enhancement] 'Block' button now immediately switches to 'Unblock' after adding a custom rule via Filtering Log [#3012](https://github.com/AdguardTeam/AdguardForAndroid/issues/3012)
- [Enhancement] Extended information written to state.txt when logs are exported [#3063](https://github.com/AdguardTeam/AdguardForAndroid/issues/3063)
- [Enhancement] Enabled userscripts are now included in the query string for the web reporting tool [#3288](https://github.com/AdguardTeam/AdguardForAndroid/issues/3288)
- [Enhancement] Updates screen now shown when "Check for updates" shortcut is used [#3318](https://github.com/AdguardTeam/AdguardForAndroid/issues/3318)
- [Enhancement] Added automation API for proxy servers [#3363](https://github.com/AdguardTeam/AdguardForAndroid/issues/3363)
- [Enhancement] Mozilla Reference browser added to the list of default browsers [#3408](https://github.com/AdguardTeam/AdguardForAndroid/issues/3408)
- [Enhancement] Added an option to disable DNS fallback [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
- [Enhancement] AdGuard Simplified Domain Names filter renamed to AdGuard DNS filter [#3475](https://github.com/AdguardTeam/AdguardForAndroid/issues/3475)
- [Enhancement] Rename adguard.crt to AdGuardCertificate.pem [#3489](https://github.com/AdguardTeam/AdguardForAndroid/issues/3489)
- [Enhancement] Huawei browser added to the list of default browsers [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
- [Enhancement] Add the "What's new" dialog [#3532](https://github.com/AdguardTeam/AdguardForAndroid/issues/3532) 
- [Enhanced] Prepare AdGuard before the v3.5 release [#3546](https://github.com/AdguardTeam/AdguardForAndroid/issues/3546) 
- [Fixed] First letter in the sentence is not capitalized automatically on the 'Message to support' screen [#3079](https://github.com/AdguardTeam/AdguardForAndroid/issues/3079)
- [Fixed] AdGuard doesn't work on devices with Restricted Account [#3299](https://github.com/AdguardTeam/AdguardForAndroid/issues/3299)
- [Fixed] Toast notification for "Checking for updates" shows late [#3343](https://github.com/AdguardTeam/AdguardForAndroid/issues/3343)
- [Fixed] Unnecessary "Android Private DNS is enabled" notification on Android 11 [#3478](https://github.com/AdguardTeam/AdguardForAndroid/issues/3478)
- [Fixed] Downloads in some apps don't work properly on Android 11 [#3516](https://github.com/AdguardTeam/AdguardForAndroid/issues/3516)
- [Fixed] Wrong state of the disabled option [#3538](https://github.com/AdguardTeam/AdguardForAndroid/issues/3538)
- [Fixed] Fix a bug related with a strange and small "m^" rule [#3548](https://github.com/AdguardTeam/AdguardForAndroid/issues/3548)
- [Other] Updated options for default DNS resolvers [#3428](https://github.com/AdguardTeam/AdguardForAndroid/issues/3428)

## DnsLibs 

- [Enhancement] Added support for comments at the end of line in hosts rules [#75](https://github.com/AdguardTeam/DnsLibs/issues/75)
- [Fixed] LDNS logging [#73](https://github.com/AdguardTeam/DnsLibs/issues/73)
- [Other] Added upstreams sorting by RTT [#39](https://github.com/AdguardTeam/DnsLibs/issues/39)

## Corelibs

- [Enhancement] #@# without any domains specified should disable the rule completely [#1296](https://github.com/AdguardTeam/CoreLibs/issues/1296)
- [Enhancement] Added verification for trusted-types CSP [#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320)
- [Fixed] Connection has timed out in state have-result [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180)
- [Fixed] Problematic userscripts [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
- [Fixed] Process name detection causes warnings in Windows Security [#1316](https://github.com/AdguardTeam/CoreLibs/issues/1316)
- [Fixed] OCSP checks aren't passed through the selected DNS [#1328](https://github.com/AdguardTeam/CoreLibs/issues/1328)
- [Fixed] AGFDVSocket doesn't return original peer address in case of outbound proxy set [#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)
- [Other] Connection speed is capped when AdGuard is enabled [#702](https://github.com/AdguardTeam/CoreLibs/issues/702)

## 3.3.3 Release

- Published: 2020-04-03T10:45:22Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.231

Yet another and hopefully the last fix before the fresh beta rolls out. Several domains have been added to SSL exceptions to fix compatibility issues with certain mobile carriers.

* [Changed] The list of HTTPS exclusions has been updated

## 3.4 Release

- Published: 2020-05-21T11:21:25Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-release

Meet AdGuard v3.4 for Android, it’s time for it to see the world! Having tested two betas, we feel confident to present this version to a wider audience. Spring is a time for renewal, and software is not an exception. We've fixed some old bugs, updated CoreLibs and made the app more compatible with Android TV.

**[Fixed] AdGuard blocks Internet connection #2842**

This bug was a hard nut to crack. For a long time it appeared randomly (at least, it seemed so) on devices of AdGuard users. Still, the symptoms matched: smartphones lost any network completely while AdGuard was turned on. Of course, it was crucial for us to solve this problem, and at last, we've managed to do it. It’s beyond words how relieved we feel afterwards, let alone the affected users!

**[Fixed] Firewall's restrictions are ignored when WiFi gets enabled #3313**

Another troublesome bug that deserves special attention. In the previous version 3.3, if you had specifically prohibited some apps from accessing the Internet via mobile data, the restrictions worked right up until you enabled Wi-Fi, which was not the intended behaviour.

**[Enhancement] Integration with DnsLibs #3229**

DnsLibs is a DNS proxy library that's required to provide DNS filtering. It supports all existing DNS protocols including DNS-over-TLS, DNS-over-HTTPS, and DNSCrypt. We developed it to replace the old DNSproxy, which had one serious flaw: it caused high battery resource consumption. DnsLibs is much better optimized and will ensure a longer lifespan for your phone's battery if you're using DNS filtering a lot.

**[Enhancement] Improved functionality on Android TV #3238**

AdGuard for Android is first and foremost an app for mobile phones and tablets, but it can be installed on other Android devices, such as smart TVs. We have made several improvements for this specific case, for example:

- AdGuard now better works with lists
- Better navigation between AG menus on smart TVs
- Option to click on snackbars
- Option to exit the promo screen
- "Close" option for all dialogues

Now AdGuard for Android will be much easier in use if you decide to install it on your smart TV. If you still encounter any bugs or inconsistent behaviour, please report it here.

## Changelog

- [Fixed] Application won’t start after the restart of the device #3286
- [Fixed] Stealth mode preset changes after an update #3287
- [Fixed] Locale change bug #3301
- [Fixed] com.android.providers.downloads traffic isn't routed #3355
- [Fixed] Filtering doesn’t work with AdGuard enabled on Android 11 #3377
- [Fixed] Impossible to enable UDP through SOCKS5 proxy #3394
- [Fixed] Impossible to create a hotspot without disabling DNS filtering #3187
- [Fixed] "HTTPS filtering is off" Snackbar covers "Data Saved" stat on the Home screen #3292
- [Fixed] The app crashes when switching from 4G to Wi-Fi in Local HTTP Proxy Mode #3431
- [Fixed] 'Back' button on the Settings screen works incorrectly #3427
- [Fixed] AdGuard doesn't launch #3430
- [Enhancement] Custom adguard: scheme is now used for adding userscripts #3000
- [Enhancement] "Cancel" button added to the "Add proxy" screen #3093
- [Enhancement] stealth.enabled=false is now sent in query string if Stealth Mode is turned off when sending a report #3169
- [Enhancement] Block ads in all apps parameter is now sent when sending a report #3350
- [Enhancement] An option to suppress HTTPS filtering error notification #3225
- [Enhancement] HTTPS filtering dialog has been improved #3284
- [Enhancement] Romanian and Thai localizations have been added #3341
- [Other] Acknowledgements page has been updated #82
- [Other] Firefox Preview Nightly for developers has been added to the list of supported browsers #3333
- [Other] Certificate installation sequence on Android 11 #3354
- [Other] Cobra Browser has been added to the list of supported browsers #3357
- [Other] Application crashes on Android 11 upon opening filtering log details #3366
- [Other] Vivaldi Snapshot and Vivaldi Sopranos have been added to the list of supported browsers #3400
- [Other] Add Brave Beta has been added to the list of supported browsers #3401
- [Other] AdGuard crashes in local HTTP proxy mode #3416
- [Other] HTTPS exclusions list has been updated #3419, #3425
- [Other] Yuzu Browser Plus added to the list of supported browsers #3424
- [Other] Brave Nightly added to the list of supported browsers #3432
- [Other] The list of HTTPS exclusions has been updated
- [Other] Translations have been updated

## CoreLibs has been updated to v1.5.265

- [Fixed] Cosmetic rules can be used as CSS rules #1293
- [Fixed] Rules selection algorithm works not as intended when HTTPS filtering is disabled #1291
- [Fixed] Rules with restricted domains do not match requests without referer #1286
- [Fixed] "Failed to initialize protocol filters" error #1282
- [Fixed] Incorrect extended CSS rule causes problems with JS rules #1147
- [Fixed] 'Proceed anyway' option doesn't work correctly if website is blocked by a rule with `$all` modifier #1267

## DnsLibs updated to v1.2.26

- [Other] 'Unblock' button is not visible in Filtering Log details #3429

## 3.6 beta 1

- Published: 2020-11-20T18:04:23Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.6-beta-1

> **Disclaimer** AdGuard for Android is not an open-source project. We use Github as an open bug tracker for users to see what developers are working on.

Today we are launching a small but still very important beta. Namely, the compatibility with the new Chrome 87 was improved and the CoreLibs was updated.

**[Other] ERR_HTTP2_PROTOCOL_ERROR on some websites [#1374](https://github.com/AdguardTeam/AdguardForAndroid/issues/1374)**

This week Chrome 87 was released, which has a compatibility problem with AdGuard when using the HTTP/2 filtering protocol - some sites may experience regular hangs and download errors. In this update we have improved HTTP/2 filtering compatibility with Chrome 87, it is recommended to upgrade to the new stable version as soon as possible. :)

## Changelog

* [Enhancement] Add com.huawei.browser to the list of browsers  [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495) 
* [Enhancement] Enable forcibly HTTPs filtering for the Firefox Fenix browser  [#3617](https://github.com/AdguardTeam/AdguardForAndroid/issues/3617)
* [Enhancement] Option to watch Youtube videos ad-free by sharing them to AdGuard [#2994](https://github.com/AdguardTeam/AdguardForAndroid/issues/2994)
* [Fixed] Does not filter plain HTTP when it uses a non-standard port  [#1366](https://github.com/AdguardTeam/CoreLibs/issues/1366)
* [Fixed] Compatibility issues

### Upgraded CoreLibs to v1.7.150

* [Enhancement] Improve socket connect with hostname provided (for Proxy mode) [#123](https://github.com/AdguardTeam/CoreLibs/issues/123) 
* [Enhancement] Indicate libraries versions  [#1150](https://github.com/AdguardTeam/CoreLibs/issues/1150) 
* [Fixed] &#96;$badfilter&#96; rules are sensitive to domain lists  [#1331](https://github.com/AdguardTeam/CoreLibs/issues/1331) 
* [Other] $generichide rule causes that assistant is showing that AdGuard is disabled  [#7](https://github.com/AdguardTeam/BrowserAssistant/issues/7) 
* [Other] Connection error after waking computer from sleep mode  [#3412](https://github.com/AdguardTeam/AdguardForWindows/issues/3412)

## 3.5 RC 1 

- Published: 2020-08-26T14:28:28Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-rc-1

A release candidate for the upcoming AdGuard v3.5 for Android is now available. We believe that exposing an RC version to trusted users is a great way to test new features before the release.

This update includes a couple of small fixes and a CoreLibs upgrade – we are eager to polish everything until it shines.   

## Changelog

* [Enhanced] Prepare AdGuard before the v3.5 release  [#3546](https://github.com/AdguardTeam/AdguardForAndroid/issues/3546) 
* [Fixed] Provide an option to disable fallback  [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
* [Fixed] Fix a bug related with a strange and small "m^" rule  [#3548](https://github.com/AdguardTeam/AdguardForAndroid/issues/3548) 

## CoreLibs

#### Upgraded CoreLibs to v1.7.64

* [Fixed] Problematic userscripts  [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [Fixed] AGFDVSocket doesn't return original peer address in case of outbound proxy set  [#1330](https://github.com/AdguardTeam/CoreLibs/issues/1330)

## 3.5 beta 2

- Published: 2020-08-21T10:56:44Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-beta-2

In this update, we added a few finishing touches, updated CoreLibs filtering engine and fixed a couple of bugs. Almost there.

## Changelog

* [Enhancement] Add the "What's new" dialog  [#3532](https://github.com/AdguardTeam/AdguardForAndroid/issues/3532)
* [Enhancement] Rename adguard.crt to AdGuardCertificate.pem  [#3489](https://github.com/AdguardTeam/AdguardForAndroid/issues/3489)
* [Fixed] Wrong state of the disabled option  [#3538](https://github.com/AdguardTeam/AdguardForAndroid/issues/3538)

## CoreLibs

#### Upgraded CoreLibs to v1.7.58

* [Enhancement] #@# without any domains specified should disable the rule completely  [#1296](https://github.com/AdguardTeam/CoreLibs/issues/1296)
* [Fixed] Connection has timed out in state have-result  [#1180](https://github.com/AdguardTeam/CoreLibs/issues/1180) 
* [Fixed] OCSP checks aren't passed through the selected DNS  [#1328](https://github.com/AdguardTeam/CoreLibs/issues/1328)

## 3.5 beta 1

- Published: 2020-08-14T17:11:03Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.5-beta-1

Today we release the first beta version of AdGuard v3.5 for Android. It features a long list of various impovements in its changelog, but the main focus is, without a doubt, on the freshly introduced compatibility mode with AdGuard VPN for Android.

**[Enhancement] Compatibility Mode with AdGuard VPN Android app [#3441](https://github.com/AdguardTeam/AdguardForAndroid/issues/3441)**

Since AdGuard VPN for Android [was first introduced](https://adguard.com/en/blog/introducing-adguard-vpn-for-android.html), there was already a way to make it work along with AdGuard ad blocker. But to make the two apps coexist in peace, you were required to jump through some hoops. Anyone who went ahead and did the thing 100% has been waiting for a proper integration ever since — and we oblige.

The best kind of compatibility is when you install two apps and they just start working together. We did exactly that. Presuming you already have AdGuard ad blocker installed, just download AdGuard VPN from [Play Store](https://play.google.com/store/apps/details?id=com.adguard.vpn) (you can get there right from the ad blocker app, there's a new item in General Settings menu). 

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/settings.gif" width="300">

Both apps will detect each other and do everything that's needed for smooth joint work. All that will be left for you is to enjoy both ad-free Internet and all the benefits of a VPN. By the way, it works the other way around just as well: install AdGuard ad blocker on top of an already-running AdGuard VPN and you're good.

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/compatibility.gif" width="300">

If you'd like to disable Compatibility Mode for any reason, it's very simple to do so from AdGuard ad blocker settings, just toggle the switch. Additionally, you can add AdGuard ad blocker and AdGuard VPN tiles to your device's notification bar and toggle them in one tap at your own will  — thanks to Compatibility Mode the configuration will change immediately and silently.

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.5/tiles.png" width="300">

* [Enhancement] Adaptive icons for app shortcuts [#2656](https://github.com/AdguardTeam/AdguardForAndroid/issues/2656)
* [Enhancement] New rules are now added to the top of User filter [#2962](https://github.com/AdguardTeam/AdguardForAndroid/issues/2962)
* [Enhancement] Huawei browser added to the list of default browsers [#3495](https://github.com/AdguardTeam/AdguardForAndroid/issues/3495)
* [Enhancement] Firefox Fenix browser added to the list of default browsers [#2861](https://github.com/AdguardTeam/AdguardForAndroid/issues/2861)
* [Enhancement] Mozilla Reference browser added to the list of default browsers [#3408](https://github.com/AdguardTeam/AdguardForAndroid/issues/3408)
* [Enhancement] 'Block' button now immediately switches to 'Unblock' after adding a custom rule via Filtering Log [#3012](https://github.com/AdguardTeam/AdguardForAndroid/issues/3012)
* [Enhancement] Added automation API for proxy servers [#3363](https://github.com/AdguardTeam/AdguardForAndroid/issues/3363)
* [Enhancement] Added an option to disable DNS fallback [#3447](https://github.com/AdguardTeam/AdguardForAndroid/issues/3447)
* [Enhancement] Extended information written to `state.txt` when logs are exported [#3063](https://github.com/AdguardTeam/AdguardForAndroid/issues/3063)
* [Enhancement] AdGuard Simplified Domain Names filter renamed to AdGuard DNS filter [#3475](https://github.com/AdguardTeam/AdguardForAndroid/issues/3475)
* [Enhancement] Enabled userscripts are now included in the query string for the web reporting tool [#3288](https://github.com/AdguardTeam/AdguardForAndroid/issues/3288)
* [Enhancement] Updates screen now shown when "Check for updates" shortcut is used [#3318](https://github.com/AdguardTeam/AdguardForAndroid/issues/3318)
* [Fixed] Downloads in some apps don't work properly on Android 11 [#3516](https://github.com/AdguardTeam/AdguardForAndroid/issues/3516)
* [Fixed] AdGuard doesn't work on devices with Restricted Account [#3299](https://github.com/AdguardTeam/AdguardForAndroid/issues/3299)
* [Fixed] First letter in the sentence is not capitalized automatically on the 'Message to support' screen [#3079](https://github.com/AdguardTeam/AdguardForAndroid/issues/3079)
* [Fixed] Unnecessary "Android Private DNS is enabled" notification on Android 11 [#3478](https://github.com/AdguardTeam/AdguardForAndroid/issues/3478)
* [Fixed] Toast notification for "Checking for updates" shows late [#3343](https://github.com/AdguardTeam/AdguardForAndroid/issues/3343)
* [Other] Updated options for default DNS resolveres [#3428](https://github.com/AdguardTeam/AdguardForAndroid/issues/3428)
* [Other] DnsLibs updated to v1.3.19
* [Other] CoreLibs updated to v1.7.49
* [Other] Compatibility issues

### DnsLibs

* [Enhancement] Added support for comments at the end of line in hosts rules [#75](https://github.com/AdguardTeam/DnsLibs/issues/75)
* [Fixed] LDNS logging [#73](https://github.com/AdguardTeam/DnsLibs/issues/73)
* [Other] Added upstreams sorting by RTT [#39](https://github.com/AdguardTeam/DnsLibs/issues/39)

### CoreLibs

* [Enhancement] Added verification for trusted-types CSP [#1320](https://github.com/AdguardTeam/CoreLibs/issues/1320)
* [Fixed] Problematic userscripts [#1273](https://github.com/AdguardTeam/CoreLibs/issues/1273)
* [Fixed] Process name detection causes warnings in Windows Security [#1316](https://github.com/AdguardTeam/CoreLibs/issues/1316)
* [Other] Connection speed is capped when AdGuard is enabled [#702](https://github.com/AdguardTeam/CoreLibs/issues/702)

## 3.4 beta 2

- Published: 2020-05-14T13:18:29Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-beta-2

In this run-of-the-mill beta we fix few bugs and update CoreLibs. It will transform into the next release version if all goes well.

## Changelog

* [Bug] 'Back' button on the Settings screen works incorrectly #3427
* [Bug] The app crashes when switching from 4G to Wi-Fi in Local HTTP Proxy Mode #3431 
* [Bug] AdGuard doesn't launch #3430
* [Other] HTTPS exclusions list has been updated #3419, #3425
* [Other] Brave Nightly added to the list of supported browsers #3432
* [Other] Yuzu Browser Plus added to the list of supported browsers #3424

### CoreLibs updated to v1.5.265

* [Bug] Incorrect extended CSS rule causes problems with JS rules #1147
* [Bug] Cosmetic rules can be used as CSS rules #1293
* [Bug] 'Proceed anyway' option doesn't work correctly if the website is blocked by a rule with `$all` modifier #1267

### DnsLibs updated to v1.2.26

* [Other] 'Unblock' button is not visible in Filtering Log details #3429

## 3.4 beta 1

- Published: 2020-04-27T11:49:40Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.4-beta-1

Please welcome the first beta version of AdGuard v3.4 for Android! To start things off, we've enhanced the app in a few directions, including fixing some of the oldest known bugs and improving Android TV compatibility. 

**[Bug] AdGuard blocks Internet connection [#2842](https://github.com/AdguardTeam/AdguardForAndroid/issues/2842)**

This bug had been puzzling us for a very long time. It appeared on various devices of AdGuard users and was seemingly random. However, the symptoms were the same: the smartphone lost any network completely while AdGuard was turned on. Needless to say, it had been our top priority to fix this issue, and finally, we've managed to beat it. Not going to lie, it's a big relief not only for the affected users but for us too!

**[Enhancement] Integration with DnsLibs [#3229](https://github.com/AdguardTeam/AdguardForAndroid/issues/3229)**

[DnsLibs](https://github.com/AdguardTeam/DnsLibs) is a DNS proxy library that's required to provide DNS filtering. It supports all existing DNS protocols including DNS-over-TLS, DNS-over-HTTPS, and DNSCrypt. We developed it to replace the old DNSproxy, which had one serious flow: it caused high battery resource consumption. DnsLibs is much better optimized and will ensure a longer lifespan for your phone's battery if you're using DNS filtering a lot. 

**[Enhancement] Improved functionality on Android TV [#3238](https://github.com/AdguardTeam/AdguardForAndroid/issues/3238)**

AdGuard for Android is first and foremost an app for mobile phones and tablets, but it can be installed on other Android devices, such as smart TVs. We have made several improvements for this specific case, for example:

- AdGuard now better works with lists
- Better navigation between AG menus on smart TVs
- Option to click on snackbars
- Option to exit the promo screen
- "Close" option for all dialogues

Now AdGuard for Android will be much easier in use if you decide to install it on your smart TV. If you still encounter any bugs or inconsistent behavior, please report it [here](https://github.com/AdguardTeam/AdguardForAndroid/issues/new/choose).  

**[Bug] Firewall's restriction are ignored when WiFi gets enabled [#3313](https://github.com/AdguardTeam/AdguardForAndroid/issues/3313)**

And another unpleasant bug that deserves a special mention. In v3.3, if you had specifically prohibited some apps from accessing the Internet via mobile data, the restrictions worked right up until you enabled WiFi, which was not the intended behaviour.

## Changelog

* [Bug] Application won’t start after the restart of the device [#3286](https://github.com/AdguardTeam/AdguardForAndroid/issues/3286)
* [Bug] Stealth mode preset changes after an update [#3287](https://github.com/AdguardTeam/AdguardForAndroid/issues/3287)
* [Bug] Locale change bug [#3301](https://github.com/AdguardTeam/AdguardForAndroid/issues/3301)
* [Bug] `com.android.providers.downloads` traffic isn't routed [#3355](https://github.com/AdguardTeam/AdguardForAndroid/issues/3355)
* [Bug] Filtering doesn’t work with enabled AdGuard on Android 11 [#3377](https://github.com/AdguardTeam/AdguardForAndroid/issues/3377)
* [Bug] Impossible to enable UDP through SOCKS5 proxy [#3394](https://github.com/AdguardTeam/AdguardForAndroid/issues/3394)
* [Bug] You can't create a hotspot without disabling DNS filtering [#3187](https://github.com/AdguardTeam/AdguardForAndroid/issues/3187)
* [Bug] "HTTPS filtering is off" SnackBar covers "Data Saved" stat on the Home screen [#3292](https://github.com/AdguardTeam/AdguardForAndroid/issues/3292)
* [Enhancement] Custom `adguard:` scheme is now used for adding userscripts [#3000](https://github.com/AdguardTeam/AdguardForAndroid/issues/3000)
* [Enhancement] "Cancel" button added to the "Add proxy" screen [#3093](https://github.com/AdguardTeam/AdguardForAndroid/issues/3093)
* [Enhancement] `stealth.enabled=false` is now sent in query string if Stealth Mode is turned off when sending a report [#3169](https://github.com/AdguardTeam/AdguardForAndroid/issues/3169)
* [Enhancement] `Block ads in all apps` parameter is now sent when sending a report [#3350](https://github.com/AdguardTeam/AdguardForAndroid/issues/3350)
* [Enhancement] An option to suppress HTTPS filtering error notification [#3225](https://github.com/AdguardTeam/AdguardForAndroid/issues/3225)
* [Enhancement] HTTPS filtering dialog has been improved [#3284](https://github.com/AdguardTeam/AdguardForAndroid/issues/3284)
* [Enhancement] Romanian and Thai localizations have been added [#3341](https://github.com/AdguardTeam/AdguardForAndroid/issues/3341)
* [Other] Firefox Preview Nightly for Developers has been added to the list of supported  browsers [#3333](https://github.com/AdguardTeam/AdguardForAndroid/issues/3333)
* [Other] Cobra Browser has been added to the list of supported browsers [#3357](https://github.com/AdguardTeam/AdguardForAndroid/issues/3357)
* [Other] Add Brave Beta has been added to the list of supported browsers [#3401](https://github.com/AdguardTeam/AdguardForAndroid/issues/3401)
* [Other] Vivaldi Snapshot and Vivaldi Sopranos have been added to the list of supported browsers [#3400](https://github.com/AdguardTeam/AdguardForAndroid/issues/3400)
* [Other] Certificate installation sequence on Android 11 [#3354](https://github.com/AdguardTeam/AdguardForAndroid/issues/3354)
* [Other] Acknowledgements page has been updated [#82](https://github.com/AdguardTeam/AdguardForAndroid/issues/82)
* [Other] AdGuard crashes in local HTTP proxy mode [#3416](https://github.com/AdguardTeam/AdguardForAndroid/issues/3416)
* [Other] Application crashes on Android 11 upon opening filtering log details [#3366](https://github.com/AdguardTeam/AdguardForAndroid/issues/3366)
* [Other] The list of HTTPS exclusions has been updated
* [Other] Translations have been updated

## CoreLibs has been updated to v1.5.249

* [Bug] Cosmetic rules can be used as CSS rules [#1293](https://github.com/AdguardTeam/CoreLibs/issues/1293)
* [Bug] Rules selection algorithm works not as intended when HTTPS filtering is disabled [#1291](https://github.com/AdguardTeam/CoreLibs/issues/1291)
* [Bug] Rules with restricted domains do not match requests without referer [#1286](https://github.com/AdguardTeam/CoreLibs/issues/1286)   
* [Bug] "Failed to initialize protocol filters" error [#1282](https://github.com/AdguardTeam/CoreLibs/issues/1282)

## 3.3.2 Release

- Published: 2020-02-13T16:26:35Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.230

In this small update, there’s only one but important fix and a few additions to the exclusions list.

* [Fixed] Protection doesn’t restart when an excluded app is installed #3340
* [Changed] The list of HTTPS exclusions has been updated

## 3.3.1 Release

- Published: 2019-12-30T11:11:34Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.229

Recently we claimed to make the last release of the year, and it kinda was that. Ignore that this update is called a 'release', it's more of a 'hotfix'. Because you wouldn't call this tiny hotfix a release, right? Just a couple of bugsfixes, that's all.

- [Fixed] The protection doesn't start autimatically if you restart the phone right after checking for filter updates #3286
- [Fixed] Stealth Mode configuration isn't saved after app update #3287

## 3.3 Release

- Published: 2019-12-26T13:21:38Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3.228

The last AdGuard for Android release of the decade! This sounds solid. Anyway, it’s more of a coincidence than anything else that such a massive update falls right on Christmas. And don’t get us wrong: it is massive. Multiple major features and over 50 lesser ones — all in all it combines to make a nice Christmas gift for y’all!

**[Improved] Filtering engine**

Version 3.3 brings scriptlets and `$redirect` modifiers support. Scriptlets is a powerful ad-blocking tool that helps to block ads on websites that use different circumvention techniques. `$redirect` modifier is another tool that allows substituting an ad with special ‘resources’ instead of blocking it. For instance, it can replace a banner with a transparent 1x1 image.

**[Changed] The onboarding process #2895**

We sure love us some redesign! This time, we revamped the onboarding sequence (basically, what you see when you launch the app for the first time). Key changes:

- An option to choose a ‘quick’ or a ‘long’ configuration: you’ll be asked to either make only key decisions or set most of the settings manually
- New option to allow sending some technical and interaction information that will help us further improve AdGuard
- Better graphics!

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/welcome.png" width="300"> <img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/create_vpn.png" width="300">

**[Added] New activation flow #2901**

Not a lot of Android users had a chance to see our AdGuard for iOS app, so they likely don’t know about the system that’s being used there for Premium features activation. But it recommended itself as one that’s convenient for users, so we adopted it for AdGuard for Android too.

<img src="https://cdn.adguard.com/public/Adguard/screenshots/android/activation_En_account.png?123" width="300"> <img src="https://cdn.adguard.com/public/Adguard/screenshots/android/activation_en_license.png" width="300">

As you can see, there are now two options: enter a license key directly, or log into AdGuard personal account. If your account has a license key that can be used to activate Premium, it will get picked up automatically after you enter credentials.

### Ad blocking

- [Added] Preset Stealth Mode settings configurations #2625
- [Added] abp:subscribe and adguard:subscribe links interception #2918
- [Added] subscribe.adblockplus.org links interception #2930
- [Changed] Internet connection availability checking method #3095
- [Changed] Whale browser has been added to the known browsers list #3175
- [Fixed] DNS User filter import bug #2972
- [Fixed] Some legit hosts lists are not recognized as valid #2982
- [Fixed] Error while checking updates of resources added from the local storage #2997
- [Fixed] Quick Settings does not allow to choose a different Privacy protection Level #2768
- [Fixed] “Exclude from filtering” button behavior #3052
- [Fixed] Google Now can’t be updated with “Always-on-VPN” enabled #3039
- [Fixed] AdGuard Extra enables automatically when there’s an available update #3216
- [Fixed] The application causes a crash if custom filters were enabled #3258
- [Fixed] AdGuard breaks some UDP connections on Samsung S10 devices with Android 10 #3259
- [Improved] AdGuard now uses on-the-fly methods of applying settings changes without restarting the protection when possible #2881
- [Improved] DNS filtering to block cloaked trackers #3228
- [Improved] “Block phishing and malware” option now is enabled automatically when Premium gets activated #3249
- [Improved] Now AdGuard can block AAAA requests in networks without IPv6 interface #3197

### UI

- [Added] An option to purchase a new license via the app #2897
- [Added] Trial period and license activation via OAuth #3081, #3244
- [Added] Whitelisting apps option to the Assistant dialog #2853
- [Added] “On/Off” switch on some screens #2877
- [Added] Notifications about certificate errors #2722
- [Added] Ability to copy the current version number by tapping on it #2773
- [Added] Link to Version history in the About tab #2774
- [Added] System default theme option #2174
- [Added] Silent update action as a long-tap on the update button #2890
- [Added] “Failed to move the certificate” notification for rooted devices with Magisk firmware #2941
- [Added] Empty field validation when adding a new extension #2983
- [Added] “Refresh license status” button #2988
- [Added] Restore purchases button: a notification if there’s nothing to restore #2990
- [Changed] The imported filter list’s URL now won’t be stored if a content: link was used #2813
- [Changed] Chrome custom tabs now open in the same window #3019
- [Changed] Premium screens now can be viewed without Premium #2843
- [Changed] Update notifications behavior #2922
- [Changed] DNS request type is now displayed in the Filtering log even when there's no answer #2961
- [Changed] Tap on filter category titles in search will bring you to the respective category’s screen #3035
- [Changed] Toast notifications parameters #3087
- [Changed] Proxy screen UI #3092
- [Changed] AdGuard now remembers the selected type of data to display in Apps Management #3140
- [Changed] Phrasing on activation screens #3141
- [Changed] “Clear DNS statistics” warning description #3194
- [Changed] Improve the in-app purchase design #3252
- [Fixed] Minor UI issues #2879
- [Fixed] Issue with distribution graphs on the main screen #2935
- [Fixed] Search on Apps Managements screen is working slow #2951
- [Fixed] Unexpected connections resets #2980
- [Fixed] Incorrect filter locale is displayed after language change #2971
- [Fixed] Scrolling issue in the Filtering log #2974
- [Fixed] Wrong filters status is shown #2987
- [Fixed] Incorrect updates status when the network is not available #3020
- [Fixed] “Preparing to start protection” notification #3034
- [Fixed] “Edit Filter” overlay bug #3045
- [Fixed] Divider stripe is still shown when there are no updates available #3047
- [Fixed] Cloudflare DNS description #3062
- [Fixed] Wrong Chinese date format #3068
- [Fixed] Application updates icon #3098
- [Fixed] Missing button shadow #3109
- [Fixed] Some buttons in the first start dialog boxes can’t be seen on certain device models #3114
- [Fixed] The switch for Custom filters incorrectly represents the state of the filter group #3119
- [Fixed] Pressing the “Buy one more license” button closes the current screen #3136
- [Fixed] Certificate installation dialog is missing #3176
- [Fixed] Wrong toast notification is displayed when the license expires #3183
- [Fixed] “Missed ad” option in the Feedback section leads to an error if DuckDuckGo is selected as the default browser #3128
- [Improved] HTTPS filtering-related UI changes #2896
- [Improved] UI elements are now focusable on Android TV #2818
- [Improved] Rich formatting added to some modules’ descriptions #2878
- [Improved] Phrasing on onboarding screens #3248
- [Improved] Phrasing in the Apps Management details activity #3250
- [Improved] Localizations have been updated: #3271, #3188, #3161

### Networking

- [Added] A prevention system for connections overflow #2989
- [Added] TLS v1.3 support for custom DNS servers #3132
- [Changed] DNS-over-HTTPS connections number limit has been abolished #3224
- [Fixed] Some apps don't see available WiFi networks when AdGuard local VPN is up #2836
- [Improved] Interaction between AdGuard DNS settings and Private DNS #2797
- [Improved] AdGuard’s network safety and stability #2995
- [Improved] Connection error processing #3195

### Other

- [Added] Whitelist export feature #3069
- [Fixed] Update window appears after a short inactivity period #3055
- [Fixed] Userscripts updates are not tracked by the battery service #3073
- [Fixed] AdGuard 3.2 does not launch #3076
- [Fixed] “Include license data” option works incorrectly when you try to export settings #3067
- [Fixed] Crash when the app runs scheduled tasks #3164
- [Fixed] Crash in the Updates activity #3165
- [Fixed] Crash when Android OS tries to load the icon #3166
- [Fixed] Crash on some Android builds #3167
- [Fixed] Crash in the main activity #3168
- [Fixed] Crash when user communicates with the extensions activity #3171
- [Fixed] Crash when the log is being collected #3212
- [Fixed] Crash on MIUI phones with Ultra battery saver #3210
- [Fixed] Max imported settings file size increased to 10 Mb #3203
- [Improved] Target SDK level has been changed to 29 #3053
- [Improved] CoreLibs has been updated to v1.5.74 #3105

## 3.2.150

- Published: 2019-08-29T14:36:38Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.2.150

>Disclaimer: AdGuard for Android is not an open source project. We use Github as an open bug tracker for users to see what developers are working on.

The previous hotfix dealt with some urgent bugs, so we had to act fast and couldn't fix the rest of the less important issues. After today's update all of them should go away.

* [Fixed] DNS filtering breaks regular filtering on HTC devices #3014
* [Fixed] AdGuard doesn't completely remove extensions #3015
* [Fixed] Disabling network access globally blocks DNS requests #3025
* [Fixed] Bypassing DNS requests breaks DNS filtering #3026
* [Fixed] AdGuard fails to start protection after an update #3024
* [Fixed] Facebook lite cannot detect that IPv6 is unreachable #3031
* [Fixed] Blocked app notification works incorrectly #3032 
* [Improved] dnsproxy library has been updated #3016

## 3.2.140 Hotfix

- Published: 2019-08-24T10:43:56Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.2.140

>Disclaimer: AdGuard for Android is not an open source project. We use Github as an open bug tracker for users to see what developers are working on.

This is a small hotfix for the recent AdGuard for Android release. Mostly squashing bugs related to the new features introduced in v3.2.

* [Fixed] DNS filtering breaks regular filtering on HTC devices #3014 
* [Fixed] AdGuard doesn't completely remove extensions #3015 
* [Improved] dnsproxy library has been updated #3016

## 3.3 beta 3.1

- Published: 2019-12-09T21:49:53Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-3.1

A quick hotfix that fixes the crash of the application when the protection starts if custom filters have been enabled.

- [Fixed] The application causes a crash if custom filters were enabled #3258

## 3.3 beta 3

- Published: 2019-12-09T17:13:16Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-3

This beta of AdGuard for Android is a bit of an outlier, in the sense that it’s the third one for v3.3. Usually, by that point changelogs become shorter, big juicy tasks get left for later. The closer we’re to release, the more we focus on fixing existing bugs rather than creating new ones 😄 

Not this time, though! We still got a lot left in us: new purchase flow, some serious ad blocking quality improvements. And of course, there’s no escaping the chores: multiple bugfixes, crash hunting etc.

**[Added] An option to purchase a new license via the app #2897**

We’ve already made it so you don’t need to leave the app to link your personal account, and from now on you can even purchase a license without ever minimizing AdGuard. Either when you start the app for the first time, or when you decide it’s time to activate Premium, you’ll face a familiar but different screen:

<img src="https://cdn.adguard.com/public/Adguard/screenshots/android/PremEN.png" width="300"> <img src="https://cdn.adguard.com/public/Adguard/screenshots/android/SubEN.png" width="299.5">

The app will offer you to choose the preferred type of license and its duration and will ask you to enter your email. So basically the same actions that you’d perform on the website but without extra clicks and new tabs in the browser. One thing to add is that you can’t renew or upgrade your license this way yet, but hey. There’s more versions to come.

### Ad blocking

- [Changed] Whale browser has been added to the known browsers list #3175
- [Fixed] “Exclude from filtering” button behavior #3052
- [Fixed] Google Now can’t be updated with “Always-on-VPN” enabled #3039
- [Fixed] AdGuard Extra enables automatically when there’s an available update #3216
- [Improved] DNS filtering to block cloaked trackers #3228
- [Improved] “Block phishing and malware” option now is enabled automatically when Premium gets activated #3249
- [Improved] Now AdGuard can block AAAA requests in networks without IPv6 interface #3197

### UI

- [Added] “Failed to move the certificate” notification for rooted devices with Magisk firmware #2941
- [Changed] AdGuard now remembers the selected type of data to display in Apps Management #3140
- [Fixed] Search on Apps Managements screen is working slow #2951
- [Fixed] Certificate installation dialog is missing #3176
- [Fixed] Wrong toast notification is displayed when the license expires #3183
- [Changed] “Clear DNS statistics” warning description #3194
- [Improved] Phrasing on onboarding screens #3248
- [Improved] Phrasing in the Apps Management details activity #3250
- [Improved] Localizations have been updated

### Networking

- [Added] A prevention system for connections overflow #2989
- [Changed] DNS-over-HTTPS connections number limit has been abolished  #3224
- [Fixed] Some apps don't see available WiFi networks when AdGuard local VPN is up #2836
- [Fixed] “Missed ad” option in the Feedback section leads to an error if DuckDuckGo is selected as the default browser #3128
- [Fixed] Compatibility issues
- [Improved] Connection error processing #3195

 ### Other

- [Fixed] Crash when the app runs scheduled tasks #3164
- [Fixed] Crash in the Updates activity #3165
- [Fixed] Crash when Android OS tries to load the icon #3166
- [Fixed] Crash on some Android builds #3167
- [Fixed] Crash in the main activity #3168
- [Fixed] Crash when user communicates with the extensions activity #3171
- [Fixed] Crash when the log is being collected #3212
- [Fixed] Crash on MIUI phones with Ultra battery saver #3210
- [Fixed] Max imported settings file size increased to 10 Mb #3203

## 3.3 beta 2

- Published: 2019-10-24T16:44:48Z
- Release: https://github.com/AdguardTeam/AdguardForAndroid/releases/tag/v3.3-beta-2

It seems that the first AdGuard v3.3 beta has opened the floodgates, and now there’s no power in the world to stop our developers from releasing more and more. Only one week has passed since, and we’re already presenting the next one. This time, our designers had a say too, and this is reflected in several UI-related changes that you won’t be able to miss.

**[Changed] The onboarding process #2895**

We sure love us some redesign! This time, we revamped the onboarding sequence (basically, what you see when you launch the app for the first time). Key changes:

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/welcome.png" width="300"> <img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/create_vpn.png" width="300">

- An option to choose a ‘quick’ or a ‘long’ configuration: you’ll be asked to either make only key decisions or set most of the settings manually
- New option to allow sending some technical and interaction information that will help us further improve AdGuard
- Better graphics!

**[Added] HTTPs filtering dialog #2967**

HTTPS filtering is a cornerstone of AdGuard for Android. Without the permission to filter the HTTPS protocol the ad blocking power of AdGuard is severely crippled. That’s why we walk an extra mile to emphasize to users its importance. 

We show a notification on the main AdGuard screen if HTTPS filtering is not enabled yet, and when you click on it, we now show a simple yet informative GIF that explains how HTTPS filtering works and why we recommend so strongly to turn it on.

<img src="https://cdn.adguard.com/public/Adguard/Release_notes/Android/v3.3/https_dialog.gif" width="300">

- [Added] “Refresh license status” button #2988
- [Added] TLS v1.3 support for custom DNS servers #3132
- [Added] Restore purchases button: a notification if there’s nothing to restore #2990
- [Changed] Phrasing on activation screens #3141
- [Changed] Internet connection availability checking method #3095
- [Fixed] Pressing the “Buy one more license” button closes the current screen #3136
- [Fixed] Some buttons in the first start dialog boxes can’t be seen on certain device models #3114
- [Fixed] The switch for Custom filters incorrectly represents the state of the filter group #3119
- [Fixed] Compatibility issues
- [Improved] CoreLibs has been updated to v1.5.84 #3143
