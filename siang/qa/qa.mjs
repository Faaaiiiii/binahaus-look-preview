/* SIANG — QA harness v2: ONE browser, ONE context, ONE page. Bounded waits.
   node qa.mjs sweep|touch|nojs|shots   (server on 127.0.0.1:8100)          */
import { chromium } from '/Users/fairuzjalil/Hermes/qa-node/node_modules/playwright/index.mjs';
import fs from 'node:fs';
import path from 'node:path';

const BASE = 'http://127.0.0.1:8100';
const OUT = new URL('.', import.meta.url).pathname.replace(/\/$/, '');
const MODE = process.argv[2] || 'sweep';
const PAGES = ['index.html', 'perkhidmatan.html', 'kerja.html', 'cara.html',
               'tentang.html', 'syarikat.html', 'kontak.html'];
const WIDTHS = [360, 390, 768, 1440];
const FORCE = `html.js [data-rev]{opacity:1!important;transform:none!important;transition:none!important}
html.js .cover .goldrule{transform:none!important;animation:none!important}
html.js .cover .plate--bleed img{animation:none!important}`;
const t0 = Date.now();
const log = (...a) => console.error(`[${((Date.now() - t0) / 1000).toFixed(1)}s]`, ...a);

const KIT = () => {
  const c = document.createElement('canvas'); c.width = c.height = 1;
  const ctx = c.getContext('2d', { willReadFrequently: true });
  function col(str) {
    if (!str || str === 'rgba(0, 0, 0, 0)' || str === 'transparent') return [0, 0, 0, 0];
    ctx.fillStyle = '#ff00ff'; ctx.fillRect(0, 0, 1, 1);
    ctx.fillStyle = str; ctx.fillRect(0, 0, 1, 1);
    const d = ctx.getImageData(0, 0, 1, 1).data;
    if (d[0] === 255 && d[1] === 0 && d[2] === 255 && !/ff00ff|255, 0, 255/i.test(str)) return null;
    return [d[0], d[1], d[2], d[3] / 255];
  }
  const over = (fg, bg) => [0, 1, 2].map(i => Math.round(fg[i] * fg[3] + bg[i] * (1 - fg[3]))).concat(1);
  const lum = (c2) => { const f = c2.slice(0, 3).map(v => { v /= 255; return v <= 0.03928 ? v / 12.92 : Math.pow((v + 0.055) / 1.055, 2.4); }); return 0.2126 * f[0] + 0.7152 * f[1] + 0.0722 * f[2]; };
  const ratio = (a, b) => { const l1 = lum(a), l2 = lum(b); return (Math.max(l1, l2) + 0.05) / (Math.min(l1, l2) + 0.05); };
  function bgOf(el) {
    let n = el;
    while (n && n.nodeType === 1) {
      const s = getComputedStyle(n);
      if (s.backgroundImage && s.backgroundImage !== 'none') return { c: null, why: 'image on ' + (n.className || n.tagName) };
      const cc = col(s.backgroundColor);
      if (cc && cc[3] > 0.92) return { c: cc, why: String(n.className || n.tagName) };
      n = n.parentElement;
    }
    return { c: col(getComputedStyle(document.body).backgroundColor) || [255, 255, 255, 1], why: 'body' };
  }
  const directText = (el) => { let t = ''; for (const n of el.childNodes) if (n.nodeType === 3) t += n.nodeValue; return t.trim(); };
  const visible = (el) => { const s = getComputedStyle(el); if (s.display === 'none' || s.visibility === 'hidden') return false; const r = el.getBoundingClientRect(); return r.width > 1 && r.height > 1; };
  window.__kit = { col, over, ratio, bgOf, directText, visible };
  return true;
};

