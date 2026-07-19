// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @version      2.1.1
// @description  Xのタイムラインで「並べ替え」メニューが開かれた際、未選択の場合に自動で「最新」を選択し、その後の手動変更を可能にします
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-following-latest-sort.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-following-latest-sort.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    // 多言語環境や仕様変更を考慮し、Setでターゲット文字列を管理
    const TARGET_TEXTS = new Set(['最新', 'Latest']);

    /**
     * 並べ替えメニューのDOMを評価・操作する
     * URL依存の制御を廃止し、DOM要素単体の処理済みフラグで管理する
     * @param {Element} rootNode 
     */
    const handleSortMenu = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        // パフォーマンス最適化: rootNode自身、または子要素のメニューのみを抽出
        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : (rootNode.querySelectorAll ? rootNode.querySelectorAll('[role="menu"]') : []);

        if (menus.length === 0) return;

        for (const menu of menus) {
            // 既に自動選択処理を実行済みのメニューはスキップし、ユーザーの手動変更を可能にする
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

            // 処理済みフラグを付与して再発火を完全に防止
            menu.setAttribute('data-sort-handled', 'true');

            // SVGパスのハードコードを避け、WAI-ARIA仕様とDOM構造から選択状態を安全に評価
            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                // React/SPAのDOM描画サイクルとの競合を避けるため、1フレーム遅延させて安全にイベントをディスパッチ
                requestAnimationFrame(() => {
                    latestItem.click();
                });
            }
        }
    };

    /**
     * モバイル最適化監視設計:
     * タイムラインのスクロールによる不要なDOM監視を完全に排除するため、
     * モーダルやポップアップがマウントされる #layers 内部のみを厳格に監視する
     */
    const startObserver = () => {
        let layersObserver = null;

        const attachLayersObserver = (layersNode) => {
            if (layersObserver) return;
            layersObserver = new MutationObserver((mutations) => {
                for (const mutation of mutations) {
                    if (mutation.addedNodes.length > 0) {
                        for (const node of mutation.addedNodes) {
                            handleSortMenu(node);
                        }
                    }
                }
            });
            // #layers 内部のみ監視。ツイートのスクロール等のタイムライン変化は一切干渉しない
            layersObserver.observe(layersNode, { childList: true, subtree: true });
        };

        const existingLayers = document.getElementById('layers');
        if (existingLayers) {
            attachLayersObserver(existingLayers);
        } else {
            // #layers が未生成の場合のみ、出現まで軽量監視を行い、見つかり次第即座に破棄する
            const bodyObserver = new MutationObserver((mutations, observer) => {
                const layersNode = document.getElementById('layers');
                if (layersNode) {
                    observer.disconnect();
                    attachLayersObserver(layersNode);
                }
            });
            bodyObserver.observe(document.documentElement, { childList: true, subtree: true });
        }
    };

    startObserver();
})();
