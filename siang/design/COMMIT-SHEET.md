# COMMIT-SHEET — Bina Haus, arah 05 "SIANG" (daylight)

> Seven decisions taken before the first line of markup. Nothing here is a default.
> Built on the owner's own assets: logo (unchanged), palette (read from his stylesheet),
> typefaces (self-hosted, chosen for this direction), his photographs, renders and video,
> and his copy, verbatim from binahaus.com.

## 1. Peak / signature — the printed spread opening in daylight

The whole direction is the brand read in **daylight** instead of dusk (arah 03 "MASUK" owns
dusk; arah 01 the drafting board; arah 02 the plaster-white workshop drawing). The one authored
moment is the **spread assembling**: a single gold hairline **draws across the full page width**
once on load — the printed rule of a magazine masthead — and the hero photograph **settles** into
place (`scale(1.035)→1`, opacity `.84→1`, 1.25s, `cubic-bezier(.22,.61,.36,1)`), the way an image
comes up in daylight. The headline rises 12px and fades. Nothing else happens on load. Gone in
`prefers-reduced-motion`, which receives the finished state, not a disabled one.

There is no door, no curtain, no full-screen takeover: this direction is quiet on purpose, because
arah 03 already owns the loud entrance.

## 2. Colour — the brand's own five, read out of his stylesheet

| token | value (his) | job |
|---|---|---|
| `--ground` | `oklch(97.96% .0057 84.57)` | beige-soft — the page, the paper |
| `--ink` | `oklch(20.21% .034 265.48)` | navy-deep — all type and rules |
| `--ink-2` | `oklch(28.83% .0503 265.9)` | navy — secondary type (captions, meta, numerals) |
| `--raised` | `oklch(89.88% .0298 80.65)` | beige — a tinted editorial band (two per site, plus the CTA) |
| `--band` | `oklch(28.83% .0503 265.9)` | navy — **the one full-bleed dark band**, on the home page only |
| `--gold` | `oklch(74.04% .0992 86.94)` | **the one accent**, hairlines and marks only, < 0.5% of pixels |

The ground is his beige-soft and the type his navy-deep — a light warm paper with cool navy ink,
which is exactly how a printed feature reads in daylight. **Gold is never text on the light
ground** (it measures ~2:1 there); it is a hairline, the tag tick, the panel's top edge, the
focus ring on the navy band, and the numerals' neighbour. Refused: terracotta, rounded corners,
gradient text, shadows, cards.

## 3. Type — a real, non-reflex pair, self-hosted

- **Libre Franklin** — the news grotesque (Franklin Gothic lineage, by Pablo Impallari / Frere-Jones's
  revival). Headlines, navigation, captions, numerals, buttons. Source: **Google Fonts**
  (`css2?family=Libre+Franklin`), served as one variable woff2 per subset, shipped in `assets/fonts/`.
- **Spectral** — the screen-reading serif (Production Type). Body copy, standfirsts, pull-quotes.
  Source: **Google Fonts** (`css2?family=Spectral:wght@400;600`), static woff2, shipped in `assets/fonts/`.

Why this pair: a printed feature is a **grotesque headline over a serif reading column** — the axis
of the whole magazine tradition — and it is the **opposite axis to arah 02** (serif display × grotesque
text) and a **different class of grotesque to arah 01** (condensed display). Archivo and Manrope are
arah 03's and are not used. Inter, Playfair Display, Instrument Serif and Fraunces are refused by rule.

12 files fetched, 6 kept (Spectral 400 + 600, Libre Franklin variable 400-range, latin + latin-ext).
No CDN: `assets/fonts/` only, `@font-face` relative to the stylesheet. **Spectral 600 lazy-loads on
the five pages that do not set it** — that is correct, not a missing font (verified: it loads and
measures on `index.html` and `tentang.html`, the only two pages that use it).

## 4. Grid break

The measure is a narrow reading column (≤66ch) while the **page furniture runs the full width**: the
masthead rule spans the whole spread, and photographs break **full-bleed past the text column** on the
cover and inside the asymmetric feature spreads (`1fr : 1.5fr`, mirrored for the construction spread).
Captions never sit on a photograph — they sit under it, on a hairline, in the reading serif. There are
no cards anywhere; structure is carried by **hairline rules** (`--ink` at 24% over the ground) and by
the tinted beige bands.

## 5. Motion budget — two families, not three

1. **The spread assembling** — the masthead rule drawing + the hero settling. Once, on `index.html` only.
2. **Rules and figures settling on scroll** — `opacity` + `translateY(12px)`, one shared timing, gated on
   `html.js` so a browser with JavaScript blocked never hides a word.

Nothing else. `prefers-reduced-motion` gets the finished state. There is no scroll-jacking, no pinning,
no parallax.

## 6. Reflex check

- **(a) The generic AI "premium renovation" page:** black ground, gold everywhere, a luxury serif,
  three identical service cards, an eyebrow above every heading, a hero-metric strip, gradient text.
- **(b) What a generic AI avoiding (a) does:** the light warm-artisan page — cream, terracotta,
  rounded corners, big friendly type, a kicker above each section.
- **This page:** the owner's own paper (beige-soft) and his own ink (navy-deep), his gold used only as
  a hairline, real photographs given room, **no cards, no shadows, no gradient text, and no eyebrow
  above any heading** (an absolute ban), and the section numbers are only the owner's own (01–07 works,
  01–03 construction, 01–05 process). The colour story is *his tokens*, not a mood board.
- **Consciously accepted, named:** the impeccable detector flags the background as `cream-palette`.
  That is the owner's pinned `--ground` token — the brief fixes it — and the reflex it warns about is
  the terracotta/rounded/friendly-cream page, which this is not. Left in, on the record.

## 7. Honesty rules

- **Nothing is invented.** No address, e-mail, registration number, founding year, service area, project
  name, statistic, testimonial or date. Fields the owner has not published print **belum diterbitkan**
  with a footnote saying why. Ask him for the real values.
- **Every image is labelled by what it is** — `Foto` (photograph), `Render` (3D render), `Video` (his own
  video, poster labelled Video). The only render/photo claim on the page is a note that says plainly the
  two kitchen tiles are the studio's renders, not photographs of a finished site.
- The chapter words that are mine (Ruang tamu, Dapur, Tapak, and the caption descriptions) are **added
  labels**, never a rewrite of his copy, and I say so in `DESIGN.md`.
- The header carries the **mark and the menu only** — no WhatsApp button in the bar (his instruction).
  WhatsApp lives on the cover, in the menu panel, on Contact and in the footer.

---

## v2 — after the inspection round

Five things were found by looking and measuring, and each changed the build:

1. **The printed rule stopped at the text column.** It read as a stray line beside the headline.
   It now spans the whole spread (`grid-column: 1 / -1`).
2. **Inner pages left half the width dead** under the h1. The page band is now two columns — h1 left,
   standfirst right, baselines aligned.
3. **The footer was beige and sat directly under the beige CTA band** — one merged slab. The footer went
   back to the page ground with a stronger hairline, so the page ends on three distinct tonal steps:
   navy band → beige CTA → light footer.
4. **Two duplicated headings.** `cara.html` repeated "A clear process from start to finish" (standfirst
   and h2) and `tentang.html` repeated both its standfirst and the first sentence of its tagline
   paragraph. Both were split so every heading says something the line under it does not.
5. **Footer links were inline runs, not rows** — a measured 27px hit box. They became real rows
   (`display:inline-flex`, `min-height:44px`), and the probe now reports 19/19 phone targets ≥44px.
