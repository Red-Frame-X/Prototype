// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    http://tampermonkey.net/
// @version      2.0
// @description  Xのタイムラインで「並べ替え」メニューが開かれた際、未選択の場合に自動で「最新」を選択し、その後の手動変更を可能にします
// @author       Modified
// @match        https://x.com/*
// @match        https://twitter.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    // UI表記・アイコンの不変要素（難読化クラスに依存しない設計）
    const TARGET_MENU_TEXT = "最新";
    const SORT_MENU_HEADER = "並べ替え";
    const CHECKMARK_PATH_PREFIX = "M9.64 18.952";
    
    // SPAのナビゲーションを考慮し、ページ（URL）ごとに処理状態を管理
    let lastProcessedUrl = null;

    function selectLatestSort() {
        const currentUrl = window.location.href;
        // 現在のURLですでに処理済みの場合は介入せず、手動変更を妨げない
        if (lastProcessedUrl === currentUrl) return;

        // メニューアイテムがDOMに存在しない場合は高速に処理を中断
        const menuItems = document.querySelectorAll('div[role="menuitem"]');
        if (menuItems.length === 0) return;

        // 開かれたメニューが「並べ替え」メニューであるかを検証
        // （他の投稿メニューやアカウント切り替えメニュー等での誤作動を防止）
        const dropdown = document.querySelector('div[data-testid="Dropdown"], div[role="menu"]');
        if (!dropdown || !dropdown.textContent.includes(SORT_MENU_HEADER)) return;

        for (const item of menuItems) {
            const itemText = item.textContent ? item.textContent.trim() : "";
            
            if (itemText === TARGET_MENU_TEXT) {
                // 「最新」アイテム内のSVGチェックマークで選択状態を判定
                const isSelected = Array.from(item.querySelectorAll('path')).some(path => {
                    const d = path.getAttribute('d');
                    return d && d.startsWith(CHECKMARK_PATH_PREFIX);
                });

                // 未選択の場合のみクリックを実行
                if (!isSelected) {
                    item.click();
                }

                // クリックの有無に関わらず、現在のページでは処理完了とマークする
                // これにより、同一ページ内で再度メニューを開いた際の手動変更（「人気」等への選択）が可能になる
                lastProcessedUrl = currentUrl;
                return;
            }
        }
    }

    // MutationObserverの最適化：DOM更新ごとのCPU負荷を最小限に抑える
    const observer = new MutationObserver((mutations) => {
        // 新たにDOMノードが追加された変更イベントのみを処理対象とする
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

    // 初期ロード時にメニューが既にある場合を想定した初回実行
    selectLatestSort();
})();
