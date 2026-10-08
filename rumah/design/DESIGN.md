# DESIGN.md — Bina Haus, arah 03 "MASUK"

Everything in this page comes from the owner. Nothing was invented, and nothing that belongs to
the brand was redrawn: the logo is his own PNG file, the colours are read out of his stylesheet,
the typefaces are the pair his own site loads, the photographs and videos are his, and every
sentence of copy is his, verbatim.

## The contract

| decision | value | where it comes from |
|---|---|---|
| ground | `--navy-deep oklch(20.21% .034 265.48)` | his `styles-BIzBvBjK.css` |
| raised surface | `--navy oklch(28.83% .0503 265.9)` | same |
| type on navy | `--beige oklch(89.88% .0298 80.65)`, `--beige-soft oklch(97.96% .0057 84.57)` | same |
| the one accent | `--gold oklch(74.04% .0992 86.94)` | same — the logo's own flat gold measures `#D5A64C`, the same colour |
| display face | **Archivo** 600 | the face his site loads for display |
| text face | **Manrope** 400/500/600 | the face his site loads for body |
| logo | `assets/logo/bina-haus-logo*.png` | his `bina-haus-logo.png`, only the transparent margin trimmed and re-encoded |
| type scale | `--s1` .875rem → `--s6` clamp(2.4rem … 4.6rem), 1.25-ish steps | — |
| body measure | ≤ 68ch (`--line-h 1.62`) | — |
| spacing | `--pad clamp(1.25rem, 4.5vw, 4.5rem)`, `--gut clamp(1.5rem, 4vw, 3.5rem)` | — |

Gold is used for: the door's seam and threshold rule, the chapter numerals, the plaque rule and
the focus ring. It is the warm light of the house, not a decoration — no gold buttons, no gold
gradient text, no gold hairlines on every edge.

## What is mine, and what is his

- **His, verbatim:** every heading and paragraph shown (RENOVATION & CONSTRUCTION label, hero copy,
  renovations and construction copy, the 7 + 3 works, the 5 process steps, why-us, about, the
  closing statement, CTA, footer, WhatsApp number `+60 11-1124 4636`, `binahaus.com`).
- **Mine, and marked as such:** the room names that give the walk its chapters (*Ruang tamu, Dapur,
  Butiran, Tapak, Pasukan*), the kind chips (*Foto / Render / Video*), the threshold strip's layout,
  and two sentences of build note inside the Dapur and Butiran chapters that say plainly which tiles
  are renders.
- **Not on his site, so not on this page:** address, e-mail, company registration, founding year,
  service areas, project names or locations. The Profil Syarikat plate prints *belum diterbitkan*
  for those and says why. **Ask the owner before filling them.**

## Provenance — every image on the page

| file | served | size | source on the owner's site |
|---|---|---|---|
| `assets/img/about-team.jpg` | 1400×1050 | 144 KB | https://binahaus.com/assets/about-team-Cs38AnSZ.jpg |
| `assets/img/construction-site.jpg` | 1600×1000 | 359 KB | https://binahaus.com/assets/construction-site-NUuTsEpO.jpg |
| `assets/img/hero-living.jpg` | 1800×1200 | 183 KB | https://binahaus.com/assets/hero-living-Brqy9b4j.jpg |
| `assets/img/reno-detail.jpg` | 1200×900 | 87 KB | https://binahaus.com/assets/reno-detail-CTESX31o.jpg |
| `assets/img/reno-kitchen.jpg` | 1040×1300 | 125 KB | https://binahaus.com/assets/reno-kitchen-BYsCvji1.jpg |
| `assets/img/reno-progress.jpg` | 1040×1300 | 116 KB | https://binahaus.com/assets/reno-progress-cAki5mYk.jpg |
| `assets/img/work-photo-1..8.jpg` | 960–1050 wide | 88–197 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-photo-N.jpg` |
| `assets/img/work-render-1..5.jpg` | 960×1280 | 49–139 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-render-N.jpg` |
| `assets/img/work-poster-1..7.jpg` | 296–787 wide | 12–95 KB | `https://binahaus.com/__l5e/assets-v1/<id>/work-poster-N.jpg` |
| `assets/img/work-video-1,2.mp4` | 606 KB, 616 KB | — | `https://binahaus.com/__l5e/assets-v1/<id>/work-video-1,2.mp4` |
| `assets/logo/bina-haus-logo*.png` | 600/320/160 wide | 133/43/15 KB | `https://binahaus.com/__l5e/assets-v1/9dbffc53-…/bina-haus-logo.png` |

Re-encoding only: resized to a sensible web size, JPEG q84 progressive, metadata stripped. No
crop, no retouch, no colour grade, no generated imagery. The five heavy videos
(`work-video-3 … 7`, ≈58 MB) are **not** copied — the page plays them from the owner's own URLs,
which answered `206 video/mp4` to a range request when this was built.

## The five colours as they are actually used

| colour | role on the page |
|---|---|
| navy-deep | the ground of everything: header, chapters, footer, the door's panels |
| navy | the raised plate (Profil Syarikat), the CTA band, the gallery tile ground |
| beige | type: paragraphs, captions, chips |
| beige-soft | headings and the type that must carry weight |
| gold | the seam of the door, the threshold rule, chapter numerals, the plaque rule, focus ring |
