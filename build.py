#!/usr/bin/env python3
"""Builds the static pages of Praneel Mohan's portfolio (v4)."""
import html, os

OUT = os.path.dirname(os.path.abspath(__file__))
e = html.escape

ARROW = '<svg aria-hidden="true" width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
PLAY = '<span class="play" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span>'
CV = 'assets/Praneel_Mohan_CV.pdf'
EMAIL = 'praneelmohan1998@gmail.com'
CUR = ' aria-current="page"'
ACC = ' class="accent"'


def head(title, desc, current):
    nav = [('index.html', 'Home'), ('work.html', 'Work'), ('performance.html', 'Case studies'), ('about.html', 'About'), ('#contact', 'Contact')]
    links = ''.join(
        f'<a href="{h}"{CUR if h == current else ""}>{t}</a>' for h, t in nav if t != 'Home')
    return f'''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{e(title)}</title>
<meta name="description" content="{e(desc)}">
<meta property="og:title" content="{e(title)}">
<meta property="og:description" content="{e(desc)}">
<meta property="og:type" content="website">
<meta name="theme-color" content="#06070e">
<link rel="icon" href="assets/favicon.svg" type="image/svg+xml">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Archivo:wdth,wght@62..125,100..900&family=Geist:wght@300..700&display=swap">
<link rel="stylesheet" href="css/pm.css">
</head>
<body>
<a class="skip" href="#main">Skip to content</a>
<header class="site-head">
<div class="wrap">
<a class="brand" href="index.html">PRANEEL MOHAN</a>
<nav class="nav" id="nav" aria-label="Main">{links}</nav>
<div class="head-right">
<span class="status"><i aria-hidden="true"></i>Open to new roles</span>
<a class="btn btn-solid" href="{CV}" download>Download CV</a>
<button class="menu-btn" type="button" aria-expanded="false" aria-controls="nav">Menu</button>
</div>
</div>
</header>
<main id="main">
'''


def foot(next_note=''):
    return f'''
<section id="contact" class="cta" aria-labelledby="cta-title">
<div class="wrap">
<div style="display:flex;flex-direction:column;gap:24px">
<h2 id="cta-title" class="disp">Let's talk.</h2>
<p style="font-size:19px;max-width:520px">Open to social media, performance marketing and account management roles in Delhi NCR, remote or hybrid.</p>
</div>
<div style="display:flex;flex-direction:column;gap:16px;align-items:flex-start">
<a class="mail" href="mailto:{EMAIL}">{EMAIL}</a>
<div class="cta-row">
<a class="btn btn-dark" href="{CV}" download>Download CV</a>
<a class="btn btn-ghost-dark" href="https://www.linkedin.com/in/praneel-mohan" target="_blank" rel="noopener">LinkedIn</a>
<a class="btn btn-ghost-dark" href="https://wa.me/917678627973" target="_blank" rel="noopener">WhatsApp</a>
</div>
</div>
</div>
</section>
</main>
<footer class="site-foot">
<div class="wrap">
<span>© <span id="year">2026</span> Praneel Mohan, Gurugram, India</span>
<span>Figures are reported campaign and channel results.</span>
</div>
</footer>
<script src="js/pm.js"></script>
</body>
</html>
'''


def vtile(vid, title, meta='', ratio='r916', cap=False, lazy=True):
    ld = ' loading="lazy"' if lazy else ''
    if cap:
        inner = f'<span class="cap">{e(title)}</span>'
    else:
        inner = f'{PLAY}<span class="shade"></span><span class="over"><b>{e(title)}</b><span>{e(meta)}</span></span>'
    return (f'<button class="tile {ratio}" type="button" data-video="{vid}" data-title="{e(title)}" aria-label="Play video: {e(title)}">'
            f'<img src="assets/posters/{vid}.webp" alt=""{ld}>{inner}</button>')


def itile(src, title, meta='', ratio='r169', below=False):
    if below:
        return (f'<figure class="thumb"><button class="tile {ratio}" type="button" data-img="{src}" data-title="{e(title)}" aria-label="View larger: {e(title)}">'
                f'<img src="{src}" alt="{e(title)}" loading="lazy"></button><figcaption>{e(title)}</figcaption></figure>')
    return (f'<button class="tile {ratio}" type="button" data-img="{src}" data-title="{e(title)}" aria-label="View larger: {e(title)}">'
            f'<img src="{src}" alt="{e(title)}" loading="lazy"><span class="shade"></span><span class="over"><b>{e(title)}</b><span>{e(meta)}</span></span></button>')


# ---------- data ----------
META = [18, 22, 30, 35, 45, 52, 55, 52, 48, 45, 40, 33, 20]
SRCH = [3, 4, 6, 7, 8, 8, 9, 8, 8, 8, 7, 7, 5]
RMM = [5, 6, 8, 10, 12, 12, 13, 13, 13, 12, 12, 12, 12]
RMG = [4, 5, 7, 9, 11, 11, 12, 11, 11, 11, 10, 10, 15]


def chart(height, label_px, axis_full=False):
    k = (height - 30) / 89
    weeks = []
    for i in range(13):
        tot = META[i] + SRCH[i] + RMM[i] + RMG[i]
        weeks.append(
            f'<div class="wk{" peak" if tot == 89 else ""}"><b>{tot}</b><div class="stack" style="transition-delay:{i*0.05:.2f}s">'
            f'<i class="c-rmg" style="height:{RMG[i]*k:.1f}px"></i><i class="c-srch" style="height:{SRCH[i]*k:.1f}px"></i>'
            f'<i class="c-rmm" style="height:{RMM[i]*k:.1f}px"></i><i class="c-meta" style="height:{META[i]*k:.1f}px"></i></div></div>')
    aria = 'Stacked weekly leads by channel over 13 weeks: 30, 37, 51, 61, 76, 83, 89, 84, 80, 76, 69, 62 and 52, a total of 850'
    out = f'<div class="chart" role="img" aria-label="{aria}" style="height:{height}px">{"".join(weeks)}</div>'
    if axis_full:
        out += '<div class="chart-axis full" style="padding-top:10px">' + ''.join(f'<span>W{i+1}</span>' for i in range(13)) + '</div>'
    else:
        out += '<div class="chart-axis"><span>Week 1</span><span>Week 7, peak</span><span>Week 13</span></div>'
    return out


