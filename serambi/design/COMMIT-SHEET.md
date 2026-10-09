# COMMIT-SHEET — Bina Haus, arah 07 "SERAMBI"

> Seven decisions taken before any markup. Reference-first: the direction was settled from
> `popular-web-designs/airbnb.md` (photography first, soft radii, three-layer shadows, warm
> near-black), `popular-web-designs/apple.md` (Navigation & type scale) and
> `impeccable/reference/craft-floor.md` + `adapt.md` (craft rules, full-screen phone menu).

## 1. Peak / signature — a house read room by room

The six earlier directions each argue something (a threshold, a drawing board, a tape, a
diary). This one does not argue: it lets the owner's own photographs carry the page and reads
it **room by room** — one space per section, in the order a visitor would walk a home, with a
2px line of the owner's gold drawn along the floor of each room as it is read. The line is the
peak: it makes the page feel like a floor plan you are walking, not a gallery you are scrolling.

## 2. Colour — the warmest reading of his own five

- Ground: his **beige-soft** (`#faf8f4`) — the page itself.
- Ambient blocks and media frames: his **beige** (`#e8dcc8`) — his own hue one step deeper, so a
  frame reads as paper rather than as a box.
- Ink: his **navy-deep** warmed with 12% of his beige → `rgb(28, 33, 47)`. A warm near-black;
  deliberately neither `#000` nor cold navy.
- Secondary: `#665c4a`, chosen along the same beige axis until it clears **4.5:1 on both the
  page and the ambient beige** — measured **6.19:1** and **4.85:1**. No cool grey anywhere.
- Accent: his **gold** (`#c6a75e`) for the floor line and hairlines only. It is never text on
  this ground; at that lightness it would fail.

## 3. Type — Petrona over DM Sans

The first **warm serif + rounded grotesque** pair in the set (the others are Archivo/Manrope,
Literata/Hanken, Schibsted/Source Sans, Libre Franklin/Spectral, Barlow Semi Condensed/
Newsreader). Petrona names the rooms; DM Sans reads everything else. Both self-hosted woff2,
no CDN. Petrona's softness is what makes the warmth read as *home* rather than *hotel*.

## 4. Grid break — rooms that alternate, doors that become rows

Rooms alternate six/five columns (text left, photograph right, then reversed) so the page never
marches in one column width. On a phone the three service doors stop being three stacked
posters and become **compact rows**: a 132px picture on the left, the label, kind chip and meta
stacked on the right. That is the mobile shape the owner asked for after the earlier
directions looked crowded on his phone.

## 5. Shapes and depth — the one direction that is not square

Every earlier direction in this set is square-cornered with hairline-only separation. Serambi
carries **8px buttons, 14px media frames, 10px plates, 22px cards**, and two soft
**three-layer shadows** (ring + blur + stronger blur) lifted from the reference system. A
shadow here is always a lift; there is no zero-offset glow anywhere.

## 6. Reflex check

- **(a) What a generic AI does for a renovation site:** a stock photograph of a man in a hard
  hat shaking hands, a gradient hero, rounded blue buttons, three identical icon cards, and the
  word "Quality" twice.
- **(b) What a generic AI avoiding (a) does:** the same list in grey with more whitespace.
- **This page:** the owner's own photographs at full width, warm paper, a soft lift instead of a
  border, and one gold floor line that draws as the room is read. No icon cards, no gradients,
  no stock.

## 7. Honesty rules for this build

- Every sentence is the owner's, verbatim; the building's own labels (`Foto`, `Render`, `Video`)
  ride on every image.
- Nothing is invented — no address, e-mail, registration number, founding year, project name or
  statistic. The company plate prints *belum diterbitkan* where his site publishes nothing.
- The owner's logo is his own PNG, unchanged, on its own dark plate, because the file carries a
  white wordmark drawn for a dark ground.
- The five heavy videos stream from the owner's own URLs with `preload="none"`; nothing is
  fetched until a visitor presses play.