const MEASURE = (cfg) => {
  const K = window.__kit;
  const out = { innerWidth: window.innerWidth, requested: cfg.width, overflow: 0, clipped: [], h1: 0, h1First: false, overlap: [], imgs: 0, imgsBad: [], fonts: {}, contrast: [], scrollH: 0, docW: 0 };
  out.docW = document.documentElement.clientWidth;
  out.overflow = document.documentElement.scrollWidth - window.innerWidth;
  out.scrollH = document.documentElement.scrollHeight;
  const all = document.querySelectorAll('body *');
  for (const el of all) {
    const s = getComputedStyle(el);
    if (s.overflowY === 'hidden' || s.overflowY === 'clip') {
      const d = el.scrollHeight - el.clientHeight;
      if (d > 12 && el.clientHeight > 0) out.clipped.push(String(el.className || el.tagName) + ' clip=' + d);
    }
  }
  const hs = [...document.querySelectorAll('h1,h2,h3,h4,h5,h6')].filter(K.visible);
  out.h1 = hs.filter(h => h.tagName === 'H1').length;
  out.h1First = hs.length > 0 && hs[0].tagName === 'H1';
  const imgs = [...document.images];
  out.imgs = imgs.length;
  out.imgsBad = imgs.filter(i => !i.complete || i.naturalWidth === 0).map(i => i.currentSrc || i.src);
  const usesSpectral600 = [...all].some(el => {
    const s = getComputedStyle(el);
    return /Spectral/.test(s.fontFamily) && parseInt(s.fontWeight, 10) >= 600 && K.directText(el).length > 0;
  });
  out.usesSpectral600 = usesSpectral600;
  out.fonts = {
    spectral400: document.fonts.check('400 16px "Spectral"'),
    spectral600: document.fonts.check('600 16px "Spectral"'),
    franklin400: document.fonts.check('400 16px "Libre Franklin"'),
    franklin600: document.fonts.check('600 16px "Libre Franklin"'),
    franklin700: document.fonts.check('700 16px "Libre Franklin"'),
  };
  const texts = [...all].filter(el => K.directText(el).length > 0 && K.visible(el));
  for (const el of texts) {
    const s = getComputedStyle(el);
    let fg = K.col(s.color); if (!fg || fg[3] < 0.05) continue;
    const bg = K.bgOf(el);
    if (!bg.c) { out.contrast.push({ sel: (el.tagName + '.' + String(el.className).split(' ')[0]).slice(0, 40), t: K.directText(el).slice(0, 24), r: null, bg: bg.why }); continue; }
    if (fg[3] < 0.95) fg = K.over(fg, bg.c);
    out.contrast.push({ sel: (el.tagName + '.' + String(el.className).split(' ')[0]).slice(0, 40), t: K.directText(el).slice(0, 24), r: Math.round(K.ratio(fg, bg.c) * 100) / 100, bg: bg.why });
  }
  const blocks = texts.map(el => ({ el, r: el.getBoundingClientRect() })).filter(b => b.r.width > 2 && b.r.height > 2);
  let n = 0;
  for (let i = 0; i < blocks.length && n < 6; i++) for (let j = i + 1; j < blocks.length && n < 6; j++) {
    const a = blocks[i], b = blocks[j];
    if (a.el.contains(b.el) || b.el.contains(a.el)) continue;
    const ox = Math.min(a.r.right, b.r.right) - Math.max(a.r.left, b.r.left);
    const oy = Math.min(a.r.bottom, b.r.bottom) - Math.max(a.r.top, b.r.top);
    if (ox > 6 && oy > 6) { out.overlap.push([a.el.className, b.el.className, Math.round(ox), Math.round(oy)]); n++; }
  }
  return out;
};

const settle = async (page, force = true) => {
  await page.evaluate(async () => {
    if (document.getElementById('__force')) return;
    const st = document.createElement('style'); st.id = '__force'; st.textContent = window.__forcecss || ''; document.head.appendChild(st);
    const step = innerHeight * 0.85;
    for (let y = 0; y < document.documentElement.scrollHeight; y += step) { scrollTo(0, y); await new Promise(r => setTimeout(r, 45)); }
    scrollTo(0, 0);
    const t = Date.now();
    while (Date.now() - t < 6000) {
      if ([...document.images].every(i => i.complete)) break;
      await new Promise(r => setTimeout(r, 120));
    }
  });
  await page.evaluate(() => document.fonts.ready.catch(() => {}));
};

const browser = await chromium.launch();
const ctx = await browser.newContext({ viewport: { width: 1440, height: 900 }, deviceScaleFactor: 1 });
const page = await ctx.newPage();
page.setDefaultTimeout(20000);
await page.addInitScript(`window.__forcecss = ${JSON.stringify(FORCE)};`);

const report = { mode: MODE, sweep: [], fails: [], lowestContrast: { ratio: 99 }, touch: {}, nojs: [], shots: [] };
fs.writeFileSync(path.join(OUT, `qa-${MODE}.json`), '{}');

