# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

<!-- Stack: static HTML/CSS, no framework, no CDN, fonts self-hosted. Not restated here. -->

## Users

**Disahkan oleh Fairuz (9 Okt 2026)**, verbatim: *"Ni audience aku iaitu siapa yg nak buat rumah
lah."* — orang yang mahu **membuat/membina rumah** (pemilik rumah). Laman pemilik juga menyebut
pejabat dan premis komersial, tetapi itu bukan audiens utama; ia kekal dalam teks kerana teks
pemilik tidak boleh diubah.

## Product Purpose

Laman ini ialah **pratonton rupa baharu** untuk binahaus.com — bukan laman rasmi, bukan pengganti,
tiada DNS atau deploy ke laman hidup. Ia wujud supaya pemilik dapat menilai arah rupa sebelum
sesuatu diubah pada laman sebenar. Arah ini, **arah 06 "PITA"**, membentangkan kerja pemilik
sebagai **rakaman**: setiap bab dipimpin video atau poster video, dengan irama pita filem yang
tertahan. Makna berjaya: pemilik memilih satu arah, atau menyatakan apa yang perlu diubah, dan
tiada fakta syarikat yang perlu dibetulkan kemudian.

## Positioning

**Disahkan oleh Fairuz (9 Okt 2026)**, verbatim: *"Mudah untuk deal."* — itu pembezaan sebenar, bukan
slogan. Halaman mengurangkan geseran pada setiap titik keputusan: satu saluran (WhatsApp), satu
pasukan sepanjang projek, proses lima langkah, tiada borang berlapis. Teks pemilik yang menyokong ini
kekal verbatim: *One team. One project. One responsibility.* dan *From consultation and site visit to
construction and handover, you know who you're dealing with at every stage.*

## Operating Context

- Sumber kebenaran produk dan visual ialah **binahaus.com** (React app; aset di `/__l5e/assets-v1/`).
- Satu-satunya saluran hubungan yang pemilik terbitkan ialah **WhatsApp +60 11-1124 4636** dan nama
  domain. Tiada borang, tiada e-mel awam, tiada harga.
- Media kerja pemilik: 13 gambar galeri, 5 render 3D, 7 poster video (dan 7 video, 5 daripadanya
  berat dan dimainkan terus dari URL pemilik).
- Arah ini ialah folder `pita/` dalam repo pratonton `binahaus-look-preview`.

## Capabilities and Constraints

- Laman ini **tidak** menerbitkan harga, jadual, atau janji tempoh — laman pemilik pun tidak.
- Semua teks syarikat adalah **verbatim** dari binahaus.com; menulis semula adalah dilarang.
- Ketujuh-tujuh halaman dijana oleh `pita/bina.py` (satu shell) supaya header, menu dan footer tidak
  boleh lari antara halaman.
- **Butiran syarikat = apa yang ada di laman** (*"Yg kat dalam website tu lah bukti butiran."*). Baris
  alamat, e-mel dan nombor pendaftaran kekal *belum diterbitkan* — dan itu betul, bukan kekurangan.

## Brand Commitments

- **Logo tidak boleh diubah.** Fail pemilik digunakan apa adanya (hanya margin lutsinar dipangkas).
- **Warna boleh diubah** — di sini warna pemilik sendiri yang digunakan: navy sebagai tanah, beige-soft
  sebagai jenis, emas sekali sahaja.
- **Teks penting tidak boleh diubah.**
- Semua imej dan video mesti aset pemilik sendiri; tiada imej dijana atau diambil dari tempat lain.
- **Jenis baru dipilih, bukan diambil dari laman pemilik:** Barlow Semi Condensed × Newsreader
  (self-hosted woff2) — bukan Archivo/Manrope (arah 03) dan bukan Literata/Hanken (arah 02).

## Evidence on Hand

- `assets/img/` — 28 aset pemilik (gambar, render, poster, dua video ringan); provenance penuh dalam
  `design/DESIGN.md`.
- `assets/logo/` — logo pemilik, tiga saiz. `assets/fonts/` — dua keluarga woff2, self-hosted.
- Keputusan reka bentuk direkodkan dalam `design/COMMIT-SHEET.md` dan `design/DESIGN.md`.

## What future work must not do

- Jangan reka alamat, e-mel, nombor pendaftaran, tahun, kawasan, nama projek, angka atau testimoni.
- Jangan tulis semula teks pemilik.
- Jangan gantikan logo.
- Jangan tandakan kerja ini sebagai laman rasmi; ia pratonton, dan footer menyatakannya.
- Jangan salin Archivo/Manrope, navy-deep sebagai tanah, atau animasi pintu arah 03.
