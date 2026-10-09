# SYSTEM-REPORT — 7 route(s), 2026-10-09

The system as **painted**, not as documented. A token in the stylesheet that never renders is
not part of the system; a one-off inline style is. Read this against `design/DESIGN.md` — every
number below that DESIGN.md does not account for is drift.

**Look at `components.png`** — one tile per distinct rendered control variant. Two tiles that look the same to you but appear separately are the drift.

## Controls

| kind | distinct variants | budget | total instances |
|---|---|---|---|
| link | **4** | 4 | 120 |
| button | **3** | 4 | 16 |

### link
- ×7 on 7 route(s) — "Skip to content" — `oklch(0.9796 0.0057 84.57) | oklab(0.383242 -0.000724008 -0.0174367) | oklab(0.383242 -0.000724008 -0.0174367) oklab(0.383242 -0.000724008 -0.0174367) oklab(0.2021 -0.00267944 -0.0338943 / 0.22) | 0b | 0r | 14/600 | 11x18 | noshadow`
- ×43 on 7 route(s) — "" — `rgba(0, 0, 0, 0) | oklab(0.383242 -0.000724008 -0.0174367) | oklab(0.383242 -0.000724008 -0.0174367) oklab(0.383242 -0.000724008 -0.0174367) rgba(0, 0, 0, 0) | 0b | 0r | 14/600 | 8x0 | noshadow`
- ×68 on 7 route(s) — "Consultation" — `rgba(0, 0, 0, 0) | oklab(0.383242 -0.000724008 -0.0174367) | oklab(0.383242 -0.000724008 -0.0174367) oklab(0.383242 -0.000724008 -0.0174367) oklab(0.2021 -0.00267944 -0.0338943 / 0.22) | 0b | 0r | 14/600 | 0x0 | noshadow`
- ×2 on 1 route(s) — "+60 11-1124 4636" — `rgba(0, 0, 0, 0) | oklch(0.2021 0.034 265.48) | oklch(0.2021 0.034 265.48) | 0b | 0r | 19/400 | 10x0 | noshadow`
- *states (not counted as variants): current ×6*

### button
- ×3 on 2 route(s) — "Get free Quotation" — `oklch(0.2021 0.034 265.48) | oklch(0.9796 0.0057 84.57) | oklch(0.2021 0.034 265.48) | 1b | 0r | 14/600 | 12x18 | noshadow`
- ×4 on 2 route(s) — "WhatsApp Us" — `rgba(0, 0, 0, 0) | oklch(0.2021 0.034 265.48) | oklab(0.2021 -0.00267944 -0.0338943 / 0.4) | 1b | 0r | 14/600 | 12x18 | noshadow`
- ×9 on 2 route(s) — "button" — `rgba(0, 0, 0, 0) | rgb(0, 0, 0) | rgb(0, 0, 0) | 0b | 0r | 13/400 | 0x0 | noshadow`

> States — disabled, current, and controls inside a row carrying a `data-state` — are
> excluded from the variant budget. A disabled button paints differently on purpose; a
> product that has no disabled state at all should not score better than one that does.

## Tokens as rendered

**Colour** (8 distinct)
- `oklab(0.383242 -0.000724008 -0.0174367)` — 181× on 7 route(s)
- `oklch(0.2883 0.0503 265.9)` — 95× on 7 route(s)
- `oklch(0.2021 0.034 265.48)` — 46× on 7 route(s)
- `oklch(0.9796 0.0057 84.57)` — 38× on 7 route(s)
- `oklch(0.8988 0.0298 80.65)` — 22× on 7 route(s)
- `oklab(0.482016 0.00146751 0.0352412)` — 10× on 2 route(s)
- `oklab(0.2021 -0.00267944 -0.0338943 / 0.78)` — 9× on 2 route(s)
- `oklab(0.896644 0.0000431035 -0.00102706)` — 1× on 1 route(s)

**Type step** (8 distinct)
- `14px/600/Schibsted Grotesk` — 193× on 7 route(s)
- `19px/400/Source Sans 3` — 46× on 7 route(s)
- `19px/700/Schibsted Grotesk` — 30× on 3 route(s)
- `14px/400/Source Sans 3` — 27× on 7 route(s)
- `27px/600/Schibsted Grotesk` — 13× on 6 route(s)
- `43px/600/Schibsted Grotesk` — 6× on 4 route(s)
- `62px/600/Schibsted Grotesk` — 3× on 3 route(s)
- `19px/600/Schibsted Grotesk` — 1× on 1 route(s)

**Radius** (1 distinct)
- `50px` — 9× on 2 route(s)

**Shadow** (0 distinct)

## Per route

| route | landmarks | h1 | focusable | console errors |
|---|---|---|---|---|
| http://127.0.0.1:8124/jurnal/ | header,nav,main,footer | 1 | 29 | 0 |
| http://127.0.0.1:8124/jurnal/perkhidmatan.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/jurnal/kerja.html | header,nav,main,footer | 1 | 24 | 0 |
| http://127.0.0.1:8124/jurnal/cara.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/jurnal/tentang.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/jurnal/syarikat.html | header,nav,main,footer | 1 | 17 | 0 |
| http://127.0.0.1:8124/jurnal/kontak.html | header,nav,main,footer | 1 | 21 | 0 |

## WARN
- no disabled control appeared on any route — the disabled state is probably undesigned, not absent
