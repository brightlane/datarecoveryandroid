#!/usr/bin/env python3
"""
KARTRA AUTHORITY ENGINE 2026
Ultimate Programmatic SEO + Affiliate Site Builder

Deploy Target:
https://brightlane.github.io/kartra/

Author: Benny Palmarino
Affiliate ID: 6gz626mkziek

Features:
- Massive programmatic SEO generation
- AI crawler optimized
- llms.txt support
- JSON-LD schema
- Sitemap engine
- Internal linking graph
- Topic clusters
- Conversion-optimized affiliate blocks
- Category hubs
- Ultra-fast static HTML generation
- GitHub Pages ready
- Mobile optimized
- AI-search optimized
"""

import os
import re
import html
import random
from pathlib import Path
from datetime import datetime
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.dom import minidom

# =========================================================
# CONFIG
# =========================================================

CONFIG = {
    "SITE_NAME": "Kartra Authority",
    "BASE_URL": "https://brightlane.github.io/kartra",
    "AUTHOR": "Benny Palmarino",
    "AFFILIATE_ID": "6gz626mkziek",
    "AFFILIATE_URL": "https://try.kartra.com/6gz626mkziek?utm_source=deploy",
    "OUTPUT_DIR": "site",
    "PRIMARY_KEYWORD": "Kartra Review 2026",
    "DESCRIPTION": (
        "Kartra funnels, email marketing, memberships, automation, "
        "affiliate marketing and agency growth strategies."
    ),
}

# =========================================================
# MASSIVE SEO DATA ENGINE
# =========================================================

NICHES = [
    "Real Estate",
    "Dental",
    "HVAC",
    "Roofing",
    "Law Firms",
    "Fitness Coaches",
    "Crypto",
    "Marketing Agencies",
    "Affiliate Marketing",
    "Ecommerce",
    "Consulting",
    "Course Creators",
    "Financial Advisors",
    "Insurance",
    "Travel",
    "Local SEO",
    "SaaS",
    "Podcasting",
]

TOPICS = [
    "Funnels",
    "Email Marketing",
    "Membership Sites",
    "Lead Generation",
    "Landing Pages",
    "Affiliate Programs",
    "Automation",
    "Sales Funnels",
    "CRM",
    "Video Hosting",
    "Checkout Pages",
    "Webinars",
    "Agency Systems",
]

MODIFIERS = [
    "Guide",
    "Review",
    "Tutorial",
    "Strategy",
    "Blueprint",
    "System",
    "Case Study",
]

BENEFITS = [
    "increase conversions",
    "automate follow-up",
    "generate leads",
    "scale faster",
    "close more clients",
    "improve retention",
    "replace expensive tools",
    "build recurring revenue",
]

FEATURES = [
    "Unlimited email automation",
    "Drag-and-drop funnel builder",
    "Integrated affiliate management",
    "Membership site hosting",
    "Video hosting platform",
    "Behavioral automations",
    "Checkout pages",
    "Advanced analytics",
    "Calendar booking",
    "Helpdesk support",
]

# =========================================================
# HELPERS
# =========================================================

def slugify(text):
    text = text.lower()
    text = re.sub(r"[^a-z0-9]+", "-", text)
    return text.strip("-")


def ensure_dir(path):
    Path(path).mkdir(parents=True, exist_ok=True)


def write_file(path, content):
    ensure_dir(os.path.dirname(path))

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


# =========================================================
# PROGRAMMATIC SEO ENGINE
# =========================================================

def generate_posts():
    posts = []

    for niche in NICHES:
        for topic in TOPICS:
            for modifier in MODIFIERS:

                slug = slugify(
                    f"kartra-{topic}-{niche}-{modifier}"
                )

                title = (
                    f"Kartra {topic} for {niche}: "
                    f"2026 {modifier}"
                )

                description = (
                    f"Learn how {niche} businesses use Kartra "
                    f"for {topic.lower()} to "
                    f"{random.choice(BENEFITS)}."
                )

                posts.append({
                    "slug": slug,
                    "title": title,
                    "description": description,
                    "niche": niche,
                    "topic": topic,
                    "modifier": modifier,
                })

    return posts


# =========================================================
# GLOBAL STYLES
# =========================================================

