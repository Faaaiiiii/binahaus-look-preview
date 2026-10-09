#!/usr/bin/env python3
"""Bina Haus — arah 04 "JURNAL TAPAK". Seven pages from one shell.

The owner's own five process steps are the spine of the site: consultation, site visit,
quotations, construction, handover. His own photographs hang off that spine, each labelled
by what it is (Proses / Siap / Render) — never dated, never claimed to be one project.

    python3 bina.py
"""
import pathlib

HERE = pathlib.Path(__file__).parent
WA = "https://wa.me/601111244636"
SITE = "https://binahaus.com/"

NAV = [
    ("perkhidmatan.html", "Services"),
    ("kerja.html", "Our Work"),
    ("cara.html", "Cara Kami Kerja"),
    ("tentang.html", "About Us"),
    ("syarikat.html", "Profil Syarikat"),
    ("kontak.html", "Contact"),
]

STEPS = [
    (1, "Consultation", "We start by understanding what you need and the scope of your project."),
    (2, "Site Visit", "Our team visits the site to assess the space and understand the work required."),
    (3, "Quotations", "You receive a quotation based on the agreed scope of work."),
    (4, "Construction", "Once everything is agreed, our team begins the work on site."),
    (5, "Handover", "When the work is completed, we hand the finished project over to you."),
]

RENO = [
    (1, "Full house Renovation", "Give your existing home a complete transformation and a fresh new feel."),
    (2, "Kitchen renovations", "Upgrade your kitchen into a space that works better for everyday living."),
    (3, "Extension", "Create the additional space you need within your existing property."),
    (4, "Flooring", "Refresh your space from the ground up with properly installed flooring."),
    (5, "Plaster Ceiling", "Give your interior a cleaner and more refined finish."),
    (6, "Painting", "Refresh the look and feel of your space with a new finish."),
    (7, "Electrical &amp; Plumbing", "Essential electrical and plumbing works for your renovation project."),
]
BUILD = [
    (1, "New house Constructions", "Building your new home from the ground up."),
    (2, "House Extension", "Add the extra space your home needs as your needs grow."),
    (3, "Structural Works", "Structural works required for your construction project."),
]

# each chapter of the diary, with the owner's own photographs and an honest label
PHASES = {
    1: [("about-team.jpg", "Proses", "Konsultasi dan pelan di atas meja", 1400, 1050)],
    2: [("work-photo-2.jpg", "Siap belum", "Kerja luaran, scaffold", 960, 1280),
        ("work-photo-8.jpg", "Proses", "Kerja plaster, dinding bata", 960, 1280)],
    3: [("work-render-2.jpg", "Render", "Kitchen — reka bentuk 3D", 960, 1280),
        ("work-render-5.jpg", "Render", "Living Area — reka bentuk 3D", 960, 1280)],
    4: [("construction-site.jpg", "Proses", "Rumah dua tingkat dalam pembinaan", 1600, 1000),
        ("reno-progress.jpg", "Proses", "Kerja dalaman: rasuk siling", 1040, 1300),
        ("work-photo-6.jpg", "Proses", "Tapak kerja, kayu di lantai", 960, 1280),
        ("work-photo-5.jpg", "Siap", "Ruang kosong, lantai kayu", 960, 1280)],
    5: [("hero-living.jpg", "Siap", "Ruang tamu, kerja siap", 1800, 1200),
        ("reno-kitchen.jpg", "Siap", "Dapur, kerja siap", 1040, 1300),
        ("reno-detail.jpg", "Siap", "Butiran lantai dan skirting", 1200, 900)],
}

VIDEOS = {
    1: ("assets/img/work-video-1.mp4", "Unit dalam kerja, kaca &amp; pelindung"),
    2: ("assets/img/work-video-2.mp4", "Unit komersial, partition kaca"),
    3: ("https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4", "Jubin lantai"),
    4: ("https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4", "Lantai &amp; skirting"),
    5: ("https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4", "Pintu &amp; dinding"),
    6: ("https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4", "Kerja hacking &amp; perobohan"),
    7: ("https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4", "Jubin lantai &amp; dinding"),
}

