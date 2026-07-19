// ==UserScript==
// @name         X Auto Select Community Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      1.6.1
// @description  Xのタイムラインで「並べ替え」メニューが開かれるたびに、未選択であれば自動的に「直近」を選択し直し、その後は手動での変更も可能にします
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-community-latest-sort.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-community-latest-sort.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    // 対象となる項目名（英語・日本語対応）
    const TARGET_TEXTS = ['直近', 'Latest'];

    /**
     * 並べ替えメニューのDOMを評価・操作する
     * @param {Node} rootNode 
     */
    const handleSortMenu = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : rootNode.querySelectorAll('[role="menu"]');

        if (menus.length === 0) return;

        for (const menu of menus) {
            if (menu.getAttribute('data-sort-handled') === 'true') {
                continue;
            }

            const menuItems = menu.querySelectorAll('[role^="menuitem"]');
            let latestItem = null;

            for (const item of menuItems) {
                const text = item.textContent ? item.textContent.trim() : '';
                if (TARGET_TEXTS.includes(text)) {
                    latestItem = item;
                    break;
                }
            }

            if (!latestItem) continue;

            menu.setAttribute('data-sort-handled', 'true');

            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                latestItem.click();
            }
        }
    };

    const startObserver = () => {
        // パフォーマンス最適化: Xのポップアップマウント先である #layers を優先監視
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
