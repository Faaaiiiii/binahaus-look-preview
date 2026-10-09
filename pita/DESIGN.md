---
version: alpha
name: Bina Haus — Pita
description: The owner's navy as the ground, his photographs as the plates, and a thin beige ribbon doing every job a border would do. Barlow Semi Condensed labels; Newsreader reads.
colors:
  primary: "oklch(28.83% 0.0503 265.9)"
  secondary: "oklch(20.21% 0.034 265.48)"
  tertiary: "oklch(89.88% 0.0298 80.65)"
  accent: "oklch(74.04% 0.0992 86.94)"
  paper: "oklch(97.96% 0.0057 84.57)"
  ink-2: "rgb(200, 192, 179)"
  inset: "rgb(26, 35, 57)"
  scrim-deep: "#05070c"
typography:
  display-1:
    fontFamily: Barlow Semi Condensed
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-0.01em"
  heading-2:
    fontFamily: Barlow Semi Condensed
    fontSize: 1.95rem
    fontWeight: 600
    lineHeight: 1.12
  body:
    fontFamily: Newsreader
    fontSize: 1.24rem
    fontWeight: 400
    lineHeight: 1.62
  label:
    fontFamily: Barlow Semi Condensed
    fontSize: 0.82rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.09em"
  label-micro:
    fontFamily: Barlow Semi Condensed
    fontSize: 0.72rem
    fontWeight: 600
    lineHeight: 1.4
  reading-sm:
    fontFamily: Newsreader
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.6
  display-2:
    fontFamily: Barlow Semi Condensed
    fontSize: 2.4rem
    fontWeight: 600
    lineHeight: 1.08
  numeral:
    fontFamily: Barlow Semi Condensed
    fontSize: 0.82rem
    fontWeight: 700
    lineHeight: 1.2
  label-nav:
    fontFamily: Barlow Semi Condensed
    fontSize: 0.82rem
    fontWeight: 500
    lineHeight: 1.4
rounded:
  none: 0px
  pill: 999px
  chrome: 6px
spacing:
  section: 96px
  gutter: 42px
  block: 28px
  row: 16px
  inline: 10px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.none}"
    padding: 13px
    height: 48px
  button-quiet:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.none}"
    padding: 13px
    height: 48px
  link-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    height: 48px
  link-band:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    height: 48px
  ribbon:
    backgroundColor: "{colors.accent}"
    height: 2px
  chip-kind:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    padding: 4px
  surface-inset:
    backgroundColor: "{colors.inset}"
    textColor: "{colors.tertiary}"
    padding: 28px
  surface-paper:
    backgroundColor: "{colors.paper}"
    textColor: "{colors.secondary}"
    padding: 28px
  play-affordance:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.pill}"
    size: 56px
  surface-scrim:
    backgroundColor: "{colors.scrim-deep}"
    textColor: "{colors.tertiary}"
    padding: 28px
  link-channel:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-2}"
    height: 48px
  link-quiet:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-2}"
    height: 48px
---

## Overview

The house at night, printed. The owner's own **navy** becomes the page itself — every page is a dark
sheet — and the photographs are hung on it as plates, full-bleed, with the warm beige doing the work a
border would normally do: a thin **ribbon** above every section, under every label, around the
numbered steps. It is the direction where the work is the only bright thing on the page.

## Colors

- **Primary — navy (`oklch(28.83% 0.0503 265.9)`):** the ground of every page.
- **Secondary — navy-deep (`oklch(20.21% 0.034 265.48)`):** the inset panels and the scrim the type
  sits on over a photograph. Same hue family as the ground, so a panel reads as a recess rather than a
  card.
- **Tertiary — beige (`oklch(89.88% 0.0298 80.65)`):** type on the navy ground and the fill of the
  primary button. Contrast on navy: 11.6:1.
- **Paper — beige-soft (`oklch(97.96% 0.0057 84.57)`):** the one light block, used where a page needs
  a breath of daylight (the company plate).
- **Accent — gold (`oklch(74.04% 0.0992 86.94)`):** the ribbon, and nothing else.

## Typography

**Barlow Semi Condensed** for everything that names or numbers — the condensed cut keeps long
Malaysian and English labels on one line inside narrow columns, and it gives the section numerals
their cool, signage-like tone. **Newsreader** for the reading text: a serif on a navy ground reads as
print, which is what this direction wants.

## Layout

A 1200px measure with a pad that never falls below 18px and a gutter of 26–42px. Sections are numbered
`01`, `02`, `03` — a visible order, the way a fabricator numbers a drawing set. Photographs are given
the full measure wherever they can carry it.

## Shapes

Square. The ribbon is 2px and always straight; the only circle in the system is the play affordance
on a video plate. When type must sit on a photograph it sits on a scrim tinted from the ground's own
hue — never on the bare image.

## Components

`button-primary` is beige on navy — the brightest thing on the page, and the only one.
`button-quiet` is the second path to WhatsApp. `chip-kind` says what each plate really is
(`Proses`, `Siap`, `Render`, `Video`) and is never dropped. `surface-inset` and `surface-paper` are the
two panels. `ribbon` marks every section change.

## Do's and Don'ts

- **Do** keep the type on photographs on a navy-tinted scrim; a bare light photograph will not carry
  beige type.
- **Do** keep every sentence and every figure the owner's own.
- **Don't** invent an address, e-mail, registration number, date, project name or statistic.
- **Don't** put the owner's logo anywhere except on its own dark plate (the file carries a white
  wordmark).
- **Don't** use the gold as body text; it is the ribbon's colour.
