import { chromium } from '/Users/fairuzjalil/Hermes/qa-node/node_modules/playwright/index.mjs';
const b = await chromium.launch();
const out = {};
for (const w of [390, 1440]) {
  const p = await (await b.newContext({ viewport: { width: w, height: 900 } })).newPage();
  await p.goto('http://127.0.0.1:8100/index.html', { waitUntil: 'load' });
  await p.waitForTimeout(300);
  out[w] = await p.evaluate(() => {
    const rows = [];
    const probes = [['.section', 'section'], ['.band', 'band'], ['.cta', 'cta'], ['.ftr__bar', 'ftr__bar'], ['.cover__head', 'cover__head'], ['.hdr__in', 'hdr__in']];
    for (const [sel, name] of probes) {
      for (const el of document.querySelectorAll(sel)) {
        const es = getComputedStyle(el);
        const eb = el.getBoundingClientRect();
        const txt = [...el.querySelectorAll('p,h1,h2,h3,b,dd,dt,li,span,small')].find(t => t.textContent.trim() && t.getClientRects().length);
        let gap = null;
        if (txt) {
          const tr = txt.getBoundingClientRect();
          // distance from the boundary (border-top of el) down to the first line box of the text
          gap = Math.round(tr.top - eb.top);
        }
        rows.push({ name, cls: String(el.className).slice(0, 34), padTop: es.paddingTop, padBlock: es.paddingBlock, borderTop: es.borderTopWidth + ' ' + es.borderTopStyle, gapToFirstText: gap, boxH: Math.round(eb.height) });
      }
    }
    return rows;
  });
}
console.log(JSON.stringify(out, null, 1));
await b.close();
