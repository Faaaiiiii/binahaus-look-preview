# COMMIT-SHEET — Bina Haus (design & build look preview)

> Direction: **"Satu Tangan"** (one hand) — reka & bina.
> Seven decisions before the first line of code. Nothing here is a default.

## 1. Peak / Signature

**One drawing, two states.** The hero carries a single full-bleed drawing of a joinery bay of a
Malaysian home (a window opening in a plastered wall), read as ONE object: its left half is the
**design** (fine linework, dimension lines, a material callout with the reason for it), its right
half the **built** (the same geometry with timber grain, wall hatch, plaster band and site notes).
One continuous **cobalt "garis kerja"** (the working line, at sill level) runs the whole width:
thin and dashed while it is still a drawing, heavier and solid once it has been built, with a single
node and the label `reka → bina` where it crosses. A visitor describes it as *"the drawing and the
thing built are the same line."* That single object is the whole design-and-build argument: one
geometry, one author, decided and then made.

## 2. Color

- **Tier: restrained field + one committed material.** Kapur ≈ 76% of pixels, teak ≈ 20%, accent < 0.3%.
- **Kapur (lime plaster)** `oklch(0.947 0.013 126)` ≈ `#EBEFE6`. A green-tinted plaster off-white. It
  is a **material colour**, not the warmth reflex: hue 126 sits outside the banned warm-cream band
  (hue 40–100), and the scene is a plastered room in Malaysian daylight. Written as `oklch()`, not hex,
  so the distinction is exact rather than an HSL approximation of it.
- **Teak** `oklch(0.285 0.048 55)` ≈ `#3C2311` — the dark **material** band (timber joinery: the making).
  Full-bleed once, for the thesis section. It is a material, not a "premium dark mood".
- **Ink** `oklch(0.275 0.021 62)` ≈ `#2F251D`; body `oklch(0.505 0.022 62)` (5.08:1 on kapur).
- **Accent — "kerja" (chalk-line cobalt)** `oklch(0.470 0.155 264)` ≈ `#2C53B0`. A builder's chalk line
  (*tali kapur*) is the line the maker marks and follows. Cobalt here is a **tool** colour, not the SaaS
  blue: it measures **6.07:1 on kapur**.
- **Background lightness as a number: target mean L ≈ 0.90.** The page lives lit, like a plastered room
  in daylight; a near-black page makes a design-and-build firm read as a nightclub (the skill's #1 tell).
- **The accent is used EXACTLY ONCE**: the one continuous garis kerja inside the hero signature.
  Its single meaning: *the decision crossing out of the drawing and into the built thing* — the proof
  that one hand did both. No cobalt buttons, no cobalt hover, no cobalt divider, no cobalt link.

## 3. Type

- **Display: Literata** (variable, optical-size axis 7–72, by TypeTogether). Voice: *authored, hand-set,
  a book's serif* — the design act. Chosen over **Fraunces** (the first pick) because the impeccable
  detector flags Fraunces as an overused AI-default display serif; Literata keeps the optical-size axis
  and the editorial warmth without the reflex, and is unmistakably not Playfair / Instrument Serif.
- **Text: Hanken Grotesk** (humanist grotesque, open apertures, real italic). Voice: *the site note,
  the specification* — the build act.
- **Axis: optical-size display serif × humanist grotesque** — a real contrast pair, and the deliberate
  *inverse* of the Tapak preview's condensed-grotesque display × humanist serif.
- **Why not Inter:** the 2024–26 AI default, banned by name. **Why not Playfair / Instrument Serif:**
  the reflex "elegant serif" shortlist.
- Hero headline is **type-led** (clamp to ~7.4rem) and declared as part of the signature; prose stays
  ≤ 4rem. (Reference for the axis: Anthropic/Claude's single-weight serif-over-warm-material system;
  the axis itself is inverted here, serif on display rather than serif on body.)

## 4. Grid break

1. **The hero signature is full-bleed.** The drawing ignores the page gutters and runs to both
   viewport edges, so its geometry reads at a scale the text column could never give it; the cobalt
   working line, drawn last, exits the sheet at the right edge.
2. **The material swatch of the decision register runs off the LEFT viewport edge.** The swatch is
   wider than its grid column and is cut by the page edge (`margin-left: calc(var(--pad) * -1 - 1.5rem)`),
   so the material leaves the document while the register's text and hairlines stay in the column.

## 5. Motion budget

Three families, no more:

1. **Hero garis kerja** — the one line draws across, thin on the design half, heavier past the node;
   the node ticks in. Once, on load.
2. **Section reveals** — content-specific: hairline rules draw, register rows settle (opacity + 10px
   rise + 1.01 scale on the swatch), swatch tiles settle.
3. **Cara Kami Kerja** — ONE continuous vertical rule advances step by step as the register is scrolled
   (`stroke-dashoffset`), with a node per step. Not a per-row rule.

Only `transform` / `opacity` / SVG `stroke-dashoffset`. `prefers-reduced-motion` gets a gentler static
alternative, not zero.

## 6. Reflex check

- **(a) What a generic AI does for a renovation "design & build" page:** a dark "architecture studio"
  portfolio, full-bleed photographs, thin white type, and two parallel service lists (Design / Build).
- **(b) What a generic AI avoiding (a) does:** the light "warm artisan" page — cream body, terracotta
  accent, one serif headline, hand-drawn squiggles. Also saturated.
- **(c) Our argued deviation:** **neither a portfolio nor two lists — a working document.** The proof of
  a design-and-build studio is not a service menu but the **decision**: what was chosen, why, and what it
  became on site, plus one drawing shown in both states. Recon read (Notion: whisper 1px hairlines as the
  only structure, generous vertical rhythm; Anthropic/Claude: single-weight serif over warm material
  neutrals, no gradients) supplies the *discipline*, not the skin.

## 7. House tells broken

1. **Near-black by default** → broken: the page is a lit plaster field at mean L ≈ 0.90; the one dark
   moment is a *material* (teak), not a mood.
2. **Mono service type in the corners** → broken: **no monospace anywhere**; labels are Hanken Grotesk
   uppercase at tracked spacing, and section openings vary (drawing sheet, statement, register, swatch
   strip, note-right). *(Also broken for free: #6 wordmark-as-hero — the hero is a drawing, not the brand
   name at 200px; #4 scroll-instruction footer — none; #5 amber/acid accent — a tool cobalt used once.)*

## 8. Why this is not the Tapak preview (deltas, stated)

| | Tapak (preview 1) | **Satu Tangan (this preview)** |
|---|---|---|
| World | the drafting board / the drawing sheet | the workshop and the sample board / the making |
| What is shown | the building *drawn* (front elevation, 1:100) | one decision *made and built* (joinery bay, two states) |
| Field | cool concrete `#E8E9EB` (chroma @ hue 250) | green lime plaster `oklch(0.947 0.013 126)` |
| Dark moment | graphite material band | teak material band |
| Accent + meaning | oxide red, setting-out line ±0.00 | cobalt, the working line crossing reka → bina |
| Type axis | condensed grotesque (display) × humanist serif (text) | optical-size serif (display) × humanist grotesque (text) |
| Grid break | headline flush left; full-bleed dark band | full-bleed drawing crossing the seam; swatch column bleeding off-edge |
| Motion | datum draws; schedule rows tick | one line crossing states; one continuous process rule |
| Narrative | services as a schedule of works | the decision register as the trust engine |
