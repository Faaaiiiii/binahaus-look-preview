---
version: alpha
name: Bina Haus — Rumah
description: A house at dusk, lit from inside. The owner's navy as the ground, his gold as the single lit line, his own photographs and words carrying the work.
colors:
  primary: "oklch(20.21% 0.034 265.48)"
  secondary: "oklch(28.83% 0.0503 265.9)"
  tertiary: "oklch(74.04% 0.0992 86.94)"
  neutral: "oklch(97.96% 0.0057 84.57)"
  muted: "oklch(89.88% 0.0298 80.65)"
  body-text: "oklch(78% 0.02 80)"
typography:
  display-1:
    fontFamily: Archivo
    fontSize: 4.6rem
    fontWeight: 600
    lineHeight: 1.06
    letterSpacing: "-0.01em"
  display-2:
    fontFamily: Archivo
    fontSize: 2.9rem
    fontWeight: 600
    lineHeight: 1.14
    letterSpacing: "-0.01em"
  heading-3:
    fontFamily: Archivo
    fontSize: 1.75rem
    fontWeight: 600
    lineHeight: 1.2
  body-md:
    fontFamily: Manrope
    fontSize: 1.19rem
    fontWeight: 400
    lineHeight: 1.62
  body-sm:
    fontFamily: Manrope
    fontSize: 0.875rem
    fontWeight: 400
    lineHeight: 1.55
  label-caps:
    fontFamily: Archivo
    fontSize: 0.8rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.16em"
  nav-link:
    fontFamily: Manrope
    fontSize: 0.92rem
    fontWeight: 500
    lineHeight: 1.6
rounded:
  none: 0px
  pill: 999px
spacing:
  section: 72px
  gutter: 56px
  block: 24px
  row: 16px
  inline: 8px
components:
  button-primary:
    backgroundColor: "{colors.neutral}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 44px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 44px
  button-quiet:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 44px
  link-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted}"
    height: 44px
  link-nav-current:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    height: 44px
  link-menu-row:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    height: 48px
  chip-kind:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    padding: 4px
  copy-body:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.body-text}"
    padding: 0px
  surface-plaque:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.neutral}"
    padding: 24px
  callout-note:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    padding: 16px
  play-affordance:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.neutral}"
    rounded: "{rounded.pill}"
    size: 56px
---

## Overview

This is the owner's own world, read out of his own material. Bina Haus is a renovation and
construction company; his website, his logo file and his stylesheet supplied every colour, every
typeface and every photograph on the seven pages. The look is a house at dusk: a deep navy ground,
warm light falling on it, and one gold line that means the work — the chalk line a maker marks and
follows.

Nothing here is a mood board. `navy`, `beige`, `beige-soft` and `gold` are the five colours declared
in the owner's own `styles-BIzBvBjK.css`; `gold` measures `#D5A64C` in the owner's logo file as well,
from two independent sources. When this spec and a screenshot disagree, the screenshot is wrong.

This file is the normative token spec. The seven decisions behind the look are in
`design/COMMIT-SHEET.md`; the prose contract, the provenance table for all 26 of the owner's media
files, and the gate results are in `design/DESIGN.md`.

## Colors

- **Primary — navy-deep (`oklch(20.21% 0.034 265.48)`):** the ground of every page, header, chapter
  and footer, and the colour of the two door panels in the opening animation.
- **Secondary — navy (`oklch(28.83% 0.0503 265.9)`):** raised surfaces only — the company plate, the
  closing call-to-action band, the ground behind media tiles.
- **Tertiary — gold (`oklch(74.04% 0.0992 86.94)`):** the one accent. The door's seam, the threshold
  rule, the process numerals, the plate's rule, the focus ring. It is the lit line, not a decoration:
  no gold buttons, no gold gradient text, no gold hairline on every edge.
- **Neutral — beige-soft (`oklch(97.96% 0.0057 84.57)`):** headings and any type that must carry weight.
- **Muted — beige (`oklch(89.88% 0.0298 80.65)`):** secondary type, captions, chips.
- **Body text:** paragraphs sit on `navy-deep` at a warm tint of beige (78% beige mixed with the
  ground), measured at ≥6.3:1.

## Typography

**Archivo** (display) and **Manrope** (text) — the exact pair the owner's own site loads from Google
Fonts, self-hosted here as woff2 so no third-party request is made at runtime.

- `display-1` is the door headline and each page's own `h1`, at most 14ch wide so it breaks like the
  owner's own hero.
- `display-2` carries the chapter's thesis — a sentence from the owner's copy, never a slogan of ours.
- `body-md` is the reading size; prose is held to 68ch.
- `label-caps` survives in exactly two places (the company plate's field names and the footer column
  labels). Everywhere else labels are sentence case: a tracked-caps label above a heading is banned
  outright.

## Layout

Twelve columns' worth of intent, one measure: `--wrap` 1180px with a page pad that clamps from 20px on
a phone to 72px on a desktop, and a gutter that clamps from 24px to 56px. Chapters are full-bleed
photographs against a hairline; the text column never sits on a photograph without a measured scrim.
On a phone the room name and its chip move **under** the photograph, the gutter tightens to 18px, the
gallery runs two columns and the hero shortens to 88svh.

## Shapes

Square. Buttons, chips, plates and media tiles all have **no** corner radius; hairlines do the work
that a shadow or a rounding would usually do. The single exception is the video play affordance,
which is a 56px circle so it cannot be mistaken for a surface. Scrollbars and focus rings follow the
palette rather than the browser default.

## Components

`button-primary` is the only filled action on a page (Get free Quotation / Get free Quotations).
`button-quiet` is the second path and never competes — it is outlined, and it always points at
WhatsApp, which is the only contact channel the owner publishes. `chip-kind` labels each piece of
media by what it is (`Foto`, `Render`, `Video`); it is a claim about provenance, so it is never
dropped. `link-menu-row` is the phone menu: every page as a 48px row. `callout-note` marks the one
honest gap on the company plate — the fields the owner has not published.

## Do's and Don'ts

- **Do** keep the owner's copy verbatim, including the WhatsApp number and the tagline.
- **Do** label every image by what it is. The library holds photographs, 3D renders and
  work-in-progress; never let one pass as another.
- **Do** measure touch targets by hit-testing: a link in prose needs to be `inline-block`, a list link
  a block, or its padding will not be reachable by a thumb.
- **Don't** invent an address, an e-mail, a registration number, a project name, a statistic or a
  testimonial. The plate prints *belum diterbitkan* and says why.
- **Don't** put a tracked-caps label above a heading, use gradient text, or add glass and blur as
  decoration.
- **Don't** replace the logo. It is the owner's own file; only its transparent margin may be trimmed.
