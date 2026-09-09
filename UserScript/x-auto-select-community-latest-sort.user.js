// ==UserScript==
// @name         X Auto Select Community Latest Sort
// @namespace    https://github.com/Red-Frame-X/Prototype
// @license      CC0-1.0
// @version      1.7.0
// @description  Xのタイムラインで「並べ替え」メニューが開かれるたびに、未選択であれば自動的に「直近」を選択し直し、その後は手動での変更も可能にします
// @author       Red-Frame-X
// @match        https://x.com/*
// @match        https://twitter.com/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-auto-select-community-latest-sort.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/x-auto-select-community-latest-sort.user.js
// @icon         https://www.google.com/s2/favicons?sz=64&domain=x.com
// @grant        none
// @run-at       document-idle
// ==/UserScript==

(function () {
    'use strict';

    const TARGET_TEXTS = new Set(['直近', 'Latest']);
    const processedMenus = new WeakSet();
    const pendingMenus = new Set();
    let frameId = 0;

    const handleMenu = (menu) => {
        if (processedMenus.has(menu)) return;

        let latestItem = null;
        for (const item of menu.querySelectorAll('[role^="menuitem"]')) {
            const text = item.textContent ? item.textContent.trim() : '';
            if (TARGET_TEXTS.has(text)) {
                latestItem = item;
                break;
            }
        }

        if (!latestItem) return;

        processedMenus.add(menu);
        const isSelected = latestItem.getAttribute('aria-checked') === 'true'
            || latestItem.querySelector('svg') !== null;

        if (!isSelected && latestItem.isConnected) {
            latestItem.click();
        }
    };

    const flushMenus = () => {
        frameId = 0;
        for (const menu of pendingMenus) {
            handleMenu(menu);
        }
        pendingMenus.clear();
    };

    const queueMenu = (menu) => {
        if (!menu || processedMenus.has(menu)) return;

        pendingMenus.add(menu);
        if (!frameId) {
            frameId = requestAnimationFrame(flushMenus);
        }
    };

    const inspectAddedNode = (node) => {
        if (!(node instanceof Element)) return;

        queueMenu(node.matches('[role="menu"]') ? node : node.closest('[role="menu"]'));
        for (const menu of node.querySelectorAll('[role="menu"]')) {
            queueMenu(menu);
        }
    };

    const attachObserver = (layers) => {
        const observer = new MutationObserver((mutations) => {
            for (const mutation of mutations) {
                for (const node of mutation.addedNodes) {
                    inspectAddedNode(node);
                }
            }
        });
        observer.observe(layers, { childList: true, subtree: true });
    };

    const layers = document.getElementById('layers');
    if (layers) {
        attachObserver(layers);
    } else {
        const bootstrapObserver = new MutationObserver(() => {
            const mountedLayers = document.getElementById('layers');
            if (!mountedLayers) return;

            bootstrapObserver.disconnect();
            attachObserver(mountedLayers);
        });
        bootstrapObserver.observe(document.documentElement, { childList: true, subtree: true });
    }
})();