def legend(counts=False):
    c = (' 495', ' 140', ' 88', ' 127') if counts else ('', '', '', '')
    return (f'<div class="legend"><span><i class="c-meta"></i>Meta prospecting{c[0]}</span><span><i class="c-rmm"></i>Meta remarketing{c[1]}</span>'
            f'<span><i class="c-srch"></i>Google Search{c[2]}</span><span><i class="c-rmg"></i>Google remarketing{c[3]}</span></div>')


FEATURE = f'''<a href="performance.html" class="feature" data-reveal>
<div class="feature-copy">
<div style="display:flex;flex-direction:column;gap:16px">
<p class="muted" style="font-size:14px">ZycomTech, real-estate client, Meta and Google Ads</p>
<h3 class="disp">850 leads in 90 days</h3>
<p class="soft">A learn, scale and optimise plan across Meta prospecting, Google Search and remarketing on both, with leads tracked by channel every week.</p>
</div>
<div class="mini-stats">
<div><b>₹1,752</b><span>blended cost per lead</span></div>
<div><b>2.32%</b><span>click-through rate</span></div>
<div><b>₹11K</b><span>under budget</span></div>
</div>
<span class="link-strong accent">Read the case study {ARROW}</span>
</div>
<div class="feature-chart">{legend()}{chart(300, 11)}</div>
</a>'''

REEL_GROUPS = [  # (group, [(id, title, meta)])
    ('Brand promotion', [
        ('VAG4z-OmH3o', 'Kapiva Spirulina', 'Brand promotion'),
        ('VAG4z1-SOzk', 'Kapiva Shilajit', 'Brand promotion'),
        ('VAG4zysH5bw', 'Kapiva Moringa', 'Brand promotion')]),
    ('Food and hospitality', [
        ('VAG4zjjMj7Y', 'Bitsy Boxy', 'Food product reel'),
        ('VAG4ziel6NI', 'Food preparation', 'Food reel'),
        ('drive-video-6', 'Event atmosphere', 'Hospitality reel')]),
    ('Creator and celebrity edits', [
        ('VAG4zvDab8s', 'Rapid Fire', 'Celebrity interview edit'),
        ('VAGmtyAPNbM', '0126 campaign', 'Creator agency, vertical edit')]),
    ('UGC edits', [
        ('VAG4zo2XV58', 'NG', 'UGC edit'),
        ('VAG4znXqyQI', 'Media Grow', 'UGC edit'),
        ('VAG4zt3yu4k', 'Aviation', 'UGC edit'),
        ('VAGoEtd8oIY', 'Passionbits', 'UGC edit')]),
    ('Originals and short-form', [
        ('VAG4z64Z9wI', 'Save Animals', 'Camera, direction and edit'),
        ('VAG4z97kjZE', 'Street story', 'Camera, direction and edit'),
        ('VAG4zwJntWc', 'Original reel', 'Camera, direction and edit'),
        ('VAG4zywB95Y', 'Mountain trip', 'Camera, direction and edit'),
        ('VAGmt5tVHhA', 'Cows Go Moo', 'Short-form edit'),
        ('VAGmt3QOyyg', 'EC', 'Creative edit')]),
]
REELS = [r for _, g in REEL_GROUPS for r in g]
FILMS = [
    ('VAG4zxmpw38', 'Bageshwar Dham', 'Spiritual and events, video edit'),
    ('VAGmt40SPCY', '0126 campaign film', 'Creator agency'),
    ('VAGmt0Tu-ZU', 'Bharat', 'Intro sequence'),
    ('VAGoEnGz3QU', 'Olmec civilisation', 'Long-form YouTube'),
    ('drive-video-1', 'Residential development', 'Property film'),
    ('drive-video-2', 'Shree Nilay walkthrough', 'Property film'),
]
THUMBS = [
    ('revcore-z4.webp', 'BMW Z4, crazy exhaust modification'),
    ('swift-vs-thar-roxx.webp', 'Swift destroyed by Thar Roxx'),
    ('polo-all-this-work.webp', 'Polo, all this work at this price?'),
    ('ciaz-flooded-roads.webp', 'Ciaz, one mistake and a huge repair bill'),
    ('bmw-z4-back-for-more-repairs.webp', 'BMW Z4, back for more repairs'),
]
LATEST = [  # three latest uploads on youtube.com/@Revcoreautos, checked 17 Nov 2026
    ('ge5dUh1kK9M', 'This VW Polo came with a lot of problems: head overhaul, AC repair, water pump and more (Part 1)'),
    ('TGNPYOFgqsw', 'Swift crashed into Thar Roxx: full front damaged'),
    ('yCYkZWGk7FE', 'Brand new Thar Roxx hit by Swift: major damage'),
]
SG = [('IMG_8289', 'A location that upgrades how you live'), ('IMG_8299', 'Grand arrival'), ('IMG_8301', 'A balcony away')]

CLIENTS = [
    ('Rapido', 'https://www.instagram.com/rapidoapp/'), ('Lenskart', 'https://www.instagram.com/lenskart/'),
    ('Kapiva', 'https://www.instagram.com/kapiva_official/'), ('Signature Global', 'https://www.instagram.com/signatureglobal/'),
    ('TPH Group', 'https://www.instagram.com/yallamaids/'), ('RevCore Autos', 'https://www.youtube.com/@Revcoreautos'),
    ("U'th Times", 'https://www.instagram.com/uthtimes01/'), ('TAKE1', None),
    ('ZycomTech', 'https://www.linkedin.com/company/zycomtech/'), ('Bageshwar Dham', 'https://www.instagram.com/iambageshwardhamsarkar/'),
    ('Sort Marketing', 'https://www.instagram.com/sortmarketing/'), ('Bloofy', 'https://www.instagram.com/bloofy.co/'),
    ('ReachHub', None), ('Zeyar', None), ('Paridhi', None),
]


