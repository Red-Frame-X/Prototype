// ==UserScript==
// @name         X (Twitter) Auto Select Following (Once)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.3
// @description  x.comのホーム画面アクセス時に、1回だけ「フォロー中」タブを自動クリックし、その後スクリプトを停止します
// @author       Red Frame X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-twitter-auto-select-following.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-twitter-auto-select-following.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    const TARGET_TAB_TEXT = "フォロー中";
    let hasClicked = false;

    function clickFollowingTab() {
        if (hasClicked) return;
        if (location.pathname !== '/home') return;

        const tabs = document.querySelectorAll('div[role="tab"]');

        for (const tab of tabs) {
            if (tab.textContent.includes(TARGET_TAB_TEXT)) {
                const isSelected = tab.getAttribute('aria-selected') === 'true';

                if (!isSelected) {
                    tab.click();
                }

                hasClicked = true;
                if (observer) {
                    observer.disconnect();
                }
                return;
            }
        }
    }

    const observer = new MutationObserver((mutations) => {
        clickFollowingTab();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    clickFollowingTab();

})();
