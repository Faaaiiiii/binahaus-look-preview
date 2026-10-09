---
version: alpha
name: Bina Haus — Serambi
description: The warmest reading of the brand. The owner's beige-soft as the page, his navy-deep warmed into a near-black ink, his gold kept for lines and marks, and soft radii with three-layer shadows so the surface feels residential rather than technical.
colors:
  primary: "#faf8f4"
  secondary: "#e8dcc8"
  tertiary: "#0f1626"
  accent: "#c6a75e"
  ink: "rgb(36, 42, 56)"
  ink-secondary: "#665c4a"
  hairline: "rgb(218, 217, 217)"
  hairline-strong: "rgb(191, 192, 194)"
  border-quiet: "rgb(198, 198, 199)"
typography:
  display-1:
    fontFamily: Petrona
    fontSize: 2.9rem
    fontWeight: 600
    lineHeight: 1.08
    letterSpacing: "-0.02em"
  display-2:
    fontFamily: Petrona
    fontSize: 2.3rem
    fontWeight: 600
    lineHeight: 1.12
    letterSpacing: "-0.015em"
  room-name:
    fontFamily: Petrona
    fontSize: 2.9rem
    fontWeight: 600
    lineHeight: 1.06
  heading-3:
    fontFamily: Petrona
    fontSize: 1.5rem
    fontWeight: 600
    lineHeight: 1.2
  lead:
    fontFamily: DM Sans
    fontSize: 1.5rem
    fontWeight: 400
    lineHeight: 1.5
  body:
    fontFamily: DM Sans
    fontSize: 1.18rem
    fontWeight: 400
    lineHeight: 1.62
  body-small:
    fontFamily: DM Sans
    fontSize: 1rem
    fontWeight: 400
    lineHeight: 1.55
  label:
    fontFamily: DM Sans
    fontSize: 0.86rem
    fontWeight: 600
    lineHeight: 1.4
  label-micro:
    fontFamily: DM Sans
    fontSize: 0.78rem
    fontWeight: 600
    lineHeight: 1.4
    letterSpacing: "0.12em"
  label-door:
    fontFamily: DM Sans
    fontSize: 1.12rem
    fontWeight: 600
    lineHeight: 1.24
  menu-row:
    fontFamily: DM Sans
    fontSize: 2rem
    fontWeight: 600
    lineHeight: 1.15
rounded:
  line: 1px
  hairline: 2px
  chip: 4px
  button: 8px
  tile: 14px
  plate: 10px
  block: 22px
  pill: 999px
spacing:
  section: 70px
  gutter: 42px
  block: 26px
  row: 14px
  inline: 9px
components:
  button-primary:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.button}"
    padding: 13px
    height: 48px
  button-primary-hover:
    backgroundColor: "{colors.accent}"
    textColor: "{colors.tertiary}"
    rounded: "{rounded.button}"
    padding: 13px
    height: 48px
  button-quiet:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
    padding: 13px
    height: 48px
  button-on-dark:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.button}"
    padding: 13px
    height: 48px
  button-quiet-on-dark:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.button}"
    padding: 13px
    height: 48px
  link-nav:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink-secondary}"
    height: 48px
  link-menu-row:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    height: 62px
  card-door:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.block}"
    padding: 11px
  tile-frame:
    backgroundColor: "{colors.secondary}"
    rounded: "{rounded.tile}"
    height: 214px
  chip-kind:
    backgroundColor: "{colors.secondary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.pill}"
    padding: 4px
  surface-plate:
    backgroundColor: "{colors.primary}"
    textColor: "{colors.ink}"
    rounded: "{rounded.plate}"
    padding: 26px
  band-dark:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.block}"
    padding: 44px
  play-affordance:
    backgroundColor: "{colors.tertiary}"
    textColor: "{colors.primary}"
    rounded: "{rounded.pill}"
    size: 58px
  floor-line:
    backgroundColor: "{colors.accent}"
    height: 2px
    rounded: "{rounded.hairline}"
  divider:
    backgroundColor: "{colors.hairline}"
    height: 1px
    rounded: "{rounded.line}"
  divider-strong:
    backgroundColor: "{colors.hairline-strong}"
    height: 1px
    rounded: "{rounded.line}"
  divider-quiet:
    backgroundColor: "{colors.border-quiet}"
    height: 1px
    rounded: "{rounded.line}"