# ---------- index ----------
def page_index():
    results = [
        ('850', '', 'leads in 90 days', 'Meta and Google Ads for a real-estate client at ZycomTech'),
        ('110', 'K', 'followers, up from 25K', "U'th Times, in six months of content planning, production and editing"),
        ('1', 'M', 'views in 3 months', 'TAKE1 social video, planned, produced and edited for retention'),
        ('10', '+', 'client accounts', 'Managed end to end, with repeat work from retained clients'),
    ]
    ledger = ''.join(f'<div class="cell"><p class="disp big"><span data-count="{n}" data-suf="{s}">{n}{s}</span></p><p class="what">{w}</p><p class="where">{e(x)}</p></div>' for n, s, w, x in results)

    cards = [
        ('work.html#creative', 'assets/revcore-z4.webp', 'RevCore Autos thumbnail of a BMW Z4 exhaust modification', 'RevCore Autos, YouTube', 'Content for a 54.9K-subscriber channel', 'Repair-story videos, short-form edits and click-worthy thumbnails for an automotive workshop.'),
        ('work.html#creative', 'assets/creatives/IMG_8289.webp', 'Signature Global creative showing a high-rise at night', 'Signature Global, real estate', 'Property campaign creatives', 'Static campaign creatives for a Gurugram real-estate developer.'),
        ('work.html#video', 'assets/posters/VAG4z-OmH3o.webp', 'Creator holding a Kapiva Spirulina bottle in the mountains', 'Kapiva, Rapid Fire and more', 'Brand and creator videos', 'Brand promotions, creator and celebrity edits, UGC and original reels.'),
    ]
    cardh = ''.join(
        f'<a href="{h}" class="card" data-reveal><div class="ph"><img src="{i}" alt="{e(a)}" loading="lazy"></div>'
        f'<div style="display:flex;flex-direction:column;gap:8px"><p class="muted" style="font-size:14px">{e(m)}</p><h3 class="disp">{e(t)}</h3>'
        f'<p class="soft" style="font-size:16px">{e(b)}</p></div></a>' for h, i, a, m, t, b in cards)

    services = [
        ('Performance marketing', 'Meta and Google Ads campaigns built to bring in leads, with budgets paced and cost per lead checked every week.', ['Meta Ads Manager', 'Google Search', 'Remarketing', 'Lead generation', 'Weekly reporting']),
        ('Social media management', 'Content strategy, calendars and copy, published on a steady schedule in one consistent brand voice.', ['Content strategy', 'Copywriting', 'Short-form video', 'Digital PR', 'Channel growth']),
        ('Client servicing', "The client's point of contact: briefs, timelines, reviews and follow-ups, with design, web, SEO and video teams kept in step.", ['10+ accounts', 'Briefs and timelines', 'Performance reviews', 'Pitching', 'HubSpot CRM']),
    ]
    svch = ''.join(f'<div class="svc" data-reveal><h3 class="disp">{t}</h3><p class="soft" style="font-size:16px">{e(b)}</p><ul class="tags">{"".join(f"<li>{e(x)}</li>" for x in tags)}</ul></div>' for t, b, tags in services)

    def cl(i, n, u):
        cls = ' class="hl"' if i % 3 == 0 else ''
        if u:
            return f'<a{cls} href="{u}" target="_blank" rel="noopener">{e(n)}</a>'
        return f'<a{cls} href="work.html">{e(n)}</a>'
    one = ''.join(cl(i, n, u) for i, (n, u) in enumerate(CLIENTS))
    two = one.replace('<a', '<a tabindex="-1" aria-hidden="true"')

    jobs = [('Mar 2026 – now', 'Content & YouTube Executive', 'RevCore Autos'),
            ('Apr 2025 – Mar 2026', 'Client Servicing & Digital Marketing Executive', 'ZycomTech'),
            ('Jan 2025 – Oct 2026', 'Freelance & Contract Marketing', '10+ clients incl. Rapido, TAKE1, TPH Group'),
            ('Apr 2025 – Sep 2025', 'Social Media Content Producer', "U'th Times / YTV Network")]
    jobh = ''.join(f'<a href="about.html" class="row"><span class="muted" style="font-size:14px">{w}</span><span class="disp">{e(r)}</span><span class="soft">{e(o)}</span><span class="arrow">{ARROW}</span></a>' for w, r, o in jobs)

    body = f'''<section class="hero" aria-labelledby="hero-title">
<div class="wrap hero-grid">
<div class="hero-copy">
<p class="muted fade" style="font-size:15px">Social media and performance marketing, Gurugram or remote</p>
<h1 id="hero-title" class="disp"><span class="line"><span>Social and paid</span></span> <span class="line"><span>media that brings</span></span> <span class="line"><span>in <span class="accent">leads.</span></span></span></h1>
<p class="lede fade">I run Meta and Google Ads, manage social channels and look after clients end to end. Nearly two years across agency, freelance and in-house roles, for brands in India, the USA and the UAE.</p>
<div class="cta-row fade">
<a class="btn btn-solid btn-lg" href="work.html">See my work {ARROW}</a>
</div>
<p class="trust fade">10+ client accounts, including Rapido, Kapiva, Signature Global and TPH Group.</p>
</div>
<div class="hero-art" aria-hidden="true">
<div class="glow"></div>
<div class="ring r1"><span class="dot d1"></span><span class="dot d2"></span></div>
<div class="ring r2"><span class="dot d3"></span></div>
<div class="phone">
<video autoplay muted loop playsinline preload="auto" poster="assets/posters/VAG4zvDab8s.webp"><source src="assets/videos/VAG4zvDab8s.mp4" type="video/mp4"></video>
<div class="ph-bar"><i></i><i></i><i></i></div>
<div class="ph-side"><span class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg><b>12.4K</b></span><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg><b>318</b></span><span class="ic"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 2L11 13M22 2l-7 20-4-9-9-4 20-7z"/></svg><b>Share</b></span></div>
<div class="hearts"><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg></span><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg></span><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg></span><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg></span><span><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 21s-7.5-4.6-9.5-9.2C1.2 8.7 3.2 5 6.7 5c2 0 3.4 1.1 4.3 2.4h2C13.9 6.1 15.3 5 17.3 5c3.5 0 5.5 3.7 4.2 6.8C19.5 16.4 12 21 12 21z"/></svg></span></div>
</div>
<div class="toast t1"><span class="ti lime"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M20 6L9 17l-5-5"/></svg></span><span><b>New lead</b><small>Meta Ads, just now</small></span></div>
<div class="toast t2"><span class="ti saf"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"><path d="M3 17l6-6 4 4 8-8M15 7h6v6"/></svg></span><span><b>+14K followers</b><small>an average month at U'th Times</small></span></div>
<div class="toast t4"><span class="ti dark"><svg viewBox="0 0 200 64" preserveAspectRatio="none" class="mini-spark"><polyline points="0.0,42.5 16.7,38.4 33.3,30.2 50.0,24.4 66.7,15.6 83.3,11.5 100.0,8.0 116.7,10.9 133.3,13.3 150.0,15.6 166.7,19.7 183.3,23.8 200.0,29.6"/></svg></span><span><b>850 leads</b><small>in 90 days, peak in week 7</small></span></div>
<div class="toast t3"><span class="ti rust"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.5"/></svg></span><span><b>CTR 2.32%</b><small>Meta + Google, 90 days</small></span></div>
</div>
</div>
</section>

<section class="ledger" aria-label="Results">
<div class="wrap">{ledger}</div>
</section>

<section class="sec" aria-labelledby="work-title" style="padding-bottom:40px">
<div class="wrap">
<div class="sec-head"><h2 id="work-title" class="disp h2">Selected work</h2><a class="link-strong" href="work.html">All work {ARROW}</a></div>
{FEATURE}
<a href="uth-times.html" class="case-split" data-reveal>
<span class="cs-copy"><span style="font-size:15px">U'th Times, case study</span>
<span style="display:flex;flex-direction:column;gap:16px"><span class="disp big">25K → 110K</span><span style="font-size:19px;max-width:520px">Followers in six months for India's youth media brand, through planning, filming and editing.</span></span>
<span class="go">Read the case study {ARROW}</span></span>
<span class="cs-art"><img src="assets/uth-times-frame.webp" alt="U'th Times logo" loading="lazy"></span>
</a>
<div class="grid-3">{cardh}</div>
</div>
</section>

<section class="sec" aria-labelledby="do-title">
<div class="wrap">
<div class="sec-head"><h2 id="do-title" class="disp h2">What I do</h2><p class="muted" style="max-width:440px">Three jobs I can own from day one, backed by the video and design skills that keep content moving.</p></div>
<div class="grid-3">{svch}</div>
<p class="band">Also on the team: short-form and YouTube editing, thumbnails and campaign creatives in Premiere Pro, DaVinci Resolve and Canva, plus reporting in Excel and SQL and automations in n8n.</p>
</div>
</section>

<section aria-labelledby="clients-title" style="padding:0 0 120px">
<h2 id="clients-title" class="wrap muted" style="font-size:15px;font-weight:500;margin-bottom:28px">Brands I've worked on, directly or through agencies</h2>
<div class="marquee-box"><div class="marquee">{one}{two}</div></div>
</section>

<section aria-labelledby="exp-title" style="padding-bottom:120px">
<div class="wrap">
<div class="sec-head" style="margin-bottom:32px"><h2 id="exp-title" class="disp h2">Experience</h2><a class="link-strong" href="about.html">Full experience and skills {ARROW}</a></div>
<div class="rows">{jobh}</div>
</div>
</section>
'''
    return head('Praneel Mohan | Social Media & Performance Marketing', 'Praneel Mohan runs Meta and Google Ads, manages social media and looks after clients end to end. 850 leads in 90 days, 25K to 110K followers in six months.', 'index.html') + body + foot()