const withRetry = async (label, fn) => {
  try { return await fn(); }
  catch (e) { report.fails.push(`[probe-error ${label}] ${String(e).slice(0, 140)}`); log('PROBE ERROR', label, String(e).slice(0, 120)); return null; }
};

if (MODE === 'sweep') {
  for (const w of WIDTHS) {
    await page.setViewportSize({ width: w, height: 900 });
    for (const pg of PAGES) {
      const before = report.fails.length;
      await withRetry(`${pg}@${w}`, async () => {
        const http = [], errs = [];
        const onR = r => { if (r.status() >= 400) http.push(r.status() + ' ' + r.url()); };
        const onF = r => http.push('REQFAILED ' + r.url());
        const onE = e => errs.push(String(e));
        page.on('response', onR); page.on('requestfailed', onF); page.on('pageerror', onE);
        await page.goto(`${BASE}/${pg}`, { waitUntil: 'domcontentloaded' });
        await page.waitForLoadState('load', { timeout: 15000 }).catch(() => {});
        await settle(page);
        await page.evaluate(KIT);
        const m = await page.evaluate(MEASURE, { width: w });
        m.page = pg; m.width = w;
        if (m.innerWidth !== w) report.fails.push(`[${pg}@${w}] innerWidth read back ${m.innerWidth} != ${w} — REFUSED`);
        if (m.overflow > 1) report.fails.push(`[${pg}@${w}] horizontal overflow ${m.overflow}px`);
        if (m.clipped.length) report.fails.push(`[${pg}@${w}] clipped scroll container: ${m.clipped.join(' | ')}`);
        if (m.h1 !== 1) report.fails.push(`[${pg}@${w}] h1 count ${m.h1}`);
        if (!m.h1First) report.fails.push(`[${pg}@${w}] first heading is not h1`);
        if (m.overlap.length) report.fails.push(`[${pg}@${w}] overlapping text ${JSON.stringify(m.overlap)}`);
        if (m.imgsBad.length) report.fails.push(`[${pg}@${w}] unloaded images: ${m.imgsBad.join(',')}`);
        const fontOk = m.fonts.spectral400 && m.fonts.franklin400 && m.fonts.franklin600 && m.fonts.franklin700 && (!m.usesSpectral600 || m.fonts.spectral600);
        if (!fontOk) report.fails.push(`[${pg}@${w}] fonts ${JSON.stringify(m.fonts)} usesSpectral600=${m.usesSpectral600}`);
        else if (!m.fonts.spectral600) report.spectral600Lazy = (report.spectral600Lazy || 0) + 1;
        if (http.length) report.fails.push(`[${pg}@${w}] HTTP>=400 ${http.join(' | ')}`);
        if (errs.length) report.fails.push(`[${pg}@${w}] page errors ${errs.join(' | ')}`);
        for (const c of m.contrast) {
          if (c.r === null) continue;
          if (c.r < report.lowestContrast.ratio) report.lowestContrast = { ratio: c.r, where: `${pg}@${w}`, sel: c.sel, text: c.t, bg: c.bg };
          (report.allPairs = report.allPairs || []).push({ r: c.r, where: `${pg}@${w}`, sel: c.sel, t: c.t, bg: c.bg });
          if (c.r < 4.5) report.fails.push(`[${pg}@${w}] contrast ${c.r}:1 ${c.sel} "${c.t}" (bg ${c.bg})`);
        }
        report.sweep.push({ page: pg, width: w, innerWidth: m.innerWidth, overflow: m.overflow, clipped: m.clipped.length, h1: m.h1, h1First: m.h1First, imgs: m.imgs, imgsBad: m.imgsBad.length, overlaps: m.overlap.length, contrastPairs: m.contrast.length, scrollH: m.scrollH, failed: report.fails.length - before });
        page.off('response', onR); page.off('requestfailed', onF); page.off('pageerror', onE);
        log(`  ${pg}@${w} ok  ov=${m.overflow} imgs=${m.imgs} pairs=${m.contrast.length} h=${m.scrollH}`);
      });
    }
    log(`sweep ${w}px done, fails=${report.fails.length}`);
  }
}

