// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      1.1.1
// @description  Xのホームタイムラインで「並べ替え」メニューが開かれた際、自動的に「最新」を選択します。手動での変更も可能です。
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-auto-select-following-latest-sort.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-auto-select-following-latest-sort.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    const processedMenus = new WeakSet();
    const pendingMenus = new Set();
    let frameId = 0;

    const handleMenu = (menu) => {
        if (processedMenus.has(menu)) return;

        let latestItem = null;
        let isLatestSelected = false;

        for (const item of menu.querySelectorAll('[role="menuitem"]')) {
            if (!(item.textContent || '').includes('最新')) continue;

            latestItem = item;
            isLatestSelected = item.querySelector('svg') !== null;
            break;
        }

        if (!latestItem) return;

        processedMenus.add(menu);
        if (!isLatestSelected && latestItem.isConnected) {
            latestItem.click();
        }
    };

    const flushMenus = () => {
        frameId = 0;
        for (const menu of pendingMenus) {
            handleMenu(menu);
        }
        pendingMenus.clear();
    };

    const queueMenu = (menu) => {
        if (!menu || processedMenus.has(menu)) return;

        pendingMenus.add(menu);
        if (!frameId) {
            frameId = requestAnimationFrame(flushMenus);
        }
    };

    const inspectAddedNode = (node) => {
        if (!(node instanceof Element)) return;

        queueMenu(node.matches('[role="menu"]') ? node : node.closest('[role="menu"]'));
        for (const menu of node.querySelectorAll('[role="menu"]')) {
            queueMenu(menu);
        }
    };

    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            for (const node of mutation.addedNodes) {
                inspectAddedNode(node);
            }
        }
    });

    observer.observe(document.body, { childList: true, subtree: true });
})();