# ---------- work ----------
def page_work():
    reels = ''.join(f'<div class="rgroup" style="--n:{len(items)}"><h3 class="sub-h">{e(g)} <small>{len(items)}</small></h3><div class="reel-grid">' + ''.join(vtile(v, ti, m) for v, ti, m in items) + '</div></div>' for g, items in REEL_GROUPS)
    films = ''.join(vtile(v, t, m, ratio='r169') for v, t, m in FILMS)
    thumbs = ''.join(itile(f'assets/{f}', t, below=True) for f, t in THUMBS)
    latest = ''.join(f'<a class="yt" href="https://www.youtube.com/watch?v={v}" target="_blank" rel="noopener"><span class="yt-ph"><img src="https://i.ytimg.com/vi/{v}/hqdefault.jpg" alt="" loading="lazy"><span class="play" aria-hidden="true"><svg width="16" height="16" viewBox="0 0 24 24" fill="currentColor"><path d="M8 5v14l11-7z"/></svg></span></span><span class="yt-t">{e(ti)}</span><span class="yt-l">Watch on YouTube</span></a>' for v, ti in LATEST)
    sg = ''.join(itile(f'assets/creatives/{f}.webp', t, 'Signature Global creative', ratio='r916') for f, t in SG)
    counts = {'all': 1 + 4 + len(REELS) + len(FILMS) + len(LATEST) + len(THUMBS) + len(SG), 'performance': 1, 'social': 4,
              'video': len(REELS) + len(FILMS) + len(LATEST), 'creative': len(THUMBS) + len(SG)}
    chips = [('all', 'All work'), ('performance', 'Performance marketing'), ('social', 'Social media'), ('video', 'Video'), ('creative', 'Thumbnails & creatives')]
    chiph = ''.join(f'<button class="chip" type="button" data-filter="{k}" aria-pressed="{"true" if k == "all" else "false"}">{t} <small>{counts[k]}</small></button>' for k, t in chips)

    body = f'''<section class="page-head">
<div class="wrap" style="display:flex;justify-content:space-between;align-items:flex-end;gap:32px;flex-wrap:wrap">
<div style="display:flex;flex-direction:column;gap:18px;max-width:780px">
<h1 class="disp">Work</h1>
<p class="lede">Campaigns, channel growth, brand and creator edits, thumbnails and creatives. Pick the kind of work you are hiring for.</p>
</div>
</div>
</section>

<div class="filters"><div class="wrap" role="group" aria-label="Filter work">{chiph}</div></div>

<div class="wrap" style="padding-bottom:120px">
<section class="wsec" data-cat="performance" aria-labelledby="w-perf">
<div class="wsec-head"><h2 id="w-perf" class="disp">Performance marketing</h2><p>Paid campaigns, planned with forecasts and reported every week.</p></div>
{FEATURE}
</section>

<section class="wsec" data-cat="social" aria-labelledby="w-social">
<div class="wsec-head"><h2 id="w-social" class="disp">Social media</h2><p>Channel growth, content strategy and publishing for brands and pages.</p></div>
<a href="uth-times.html" class="case-split" data-reveal>
<span class="cs-copy"><span style="font-size:15px">U'th Times, case study</span>
<span style="display:flex;flex-direction:column;gap:16px"><span class="disp big">25K → 110K</span><span style="font-size:19px;max-width:520px">Followers in six months for India's youth media brand, through planning, filming and editing.</span></span>
<span class="go">Read the case study {ARROW}</span></span>
<span class="cs-art"><img src="assets/uth-times-frame.webp" alt="U'th Times logo"></span>
</a>
<div class="stat-cards">
<div class="stat-card sf" data-reveal><span class="sc-k">TAKE1</span><p class="disp sc-h">1M views</p><p>In 3 months, from social video planned, produced and edited for retention.</p></div>
<div class="stat-card" data-reveal><span class="sc-k">TPH Group, Dubai</span><p class="disp sc-h">Social for a services group</p><p class="soft">Content strategy and publishing that turned workforce, facility and cleaning services into clear posts for homes and businesses.</p><a class="link-strong sc-link" href="https://www.instagram.com/yallamaids/" target="_blank" rel="noopener">See on Instagram {ARROW}</a></div>
<div class="stat-card" data-reveal><span class="sc-k">Artist pages</span><p class="disp sc-h">Social and digital PR</p><p class="soft">Managed social content and digital PR for music artist pages as part of freelance work.</p></div>
</div>
</section>

<section class="wsec" data-cat="video" aria-labelledby="w-reels">
<div class="wsec-head"><h2 id="w-reels" class="disp">Reels and short-form</h2><p>Grouped by type of video. Select one to play.</p></div>
<div class="reel-groups">{reels}</div>
</section>

<section class="wsec" data-cat="video" aria-labelledby="w-films">
<div class="wsec-head"><h2 id="w-films" class="disp">Films and long-form</h2><p>Event edits, campaign films, intros, YouTube explainers and property films.</p></div>
<div class="wide-grid">{films}</div>
</section>

<section class="wsec" data-cat="video creative" aria-labelledby="w-yt">
<div class="wsec-head"><h2 id="w-yt" class="disp">RevCore Autos on YouTube</h2><p>Repair-story videos and thumbnails for a 54.9K-subscriber automotive channel. <a href="https://www.youtube.com/@Revcoreautos" target="_blank" rel="noopener">Visit the channel</a></p></div>
<h3 class="sub-h">Latest videos</h3>
<div class="yt-grid">{latest}</div>
<h3 class="sub-h">Thumbnail picks</h3>
<div class="bento">{thumbs}</div>
</section>

<section class="wsec" data-cat="creative" aria-labelledby="w-sg">
<div class="wsec-head"><h2 id="w-sg" class="disp">Signature Global creatives</h2><p>Static campaign creatives for a Gurugram real-estate developer.</p></div>
<div class="creative-grid">{sg}</div>
</section>
</div>
'''
    return head('Work | Praneel Mohan', 'Campaigns, social media growth, brand and creator video edits, YouTube thumbnails and property creatives by Praneel Mohan.', 'work.html') + body + foot()


