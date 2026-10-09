#!/usr/bin/env python3
"""BINA HAUS — arah 05 "SIANG" (daylight): build the seven pages from one shell.

A printed magazine feature about a house, read in daylight.

Every sentence the pages show is the owner's own copy, taken verbatim from
binahaus.com (recorded in design/DESIGN.md).  Every image and video is his own
asset, copied from the owner's library; the five heavy videos stream from his
own URLs.  This builder exists so the header, the menu and the footer are
written once — seven hand-copied headers drift within a day.

    python3 bina.py        # writes index.html, perkhidmatan.html, kerja.html, …
"""
import pathlib

HERE = pathlib.Path(__file__).parent
WA = "https://wa.me/601111244636"
SITE = "https://binahaus.com/"

# the seven pages, in the owner's own menu order
NAV = [
    ("perkhidmatan.html", "Services"),
    ("kerja.html", "Our Work"),
    ("cara.html", "Cara Kami Kerja"),
    ("tentang.html", "About Us"),
    ("syarikat.html", "Profil Syarikat"),
    ("kontak.html", "Contact"),
]
MENU = [("index.html", "Utama")] + NAV          # the panel lists all seven pages

SPEC_PRELOAD = [
    "spectral-400-latin.woff2",
    "librefranklin-400-latin.woff2",
]


def head(title, desc, active):
    cur = ' aria-current="page"'
    links = "\n".join(
        '        <a href="%s"%s>%s</a>' % (href, cur if href == active else "", label)
        for href, label in NAV
    )
    menu = "\n".join(
        '          <a href="%s"%s>%s</a>' % (href, cur if href == active else "", label)
        for href, label in MENU
    )
    preload = "\n".join(
        '<link rel="preload" as="font" type="font/woff2" href="assets/fonts/%s" crossorigin>' % f
        for f in SPEC_PRELOAD
    )
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title}</title>
<meta name="description" content="{desc}">
<meta name="author" content="BINA HAUS">
<meta name="theme-color" content="#faf8f4">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:type" content="website">
<link rel="icon" type="image/png" href="assets/logo/bina-haus-logo-160.png">
{preload}
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
    nav = "\n".join(f'        <li><a href="{href}">{label}</a></li>' for href, label in NAV)
    return f"""
<footer class="ftr">
  <div class="wrap ftr__in">
    <div>
      <img class="ftr__mark" src="assets/logo/bina-haus-logo-320.png" alt="BINA HAUS" width="320" height="312">
      <p class="ftr__tag">Ruang dibina dengan rasa</p>
      <p class="ftr__site"><a href="{SITE}">binahaus.com</a> · Renovation &amp; Construction</p>
    </div>
    <div>
      <p class="ftr__label">Contact</p>
      <ul>
        <li><a href="{WA}">WhatsApp +60 11-1124 4636</a></li>
        <li><a href="kontak.html">Contact</a></li>
      </ul>
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
    <span>Look preview: arah 05 “Siang”, bukan laman rasmi.</span>
  </div>
</footer>

<script src="assets/app.js" defer></script>
</body>
</html>
"""


def band(title, stand=""):
    """The head of an inner page: one h1, one standfirst.  No eyebrow above it."""
    s = f'\n    <p class="section__stand">{stand}</p>' if stand else ""
    return f"""<main id="main">

<section class="section" style="border-top:0">
  <div class="wrap band-head">
    <h1>{title}</h1>{s}
  </div>
</section>
"""


def works(items, tag="Renovations"):
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