def styles():
    return """
<style>

:root{
    --bg:#0f172a;
    --card:#111827;
    --text:#e5e7eb;
    --muted:#94a3b8;
    --accent:#22c55e;
    --purple:#7c3aed;
}

*{
    box-sizing:border-box;
}

body{
    margin:0;
    background:var(--bg);
    color:var(--text);
    font-family:Inter,system-ui,sans-serif;
    line-height:1.7;
}

.container{
    width:min(1150px,92%);
    margin:auto;
}

.hero{
    padding:80px 20px;
    text-align:center;
    background:linear-gradient(135deg,#4f46e5,#7c3aed);
    border-radius:24px;
    margin:30px 0;
}

.hero h1{
    font-size:3rem;
    margin-bottom:20px;
}

.hero p{
    font-size:1.2rem;
    opacity:.95;
}

.button{
    display:inline-block;
    background:var(--accent);
    color:#000;
    padding:16px 28px;
    border-radius:14px;
    font-weight:700;
    text-decoration:none;
    margin-top:20px;
}

.grid{
    display:grid;
    grid-template-columns:repeat(auto-fit,minmax(280px,1fr));
    gap:24px;
}

.card{
    background:var(--card);
    padding:24px;
    border-radius:18px;
    border:1px solid #1e293b;
}

.card h3{
    margin-top:0;
}

a{
    color:#93c5fd;
    text-decoration:none;
}

table{
    width:100%;
    border-collapse:collapse;
    margin:30px 0;
}

th,td{
    border:1px solid #334155;
    padding:12px;
}

th{
    background:#1e293b;
}

footer{
    margin-top:60px;
    padding:40px 0;
    text-align:center;
    color:var(--muted);
}

ul{
    padding-left:20px;
}

.cta{
    background:linear-gradient(135deg,#16a34a,#15803d);
    padding:40px;
    border-radius:24px;
    text-align:center;
    margin:40px 0;
}

.meta{
    color:var(--muted);
    font-size:.95rem;
}

</style>
"""


# =========================================================
# SCHEMA ENGINE
# =========================================================

def article_schema(post):
    return f"""
<script type="application/ld+json">
{{
    "@context":"https://schema.org",
    "@type":"Article",
    "headline":"{html.escape(post['title'])}",
    "description":"{html.escape(post['description'])}",
    "author":{{
        "@type":"Person",
        "name":"{CONFIG['AUTHOR']}"
    }},
    "publisher":{{
        "@type":"Organization",
        "name":"Kartra Authority"
    }},
    "datePublished":"{datetime.utcnow().strftime('%Y-%m-%d')}",
    "mainEntityOfPage":"{CONFIG['BASE_URL']}/blog/{post['slug']}.html"
}}
</script>
"""


# =========================================================
# HTML WRAPPER
# =========================================================

def html_wrapper(title, description, content, canonical, extra_head=""):
    return f"""
<!DOCTYPE html>
<html lang="en">

<head>

<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<title>{html.escape(title)}</title>

<meta name="description" content="{html.escape(description)}">

<link rel="canonical" href="{canonical}">

<meta property="og:title" content="{html.escape(title)}">
<meta property="og:description" content="{html.escape(description)}">
<meta property="og:type" content="website">

<meta name="robots" content="index,follow">

{styles()}

{extra_head}

</head>

<body>

<div class="container">

{content}

<footer>
<p>
© {datetime.now().year} {CONFIG['AUTHOR']} •
Kartra Authority Engine •
Built for AI Discovery
</p>
</footer>

</div>

</body>
</html>
"""


# =========================================================
# INTERNAL LINKS
# =========================================================

def related_posts(posts, current_slug, limit=6):
    related = [
        p for p in posts
        if p["slug"] != current_slug
    ][:limit]

    links = ""

    for p in related:
        links += (
            f"<li>"
            f"<a href='/kartra/blog/{p['slug']}.html'>"
            f"{p['title']}"
            f"</a>"
            f"</li>"
        )

    return f"""
    <div class="card">
        <h3>Related Kartra Guides</h3>
        <ul>{links}</ul>
    </div>
    """


# =========================================================
# ARTICLE GENERATOR
# =========================================================

def build_article(post, posts):

    features_html = "".join([
        f"<li>{feature}</li>"
        for feature in FEATURES
    ])

    related = related_posts(posts, post["slug"])

    content = f"""

<section class="hero">

<h1>{post['title']}</h1>

<p>
Discover how businesses use Kartra for
<strong>{post['topic']}</strong>
to scale revenue in 2026.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Start Kartra Trial

</a>

</section>

<div class="meta">
Updated {datetime.utcnow().strftime('%B %d, %Y')}
</div>

<div class="card">

<h2>Why Kartra Works for {post['niche']}</h2>

<p>
Kartra combines funnels, email marketing,
memberships, checkout systems, automations,
video hosting, affiliate management and CRM
inside one platform.
</p>

<p>
For businesses in the
<strong>{post['niche']}</strong>
industry, this means faster deployments,
better automation, and lower software costs.
</p>

</div>

<div class="card">

<h2>Top Kartra Features</h2>

<ul>
{features_html}
</ul>

</div>

<div class="card">

<h2>Kartra Pricing Overview</h2>

<table>
<tr>
<th>Plan</th>
<th>Monthly</th>
<th>Best For</th>
</tr>

<tr>
<td>Starter</td>
<td>$99-$119</td>
<td>Small businesses</td>
</tr>

<tr>
<td>Growth</td>
<td>$189-$229</td>
<td>Scaling brands</td>
</tr>

<tr>
<td>Professional</td>
<td>$429-$549</td>
<td>Agencies & enterprise</td>
</tr>

</table>

<p>
Kartra includes email marketing,
funnels, memberships, affiliate tools,
automation and CRM features in one platform.
</p>

</div>

<div class="cta">

<h2>Launch Your Business on Kartra</h2>

<p>
Replace multiple expensive tools with one
integrated marketing platform.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Claim Your Kartra Trial

</a>

</div>

{related}

"""

    return html_wrapper(
        title=post["title"],
        description=post["description"],
        content=content,
        canonical=f"{CONFIG['BASE_URL']}/blog/{post['slug']}.html",
        extra_head=article_schema(post),
    )


