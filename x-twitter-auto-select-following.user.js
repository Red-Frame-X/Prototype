// ==UserScript==
// @name         X (Twitter) Auto Select Latest Sort (Smart Reset)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.6.0
// @description  Xのタイムラインで「並べ替え」メニューが開かれるたびに「直近」を一度だけ自動選択し、その後は手動で自由に選択できるようにします。
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    // 多言語対応のキーワード定義（必要に応じて追加可能）
    const LATEST_KEYWORDS = /^(\s*直近\s*|\s*Latest\s*)$/i;

    /**
     * ソートメニューを評価し、条件に合致する場合のみ「直近」を選択する
     * @param {Element} menuNode
     */
    const handleSortMenu = (menuNode) => {
        // 1. 既に処理済みのメニューはスキップし、ユーザーの手動操作を尊重する
        if (menuNode.dataset.sortHandled === 'true') return;

        // 2. menuitem, menuitemradio, menuitemcheckbox 等のロールを持つ要素を取得
        const menuItems = menuNode.querySelectorAll('[role^="menuitem"]');
        if (menuItems.length === 0) return;

        let latestItem = null;

        for (const item of menuItems) {
            const text = item.textContent || '';
            if (LATEST_KEYWORDS.test(text)) {
                latestItem = item;
                break;
            }
        }

        // 「直近」項目が存在しないメニュー（投稿のオプションメニュー等）は除外
        if (!latestItem) return;

        // 3. 対象メニューと特定できたため、処理済みフラグを立てる
        menuNode.dataset.sortHandled = 'true';

        // 4. 選択状態の判定（WAI-ARIA標準の aria-checked 属性を最優先で評価）
        const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
        const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

        // 未選択の場合のみクリックを実行する
        if (!isAriaChecked && !hasCheckmarkSvg) {
            latestItem.click();
        }
    };

    /**
     * 追加されたDOMノードから効率的にメニューを検出する
     * @param {Node} rootNode
     */
    const inspectAddedNode = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        // 追加されたノード自体がメニューの場合
        if (rootNode.getAttribute('role') === 'menu') {
            handleSortMenu(rootNode);
        }

        // 追加されたノードの子孫にメニューが存在する場合
        const nestedMenus = rootNode.querySelectorAll('[role="menu"]');
        for (const menu of nestedMenus) {
            handleSortMenu(menu);
        }
    };

    const startObserver = () => {
        // Xのポップアップレイヤーが格納されるコンテナを優先的に監視
        const targetNode = document.getElementById('layers') || document.body;

        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                if (mutation.addedNodes.length > 0) {
                    for (const node of mutation.addedNodes) {
                        inspectAddedNode(node);
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