# ---------- performance ----------
def page_perf():
    kpis = [('850', '', '', 'reported leads', True), ('1752', '₹', '', 'blended cost per lead', False), ('2.32', '', '%', 'click-through rate', False),
            ('14.89', '₹', 'L', 'spend of ₹15L budget', False), ('16', '', ' lakh', 'impressions', False), ('37120', '', '', 'clicks', False)]
    kh = ''.join(f'<div class="k"><b{ACC if hot else ""}><span data-count="{n}" data-pre="{p}" data-suf="{s}">{p}{n}{s}</span></b><span>{l}</span></div>' for n, p, s, l, hot in kpis)
    phases = [('01', 'weeks 1–2', 'Learning', 'Let the platforms learn, test audiences and set the baseline.', '#6f7d12'),
              ('02', 'weeks 3–4', 'Ramp-up', 'Shift budget to what converted; lead volume climbs fast.', '#c1df1f'),
              ('03', 'weeks 5–8', 'Peak', 'Highest volume across every channel, topping out at 89 in week 7.', '#faa613'),
              ('04', 'weeks 9–13', 'Optimise', 'A steady, efficient run that kept results consistent to the end.', '#fdd892')]
    ph = ''.join(f'<li style="--c:{c}" data-reveal><span class="n">{n}, {w}</span><span class="disp">{t}</span><p>{b}</p></li>' for n, w, t, b, c in phases)
    rows = [('Meta prospecting', '₹7,80,000', '460–530', '495', '₹1,500–1,700', '₹1,576', '1.20%'),
            ('Google Search', '₹3,10,000', '75–110', '88', '₹3,000–4,000', '₹3,523', '6.00%'),
            ('Meta remarketing', '₹2,20,000', '105–160', '140', '₹2,000–3,000', '₹1,571', '2.50%'),
            ('Google remarketing', '₹1,78,989', '60–100', '127', '₹1,500–2,500', '₹1,409', '3.97%')]
    rh = ''.join(f'<tr><td>{a}</td><td>{b}</td><td class="muted">{c}</td><td class="hot">{d}</td><td class="muted">{x}</td><td>{f}</td><td>{g}</td></tr>' for a, b, c, d, x, f, g in rows)
    body = f'''<section class="page-head">
<div class="wrap">
<nav class="crumb" aria-label="Breadcrumb"><a href="work.html">Work</a> / Performance marketing</nav>
<div class="hero-grid" style="align-items:end">
<div style="display:flex;flex-direction:column;gap:24px">
<h1 class="disp">850 leads in <span class="accent">90 days.</span></h1>
<p class="lede" style="font-size:20px">A Meta and Google Ads lead-generation campaign for a real-estate developer, planned with forecast ranges and run on a learn, scale and optimise plan.</p>
</div>
<dl class="meta-box">
<div><dt>Client</dt><dd>Real-estate developer, name withheld</dd></div>
<div><dt>Agency</dt><dd>ZycomTech</dd></div>
<div><dt>My role</dt><dd>Campaign execution, weekly tracking and client reviews</dd></div>
<div><dt>Channels</dt><dd>Meta, Google Search, remarketing on both</dd></div>
</dl>
</div>
</div>
</section>

<section class="kpis" aria-label="Headline results"><div class="wrap">{kh}</div></section>

<section class="sec" style="padding-bottom:0"><div class="wrap two-col">
<div data-reveal><h2 class="disp">The brief</h2><p class="soft">Bring in property enquiries across three moments: people discovering the project, people actively searching for homes, and people who had already shown interest. The approved budget was ₹15,00,000 for 90 days.</p></div>
<div data-reveal><h2 class="disp">The approach</h2><p class="soft">Each channel got an estimated range for leads, cost per lead and CTR before launch. Leads were tracked weekly by channel in Excel, and budget moved toward whatever converted. Results went back to the client in regular performance reviews with next-step recommendations.</p></div>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="phases"><div class="wrap">
<h2 id="phases" class="disp h2" style="margin-bottom:40px">Learn. Ramp up. Peak. Optimise.</h2>
<ol class="phases">{ph}</ol>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="weekly"><div class="wrap">
<div class="sec-head" style="margin-bottom:32px"><h2 id="weekly" class="disp h2">Leads, week by week</h2>{legend(True)}</div>
<div class="chart-box">{chart(380, 13, True)}</div>
<p class="footnote">Reported leads from the campaign report, not confirmed sales. Weekly totals add up to 850.</p>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="planned"><div class="wrap">
<div class="growth" style="grid-template-columns:minmax(0,4fr) minmax(0,8fr);align-items:start">
<div style="display:flex;flex-direction:column;gap:16px"><h2 id="planned" class="disp h2">Planned it. Then hit it.</h2><p class="soft">Every channel launched with a forecast range. Total leads, cost per lead and CTR all landed inside it, and spend finished ₹11,011 under budget.</p></div>
<div class="tbl-box"><table>
<thead><tr><th scope="col">Channel</th><th scope="col">Spend</th><th scope="col">Est. leads</th><th scope="col">Leads</th><th scope="col">Est. CPL</th><th scope="col">CPL</th><th scope="col">CTR</th></tr></thead>
<tbody>{rh}<tr class="total"><td>Total</td><td>₹14,88,989</td><td class="muted">700–900</td><td class="hot">850</td><td class="muted">₹1,700–2,200</td><td>₹1,752</td><td>2.32%</td></tr></tbody>
</table></div>
</div>
<p class="footnote">Source: ZycomTech campaign report. Cost per lead is spend divided by reported leads.</p>
</div></section>

<section class="sec"><div class="wrap">
<a href="uth-times.html" class="next"><span style="display:flex;flex-direction:column;gap:8px"><span style="font-size:14px">Next case study</span><span class="disp">U'th Times: 25K to 110K followers</span></span><svg aria-hidden="true" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div></section>
'''
    return head('850 leads in 90 days | Praneel Mohan', 'Case study: a 90-day Meta and Google Ads campaign for a real-estate client that delivered 850 leads at ₹1,752 cost per lead.', 'performance.html') + body + foot()


