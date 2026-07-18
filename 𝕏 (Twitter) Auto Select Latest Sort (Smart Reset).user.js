// ==UserScript==
// @name         𝕏 (Twitter) Auto Select Latest Sort (Smart Reset)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.5.0
// @description  𝕏のタイムラインで「並べ替え」メニューが開かれた際、未選択の場合に「直近」を一度だけクリックして動作を解除し、手動での自由な選択を可能にします。
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    /**
     * DOM要素から「直近」のメニューアイテムを探し、適切に自動選択と介入解除を行う
     * @param {Element} rootNode MutationObserverから検知された追加ノード
     */
    const handleSortMenu = (rootNode) => {
        if (rootNode.nodeType !== Node.ELEMENT_NODE) return;

        // Xのメニューは通常 #layers の下に [role="menu"] としてマウントされる
        const menus = rootNode.getAttribute('role') === 'menu'
            ? [rootNode]
            : rootNode.querySelectorAll('[role="menu"]');

        if (menus.length === 0) return;

        for (const menu of menus) {
            // 【介入解除チェック】
            // 既にこのメニューコンテナに対して処理を行った場合は即座にスキップし、手動操作を絶対に阻害しない
            if (menu.dataset.sortHandled === 'true') continue;

            // role="menuitem", role="menuitemradio", role="menuitemcheckbox" を包括的に取得
            const menuItems = menu.querySelectorAll('[role^="menuitem"]');
            let latestItem = null;

            for (const item of menuItems) {
                // テキストの完全一致・前後の余白除去で正確に「直近」を特定
                if (item.textContent && item.textContent.trim() === '直近') {
                    latestItem = item;
                    break;
                }
            }

            // 「直近」が存在しないメニュー（ツイートの共有メニューや設定メニューなど）は無視
            if (!latestItem) continue;

            // 【ロックの実行】
            // 「直近」が含まれる並べ替えメニューと特定できた時点で、即座に処理済みフラグを刻印する。
            // これにより、自動クリック直後や、ユーザーが手動でメニューを開き直した際にもスクリプトは完全に沈黙する。
            menu.dataset.sortHandled = 'true';

            // 【厳格な選択状態の判定】
            // 脆弱な「svgの存在確認」だけでなく、WAI-ARIA標準属性(aria-checked)と
            // XのDOMの特性（チェックマークアイコン）を複数併用して「既に選択済みか」を厳密に評価する。
            const isAriaChecked = latestItem.getAttribute('aria-checked') === 'true';
            const hasCheckmarkSvg = latestItem.querySelector('svg') !== null;

            // 「直近」がまだ選択されていない場合のみ、1回だけクリックしてタイムラインを切り替える
            if (!isAriaChecked && !hasCheckmarkSvg) {
                latestItem.click();
            }
            // 既に選択されている場合（＝ユーザーが手動で並べ替えメニューを開き直した時）は、
            // 何もクリックせずに処理を終了するため、メニューが開いたまま「関連」や「いいね」を自由にクリックできる。
        }
    };

    /**
     * XのSPA構造とモーダル展開領域(#layers)に最適化した低負荷・高レスポンスな監視を開始
     */
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
