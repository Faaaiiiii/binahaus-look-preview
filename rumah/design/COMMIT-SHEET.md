# COMMIT-SHEET — Bina Haus, arah 03 "MASUK" (the threshold)

> Seven decisions taken before the first line of markup. Nothing here is a default.
> Built on the owner's own assets: logo (unchanged), palette (read from his CSS), typefaces
> (his own Archivo + Manrope), photographs and copy (verbatim from binahaus.com).

## 1. Peak / signature — the door

The page opens. Two panels part over the photograph of the finished living room, exactly once, on
load, and the logo sits behind them as a **lit sign** — because that is what the owner's logo file
actually is: a warm-glow white-and-gold mark on transparency, drawn for a dark ground. The visitor's
first act is the brief's own: *bila buka website, seperti berada dalam sebuah design rumah*. The one
authored moment, 1.1s, `ease-out`, gone in reduced-motion.

## 2. Colour — the brand's own five, read out of his stylesheet

| token | value (his) | job |
|---|---|---|
| `--navy-deep` | `oklch(20.21% .034 265.48)` | the ground: a navy house at dusk, not black |
| `--navy` | `oklch(28.83% .0503 265.9)` | raised surfaces (plaque, tiles) |
| `--beige` | `oklch(89.88% .0298 80.65)` | type on navy |
| `--beige-soft` | `oklch(97.96% .0057 84.57)` | headings and the light that falls on them |
| `--gold` | `oklch(74.04% .0992 86.94)` | **the one accent**, < 0.5% of pixels |

The logo's own flat gold measures `#D5A64C` from the file — the same gold, two independent sources.
Light is warm (beige/gold) on a cool ground (navy), the way a lit interior reads from a dark street.
Refused: black; gold hairlines on every edge; gold gradient text.

## 3. Type — the brand's own pair, self-hosted

**Archivo** (display, 600/700, wide tracking in the caps) matches the lettering under the house mark;
**Manrope** (text, 400/500/600) is what the owner's own site sets its body in. Both are fetched from
Google Fonts and shipped as woff2 in `assets/fonts/` — no CDN, no third-party request at runtime.

## 4. Grid break

The photograph is the page's **floor plan**: room chapters are full-bleed and run past the text
column, and the "TAPAK" construction plate breaks the right edge of the viewport while its note
stays in the gutter. Text never sits on a photograph without a measured scrim.

## 5. Motion budget — three families

1. **The door** (once, on load; the only full-screen moment).
2. **Hairline rules drawing + photographs settling** (`clip-path`/`transform` + `opacity`, per
   chapter, on scroll).
3. **Chapter numerals and the plaque rows settling.** Nothing else. `prefers-reduced-motion`
   receives the finished state, not a disabled one.

## 6. Reflex check

- **(a) The generic AI "premium renovation" page:** black ground, gold everywhere, a serif luxury
  voice, three identical service cards, an eyebrow above every heading, a hero-metric strip.
- **(b) What a generic AI avoiding (a) does:** the light warm-artisan page — cream, terracotta,
  rounded corners, big friendly type.
- **This page:** the owner's navy at dusk, the owner's gold used **once**, the owner's grotesque
  pair instead of a luxury serif, and the page structured as the walk through one home rather than
  a scaffold of cards. No eyebrow above any heading (an absolute ban), no section numbers except the
  owner's own service numbering, no gradient text, no glass.

## 7. Honesty rules for this build

- **Nothing is invented.** No address, e-mail, registration number, project name, statistic, date or
  testimonial is written unless it exists on binahaus.com. Fields the owner has not published are
  printed as *belum diterbitkan* with a footnote, so he can see exactly what to supply.
- **Every image is labelled by what it is:** `FOTO` (photograph), `RENDER` (3D render), `PROSES`
  (work in progress). The library holds all three; the page never passes a render off as a photo.
- The room names (Ruang tamu, Dapur, Butiran, Bilik) are **added labels** that give the walk its
  chapters; the brief's own words are never rewritten.
