// ==UserScript==
// @name         X Auto Select Community Latest Sort
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.6.0
// @description  Xのタイムラインで「並べ替え」メニューが開かれるたびに、未選択であれば自動的に「直近」を選択し直し、その後は手動での変更も可能にします
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

    // 対象となる項目名（将来的な英語UI等のサポートを考慮し配列化）
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
            // 既にこのメニューDOMに対する判定・自動選択が処理済みである場合はスキップ
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

            // 「直近」を含まない全く別のメニュー（ツイートのオプション等）だった場合は無視
            if (!latestItem) continue;

            // MutationObserverによる重複処理を防ぐため、対象のメニューであると判明した時点で処理済みマークを付与
            menu.setAttribute('data-sort-handled', 'true');

            // 選択状態の判定（aria-checked属性 または SVGチェックマークの存在）
            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                // 「直近」以外が選択されている（未選択の）場合のみ自動クリックを実行
                latestItem.click();
            }
        }
    };

    const startObserver = () => {
        // X (Twitter) のポップアップやメニューは原則として #layers 配下にマウントされるため、
        // 監視対象を絞り込んでパフォーマンスの低下を防ぐ
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
