# DESIGN.md — Bina Haus, arah 05 "SIANG" (daylight)

> The prose contract: why each decision, the full 26-asset provenance table, and the gate results.
> Everything on the page belongs to the owner: the logo is his own PNG file, the colours are read out
> of his stylesheet, the photographs, renders and videos are his, and every sentence of company copy is
> his, verbatim from binahaus.com. Nothing was invented; nothing that belongs to the brand was redrawn.

## The contract

| decision | value | where it comes from |
|---|---|---|
| ground (paper) | `--ground: oklch(97.96% .0057 84.57)` | his stylesheet — beige-soft |
| type + rules | `--ink: oklch(20.21% .034 265.48)` | same — navy-deep |
| secondary type | `--ink-2: oklch(28.83% .0503 265.9)` | same — navy |
| tinted band | `--raised: oklch(89.88% .0298 80.65)` | same — beige |
| the one dark band | `--band: oklch(28.83% .0503 265.9)` | same — navy, home page only |
| the one accent | `--gold: oklch(74.04% .0992 86.94)` | same; the logo's own flat gold measures `#D5A64C`, the same colour |
| hairline | `--rule: color-mix(in oklab, var(--ink) 24%, var(--ground))` | derived from his navy |
| display / furniture face | **Libre Franklin** 400–700 (variable, self-hosted) | Google Fonts / Impallari Type |
| reading face | **Spectral** 400 / 600 (static, self-hosted) | Google Fonts / Production Type |
| logo | `assets/logo/bina-haus-logo{,-320,-160}.png` | his `bina-haus-logo.png`, only the transparent margin trimmed and re-encoded |
| type scale | `--s1` 1.0625rem (body floor) → `--h1` clamp(2.45rem … 5.3rem), 1.25-ish steps | — |
| body measure | ≤ 66ch, `line-height 1.68` | — |
| spacing | `--gut clamp(1.125rem, 5vw, 4.5rem)` (never below 18px), `--pad clamp(3.2rem, 9vw, 7.5rem)` | — |
| theme colour | `#faf8f4` — the measured sRGB of his beige-soft | resolved through a canvas |

Gold is used for: the masthead rule that draws on load, the tag tick after every `FOTO / RENDER / VIDEO`
chip, the menu panel's top edge, the goldline mark on the company plate and inside the dark band, the
closing statement's end-mark, and the focus ring on the dark band. It is never body text on the light
ground — that was measured, not assumed.

## What is his, and what is mine

- **His, verbatim:** the hero tagline and both ledes, `RENOVATION & CONSTRUCTION`, the CTA lines
  (`GET FREE QUOTATION`, `GET FREE QUOTATIONS`, `WHATSAPP US`), the Renovations block and its 7 works,
  the Construction block and its 3 works, the 5 process steps, the Why-choose-us block, the About text,
  the closing statement, the footer, the WhatsApp number `+60 11-1124 4636` and `binahaus.com`.
- **Mine, and marked as such:** the page's own `FOTO / RENDER / VIDEO` chips and the descriptive
  captions under each image; the three chapter words on the home page (*Ruang tamu, Dapur, Tapak*); and
  one build note on Services that says plainly which two tiles are the studio's renders.
- **Not on his site, so not on this page:** address, e-mail, company registration, founding year,
  service areas, project names, statistics, testimonials. The Profil Syarikat plate prints
  **Belum diterbitkan** for those and says why. **Ask the owner before filling them.**
- **Three owner strings are deliberately not used** (checked: 103 of 106 lines of his live copy appear
  in wording, case-insensitively). `KITCHEN RENOVATION — PLACEHOLDER PROJECT` is a stray placeholder on
  his own site; `LOAD MORE` is his gallery pagination, and this page shows all 20 items at once, so a
  "load more" button would be a lie; `KENAPA PILIH KAMI?` is his label over the one-team block, and the
  block is headed here by his own statement for it, *One team. One project. One responsibility.* — a small
  label above a heading is a pattern this direction refuses. Nothing was rewritten; the wording that
  appears is his.
- Navigation, footer and a few section labels are authored in **title case in the markup and set
  uppercase by CSS** (`SERVICES`, `OUR WORK`, `CARA KAMI KERJA`, `ABOUT US`, `CONTACT`, `WHATSAPP US`,
  `GET FREE QUOTATION(S)`, `RENOVATIONS`, `CONSTRUCTION`, `CONTACT`/`NAVIGATION`, `RENOVATION &
  CONSTRUCTION`). The words are his; his own site uppercases them the same way.

## Provenance — every local asset mapped to its source on the owner's site