# poster -> own local file, or the owner's own URL (the five heavy ones stream from him)
VIDEOS = {
    1: ("assets/img/work-video-1.mp4", "Unit dalam kerja, kaca &amp; pelindung"),
    2: ("assets/img/work-video-2.mp4", "Unit komersial, partition kaca"),
    3: ("https://binahaus.com/__l5e/assets-v1/7399f2b8-894b-4ae3-974b-6b79ffef72fe/work-video-3.mp4", "Jubin lantai"),
    4: ("https://binahaus.com/__l5e/assets-v1/7dade64d-a9ec-4578-b7c2-cb63df991d48/work-video-4.mp4", "Lantai &amp; skirting"),
    5: ("https://binahaus.com/__l5e/assets-v1/082f870d-e0f9-44c8-bfac-ea02d0e7927f/work-video-5.mp4", "Pintu &amp; dinding"),
    6: ("https://binahaus.com/__l5e/assets-v1/5d7c8ae3-bd4e-4b5b-9c0e-78c3b9939cde/work-video-6.mp4", "Kerja hacking &amp; perobohan"),
    7: ("https://binahaus.com/__l5e/assets-v1/62ec1448-6e1f-48c2-9292-c925485c19a6/work-video-7.mp4", "Jubin lantai &amp; dinding"),
}
POSTER_WH = {1: (787, 1400), 2: (787, 1400), 3: (360, 640), 4: (360, 640),
             5: (360, 640), 6: (360, 640), 7: (296, 642)}

# the gallery, in the owner's own order: photograph, render, video, …
GALLERY = [
    ("img", "work-photo-1.jpg", "Bangunan sedia ada, kerja luaran", "Foto"),
    ("video", 1, None, None),
    ("img", "work-photo-3.jpg", "Ruang dalaman, tingkap besar", "Foto"),
    ("img", "work-render-1.jpg", "Dry Kitchen", "Render"),
    ("video", 2, None, None),
    ("img", "work-photo-2.jpg", "Kerja luaran, scaffold", "Foto"),
    ("img", "work-photo-4.jpg", "Ruang dalaman, lantai kayu", "Foto"),
    ("video", 3, None, None),
    ("img", "work-render-3.jpg", "Living and Dining", "Render"),
    ("img", "work-photo-6.jpg", "Tapak kerja, kayu di lantai", "Foto"),
    ("video", 5, None, None),
    ("img", "work-photo-5.jpg", "Ruang kosong, lantai kayu", "Foto"),
    ("img", "work-render-4.jpg", "Walk-in Wardrobe", "Render"),
    ("video", 6, None, None),
    ("img", "work-photo-8.jpg", "Kerja plaster, dinding bata", "Foto"),
    ("img", "work-render-5.jpg", "Living Area", "Render"),
    ("video", 7, None, None),
    ("img", "work-photo-7.jpg", "Ruang kosong, lantai kayu", "Foto"),
    ("img", "work-render-2.jpg", "Kitchen", "Render"),
    ("video", 4, None, None),
]
PHOTO_WH = {
    "work-photo-1.jpg": (960, 1280), "work-photo-2.jpg": (960, 1280), "work-photo-3.jpg": (960, 1280),
    "work-photo-4.jpg": (1050, 1400), "work-photo-5.jpg": (960, 1280), "work-photo-6.jpg": (960, 1280),
    "work-photo-7.jpg": (960, 1280), "work-photo-8.jpg": (960, 1280),
    "work-render-1.jpg": (960, 1280), "work-render-2.jpg": (960, 1280), "work-render-3.jpg": (960, 1280),
    "work-render-4.jpg": (960, 1280), "work-render-5.jpg": (960, 1280),
    "hero-living.jpg": (1800, 1200), "reno-kitchen.jpg": (1040, 1300), "reno-detail.jpg": (1200, 900),
    "reno-progress.jpg": (1040, 1300), "construction-site.jpg": (1600, 1000), "about-team.jpg": (1400, 1050),
}


def plate(src, alt, tag, caption, cls="plate", eager=False, wh=None):
    w, h = wh or PHOTO_WH[src]
    load = ' fetchpriority="high"' if eager else ' loading="lazy"'
    return f"""<figure class="{cls}">
    <img src="assets/img/{src}" alt="{alt}" width="{w}" height="{h}"{load} decoding="async">
    <figcaption><span class="tag">{tag}</span><span>{caption}</span></figcaption>
  </figure>"""