if (MODE === 'touch') {
  const w = 390;
  await page.setViewportSize({ width: w, height: 844 });
  await page.goto(`${BASE}/index.html`, { waitUntil: 'load' });
  await settle(page); await page.evaluate(KIT);

  // scroll-behavior:smooth makes a synchronous scrollIntoView a lie: the rect
  // is read before the scroll lands and every target reads as a probe error.
  await page.evaluate(() => { document.documentElement.style.scrollBehavior = 'auto'; });

  const WALK = (sel) => {
    const out = [];
    const els = [...document.querySelectorAll(sel)];
    els.forEach((el) => {
      const s = getComputedStyle(el);
      const label = (el.getAttribute('aria-label') || el.textContent || el.className || el.tagName).trim().slice(0, 26);
      if (s.display === 'none' || s.visibility === 'hidden' || el.getClientRects().length === 0) { out.push({ label, h: -1, rect: 0, why: 'not rendered (hidden or inside a hidden ancestor)' }); return; }
      const padAdd = (px) => { document.body.style.paddingTop = (parseFloat(getComputedStyle(document.body).paddingTop) + px) + 'px'; };
      document.body.style.paddingTop = '';
      el.scrollIntoView({ block: 'center', behavior: 'instant' });
      let r = el.getBoundingClientRect();
      if (r.top < 40) {                       // at the document top: grow the page above it so the walk is symmetric
        padAdd(Math.ceil(innerHeight / 2 - (r.top + r.height / 2)) + 40);
        el.scrollIntoView({ block: 'center', behavior: 'instant' });
        r = el.getBoundingClientRect();
      }
      const x = r.left + r.width / 2, y = r.top + r.height / 2;
      if (y < 1 || y > innerHeight - 1) { document.body.style.paddingTop = ''; out.push({ label, h: 0, rect: Math.round(r.height), why: 'probe-error(y=' + Math.round(y) + ')' }); return; }
      const hit = (yy) => { const t = document.elementFromPoint(x, yy); return !!t && (t === el || el.contains(t)); };
      let top = y, bot = y, k = 0;
      while (top > 0 && k++ < 500 && hit(top - 1)) top--;
      const clipTop = top <= 0;
      k = 0;
      while (bot < innerHeight - 1 && k++ < 500 && hit(bot + 1)) bot++;
      const clipBot = bot >= innerHeight - 1;
      document.body.style.paddingTop = '';
      out.push({ label, h: Math.round(bot - top + 1), rect: Math.round(r.height), why: 'ok', clipTop, clipBot, w: Math.round(r.width) });
    });
    return out;
  };

  const all = await page.evaluate(WALK, 'a,button');
  const rows = all.filter(r => !/^(Skip to content)$/.test(r.label));   // the skip link is measured on its own, focused
  const skip = {
    unfocused: all.find(r => r.label === 'Skip to content') || null,
    onFocus: await page.evaluate(() => {
      window.scrollTo(0, 0);
      const s = document.querySelector('.skip'); s.focus();
      const r = s.getBoundingClientRect();
      const top = document.elementFromPoint(r.left + r.width / 2, r.top + r.height / 2);
      return { h: Math.round(r.height), w: Math.round(r.width), top: Math.round(r.top), isIt: top === s || (top && s.contains(top)), visible: r.top >= 0 && r.height >= 44 };
    }),
  };
  const under = rows.filter(r => r.why === 'ok' && r.h < 44);
  report.touch = {
    measured: rows.filter(r => r.why === 'ok').length,
    pass44: rows.filter(r => r.why === 'ok' && r.h >= 44).length,
    under44: under.map(r => `${r.label}=${r.h}px(rect ${r.rect})`),
    probeErrors: rows.filter(r => String(r.why).startsWith('probe-error')).map(r => `${r.label} ${r.why}`),
    notRendered: rows.filter(r => /^not rendered/.test(r.why)).map(r => r.label + ' — ' + r.why.replace('not rendered', '')),
    clippedProbe: rows.filter(r => r.clipTop || r.clipBot).map(r => `${r.label} ${r.clipTop ? 'top-clip' : ''}${r.clipBot ? ' bottom-clip' : ''}`),
    skipLink: skip,
    all: rows.map(r => `${r.label} hit=${r.h} rect=${r.rect} ${r.why}${r.clipTop ? ' [top-clip]' : ''}${r.clipBot ? ' [bottom-clip]' : ''}`),
  };
  for (const r of under) report.fails.push(`[touch] ${r.label} hit ${r.h}px < 44px (rect ${r.rect})`);
  if (!skip.onFocus.visible) report.fails.push(`[touch] the skip link is not a visible 44px control when focused (${JSON.stringify(skip.onFocus)})`);
  log(`touch: ${report.touch.pass44}/${report.touch.measured} pass, under=${JSON.stringify(report.touch.under44)}`);

  // the menu panel: open it and measure all seven page rows + the WhatsApp row
  await page.evaluate(() => { document.querySelector('.burger').click(); });
  await page.waitForTimeout(300);
  const menuRows = await page.evaluate(WALK, '.menu a');
  const menu = await page.evaluate(() => ({
    pageLinks: document.querySelectorAll('.menu a[href$=".html"]').length,
    waLinks: document.querySelectorAll('.menu a[href^="https://wa.me/"]').length,
    visibleRows: [...document.querySelectorAll('.menu a')].filter(a => a.getBoundingClientRect().height > 1).length,
  }));
  menu.rows = menuRows.map(r => `${r.label}=${r.h}px`);
  report.touch.menu = menu;
  if (menu.pageLinks !== 7) report.fails.push(`[touch] the menu lists ${menu.pageLinks} of 7 pages`);
  if (menu.waLinks !== 1) report.fails.push(`[touch] the menu has ${menu.waLinks} WhatsApp line(s)`);
  for (const r of menuRows) if (r.why === 'ok' && r.h < 44) report.fails.push(`[touch menu] ${r.label} hit ${r.h}px < 44px`);

  // the band colours are the only place the accent is text: measure them open
  const menuContrast = await page.evaluate(() => {
    const K = window.__kit;
    const rowsOut = [];
    for (const a of document.querySelectorAll('.menu a, .menu__tag')) {
      const s = getComputedStyle(a); const fg = K.col(s.color); const bg = K.bgOf(a);
      if (fg && bg.c) rowsOut.push({ sel: String(a.className || 'a'), text: a.textContent.trim().slice(0, 22), r: Math.round(K.ratio(fg, bg.c) * 100) / 100, bg: bg.why });
    }
    return rowsOut;
  });
  report.touch.menuContrast = menuContrast;
  for (const c of menuContrast) if (c.r < 4.5) report.fails.push(`[touch menu] contrast ${c.r}:1 ${c.text}`);
  log('touch done', JSON.stringify(report.touch.under44), 'menu', menu.pageLinks, '+', menu.waLinks);
}

