# DESIGN.md — Bina Haus, arah 04 "Jurnal Tapak"

> Token spec rasmi (normatif, lulus `@google/design.md lint` tanpa error atau warning): `../DESIGN.md`
> — bersama eksport `../tailwind.theme.json` dan `../tokens.json`.
> Fail ini pula kontrak prosa: sebab setiap keputusan, dan dari mana setiap fail datang.

## Apa yang datang dari pemilik, dan apa yang aku tambah

| perkara | sumber |
|---|---|
| lima warna | `styles-BIzBvBjK.css` laman pemilik: `beige`, `beige-soft`, `navy-deep`, `navy`, `gold` |
| fon | Schibsted Grotesk + Source Sans 3, diambil dari Google Fonts dan dihoskan sendiri sebagai woff2 |
| logo | fail PNG pemilik sendiri, tiga saiz; **tidak pernah dilukis semula**, hanya diletak di atas plat gelapnya sendiri |
| semua teks | verbatim dari binahaus.com — lima langkah, tujuh kerja renovasi, tiga kerja pembinaan, teks tentang, tagline, CTA, WhatsApp +60 11-1124 4636 |
| semua gambar & video | aset pemilik sendiri, disalin dari `binahaus.com` (lihat provenance di bawah) |
| label bilik/kronologi | **aku** — bukan pemilik: susunan lima fasa mengikut langkah pemilik sendiri |

## Provenance setiap aset

Semua fail dalam `assets/img/` ialah salinan **bit-identik-nama** daripada aset pemilik: nama fail
dikekalkan seperti di laman asalnya, hanya saiz semula dikecilkan dan JPEG dienkod semula (q84,
progressive, metadata dibuang). Jadual provenance penuh — termasuk URL sumber bagi setiap satu daripada
26 fail, dan dua video yang disertakan — ada dalam `../../rumah/design/DESIGN.md`; fail di sini
ialah salinan yang sama (nama fail sama, saiz sama). Logo dalam `assets/logo/` ialah fail pemilik
`bina-haus-logo.png`, hanya dipangkas margin lutsinar dan dikecilkan.

Lima video berat (`work-video-3` hingga `work-video-7`) **tidak** disertakan: halaman memainkannya
terus dari URL pemilik sendiri, yang menjawab `206 video/mp4` kepada permintaan julat.

## Sistem token (ringkas — spec penuh dalam `../DESIGN.md`)

- Ground: sand `oklch(89.88% .0298 80.65)`; raised: paper `oklch(97.96% .0057 84.57)`.
- Ink: navy-deep `oklch(20.21% .034 265.48)`; satu jalur gelap setiap halaman: navy `oklch(28.83% .0503 265.9)`.
- Aksen: gold `oklch(74.04% .0992 86.94)` — **hiasan sahaja** (garis, underline halaman semasa).
- Aksen sebagai teks: `accent-ink` `oklch(48.2% .03 84)` — 4.79:1 pada sand. Nombor fasa guna ini.
- Skala huruf: `--s1` .875rem hingga `--s6` clamp(2.1rem…3.9rem); setiap saiz komponen mengambil
  token, bukan nilai rem ad-hoc (ini yang mengurangkan 13 langkah huruf kepada 9).
- Bentuk: 0 radius di mana-mana; satu bulatan sahaja — butang main video 56px.

## Yang pemeriksa tangkap, dan apa yang aku buat

| pemeriksa | dapatan | tindakan |
|---|---|---|
| impeccable | `skipped-heading` — `h1` → `h3` pada halaman Cara Kami Kerja | tajuk fasa jadi `h2` |
| sapuan kontras | `01` fasa pada sand: **1.71:1** | `accent-ink` diperkenalkan; kini 4.79:1 |
| sapuan kontras | butang "Get free Quotations" di halaman Contact: **ratio 1** (teks dan latar sama warna) | `.prose a:not(.btn)` — peraturan pautan prosa tidak lagi mengecat butang |
| sasaran sentuh | pautan prosa dan logo header di bawah 44px | `inline-block` + `min-height`, diukur semula dengan `elementFromPoint`: 0 bawah 44px |
| systemscan | varian pautan/butang melebihi bajet; saiz huruf bertaburan | keluarga pautan disatukan (nav/menu/footer/rail satu cap jari), saiz komponen dipindah ke token |
