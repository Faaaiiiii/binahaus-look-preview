# DESIGN.md — Bina Haus, arah 07 "Serambi"

> Token spec rasmi (normatif, lulus `@google/design.md lint` tanpa error atau warning):
> `../DESIGN.md` — bersama eksport `../tailwind.theme.json` dan `../tokens.json`.
> Fail ini kontrak prosa: sebab setiap keputusan, dari mana setiap fail datang, dan apa yang
> pemeriksa tangkap sebelum ia sampai kepada pemilik.

## Rujukan yang dibaca dahulu (arahan tetap pemilik: cari rujukan sampai jumpa)

| fail | apa yang diambil daripadanya |
|---|---|
| `popular-web-designs/templates/airbnb.md` | dunia "residential warmth": fotografi dahulu, putih hangat sebagai kanvas, radius lembut (8/14/20–32px), bayang tiga lapis (ring + blur lembut + blur kuat), teks hampir hitam **hangat** (`#222`), bukan hitam sejuk |
| `popular-web-designs/templates/apple.md` | bahagian Navigation & Typography: kekangan, tangga saiz yang jelas, tajuk navigasi besar |
| `impeccable/reference/craft-floor.md` | kontras ≥4.5:1; "kumpulan rapat, pemisahan lapang"; measure 65–75ch; gerakan = satu momen authored dengan ease-out eksponen; tema permukaan pelayar |
| `impeccable/reference/adapt.md` | telefon: hamburger + drawer penuh skrin |

## Apa yang datang dari pemilik, dan apa yang aku tambah

| perkara | sumber |
|---|---|
| lima warna | `styles-BIzBvBjK.css` laman pemilik: `beige-soft`, `beige`, `navy-deep`, `gold` (dan `navy` sebagai sumber campuran) |
| logo | fail PNG pemilik sendiri; **tidak dilukis semula**, duduk atas plat navy-deepnya sendiri |
| semua teks | verbatim dari binahaus.com — lima langkah, tujuh kerja renovasi, tiga kerja pembinaan, teks tentang, tagline, ajakan, WhatsApp +60 11-1124 4636 |
| semua gambar & video | aset pemilik sendiri (26 fail; lima video berat distrim dari URL pemilik) |
| label bilik/kronologi | **aku** — bukan pemilik: susunan babak halaman mengikut cara orang melawat rumah |

## Provenance aset

Semua fail dalam `assets/img/` ialah salinan aset pemilik dengan nama fail asal dikekalkan;
jadual provenance penuh (URL sumber bagi setiap fail) ada dalam `../../rumah/design/DESIGN.md`
dan fail di sini ialah salinan yang sama. Logo dalam `assets/logo/` ialah `bina-haus-logo.png`
pemilik, hanya dipangkas margin lutsinar dan dikecilkan. Fon (Petrona + DM Sans, variable,
woff2) dimuat turun dari Google Fonts dan dihoskan sendiri — tiada CDN dalam halaman.

## Kontras yang diukur (bukan dianda)

- Dakwat `rgb(28, 33, 47)` di atas tanah `#faf8f4` — jauh melebihi 4.5:1.
- Dakwat sekunder `#665c4a`: **6.19:1** di atas tanah, **4.85:1** di atas blok beige.
- Emas `#c6a75e` **tidak pernah** jadi teks: ia garis lantai dan tanda halus sahaja.

## Yang pemeriksa tangkap, dan apa yang aku betulkan

| pemeriksa | dapatan | tindakan |
|---|---|---|
| pandangan mata (tangkap penuh) | blok ajakan navy kelihatan KOSONG | bukan cacat: keadaan animasi `animation-timeline: view()` dalam tangkapan halaman penuh. Diukur dalam viewport sebenar: teks ada, `rgb(250,248,244)` di atas `rgb(15,22,38)`, opacity 1 |
| pandangan mata (tangkap penuh) | dua jubin video kelihatan gelap/kosong | bukan cacat: pengukuran pertama tersalah baca `<video>` (`display:none` sebelum ditekan). Diukur semula: bingkai 171×214, butang 171×214, poster 171×214 dan dimuat |
| ukuran bingkai (390px) | kad perkhidmatan bertindan: kapsyen tercicir KELUAR dari baris (timbul lubang berbentuk L, kapsyen 132px di bawah gambar) | `.door figure{ display:contents }` supaya bingkai dan kapsyennya jadi item grid kad; kini baris padat: gambar 132×132 kiri, label + cip + meta kanan |
| ukuran bingkai (1440px) | tiga kad perkhidmatan sama saiz (382×583) — tiada lagi berbagi saiz | disahkan selepas pembetulan |
