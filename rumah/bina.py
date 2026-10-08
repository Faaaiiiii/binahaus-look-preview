#!/usr/bin/env python3
"""Bina Haus — arah 03 "MASUK": build the seven pages from one shell.

Everything the pages say is the owner's own copy, taken verbatim from binahaus.com
(recorded in design/DESIGN.md). This builder exists so the header, the menu and the
footer are written once — seven hand-copied headers drift within a day.

    python3 bina.py        # writes index.html, perkhidmatan.html, kerja.html, …
"""
import html
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


def head(title, desc, active):
    cur = ' aria-current="page"'
    menu_cur = ' aria-current="page"'
    links = "\n".join(
        '        <a href="%s"%s>%s</a>' % (href, cur if href == active else "", label)
        for href, label in NAV
    )
    menu = "\n".join(
        '          <a href="%s"%s>%s</a>' % (href, menu_cur if href == active else "", label)
        for href, label in NAV
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="BINA HAUS">
<meta name="theme-color" content="#0d1420">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/logo/bina-haus-logo-160.png">
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/archivo-600-latin.woff2" crossorigin>
<link rel="preload" as="font" type="font/woff2" href="assets/fonts/manrope-400-latin.woff2" crossorigin>
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
      <button class="burger" type="button" aria-expanded="false" aria-controls="navwrap">Menu</button>
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
    nav = "\n".join(f'        <li><a href="{href}">{label}</a></li>' for href, label in NAV)
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
{nav}
      </ul>
    </div>
  </div>
  <div class="wrap ftr__bar">
    <span>© 2026 Bina Haus. All rights reserved.</span>
    <span>Look preview: arah 03, bukan laman rasmi.</span>
  </div>
</footer>

<script src="assets/app.js" defer></script>
</body>
</html>
"""


def page_head(title, lead, img=None, alt=None, chip=None):
    """The band at the top of every inner page: one heading, one lead, one photograph."""
    media = ""
    if img:
        media = f"""
  <figure class="band__media">
    <img src="assets/img/{img}" alt="{alt}" loading="eager" decoding="async">
    <figcaption class="band__plate"><h1>{title}</h1><span class="room__kind">{chip}</span></figcaption>
  </figure>"""
        return f'<section class="band band--photo">{media}<div class="wrap band__in"><p class="band__lead">{lead}</p></div></section>'
    return f"""
<section class="band">
  <div class="wrap band__in">
    <h1>{title}</h1>
    <p class="band__lead">{lead}</p>
  </div>
</section>"""


def room(rid, name, thesis, body, media=None, alt=None, chip=None, side=False, extra=""):
    plate = ""
    if media:
        plate = f"""
  <figure class="room__media">
    <img src="assets/img/{media}" alt="{alt}" loading="lazy" decoding="async">
    <figcaption class="room__plate"><h2 id="{rid}-h">{name}</h2><span class="room__kind">{chip}</span></figcaption>
  </figure>"""
    return f"""
<section class="room{' room--side' if side else ''}" id="{rid}" aria-labelledby="{rid}-h">
{plate}
  <div class="wrap room__in">
    <h3 class="room__thesis">{thesis}</h3>
    <div class="room__prose prose" data-rev="rise">
{body}
    </div>{extra}
  </div>
</section>"""


def works(items):
    rows = "\n".join(
        f'          <li><span class="n">{n:02d}</span><div><b>{t}</b><p>{d}</p></div></li>'
        for n, t, d in items
    )
    return f'      <ul class="works">\n{rows}\n      </ul>'


RENO_WORKS = [
    (1, "Full house Renovation", "Give your existing home a complete transformation and a fresh new feel."),
    (2, "Kitchen renovations", "Upgrade your kitchen into a space that works better for everyday living."),
    (3, "Extension", "Create the additional space you need within your existing property."),
    (4, "Flooring", "Refresh your space from the ground up with properly installed flooring."),
    (5, "Plaster Ceiling", "Give your interior a cleaner and more refined finish."),
    (6, "Painting", "Refresh the look and feel of your space with a new finish."),
    (7, "Electrical &amp; Plumbing", "Essential electrical and plumbing works for your renovation project."),
]
BUILD_WORKS = [
    (1, "New house Constructions", "Building your new home from the ground up."),
    (2, "House Extension", "Add the extra space your home needs as your needs grow."),
    (3, "Structural Works", "Structural works required for your construction project."),
]
STEPS = [
    (1, "Consultation", "We start by understanding what you need and the scope of your project."),
    (2, "Site Visit", "Our team visits the site to assess the space and understand the work required."),
    (3, "Quotations", "You receive a quotation based on the agreed scope of work."),
    (4, "Construction", "Once everything is agreed, our team begins the work on site."),
    (5, "Handover", "When the work is completed, we hand the finished project over to you."),
]
VIDEOS = {  # poster -> own file or the owner's own URL (the five heavy ones stream from him)
    1: ("assets/img/work-video-1.mp4", "Unit dalam kerja, kaca &amp; pelindung"),
    2: ("assets/img/work-video-2.mp4", "Unit komersial, partition kaca"),
    3: ("https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4", "Jubin lantai"),
    4: ("https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4", "Lantai &amp; skirting"),
    5: ("https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4", "Pintu &amp; dinding"),
    6: ("https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4", "Kerja hacking &amp; perobohan"),
    7: ("https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4", "Jubin lantai &amp; dinding"),
}

# the gallery, in the owner's own order: photograph, render, video, …
GALLERY = [
    ("img", "work-photo-1.jpg", "Bangunan sedia ada, kerja luaran"),
    ("video", 1, None),
    ("img", "work-photo-3.jpg", "Ruang dalaman, tingkap besar"),
    ("img", "work-render-1.jpg", "Dry Kitchen"),
    ("video", 2, None),
    ("img", "work-photo-2.jpg", "Kerja luaran, scaffold"),
    ("img", "work-photo-4.jpg", "Ruang dalaman, lantai kayu"),
    ("video", 3, None),
    ("img", "work-render-3.jpg", "Living and Dining"),
    ("img", "work-photo-6.jpg", "Tapak kerja, kayu di lantai"),
    ("video", 5, None),
    ("img", "work-photo-5.jpg", "Ruang kosong, lantai kayu"),
    ("img", "work-render-4.jpg", "Walk-in Wardrobe"),
    ("video", 6, None),
    ("img", "work-photo-8.jpg", "Kerja plaster, dinding bata"),
    ("img", "work-render-5.jpg", "Living Area"),
    ("video", 7, None),
    ("img", "work-photo-7.jpg", "Ruang kosong, lantai kayu"),
    ("img", "work-render-2.jpg", "Kitchen"),
    ("video", 4, None),
]


def tile(kind, a, b=None):
    if kind == "img":
        return f"""      <li><figure><div class="wk__fr"><img src="assets/img/{a}" alt="{b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption><span class="wk__tag">Foto</span><span>{b}</span></figcaption></figure></li>"""
    if kind == "render":
        return f"""      <li><figure><div class="wk__fr"><img src="assets/img/{a}" alt="Render reka bentuk: {b}" width="960" height="1280" loading="lazy" decoding="async"></div><figcaption><span class="wk__tag">Render</span><span>{b}</span></figcaption></figure></li>"""
    poster, cap = VIDEOS[a]
    return f"""      <li class="wk--video"><figure><div class="wk__fr">
        <video src="{poster}" poster="assets/img/work-poster-{a}.jpg" controls playsinline preload="none"></video>
        <button class="wk__play" type="button" aria-label="Main video: {cap}">
          <img src="assets/img/work-poster-{a}.jpg" alt="Pratonton video: {cap}" width="787" height="1400" loading="lazy" decoding="async">
          <span class="wk__btn" aria-hidden="true"><svg viewBox="0 0 16 16" aria-hidden="true" focusable="false"><path d="M2 1.2 14 8 2 14.8Z" fill="currentColor"/></svg></span>
        </button></div><figcaption><span class="wk__tag">Video</span><span>{cap}</span></figcaption></figure></li>"""


def gallery(limit=None):
    items = GALLERY[:limit] if limit else GALLERY
    out = []
    for kind, a, b in items:
        if kind == "video":
            out.append(tile("video", a))
        elif a.startswith("work-render"):
            out.append(tile("render", a, b))
        else:
            out.append(tile("img", a, b))
    return '    <ul class="wk">\n' + "\n".join(out) + "\n    </ul>"


def write(name, body):
    (HERE / name).write_text(body, encoding="utf-8")
    print("wrote", name, len(body), "bytes")


DOOR = f"""
<header class="door" id="top">
  <img class="door__photo" src="assets/img/hero-living.jpg" alt="Ruang tamu sebuah rumah selepas kerja siap: sofa, console TV dan tingkap besar" width="1800" height="1200" fetchpriority="high" decoding="async">
  <div class="door__grade" aria-hidden="true"></div>
  <div class="door__panels" aria-hidden="true"><span class="door__panel"></span><span class="door__panel"></span></div>

  <div class="wrap door__in">
    <img class="door__mark" src="assets/logo/bina-haus-logo.png" alt="BINA HAUS" width="600" height="585">
    <h1>Ruang dibina dengan rasa</h1>
    <p class="door__lede">Renovation and construction for homes, offices and commercial spaces.</p>
    <p class="door__lede">From the first consultation to the final handover, Bina Haus brings your project together under one team.</p>
    <div class="door__cta">
      <a class="btn" href="kontak.html">Get free Quotation</a>
      <a class="btn btn--quiet" href="{WA}">WhatsApp Us</a>
    </div>
    <div class="door__bar kind">
      <span>Renovation &amp; Construction</span>
      <span>binahaus.com</span>
    </div>
  </div>
</header>
"""

# ----------------------------------------------------------------- index ----
INDEX_BODY = DOOR + """
<main id="main">

<section class="tiga">
  <div class="wrap">
    <h2 class="tiga__h">Masuk ke dalam rumah</h2>
    <p class="tiga__p prose">Setiap ruang di bawah ialah kerja sebenar Bina Haus — gambar, render dan video daripada laman syarikat sendiri.</p>
    <ul class="tiga__list">
      <li><a href="perkhidmatan.html">
        <figure><div class="wk__fr"><img src="assets/img/work-photo-3.jpg" alt="Ruang dalaman siap: lantai kayu, tingkap besar" width="960" height="1280" loading="lazy" decoding="async"></div>
        <figcaption><span class="wk__tag">Ruang tamu</span><span>Kerja renovasi: tujuh jenis kerja</span></figcaption></figure>
      </a></li>
      <li><a href="perkhidmatan.html#dapur">
        <figure><div class="wk__fr"><img src="assets/img/reno-kitchen.jpg" alt="Dapur siap: kabinet kelabu, sinki dan tingkap" width="1040" height="1300" loading="lazy" decoding="async"></div>
        <figcaption><span class="wk__tag">Dapur</span><span>Kitchen renovations</span></figcaption></figure>
      </a></li>
      <li><a href="perkhidmatan.html#tapak">
        <figure><div class="wk__fr"><img src="assets/img/construction-site.jpg" alt="Rumah dua tingkat dalam pembinaan" width="1600" height="1000" loading="lazy" decoding="async"></div>
        <figcaption><span class="wk__tag">Tapak</span><span>Kerja pembinaan &amp; struktur</span></figcaption></figure>
      </a></li>
    </ul>
  </div>
</section>

<section class="strip">
  <div class="wrap">
    <div class="strip__hd">
      <h2>See the work for yourself.</h2>
      <p class="prose">A collection of work by Bina Haus.</p>
    </div>
""" + gallery(6) + """
    <p class="strip__more"><a class="btn btn--quiet" href="kerja.html">All work</a></p>
  </div>
</section>

<section class="room">
  <div class="wrap room__in">
    <h3 class="room__thesis">One team. One project. One responsibility.</h3>
    <div class="room__prose prose" data-rev="rise">
      <p>Renovation and construction can involve many moving parts.</p>
      <p>With Bina Haus, you have one team to communicate with throughout the project.</p>
      <p>From consultation and site visit to construction and handover, you know who you're dealing with at every stage.</p>
      <p>One project. One point of responsibility.</p>
    </div>
    <div class="wide" data-rev="rise">
      <p><a class="btn btn--quiet" href="tentang.html">About Us</a> <a class="btn btn--quiet" href="syarikat.html">Profil Syarikat</a></p>
    </div>
  </div>
</section>

<section class="cta" id="kontak" aria-labelledby="kontak-h">
  <div class="wrap cta__in">
    <div data-rev="rise">
      <h2 id="kontak-h">Planning to renovate your space?</h2>
      <p>Tell us what you need and let's start with a conversation.</p>
    </div>
    <div class="cta__btns wide" data-rev="rise">
      <a class="btn" href="kontak.html">Get free Quotations</a>
      <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
    </div>
  </div>
</section>

</main>
"""

# ---------------------------------------------------------- perkhidmatan ----
SERVICES_BODY = """<main id="main">
""" + page_head(
    "Services",
    "Whether you're renovating the whole house or improving specific parts of your space, Bina Haus handles the work with attention to detail from start to finish.",
    img="work-photo-3.jpg", alt="Ruang dalaman siap: lantai kayu, tingkap besar dan langsir", chip="Foto",
) + """
<div class="wrap room__in">
  <h2 class="band__sub">Renovations</h2>
  <div class="wide" data-rev="rise">
""" + works(RENO_WORKS) + """
  </div>
</div>
""" + room(
    "dapur", "Dapur",
    "Upgrade your kitchen into a space that works better for everyday living.",
    """      <p>Kitchen renovations are one of the works Bina Haus takes on, from a single run of cabinets to the whole room. The two tiles beside this note are the studio's own 3D renders of kitchen work — shown here as renders, not as photographs of a finished site.</p>
      <p class="kind" style="margin-top:1.2rem;color:var(--ink-2)">Renovations · 02 Kitchen renovations</p>""",
    media="reno-kitchen.jpg", alt="Dapur siap: kabinet kelabu, sinki dan tingkap", chip="Foto", side=True,
    extra="""    <div data-rev="rise">
      <div class="pair">
        <figure><img src="assets/img/work-render-2.jpg" alt="Render reka bentuk: Kitchen" width="960" height="1280" loading="lazy" decoding="async"><figcaption>Render · Kitchen</figcaption></figure>
        <figure><img src="assets/img/work-render-1.jpg" alt="Render reka bentuk: Dry Kitchen" width="960" height="1280" loading="lazy" decoding="async"><figcaption>Render · Dry Kitchen</figcaption></figure>
      </div>
    </div>""",
) + room(
    "butiran", "Butiran",
    "Give your interior a cleaner and more refined finish.",
    """      <p>Where one material meets another is where a renovation is judged: the joint between floor and skirting, the line of a ceiling, the grain of a tile. Two of the owner's own videos cover exactly that work — flooring and skirting, and floor-and-wall tiling.</p>
      <p class="kind" style="margin-top:1.2rem;color:var(--ink-2)">Renovations · 04 Flooring · 05 Plaster Ceiling · 06 Painting</p>""",
    media="reno-detail.jpg", alt="Butiran lantai kayu bertemu skirting putih", chip="Foto",
    extra="""    <div data-rev="rise">
      <div class="pair">
""" + tile("video", 4).replace('      <li class="wk--video"><figure>', '<figure class="wk--video">').replace('</figure></li>', '</figure>') + tile("video", 7).replace('      <li class="wk--video"><figure>', '<figure class="wk--video">').replace('</figure></li>', '</figure>') + """
      </div>
    </div>""",
) + room(
    "tapak", "Tapak",
    "Built for what comes next.",
    """      <p>Whether you're building a new house, extending your existing property or carrying out structural works, Bina Haus takes your project from planning to completion.</p>
""" + works(BUILD_WORKS),
    media="construction-site.jpg", alt="Rumah dua tingkat dalam pembinaan: struktur, scaffold dan kerja bata", chip="Foto",
    extra="""    <div data-rev="rise">
      <div class="pair pair--wide">
        <figure><img src="assets/img/work-photo-2.jpg" alt="Kerja luaran: fasad dengan scaffold" width="960" height="1280" loading="lazy" decoding="async"><figcaption>Foto · Kerja luaran, scaffold</figcaption></figure>
        <figure><img src="assets/img/work-photo-8.jpg" alt="Kerja plaster pada dinding bata" width="960" height="1280" loading="lazy" decoding="async"><figcaption>Foto · Kerja plaster, dinding bata</figcaption></figure>
        <figure><img src="assets/img/reno-progress.jpg" alt="Kerja dalaman dalam proses: rasuk kayu siling dan peralatan di lantai" width="1040" height="1300" loading="lazy" decoding="async"><figcaption>Foto · Kerja dalaman dalam proses</figcaption></figure>
        <figure><img src="assets/img/work-photo-1.jpg" alt="Bangunan sedia ada selepas kerja luaran" width="960" height="1280" loading="lazy" decoding="async"><figcaption>Foto · Bangunan sedia ada, kerja luaran</figcaption></figure>
      </div>
    </div>""",
) + """
</main>
"""

# ---------------------------------------------------------------- kerja -----
WORK_BODY = """<main id="main">
""" + page_head(
    "Hasil Kerja",
    "Every tile below is the owner's own asset, taken from binahaus.com and served from this page: photographs, 3D renders and video, each labelled by what it is.",
    img="reno-progress.jpg", alt="Kerja dalaman dalam proses: rasuk kayu siling dan peralatan di lantai", chip="Foto",
) + """
<section class="room">
  <div class="wrap">
""" + gallery() + """
    <p class="strip__note prose">Media di atas ialah aset Bina Haus sendiri dari binahaus.com: gambar dan video kecil dihidangkan dari halaman ini, video besar dimainkan terus dari binahaus.com. Tiada nama, lokasi atau angka projek direka.</p>
  </div>
</section>
</main>
"""

# ----------------------------------------------------------------- cara -----
PROCESS_BODY = """<main id="main">
""" + page_head(
    "Cara Kami Kerja",
    "Satu proses yang jelas, dari mula sampai siap. A clear process from start to finish.",
    img="about-team.jpg", alt="Dua ahli pasukan Bina Haus meneliti pelan di tapak kerja", chip="Foto",
) + """
<section class="room">
  <div class="wrap room__in">
    <div class="wide" data-rev="rise">
      <ol class="steps">
""" + "\n".join(
    f'        <li><span class="n">{n:02d}</span><div><h2>{t}</h2><p>{d}</p></div></li>' for n, t, d in STEPS
) + """
      </ol>
    </div>
  </div>
</section>
</main>
"""

# -------------------------------------------------------------- tentang -----
ABOUT_BODY = """<main id="main">
""" + page_head(
    "About Us",
    "We build spaces for everyday life.",
    img="hero-living.jpg", alt="Ruang tamu siap dengan sofa dan tingkap besar", chip="Foto",
) + """
<section class="room">
  <div class="wrap room__in">
    <div class="room__prose prose" data-rev="rise">
      <p>Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.</p>
      <p>Our work ranges from full house renovations and individual renovation works to new house construction, house extensions and structural works.</p>
      <p>Whatever the scale of the project, our focus remains the same: Do the work properly. Keep the process clear. Deliver the space.</p>
    </div>
    <div class="room__prose prose" data-rev="rise">
      <h2 style="font-size:var(--s4);max-width:26ch">Ruang dibina dengan rasa</h2>
      <p>Because a space is more than walls, floors and finishes. It's where people live, work and spend their everyday lives.</p>
      <p>So when we build or renovate a space, the work should feel considered from beginning to end.</p>
      <p class="kind" style="margin-top:1.2rem;color:var(--ink)">Bina Haus. Ruang dibina dengan rasa.</p>
    </div>
  </div>
</section>

<section class="cta">
  <div class="wrap cta__in">
    <div data-rev="rise">
      <h2>One team. One project. One responsibility.</h2>
      <p>From consultation and site visit to construction and handover, you know who you're dealing with at every stage.</p>
    </div>
    <div class="cta__btns wide" data-rev="rise">
      <a class="btn btn--quiet" href="syarikat.html">Profil Syarikat</a>
      <a class="btn" href="kontak.html">Contact</a>
    </div>
  </div>
</section>
</main>
"""

# ------------------------------------------------------------- syarikat -----
COMPANY_BODY = """<main id="main">
""" + page_head(
    "Profil Syarikat",
    "Everything the company publishes about itself, on one plate — read from binahaus.com, nothing filled in, estimated or invented.",
) + """
<section class="room">
  <div class="wrap">
    <div class="plaque">
      <div class="plaque__hd">
        <h2>BINA HAUS — Ruang dibina dengan rasa</h2>
      </div>
      <dl>
        <div class="row"><dt>Nama syarikat</dt><dd>Bina Haus<small>Seperti yang dipaparkan di binahaus.com</small></dd></div>
        <div class="row"><dt>Bidang</dt><dd>Renovation and construction<small>Homes, offices and commercial spaces</small></dd></div>
        <div class="row"><dt>Skop kerja — renovasi</dt><dd>Full house renovation · Kitchen renovations · Extension · Flooring · Plaster ceiling · Painting · Electrical &amp; plumbing<small>7 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Skop kerja — pembinaan</dt><dd>New house construction · House extension · Structural works<small>3 jenis kerja, seperti di laman</small></dd></div>
        <div class="row"><dt>Proses</dt><dd>Consultation → Site visit → Quotations → Construction → Handover<small>Lima langkah yang sama pada setiap projek</small></dd></div>
        <div class="row"><dt>Cara kami bekerja</dt><dd>One team. One project. One responsibility.<small>Satu pasukan dari konsultasi sampai serah</small></dd></div>
        <div class="row"><dt>Hubungan</dt><dd>WhatsApp +60 11-1124 4636<br>binahaus.com<small>Satu-satunya saluran yang diterbitkan di laman</small></dd></div>
        <div class="row"><dt>Alamat · E-mel · Pendaftaran</dt><dd>Belum diterbitkan<small>Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat. Tidak diisi di sini supaya tiada butiran palsu.</small></dd></div>
      </dl>
      <p class="plaque__ft">Profil ini dibaca terus daripada binahaus.com. Kalau ada butiran yang patut muncul di laman (alamat, e-mel, nombor pendaftaran, tahun mula, kawasan perkhidmatan), beritahu sahaja — ia akan masuk ke plat ini sebagai fakta, bukan anggaran.</p>
    </div>
  </div>
</section>
</main>
"""

# ---------------------------------------------------------------- kontak ----
CONTACT_BODY = """<main id="main">
""" + page_head(
    "Contact",
    "Tell us what you need and let's start with a conversation.",
) + """
<section class="room">
  <div class="wrap room__in">
    <div class="room__prose prose" data-rev="rise">
      <h2 style="font-size:var(--s4)">Planning to renovate your space?</h2>
      <p>Get free quotations, or send a message on WhatsApp with what you have in mind: the space, the work, and when you would like to start.</p>
      <div class="cta__btns" style="margin-top:1.4rem">
        <a class="btn" href="https://wa.me/601111244636">Get free Quotations</a>
        <a class="btn btn--quiet" href="https://wa.me/601111244636">WhatsApp Us</a>
      </div>
    </div>
    <div class="room__prose prose" data-rev="rise">
      <p class="ftr__label" style="color:var(--ink-2)">Saluran yang diterbitkan</p>
      <p style="margin-top:.6rem">WhatsApp <a href="https://wa.me/601111244636">+60 11-1124 4636</a><br>Web <a href="https://binahaus.com/">binahaus.com</a></p>
      <p style="margin-top:1rem;color:var(--ink-2)">Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat, jadi halaman ini tidak mereka-reka satu.</p>
    </div>
  </div>
</section>
</main>
"""

write("index.html", head("BINA HAUS — Ruang dibina dengan rasa",
                         "Bina Haus is a renovation and construction company for homes, offices and commercial spaces. Ruang dibina dengan rasa.",
                         "index.html") + INDEX_BODY + foot())
write("perkhidmatan.html", head("Services — BINA HAUS",
                                "Renovations and construction: full house renovation, kitchen, extension, flooring, plaster ceiling, painting, electrical and plumbing; new house construction and structural works.",
                                "perkhidmatan.html") + SERVICES_BODY + foot())
write("kerja.html", head("Hasil Kerja — BINA HAUS",
                         "A collection of work by Bina Haus: photographs, 3D renders and video from the company's own site.",
                         "kerja.html") + WORK_BODY + foot())
write("cara.html", head("Cara Kami Kerja — BINA HAUS",
                        "Satu proses yang jelas, dari mula sampai siap: consultation, site visit, quotations, construction, handover.",
                        "cara.html") + PROCESS_BODY + foot())
write("tentang.html", head("About Us — BINA HAUS",
                           "Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.",
                           "tentang.html") + ABOUT_BODY + foot())
write("syarikat.html", head("Profil Syarikat — BINA HAUS",
                            "Company details as published on binahaus.com: field of work, scope, process and contact.",
                            "syarikat.html") + COMPANY_BODY + foot())
write("kontak.html", head("Contact — BINA HAUS",
                          "Tell us what you need and let's start with a conversation. WhatsApp +60 11-1124 4636.",
                          "kontak.html") + CONTACT_BODY + foot())
print("\nseven pages written to", HERE)
