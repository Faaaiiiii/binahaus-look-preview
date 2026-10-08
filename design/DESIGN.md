# DESIGN.md — Bina Haus (look preview)

The style contract. Every later edit reuses these tokens, section openings and motion families.

## Direction

**"Tapak" — the setting-out board.** A lit drafting board, not a photo hero; a specification
document, not a marketing page. The building is *drawn* (hand-authored SVG elevation), the voice
is a *schedule of works*, and the one accent is the *setting-out line* a build is set from.

## Tokens

| Token | Value | Role |
|---|---|---|
| `--board` | `#E8E9EB` | page surface — cool concrete, chroma 0.004 @ hue 250 |
| `--board-2` | `#DDDFE1` | recessed surface / row hover |
| `--board-3` | `#D2D4D4` | reserved |
| `--ink` | `#262320` | primary type |
| `--ink-soft` | `#5A554C` | body on board (6.09:1) |
| `--ink-faint` | `#666257` | numbers, meta (5.01:1) |
| `--dark` | `#1E1B17` | material band / footer / CTA |
| `--dark-2` | `#2C2823` | recessed on dark |
| `--on-dark` | `#E6E2DA` | type on dark (12.9:1) |
| `--on-dark-d` | `#9C958A` | secondary on dark (5.78:1) |
| `--set` | `#BE341F` | **the one accent** — setting-out line + its labels only (4.67:1 on board) |
| `--line` / `--line-hard` / `--line-dk` | rgba hairline ramps | schedule rules, drawing rules |

Background lightness target: **mean L ≈ 0.90** (lit page). Dark appears once as a material band.

## Type

- **Display** — `Big Shoulders Display` (variable, condensed industrial grotesque). Site-signage voice. Weights 600–700, letter-spacing ≥ −0.012em, line-height 0.94.
- **Text** — `Newsreader` (optical-size humanist serif, real italic). Specification voice.
- **Axis** — condensed industrial grotesque × humanist serif. Explicitly not Inter / Space Grotesk; not Playfair / Instrument Serif.
- Sizes: hero h1 `clamp(3.5rem, 8.4vw, 8.6rem)` (type-led, exempt from the 6rem prose ceiling); section h2 `clamp(2.3rem,4.6vw,4.2rem)`; body `clamp(1.06rem, …)` at 65–75ch.

## Grid

- Page container `--pad: clamp(1.25rem, 4.2vw, 4.5rem)`.
- **Grid break 1** — hero h1 pulled flush to the physical left edge (`margin-left: calc(var(--pad) * -1)`); the elevation drawing runs into the right margin (`margin-right: calc(var(--pad) * -.55)`) and is never cropped.
- **Grid break 2** — a full-bleed dark material band interrupts the contained sections.
- Work / service lists are **schedules** (hairline rules + numbered rows), never card grids.
- Section openings vary: heading + note-right, heading + Malay/English subline, blockquote, two-column statement. Only the hero carries a kicker, and it lives in the drawing-sheet header, not above the h1.

## Motion

Three families, `transform` / `opacity` / SVG `stroke-dashoffset` only:

1. **Datum draw** — hero setting-out line draws in, 1500 ms, 260 ms delay, once.
2. **Section reveals** — `[data-rev]` rise 18px, 620 ms ease-out, staggered per row.
3. **Process register** — one hairline rule scales in per step as it enters (620 ms, scaleX from left).

Rules: durations 130–160 ms for controls; no `transition: all`; no `scale(0)`; entrance easing is
ease-out. `prefers-reduced-motion` collapses all of the above to a static, fully legible page.

## Robustness contract

- Content is **fully readable with JS disabled** — reveals are additive (`html.is-ready` gates them).
- Reveals can never leave copy hidden: IntersectionObserver plus a bounded, self-clearing sweep.
- No scroll listener anywhere. No horizontal overflow 320 → 1920 px (verified).