GALLERY = [
    ("img", "work-photo-1.jpg", "Bangunan sedia ada, kerja luaran"),
    ("video", 1), ("img", "work-photo-3.jpg", "Ruang dalaman, tingkap besar"),
    ("render", "work-render-1.jpg", "Dry Kitchen"), ("video", 2),
    ("img", "work-photo-2.jpg", "Kerja luaran, scaffold"), ("img", "work-photo-4.jpg", "Ruang dalaman, lantai kayu"),
    ("video", 3), ("render", "work-render-3.jpg", "Living and Dining"), ("img", "work-photo-6.jpg", "Tapak kerja, kayu di lantai"),
    ("video", 5), ("img", "work-photo-5.jpg", "Ruang kosong, lantai kayu"), ("render", "work-render-4.jpg", "Walk-in Wardrobe"),
    ("video", 6), ("img", "work-photo-8.jpg", "Kerja plaster, dinding bata"), ("render", "work-render-5.jpg", "Living Area"),
    ("video", 7), ("img", "work-photo-7.jpg", "Ruang kosong, lantai kayu"), ("render", "work-render-2.jpg", "Kitchen"),
    ("video", 4),
]


def head(title, desc, active):
    cur = ' aria-current="page"'
    links = "\n".join('        <a href="%s"%s>%s</a>' % (h, cur if h == active else "", l) for h, l in NAV)
    menu = "\n".join('          <a href="%s"%s>%s</a>' % (h, cur if h == active else "", l) for h, l in NAV)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="BINA HAUS">
<meta name="theme-color" content="#e6ddc9">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/logo/bina-haus-logo-160.png">
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/schibsted-grotesk-700-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/source-sans-3-400-latin.woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="hdr">
  <div class="wrap hdr__in">
    <a class="mark" href="index.html" aria-label="Bina Haus — utama">
      <img src="assets/logo/bina-haus-logo-320.png" alt="BINA HAUS" width="320" height="312">
    </a>
    <div class="navwrap" id="navwrap">
      <nav class="nav" aria-label="Utama">
{links}
      </nav>
      <button class="burger" type="button" aria-expanded="false" aria-controls="menu">Menu</button>
      <div class="menu" id="menu" hidden>
        <nav aria-label="Menu">
{menu}
          <a class="menu__wa" href="{WA}">WhatsApp +60 11-1124 4636</a>
        </nav>
        <p class="menu__tag">Ruang dibina dengan rasa</p>
      </div>
    </div>
  </div>
</header>
"""


def foot():
    items = "\n".join('        <li><a href="%s">%s</a></li>' % (h, l) for h, l in NAV)
    return f"""
<footer class="ftr">
  <div class="wrap ftr__in">
    <div>
      <img class="ftr__mark" src="assets/logo/bina-haus-logo-320.png" alt="BINA HAUS" width="320" height="312">
      <p class="ftr__tag">Ruang dibina dengan rasa</p>
      <p class="ftr__site"><a href="{SITE}">binahaus.com</a></p>
    </div>
    <div>
      <p class="ftr__label">Contact</p>
      <ul><li><a href="{WA}">WhatsApp +60 11-1124 4636</a></li><li><a href="kontak.html">Contact</a></li></ul>
    </div>
    <div>
      <p class="ftr__label">Navigation</p>
      <ul>
{items}
      </ul>
    </div>
  </div>
  <div class="wrap ftr__bar">
    <span>© 2026 Bina Haus. All rights reserved.</span>
    <span>Look preview: arah 04, bukan laman rasmi.</span>
  </div>
</footer>