def tile(item):
    kind, a, b, tag = item
    if kind == "img":
        w, h = PHOTO_WH[a]
        return (f'      <li><figure><div class="wk__fr">'
                f'<img src="assets/img/{a}" alt="{b}" width="{w}" height="{h}" loading="lazy" decoding="async">'
                f'</div><figcaption><span class="tag">{tag}</span><span>{b}</span></figcaption></figure></li>')
    src, cap = VIDEOS[a]
    w, h = POSTER_WH[a]
    return (f'      <li><figure><div class="wk__fr">'
            f'<video controls playsinline preload="none" width="{w}" height="{h}" '
            f'poster="assets/img/work-poster-{a}.jpg" src="{src}"></video>'
            f'</div><figcaption><span class="tag">Video</span><span>{cap}</span></figcaption></figure></li>')


def gallery(limit=None):
    items = GALLERY[:limit] if limit else GALLERY
    return '    <ul class="wk">\n' + "\n".join(tile(i) for i in items) + "\n    </ul>"


# =============================================================== index ======
COVER = """<div class="cover">
  <div class="wrap cover__head">
    <div class="goldrule" aria-hidden="true"></div>
    <div class="cover__main">
      <h1>Ruang dibina dengan rasa</h1>
    </div>
    <div class="cover__aside">
      <p class="lede">Renovation and construction for homes, offices and commercial spaces.</p>
      <p>From the first consultation to the final handover, Bina Haus brings your project together under one team.</p>
      <p class="cover__cta">
        <a class="btn" href="kontak.html">Get free Quotation</a>
        <a class="btn btn--line" href="%(WA)s">WhatsApp Us</a>
      </p>
    </div>
  </div>
  <figure class="plate plate--bleed">
    <img src="assets/img/hero-living.jpg" alt="Ruang tamu sebuah rumah selepas kerja siap: sofa, console TV dan tingkap besar" width="1800" height="1200" fetchpriority="high" decoding="async">
    <figcaption><span class="tag">Foto</span><span>Ruang tamu sebuah rumah selepas kerja siap. Bina Haus — Renovation &amp; Construction.</span></figcaption>
  </figure>
</div>""" % {"WA": WA}

INDEX_INVITE = """
<main id="main">

<section class="section" aria-labelledby="masuk-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="masuk-h">Masuk ke dalam rumah</h2>
      <p class="section__stand">Setiap ruang di bawah ialah kerja sebenar Bina Haus — gambar, render dan video daripada laman syarikat sendiri.</p>
    </div>
    <ul class="invite">
      <li><a href="perkhidmatan.html">
        <figure><div class="wk__fr"><img src="assets/img/work-photo-3.jpg" alt="Ruang dalaman siap: lantai kayu dan tingkap besar" width="960" height="1280" loading="lazy" decoding="async"></div>
        <figcaption><span class="tag">Foto</span><span>Ruang tamu — tujuh jenis kerja renovasi</span></figcaption></figure>
      </a></li>
      <li><a href="perkhidmatan.html">
        <figure><div class="wk__fr"><img src="assets/img/reno-kitchen.jpg" alt="Dapur siap: kabinet kelabu, sinki dan tingkap" width="1040" height="1300" loading="lazy" decoding="async"></div>
        <figcaption><span class="tag">Foto</span><span>Dapur — kitchen renovations</span></figcaption></figure>
      </a></li>
      <li><a href="kerja.html">
        <figure><div class="wk__fr"><img src="assets/img/construction-site.jpg" alt="Rumah dua tingkat dalam pembinaan: struktur, scaffold dan kerja bata" width="1600" height="1000" loading="lazy" decoding="async"></div>
        <figcaption><span class="tag">Foto</span><span>Tapak — kerja pembinaan &amp; struktur</span></figcaption></figure>
      </a></li>
    </ul>
  </div>
</section>

<section class="section" aria-labelledby="works-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="works-h">See the work for yourself.</h2>
      <p class="section__stand">A collection of work by Bina Haus.</p>
    </div>
""" + gallery(6) + """
    <p class="strip__note"><a class="btn btn--line" href="kerja.html">All work</a></p>
  </div>
</section>
"""

