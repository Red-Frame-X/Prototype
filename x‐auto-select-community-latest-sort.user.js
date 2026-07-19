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

    // SPA（単一ページアプリケーション）のページ遷移を追跡し、
    // 「現在のURL（タイムライン）につき1回だけ自動選択を行う」ための状態管理
    let currentUrl = location.href;
    let isAutoSelectedForCurrentUrl = false;

    // 対象となる項目名（将来的な英語UI等のサポートを考慮し配列化）
    const TARGET_TEXTS = ['直近', 'Latest'];

    /**
     * URLの変更を検知し、処理済みの状態をリセットする
     */
    const checkAndResetIfUrlChanged = () => {
        if (currentUrl !== location.href) {
            currentUrl = location.href;
            isAutoSelectedForCurrentUrl = false;
        }
    };

    /**
     * 並べ替えメニューのDOMを評価・操作する
     * @param {Node} rootNode 
     */
    const handleSortMenu = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        checkAndResetIfUrlChanged();

        // 既に現在のページ（タイムライン）で自動選択を処理済みの場合は、
        // ユーザーの手動操作を優先して一切の介入を行わない
        if (isAutoSelectedForCurrentUrl) return;

        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : rootNode.querySelectorAll('[role="menu"]');

        if (menus.length === 0) return;

        for (const menu of menus) {
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

            // 選択状態の判定（aria-checked属性 または SVGチェックマークの存在）
            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            if (!isAriaChecked && !hasCheckmarkSvg) {
                // 「直近」以外が選択されている（未選択の）場合のみ自動クリックを実行
                latestItem.click();
            }

            // メニューの確認および自動選択が完了したためフラグを立てる
            // （これ以降、同じタイムラインにいる間はメニューを再展開しても自動クリックされない）
            isAutoSelectedForCurrentUrl = true;
            break;
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
