// ==UserScript==
// @name         YouTube Description Auto Expander
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.1
// @description  YouTubeの動画概要欄を自動で展開します（MutationObserver対応版）
// @author       Red Frame X
// @match        https://www.youtube.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/youtube-description-auto-expander.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/youtube-description-auto-expander.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        none
// ==/UserScript==

(function() {
    'use strict';

    function tryExpandDescription() {
        const expander = document.querySelector('ytd-text-inline-expander');

        if (!expander || expander.hasAttribute('is-expanded')) {
            return;
        }

        const button = expander.querySelector('#expand');

        if (button && !button.hidden && button.offsetParent !== null) {
            button.click();
        }
    }

    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            if (mutation.type === 'childList' || mutation.type === 'attributes') {
                const target = mutation.target;
                if (target instanceof Element &&
                   (target.tagName === 'YTD-TEXT-INLINE-EXPANDER' ||
                    target.querySelector?.('ytd-text-inline-expander'))) {
                    tryExpandDescription();
                    break;
                }
            }
        }
    });

    function startObserver() {
        const app = document.querySelector('ytd-app');
        if (app) {
            observer.observe(app, {
                childList: true,
                subtree: true,
                attributes: true,
                attributeFilter: ['hidden', 'is-expanded']
            });
            tryExpandDescription();
        } else {
            setTimeout(startObserver, 500);
        }
    }

    startObserver();

    document.addEventListener('yt-navigate-finish', () => {
        setTimeout(tryExpandDescription, 500);
    });

})();