BAND_BLOCK = """
<section class="band" aria-labelledby="team-h">
  <div class="wrap">
    <div class="goldline" aria-hidden="true"></div>
    <h2 id="team-h">One team. One project. One responsibility.</h2>
    <div class="stack" style="margin-top:clamp(1.4rem,3vw,2.2rem)">
      <p>Renovation and construction can involve many moving parts.</p>
      <p>With Bina Haus, you have one team to communicate with throughout the project.</p>
      <p>From consultation and site visit to construction and handover, you know who you're dealing with at every stage.</p>
      <p class="pull">One project. One point of responsibility.</p>
    </div>
  </div>
</section>
"""

INDEX_CTA = """
<section class="cta" aria-labelledby="cta-h">
  <div class="wrap cta__in">
    <div>
      <h2 id="cta-h">Planning to renovate your space?</h2>
      <p>Tell us what you need and let's start with a conversation.</p>
    </div>
    <div class="cta__btns">
      <a class="btn" href="kontak.html">Get free Quotations</a>
      <a class="btn btn--line" href="%(WA)s">WhatsApp Us</a>
    </div>
  </div>
</section>

</main>
""" % {"WA": WA}

INDEX_BODY = COVER + INDEX_INVITE + BAND_BLOCK + INDEX_CTA


# ======================================================== perkhidmatan ======
SERVICES_BODY = band(
    "Services",
    "Whether you're renovating the whole house or improving specific parts of your space, Bina Haus handles the work with attention to detail from start to finish.",
) + """
<section class="section" aria-labelledby="reno-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="reno-h">Renovations</h2>
      <p class="section__stand">A better space starts with the right work.</p>
    </div>
""" + works(RENO_WORKS) + """
  </div>
</section>

<section class="section section--raised" aria-labelledby="dapur-h">
  <div class="wrap">
    <div class="feature">
      <div class="feature__text">
        <h2 id="dapur-h">Kitchen renovations</h2>
        <p class="section__stand" style="margin-top:.8rem">Upgrade your kitchen into a space that works better for everyday living.</p>
        <p class="strip__note">The two tiles opposite are the studio's own 3D renders of kitchen work, shown here as renders, not as photographs of a finished site.</p>
      </div>
      <div class="feature__media">
""" + plate("reno-kitchen.jpg", "Dapur siap: kabinet kelabu, sinki dan tingkap",
            "Foto", "Dapur selepas kerja — kabinet, sinki dan tingkap.") + """
        <ul class="wk wk--pair" style="margin-top:clamp(1rem,2.4vw,1.6rem)">
""" + tile(("img", "work-render-2.jpg", "Kitchen", "Render")) + "\n" + tile(("img", "work-render-1.jpg", "Dry Kitchen", "Render")) + """
        </ul>
      </div>
    </div>
  </div>
</section>

<section class="section" aria-labelledby="build-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="build-h">Construction</h2>
      <p class="section__stand">Built for what comes next.</p>
      <p class="section__stand" style="max-width:56ch">Whether you're building a new house, extending your existing property or carrying out structural works, Bina Haus takes your project from planning to completion.</p>
    </div>
""" + works(BUILD_WORKS, "Construction") + """
  </div>
</section>

<section class="section section--raised" aria-labelledby="tapak-h">
  <div class="wrap">
    <div class="feature feature--flip">
      <div class="feature__text">
        <h2 id="tapak-h">Structural works</h2>
        <p class="section__stand" style="margin-top:.8rem">Structural works required for your construction project.</p>
        <p class="strip__note">A site in progress and the finished exterior — photographs, not renders. Two of the owner's own videos (flooring and skirting; floor-and-wall tiling) sit beside them.</p>
      </div>
      <div class="feature__media">
""" + plate("construction-site.jpg", "Rumah dua tingkat dalam pembinaan: struktur, scaffold dan kerja bata",
            "Foto", "Tapak pembinaan: struktur, scaffold dan kerja bata.") + """
        <ul class="wk wk--pair" style="margin-top:clamp(1rem,2.4vw,1.6rem)">
""" + tile(("img", "work-photo-2.jpg", "Kerja luaran, scaffold", "Foto")) + "\n" + tile(("img", "work-photo-8.jpg", "Kerja plaster, dinding bata", "Foto")) + """
        </ul>
        <ul class="wk wk--pair" style="margin-top:clamp(1rem,2.4vw,1.6rem)">
""" + tile(("video", 4, None, None)) + "\n" + tile(("video", 7, None, None)) + """
        </ul>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ================================================================ kerja =====
WORK_BODY = band(
    "Our Work",
    "A collection of work by Bina Haus.",
) + """
<section class="section" aria-labelledby="gallery-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="gallery-h">See the work for yourself.</h2>
      <p class="section__stand">Photographs, 3D renders and video from the company's own site — each tile labelled by what it is.</p>
    </div>