<script src="assets/app.js" defer></script>
</body>
</html>
"""


def photo_card(img, kind, cap, w, h):
    return f"""      <figure class="ph">
        <img src="assets/img/{img}" alt="{cap}" width="{w}" height="{h}" loading="lazy" decoding="async">
        <figcaption><span class="ph__kind">{kind}</span>{cap}</figcaption>
      </figure>"""


def phase_block(n, title, desc, body_extra=""):
    cards = "\n".join(photo_card(*p) for p in PHASES.get(n, []))
    return f"""  <li class="fp" id="fasa-{n}">
    <div class="fp__hd">
      <span class="fp__n">{n:02d}</span>
      <h2>{title}</h2>
      <p>{desc}</p>
    </div>
    <div class="fp__body">
      <div class="ph-grid">{cards}</div>
{body_extra}    </div>
  </li>"""


def works(items):
    return '      <ul class="works">\n' + "\n".join(
        '        <li><span class="n">%02d</span><div><b>%s</b><p>%s</p></div></li>' % (n, t, d) for n, t, d in items
    ) + "\n      </ul>"


def tile(kind, a, b=None):
    if kind == "img":
        return f"""      <li><figure><div class="ph__fr"><img src="assets/img/{a}" alt="{b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption><span class="ph__kind">Foto</span>{b}</figcaption></figure></li>"""
    if kind == "render":
        return f"""      <li><figure><div class="ph__fr"><img src="assets/img/{a}" alt="Render reka bentuk: {b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption><span class="ph__kind">Render</span>{b}</figcaption></figure></li>"""
    src, cap = VIDEOS[a]
    return f"""      <li class="wk--video"><figure><div class="ph__fr">
        <video src="{src}" poster="assets/img/work-poster-{a}.jpg" controls playsinline preload="none"></video>
        <button class="wk__play" type="button" aria-label="Main video: {cap}">
          <img src="assets/img/work-poster-{a}.jpg" alt="Pratonton video: {cap}" width="787" height="1400" loading="lazy" decoding="async">
          <span class="wk__btn" aria-hidden="true"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2 1.2 14 8 2 14.8Z" fill="currentColor"/></svg></span>
        </button></div><figcaption><span class="ph__kind">Video</span>{cap}</figcaption></figure></li>"""


def gallery(limit=None):
    items = GALLERY[:limit] if limit else GALLERY
    out = [tile("img", a, b) if k == "img" else (tile("render", a, b) if k == "render" else tile("video", a)) for k, a, b in
           [(x[0], x[1], x[2] if len(x) > 2 else None) for x in items]]
    return '    <ul class="wk">\n' + "\n".join(out) + "\n    </ul>"


def band(title, lead, img=None, alt=None, kind=None):
    if img:
        return f"""
<section class="band">
  <figure class="band__media">
    <img src="assets/img/{img}" alt="{alt}" loading="eager" decoding="async">
    <figcaption class="band__plate"><h1>{title}</h1><span class="ph__kind">{kind}</span></figcaption>
  </figure>
  <div class="wrap"><p class="band__lead">{lead}</p></div>
</section>
"""
    return f"""
<section class="band">
  <div class="wrap band__in"><h1>{title}</h1><p class="band__lead">{lead}</p></div>
</section>
"""


def write(name, body):
    (HERE / name).write_text(body, encoding="utf-8")
    print("wrote", name, len(body), "bytes")


INDEX = """
<main id="main">

<section class="hero">
  <img class="hero__photo" src="assets/img/hero-living.jpg" alt="Ruang tamu selepas kerja siap: sofa, console TV dan tingkap besar" width="1800" height="1200" fetchpriority="high" decoding="async">
  <div class="wrap hero__in">
    <p class="hero__kicker">Ruang dibina dengan rasa</p>
    <h1>Renovation and construction for homes, offices and commercial spaces.</h1>
    <p class="hero__lede">From the first consultation to the final handover, Bina Haus brings your project together under one team.</p>
    <div class="hero__cta">
      <a class="btn" href="kontak.html">Get free Quotation</a>
      <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
    </div>
  </div>
</section>

<section class="rail-intro">
  <div class="wrap">
    <h2>Lima langkah, satu jurnal</h2>
    <p class="prose">Setiap projek Bina Haus bergerak melalui lima langkah yang sama. Halaman-halaman ini menyusun kerja syarikat mengikut urutan itu — gambar sebenar daripada tapak, dilabel mengikut apa yang benar-benar ditunjukkannya.</p>
    <ol class="rail">
""" + "\n".join(
    f'      <li><span class="rail__n">{n:02d}</span><a href="cara.html#fasa-{n}">{t}</a></li>' for n, t, d in STEPS
) + """
    </ol>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <h2>See the work for yourself.</h2>
    <p class="prose">A collection of work by Bina Haus.</p>
""" + gallery(6) + """
    <p class="more"><a class="btn btn--quiet" href="kerja.html">All work</a></p>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <h2>Planning to renovate your space?</h2>
    <p>Tell us what you need and let's start with a conversation.</p>
  </div>
</section>
<section class="cta__act">
  <div class="wrap cta__btns">
    <a class="btn" href="kontak.html">Get free Quotations</a>
    <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
  </div>
</section>

</main>
"""

