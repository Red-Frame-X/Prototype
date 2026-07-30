// ==UserScript==
// @name         X Spaces & Live Broadcast Blocker
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      2.0.1
// @description  「𝕏でライブ放送する」「スペース」バーを強制的に排除します（低負荷・CSS注入＆高堅牢性対応版）
// @author       Red Frame X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-spaces-and-live-broadcast-blocker.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-spaces-and-live-broadcast-blocker.user.js
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
     * CSSの:has()等で捕捉しきれない親要素コンテナのみ、
     * 最小限のJavaScriptで確実に折りたたむ
     */
    const hideParentContainer = (element) => {
        if (!element || element.style.display === 'none') return;
        
        const cellInner = element.closest('[data-testid="cellInnerDiv"]');
        
        // 修正箇所: cellInnerDivが見つからない場合、直接の親要素(parentElement)を隠蔽対象とする
        // これにより「Xでライブ放送する」の外枠となっている div.css-175oi2r 等の空白残りを防ぐ
        const target = cellInner || element.parentElement || element;
        
        target.style.setProperty('display', 'none', 'important');
        target.style.setProperty('height', '0', 'important');
        target.style.setProperty('margin', '0', 'important');
        target.style.setProperty('padding', '0', 'important');
        target.style.setProperty('min-height', '0', 'important');
        target.style.setProperty('border', 'none', 'important'); // 枠線の残存対策
    };

    const processDOM = () => {
        // 見出し（Header）の処理: テキスト内容による判定が必要な部分のみ抽出
        const headers = document.querySelectorAll('h2[role="heading"]:not([data-blocked="true"])');
        headers.forEach(h2 => {
            h2.setAttribute('data-blocked', 'true');
            if (h2.textContent.includes('Xでライブ放送する') || h2.textContent.includes('𝕏でライブ放送する')) {
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

    // 2. スロットリングを用いたMutationObserverによる監視
    let timeoutId = null;
    const observer = new MutationObserver(() => {
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
