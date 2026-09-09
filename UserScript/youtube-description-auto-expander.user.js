// ==UserScript==
// @name         YouTube Description Auto Expander
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.2.0
// @description  YouTubeの動画概要欄を自動で展開します（MutationObserver対応版）
// @author       Red Frame X
// @match        https://www.youtube.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/youtube-description-auto-expander.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/youtube-description-auto-expander.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        none
// ==/UserScript==

(function () {
    'use strict';

    // 未展開の概要欄を自動で開く
    const tryExpandDescription = () => {
        const expander = document.querySelector('ytd-text-inline-expander');

        if (!expander || expander.hasAttribute('is-expanded')) return;

        const button = expander.querySelector('#expand');
        if (button && !button.hidden && button.offsetParent !== null) {
            button.click();
        }
    };

    let frameId = 0;
    const scheduleExpand = () => {
        if (frameId) return;

        frameId = requestAnimationFrame(() => {
            frameId = 0;
            tryExpandDescription();
        });
    };

    // YouTubeの動的更新を監視
    const observer = new MutationObserver(scheduleExpand);

    const observeApp = (app) => {
        observer.observe(app, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['hidden', 'is-expanded']
        });
        scheduleExpand();
    };

    const app = document.querySelector('ytd-app');
    if (app) {
        observeApp(app);
    } else {
        const bootstrapObserver = new MutationObserver(() => {
            const mountedApp = document.querySelector('ytd-app');
            if (!mountedApp) return;

            bootstrapObserver.disconnect();
            observeApp(mountedApp);
        });
        bootstrapObserver.observe(document.documentElement, { childList: true, subtree: true });
    }

    // ページ内遷移後にも再確認
    let navigationTimer = 0;
    document.addEventListener('yt-navigate-finish', () => {
        clearTimeout(navigationTimer);
        navigationTimer = setTimeout(scheduleExpand, 500);
    });
})();
