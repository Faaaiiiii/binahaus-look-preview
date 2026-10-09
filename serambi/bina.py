#!/usr/bin/env python3
"""Bina Haus — arah 07 "SERAMBI". Seven pages from one shell.

The owner's own house, walked room by room. Every section of the home page is one
room; a gold 2px floor line runs under each room and draws itself as the room is read.
His own photographs, renders and video hang off the rooms, each labelled by what it
is (Foto / Render / Proses / Video) — never dated, never claimed to be one project.

Type: DM Sans (UI/text) + Petrona (room names and large headings), self-hosted woff2.

    python3 bina.py
"""
import hashlib, pathlib
# Cop pelayar/CDN menahan CSS lama sampai 10 minit selepas setiap perubahan — pemilik
# nampak halaman lama walaupun terbitan sudah siap. Setiap binaan mengecap nama fail
# dengan cap jari kandungannya, jadi pelayar sentiasa tarik fail yang betul.
def cap(fail):
    try:
        return hashlib.sha1(pathlib.Path(fail).read_bytes()).hexdigest()[:8]
    except OSError:
        return '0'

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
MENU = [("index.html", "Utama")] + NAV

STEPS = [
    (1, "Consultation", "We start by understanding what you need and the scope of your project.", "about-team.jpg", "Proses", "Konsultasi dan pelan di atas meja", 1400, 1050),
    (2, "Site Visit", "Our team visits the site to assess the space and understand the work required.", "work-photo-2.jpg", "Proses", "Kerja luaran, scaffold", 960, 1280),
    (3, "Quotations", "You receive a quotation based on the agreed scope of work.", "work-render-2.jpg", "Render", "Kitchen — reka bentuk 3D", 960, 1280),
    (4, "Construction", "Once everything is agreed, our team begins the work on site.", "construction-site.jpg", "Proses", "Rumah dua tingkat dalam pembinaan", 1600, 1000),
    (5, "Handover", "When the work is completed, we hand the finished project over to you.", "hero-living.jpg", "Siap", "Ruang tamu, kerja siap", 1800, 1200),
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

VIDEOS = {
    1: ("assets/img/work-video-1.mp4", "Unit dalam kerja, kaca &amp; pelindung"),
    2: ("assets/img/work-video-2.mp4", "Unit komersial, partition kaca"),
    3: ("https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4", "Jubin lantai"),
    4: ("https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4", "Lantai &amp; skirting"),
    5: ("https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4", "Pintu &amp; dinding"),
    6: ("https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4", "Kerja hacking &amp; perobohan"),
    7: ("https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4", "Jubin lantai &amp; dinding"),
}

# the gallery wall, exactly as the owner serves it: photographs, 3D renders, video
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

# the home page's own walk: three rooms, one gold floor line each
HOME_ROOMS = [
    dict(id="dapur", name="Dapur", lead="A better space starts with the right work.",
         body="Whether you're renovating the whole house or improving specific parts of your space, Bina Haus handles the work with attention to detail from start to finish.",
         href="perkhidmatan.html", link="Renovations &amp; construction",
         img="reno-kitchen.jpg", kind="Siap", cap="Dapur, kerja siap", w=1040, h=1300),
    dict(id="ruang", name="Ruang tamu", lead="See the work for yourself.",
         body="A collection of work by Bina Haus — photographs, 3D renders and video, each labelled by what it is.",
         href="kerja.html", link="All work",
         img="work-photo-3.jpg", kind="Siap", cap="Ruang dalaman siap: lantai kayu, tingkap besar", w=960, h=1280),
    dict(id="tapak", name="Tapak", lead="Built for what comes next.",
         body="Whether you're building a new house, extending your existing property or carrying out structural works, Bina Haus takes your project from planning to completion.",
         href="perkhidmatan.html#pembinaan", link="Construction",
         img="construction-site.jpg", kind="Proses", cap="Rumah dua tingkat dalam pembinaan", w=1600, h=1000),
]


def head(title, desc, active):
    cur = ' aria-current="page"'
    links = "\n".join('        <a href="%s"%s>%s</a>' % (h, cur if h == active else "", l) for h, l in NAV)
    menu = "\n".join('          <a href="%s"%s>%s</a>' % (h, cur if h == active else "", l) for h, l in MENU)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="BINA HAUS">
<meta name="theme-color" content="#faf8f4">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/logo/bina-haus-logo-160.png">
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/dmsans-vf-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/petrona-vf-latin.woff2" crossorigin>
<link rel="stylesheet" href="assets/style.css?v={cap('assets/style.css')}">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>

<header class="hdr">
  <div class="wrap hdr__in">
    <a class="mark" href="index.html" aria-label="Bina Haus — utama">
      <span class="mark__plate"><img src="assets/logo/bina-haus-logo-320.png" alt="BINA HAUS" width="320" height="312"></span>
    </a>
    <div class="navwrap">
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
    <div class="ftr__brand">
      <span class="mark__plate mark__plate--lg"><img src="assets/logo/bina-haus-logo-320.png" alt="BINA HAUS" width="320" height="312"></span>
      <p class="ftr__tag">Ruang dibina dengan rasa</p>
      <p class="ftr__site"><a href="{SITE}">binahaus.com</a></p>
    </div>
    <div class="ftr__col">
      <p class="ftr__label">Contact</p>
      <ul><li><a href="{WA}">WhatsApp +60 11-1124 4636</a></li><li><a href="kontak.html">Contact</a></li></ul>
    </div>
    <div class="ftr__col">
      <p class="ftr__label">Navigation</p>
      <ul>
{items}
      </ul>
    </div>
  </div>
  <div class="wrap ftr__bar">
    <span>© 2026 Bina Haus. All rights reserved.</span>
    <span>Look preview: arah 07, bukan laman rasmi.</span>
  </div>
</footer>

<script src="assets/app.js?v={cap('assets/app.js')}" defer></script>
</body>
</html>
"""


def shot(img, kind, cap, w, h, extra="", eager=False):
    load = 'loading="eager" fetchpriority="high"' if eager else 'loading="lazy"'
    return f"""      <figure class="shot{extra}">
        <div class="shot__fr"><img src="assets/img/{img}" alt="{cap}" width="{w}" height="{h}" {load} decoding="async"></div>
        <figcaption class="shot__cap"><span class="kind">{kind}</span>{cap}</figcaption>
      </figure>"""


def room(r):
    return f"""
<section class="room" id="{r['id']}">
  <div class="wrap room__in">
    <div class="room__hd" data-rv="name"><h2>{r['name']}</h2></div>
    <div class="room__body">
      <div class="room__text" data-rv="rise">
        <p class="lead">{r['lead']}</p>
        <p>{r['body']}</p>
        <p class="room__link"><a class="btn btn--quiet" href="{r['href']}">{r['link']}</a></p>
      </div>
      <div class="room__media" data-rv="media">
{shot(r['img'], r['kind'], r['cap'], r['w'], r['h'])}
      </div>
    </div>
  </div>
  <span class="floor" data-rv="floor" aria-hidden="true"></span>
</section>"""


def works(items, anchor=None):
    a = f' id="{anchor}"' if anchor else ""
    return f'      <ul class="list"{a}>\n' + "\n".join(
        '        <li><span class="list__n">%02d</span><div><b>%s</b><p>%s</p></div></li>' % (n, t, d) for n, t, d in items
    ) + "\n      </ul>"


def tile(kind, a, b=None):
    if kind == "img":
        return f"""        <li><figure class="tile"><div class="tile__fr"><img src="assets/img/{a}" alt="{b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption class="shot__cap"><span class="kind">Foto</span>{b}</figcaption></figure></li>"""
    if kind == "render":
        return f"""        <li><figure class="tile"><div class="tile__fr"><img src="assets/img/{a}" alt="Render reka bentuk: {b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption class="shot__cap"><span class="kind">Render</span>{b}</figcaption></figure></li>"""
    src, cap = VIDEOS[a]
    return f"""        <li class="tile--video"><figure class="tile"><div class="tile__fr">
          <video src="{src}" poster="assets/img/work-poster-{a}.jpg" controls playsinline preload="none"></video>
          <button class="tile__play" type="button" aria-label="Main video: {cap}">
            <img src="assets/img/work-poster-{a}.jpg" alt="Pratonton video: {cap}" width="787" height="1400" loading="lazy" decoding="async">
            <span class="tile__btn" aria-hidden="true"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M3 1.4 13.6 8 3 14.6Z" fill="currentColor"/></svg></span>
          </button></div><figcaption class="shot__cap"><span class="kind">Video</span>{cap}</figcaption></figure></li>"""


def wall(limit=None, cls="wall"):
    items = GALLERY[:limit] if limit else GALLERY
    out = []
    for x in items:
        k = x[0]
        if k == "img":
            out.append(tile("img", x[1], x[2]))
        elif k == "render":
            out.append(tile("render", x[1], x[2]))
        else:
            out.append(tile("video", x[1]))
    return f'      <ul class="{cls}">\n' + "\n".join(out) + "\n      </ul>"


def write(name, body):
    (HERE / name).write_text(body, encoding="utf-8")
    print("wrote", name, len(body), "bytes")


INDEX = """
<main id="main">

<section class="hero">
  <div class="wrap hero__in">
    <div class="hero__text" data-rv="name">
      <h1>Ruang dibina dengan rasa</h1>
      <p class="hero__lede">Renovation and construction for homes, offices and commercial spaces.</p>
      <p class="hero__lede">From the first consultation to the final handover, Bina Haus brings your project together under one team.</p>
      <div class="hero__cta">
        <a class="btn" href="kontak.html">Get free Quotation</a>
        <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
      </div>
    </div>
    <figure class="hero__media" data-rv="media">
      <div class="shot__fr shot__fr--hero"><img src="assets/img/hero-living.jpg" alt="Ruang tamu selepas kerja siap: sofa, console TV dan tingkap besar" width="1800" height="1200" fetchpriority="high" decoding="async"></div>
      <figcaption class="shot__cap"><span class="kind">Siap</span>Ruang tamu, kerja siap</figcaption>
    </figure>
  </div>
  <span class="floor" data-rv="floor" aria-hidden="true"></span>
</section>

<section class="doors">
  <div class="wrap">
    <h2 data-rv="name">Bilik demi bilik</h2>
    <p class="prose" data-rv="rise">Laman ini dibaca seperti sebuah rumah: satu ruang pada satu masa, gambar sebenar kerja Bina Haus pada setiap ruang.</p>
    <ul class="trio">
      <li data-rv="media"><a href="perkhidmatan.html" class="door">
        <figure class="tile"><div class="tile__fr"><img src="assets/img/reno-kitchen.jpg" alt="Dapur, kerja siap" width="1040" height="1300" loading="lazy" decoding="async"></div>
        <figcaption class="shot__cap"><span class="kind">Siap</span>Dapur, kerja siap</figcaption></figure>
        <span class="door__label">A better space starts with the right work.</span>
        <span class="door__meta">Services</span></a></li>
      <li data-rv="media"><a href="kerja.html" class="door">
        <figure class="tile"><div class="tile__fr"><img src="assets/img/work-photo-3.jpg" alt="Ruang dalaman siap: lantai kayu, tingkap besar" width="960" height="1280" loading="lazy" decoding="async"></div>
        <figcaption class="shot__cap"><span class="kind">Siap</span>Ruang dalaman siap</figcaption></figure>
        <span class="door__label">See the work for yourself.</span>
        <span class="door__meta">Our Work</span></a></li>
      <li data-rv="media"><a href="cara.html" class="door">
        <figure class="tile"><div class="tile__fr"><img src="assets/img/about-team.jpg" alt="Pasukan meneliti pelan di tapak" width="1400" height="1050" loading="lazy" decoding="async"></div>
        <figcaption class="shot__cap"><span class="kind">Proses</span>Pasukan meneliti pelan di tapak</figcaption></figure>
        <span class="door__label">A clear process from start to finish.</span>
        <span class="door__meta">Cara Kami Kerja</span></a></li>
    </ul>
  </div>
  <span class="floor" data-rv="floor" aria-hidden="true"></span>
</section>
""" + "\n".join(room(r) for r in HOME_ROOMS) + """

<section class="wall-sect">
  <div class="wrap">
    <h2 data-rv="name">Ruang yang siap</h2>
    <p class="prose" data-rv="rise">A collection of work by Bina Haus.</p>
""" + wall(6, "wall wall--home") + """
    <p class="more" data-rv="rise"><a class="btn btn--quiet" href="kerja.html">All work</a></p>
  </div>
  <span class="floor" data-rv="floor" aria-hidden="true"></span>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <div data-rv="rise">
      <h2>Planning to renovate your space?</h2>
      <p>Tell us what you need and let's start with a conversation.</p>
    </div>
    <div class="cta__btns" data-rv="rise">
      <a class="btn btn--onDark" href="kontak.html">Get free Quotations</a>
      <a class="btn btn--quietOnDark" href="https://wa.me/601111244636">WhatsApp Us</a>
    </div>
  </div>
</section>

</main>
"""

SERVICES = """<main id="main">

<section class="band">
  <div class="wrap band__in">
    <h1 data-rv="name">A better space starts with the right work.</h1>
    <p class="band__lead" data-rv="rise">Whether you're renovating the whole house or improving specific parts of your space, Bina Haus handles the work with attention to detail from start to finish.</p>
  </div>
  <figure class="band__media" data-rv="media">
    <div class="shot__fr shot__fr--band"><img src="assets/img/work-photo-3.jpg" alt="Ruang dalaman siap: lantai kayu, tingkap besar dan langsir" width="960" height="1280" fetchpriority="high" decoding="async"></div>
    <figcaption class="shot__cap"><span class="kind">Siap</span>Ruang dalaman siap: lantai kayu, tingkap besar</figcaption>
  </figure>
</section>

<section class="sect">
  <div class="wrap">
    <h2 data-rv="name">Renovations</h2>
""" + works(RENO) + """
  </div>
</section>

<section class="sect">
  <div class="wrap">
    <h2 data-rv="name">Construction</h2>
    <p class="prose" data-rv="rise">Whether you're building a new house, extending your existing property or carrying out structural works, Bina Haus takes your project from planning to completion.</p>
""" + works(BUILD, "pembinaan") + """
  </div>
</section>

<section class="sect sect--media">
  <div class="wrap">
    <h2 data-rv="name">Dapur, dan butiran</h2>
    <div class="grid grid--3">
""" + shot("reno-kitchen.jpg", "Siap", "Dapur, kerja siap", 1040, 1300, " shot--room") + "\n" + \
    shot("reno-detail.jpg", "Siap", "Butiran lantai bertemu skirting", 1200, 900, " shot--room") + "\n" + \
    shot("work-render-2.jpg", "Render", "Kitchen — reka bentuk 3D", 960, 1280, " shot--room") + """
    </div>
  </div>
</section>

</main>
"""

WORK = """<main id="main">

<section class="band">
  <div class="wrap band__in">
    <h1 data-rv="name">See the work for yourself.</h1>
    <p class="band__lead" data-rv="rise">Every tile below is the owner's own asset, taken from binahaus.com and served from this page: photographs, 3D renders and video, each labelled by what it is.</p>
  </div>
  <figure class="band__media" data-rv="media">
    <div class="shot__fr shot__fr--band"><img src="assets/img/reno-progress.jpg" alt="Kerja dalaman dalam proses: rasuk kayu siling dan peralatan di lantai" width="1040" height="1300" fetchpriority="high" decoding="async"></div>
    <figcaption class="shot__cap"><span class="kind">Proses</span>Kerja dalaman dalam proses: rasuk kayu siling</figcaption>
  </figure>
</section>

<section class="sect">
  <div class="wrap">
""" + wall() + """
    <p class="note">Media di atas ialah aset Bina Haus sendiri dari binahaus.com: gambar dan video kecil dihidangkan dari halaman ini, video besar dimainkan terus dari binahaus.com. Tiada nama, lokasi atau angka projek direka.</p>
  </div>
</section>

</main>
"""

PROCESS = """<main id="main">

<section class="band band--plain">
  <div class="wrap band__in">
    <h1 data-rv="name">Satu proses yang jelas, dari mula sampai siap.</h1>
    <p class="band__lead" data-rv="rise">A clear process from start to finish.</p>
  </div>
</section>

<section class="sect">
  <div class="wrap">
    <ol class="steps">
""" + "\n".join(
    f"""      <li class="step" id="fasa-{n}" data-rv="rise">
        <span class="step__n">{n:02d}</span>
        <div class="step__bd">
          <h2>{t}</h2>
          <p>{d}</p>
        </div>
        <div class="step__media" data-rv="media">
{shot(img, kind, cap, w, h)}
        </div>
      </li>""" for n, t, d, img, kind, cap, w, h in STEPS
) + """
    </ol>
    <p class="note">Gambar-gambar ini daripada kerja Bina Haus sendiri, tetapi ia bukan satu projek yang sama dan tiada tarikh. Setiap satu dilabel mengikut apa yang ditunjukkannya: <em>Proses</em> (kerja sedang berjalan), <em>Siap</em> (kerja selesai), <em>Render</em> (reka bentuk 3D).</p>
  </div>
</section>

</main>
"""

ABOUT = """<main id="main">

<section class="band">
  <div class="wrap band__in">
    <h1 data-rv="name">We build spaces for everyday life.</h1>
  </div>
  <figure class="band__media" data-rv="media">
    <div class="shot__fr shot__fr--band"><img src="assets/img/hero-living.jpg" alt="Ruang tamu siap dengan sofa dan tingkap besar" width="1800" height="1200" fetchpriority="high" decoding="async"></div>
    <figcaption class="shot__cap"><span class="kind">Siap</span>Ruang tamu siap dengan sofa dan tingkap besar</figcaption>
  </figure>
</section>

<section class="sect">
  <div class="wrap twocol">
    <div class="prose" data-rv="rise">
      <p>Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.</p>
      <p>Our work ranges from full house renovations and individual renovation works to new house construction, house extensions and structural works.</p>
      <p>Whatever the scale of the project, our focus remains the same: Do the work properly. Keep the process clear. Deliver the space.</p>
    </div>
    <div class="prose" data-rv="rise">
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
    <div class="grid grid--2">
""" + shot("about-team.jpg", "Proses", "Pasukan meneliti pelan di tapak", 1400, 1050, " shot--room") + "\n" + \
    shot("construction-site.jpg", "Proses", "Rumah dua tingkat dalam pembinaan", 1600, 1000, " shot--room") + """
    </div>
    <p class="quote" data-rv="rise">Ruang dibina dengan rasa</p>
    <p class="prose" data-rv="rise">Because a space is more than walls, floors and finishes. It's where people live, work and spend their everyday lives.</p>
    <p class="prose" data-rv="rise">So when we build or renovate a space, the work should feel considered from beginning to end.</p>
  </div>
</section>

</main>
"""

COMPANY = """<main id="main">

<section class="band band--plain">
  <div class="wrap band__in">
    <h1 data-rv="name">Bina Haus</h1>
    <p class="band__lead" data-rv="rise">Everything the company publishes about itself, on one plate: read from binahaus.com, nothing filled in, estimated or invented.</p>
  </div>
</section>

<section class="sect">
  <div class="wrap">
    <div class="plate" data-rv="media">
      <div class="plate__hd"><h2>BINA HAUS — Ruang dibina dengan rasa</h2></div>
      <dl>
        <div class="row"><dt>Nama syarikat</dt><dd>Bina Haus<small>Seperti yang dipaparkan di binahaus.com</small></dd></div>
        <div class="row"><dt>Bidang</dt><dd>Renovation and construction<small>Homes, offices and commercial spaces</small></dd></div>
        <div class="row"><dt>Skop kerja: renovasi</dt><dd>Full house renovation · Kitchen renovations · Extension · Flooring · Plaster ceiling · Painting · Electrical &amp; plumbing<small>7 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Skop kerja: pembinaan</dt><dd>New house construction · House extension · Structural works<small>3 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Proses</dt><dd>Consultation → Site visit → Quotations → Construction → Handover<small>Lima langkah, sama pada setiap projek</small></dd></div>
        <div class="row"><dt>Cara kami bekerja</dt><dd>One team. One project. One responsibility.<small>Satu pasukan dari konsultasi sampai serah</small></dd></div>
        <div class="row"><dt>Hubungan</dt><dd>WhatsApp <a href="https://wa.me/601111244636">+60 11-1124 4636</a><br><a href="https://binahaus.com/">binahaus.com</a><small>Satu-satunya saluran yang diterbitkan di laman</small></dd></div>
        <div class="row"><dt>Alamat · E-mel · Pendaftaran</dt><dd>Belum diterbitkan<small>Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat. Tidak diisi di sini supaya tiada butiran palsu.</small></dd></div>
      </dl>
      <p class="plate__ft">Profil ini dibaca terus daripada binahaus.com. Kalau ada butiran yang patut muncul di laman (alamat, e-mel, nombor pendaftaran, tahun mula, kawasan perkhidmatan), beritahu sahaja — ia akan masuk sebagai fakta, bukan anggaran.</p>
    </div>
  </div>
</section>

</main>
"""

CONTACT = """<main id="main">

<section class="band band--plain">
  <div class="wrap band__in">
    <h1 data-rv="name">Contact</h1>
    <p class="band__lead" data-rv="rise">Tell us what you need and let's start with a conversation.</p>
  </div>
</section>

<section class="sect">
  <div class="wrap twocol">
    <div class="prose" data-rv="rise">
      <h2>Planning to renovate your space?</h2>
      <p>Get free quotations, or send a message on WhatsApp with what you have in mind: the space, the work, and when you would like to start.</p>
      <div class="cta__btns">
        <a class="btn" href="https://wa.me/601111244636">Get free Quotations</a>
        <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
      </div>
    </div>
    <div class="prose" data-rv="rise">
      <p class="ftr__label">Saluran yang diterbitkan</p>
      <p>WhatsApp <a href="https://wa.me/601111244636">+60 11-1124 4636</a><br>Web <a href="https://binahaus.com/">binahaus.com</a></p>
      <p>Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat, jadi halaman ini tidak mereka-reka satu.</p>
    </div>
  </div>
</section>

</main>
"""

write("index.html", head("BINA HAUS — Serambi", "Renovation and construction for homes, offices and commercial spaces. Ruang dibina dengan rasa.", "index.html") + INDEX + foot())
write("perkhidmatan.html", head("Services — BINA HAUS", "Renovations and construction: full house renovation, kitchen, extension, flooring, plaster ceiling, painting, electrical and plumbing; new house construction and structural works.", "perkhidmatan.html") + SERVICES + foot())
write("kerja.html", head("Our Work — BINA HAUS", "A collection of work by Bina Haus: photographs, 3D renders and video from the company's own site.", "kerja.html") + WORK + foot())
write("cara.html", head("Cara Kami Kerja — BINA HAUS", "Satu proses yang jelas, dari mula sampai siap: consultation, site visit, quotations, construction, handover.", "cara.html") + PROCESS + foot())
write("tentang.html", head("About Us — BINA HAUS", "Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.", "tentang.html") + ABOUT + foot())
write("syarikat.html", head("Profil Syarikat — BINA HAUS", "Company details as published on binahaus.com: field of work, scope, process and contact.", "syarikat.html") + COMPANY + foot())
write("kontak.html", head("Contact — BINA HAUS", "Tell us what you need and let's start with a conversation. WhatsApp +60 11-1124 4636.", "kontak.html") + CONTACT + foot())
print("\nseven pages written to", HERE)