SERVICES = """<main id="main">
""" + band("Services",
           "Whether you're renovating the whole house or improving specific parts of your space, Bina Haus handles the work with attention to detail from start to finish.",
           "work-photo-3.jpg", "Ruang dalaman siap: lantai kayu, tingkap besar dan langsir", "Siap") + """
<section class="sect">
  <div class="wrap">
    <h2>Renovations</h2>
""" + works(RENO) + """
  </div>
</section>

<section class="sect">
  <div class="wrap">
    <h2>Construction</h2>
    <p class="prose">Whether you're building a new house, extending your existing property or carrying out structural works, Bina Haus takes your project from planning to completion.</p>
""" + works(BUILD) + """
  </div>
</section>

<section class="sect sect--media">
  <div class="wrap">
    <h2>Dapur, dan butiran</h2>
    <div class="ph-grid ph-grid--3">
""" + photo_card("reno-kitchen.jpg", "Siap", "Dapur, kerja siap", 1040, 1300) + "\n" + \
    photo_card("reno-detail.jpg", "Siap", "Butiran lantai bertemu skirting", 1200, 900) + "\n" + \
    photo_card("work-render-2.jpg", "Render", "Kitchen — reka bentuk 3D", 960, 1280) + """
    </div>
  </div>
</section>
</main>
"""

WORK = """<main id="main">
""" + band("Hasil Kerja",
           "Every tile below is the owner's own asset, taken from binahaus.com and served from this page: photographs, 3D renders and video, each labelled by what it is.",
           "reno-progress.jpg", "Kerja dalaman dalam proses: rasuk kayu siling dan peralatan di lantai", "Proses") + """
<section class="sect">
  <div class="wrap">
""" + gallery() + """
    <p class="note">Media di atas ialah aset Bina Haus sendiri dari binahaus.com: gambar dan video kecil dihidangkan dari halaman ini, video besar dimainkan terus dari binahaus.com. Tiada nama, lokasi atau angka projek direka.</p>
  </div>
</section>
</main>
"""

PROCESS = """<main id="main">
""" + band("Cara Kami Kerja",
           "Satu proses yang jelas, dari mula sampai siap. A clear process from start to finish.") + """
<section class="sect">
  <div class="wrap">
    <ol class="fasa">
""" + "\n".join(phase_block(n, t, d) for n, t, d in STEPS) + """
    </ol>
    <p class="note">Gambar-gambar ini daripada kerja Bina Haus sendiri, tetapi ia bukan satu projek yang sama dan tiada tarikh. Setiap satu dilabel mengikut apa yang ditunjukkannya: <em>Proses</em> (kerja sedang berjalan), <em>Siap</em> (kerja selesai), <em>Render</em> (reka bentuk 3D).</p>
  </div>
</section>
</main>
"""

ABOUT = """<main id="main">
""" + band("About Us", "We build spaces for everyday life.",
           "hero-living.jpg", "Ruang tamu siap dengan sofa dan tingkap besar", "Siap") + """
<section class="sect">
  <div class="wrap twocol">
    <div class="prose">
      <p>Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.</p>
      <p>Our work ranges from full house renovations and individual renovation works to new house construction, house extensions and structural works.</p>
      <p>Whatever the scale of the project, our focus remains the same: Do the work properly. Keep the process clear. Deliver the space.</p>
    </div>
    <div class="prose">
      <h2>One team. One project. One responsibility.</h2>
      <p>Renovation and construction can involve many moving parts.</p>
      <p>With Bina Haus, you have one team to communicate with throughout the project.</p>
      <p>From consultation and site visit to construction and handover, you know who you're dealing with at every stage.</p>
      <p>One project. One point of responsibility.</p>
    </div>
  </div>
</section>
<section class="sect sect--media">
  <div class="wrap">
    <div class="ph-grid ph-grid--2">
""" + photo_card("about-team.jpg", "Proses", "Pasukan meneliti pelan di tapak", 1400, 1050) + "\n" + \
    photo_card("construction-site.jpg", "Proses", "Rumah dua tingkat dalam pembinaan", 1600, 1000) + """
    </div>
    <p class="quote">Ruang dibina dengan rasa</p>
    <p class="prose">Because a space is more than walls, floors and finishes. It's where people live, work and spend their everyday lives.</p>
    <p class="prose">So when we build or renovate a space, the work should feel considered from beginning to end.</p>
  </div>
</section>
</main>
"""

