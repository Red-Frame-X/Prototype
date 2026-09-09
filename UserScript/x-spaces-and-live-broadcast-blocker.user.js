// ==UserScript==
// @name         X スペース・ライブ放送非表示
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      2.1.0
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

(function () {
    'use strict';

    const style = document.createElement('style');
    style.id = 'x-spaces-live-blocker-style';
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
    if (!document.getElementById(style.id)) {
        (document.head || document.documentElement).appendChild(style);
    }

    const processedElements = new WeakSet();
    const pendingRoots = new Set();
    const targetSelector = [
        'h2[role="heading"]',
        'button[aria-label*="ライブ放送"]',
        'button[aria-label*="さんがホスト"]',
        'button[aria-label*="スペース"]'
    ].join(',');

    const hideParentContainer = (element) => {
        const target = element.closest('[data-testid="cellInnerDiv"]')
            || element.parentElement
            || element;

        for (const property of ['display', 'height', 'margin', 'padding', 'min-height', 'border']) {
            target.style.setProperty(property, property === 'display' ? 'none' : '0', 'important');
        }
    };

    const processElement = (element) => {
        if (processedElements.has(element)) return;

        if (element.matches('h2[role="heading"]')) {
            const text = element.textContent;
            if (!text.includes('Xでライブ放送する') && !text.includes('𝕏でライブ放送する')) {
                return;
            }
        }

        processedElements.add(element);
        hideParentContainer(element);
    };

    const processRoot = (root) => {
        if (!(root instanceof Element)) return;

        if (root.matches(targetSelector)) {
            processElement(root);
        }
        for (const element of root.querySelectorAll(targetSelector)) {
            processElement(element);
        }
    };

    const flushRoots = () => {
        frameId = 0;
        for (const root of pendingRoots) {
            processRoot(root);
        }
        pendingRoots.clear();
    };

    let frameId = 0;
    const observer = new MutationObserver((mutations) => {
        for (const mutation of mutations) {
            for (const node of mutation.addedNodes) {
                if (node instanceof Element) {
                    pendingRoots.add(node);
                }
            }
        }

        if (pendingRoots.size && !frameId) {
            frameId = requestAnimationFrame(flushRoots);
        }
    });

    processRoot(document.body);
    observer.observe(document.body, { childList: true, subtree: true });
})();
