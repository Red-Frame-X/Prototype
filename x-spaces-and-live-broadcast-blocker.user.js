// ==UserScript==
// @name         X Spaces & Live Broadcast Blocker
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      2.0.0
// @description  「𝕏でライブ放送する」「スペース」バーを強制的に排除します（低負荷・CSS注入＆高堅牢性対応版）
// @author       Red Frame X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-spaces-and-live-broadcast-blocker.user.js
// @downloadURL  https://raw.githubusercontent.com/Red-Frame-X/Prototype/main/x-spaces-and-live-broadcast-blocker.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function() {
    'use strict';

    /**
     * 【ベストプラクティス適用】
     * PC・モバイル端末のCPU・バッテリー負荷を最小化するため、
     * JSのスクロール監視を廃止し、まずは静的なCSSルール（UserStyle）として非表示化を試みます。
     */
    const injectCSS = () => {
        const styleId = 'x-spaces-live-blocker-style';
        if (document.getElementById(styleId)) return;

        const style = document.createElement('style');
        style.id = styleId;
        // 難読化クラスへの依存を避け、意味論的な属性セレクタで直接隠蔽
        style.textContent = `
            button[aria-label*="ライブ放送"],
            button[aria-label*="さんがホスト"],
            button[aria-label*="スペース"],
            button[aria-label*="リスニング中"],
            [data-testid="placementTracking"]:has(button[aria-label*="スペース"]) {
                display: none !important;
                height: 0 !important;
                margin: 0 !important;
                padding: 0 !important;
                min-height: 0 !important;
                pointer-events: none !important;
            }
        `;
        (document.head || document.documentElement).appendChild(style);
    };

    /**
     * CSSの:has()等で捕捉しきれない親要素コンテナ（cellInnerDiv）のみ、
     * 最小限のJavaScriptで確実に折りたたむ
     */
    const hideParentContainer = (element) => {
        if (!element || element.style.display === 'none') return;
        
        const cellInner = element.closest('[data-testid="cellInnerDiv"]');
        const target = cellInner || element;
        
        target.style.setProperty('display', 'none', 'important');
        target.style.setProperty('height', '0', 'important');
        target.style.setProperty('margin', '0', 'important');
        target.style.setProperty('padding', '0', 'important');
        target.style.setProperty('min-height', '0', 'important');
    };

    const processDOM = () => {
        // 見出し（Header）の処理: テキスト内容による判定が必要な部分のみ抽出
        const headers = document.querySelectorAll('h2[role="heading"]:not([data-blocked="true"])');
        headers.forEach(h2 => {
            h2.setAttribute('data-blocked', 'true');
            if (h2.textContent.includes('Xでライブ放送する')) {
                hideParentContainer(h2);
            }
        });

        // ボタンの親コンテナ折りたたみ処理（ボタン自体はCSSで不可視化済み）
        const spaceButtons = document.querySelectorAll('button[aria-label*="ライブ放送"]:not([data-blocked="true"]), button[aria-label*="さんがホスト"]:not([data-blocked="true"]), button[aria-label*="スペース"]:not([data-blocked="true"])');
        spaceButtons.forEach(btn => {
            btn.setAttribute('data-blocked', 'true');
            hideParentContainer(btn);
        });
    };

    // 1. 静的CSSの注入（最も高速な非表示化）
    injectCSS();
    processDOM();

    // 2. スクロールイベント監視を廃止し、負荷を抑えたMutationObserverのみに統一
    let timeoutId = null;
    const observer = new MutationObserver(() => {
        // スロットリング処理により、連続するDOM変化時のCPU負荷を低減
        if (timeoutId) return;
        timeoutId = requestAnimationFrame(() => {
            processDOM();
            timeoutId = null;
        });
    });

    observer.observe(document.body, {
        childList: true,
        subtree: true
    });
})();
