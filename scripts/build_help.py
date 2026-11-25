#!/usr/bin/env python3
"""Build the Help center from scripts/help_articles.py.

Writes help/index.html (the hub, with search), help/<slug>.html (one page per
question) and the help entries in sitemap.xml. Run from anywhere:

    python3 scripts/build_help.py

Generated files are committed; Cloudflare Pages serves them as-is.
"""
import html
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PUBLIC = ROOT / "public"   # the published site
sys.path.insert(0, str(Path(__file__).resolve().parent))
from help_articles import ARTICLES, TOPICS, COMMON, ELSEWHERE  # noqa: E402

SITE = "https://trytokenomics.com"
TODAY = date.today().isoformat()
TOPIC = {t["id"]: t for t in TOPICS}
BY_SLUG = {a["slug"]: a for a in ARTICLES}
SEARCH_JS = (ROOT / "scripts" / "help-search.js.html").read_text()

esc = html.escape


def text_of(body_html):
    """Plain text of an answer, for search and structured data."""
    t = re.sub(r"<(?:/p|/li|/h2|br\s*/?|/tr|/td|/th)>", " ", body_html)
    t = re.sub(r"<[^>]+>", "", t)
    return re.sub(r"\s+", " ", html.unescape(t)).strip()


def head(title, description, canonical, og_type="article", extra=""):
    return f"""<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>{esc(title)}</title>
  <meta name="description" content="{esc(description)}" />
  <meta property="og:title" content="{esc(title)}" />
  <meta property="og:description" content="{esc(description)}" />
  <meta property="og:type" content="{og_type}" />
  <meta property="og:url" content="{canonical}" />
  <meta property="og:image" content="{SITE}/assets/sharing/OG-Image.png" />
  <meta name="twitter:card" content="summary_large_image" />
  <meta name="twitter:image" content="{SITE}/assets/sharing/OG-Image.png" />
  <link rel="canonical" href="{canonical}" />
  <meta name="theme-color" content="#F3EFE5" media="(prefers-color-scheme: light)" />
  <meta name="theme-color" content="#0E334D" media="(prefers-color-scheme: dark)" />
  <script>document.documentElement.classList.add('js');</script>

  <link rel="icon" href="/favicon.ico" sizes="any" />
  <link rel="icon" type="image/svg+xml" href="/assets/sharing/Favicon-180x180.svg" />
  <link rel="icon" type="image/png" sizes="180x180" href="/assets/sharing/Favicon-180x180.png" />
  <link rel="apple-touch-icon" sizes="180x180" href="/assets/sharing/Apple-Touch-Icon-180x180.png" />
  <link rel="manifest" href="/site.webmanifest" />

  <link rel="preload" href="/assets/fonts/dm-sans-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="preload" href="/assets/fonts/hedvig-letters-serif-normal-latin.woff2" as="font" type="font/woff2" crossorigin>
  <link rel="stylesheet" href="/assets/fonts/fonts.css">
  <link rel="stylesheet" href="/styles.css" />
  <link rel="stylesheet" href="/help.css" />
{extra}</head>
<body>
"""


NAV = """
<nav class="nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="/" class="brand" aria-label="Tokenomics home">
      <span class="brand-mark">
        <img src="/assets/Tokenomics-logo.svg" alt="" width="24" height="24" />
      </span>
      Tokenomics
    </a>

    <div class="nav-links">
      <a href="/#features">Features</a>
      <a href="/#widgets">Widgets</a>
      <a href="/#install">Download</a>
      <a href="/setup">Setup</a>
      <a href="/help/" aria-current="page">Help</a>
      <a href="https://github.com/rob-stout/Tokenomics" target="_blank" rel="noopener">GitHub</a>
    </div>

    <div style="display:flex; gap: 10px; align-items:center; flex-shrink:0;">
      <button class="theme-toggle" id="themeToggle" aria-label="Toggle theme">Dark</button>
      <a href="/download/dmg/latest" class="btn btn-primary btn-sm" rel="noopener">Download</a>
    </div>
  </div>
</nav>
"""

