// ==UserScript==
// @name         X (Twitter) Auto Select Latest Sort (Most Recent)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.5.0
// @description  𝕏のタイムラインで「並べ替え」メニューが開かれた際、未選択の場合に「直近」を一度だけクリックして動作を解除し、手動での自由な選択を可能にします。
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-twitter-auto-select-latest-sort.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-twitter-auto-select-latest-sort.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    const handleSortMenu = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : rootNode.querySelectorAll('[role="menu"]');

        if (menus.length === 0) return;

        for (const menu of menus) {
            if (menu.dataset.sortHandled === 'true') continue;

            const menuItems = menu.querySelectorAll('[role^="menuitem"]');
            let latestItem = null;

            for (const item of menuItems) {
                if (item.textContent && item.textContent.trim() === '直近') {
                    latestItem = item;
                    break;
                }
            }

            if (!latestItem) continue;

            menu.dataset.sortHandled = 'true';

            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                latestItem.click();
            }
        }
    };

    const startObserver = () => {
        const targetNode = document.getElementById('layers') || document.body;

        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                if (mutation.addedNodes.length > 0) {
                    for (const node of mutation.addedNodes) {
                        handleSortMenu(node);
                    }
                }
            }
        });

        observer.observe(targetNode, {
            childList: true,
            subtree: true
        });
    };

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startObserver);
    } else {
        startObserver();
    }
})();
