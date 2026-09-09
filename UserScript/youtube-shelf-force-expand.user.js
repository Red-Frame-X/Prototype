// ==UserScript==
// @name         YouTube Shelf Force Expand
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.1.1
// @description  YouTubeのシェルフの「もっと見る」を強制的に展開しボタンを隠す
// @author       Red Frame X
// @match        https://www.youtube.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/youtube-shelf-force-expand.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/youtube-shelf-force-expand.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=youtube.com
// @grant        GM_addStyle
// @run-at       document-start
// ==/UserScript==

(function () {
    'use strict';

    // 「もっと見る」ボタンを非表示
    const css = `
        ytd-rich-shelf-renderer .button-container {
            display: none !important;
        }
    `;

    if (typeof GM_addStyle === 'function') {
        GM_addStyle(css);
    } else {
        const style = document.createElement('style');
        style.textContent = css;
        document.documentElement.appendChild(style);
    }

    // 非表示項目を表示してシェルフを展開
    const applyAttributes = () => {
        for (const item of document.querySelectorAll('ytd-rich-shelf-renderer ytd-rich-item-renderer[hidden]')) {
            item.removeAttribute('hidden');
        }

        for (const shelf of document.querySelectorAll('ytd-rich-shelf-renderer:not([is-show-more-hidden])')) {
            shelf.setAttribute('is-show-more-hidden', '');
        }
    };

    let frameId = 0;
    const scheduleApply = () => {
        if (frameId) return;

        frameId = requestAnimationFrame(() => {
            frameId = 0;
            applyAttributes();
        });
    };

    // 動的更新に合わせて再適用
    const observer = new MutationObserver(scheduleApply);

    const start = () => {
        applyAttributes();
        observer.observe(document.body, {
            childList: true,
            subtree: true,
            attributes: true,
            attributeFilter: ['hidden']
        });
    };

    if (document.body) {
        start();
    } else {
        document.addEventListener('DOMContentLoaded', start, { once: true });
    }
})();