# ---------- U'th Times ----------
def page_uth():
    kpis = [('25', '', 'K', 'followers at the start', False), ('110', '', 'K', 'followers six months later', True),
            ('4.4', '', 'x', 'growth in the following', False), ('85', '+', 'K', 'new followers', False),
            ('14', '~', 'K', 'added per month, on average', False), ('6', '', '', 'months, part-time', False)]
    kh = ''.join(f'<div class="k"><b{ACC if hot else ""}><span data-count="{n}" data-pre="{p}" data-suf="{s}">{p}{n}{s}</span></b><span>{l}</span></div>' for n, p, s, l, hot in kpis)
    steps = [('Plan the idea', 'Pitch topics that young Indians already talk about, shape each one around a single hook, and slot it into a weekly content calendar.'),
             ('Film it', 'Shoot on location and with real people, capturing extra angles and reactions so the edit has room to move.'),
             ('Cut for retention', 'Open on the strongest moment, keep the pace tight, add captions for silent viewing and finish in the brand look.'),
             ('Publish and learn', 'Post on a steady schedule, check what held attention, and feed those lessons into the next round of ideas.')]
    sh = ''.join(f'<li data-reveal><h3 class="disp">{t}</h3><p>{b}</p></li>' for t, b in steps)
    icons = {
        'hook': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M13 2L3 14h9l-1 8 10-12h-9l1-8z"/></svg>',
        'cut': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><circle cx="6" cy="6" r="3"/><circle cx="6" cy="18" r="3"/><path d="M20 4L8.12 15.88M14.47 14.48L20 20M8.12 8.12L12 12"/></svg>',
        'cal': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/></svg>',
        'voice': '<svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M21 15a2 2 0 0 1-2 2H7l-4 4V5a2 2 0 0 1 2-2h14a2 2 0 0 1 2 2z"/></svg>',
    }
    principles = [('hook', 'Win the first second', 'Every video opened on its most surprising line or image. If the first frame did not stop the scroll, nothing after it mattered.'),
                  ('cut', 'Edit for the rewatch', 'Tight cuts, no dead air, and an ending that loops or pays off, so people watch to the end and share it on.'),
                  ('cal', 'Show up every week', 'A planned calendar kept posts going out on schedule, so new viewers always had a reason to follow for the next one.'),
                  ('voice', "Sound like U'th Times", "Young, direct and honest. Every piece stayed in the brand's voice, so growth built one recognisable identity.")]
    pr = ''.join(f'<div class="principle" data-reveal><span class="ic" aria-hidden="true">{icons[i]}</span><div><h3 class="disp">{t}</h3><p>{b}</p></div></div>' for i, t, b in principles)

    body = f'''<section class="uth-hero" aria-labelledby="uth-title">
<div class="wrap uth-grid">
<div>
<nav class="crumb" aria-label="Breadcrumb"><a href="work.html">Work</a> / Social media</nav>
<h1 id="uth-title" class="disp">25K<br><span class="to">→ 110K</span></h1>
<p class="sub">Followers in six months for U'th Times, India's youth media brand. Here is how planning, filming and editing every week more than quadrupled its audience.</p>
</div>
<img class="logo" src="assets/uth-times-frame.webp" alt="U'th Times logo">
</div>
</section>

<section class="kpis" aria-label="Headline results"><div class="wrap">{kh}</div></section>

<section class="sec" style="padding-bottom:0"><div class="wrap">
<dl class="meta-box" style="grid-template-columns:repeat(4,minmax(0,1fr))" data-reveal>
<div><dt>Brand</dt><dd>U'th Times, part of YTV Network</dd></div>
<div><dt>My role</dt><dd>Social Media Content Producer</dd></div>
<div><dt>Timeline</dt><dd>Apr to Sep 2025, part-time, remote</dd></div>
<div><dt>What I owned</dt><dd>Content planning, filming and editing</dd></div>
</dl>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="jump"><div class="wrap growth">
<div style="display:flex;flex-direction:column;gap:20px" data-reveal>
<h2 id="jump" class="disp h2">The jump, at a glance</h2>
<p class="soft">In April the channel had 25,000 followers. By September it had 110,000. That is 85,000 new people choosing to follow, or roughly 14,000 every month, while I worked on it part-time.</p>
<p class="soft">The brand already had a large YouTube audience. The opportunity was to bring that energy to short-form social, where a follow has to be earned in seconds.</p>
</div>
<div>
<div class="gbars" role="img" aria-label="Followers grew from 25,000 in April 2025 to 110,000 in September 2025">
<div class="gbar"><span class="val">25K</span><div class="fill" style="--h:92px;background:#3a3b44"></div><span class="lab">April 2025</span></div>
<div class="gap-tag">+340%<small>4.4x the audience</small></div>
<div class="gbar"><span class="val accent">110K</span><div class="fill" style="--h:400px;background:var(--saffron);transition-delay:.15s"></div><span class="lab">September 2025</span></div>
</div>
</div>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="how"><div class="wrap">
<div class="sec-head"><h2 id="how" class="disp h2">How each video got made</h2><p class="muted" style="max-width:440px">I took ideas all the way from concept to the final cut, so the brand's voice stayed intact at every step.</p></div>
<ol class="steps">{sh}</ol>
</div></section>

<section class="quote-band" style="margin-top:120px"><div class="wrap">
<p data-reveal>Every video had one job: make a stranger <span class="accent">stop scrolling</span>, then give them a reason to <span class="accent">follow for the next one.</span></p>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="why"><div class="wrap">
<div class="sec-head"><h2 id="why" class="disp h2">What made it work</h2></div>
<div class="principles">{pr}</div>
</div></section>

<section class="sec" style="padding-bottom:0" aria-labelledby="see"><div class="wrap">
<div class="feature" style="grid-template-columns:minmax(0,1fr);background:var(--ink-3)">
<div class="feature-copy" style="gap:24px">
<h2 id="see" class="disp" style="font-size:clamp(30px,3.5vw,44px)">See U'th Times today</h2>
<p class="soft" style="max-width:640px">The brand keeps growing across platforms, including a YouTube channel with 618K subscribers.</p>
<div class="links-row">
<a class="btn btn-solid" href="https://www.instagram.com/uthtimes01/" target="_blank" rel="noopener">Instagram</a>
<a class="btn btn-line" href="https://www.youtube.com/@uthtimes" target="_blank" rel="noopener">YouTube</a>
<a class="btn btn-line" href="https://uthtimes.com" target="_blank" rel="noopener">uthtimes.com</a>
</div>
</div>
</div>
</div></section>

<section class="sec"><div class="wrap">
<a href="performance.html" class="next"><span style="display:flex;flex-direction:column;gap:8px"><span style="font-size:14px">Next case study</span><span class="disp">850 leads in 90 days</span></span><svg aria-hidden="true" width="48" height="48" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div></section>
'''
    return head("U'th Times: 25K to 110K followers | Praneel Mohan", "Case study: how Praneel Mohan helped U'th Times grow from 25K to 110K followers in six months through content planning, filming and editing.", 'performance.html') + body + foot()