if (MODE === 'nojs') {
  const ctx2 = await browser.newContext({ viewport: { width: 390, height: 844 }, javaScriptEnabled: true });
  const p2 = await ctx2.newPage();
  await p2.route('**/assets/app.js', r => r.abort());
  for (const pg of PAGES) {
    await withRetry(`nojs ${pg}`, async () => {
      await p2.goto(`${BASE}/${pg}`, { waitUntil: 'load' });
      await p2.waitForTimeout(250);
      const r = await p2.evaluate(() => {
        const vis = (el) => { const s = getComputedStyle(el); const b = el.getBoundingClientRect(); return s.display !== 'none' && s.visibility !== 'hidden' && b.height > 1; };
        return {
          nav: [...document.querySelectorAll('.nav a')].filter(vis).length,
          navLabels: [...document.querySelectorAll('.nav a')].filter(vis).map(a => a.textContent.trim()),
          hiddenRev: [...document.querySelectorAll('[data-rev]')].filter(e => parseFloat(getComputedStyle(e).opacity) < 0.99).length,
          markVisible: vis(document.querySelector('.mark')),
          videos: document.querySelectorAll('video').length,
          bodyText: (document.querySelector('main') || document.body).innerText.replace(/\s+/g, ' ').length,
          hasJs: document.documentElement.classList.contains('js'),
          h1: document.querySelectorAll('h1').length,
        };
      });
      r.page = pg; report.nojs.push(r);
      if (r.hasJs) report.fails.push(`[nojs ${pg}] html.js present without JS`);
      if (r.nav < 6) report.fails.push(`[nojs ${pg}] only ${r.nav} nav links visible`);
      if (r.hiddenRev) report.fails.push(`[nojs ${pg}] ${r.hiddenRev} blocks hidden`);
      if (r.bodyText < 400) report.fails.push(`[nojs ${pg}] page incomplete (${r.bodyText} chars)`);
      if (!r.markVisible) report.fails.push(`[nojs ${pg}] wordmark link not visible`);
      const navHits = await p2.evaluate(() => {
        document.documentElement.style.scrollBehavior = 'auto';
        const out = [];
        for (const el of document.querySelectorAll('.nav a, .mark, .btn')) {
          const s = getComputedStyle(el);
          if (s.display === 'none' || el.getClientRects().length === 0) { out.push({ l: 'hidden', h: -1 }); continue; }
          const l = (el.textContent || el.getAttribute('aria-label') || '').trim().slice(0, 22);
          document.body.style.paddingTop = '';
          el.scrollIntoView({ block: 'center', behavior: 'instant' });
          let rr = el.getBoundingClientRect();
          if (rr.top < 40) { document.body.style.paddingTop = (Math.ceil(innerHeight / 2 - (rr.top + rr.height / 2)) + 40) + 'px'; el.scrollIntoView({ block: 'center', behavior: 'instant' }); rr = el.getBoundingClientRect(); }
          const x = rr.left + rr.width / 2, y = rr.top + rr.height / 2;
          if (y < 1 || y > innerHeight - 1) { document.body.style.paddingTop = ''; out.push({ l, h: 0 }); continue; }
          const hit = (yy) => { const t = document.elementFromPoint(x, yy); return !!t && (t === el || el.contains(t)); };
          let t1 = y, b1 = y, k = 0; while (t1 > 0 && k++ < 400 && hit(t1 - 1)) t1--; k = 0; while (b1 < innerHeight - 1 && k++ < 400 && hit(b1 + 1)) b1++;
          document.body.style.paddingTop = '';
          out.push({ l, h: Math.round(b1 - t1 + 1) });
        }
        return out;
      });
      r.navHits = navHits.filter(x => x.h > 0).map(x => `${x.l}=${x.h}px`);
      const navUnder = navHits.filter(x => x.h > 0 && x.h < 44);
      if (navUnder.length) report.fails.push(`[nojs ${pg}] nav/CTA under 44px: ${navUnder.map(x => x.l + '=' + x.h).join(',')}`);
      log(`  nojs ${pg} nav=${r.nav} hidden=${r.hiddenRev} videos=${r.videos} text=${r.bodyText} navHit=${JSON.stringify(navHits.filter(x => x.h > 0).map(x => x.h).sort((a, b) => a - b))}`);
    });
  }
  await ctx2.close();
}

