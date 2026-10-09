# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

<!-- Stack: an existing codebase already answers it — static HTML/CSS, no framework, no CDN,
     fonts self-hosted. Not restated here. -->

## Users

**Disahkan oleh Fairuz (9 Okt 2026)**, verbatim: *"Ni audience aku iaitu siapa yg nak buat rumah
lah."* — orang yang mahu **membuat/membina rumah** (pemilik rumah). Laman pemilik juga menyebut
pejabat dan premis komersial, tetapi itu bukan audiens utama; ia kekal dalam teks kerana teks
pemilik tidak boleh diubah.

## Product Purpose

Laman ini ialah **pratonton rupa baharu** untuk binahaus.com — bukan laman rasmi, bukan pengganti,
tiada DNS atau deploy ke laman hidup. Ia wujud supaya pemilik dapat menilai arah rupa sebelum
sesuatu diubah pada laman sebenar. Makna berjaya: pemilik memilih satu arah, atau menyatakan apa
yang perlu diubah, dan tiada fakta syarikat yang perlu dibetulkan kemudian.

## Positioning

**Disahkan oleh Fairuz (9 Okt 2026)**, verbatim: *"Mudah untuk deal."*

Itulah pembezaan sebenar — bukan slogan. Maksud kerjaan untuk halaman: kurangkan geseran pada
setiap titik keputusan. Satu saluran (WhatsApp), satu pasukan sepanjang projek, proses lima langkah
yang dinyatakan, tiada borang berlapis, tiada harga berteka-teki. Teks pemilik sendiri yang
menyokong ini dan mesti dikekalkan verbatim: *One team. One project. One responsibility.* dan
*From consultation and site visit to construction and handover, you know who you're dealing with at
every stage.* Jangan gantikan dengan slogan baharu — pemilik tidak berkata begitu dan teksnya tidak
boleh diubah.

## Operating Context

- Sumber kebenaran produk dan visual ialah **binahaus.com** (React app; aset di `/__l5e/assets-v1/`).
- Satu-satunya saluran hubungan yang pemilik terbitkan ialah **WhatsApp +60 11-1124 4636** dan
  nama domain. Tiada borang, tiada e-mel awam, tiada harga.
- Media kerja pemilik: 13 gambar galeri, 5 render 3D, 7 poster video (dan 7 video, 5 daripadanya
  berat dan dimainkan terus dari URL pemilik).
- Kerja dijalankan sebagai repo pratonton berasingan (`binahaus-look-preview`) dengan satu folder
  setiap arah (`/`, `/db/`, `/rumah/`), diterbitkan melalui GitHub Pages.

## Capabilities and Constraints

- Laman ini **tidak** menerbitkan harga, jadual, atau janji tempoh — laman pemilik pun tidak.
- Semua teks syarikat adalah **verbatim** dari binahaus.com; menulis semula adalah dilarang oleh
  pemilik.
- Ketujuh-tujuh halaman dijana oleh `bina.py` (satu shell) supaya header, menu dan footer tidak
  boleh lari antara halaman.
- **Butiran syarikat = apa yang ada di laman.** Disahkan oleh Fairuz (9 Okt 2026), verbatim:
  *"Yg kat dalam website tu lah bukti butiran."* Jadi tiada butiran tambahan akan datang daripada
  pihaknya buat masa ini: apa yang binahaus.com terbitkan itulah set lengkapnya. Baris alamat,
  e-mel dan nombor pendaftaran kekal *belum diterbitkan* — dan itu betul, bukan kekurangan yang
  perlu diisi dengan andaian.

## Brand Commitments

Dinyatakan oleh pemilik secara lisan, jadi ia mengikat:

- **Logo tidak boleh diubah.** Fail pemilik digunakan apa adanya (hanya margin lutsinar dipangkas
  dan saiz dikecilkan untuk web).
- **Warna boleh diubah.**
- **Teks penting tidak boleh diubah**, khususnya butiran berkaitan syarikat.
- Semua imej dan video mesti aset pemilik sendiri; tiada imej dijana atau diambil dari tempat lain.

## Evidence on Hand

- `rumah/assets/img/` — 26 aset pemilik (gambar, render, poster, dua video ringan), provenance penuh
  dalam `rumah/design/DESIGN.md`.
- `rumah/assets/logo/` — logo pemilik, tiga saiz.
- Salinan verbatim laman pemilik dikumpul semasa recon; keputusan reka bentuk direkodkan dalam
  `rumah/design/COMMIT-SHEET.md` dan `rumah/design/DESIGN.md`.

## What future work must not do

- Jangan reka alamat, e-mel, nombor pendaftaran, tahun, kawasan, nama projek, angka atau testimoni.
- Jangan tulis semula teks pemilik.
- Jangan gantikan logo.
- Jangan tandakan kerja ini sebagai laman rasmi; ia pratonton, dan footer menyatakannya.
