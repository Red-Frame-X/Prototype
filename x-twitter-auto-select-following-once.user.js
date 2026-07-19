// ==UserScript==
// @name         X (Twitter) Auto Select Following Latest Sort (Once)
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      2.0
// @description  Xのタイムラインで「並べ替え」メニューが開かれた際、未選択の場合に一度だけ「最新」を自動選択し、その後の手動変更を可能にします。
// @author       Red Frame X (Modified)
// @match        https://x.com/*
// @match        https://twitter.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    const TARGET_MENU_TEXT = "最新";

    // SPAの画面遷移を考慮した実行状態管理
    let hasProcessedForCurrentPage = false;
    let currentUrl = location.href;

    // URLの変更（画面遷移）を検知してフラグをリセットする
    function checkUrlChange() {
        if (location.href !== currentUrl) {
            currentUrl = location.href;
            hasProcessedForCurrentPage = false;
        }
    }

    function selectLatestSort() {
        // 現在の画面ですでに処理済み（自動選択 or 検知完了）の場合は手動操作を優先して中断
        if (hasProcessedForCurrentPage) return;

        const menuItems = document.querySelectorAll('div[role="menuitem"]');
        if (menuItems.length === 0) return;

        for (const item of menuItems) {
            const itemText = item.textContent ? item.textContent.trim() : "";

            if (itemText === TARGET_MENU_TEXT) {
                // 【改善ポイント】脆弱なSVGパス文字列ではなく「SVGノードの有無」で選択状態を判定
                // 提示されたHTML構造上、選択中の項目にのみチェックマークの <svg> が存在する
                const isSelected = item.querySelector('svg') !== null;

                if (!isSelected) {
                    // Reactのイベントリスナーアタッチとの競合を防ぐため、描画フレームに同期してクリック
                    requestAnimationFrame(() => {
                        item.click();
                    });
                }

                // 「最新」メニューを検知した時点で同一ページ内での処理を完了とする
                // これにより、以降ユーザーが手動でメニューを開いて「人気」に変更しても再干渉しない
                hasProcessedForCurrentPage = true;
                return;
            }
        }
    }

    // MutationObserverの最適化
    const observer = new MutationObserver((mutations) => {
        checkUrlChange();

        // ノードが追加された場合のみ検索処理を実行し、パフォーマンスを維持する
        let hasAddedNodes = false;
        for (const mutation of mutations) {
            if (mutation.addedNodes.length > 0) {
                hasAddedNodes = true;
                break;
            }
        }

        if (hasAddedNodes) {
            selectLatestSort();
        }
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    selectLatestSort();
})();
