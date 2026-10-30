// ==UserScript==
// @name         GIGAZINE 記事の空き枠補充
// @name:ja      GIGAZINE 記事の空き枠補充
// @namespace    local.gigazine
// @license      CC0-1.0
// @version      202610310740
// @description  AdGuardユーザールールによる記事の非表示を補完し、次ページの記事で空き枠を補充し、取得できない場合も最終行を記事で埋めます。
// @author       Red Frame X
// @match        https://gigazine.net/*
// @updateURL    https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/gigazine-fill-article-grid.user.js
// @downloadURL  https://github.com/Red-Frame-X/Prototype/raw/refs/heads/main/UserScript/gigazine-fill-article-grid.user.js
// @run-at       document-idle
// @grant        none
// ==/UserScript==

(async () => {
    'use strict';

    const list = document.querySelector('#section .content');
    const pager = list?.querySelector('#nextpage');
    const button = pager?.querySelector('a[href]');
    if (!list || !pager || !button) return;

    const excluded = new Set(['試食', '広告', '有料メンバー']);
    const buffer = [];
    const seen = new Set();
    const fetched = new Set([location.href]);
    const originalLabel = button.textContent;
    let next = sameOrigin(button.getAttribute('href'), location.href);
    let busy = false;
    let failed = false;
    let retryMore = false;
    let queued = false;
    let columns = 1;
    let layoutKey = '';
    const gridValue = list.style.getPropertyValue('grid-template-columns');
    const gridPriority = list.style.getPropertyPriority('grid-template-columns');
    const layoutStyle = document.createElement('style');
    layoutStyle.textContent = `
        #section .content > section[data-gigazine-empty] { display: none !important; }
        #section .content > #nextpage { grid-column: 1 / -1 !important; }
    `;
    document.head.append(layoutStyle);

    // 最終行を均等に広げるため、通常行と最終行の共通の細かいGridを使う。
    // 通信の成功を前提にしないため、取得不能・末尾到達時にも空き枠を残さない。
    function layout() {
        observer.disconnect();
        try {
            if (gridValue) list.style.setProperty('grid-template-columns', gridValue, gridPriority);
            else list.style.removeProperty('grid-template-columns');
            // 前回のspanが暗黙の列を作る前に、配置を通常に戻す。
            const sections = cards();
            sections.forEach(section => section.style.removeProperty('grid-column'));
            const tracks = getComputedStyle(list).gridTemplateColumns;
            columns = Math.max(1, tracks.match(/(?:\([^)]*\)|[^\s])+/g)?.length || 1);
            const visible = [];
            for (const section of sections) {
                section.removeAttribute('data-gigazine-empty');
                section.style.removeProperty('grid-column');
                const card = section.querySelector(':scope > .card');
                const hidden = [section, card].some(el => {
                    const style = getComputedStyle(el);
                    return style.display === 'none' || style.visibility === 'hidden' ||
                        style.visibility === 'collapse' || style.opacity === '0';
                });
                if (blocked(section) || hidden || !articleURL(section, location.href)) {
                    section.setAttribute('data-gigazine-empty', '');
                } else visible.push(section);
            }
            const remainder = visible.length % columns;
            const unit = remainder || 1;
            list.style.setProperty('grid-template-columns',
                `repeat(${columns * unit}, minmax(0, 1fr))`, 'important');
            visible.forEach((section, index) => {
                const span = remainder && index >= visible.length - remainder ? columns : unit;
                section.style.setProperty('grid-column', `span ${span}`, 'important');
            });
            layoutKey = `${columns}:${visible.length}`;
            return visible.length;
        } finally {
            observer.observe(list, { childList: true, subtree: true, attributes: true,
                characterData: true });
        }
    }

    function schedule() {
        if (queued) return;
        queued = true;
        requestAnimationFrame(() => {
            queued = false;
            const previous = layoutKey;
            layout();
            if (previous !== layoutKey && !busy && !failed) void fill();
        });
    }
    const observer = new MutationObserver(schedule);

    const status = document.createElement('div');
    status.style.cssText = 'text-align:center;padding:6px;font-size:14px';
    status.setAttribute('role', 'status');
    pager.append(status);

    function sameOrigin(value, base) {
        if (!value) return null;
        try {
            const url = new URL(value, base);
            url.hash = '';
            return url.origin === location.origin ? url.href : null;
        } catch { return null; }
    }

    function cards() {
        return [...list.querySelectorAll(':scope > section')]
            .filter(el => el.querySelector(':scope > .card'));
    }

    function blocked(section) {
        return [...section.querySelectorAll('.catab')]
            .some(el => excluded.has(el.textContent.trim()));
    }

    function articleURL(section, base) {
        return sameOrigin(
            section.querySelector('.card h2 a[href]')?.getAttribute('href'), base
        );
    }

    function vacancies() {
        const count = layout();
        return (columns - count % columns) % columns;
    }

    function prepare(section, base) {
        section.querySelectorAll('script,iframe,object,embed')
            .forEach(el => el.remove());
        for (const el of [section, ...section.querySelectorAll('*')]) {
            // 元ページとのID重複とインラインイベントを除去する。
            for (const attr of [...el.attributes]) {
                if (attr.name === 'id' || /^on/i.test(attr.name)) {
                    el.removeAttribute(attr.name);
                }
            }
            for (const attr of ['href', 'src']) {
                const value = el.getAttribute(attr);
                if (!value) continue;
                const url = new URL(value, base);
                if (['https:', 'http:'].includes(url.protocol)) {
                    el.setAttribute(attr, url.href);
                } else {
                    el.removeAttribute(attr);
                }
            }
        }
        // 追加した記事の遅延読み込み画像を表示する。
        for (const img of section.querySelectorAll('img')) {
            const source = img.dataset.src || img.dataset.original;
            if (source) {
                const url = new URL(source, base);
                if (['https:', 'http:'].includes(url.protocol)) img.src = url.href;
            }
            if (img.dataset.srcset) img.srcset = img.dataset.srcset;
            img.classList.remove('lazyload', 'lazyloading');
            img.classList.add('lazyloaded');
            img.loading = 'lazy';
        }
        return document.importNode(section, true);
    }

    async function fetchNext() {
        if (!next || fetched.has(next)) {
            next = null;
            return;
        }
        const url = next;
        const controller = new AbortController();
        const timeout = setTimeout(() => controller.abort(), 20000);
        try {
            const response = await fetch(url, {
                credentials: 'same-origin', signal: controller.signal
            });
            if (!response.ok) throw new Error('HTTP ' + response.status);
            if (new URL(response.url).origin !== location.origin) {
                throw new Error('取得先が変わりました');
            }
            const doc = new DOMParser().parseFromString(
                await response.text(), 'text/html'
            );
            const content = doc.querySelector('#section .content');
            const sections = content?.querySelectorAll(':scope > section');
            if (!sections?.length) throw new Error('記事一覧が見つかりません');

            const additions = [];
            const keys = new Set();
            for (const section of sections) {
                const key = articleURL(section, response.url);
                if (!key || seen.has(key) || keys.has(key) || blocked(section)) continue;
                additions.push(prepare(section, response.url));
                keys.add(key);
            }
            // 解析に成功してから状態を更新し、失敗時には同じページを再試行する。
            keys.forEach(key => seen.add(key));
            buffer.push(...additions);
            fetched.add(url);
            next = sameOrigin(
                content.querySelector('#nextpage a[href]')?.getAttribute('href'),
                response.url
            );
            if (fetched.has(next)) next = null;
        } finally {
            clearTimeout(timeout);
        }
    }

    async function fill(showMore = false) {
        if (busy) return;
        busy = true;
        failed = false;
        retryMore = showMore;
        status.textContent = '次の記事を読み込み中…';
        try {
            cards().filter(blocked).forEach(el => el.remove());
            let requests = 0;
            if (showMore) {
                if (!buffer.length && next) {
                    await fetchNext();
                    requests++;
                }
                for (const section of buffer.splice(0)) {
                    list.insertBefore(section, pager);
                }
                retryMore = false;
            }
            while (vacancies()) {
                if (!buffer.length) {
                    // 除外記事が続く場合も、1回の処理で最大10ページまで取得する。
                    if (!next || requests >= 10) break;
                    await fetchNext();
                    requests++;
                    continue;
                }
                for (const section of buffer.splice(0, vacancies())) {
                    list.insertBefore(section, pager);
                }
            }
            status.textContent = !next && !buffer.length
                ? 'これ以上の記事はありません。' : '';
        } catch (error) {
            failed = true;
            status.textContent = '取得に失敗しました。ボタンで再試行してください。(' +
                error.message + ')';
        } finally {
            layout();
            busy = false;
            button.textContent = failed ? '再試行' : originalLabel;
            button.style.display = next || buffer.length || failed ? '' : 'none';
            if (next) button.href = next;
        }
    }

    for (const section of cards()) {
        const key = articleURL(section, location.href);
        if (key) seen.add(key);
    }
    button.addEventListener('click', event => {
        if (event.ctrlKey || event.metaKey || event.shiftKey || event.altKey) return;
        event.preventDefault();
        void fill(failed ? retryMore : true);
    });
    let resizeTimer;
    window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
            schedule();
        }, 300);
    });

    // CSS注入だけで行われる非表示も検出する（DOM変更を伴わない場合がある）。
    setInterval(() => {
        if (!document.hidden) schedule();
    }, 1000);
    window.addEventListener('online', () => { failed = false; void fill(retryMore); });
    document.addEventListener('visibilitychange', schedule);
    layout();
    await fill();
    // AdGuardの非表示処理が遅れて反映された場合にも補充する。
    setTimeout(() => {
        if (!failed) void fill();
    }, 1500);
})();
