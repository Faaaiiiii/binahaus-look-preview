---
version: alpha
name: Bina Haus — Jurnal Tapak
description: Daylight on the owner's sand. Five steps as the spine, his own photographs hanging off them, each labelled by what it actually shows.
colors:
  primary: "oklch(89.88% 0.0298 80.65)"
  secondary: "oklch(97.96% 0.0057 84.57)"
  tertiary: "oklch(20.21% 0.034 265.48)"
  accent: "oklch(74.04% 0.0992 86.94)"
  accent-ink: "oklch(48.2% 0.03 84)"
  surface-deep: "oklch(28.83% 0.0503 265.9)"
  muted-ink: "oklch(38% 0.035 265)"
typography:
  display-1:
    fontFamily: Schibsted Grotesk
    fontSize: 2.7rem
    fontWeight: 600
    lineHeight: 1.1
    letterSpacing: "-0.008em"
  display-2:
    fontFamily: Schibsted Grotesk
    fontSize: 2.7rem
    fontWeight: 600
    lineHeight: 1.1
  heading-2:
    fontFamily: Schibsted Grotesk
    fontSize: 1.7rem
    fontWeight: 600
    lineHeight: 1.15
  body-md:
    fontFamily: Source Sans 3
    fontSize: 1.2rem
    fontWeight: 400
    lineHeight: 1.6
  body-sm:
    fontFamily: Source Sans 3
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: Schibsted Grotesk
    fontSize: 0.875rem
    fontWeight: 600
    lineHeight: 1.4
  numeral:
    fontFamily: Schibsted Grotesk
    fontSize: 1.2rem
    fontWeight: 700
    lineHeight: 1.2
rounded:
  none: 0px
  pill: 999px
spacing:
  section: 64px
  gutter: 56px
  block: 24px
  row: 16px
  inline: 9px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 46px
  button-primary-hover:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 46px
  button-quiet:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.none}"
    padding: 12px
    height: 46px
  link-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted-ink}"
    height: 44px
  link-nav-current:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
    height: 44px
  link-menu-row:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.muted-ink}"
    height: 52px
  link-footer-row:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.muted-ink}"
    height: 52px
  link-inline:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.tertiary}"
  rule-accent:
    backgroundColor: "{colors.accent}"
    height: 2px
  numeral-rail:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-ink}"
  numeral-phase:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.accent-ink}"
  chip-kind:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.surface-deep}"
    padding: 4px
  surface-plaque:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.tertiary}"
    padding: 24px
  band-dark:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.secondary}"
    padding: 40px
  play-affordance:
    backgroundColor: "{colors.surface-deep}"
    textColor: "{colors.secondary}"
    rounded: "{rounded.pill}"
    size: 56px
---

## Overview

The daylight reading of the same brand. Where arah 03 stands the house at dusk, this one puts it on
the owner's own **sand** — `beige` at `oklch(89.88% 0.0298 80.65)` — with his `navy-deep` as ink and
his `gold` kept for the one thing that moves: where the work has reached.

The structure is his own, not mine: the five steps he publishes (consultation, site visit,
quotations, construction, handover) are the spine of the site, and his own photographs hang off that
spine, each labelled by what it actually shows — `Proses`, `Siap`, `Render`, `Video`. The pages are a
build diary, not a brochure: nothing is dated, no photograph is claimed to be part of one project,
and the note under the diary says so in plain words.

## Colors

- **Primary — sand (`oklch(89.88% 0.0298 80.65)`):** the ground of every page. Warm, light, and warm
  enough that a photograph sits on it without a frame.
- **Secondary — paper (`oklch(97.96% 0.0057 84.57)`):** raised surfaces (the company plate), and the
  ground of the phone menu.
- **Tertiary — ink (`oklch(20.21% 0.034 265.48)`):** all type that carries weight, and the fill of
  the primary button.
- **Accent — gold (`oklch(74.04% 0.0992 86.94)`):** decoration only — the rule under the kicker, the
  current-page underline, the segment that marks progress. **It is never used as text on sand.**
- **Accent as ink (`oklch(48.2% 0.03 84)`):** the same hue darkened until it passes 4.5:1 on sand
  (measured 4.79:1). Numerals — the five steps, the five phases — use this, not the decorative gold.
- **Surface deep (`oklch(28.83% 0.0503 265.9)`):** exactly one dark band per page (the closing
  call-to-action) and the small plate the owner's logo sits on.

## Typography

**Schibsted Grotesk** (display, labels, numerals — 600/700) and **Source Sans 3** (body — 400/600),
both self-hosted as woff2. Neither is Archivo nor Manrope, which arah 03 owns; neither is on the
overused-face list.

- `display-1` is the page's own `h1`; the home page carries the owner's own hero sentence, set at
  2.7rem so a twelve-word sentence does not become five stacked lines.
- `numeral` marks the five steps and the five phases — the only place the gold family appears as
  text.
- Body measure stops at 66ch; the diary's own honesty note stops at 76ch.

## Layout

A 1200px measure with a pad that clamps from 18px (phone) to 72px (desktop) and a gutter from 24px to
56px. Hairlines do all the dividing: every section is closed by a 1px rule, never by a shadow or a
card. On the home page the hero is **split** — the owner's words on the sand at the left, one of his
own photographs full-height at the right — and on a phone the photograph moves below the words.

## Shapes

Square. Every button, chip, plate and tile has no corner radius. The only circle in the system is the
56px video play affordance, which must not be mistaken for a surface.

## Components

`button-primary` is the single filled action; `button-quiet` is the second path and always points at
WhatsApp, the only contact channel the company publishes. `chip-kind` is the provenance chip: it says
`Proses`, `Siap`, `Render` or `Video`, and it is never dropped, because a work-in-progress photograph
passed off as a finished room would be a lie. `numeral-rail` and `numeral-phase` carry the five steps.
`band-dark` is the one dark moment per page.

## Do's and Don'ts

- **Do** keep the owner's copy verbatim; the site's own words are the diary's voice.
- **Do** label every image by what it is, and keep the note that says the photographs are not one
  project.
- **Do** use `accent-ink` for any accent text on sand; the decorative gold fails contrast there.
- **Don't** invent a date, an address, an e-mail, a registration number, a project name or a
  statistic. The company plate prints *belum diterbitkan* where the owner has published nothing.
- **Don't** put a kicker above a heading, use gradient text, or add glass and blur as decoration.
- **Don't** reproduce the owner's logo anywhere except on its own dark plate: the file is drawn with
  a white wordmark for a dark ground, and on sand it washes out.