""" + gallery() + """
    <p class="strip__note">Media di atas ialah aset Bina Haus sendiri dari binahaus.com: gambar, render dan video kecil dihidangkan dari halaman ini, video besar dimainkan terus dari binahaus.com. Tiada nama, lokasi atau angka projek direka.</p>
  </div>
</section>
</main>
"""

# ================================================================= cara =====
PROCESS_BODY = band(
    "Cara Kami Kerja",
    "Satu proses yang jelas, dari mula sampai siap.",
) + """
<section class="section" aria-labelledby="steps-h">
  <div class="wrap">
    <div class="section__hd">
      <h2 id="steps-h">A clear process from start to finish.</h2>
    </div>
    <ol class="steps">
""" + "\n".join(
    f'      <li><span class="n">{n:02d}</span><div><h3>{t}</h3><p>{d}</p></div></li>'
    for n, t, d in STEPS
) + """
    </ol>
  </div>
</section>

<section class="section section--raised" aria-labelledby="team-photo-h">
  <div class="wrap">
    <div class="feature">
      <div class="feature__text">
        <h2 id="team-photo-h">One team. One project. One responsibility.</h2>
        <p class="section__stand" style="margin-top:.8rem">From consultation and site visit to construction and handover, you know who you're dealing with at every stage.</p>
      </div>
      <div class="feature__media">
""" + plate("about-team.jpg", "Dua ahli pasukan Bina Haus meneliti pelan di tapak kerja",
            "Foto", "Pasukan di tapak kerja, meneliti pelan.") + """
        <ul class="wk wk--pair" style="margin-top:clamp(1rem,2.4vw,1.6rem)">
""" + plate("reno-progress.jpg", "Kerja dalaman dalam proses: rasuk kayu siling dan peralatan di lantai",
            "Foto", "Kerja dalaman dalam proses.") + """
        </ul>
      </div>
    </div>
  </div>
</section>
</main>
"""

# ============================================================== tentang =====
ABOUT_BODY = band(
    "About Us",
    "Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.",
) + """
<section class="section" aria-labelledby="about-h">
  <div class="wrap">
    <div class="feature">
      <div class="feature__text prose" data-rev="rise">
        <h2 id="about-h">We build spaces for everyday life.</h2>
        <p>Our work ranges from full house renovations and individual renovation works to new house construction, house extensions and structural works.</p>
        <p>Whatever the scale of the project, our focus remains the same: Do the work properly. Keep the process clear. Deliver the space.</p>
      </div>
      <div class="feature__media">
""" + plate("about-team.jpg", "Dua ahli pasukan Bina Haus meneliti pelan di tapak kerja",
            "Foto", "Pasukan Bina Haus di tapak kerja.") + """
      </div>
    </div>
  </div>
</section>

<section class="section section--raised" aria-labelledby="rasa-h">
  <div class="wrap">
    <div class="prose" data-rev="rise">
      <h2 class="pull" id="rasa-h">Ruang dibina dengan rasa</h2>
      <p>Because a space is more than walls, floors and finishes. It's where people live, work and spend their everyday lives.</p>
      <p>So when we build or renovate a space, the work should feel considered from beginning to end.</p>
      <p class="tag" style="margin-top:1.4rem">BINA HAUS. RUANG DIBINA DENGAN RASA.</p>
    </div>
  </div>