CONTACT = """
    <div class="faq-contact" id="contact">
      <p>
        Still stuck, or hit something this doesn't cover? Email <a href="mailto:hello@trytokenomics.com">hello@trytokenomics.com</a> or open an issue on <a href="https://github.com/rob-stout/Tokenomics/issues" target="_blank" rel="noopener">GitHub</a>.
      </p>
    </div>
"""

FOOTER = """
<footer class="site-footer" role="contentinfo">
  <div class="footer-inner">
    <p class="footer-tagline">Know where you <em>stand</em>.</p>

    <nav class="footer-links" aria-label="Footer navigation">
      <a href="/">Home</a>
      <a href="/setup">Setup</a>
      <a href="/help/">Help</a>
      <a href="https://github.com/rob-stout/Tokenomics" target="_blank" rel="noopener">GitHub</a>
      <a href="https://github.com/rob-stout/Tokenomics/releases" target="_blank" rel="noopener">Changelog</a>
      <a href="/license">License</a>
      <a href="/privacy">Privacy</a>
      <a href="mailto:hello@trytokenomics.com">hello@trytokenomics.com</a>
    </nav>

    <div class="footer-meta">
      <span class="pill dot js-version" style="font-size: 11px; padding: 2px 8px;">v2.10 · macOS 14+</span>
      <span class="sep">·</span>
      <span>&copy; 2026 Acorn Designs, LLC · Created by Rob Stout</span>
      <span class="sep">·</span>
      <span>Not affiliated with, endorsed by, or sponsored by any AI service Tokenomics works with.</span>
    </div>
  </div>
</footer>

<script src="/app.js"></script>
"""

ARROW = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round"><path d="M3 8h10M9 4l4 4-4 4"/></svg>'
BACK = '<svg viewBox="0 0 16 16" fill="currentColor" aria-hidden="true"><path d="M9.78 4.22a.75.75 0 0 1 0 1.06L7.06 8l2.72 2.72a.75.75 0 1 1-1.06 1.06l-3.25-3.25a.75.75 0 0 1 0-1.06l3.25-3.25a.75.75 0 0 1 1.06 0z"/></svg>'
SEARCH_ICON = '<svg class="faq-search-icon" viewBox="0 0 20 20" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" aria-hidden="true"><circle cx="8.75" cy="8.75" r="5.75"/><path d="M13 13l4.25 4.25"/></svg>'


def ld(obj):
    return '  <script type="application/ld+json">\n' + json.dumps(obj, indent=2, ensure_ascii=False) + "\n  </script>\n"


def topic_short(t):
    return t["title"].replace("&", "and")