---

## Overview

The warmest reading of the brand in the set. Where the other directions argue with the
visitor (a threshold, a drawing board, a tape), Serambi simply makes the page feel like a
home: the owner's `beige-soft` as the paper, his `navy-deep` warmed until it reads as a
near-black ink rather than a cool navy, generous soft radii, and a three-layer shadow that
lifts a card the way daylight lifts a photograph on a wall. The surface is read **room by
room** — one space per section, a gold floor line under each — and it never looks like a
contractor's site or a technical sheet.

## Colors

- **Primary — beige-soft (`#faf8f4`):** the ground. Warm white, never grey; it is the owner's
  own token, not a taste decision.
- **Secondary — beige (`#e8dcc8`):** ambient blocks — media frames, chips. It is the ground's
  own hue one step deeper, so a frame reads as paper, not as a box.
- **Tertiary — navy-deep (`#0f1626`):** the dark plate (the logo's own ground) and the single
  closing band.
- **Accent — gold (`#c6a75e`):** the floor line under each room, and the hairline marks. It is
  never small text: at this lightness it fails contrast on the warm page.
- **Ink (`color-mix(navy-deep 88%, beige 12%)` → `rgb(36, 42, 56)`):** all type that carries
  weight. Warm near-black, deliberately not `#000` and not cold navy.
- **Ink secondary (`#665c4a`):** captions and metadata. Chosen along the beige axis until it
  clears **4.5:1 on both grounds** — measured 6.19:1 on the page (`rgb(250,248,244)`) and 4.85:1 on the ambient
  beige (`rgb(232,220,200)`). Never a cool grey. Hairlines: `rgb(218,217,217)` and
  `rgb(191,192,194)`.

## Typography

**Petrona** (a warm variable serif) names the rooms and carries the display
voice; **DM Sans** (variable grotesque) reads everything else. Both self-hosted as woff2, and
neither pair is used by the six other directions — this is the first time the set speaks with a
rounded sans and a soft serif together, which is what makes it read as residential.

- Room names are display size with tight tracking; body measure stops at 68ch.
- Labels are small, semibold and spacing-wide; they never compete with a room name.

## Layout

A 1180px measure. Pad clamps 18px → 58px, gutter 19px → 42px. Rooms alternate
six/five columns so the page never marches: text left, photograph right, then reversed. On
a phone the three service doors become **compact rows** (a 132px picture on the left, label
and metadata on the right) instead of three stacked posters.

## Shapes

Soft. `8px` buttons, `14px` media frames, `10px` plates, `22px` cards and blocks; the only
full circles are the play affordance and the kind chips' pill radius. Six directions in this
set are square-cornered; this is the one that is not.

## Depth

Two soft three-layer shadows (ring + blur + stronger blur) and a plate shadow. A shadow is
always a lift, never a glow: no zero-offset halo anywhere.

## Motion

One authored moment, shared by the whole surface: content arrives with a clip-path reveal,
room names resolve from a slight blur to sharp, and each room's **gold floor line draws**
left to right as the room is read. The phone menu is a full-screen drawer whose rows arrive
in sequence. Everything stands down under `prefers-reduced-motion`, and nothing is left
invisible without JavaScript.

## Components

`button-primary` is the single filled action; `button-quiet` the second path (always
WhatsApp). `card-door` is the service door: media frame, kind chip, label, meta.
`tile-frame` is the one media frame class — video tiles keep a poster and fetch nothing
until pressed. `band-dark` is the one dark block per page. `floor-line` is the signature.

## Do's and Don'ts

- **Do** keep every sentence the owner's own, and label every image `Foto`, `Render` or
  `Video`.
- **Do** tint secondary text along the beige axis; a grey caption breaks the warmth.
- **Don't** invent an address, e-mail, registration number, date, project name or statistic —
  the company plate prints *belum diterbitkan* where his site publishes nothing.
- **Don't** put the owner's logo anywhere except on its own dark plate: the file carries a
  white wordmark.
- **Don't** use the gold for body text, and don't add a third shadow or a glow.
