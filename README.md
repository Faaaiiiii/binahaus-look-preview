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
