# SYSTEM-REPORT — 7 route(s), 2026-10-09

The system as **painted**, not as documented. A token in the stylesheet that never renders is
not part of the system; a one-off inline style is. Read this against `design/DESIGN.md` — every
number below that DESIGN.md does not account for is drift.

**Look at `components.png`** — one tile per distinct rendered control variant. Two tiles that look the same to you but appear separately are the drift.

## Controls

| kind | distinct variants | budget | total instances |
|---|---|---|---|
| link | **5** | 4 | 118 |
| button | **2** | 4 | 7 |

### link
- ×7 on 7 route(s) — "SKIP TO CONTENT" — `oklch(0.2021 0.034 265.48) | oklch(0.9796 0.0057 84.57) | oklch(0.9796 0.0057 84.57) | 0b | 0r | 13/600 | 11x18 | noshadow`
- ×7 on 7 route(s) — "" — `rgba(0, 0, 0, 0) | oklch(0.2883 0.0503 265.9) | oklch(0.2883 0.0503 265.9) | 0b | 0r | 15/500 | 5x2 | noshadow`
- ×36 on 7 route(s) — "Services" — `rgba(0, 0, 0, 0) | oklch(0.2883 0.0503 265.9) | oklch(0.2883 0.0503 265.9) oklch(0.2883 0.0503 265.9) rgba(0, 0, 0, 0) | 0b | 0r | 15/500 | 5x2 | noshadow`
- ×66 on 7 route(s) — "FOTO
Ruang tamu — tujuh " — `rgba(0, 0, 0, 0) | oklch(0.2021 0.034 265.48) | oklch(0.2021 0.034 265.48) | 0b | 0r | 17/400 | 0x0 | noshadow`
- ×2 on 1 route(s) — "WhatsApp +60 11-1124 463" — `rgba(0, 0, 0, 0) | oklch(0.2021 0.034 265.48) | oklch(0.2021 0.034 265.48) oklch(0.2021 0.034 265.48) oklab(0.793 -0.000233131 -0.00382206) | 0b | 0r | 17/500 | 6x2 | noshadow`
- *states (not counted as variants): current ×6*

### button
- ×3 on 2 route(s) — "GET FREE QUOTATION" — `oklch(0.2021 0.034 265.48) | oklch(0.9796 0.0057 84.57) | oklch(0.2021 0.034 265.48) | 1b | 0r | 13/600 | 12x20 | noshadow`
- ×4 on 2 route(s) — "WHATSAPP US" — `rgba(0, 0, 0, 0) | oklch(0.2021 0.034 265.48) | oklab(0.5753 -0.0011344 -0.0149013) | 1b | 0r | 13/600 | 12x20 | noshadow`

> States — disabled, current, and controls inside a row carrying a `data-state` — are
> excluded from the variant budget. A disabled button paints differently on purpose; a
> product that has no disabled state at all should not score better than one that does.

## Tokens as rendered

**Colour** (7 distinct)
- `oklch(0.2883 0.0503 265.9)` — 184× on 7 route(s)
- `oklch(0.2021 0.034 265.48)` — 169× on 7 route(s)
- `oklab(0.925175 0.00031407 0.00290461)` — 35× on 3 route(s)
- `oklch(0.9796 0.0057 84.57)` — 33× on 7 route(s)
- `oklch(0.8988 0.0298 80.65)` — 8× on 4 route(s)
- `oklab(0.9174 0.000281882 0.00250893)` — 7× on 5 route(s)
- `oklch(0.7404 0.0992 86.94)` — 3× on 2 route(s)

**Type step** (16 distinct)
- `17px/400/Spectral` — 97× on 7 route(s)
- `12px/600/Libre Franklin` — 66× on 7 route(s)
- `13px/400/Spectral` — 65× on 7 route(s)
- `15px/500/Libre Franklin` — 36× on 7 route(s)
- `13px/600/Libre Franklin` — 29× on 7 route(s)
- `25px/400/Spectral` — 18× on 7 route(s)
- `40px/700/Libre Franklin` — 12× on 6 route(s)
- `24px/600/Libre Franklin` — 10× on 1 route(s)
- `15px/600/Libre Franklin` — 6× on 6 route(s)
- `58px/700/Libre Franklin` — 6× on 6 route(s)
- …and 6 more

**Radius** (0 distinct)

**Shadow** (0 distinct)

## Per route

| route | landmarks | h1 | focusable | console errors |
|---|---|---|---|---|
| http://127.0.0.1:8124/siang/ | header,nav,main,footer | 1 | 25 | 0 |
| http://127.0.0.1:8124/siang/perkhidmatan.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/siang/kerja.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/siang/cara.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/siang/tentang.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/siang/syarikat.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/siang/kontak.html | header,nav,main,footer | 1 | 21 | 0 |

## FAIL
- link: 5 distinct rendered variants (budget 4). A variant nobody can name is drift.

## WARN
- 1 type step(s) appear on exactly one route and nowhere else — that is where the system is splitting: 24px/600/Libre Franklin
- 16 distinct type steps across the product — a scale nobody can hold in their head is not a scale
- no disabled control appeared on any route — the disabled state is probably undesigned, not absent
