// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      1.2.0
// @description  Xのホームで「フォロー中」を既定選択し、並べ替えメニューでは自動的に「最新」を選択します。
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

    let followingFrameId = 0;
    let lastPathname = location.pathname;
    let followingSelectionRequested = false;

    // ホームの「フォロー中」を自動選択
    const selectFollowingTab = () => {
        followingFrameId = 0;

        if (location.pathname !== lastPathname) {
            lastPathname = location.pathname;
            followingSelectionRequested = false;
        }
        if (location.pathname !== '/home') return;

        for (const tab of document.querySelectorAll('[role="tab"]')) {
            const label = (tab.textContent || '').trim();
            if (label !== 'フォロー中' && label !== 'Following') continue;

            if (tab.getAttribute('aria-selected') === 'true') {
                followingSelectionRequested = true;
                return;
            }
            if (!followingSelectionRequested && tab.isConnected) {
                followingSelectionRequested = true;
                tab.click();
            }
            return;
        }
    };

    const queueFollowingTabSelection = () => {
        if (!followingFrameId) {
            followingFrameId = requestAnimationFrame(selectFollowingTab);
        }
    };

    // 並べ替えメニューの「最新」を自動選択
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

    // DOM更新時に選択状態を再確認
    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            for (const node of mutation.addedNodes) {
                inspectAddedNode(node);
            }
        }
        queueFollowingTabSelection();
    });

    observer.observe(document.body, { childList: true, subtree: true });
    queueFollowingTabSelection();
})();
