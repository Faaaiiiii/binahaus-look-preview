# COMMIT-SHEET — Bina Haus, arah 06 "PITA" (the reel / the tape)

> Seven decisions taken before the first line of markup. Nothing here is a default.
> Built on the owner's own assets: logo (unchanged), palette (read from his CSS), photographs,
> renders and footage (his), and copy (verbatim from binahaus.com). The typefaces are chosen here,
> self-hosted, and are **not** his own pair and **not** arah 03's pair.

## 1. Peak / signature — the reel plays

The home page is a reel, not a photograph. Two of the owner's own work videos — `work-video-1.mp4`
(an interior unit under works, glass and protection) and `work-video-2.mp4` (a commercial unit,
glass partition) — sit stacked full-bleed behind the tagline and **crossfade slowly, once around,
forever**: a 24s cycle with a ~1s blend, muted, looped, `playsinline`. Under the copy a **tape
strip** runs a gold numeral, the standard, a hairline rule and the domain, like a slate at the head
of a roll. Every chapter below is led by a video or a video poster, so the page reads as footage of
the owner's work rather than a gallery of stills. The single authored motion moment is the
crossfade; `prefers-reduced-motion` holds one frame instead of animating.

## 2. Colour — the owner's navy as the ground, his gold used once

| token | value (his) | job |
|---|---|---|
| `--navy` | `oklch(28.83% .0503 265.9)` | **the ground** — every surface, header, chapters, footer |
| `--beige` | `oklch(89.88% .0298 80.65)` | secondary type, mixed into `--ink-2` |
| `--beige-soft` | `oklch(97.96% .0057 84.57)` | headings and body light |
| `--gold` | `oklch(74.04% .0992 86.94)` | **the one accent** — the tape numeral/rule, chapter numerals, the rec dot, focus ring |

Committing to the **mid navy**, not arah 03's `navy-deep`. Background lightness is **L ≈ 0.29**
(the owner's navy), and the page's mean lightness is checked against that number, not a mood: a
footage ground reads as a screen at dusk, never a black void. `--inset` is the owner's navy shaded
16% toward black, used only for insets (media frames, the CTA band) — same hue, no new colour.
Refused: black; gold hairlines on every edge; gold gradient text; a second "brand" colour.

## 3. Type — a compact technical grotesque × a quiet text serif

- **Barlow Semi Condensed** (500/600/700) — a compact, slightly technical grotesque with a
  highway-signage / DIN lineage. It carries the tape numerals, chapter numerals, labels, nav,
  buttons and headings; its narrow caps read like camera-slate lettering, which is the point.
- **Newsreader** (400 + 400 italic) — a quiet, low-contrast text serif designed for reading
  (Production Type). It carries every paragraph: the owner's voice, set softly.

Both are fetched from **Google Fonts** (SIL OFL 1.1) and shipped as woff2 in `assets/fonts/` — no
CDN, no third-party request at runtime. **Why not the banned list:** this is a contrast-axis pair
(grotesque × serif) chosen for a footage-led, documentary register; it is not Inter or Space Grotesk
(the 2024–26 AI defaults), not Archivo/Manrope (the owner's own pair, which arah 03 owns), not
Literata/Hanken (arah 02), and not Playfair/Instrument Serif/Fraunces (the "elegant serif" reflex).

## 4. Grid break — the reel numeral hangs in the gutter

The one concrete break from the symmetric grid: every chapter's **running numeral sits in the left
gutter, outside the text measure**, and the chapter's media runs **full-bleed past the column**. The
eye reads the number as the tape's index and the picture as the frame — the numeral never sits above
a heading as an eyebrow (that is a ban), it sits beside the heading it counts.

## 5. Motion budget — one family

1. **The reel crossfade** — the only authored moment; `reelA`/`reelB` opacity keyframes, 24s, once
   per cycle, both videos muted and looping.
2. UI-level transitions only: link underline, button 160ms, focus ring. Nothing else.

No scroll reveals, no per-section fade-in, no parallax, no scrubbed timeline. Restraint is the
budget here: the footage carries the motion. `prefers-reduced-motion` receives a single held frame
(video 2 hidden), which is a *watchable* alternative, not a disabled page.

## 6. Reflex check

- **(a) The generic AI "premium renovation" page:** near-black ground, gold everywhere, a luxury
  serif voice, three identical service cards, an eyebrow above every heading, a hero-metric strip.
- **(b) What a generic AI avoiding (a) does:** the warm-artisan page — cream, terracotta, rounded
  corners, big friendly type, stock photography.
- **This page:** the owner's **mid navy** (not near-black), his **own footage** leading every
  chapter, his **gold used once** as the tape's playhead/numeral, and a **compact technical grotesque
  + quiet serif** pair instead of either a luxury serif or a friendly geometric. The structure is a
  reel of his real work, not a scaffold of identical cards. No eyebrow above any heading, no
  numbered-section scaffolding (numerals are the tape's real sequence), no gradient text, no glass.

## 7. Honesty rules for this build

- **Nothing is invented.** No address, e-mail, registration number, project name, statistic, date or
  testimonial is written unless it exists on binahaus.com. Company fields he has not published are
  printed as *belum diterbitkan*, so he can see exactly what to supply.
- **Every media item is labelled by what it is:** `Foto`, `Render` or `Video`. The library holds
  photographs, 3D renders and work-in-progress shots, and the page never passes a render off as a
  photo or a still as footage.
- **Added labels are mine and marked as such:** the chapter numerals, the room names
  (*Ruang tamu, Dapur, Butiran, Tapak*), the `REEL 01` tape strip, and the two build-note sentences
  that say plainly which tiles are renders.
- **The five heavy videos stream from the owner's own URLs** (`work-video-3…7`, ≈58 MB, each answering
  `206 video/mp4` to a range request); the two light ones are served from this page. His copy is
  verbatim; his logo is his own PNG file, only the transparent margin trimmed.

---

## House tells deliberately broken (min two)

- **Near-black background** — *broken*: the ground is the owner's mid navy (L ≈ 0.29), a lit screen,
  not a void.
- **The wordmark-as-hero** — *broken*: the hero is footage plus the tagline; the logo appears only as
  the header and footer mark, never enlarged as the page's subject.
- **Monospace as a technical costume** — *broken*: the tape labels use a compact **grotesque** with
  tabular figures, not a mono.
- **Glow standing in for lighting** — *broken*: no glow, no gradient text, no bloom; the only light is
  the gold numeral and the footage itself.
