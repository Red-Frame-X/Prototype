// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    https://greasyfork.org/ja/users/your-profile
// @version      1.0.0
// @description  Xのホームタイムラインで「並べ替え」メニューが開かれた際、自動的に「最新」を選択します。手動での変更も可能です。
// @author       You
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-following-latest-sort.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-auto-select-following-latest-sort.user.js
// @icon         https://abs.twimg.com/favicons/twitter.3.ico
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    // 処理済みのメニューDOMを追跡し、手動操作時の再強制（無限ループや操作妨害）を防ぐ
    const processedMenus = new WeakSet();

    /**
     * メニュー要素を検査し、必要であれば「最新」をクリックする
     * @param {Element} menu - 検知された role="menu" 要素
     */
    const handleMenu = (menu) => {
        // 既にこのメニューで自動選択処理を実行済みの場合はスキップ（手動変更を可能にするため）
        if (processedMenus.has(menu)) return;

        const menuItems = menu.querySelectorAll('[role="menuitem"]');
        if (menuItems.length === 0) return;

        let latestItem = null;
        let isLatestSelected = false;

        // メニューの中から「最新」の項目を探す
        for (const item of menuItems) {
            const text = item.textContent || '';
            if (text.includes('最新')) {
                latestItem = item;
                // SVG（チェックマークのアイコン）が存在すれば既に選択されていると判断
                if (item.querySelector('svg')) {
                    isLatestSelected = true;
                }
                break;
            }
        }

        // 「最新」という選択肢を含むメニュー（並べ替えメニュー）であると確認できた場合
        if (latestItem) {
            // 対象のメニューインスタンスを処理済みとしてマーク
            processedMenus.add(menu);

            // 「最新」が未選択の場合のみ、自動でクリックをトリガーする
            if (!isLatestSelected) {
                latestItem.click();
            }
        }
    };

    /**
     * MutationObserver による非同期のDOM変更監視
     * AdGuard for Android等モバイル環境でも負荷にならないようノード検査を最適化
     */
    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            if (mutation.addedNodes.length === 0) continue;

            for (const node of mutation.addedNodes) {
                if (node.nodeType !== Node.ELEMENT_NODE) continue;

                // 追加されたノード自体がメニューの場合、またはその内部にメニューが含まれる場合
                if (node.getAttribute('role') === 'menu') {
                    handleMenu(node);
                } else if (node.querySelectorAll) {
                    const menus = node.querySelectorAll('[role="menu"]');
                    for (const menu of menus) {
                        handleMenu(menu);
                    }
                }
            }
        }
    });

    // 監視の開始
    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