COMPANY = """<main id="main">
""" + band("Profil Syarikat",
           "Everything the company publishes about itself, on one plate: read from binahaus.com, nothing filled in, estimated or invented.") + """
<section class="sect">
  <div class="wrap">
    <div class="plaque">
      <div class="plaque__hd"><h2>BINA HAUS — Ruang dibina dengan rasa</h2></div>
      <dl>
        <div class="row"><dt>Nama syarikat</dt><dd>Bina Haus<small>Seperti yang dipaparkan di binahaus.com</small></dd></div>
        <div class="row"><dt>Bidang</dt><dd>Renovation and construction<small>Homes, offices and commercial spaces</small></dd></div>
        <div class="row"><dt>Skop kerja: renovasi</dt><dd>Full house renovation · Kitchen renovations · Extension · Flooring · Plaster ceiling · Painting · Electrical &amp; plumbing<small>7 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Skop kerja: pembinaan</dt><dd>New house construction · House extension · Structural works<small>3 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Proses</dt><dd>Consultation → Site visit → Quotations → Construction → Handover<small>Lima langkah, sama pada setiap projek</small></dd></div>
        <div class="row"><dt>Cara kami bekerja</dt><dd>One team. One project. One responsibility.<small>Satu pasukan dari konsultasi sampai serah</small></dd></div>
        <div class="row"><dt>Hubungan</dt><dd>WhatsApp +60 11-1124 4636<br>binahaus.com<small>Satu-satunya saluran yang diterbitkan di laman</small></dd></div>
        <div class="row"><dt>Alamat · E-mel · Pendaftaran</dt><dd>Belum diterbitkan<small>Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat. Tidak diisi di sini supaya tiada butiran palsu.</small></dd></div>
      </dl>
      <p class="plaque__ft">Profil ini dibaca terus daripada binahaus.com. Kalau ada butiran yang patut muncul di laman (alamat, e-mel, nombor pendaftaran, tahun mula, kawasan perkhidmatan), beritahu sahaja — ia akan masuk sebagai fakta, bukan anggaran.</p>
    </div>
  </div>
</section>
</main>
"""

CONTACT = """<main id="main">
""" + band("Contact", "Tell us what you need and let's start with a conversation.") + """
<section class="sect">
  <div class="wrap twocol">
    <div class="prose">
      <h2>Planning to renovate your space?</h2>
      <p>Get free quotations, or send a message on WhatsApp with what you have in mind: the space, the work, and when you would like to start.</p>
      <div class="cta__btns">
        <a class="btn" href="https://wa.me/601111244636">Get free Quotations</a>
        <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
      </div>
    </div>
    <div class="prose">
      <p class="ftr__label">Saluran yang diterbitkan</p>
      <p>WhatsApp <a href="https://wa.me/601111244636">+60 11-1124 4636</a><br>Web <a href="https://binahaus.com/">binahaus.com</a></p>
      <p>Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat, jadi halaman ini tidak mereka-reka satu.</p>
    </div>
  </div>
</section>
</main>
"""

write("index.html", head("BINA HAUS — Jurnal Tapak", "Renovation and construction for homes, offices and commercial spaces. Ruang dibina dengan rasa.", "index.html") + INDEX + foot())
write("perkhidmatan.html", head("Services — BINA HAUS", "Renovations and construction: full house renovation, kitchen, extension, flooring, plaster ceiling, painting, electrical and plumbing; new house construction and structural works.", "perkhidmatan.html") + SERVICES + foot())
write("kerja.html", head("Hasil Kerja — BINA HAUS", "A collection of work by Bina Haus: photographs, 3D renders and video from the company's own site.", "kerja.html") + WORK + foot())
write("cara.html", head("Cara Kami Kerja — BINA HAUS", "Satu proses yang jelas, dari mula sampai siap: consultation, site visit, quotations, construction, handover.", "cara.html") + PROCESS + foot())
write("tentang.html", head("About Us — BINA HAUS", "Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.", "tentang.html") + ABOUT + foot())
write("syarikat.html", head("Profil Syarikat — BINA HAUS", "Company details as published on binahaus.com: field of work, scope, process and contact.", "syarikat.html") + COMPANY + foot())
write("kontak.html", head("Contact — BINA HAUS", "Tell us what you need and let's start with a conversation. WhatsApp +60 11-1124 4636.", "kontak.html") + CONTACT + foot())
print("\nseven pages written to", HERE)
