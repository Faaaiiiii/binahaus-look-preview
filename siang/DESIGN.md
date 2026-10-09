---
version: alpha
name: Bina Haus — Siang
description: The owner's daylight. Beige-soft as the page, navy-deep as the type, one navy band per page, and the gold kept to a single hairline. Libre Franklin labels a day; Spectral reads it.
colors:
  primary: "oklch(97.96% 0.0057 84.57)"
  secondary: "oklch(89.88% 0.0298 80.65)"
  tertiary: "oklch(20.21% 0.034 265.48)"
  accent: "oklch(74.04% 0.0992 86.94)"
  band: "oklch(28.83% 0.0503 265.9)"
  ink-2: "oklch(28.83% 0.0503 265.9)"
  rule: "rgb(194, 194, 195)"
  rule-strong: "rgb(128, 130, 137)"
  placeholder: "rgb(231, 230, 228)"
typography:
  display-1:
    fontFamily: Libre Franklin
    fontSize: 5.3rem
    fontWeight: 600
    lineHeight: 1.02
    letterSpacing: "-0.015em"
  heading-2:
    fontFamily: Libre Franklin
    fontSize: 2.5rem
    fontWeight: 600
    lineHeight: 1.1
  lead:
    fontFamily: Spectral
    fontSize: 1.55rem
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: Spectral
    fontSize: 1.0625rem
    fontWeight: 400
    lineHeight: 1.7
  label:
    fontFamily: Libre Franklin
    fontSize: 0.8rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.08em"
  label-control:
    fontFamily: Libre Franklin
    fontSize: 0.92rem
    fontWeight: 500
    lineHeight: 1.4
  display-2:
    fontFamily: Libre Franklin
    fontSize: 3rem
    fontWeight: 600
    lineHeight: 1.06
  heading-3:
    fontFamily: Libre Franklin
    fontSize: 2.1rem
    fontWeight: 600
    lineHeight: 1.12
  reading:
    fontFamily: Spectral
    fontSize: 1.0625rem
    fontWeight: 400
    lineHeight: 1.7
rounded:
  none: 0px
  pill: 999px
spacing:
  section: 120px
  gutter: 72px
  block: 28px
  row: 16px
  inline: 9px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.none}"
    padding: 13px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
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
    textColor: "{colors.ink-2}"
    height: 48px
  link-band:
    backgroundColor: "{colors.band}"
    textColor: "{colors.primary}"
    height: 48px
  label-section:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
  rule-accent:
    backgroundColor: "{colors.accent}"
    height: 1px
  surface-band:
    backgroundColor: "{colors.band}"
    textColor: "{colors.primary}"
    padding: 48px
  surface-raised:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    padding: 28px
  divider:
    backgroundColor: "{colors.rule}"
    height: 1px
  divider-strong:
    backgroundColor: "{colors.rule-strong}"
    height: 1px
  media-placeholder:
    backgroundColor: "{colors.placeholder}"
    height: 220px
---

## Overview

Daylight on the owner's own paper. Where arah 03 stands the house at dusk and arah 04 keeps it on
sand, this one lets the page go almost white — his `beige-soft` as the ground — and lets the type do
the talking in his `navy-deep`, with exactly one navy band per page and the owner's gold reduced to a
single hairline. Sobriety is the idea: a daylight showroom for the work, not a story about the visit.

## Colors

- **Primary — beige-soft (`oklch(97.96% 0.0057 84.57)`):** the ground. Almost white, warm rather
  than grey, so photographs sit on it without a frame.
- **Secondary — beige (`oklch(89.88% 0.0298 80.65)`):** one tinted editorial band, used once per page.
- **Tertiary — navy-deep (`oklch(20.21% 0.034 265.48)`):** all type that carries weight.
- **Band — navy (`oklch(28.83% 0.0503 265.9)`):** the one full-bleed dark band (the closing statement)
  and the ground the footer sits on. Its text is beige-soft (13.4:1).
- **Accent — gold (`oklch(74.04% 0.0992 86.94)`):** a hairline only. It is never text on this ground;
  at 74% lightness it measures well under 4.5:1 against the page.

## Typography

**Libre Franklin** labels — headings, section numbers, buttons, navigation. **Spectral** reads —
body, lead, captions. A grotesque for the sign, a serif for the report; the pairing is why the
direction reads as a printed daylight page rather than a template.

## Layout

An 82rem measure, a gutter that never falls below 18px, and a section rhythm of 3.2–7.5rem so the
page breathes the way a gallery does. Hairlines, not cards, do the dividing.

## Shapes

Square. Zero radius on every surface. The only circle is a media-control affordance.

## Components

`button-primary` (navy fill) is the single filled action; `button-quiet` is the second path to
WhatsApp. `link-band` is the same link family re-tinted for the navy band — a contrast necessity, not
a new shape. `surface-raised` is the one tinted block; `surface-band` the one dark block.

## Do's and Don'ts

- **Do** keep the owner's copy verbatim and label every photograph by what it is.
- **Do** keep the gold to hairlines; it fails contrast as text on beige-soft.
- **Don't** invent an address, e-mail, registration number, date or statistic.
- **Don't** put a kicker above a heading, use gradient text, or add glass as decoration.
- **Don't** put the owner's logo anywhere without its dark plate: the file carries a white wordmark.