# ── Article pages ──────────────────────────────────────────────────────
def build_article(a):
    t = TOPIC[a["topic"]]
    url = f"{SITE}/help/{a['slug']}"
    siblings = [x for x in ARTICLES if x["topic"] == a["topic"] and x["slug"] != a["slug"]]
    # Related: the articles this one links to first, then same-topic neighbours.
    linked = [s for s in re.findall(r'href="/help/([a-z0-9-]+)"', a["body"]) if s in BY_SLUG and s != a["slug"]]
    related, seen = [], set()
    for s in linked + [x["slug"] for x in siblings]:
        if s not in seen:
            seen.add(s)
            related.append(BY_SLUG[s])
    related = related[:4]

    structured = ld({
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "TechArticle",
                "headline": a["title"],
                "description": a["summary"],
                "url": url,
                "dateModified": TODAY,
                "author": {"@type": "Person", "name": "Rob Stout"},
                "publisher": {"@type": "Organization", "name": "Acorn Designs, LLC"},
                "about": {"@type": "SoftwareApplication", "name": "Tokenomics", "operatingSystem": "macOS, Chrome"},
            },
            {
                "@type": "BreadcrumbList",
                "itemListElement": [
                    {"@type": "ListItem", "position": 1, "name": "Help", "item": f"{SITE}/help/"},
                    {"@type": "ListItem", "position": 2, "name": topic_short(t), "item": f"{SITE}/help/#{t['id']}"},
                    {"@type": "ListItem", "position": 3, "name": a["title"], "item": url},
                ],
            },
        ],
    })

    rel_html = "\n".join(
        f'          <li><a href="/help/{r["slug"]}">{esc(r["title"])}</a></li>' for r in related
    )
    page = head(f'{a["title"]} | Tokenomics Help', a["summary"], url, extra=structured)
    page += NAV + f"""

<main id="main-content">
<article class="help-article">
  <div class="section-wrap">
    <div class="help-article-top">
      <nav class="help-crumbs" aria-label="Breadcrumb">
        <a href="/help/">Help</a>
        <span aria-hidden="true">/</span>
        <a href="/help/#{t['id']}">{esc(t['title'])}</a>
      </nav>
      <form class="help-mini-search" role="search" action="/help/" method="get">
        <label for="help-q" class="sr-only">Search help</label>
        {SEARCH_ICON}
        <input id="help-q" class="faq-search-input" type="search" name="q" placeholder="Search help" autocomplete="off" enterkeyhint="search" />
      </form>
    </div>

    <h1 class="help-title">{esc(a['title'])}</h1>
    <p class="help-summary">{esc(a['summary'])}</p>

    <div class="doc-body help-body">
{a['body'].strip()}
    </div>

    <aside class="help-related" aria-labelledby="related-heading">
      <h2 class="faq-label" id="related-heading">Related questions</h2>
      <ul>
{rel_html}
      </ul>
    </aside>
{CONTACT}
  </div>
</article>
</main>
""" + FOOTER + "</body>\n</html>\n"
    return page


# ── Hub ────────────────────────────────────────────────────────────────
def build_hub():
    url = f"{SITE}/help/"
    desc = ("Answers about Tokenomics, the menu bar app and browser extension that track your AI usage: "
            "supported tools, Claude's 5-hour and 7-day limits, setup, troubleshooting and privacy.")
    topics = "\n".join(f"""      <li><a href="#{t['id']}">
        <span class="faq-topic-num" aria-hidden="true">{t['num']}</span>
        <span class="faq-topic-title">{esc(t['title'])}</span>
        <span class="faq-topic-desc">{esc(t['desc'])}</span>
      </a></li>""" for t in TOPICS)

    cards = "\n".join(f"""          <li class="faq-card">
            <h3><a href="/help/{s}">{esc(BY_SLUG[s]['title'])}</a></h3>
            <p>{esc(BY_SLUG[s].get('common', BY_SLUG[s]['summary']))}</p>
            <span class="faq-card-more" aria-hidden="true">Read answer {ARROW}</span>
          </li>""" for s in COMMON)

    groups = []
    for t in TOPICS:
        items = "\n".join(f"""        <li class="help-item">
          <a class="help-item-link" href="/help/{a['slug']}">{esc(a['title'])}</a>
          <p>{esc(a['summary'])}</p>
        </li>""" for a in ARTICLES if a["topic"] == t["id"])
        groups.append(f"""    <h2 class="faq-group" id="{t['id']}">{esc(t['title'])}</h2>
    <ul class="help-list">
{items}
    </ul>""")

    index = {
        "articles": [
            {"title": a["title"], "text": a["summary"] + " " + text_of(a["body"]), "kw": a["keywords"],
             "href": f"/help/{a['slug']}"}
            for a in ARTICLES
        ],
        "elsewhere": ELSEWHERE,
        "legacy": {old: a["slug"] for a in ARTICLES for old in a["legacy"]},
    }
    index_json = json.dumps(index, ensure_ascii=False).replace("</", "<\\/")

    structured = ld({
        "@context": "https://schema.org",
        "@type": "CollectionPage",
        "name": "Tokenomics Help",
        "url": url,
        "description": desc,
        "hasPart": [{"@type": "TechArticle", "headline": a["title"], "url": f"{SITE}/help/{a['slug']}"} for a in ARTICLES],
    })

    page = head("Help — Tokenomics", desc, url, og_type="website", extra=structured)
    page += NAV + f"""

<main id="main-content">

<header class="doc-hero">
  <div class="section-wrap">
    <a href="/" class="doc-backlink">
      {BACK}
      Back to home
    </a>

    <p class="feature-kicker">Help</p>
    <h1>How can we <em>help</em>?</h1>
    <ul class="faq-topics" aria-label="What Help covers">
{topics}
    </ul>

    <div class="faq-find">
      <form class="faq-search" id="faq-search" role="search" action="/help/" method="get" hidden>
        <label for="faq-search-input" class="sr-only">Search help</label>
        {SEARCH_ICON}
        <input class="faq-search-input" id="faq-search-input" type="search" name="q"
               placeholder="Search, like “privacy” or “ElevenLabs key”"
               autocomplete="off" autocapitalize="off" spellcheck="false" enterkeyhint="search"
               aria-describedby="faq-search-hint" aria-controls="faq-result-list" />
        <span id="faq-search-hint" class="sr-only">Results appear below as you type. Press Enter to open the first one, or the down arrow to move through them.</span>
      </form>

      <p class="faq-status" id="faq-status" role="status" aria-live="polite"></p>

      <div class="faq-results" id="faq-results" hidden>
        <ol class="faq-result-list" id="faq-result-list" aria-label="Search results"></ol>
      </div>

      <div class="faq-empty" id="faq-empty" hidden>
        <p>Try fewer words, or the name of a tool like Claude, ChatGPT or ElevenLabs.</p>
        <p>Still stuck? Email <a href="mailto:hello@trytokenomics.com">hello@trytokenomics.com</a> or open an issue on <a href="https://github.com/rob-stout/Tokenomics/issues" target="_blank" rel="noopener">GitHub</a>.</p>
      </div>

      <section class="faq-common" id="faq-common" aria-labelledby="faq-common-heading">
        <h2 class="faq-label" id="faq-common-heading">Common questions</h2>
        <ul class="faq-cards">
{cards}
        </ul>
      </section>
    </div>
  </div>
</header>

<section class="doc-body" aria-labelledby="all-questions">
  <div class="section-wrap">
    <div class="faq-browse-head">
      <p class="faq-label" id="all-questions">All questions</p>
    </div>

{chr(10).join(groups)}
{CONTACT}
  </div>
</section>

</main>
""" + FOOTER + f"""
<script type="application/json" id="help-index">{index_json}</script>
{SEARCH_JS.rstrip()}
</script>
</body>
</html>
"""
    return page


