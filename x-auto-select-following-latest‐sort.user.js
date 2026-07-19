// ==UserScript==
// @name         X Auto Select Following Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @version      2.1.0
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

(function() {
    'use strict';

    const TARGET_MENU_TEXT = "最新";
    const SORT_MENU_HEADER = "並べ替え";
    const CHECKMARK_PATH_PREFIX = "M9.64 18.952";
    
    let lastProcessedUrl = null;

    function selectLatestSort() {
        const currentUrl = window.location.href;
        if (lastProcessedUrl === currentUrl) return;

        const menuItems = document.querySelectorAll('div[role="menuitem"]');
        if (menuItems.length === 0) return;

        const dropdown = document.querySelector('div[data-testid="Dropdown"], div[role="menu"]');
        if (!dropdown || !dropdown.textContent.includes(SORT_MENU_HEADER)) return;

        for (const item of menuItems) {
            const itemText = item.textContent ? item.textContent.trim() : "";
            
            if (itemText === TARGET_MENU_TEXT) {
                const isSelected = Array.from(item.querySelectorAll('path')).some(path => {
                    const d = path.getAttribute('d');
                    return d && d.startsWith(CHECKMARK_PATH_PREFIX);
                });

                if (!isSelected) {
                    item.click();
                }

                lastProcessedUrl = currentUrl;
                return;
            }
        }
    }

    // 監視対象を #layers または body に最適化し、CPU負荷を軽減
    const targetNode = document.getElementById('layers') || document.body;

    const observer = new MutationObserver((mutations) => {
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

    observer.observe(targetNode, {
        childList: true,
        subtree: true
    });

    selectLatestSort();
})();