# ---------- about ----------
def page_about():
    CASES = {"U'th Times / YTV Network": f'<a class="link-strong job-link" href="uth-times.html">Read the U\'th Times case study {ARROW}</a>',
             'ZycomTech': f'<a class="link-strong job-link" href="performance.html">Read the 850-lead case study {ARROW}</a>'}
    jobs = [
        ('Mar 2026 – present', 'Full-time, Gurugram', 'Content & YouTube Executive', 'RevCore Autos', [
            'Plan and deliver content for an automotive YouTube channel of about 54.9K subscribers and its workshop: videos, short-form edits and thumbnails.',
            'Track video performance and recommend improvements to engagement and retention.']),
        ('Apr 2025 – Mar 2026', 'Full-time, Delhi, hybrid', 'Client Servicing & Digital Marketing Executive', 'ZycomTech', [
            'Client point of contact at an award-winning 360° digital marketing agency with 30+ active clients, for India and USA accounts in real estate, FMCG, insurance and media.',
            'Ran a 90-day Meta and Google Ads lead-generation campaign for a real-estate client that delivered 850 leads.',
            'Tracked leads weekly by channel in Excel and presented performance reviews and recommendations to clients.',
            'Scoped briefs and timelines and coordinated design, web, SEO, social and video teams to deliver on time.']),
        ('Jan 2025 – Oct 2026', 'Freelance and contract', 'Freelance & Contract Marketing', '10+ clients', [
            'Managed 10+ accounts end to end across education, fashion, automotive and marketing, winning repeat work.',
            'Closed 4 creative-services deals through pitches and follow-ups, with the pipeline in HubSpot CRM.',
            'Produced video campaigns for Rapido, contributed to 1M views in 3 months for TAKE1, and ran content and social for TPH Group in Dubai.',
            'Reported results in Excel and SQL and built n8n automations and SOPs for content workflows.']),
        ('Apr 2025 – Sep 2025', 'Part-time, remote', 'Social Media Content Producer', "U'th Times / YTV Network", [
            'Helped grow the channel from 25K to 110K followers in 6 months, about 14K new followers a month, through content planning, production and editing.',
            'Pitched topics around what young Indians were talking about and planned them into a weekly content calendar.',
            'Filmed on location and with real people, then edited for retention: strong opening hooks, tight pacing and captions for silent viewing.',
            "Kept every piece in the brand's voice, published on a steady schedule, and used what performed to shape the next round of ideas."]),
        ('Feb 2025 – Mar 2025', 'Internship, remote', 'Video Editor (Intern)', 'Sort Marketing', [
            'Short-form edits, animated GIFs and motion graphics for social media.']),
        ('Jan 2025 – Feb 2025', 'Internship, remote', 'Video Editor (Intern)', 'Bloofy', [
            'Short-form edits and motion graphics, with footage selected and cut for pacing and continuity.']),
    ]
    jh = ''.join(f'''<li class="job"><div style="display:flex;gap:14px;align-items:flex-start"><span class="dot" aria-hidden="true"></span><div style="display:flex;flex-direction:column;gap:4px"><span style="font-weight:600">{w}</span><span class="muted" style="font-size:14px">{t}</span></div></div>
<div><h3 class="disp">{e(r)}</h3><p class="org">{e(o)}</p><ul>{"".join(f"<li>{e(p)}</li>" for p in pts)}</ul>{CASES.get(o, "")}</div></li>''' for w, t, r, o, pts in jobs)
    skills = [('Paid ads', ['Meta Ads Manager', 'Google Ads, Search and remarketing', 'Lead generation', 'Campaign optimisation', 'Performance reporting']),
              ('Social media', ['Content strategy and planning', 'Copywriting', 'Short-form video', 'Social media management', 'Digital PR']),
              ('Client servicing', ['Account management', 'Onboarding and briefs', 'Reviews and retention', 'Pitching', 'Stakeholder management']),
              ('Data and tools', ['Excel and SQL', 'HubSpot CRM', 'n8n automation', 'Canva', 'Premiere Pro and DaVinci Resolve'])]
    skh = ''.join(f'<div class="skill" data-reveal><h3 class="disp">{t}</h3><ul>{"".join(f"<li>{e(i)}</li>" for i in items)}</ul></div>' for t, items in skills)
    body = f'''<section class="page-head" style="padding-bottom:96px">
<div class="wrap hero-grid" style="gap:64px;align-items:end">
<h1 class="disp">Engineer by training. <span class="accent">Marketer</span> by trade.</h1>
<div style="display:flex;flex-direction:column;gap:18px" class="soft">
<p>I studied Electrical and Electronics Engineering at MAIT, Delhi, and found my way into marketing with the analytical habits intact.</p>
<p>For nearly two years I've run Meta and Google Ads, managed social channels and been the person clients call, across agency, freelance and in-house roles. I track numbers in Excel and SQL, keep pipelines in HubSpot and automate the repetitive parts with n8n.</p>
<p>Video and design are strengths I bring along, not the whole story.</p>
</div>
</div>
</section>

<section aria-labelledby="exp" style="padding-bottom:112px"><div class="wrap">
<div class="sec-head" style="margin-bottom:32px"><h2 id="exp" class="disp h2">Experience</h2><a class="link-strong" href="https://www.linkedin.com/in/praneel-mohan" target="_blank" rel="noopener">LinkedIn profile {ARROW}</a></div>
<ol style="margin:0;padding:0;list-style:none;border-top:1px solid #23242c">{jh}</ol>
</div></section>

<section aria-labelledby="skills" style="background:var(--ink-2);border-top:1px solid var(--line);border-bottom:1px solid var(--line)"><div class="wrap sec">
<h2 id="skills" class="disp h2" style="margin-bottom:40px">Skills and tools</h2>
<div class="grid-4">{skh}</div>
</div></section>

<section class="sec"><div class="wrap two-col" style="gap:24px">
<div style="padding:40px;border-radius:28px;border:1px solid #23242c;display:flex;flex-direction:column;gap:12px">
<h2 class="muted" style="font-size:15px;font-weight:500;margin:0">Education</h2>
<p class="disp" style="font-size:28px;line-height:1.15">B.Tech, Electrical and Electronics Engineering</p>
<p class="soft">Maharaja Agrasen Institute of Technology, Delhi. 2022 to 2026, completed August 2026.</p>
</div>
<div style="padding:40px;border-radius:28px;background:var(--saffron);color:var(--ink);display:flex;flex-direction:column;justify-content:space-between;gap:24px">
<p class="disp" style="font-size:36px;line-height:1.05">The one-page version.</p>
<div class="cta-row"><a class="btn btn-dark" href="{CV}" download>Download CV (PDF)</a><a class="btn btn-ghost-dark" href="mailto:{EMAIL}">Email me</a></div>
</div>
</div></section>
'''
    return head('About | Praneel Mohan', 'Praneel Mohan: engineer by training, marketer by trade. Experience at ZycomTech, RevCore Autos, U\'th Times and 10+ freelance clients.', 'about.html') + body + foot()


pages = {'index.html': page_index, 'work.html': page_work, 'performance.html': page_perf, 'uth-times.html': page_uth, 'about.html': page_about}
for name, fn in pages.items():
    with open(os.path.join(OUT, name), 'w') as f:
        f.write(fn())
    print('wrote', name)