if (MODE === 'shots') {
  for (const pg of PAGES) {
    await withRetry(`shots ${pg}`, async () => {
      for (const w of [390, 768, 1440]) {
        await page.setViewportSize({ width: w, height: 900 });
        await page.goto(`${BASE}/${pg}`, { waitUntil: 'load' });
        await settle(page);
        await page.evaluate(() => document.querySelectorAll('[data-rev]').forEach(e => e.classList.add('in')));
        await page.waitForTimeout(700);
        const name = pg.replace('.html', '');
        const full = path.join(OUT, `full-${w}-${name}.png`);
        await page.screenshot({ path: full, fullPage: true });
        const vp = path.join(OUT, `${w}-${name}.png`);
        await page.screenshot({ path: vp });
        report.shots.push(full, vp);
      }
      log(`  shots ${pg}`);
    });
  }
}

await browser.close();
fs.writeFileSync(path.join(OUT, `qa-${MODE}.json`), JSON.stringify(report, null, 1));
console.log(JSON.stringify({
  mode: MODE, runs: report.sweep.length, fails: report.fails.length,
  failList: report.fails.slice(0, 40),
  lowestContrast: report.lowestContrast,
  touch: report.touch.measured === undefined ? undefined : { measured: report.touch.measured, pass44: report.touch.pass44, under44: report.touch.under44, probeErrors: report.touch.probeErrors, notRendered: report.touch.notRendered, clippedProbe: report.touch.clippedProbe, skipLink: report.touch.skipLink, menu: report.touch.menu, menuContrast: report.touch.menuContrast },
  nojs: report.nojs.map(r => ({ page: r.page, nav: r.nav, hidden: r.hiddenRev, videos: r.videos, text: r.bodyText })),
  shots: report.shots.length,
  contrastBottom: (report.allPairs || []).sort((a, b) => a.r - b.r).slice(0, 14),
  contrastPairsTotal: (report.allPairs || []).length,
  spectral600LazyPages: report.spectral600Lazy || 0,
}, null, 1));