</section>
</main>
"""

# ============================================================= syarikat =====
COMPANY_BODY = band(
    "Profil Syarikat",
    "Everything the company publishes about itself, on one plate — read from binahaus.com, nothing filled in, estimated or invented.",
) + """
<section class="section" aria-labelledby="plate-h">
  <div class="wrap" style="max-width:56rem">
    <div class="plaque">
      <div class="goldline" aria-hidden="true"></div>
      <div class="plaque__hd">
        <h2 id="plate-h">BINA HAUS — Ruang dibina dengan rasa</h2>
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

# =============================================================== kontak =====
CONTACT_BODY = band(
    "Contact",
    "Tell us what you need and let's start with a conversation.",
) + """
<section class="section" aria-labelledby="hello-h">
  <div class="wrap">
    <div class="feature">
      <div class="feature__text">
        <h2 id="hello-h">Planning to renovate your space?</h2>
        <p class="section__stand" style="margin-top:.8rem">Get free quotations, or send a message on WhatsApp with what you have in mind: the space, the work, and when you would like to start.</p>
        <p class="cover__cta" style="margin-top:clamp(1.4rem,3vw,2rem)">
          <a class="btn" href="%(WA)s">Get free Quotations</a>
          <a class="btn btn--line" href="%(WA)s">WhatsApp Us</a>
        </p>
        <p class="ftr__label" style="margin-top:clamp(1.6rem,3.4vw,2.4rem)">Saluran yang diterbitkan</p>
        <ul class="chan">
          <li><a href="%(WA)s">WhatsApp +60 11-1124 4636</a></li>
          <li><a href="%(SITE)s">binahaus.com</a></li>
        </ul>
        <p class="strip__note">Laman binahaus.com tidak memaparkan alamat premis, e-mel rasmi atau nombor pendaftaran syarikat, jadi halaman ini tidak mereka-reka satu.</p>
      </div>
      <div class="feature__media">
""" % {"WA": WA, "SITE": SITE} + plate("work-photo-3.jpg", "Ruang dalaman siap: lantai kayu dan tingkap besar",
            "Foto", "Ruang dalaman selepas kerja.") + """
      </div>
    </div>
  </div>
</section>
</main>
"""


def write(name, body):
    (HERE / name).write_text(body, encoding="utf-8")
    print("wrote", name, len(body), "bytes")


write("index.html", head(
    "BINA HAUS — Ruang dibina dengan rasa",
    "Bina Haus is a renovation and construction company for homes, offices and commercial spaces. Ruang dibina dengan rasa.",
    "index.html") + INDEX_BODY + foot())
write("perkhidmatan.html", head(
    "Services — BINA HAUS",
    "Renovations and construction: full house renovation, kitchen, extension, flooring, plaster ceiling, painting, electrical and plumbing; new house construction and structural works.",
    "perkhidmatan.html") + SERVICES_BODY + foot())
write("kerja.html", head(
    "Our Work — BINA HAUS",
    "A collection of work by Bina Haus: photographs, 3D renders and video from the company's own site.",
    "kerja.html") + WORK_BODY + foot())
write("cara.html", head(
    "Cara Kami Kerja — BINA HAUS",
    "Satu proses yang jelas, dari mula sampai siap: consultation, site visit, quotations, construction, handover.",
    "cara.html") + PROCESS_BODY + foot())
write("tentang.html", head(
    "About Us — BINA HAUS",
    "Bina Haus is a renovation and construction company serving homes, offices and commercial spaces.",
    "tentang.html") + ABOUT_BODY + foot())
write("syarikat.html", head(
    "Profil Syarikat — BINA HAUS",
    "Company details as published on binahaus.com: field of work, scope, process and contact.",
    "syarikat.html") + COMPANY_BODY + foot())
write("kontak.html", head(
    "Contact — BINA HAUS",
    "Tell us what you need and let's start with a conversation. WhatsApp +60 11-1124 4636.",
    "kontak.html") + CONTACT_BODY + foot())
print("\nseven pages written to", HERE)