| local file | served as | size | source | label on page |
|---|---|---|---|---|
| `assets/img/about-team.jpg` | 1400×1050 | 144 KB | https://binahaus.com/assets/about-team-Cs38AnSZ.jpg | Foto |
| `assets/img/construction-site.jpg` | 1600×1000 | 360 KB | https://binahaus.com/assets/construction-site-NUuTsEpO.jpg | Foto |
| `assets/img/hero-living.jpg` | 1800×1200 | 184 KB | https://binahaus.com/assets/hero-living-Brqy9b4j.jpg | Foto |
| `assets/img/reno-detail.jpg` | 1200×900 | 88 KB | https://binahaus.com/assets/reno-detail-CTESX31o.jpg | *(library only)* |
| `assets/img/reno-kitchen.jpg` | 1040×1300 | 126 KB | https://binahaus.com/assets/reno-kitchen-BYsCvji1.jpg | Foto |
| `assets/img/reno-progress.jpg` | 1040×1300 | 117 KB | https://binahaus.com/assets/reno-progress-cAki5mYk.jpg | Foto |
| `assets/img/work-photo-1..8.jpg` | 960×1280 (photo-4 1050×1400) | 88–197 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-photo-N.jpg` | Foto |
| `assets/img/work-render-1..5.jpg` | 960×1280 | 49–139 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-render-N.jpg` | Render |
| `assets/img/work-poster-1..7.jpg` | 296–787 × 640–1400 | 12–95 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-poster-N.jpg` | Video (used as the player poster) |
| `assets/img/work-video-1.mp4` · `-2.mp4` | 606 KB · 616 KB | — | `https://binahaus.com/__l5e/assets-v1/<id>/work-video-1,2.mp4` | Video |
| `assets/logo/bina-haus-logo{,-320,-160}.png` | 600 / 320 / 160 wide | 133 / 43 / 15 KB | `https://binahaus.com/__l5e/assets-v1/9dbffc53-…/bina-haus-logo.png` | — |

Re-encoding only: resized to a sensible web size, metadata stripped. **No crop, no retouch, no colour
grade, no generated imagery, no stock, no hotlinking of stills.**

**The five heavy videos are not copied** (≈58 MB). Their posters are local; each `<video>` carries the
owner's own absolute URL and `preload="none"`, so nothing is fetched until a visitor presses play:

| poster | streams from |
|---|---|
| `work-poster-3.jpg` | https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4 |
| `work-poster-4.jpg` | https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4 |
| `work-poster-5.jpg` | https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4 |
| `work-poster-6.jpg` | https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4 |
| `work-poster-7.jpg` | https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4 |

`reno-detail.jpg` is copied into the library for completeness (the brief lists it) but is not placed on
any of the seven pages — the detail work is shown by the owner's two flooring videos instead.

## The seven pages — one shell, one builder

`bina.py` writes all seven from a single shell, so the header, the menu and the footer cannot drift:

| page | carries |
|---|---|
| `index.html` | the cover (rule + headline + hero plate), three ways in, six tiles of work, the navy band, the CTA |
| `perkhidmatan.html` | the 7 renovation works, the 3 construction works, two feature spreads, 4 video plates |
| `kerja.html` | all 20 own media items, photographs + renders + video, each labelled |
| `cara.html` | the 5 process steps, the team, work in progress |
| `tentang.html` | the About text and the tagline spread |
| `syarikat.html` | every company detail the site publishes, on one plate |
| `kontak.html` | the two ways to start, the published channels, the "not invented" note |

Header = mark + menu only (no WhatsApp button, his instruction). The menu opens as a panel listing all
seven pages plus one WhatsApp line. Mobile: section names and captions sit **under** their photograph,
body type ≥ 1.05rem at `line-height 1.68`, gutters ≥ 18px, the gallery runs two columns, and no text sits
on a photograph anywhere.

## Gate results (final build)

| gate | command | result |
|---|---|---|
| auteur slopscan | `node …/auteur/scripts/slopscan.mjs /Users/fairuzjalil/binahaus-look-preview/siang` | **exit 0 — `Summary: 0 fails, 0 warns, 0 suppressed`** |
| impeccable detect | `impeccable detect --json siang/index.html siang/assets/style.css siang/assets/app.js` | **exit 2 — 6 findings: 5 `cramped-padding` (measured false positives, see below) + 1 `cream-palette` (the owner's pinned `--ground`, consciously accepted)** |
| device sweep | Playwright, 360/390/768/1440 × 7 pages (28 runs) | **0 fails** — `innerWidth` read back equals the requested width on every run, horizontal overflow 0, no clipped scroll container, exactly one `h1` and it is the first heading, no overlapping text blocks, every image loaded, both webfonts loaded, 0 HTTP ≥400, 0 page errors |
| contrast | 1383 text/ground pairs, every `oklch()` resolved through a canvas | lowest **10.53:1** (floor 4.5:1) |
| touch targets | 390px, `elementFromPoint` walk from the centre after `scrollIntoView` | **19/19 in-flow targets ≥ 44px**; menu panel 7 pages + 1 WhatsApp line, every row 48px; the skip link is a 45px control when focused |
| no-JS | `assets/app.js` aborted on all seven pages | every page complete, **all 6 nav links visible**, 0 blocks left hidden, 9 native video players reachable |
| screenshots | 390/768/1440 × 7 pages | 42 frames reviewed |

### The 6 impeccable findings, read one by one

- **5 × `cramped-padding`** — reported at the `<section>`, `.band`, `.cta` and `.wrap` boundaries because
  the detector cannot resolve `var()`/`clamp()` padding and treats a section's own background as the
  container edge. Measured for real in the browser: the gap from the boundary to the first line of text is
  **52px at 390px and 121px at 1440px** for `.section` and `.cta`, **76/157px** for the dark band, and
  **19px** for the footer bar. Every one is far above the 8px the rule asks for. **False positives.**
- **1 × `cream-palette`** — the detector says a warm cream/beige page background is the reflex "tasteful"
  AI surface. True in general; here the background is the owner's own token `oklch(97.96% .0057 84.57)`,
  pinned by the brief. Accepted deliberately, with the reason on the record in `COMMIT-SHEET.md §6`.
