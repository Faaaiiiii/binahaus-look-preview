# DESIGN.md — Bina Haus, arah 06 "PITA" (the reel / the tape)

> The prose contract: why each decision was taken, the provenance of every local asset, and the
> gate results. Product truth is in `../PRODUCT.md`; the seven decisions are in `COMMIT-SHEET.md`.

Everything on this page comes from the owner. Nothing was invented and nothing that belongs to the
brand was redrawn: the logo is his own PNG, the colours are read out of his stylesheet, the
photographs, renders, posters and videos are his, and every sentence of copy is his, verbatim.

## The contract

| decision | value | where it comes from |
|---|---|---|
| ground | `--navy oklch(28.83% .0503 265.9)` | his `styles-BIzBvBjK.css` |
| inset (frames, CTA band) | `--inset = color-mix(in oklab, --navy 84%, black)` | his navy, shaded — no new colour |
| type on navy | `--ink = --beige-soft oklch(97.96% .0057 84.57)`, `--ink-2 = color-mix(--beige 84%, --navy)` | his stylesheet |
| the one accent | `--gold oklch(74.04% .0992 86.94)` | his stylesheet — the logo's own flat gold measures `#D5A64C`, the same colour |
| label / display face | **Barlow Semi Condensed** 500/600/700 | self-hosted woff2 (Google Fonts, SIL OFL 1.1) |
| text face | **Newsreader** 400 + 400 italic | self-hosted woff2 (Google Fonts, SIL OFL 1.1) |
| logo | `assets/logo/bina-haus-logo*.png` | his `bina-haus-logo.png`, only the transparent margin trimmed and re-encoded |
| type scale | `--s0` .72rem → `--s6` clamp(2.35rem … 5rem) | — |
| body measure | ≤ 66ch (`--line-h 1.64`; phone 1.66) | — |
| spacing | `--pad clamp(1.15rem,4.5vw,4.6rem)` (≥18px on the smallest phone), `--gut clamp(1.3rem,3vw,2.6rem)` | — |

Gold is used for: the tape numeral and its rule, the chapter numerals, the `rec` dot on video tiles,
and the focus ring. It is the playhead light of the reel, not a decoration — no gold buttons, no gold
gradient text, no gold hairlines on every edge.

## The text contract

Nothing is rewritten. His sentences are reproduced exactly, including the 7 renovation works, the 3
construction works, the 5 process steps, the about text, the tagline *Ruang dibina dengan rasa*, the
one-team promise, the WhatsApp number `+60 11-1124 4636` and `binahaus.com`.

