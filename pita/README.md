# PITA — arah 06 (the reel / the tape)

A video-led look for binahaus.com: the owner's own work presented as **footage**. Every chapter is
led by a video or a video poster, with a restrained film-adjacent treatment — full-bleed media,
running numerals, thin rules, minimal type — and the whole motion budget spent on one authored
moment: two of his own work videos crossfading slowly in the hero.

Static, self-contained, no framework, no CDN, fonts self-hosted, complete with JavaScript blocked.

## Pages (one shell — `bina.py`)

| file | what it carries |
|---|---|
| `index.html` | the reel (two videos crossfading), the three ways in, six tiles of work, the one-team promise, the CTA |
| `perkhidmatan.html` | Services: the 7 renovation works, the 3 construction works, and the Dapur / Butiran / Tapak chapters |
| `kerja.html` | Hasil Kerja: all 20 own media items, each labelled Foto / Render / Video |
| `cara.html` | Cara Kami Kerja: the 5 process steps |
| `tentang.html` | About Us |
| `syarikat.html` | Profil Syarikat — every detail the site publishes; unpublished fields read *belum diterbitkan* |
| `kontak.html` | Contact — the two ways to start |

## Files

- `bina.py` — the builder (writes all seven pages from one shell)
- `assets/style.css` · `assets/app.js` · `assets/fonts/` (Barlow Semi Condensed + Newsreader, woff2)
- `assets/img/` (28 owner assets) · `assets/logo/` (his own PNG)
- `design/COMMIT-SHEET.md` (the seven decisions) · `design/DESIGN.md` (contract + provenance + gates)
- `PRODUCT.md` (product truth) · `qa/` (frames at 390 / 768 / 1440)

Everything the pages say is the owner's copy, verbatim. Every image and video is his. Nothing is
invented. Run `python3 bina.py` to rebuild the seven pages.
