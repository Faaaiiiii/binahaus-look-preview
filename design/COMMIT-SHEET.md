# COMMIT-SHEET — Bina Haus (look preview)

> Seven decisions before the first line of code. Nothing here is a default.

## 1. Peak / Signature

**The hero carries a hand-drawn front elevation of a Malaysian terrace house — authored in SVG — in the place where every competitor puts a photograph.** The drawing sits on a drafting board; the single red *setting-out line* ("datuk / datum" line, marked ±0.00) draws itself under the headline on load. A visitor describes it as "the house is drawn, not photographed". A renovation company's strongest proof is finished work; we cannot use the client's photography in a preview, so the proof becomes the **drawing** — the second-oldest document in construction after the handshake.

## 2. Color

- **Tier: restrained field + one committed mark.** Board (surface) ≈ 82% of pixels; ink ≈ 15%; accent < 0.4%.
- **Board** `oklch(0.918 0.004 250)` ≈ `#E8E9EB` — a **cool** concrete board, chroma ~0.004 at hue 250 (blue). Deliberately not the cream/beige band (hue 40–100): the page must not read "warm artisan brand".
- **Ink / kiln graphite** `oklch(0.26 0.010 70)` ≈ `#2A2723`; dark material band `oklch(0.205 0.012 62)` ≈ `#1E1B17`.
- **Accent — "chalk-set oxide"** `oklch(0.575 0.185 32)` ≈ `#BE341F`. It is a **red-vermilion tablet pigment**, the colour of a contractor's setting-out chalk / red lead, **not** the amber house tell (hue ≈30 warm glow); it is at hue ~32 but at chroma 0.185 and value 0.575 — a pigment, not a glow. Measured 4.67:1 on the board, so it also clears AA as text.
- **Background lightness as a number: target mean L ≈ 0.90.** The page lives *lit*: this is a daytime building site at handover, seen in flat Malaysian daylight. A near-black page would make a renovation business read as a nightclub and is the skill's #1 house tell — broken on purpose.
- **The accent is used EXACTLY ONCE**: the datum line + its `±0.00` annotation in the hero. Nowhere else. No red button, no red hover, no red divider. Its meaning is singular: the line every build is set out from.

## 3. Type

- **Display: "Big Shoulders Display"** (variable, condensed industrial grotesque). Voice: *signage, hoarding, site marking* — a construction brand's native letterform.
- **Text: "Newsreader"** (optical-size humanist serif). Voice: *specification, schedule of works, the report* — documentation, not marketing.
- **Axis: condensed industrial grotesque × humanist serif.** A real contrast pair, not two similar sans faces.
- **Why not Inter:** Inter (and Space Grotesk) are the 2024–26 AI default; **why not Playfair / Instrument Serif:** the reflex "elegant serif" shortlist, banned by name.
- Display exceeds the 6rem prose ceiling: the hero headline is **type-led** (clamp to ~9.5rem) and the commit-sheet declares the type as part of the signature. Prose stays ≤ 4.2rem.

## 4. Grid break

**Both columns break the container, each in a different direction.** The hero headline is pulled flush to the physical left edge of the board (`margin-left: calc(var(--pad) * -1)`), so the display type starts where the page starts while the kicker, body and CTAs stay indented at the pad. The elevation drawing runs out into the right-hand margin (`margin-right: calc(var(--pad) * -.55)`) without ever being cropped. Second break: between *Renovations* and *Construction* a **full-bleed dark material band** interrupts the two contained sections — a section boundary you feel rather than see.

## 5. Motion budget

Three families, no more:
1. **Hero**: datum line draws (`stroke-dashoffset`) + headline line-rise stagger on load.
2. **Section reveals**: content-specific — hairline rules draw, indexed list rows stagger like a schedule of works ticking in (30–70 ms).
3. **Process (Cara Kami Kerja)**: steps advance as a drafting register — one ledger rule extends per step as it enters.

Only `transform` / `opacity` / SVG `stroke-dashoffset` animate. `prefers-reduced-motion` gets a gentler alternative, not zero.

## 6. Reflex check

- **(a) What a generic AI does for architecture/construction** (recon, cssnectar/awwwards 2025–26): full-bleed white page, oversized photograph grid, tiny tracked mono captions, "modern minimal" with an Inter body and a gold/amber accent. **This is exactly the incumbent binahaus.com.**
- **(b) What a generic AI avoiding (a) does:** the dark "stone, light, silence" cinematic studio site (the awwwards architecture default, e.g. dark editorial portfolios) — also saturated.
- **(c) Our argued deviation:** **a lit drafting board.** The building is shown as a *drawing*, the voice is a *specification document*, and the one accent is a *setting-out line*. Construction's own visual language (elevations, dimensions, schedules) used as the design system — not photography, not darkness.

## 7. House tells broken (taste.md §2.5)

1. **Near-black by default** → broken: the page is **lit** at mean L ≈ 0.90 board with a single dark material band; the drama is in the ink-vs-board contrast and the drawn line.
2. **Mono service labels in the corners** → broken: **no monospace anywhere**; service/label type is Big Shoulders at small size and Newsreader small caps.
   (Also broken, for free: #4 scroll-instruction footer — none; #6 wordmark-as-hero — the hero is a drawing, not the brand name at 200px; #5 amber accent — the accent is a pigment red used once.)
