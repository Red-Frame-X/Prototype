// ==UserScript==
// @name         X (Twitter) Auto Select Following Latest Sort Once
// @namespace    http://tampermonkey.net/
// @license      CC0-1.0
// @version      1.5
// @description  Xのタイムラインで「並べ替え」メニューが開かれた際、一度だけ「最新」を自動選択し、その後の手動変更を可能にします
// @author       Red Frame X (Modified)
// @match        https://x.com/*
// @match        https://twitter.com/*
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    // ターゲットとするメニューの完全なテキスト（UI表記に準拠）
    const TARGET_MENU_TEXT = "最新";
    // 選択時に表示されるチェックマークアイコンの特有のパスデータ
    const CHECKMARK_PATH_PREFIX = "M9.64 18.952";
    
    let hasClicked = false;

    function selectLatestSort() {
        if (hasClicked) return;

        // ドロップダウンメニューのアイテムを取得（生成前なら処理中断）
        const menuItems = document.querySelectorAll('div[role="menuitem"]');
        if (menuItems.length === 0) return;

        for (const item of menuItems) {
            // 前後の余白を除去したテキストがターゲットと完全に一致するか判定
            const itemText = item.textContent ? item.textContent.trim() : "";
            
            if (itemText === TARGET_MENU_TEXT) {
                // チェックマークのSVGパスが存在するかで「選択済み」かを判定
                const isSelected = Array.from(item.querySelectorAll('path')).some(path => {
                    const d = path.getAttribute('d');
                    return d && d.startsWith(CHECKMARK_PATH_PREFIX);
                });

                // 未選択の場合のみクリックを実行
                if (!isSelected) {
                    item.click();
                }

                // 「最新」メニューを検知した時点で（クリック有無に関わらず）処理完了とし、監視を完全停止
                hasClicked = true;
                if (observer) {
                    observer.disconnect();
                }
                return;
            }
        }
    }

    // メニューが開かれてDOMに追加されるタイミングを監視
    const observer = new MutationObserver(() => {
        selectLatestSort();
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });

    // 初期ロード時にすでにメニューが存在する場合を考慮した初回実行
    selectLatestSort();

})();