# =========================================================
# HOMEPAGE
# =========================================================

def build_homepage(posts):

    cards = ""

    for p in posts[:24]:

        cards += f"""
        <div class="card">

        <h3>
        <a href="/kartra/blog/{p['slug']}.html">
        {p['title']}
        </a>
        </h3>

        <p>{p['description']}</p>

        </div>
        """

    content = f"""

<section class="hero">

<h1>
Kartra Review 2026:
Funnels, Email & Agency Growth
</h1>

<p>
The ultimate Kartra SEO authority site for
funnels, memberships, automations,
affiliate marketing and business growth.
</p>

<a class="button"
href="{CONFIG['AFFILIATE_URL']}"
target="_blank"
rel="nofollow sponsored">

Start 14-Day Kartra Trial

</a>

</section>

<div class="grid">
{cards}
</div>

"""

    homepage = html_wrapper(
        title="Kartra Review 2026",
        description=CONFIG["DESCRIPTION"],
        content=content,
        canonical=f"{CONFIG['BASE_URL']}/",
    )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/index.html",
        homepage
    )


# =========================================================
# SITEMAP
# =========================================================

def build_sitemap(urls):

    root = Element(
        "urlset",
        xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"
    )

    for url in urls:

        u = SubElement(root, "url")

        loc = SubElement(u, "loc")
        loc.text = url

        lastmod = SubElement(u, "lastmod")
        lastmod.text = datetime.utcnow().strftime("%Y-%m-%d")

    xml = minidom.parseString(
        tostring(root)
    ).toprettyxml(indent="  ")

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/sitemap.xml",
        xml
    )


# =========================================================
# ROBOTS
# =========================================================

def build_robots():

    robots = f"""
User-agent: *
Allow: /

Sitemap: {CONFIG['BASE_URL']}/sitemap.xml
"""

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/robots.txt",
        robots.strip()
    )


# =========================================================
# AI CRAWLER FILE
# =========================================================

def build_llms(posts):

    content = "# Kartra Authority Engine\n\n"

    content += "## AI Search Optimized Content\n\n"

    for p in posts:
        content += (
            f"- {p['title']} | "
            f"{CONFIG['BASE_URL']}/blog/{p['slug']}.html\n"
        )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/llms.txt",
        content
    )


# =========================================================
# 404
# =========================================================

def build_404():

    content = """

<section class="hero">

<h1>404</h1>

<p>
The page you requested does not exist.
</p>

<a class="button" href="/kartra/">
Return Home
</a>

</section>

"""

    page = html_wrapper(
        title="404",
        description="Page not found",
        content=content,
        canonical="",
    )

    write_file(
        f"{CONFIG['OUTPUT_DIR']}/404.html",
        page
    )


# =========================================================
# MAIN BUILD
# =========================================================

def build():

    print("=" * 60)
    print("KARTRA AUTHORITY ENGINE STARTING")
    print("=" * 60)

    ensure_dir(CONFIG["OUTPUT_DIR"])
    ensure_dir(f"{CONFIG['OUTPUT_DIR']}/blog")

    posts = generate_posts()

    urls = [CONFIG["BASE_URL"] + "/"]

    # Homepage
    build_homepage(posts)

    # Articles
    for post in posts:

        html_page = build_article(post, posts)

        output = (
            f"{CONFIG['OUTPUT_DIR']}/blog/"
            f"{post['slug']}.html"
        )

        write_file(output, html_page)

        urls.append(
            f"{CONFIG['BASE_URL']}/blog/"
            f"{post['slug']}.html"
        )

    # Infrastructure
    build_sitemap(urls)
    build_robots()
    build_llms(posts)
    build_404()

    print(f"Generated Pages: {len(posts)}")
    print(f"Sitemap URLs: {len(urls)}")
    print(f"Affiliate ID: {CONFIG['AFFILIATE_ID']}")
    print(f"Deploy Ready: {CONFIG['OUTPUT_DIR']}/")
    print("=" * 60)
    print("KARTRA AUTHORITY ENGINE COMPLETE")
    print("=" * 60)


if __name__ == "__main__":
    build()