def update_sitemap():
    path = PUBLIC / "sitemap.xml"
    xml = path.read_text()
    # Drop old FAQ/help entries, then add the hub and every article.
    xml = re.sub(r"\s*<url>\s*<loc>https://trytokenomics\.com/(?:faq|help)[^<]*</loc>.*?</url>", "", xml, flags=re.S)
    entries = [f"""  <url>
    <loc>{SITE}/help/</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>0.8</priority>
  </url>"""] + [f"""  <url>
    <loc>{SITE}/help/{a['slug']}</loc>
    <lastmod>{TODAY}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.6</priority>
  </url>""" for a in ARTICLES]
    xml = xml.replace("</urlset>", "\n".join(entries) + "\n</urlset>")
    path.write_text(xml)


def main():
    out = PUBLIC / "help"
    out.mkdir(exist_ok=True)
    slugs = [a["slug"] for a in ARTICLES]
    assert len(slugs) == len(set(slugs)), "duplicate slug"
    legacy = [o for a in ARTICLES for o in a["legacy"]]
    assert len(legacy) == len(set(legacy)), "legacy anchor used twice"
    for a in ARTICLES:
        for s in re.findall(r'href="/help/([a-z0-9-]+)"', a["body"]):
            assert s in BY_SLUG, f"{a['slug']} links to missing article {s}"
    for old in out.glob("*.html"):
        old.unlink()
    (out / "index.html").write_text(build_hub())
    for a in ARTICLES:
        (out / f"{a['slug']}.html").write_text(build_article(a))
    update_sitemap()
    print(f"Built help/index.html + {len(ARTICLES)} articles; sitemap updated.")


if __name__ == "__main__":
    main()
