const assert = require('node:assert/strict');
const fs = require('node:fs');
const vm = require('node:vm');
const source = fs.readFileSync(process.argv[2], 'utf8');
for (const lateLayers of [false, true]) {
    for (const selected of [false, true]) {
        const frames = [];
        const observers = [];
        let clicks = 0;
        let checked = selected;
        class Element {}
        const item = new Element();
        Object.assign(item, {
            textContent: 'Latest', isConnected: true,
            getAttribute: () => String(checked),
            querySelector: () => null,
            click: () => { clicks++; checked = true; },
            matches: () => false,
            closest: () => menu,
            querySelectorAll: () => [],
        });
        const menu = new Element();
        Object.assign(menu, {
            querySelectorAll: selector => selector === '[role="menu"]' ? [] : [item],
            matches: selector => selector === '[role="menu"]',
            closest: () => menu,
        });
        const layers = new Element();
        layers.querySelectorAll = () => [menu];
        let mounted = lateLayers ? null : layers;
        const document = { documentElement: {}, getElementById: () => mounted };
        class MutationObserver {
            constructor(callback) { this.callback = callback; observers.push(this); }
            observe(target) { this.target = target; }
            disconnect() { this.target = null; }
        }
        vm.runInNewContext(source, {
            document, Element, MutationObserver,
            requestAnimationFrame: callback => { frames.push(callback); return frames.length; },
        });
        if (lateLayers) {
            mounted = layers;
            observers.find(observer => observer.target === document.documentElement)
                .callback([{ addedNodes: [layers] }]);
        }
        while (frames.length) frames.shift()();
        assert.equal(clicks, selected ? 0 : 1, '初期メニューの未選択時だけ自動選択する');
        checked = false;
        observers.find(observer => observer.target === layers).callback([{ addedNodes: [item] }]);
        while (frames.length) frames.shift()();
        assert.equal(clicks, selected ? 0 : 1, '同じメニュー内の手動変更を維持する');
    }
}
