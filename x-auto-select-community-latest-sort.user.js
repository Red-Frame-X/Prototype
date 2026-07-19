// ==UserScript==
// @name         X Auto Select Community Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      1.6.3
// @description  Xのタイムラインで「並べ替え」メニューが開かれるたびに、未選択であれば自動的に「直近」を選択し直し、その後は手動での変更も可能にします
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-community-latest-sort.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-community-latest-sort.user.js
// @icon         https://abs.twimg.com/favicons/twitter.3.ico
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    const TARGET_TEXTS = new Set(['直近', 'Latest']);

    /**
     * 並べ替えメニューのDOMを評価・操作する
     * @param {Element} rootNode 
     */
    const handleSortMenu = (rootNode) => {
        // パフォーマンス最適化: rootNode自身がmenuであるか、子要素にmenuを持つ可能性を評価
        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : (rootNode.querySelectorAll ? rootNode.querySelectorAll('[role="menu"]') : []);

        if (menus.length === 0) return;

        for (const menu of menus) {
            if (menu.getAttribute('data-sort-handled') === 'true') {
                continue;
            }

            const menuItems = menu.querySelectorAll('[role^="menuitem"]');
            let latestItem = null;

            for (const item of menuItems) {
                const text = item.textContent ? item.textContent.trim() : '';
                if (TARGET_TEXTS.has(text)) {
                    latestItem = item;
                    break;
                }
            }

            if (!latestItem) continue;

            // 再帰発火や重複処理を防ぐためにフラグを確実に付与
            menu.setAttribute('data-sort-handled', 'true');

            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                // ReactのDOMライフサイクルとの競合を避け、UIアニメーションを正常にするために1フレーム遅延させる
                requestAnimationFrame(() => {
                    latestItem.click();
                });
            }
        }
    };

    /**
     * DOM監視の最適化設計:
     * タイムライン全体（document.body）の不要な監視を避け、ポップアップマウント先の #layers のみにスコープを絞る
     */
    const startObserver = () => {
        let layersObserver = null;

        const attachLayersObserver = (layersNode) => {
            if (layersObserver) return;
            layersObserver = new MutationObserver((mutations) => {
                for (const mutation of mutations) {
                    if (mutation.addedNodes.length > 0) {
                        for (const node of mutation.addedNodes) {
                            if (node.nodeType === Node.ELEMENT_NODE) {
                                handleSortMenu(node);
                            }
                        }
                    }
                }
            });
            // #layers の内部のみを監視（タイムラインのスクロール等によるDOM変更は完全に無視される）
            layersObserver.observe(layersNode, { childList: true, subtree: true });
        };

        const existingLayers = document.getElementById('layers');
        if (existingLayers) {
            attachLayersObserver(existingLayers);
        } else {
            // #layers がまだ生成されていない場合のみ、出現するまでドキュメント全体を一時的に軽量監視
            const bodyObserver = new MutationObserver((mutations, observer) => {
                const layersNode = document.getElementById('layers');
                if (layersNode) {
                    observer.disconnect(); // #layers が見つかり次第、重いbody監視を即座に破棄
                    attachLayersObserver(layersNode);
                }
            });
            bodyObserver.observe(document.documentElement, { childList: true, subtree: true });
        }
    };

    startObserver();
})();
