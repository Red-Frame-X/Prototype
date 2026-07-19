// ==UserScript==
// @name         YouTube Shelf Force Expand
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.0
// @description  YouTubeのシェルフの「もっと見る」を強制的に展開しボタンを隠す
// @author       Red Frame X
// @match        https://www.youtube.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/youtube-shelf-force-expand.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/youtube-shelf-force-expand.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        GM_addStyle
// @run-at       document-start
// ==/UserScript==

(function() {
    'use strict';

    // 1. CSSルールの適用
    // AdGuard: www.youtube.com##ytd-rich-shelf-renderer .button-container
    const css = `
        ytd-rich-shelf-renderer .button-container {
            display: none !important;
        }
    `;

    if (typeof GM_addStyle !== 'undefined') {
        GM_addStyle(css);
    } else {
        const style = document.createElement('style');
        style.textContent = css;
        document.head.appendChild(style);
    }

    // 2. スクリプトレットのロジック（属性操作）
    function applyAttributes() {
        const hiddenItems = document.querySelectorAll('ytd-rich-item-renderer[hidden]');
        if (hiddenItems.length > 0) {
            for (const item of hiddenItems) {
                item.removeAttribute('hidden');
            }
        }

        const shelves = document.querySelectorAll('ytd-rich-shelf-renderer:not([is-show-more-hidden])');
        if (shelves.length > 0) {
            for (const shelf of shelves) {
                shelf.setAttribute('is-show-more-hidden', '');
            }
        }
    }

    // 3. 監視設定 (YouTubeはSPAで動的に要素が増えるため)
    const observer = new MutationObserver((mutations) => {
        let shouldProcess = false;
        for (const mutation of mutations) {
            if (mutation.addedNodes.length > 0 || mutation.type === 'attributes') {
                shouldProcess = true;
                break;
            }
        }

        if (shouldProcess) {
            applyAttributes();
        }
    });

    window.addEventListener('load', () => {
        applyAttributes();
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['hidden']
        });
    });

    applyAttributes();

})();
