# Bina Haus — look preview

A **static preview of a new look** for [binahaus.com](https://binahaus.com). It is a design
proposal only: a separate repo, no deploy to the live site, no DNS change. The live site is
untouched.

**Direction — "Tapak" (the setting-out board).** A lit drafting board instead of a photo hero:
the house is shown as a hand-authored SVG elevation, the voice is a schedule of works, and the
single accent is the red *setting-out line* a build is set from. Everything is hand-authored
HTML/CSS/SVG — no frameworks, no photographs, no hotlinked assets.

- `index.html` — the whole page
- `assets/style.css` — tokens + layout (see `design/DESIGN.md` for the contract)
- `assets/app.js` — progressive enhancement only; the page is fully readable without JS
- `design/COMMIT-SHEET.md` — the seven decisions taken before any markup
- `design/DESIGN.md` — the style contract
- `qa/` — screenshots at 390 / 768 / 1440

## Content

All copy is the **real copy from binahaus.com** (Malay/English as published), kept verbatim.
The work-gallery tiles are schematic drawings, labelled as such on the page — no photographs were
used, invented or hotlinked.

## Gates

| Gate | Command | Result |
|---|---|---|
| Auteur slopscan | `node slopscan.mjs .` | exit 0 — 0 fails, 0 warns |
| Impeccable detect | `impeccable detect --json index.html assets/style.css assets/app.js` | exit 2 — 27 residual `cramped-padding` heuristic hits on the hairline-rule schedules (reviewed; not real defects) |
| Overflow probe | Playwright, 320 → 1920 px | 0 horizontal overflow at every width |
| Console errors | Playwright | 0 |

---

# Preview 02 — “Satu Tangan” (reka & bina)

`db/` — the second look, built on the same copy and the same repo, deliberately the opposite
argument to *Tapak*. Where Tapak shows a **drafting board** (the design act, told as a schedule of
works), Satu Tangan shows the **design act and the build act as one thing** — so a visitor reads one
author, deciding and making.

**Direction.** One drawing, two states: a joinery bay whose left half is the *design* (dimension
lines, a material callout with its reason) and whose right half is the *built* (the same geometry
with timber grain, wall hatch, site notes). One continuous cobalt **garis kerja** — the chalk line a
maker marks and follows — runs the whole width, thin and dashed while it is still a drawing, heavier
and solid once it has been built, with a single node and the label `reka → bina` where it crosses.

**How it differs from Tapak**

- Argument: Tapak = *the design act only*; Satu Tangan = *design and build joined by one line*.
- Palette: Tapak's lit drafting board with a red setting-out line → here a **plaster-white field with
  teak as a material band**, accent = a **cobalt chalk line used exactly once**.
- Type axis inverted: Tapak's condensed-grotesque display × humanist serif → here
  **Literata (optical-size display serif) × Hanken Grotesk**.
- The work gallery is real: photos, renders and videos from binahaus.com, labelled by kind.

**Gates**

| Gate | Command | Result |
|---|---|---|
| Auteur slopscan | `node slopscan.mjs db` | exit 0 — 0 fails, 0 warns |
| Impeccable detect | `impeccable detect --json db/index.html db/assets/style.css db/assets/app.js` | exit 2 — 27 `cramped-padding` warnings, all reviewed and measured as false positives (the detector cannot resolve `clamp()` padding; the only 0-inset shape is `.thesis`, a grid wrapper with no fill or border) |
| Contrast | Playwright, 46 sampled elements | PASS — lowest 5.08:1 |
| Overflow | Playwright, 320 → 1920 px | 0 horizontal overflow |
| No-JS | JS disabled | complete: cobalt line drawn, register rows visible, native video controls |
| Console errors | Playwright | 0 |
| Device sweep | Playwright, 360/375/390/412/768/834/1024/1280/1440 | 0 fails — no horizontal overflow, no clipped scroll container, exactly one `h1` and first in the DOM, no overlapping text blocks, 20/20 images and the fonts loaded, 0 HTTP errors. `innerWidth` read back at every width (a sweep that does not read the width back is not a sweep) |
| Tap targets | measured by `elementFromPoint` hit height, not by bounding box | wordmark 46–52px, nav links 53px, footer link rows 28px — was 30–36 / 37 / 22. Extended out of flow, so page height is identical at 390/768/1440 (shift 0) |

- `db/index.html` · `db/assets/style.css` · `db/assets/app.js`
- `db/design/COMMIT-SHEET.md` — the seven decisions · `db/design/DESIGN.md` — the style contract
- `db/qa/` — full-page captures at 390 / 768 / 1440

---

# Preview 03 — “MASUK” (the threshold)

`rumah/` — the third look, and the one that answers the brief *“bila buka website, seperti berada
dalam sebuah design rumah”*: opening the page **is** the act of entering the house.

**Direction.** Two panels part over the photograph of the finished living room and the owner's logo
sits behind them as a lit sign — which is what his logo file actually is (a warm-glow mark on
transparency, drawn for a dark ground). Behind the door, the page is a walk through one home:
*Ruang tamu → Dapur → Butiran → Tapak → Pasukan*, each chapter a full-bleed photograph of the real
work with the room name and a `Foto / Render / Video` chip on it, then the owner's own words.

**The branding is literal, not a mood.** Everything that carries the brand is the owner's:

- logo — his own PNG, unchanged (only the transparent margin trimmed); used as the hero sign, the
  header mark, the footer mark and the favicon
- palette — the five tokens read straight out of his stylesheet: navy-deep, navy, beige, beige-soft,
  and the brand gold (`oklch(74.04% .0992 86.94)`, which measures `#D5A64C` in the logo file too)
- type — **Archivo** + **Manrope**, the pair his own site loads, self-hosted here (no CDN)
- copy — every sentence verbatim from binahaus.com, plus a **Profil Syarikat** plate that prints
  every company detail his site publishes (name, field, the 7 renovation works, the 3 construction
  works, the 5 process steps, the one-team promise, WhatsApp +60 11-1124 4636, binahaus.com)
- media — 26 of his own images and videos, provenance listed in `rumah/design/DESIGN.md`

**What this preview does not do:** it invents nothing. His site publishes no address, e-mail,
registration number, founding year or project names, so the plate prints *belum diterbitkan* on that
row and says why. **Tell me the real values and they go in.**

**Gates**

| Gate | Command | Result |
|---|---|---|
| Auteur slopscan | `node slopscan.mjs rumah` | exit 0 — 0 fails, 0 warns |
| Impeccable detect | `impeccable detect --json rumah/index.html rumah/assets/style.css rumah/assets/app.js` | exit 2 — 39 `cramped-padding` warnings, **all measured as false positives**: over 53 flagged shapes the smallest real inset between a border and its text is 16 px, and 20 of the shapes have no border and no fill to inset from |
| Device sweep | Playwright, 360/375/390/412/768/834/1024/1280/1440 | 0 fails — `innerWidth` read back at every width, no horizontal overflow, nothing clipped, exactly one `h1` and first in the DOM, no overlapping text blocks, 39/39 images loaded, both webfonts loaded, 0 HTTP errors |
| Contrast | every text/ground pair over a solid ground, resolved through a canvas (so `oklch()` is measured as sRGB) | 20–21 pairs per width, **lowest 6.32:1** (floor 4.5:1) |
| No-JS | `assets/app.js` blocked | complete: door opens by CSS alone, all five nav links visible at every width, 9 native video players reachable, nothing hidden |
| Live | `curl` page + CSS + JS + fonts + logo + media | 200 across the board |

- `rumah/index.html` · `rumah/assets/style.css` · `rumah/assets/app.js`
- `rumah/design/COMMIT-SHEET.md` — the seven decisions · `rumah/design/DESIGN.md` — the contract and
  the full image provenance table
