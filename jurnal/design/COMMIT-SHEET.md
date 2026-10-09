# COMMIT-SHEET — Bina Haus, arah 04 "JURNAL TAPAK"

> Seven decisions taken before the first line of markup.
> The owner's own five process steps are the spine; his own photographs hang off it.

## 1. Peak / signature — the diary, not the brochure

Every renovation site shows finished rooms. Almost none shows **how the work actually moves**: the
site visit, the plaster, the scaffold, the piles of timber on the floor. Bina Haus has all of those
photographs — his own library is full of them — and his own site publishes the five steps that give
them an order. So this direction's peak is not a hero animation and not a drawing: it is the
**five-step spine**, with his real work photographed at every step and labelled by what it truly
shows (`Proses`, `Siap`, `Render`, `Video`). A visitor describes it as *"the diary of a build, in the
order it happens."*

## 2. Colour — daylight on the owner's own sand

Where arah 03 stands the house at dusk, this one puts it in daylight: the owner's own **sand**
(`beige`, `oklch(89.88% .0298 80.65)`) as the ground, his **navy-deep** as ink, his **paper**
(`beige-soft`) for the one raised surface, and his **gold** kept for the single thing that moves —
where the work has reached. One dark band per page (the closing call-to-action) and one small dark
plate for the logo, because the logo file is drawn with a white wordmark for a dark ground.

**The accent is never text on sand.** His gold measures 1.7:1 there; the numerals use
`accent-ink = color-mix(gold 52%, ink)`, measured **4.79:1**. Decorative gold stays decorative.

## 3. Type — Schibsted Grotesk + Source Sans 3

Both self-hosted as woff2, neither on the overused-face list, and neither is Archivo or Manrope
(arah 03 owns that pair). Schibsted Grotesk does the display voice, the labels and the numerals — the
diary needs figures that hold a column. Source Sans 3 carries the reading text.

## 4. Grid break

The **split hero**: the owner's own hero sentence on the sand at the left, one of his photographs
full-height at the right, each getting half the viewport. On a phone the photograph drops below the
words. The diary rows break the measure: each phase is a four/five-column pair with a hairline
running down the gutter between them, and the photographs are given the wider side.

## 5. Motion budget — two families, no more

1. **Reveals** — a scroll-driven rise (opacity + 14px), the same family everywhere, no per-section
   choreography.
2. **The rail** — the numerals mark progress; nothing else moves.

Nothing sits on a photograph, so there is no scrim choreography and no parallax. `prefers-reduced-motion`
receives the finished state.

## 6. Reflex check

- **(a) What a generic AI does for a renovation site's "process" page:** a timeline with rounded cards,
   icons in circles, a coloured left border, and a stock photo of a man in a hard hat shaking hands.
- **(b) What a generic AI avoiding (a) does:** the same list in a quieter grey with more whitespace.
- **This page:** no cards, no icons, no rounded corners, no stock — the owner's own progress
  photographs, full-bleed, attached to his own steps, with a provenance chip on every one. The only
  circles in the whole system are the video play buttons.

## 7. Honesty rules for this build

- **The photographs are not one project.** They come from the company's library, undated. The diary
  says so in plain words directly under the five phases, and every image carries its kind.
- **Nothing is invented** — no date, address, e-mail, registration number, project name, statistic or
  testimonial. The company plate prints *belum diterbitkan* where the owner has published nothing.
- The five steps, the seven renovation works, the three construction works and every sentence of copy
  are the owner's, verbatim.
