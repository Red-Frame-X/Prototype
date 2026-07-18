// ==UserScript==
// @name         𝕏 (Twitter) Auto Select Latest Sort (Smart Reset)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.3.1
// @description  𝕏のタイムラインで「並べ替え」メニューが開かれるたびに「直近」を一度だけクリックして動作を解除し、別のメニューが開かれたら再び同様に動作します。
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/x-auto-select-latest.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/x-auto-select-latest.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    /**
     * 新規に追加された要素から「直近」メニューを検出し、
     * 一度だけクリックした上でそのメニューへの介入動作を完全に解除する
     * @param {Element} rootNode 探索対象のノード
     */
    const findAndClickLatest = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        // 対象ノード自身がmenuitemか、または子孫にmenuitemを持つかを効率的に取得
        const menuItems = rootNode.getAttribute('role') === 'menuitem'
            ? [rootNode]
            : rootNode.querySelectorAll('[role="menuitem"]');

        if (menuItems.length === 0) return;

        for (const item of menuItems) {
            // 【動作解除のチェック】既にこのアイテム、または親メニューで処理完了フラグが立っている場合は無視する
            if (item.dataset.sortHandled === 'true') continue;

            // テキストが「直近」に一致するか確認
            if (item.textContent && item.textContent.trim() === '直近') {
                // ご提示いただいたソース通り、既に選択されている場合はチェックマークのSVGが存在する
                const isAlreadySelected = item.querySelector('svg');

                // 未選択状態の場合のみ、一度だけクリックを実行する
                if (!isAlreadySelected) {
                    item.click();
                }

                // 【動作の解除】このメニューアイテム、およびそれを内包するメニュー全体に対し、
                // 「処理完了（＝動作解除）」のマーカーを直接DOMに書き込む。
                // これにより、このメニューが開いている間は二度とスクリプトが介入しなくなる。
                item.dataset.sortHandled = 'true';
                const parentMenu = item.closest('[role="menu"]') || item.parentElement;
                if (parentMenu) {
                    parentMenu.dataset.sortHandled = 'true';
                }

                // 目当ての要素に対する処理と解除が完了したためループを終了
                break;
            }
        }
    };

    /**
     * XのSPAルーティングとモーダル展開領域に合わせた監視を開始
     */
    const startObserver = () => {
        // ポップアップやメニューがマウントされる #layers を優先監視し、フォールバックとして body を指定
        const targetNode = document.getElementById('layers') || document.body;

        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                if (mutation.addedNodes.length > 0) {
                    for (const node of mutation.addedNodes) {
                        // 新たに「並べ替え」メニュー（未処理のDOM）が開かれた場合のみ検出されて実行される
                        findAndClickLatest(node);
                    }
                }
            }
        });

        observer.observe(targetNode, {
            childList: true,
            subtree: true
        });
    };

    // DOMの構築完了に合わせて安全に初期化
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', startObserver);
    } else {
        startObserver();
    }
})();
