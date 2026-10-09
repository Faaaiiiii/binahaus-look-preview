# Product

<!-- impeccable:product-schema 1 -->

## Platform

web

<!-- Stack: an existing codebase already answers it — static HTML/CSS, no framework, no CDN,
     fonts self-hosted. Not restated here. -->

## Users

Ketua pengguna ( **diandaikan dari laman pemilik**, belum disahkan ): pemilik rumah kediaman di
Malaysia yang mahu renovasi atau membina rumah, dan yang sedang menimbang antara beberapa
kontraktor. (Catatan mekanikal: borang tiga soalan dipulangkan dengan status `cancelled` tanpa
jawapan, jadi tiada jawapan pemilik direkod di sini.) Laman pemilik turut menyebut pejabat dan
premis komersial; mana yang utama masih **keputusan terbuka**.

## Product Purpose

Laman ini ialah **pratonton rupa baharu** untuk binahaus.com — bukan laman rasmi, bukan pengganti,
tiada DNS atau deploy ke laman hidup. Ia wujud supaya pemilik dapat menilai arah rupa sebelum
sesuatu diubah pada laman sebenar. Makna berjaya: pemilik memilih satu arah, atau menyatakan apa
yang perlu diubah, dan tiada fakta syarikat yang perlu dibetulkan kemudian.

## Positioning

Laman pemilik sendiri mendakwa: *One team. One project. One responsibility.* — satu pasukan dari
konsultasi sampai serah. Dakwaan itu diterbitkan di binahaus.com dan dalam laman ini **verbatim**.
Yang **belum disahkan**: apa sebenarnya yang paling membezakan Bina Haus daripada kontraktor lain
(pasukan sendiri lawan sub-kontrak, reka-dan-bina dalam satu rumah, kelajuan, harga). Ini keputusan
terbuka yang mengubah tulang setiap halaman.

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
- **Keputusan terbuka:** alamat premis, e-mel rasmi, nombor pendaftaran syarikat, tahun mula,
  kawasan perkhidmatan, nama dan lokasi projek, testimoni. Laman pemilik tidak menerbitkan satu
  pun, jadi tiada satu pun direka; baris berkaitan dicetak *belum diterbitkan*.

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
