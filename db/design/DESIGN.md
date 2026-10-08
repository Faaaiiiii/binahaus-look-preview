# DESIGN.md — Bina Haus, direction "Satu Tangan" (reka & bina)

The style contract. Every later edit reuses these tokens, section openings and motion families.

## Direction

**"Satu Tangan" — one hand, design and build.** Not a portfolio and not two service lists: a **working
document**. The page's argument is that the same hand decides and makes, shown as one drawing in two
states (design → built) joined by a single cobalt working line, plus a **decision register** (what was
chosen, why, what it became on site). The design act and the build act appear as facets of one object,
never as parallel columns.

## Tokens

| Token | Value (oklch) | Hex | Role |
|---|---|---|---|
| `--kapur` | `oklch(0.947 0.013 126)` | `#EBEFE6` | page field — lime plaster |
| `--kapur-2` | `oklch(0.918 0.015 126)` | `#E1E6DB` | recessed surface / row hover |
| `--kapur-3` | `oklch(0.884 0.017 124)` | `#D6DBCF` | tinted band (Kenapa Pilih Kami) |
| `--ink` | `oklch(0.275 0.021 62)` | `#2F251D` | primary type |
| `--ink-soft` | `oklch(0.452 0.023 62)` | `#5F5349` | body (6.39:1 on kapur) |
| `--ink-faint` | `oklch(0.505 0.022 62)` | `#6E6258` | meta (5.08:1 on kapur) |
| `--teak` | `oklch(0.285 0.048 55)` | `#3C2311` | material band / CTA / footer |
| `--teak-2` | `oklch(0.345 0.050 55)` | `#4D321F` | recessed on teak |
| `--on-teak` | `oklch(0.930 0.020 80)` | `#EFE7D9` | type on teak (11.9:1) |
| `--on-teak-d` | `oklch(0.765 0.030 72)` | `#BFB09E` | secondary on teak (6.9:1) |
| `--kerja` | `oklch(0.470 0.155 264)` | `#2C53B0` | **the one accent** — the working line (6.07:1 on kapur) |
| `--line` / `--line-hard` / `--line-dk` | rgba hairline ramps | | structure, drawing rules |

Background lightness target: **mean L ≈ 0.90** (a lit plaster field). Dark appears as a *material*
(teak) twice, spaced apart, never as a mood.

## Type

- **Display** — `Literata` (variable, optical size 7–72; real italic). Weights 400–600.
  Letter-spacing ≥ −0.02em; line-height 0.98–1.05.
- **Text** — `Hanken Grotesk` (humanist grotesque, real italic). Body 65–75ch.
- **Axis** — optical-size display serif × humanist grotesque. Explicitly not Inter / Space Grotesk;
  not Playfair / Instrument Serif.
- Sizes: hero h1 `clamp(3.4rem, 7.6vw, 7.4rem)` (type-led, exempt from the 6rem prose ceiling);
  section h2 `clamp(2.1rem, 4.2vw, 3.9rem)`; body `clamp(1.03rem, …)`, line-height 1.55.
- All fonts are **self-hosted woff2** under `assets/fonts/` with `unicode-range` per subset. No CDN,
  no third-party request at runtime.

## Grid

- Page container `--pad: clamp(1.25rem, 4.2vw, 4.5rem)`.
- **Grid break 1** — the hero signature is full-bleed: it ignores the page gutters and runs to both
  viewport edges, with the working line exiting the sheet at the right edge.
- **Grid break 2** — the decision register's material swatch is wider than its column and runs off the
  LEFT viewport edge (`margin-left: calc(var(--pad) * -1 - 1.5rem)`), out of the text column.
- Work lists are **registers** (hairline rules + numbered rows), never card grids.
- Section openings **rotate** across four treatments and never repeat an eyebrow: (I) heading +
  note-right (`#kerja`, `.tangan`), (II) heading + serif italic subline (`#hasil`, `#cara`),
  (III) ruled serif italic label (`Renovations`, `Construction`, `#tentang`), (IV) marginal italic
  note in the second column (`.kenapa`, the decision register). There is **no uppercase tracked kicker
  above any heading** — the one is a ban in impeccable's craft floor and auteur's eyebrow tell.

## Motion

Three families; only `transform` / `opacity` / SVG `stroke-dashoffset`:

1. **Garis kerja (hero)** — the one line draws across; the design half draws thin and dashed, the built
   half draws heavier after the node; the node ticks in. 1400ms, 200ms delay, once.
2. **Section reveals** — `[data-rev]`: rise 10px + fade, 560ms ease-out; register rows stagger 40–70ms.
3. **Cara Kami Kerja** — one continuous vertical rule advances per step as it enters (620ms).

Rules: durations 130–160ms for controls; no `transition: all`; no `scale(0)`; entrances ease-out.
`prefers-reduced-motion` collapses all of the above to a static, fully legible page.

## Robustness contract

- Content is **fully readable with JS disabled** — and also with JS enabled but no scrolling: the
  hidden state lives only inside `@supports not (animation-timeline: view())`, so where scroll-driven
  animations exist the reveal is a pure additive animation and the default is visible.
- No scroll listener anywhere; IntersectionObserver only (fallback path), plus bounded self-clearing sweeps.
- No horizontal overflow 320 → 1920px.
- Every <p> in visible copy is free of em dashes (slopscan EM_DASH_COPY density rule); sentences carry
  the structure instead.