**Mine, and marked as such:** the chapter numerals (the tape's real sequence — seven pages, one reel),
the room names (*Ruang tamu, Dapur, Butiran, Tapak*), the `REEL 01` tape strip, the `Foto / Render /
Video` kind labels, and two build-note sentences (Dapur, Butiran) that say plainly which tiles are
renders.

**Not on his site, so not on this page:** address, e-mail, company registration, founding year,
service areas, project names or locations. The Profil Syarikat plate prints *belum diterbitkan* for
those, and the contact page says why. **Ask the owner before filling them.**

## Provenance — every local asset

Re-encoding only: resized to a web size, JPEG q84 progressive, metadata stripped. No crop, no retouch,
no colour grade, no generated or stock image. The five heavy videos are **not** copied — the page
plays them from the owner's own URLs.

| local file (in `assets/img/`) | source on the owner's site |
|---|---|
| `about-team.jpg` | `https://binahaus.com/assets/about-team-Cs38AnSZ.jpg` |
| `construction-site.jpg` | `https://binahaus.com/assets/construction-site-NUuTsEpO.jpg` |
| `hero-living.jpg` | `https://binahaus.com/assets/hero-living-Brqy9b4j.jpg` |
| `reno-detail.jpg` | `https://binahaus.com/assets/reno-detail-CTESX31o.jpg` |
| `reno-kitchen.jpg` | `https://binahaus.com/assets/reno-kitchen-BYsCvji1.jpg` |
| `reno-progress.jpg` | `https://binahaus.com/assets/reno-progress-cAki5mYk.jpg` |
| `work-photo-1…8.jpg` | `https://binahaus.com/__l5e/assets-v1/<id>/work-photo-N.jpg` |
| `work-render-1…5.jpg` | `https://binahaus.com/__l5e/assets-v1/<id>/work-render-N.jpg` |
| `work-poster-1…7.jpg` | `https://binahaus.com/__l5e/assets-v1/<id>/work-poster-N.jpg` |
| `work-video-1.mp4`, `work-video-2.mp4` (596 KB, 604 KB) | `https://binahaus.com/__l5e/assets-v1/<id>/work-video-1,2.mp4` |
| `assets/logo/bina-haus-logo{,-320,-160}.png` | `https://binahaus.com/__l5e/assets-v1/9dbffc53-…/bina-haus-logo.png` |

**Streamed live from the owner's own URLs** (≈58 MB, never copied), each verified `206 video/mp4` to a
range request:

| poster | src |
|---|---|
| `work-poster-3.jpg` | `https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4` |
| `work-poster-4.jpg` | `https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4` |
| `work-poster-5.jpg` | `https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4` |
| `work-poster-6.jpg` | `https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4` |
| `work-poster-7.jpg` | `https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4` |

**Fonts** (`assets/fonts/`, self-hosted woff2, no CDN): `bsc-500/600/700-{latin,latin-ext}.woff2` from
Google Fonts *Barlow Semi Condensed*; `news-400{,-latin-ext}` and `news-400i-{latin,latin-ext}` from
Google Fonts *Newsreader*. Both SIL OFL 1.1.

## The seven pages (one shell, `bina.py`)

`index.html` · `perkhidmatan.html` · `kerja.html` · `cara.html` · `tentang.html` · `syarikat.html` ·
`kontak.html`. The header, the menu and the footer are written once in `bina.py`, so they cannot drift.
The header is the mark and the menu only (no WhatsApp button in the bar); the menu panel lists all
seven pages plus one WhatsApp line. See `../README.md` for the page map.

## Gate results (all measured on the built pages, not intentions)

| gate | command | result |
|---|---|---|
| Auteur slopscan | `node slopscan.mjs pita` | **exit 0 — 0 fails, 0 warns, 0 suppressed** |
| Impeccable context | `impeccable context --target pita/index.html` (before code) | `PRODUCT_INIT_REQUIRED` (a new surface) → PRODUCT.md + COMMIT-SHEET written |
| Impeccable detect | `impeccable detect --json pita/index.html pita/assets/style.css pita/assets/app.js` | exit 2 — 5 findings, **all `cramped-padding` false positives**: measured border→first-text gap 80px (`.chap`) and 84px (`.cta__in`); the detector cannot resolve `clamp()` padding |
| Device sweep | Playwright, 360/390/768/1440 × 7 pages (28 runs) | **0 fails** — `innerWidth` read back at every width, 0 horizontal overflow, nothing clipped, exactly one `h1` and first in the DOM, no overlapping text blocks, every image loaded, both webfonts loaded, 0 HTTP ≥ 400 |
| Contrast | every text/ground pair, resolved through a canvas (so `oklch()`/`color-mix()` are measured as sRGB) | lowest **6.17:1** (floor 4.5:1) |
| Touch targets | `elementFromPoint` hit height after `scrollIntoView`, per width | **0 fails** — min hit 45px @390, 45px @768, 46px @1440 (mark, burger, buttons, play tiles, footer rows, menu rows) |
| Perf (index) | LCP / CLS / long-task at 4× CPU throttle | LCP **0.37s** @1440, 0.06s @390; CLS **0.001**; **no long task > 50ms** |
| No-JS | `assets/app.js` aborted on all seven pages | every page **complete**: `h1` present, all six nav links visible at 390px, native video players reachable, nothing left hidden |
| Frames | 28 viewport captures at 390/768/1440, `qa/` | reviewed; media-led chapters, labels correct, no blank frames |
