"""
Generate one crawlable, SEO-optimized landing page per tool (+ an all-tools hub),
so search engines and AdSense see 200+ real content pages instead of one SPA.
Run from the mastertools/ folder:  python build_seo_pages.py
"""
import re, html, os
from pathlib import Path

HERE = Path(__file__).parent
DATA = (HERE / "js" / "tools-data.js").read_text(encoding="utf-8")

# ---- change this to your real domain once you have one ----
SITE = "https://jahid124421.github.io/mastertools"

# ---- parse categories + tools out of tools-data.js ----
cat_re = re.compile(
    r'id:\s*"([^"]+)",\s*name:\s*"([^"]+)",\s*icon:\s*"([^"]+)",\s*desc:\s*"([^"]+)",\s*\n\s*tools:\s*\[(.*?)\]\s*\n\s*\}',
    re.S)
tool_re = re.compile(r'\{\s*id:\s*"([^"]+)",\s*name:\s*"([^"]+)",\s*icon:\s*"([^"]+)",\s*desc:\s*"([^"]+)"')

categories = []
for cm in cat_re.finditer(DATA):
    cid, cname, cicon, cdesc, body = cm.groups()
    tools = [{"id": t.group(1), "name": t.group(2), "icon": t.group(3), "desc": t.group(4)} for t in tool_re.finditer(body)]
    categories.append({"id": cid, "name": cname, "icon": cicon, "desc": cdesc, "tools": tools})

ALL = [dict(t, cat=c["name"], catid=c["id"]) for c in categories for t in c["tools"]]
by_id = {t["id"]: t for t in ALL}
print(f"parsed {len(categories)} categories, {len(ALL)} tools")

FONTS = ('<link rel="preconnect" href="https://fonts.googleapis.com"><link href="https://fonts.googleapis.com/'
         'css2?family=Orbitron:wght@500;700;900&family=Rajdhani:wght@400;500;600;700&display=swap" rel="stylesheet">')
ICON = ('<link rel="icon" href="data:image/svg+xml,'
        '<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>🛸</text></svg>">')

def esc(s): return html.escape(s, quote=True)

def page(t, up):
    """up = relative prefix to site root, e.g. '../../'"""
    name, icon, desc, cat, catid, tid = t["name"], t["icon"], t["desc"], t["cat"], t["catid"], t["id"]
    related = [x for x in ALL if x["catid"] == catid and x["id"] != tid][:8]
    intro = desc.rstrip(".")
    rel_html = "".join(
        f'<a class="chip" href="{up}tools/{r["id"]}/">{r["icon"]} {esc(r["name"])}</a>' for r in related)
    return f"""<!DOCTYPE html>
<html lang="en" data-theme="dark">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{esc(name)} — Free Online Tool | MasterTools</title>
<meta name="description" content="{esc(intro)}. 100% free, fast and private — runs in your browser with no signup, no uploads and no limits.">
<meta name="keywords" content="{esc(name.lower())}, free {esc(name.lower())}, online {esc(name.lower())}, {esc(cat.lower())}">
<link rel="canonical" href="{SITE}/tools/{tid}/">
<meta property="og:title" content="{esc(name)} — MasterTools">
<meta property="og:description" content="{esc(intro)}. Free, private, in your browser.">
<meta property="og:type" content="website">
<meta property="og:url" content="{SITE}/tools/{tid}/">
{ICON}
{FONTS}
<link rel="stylesheet" href="{up}css/styles.css">
</head>
<body>
<header class="topbar"><div class="topbar-inner">
  <a href="{up}" class="brand"><span class="brand-icon">🛸</span><span class="brand-name">Master<span class="brand-accent">Tools</span></span></a>
  <div style="flex:1"></div>
  <a class="btn small" href="{up}">All tools</a>
</div></header>

<div class="ad-slot ad-leaderboard" data-ad="top"><span>Ad space — 728×90 leaderboard</span></div>

<main class="app">
  <div class="breadcrumb"><a href="{up}">Home</a> / <a href="{up}#/category/{catid}">{esc(cat)}</a> / {esc(name)}</div>
  <div class="tool-header"><span class="th-icon">{icon}</span><h1>{esc(name)}</h1></div>
  <p class="tool-sub">{esc(desc)}</p>

  <a class="btn" style="font-size:18px;padding:14px 26px" href="{up}#/tool/{tid}">▶ Open {esc(name)}</a>

  <div class="tool-layout">
    <div class="tool-panel">
      <h2>What is {esc(name)}?</h2>
      <p>{esc(name)} is a free online tool that lets you {esc(intro.lower())}. It runs entirely inside your web browser, which means your files and text never leave your device — there are no uploads to a server, no account to create, and no limits on how many times you can use it.</p>

      <h2>How to use {esc(name)}</h2>
      <ol>
        <li>Click the <b>“Open {esc(name)}”</b> button above to launch the tool.</li>
        <li>Enter your text or upload your file directly in your browser.</li>
        <li>Get your result instantly, then copy or download it — done in seconds.</li>
      </ol>

      <h2>Why use MasterTools?</h2>
      <ul>
        <li><b>Free forever</b> — every feature, no hidden paywall.</li>
        <li><b>Private</b> — processing happens on your device, not our servers.</li>
        <li><b>Fast</b> — instant results, no waiting in a queue.</li>
        <li><b>Works everywhere</b> — desktop, tablet and mobile, no install.</li>
        <li><b>No signup</b> — just open and use it.</li>
      </ul>

      <h2>Related {esc(cat)} tools</h2>
      <div class="chip-row">{rel_html}</div>
    </div>
    <aside class="ad-rail"><div class="ad-slot" style="min-height:250px;flex-direction:column"><span>Ad space</span><span>300×250</span></div></aside>
  </div>
</main>

<footer class="footer"><div class="footer-inner">
  <div><strong>MasterTools</strong> — 200+ free tools, one place.</div>
  <nav class="footer-links">
    <a href="{up}">Home</a><a href="{up}#/page/about">About</a><a href="{up}#/page/contact">Contact</a>
    <a href="{up}#/page/privacy">Privacy</a><a href="{up}#/page/terms">Terms</a><a href="{up}#/page/disclaimer">Disclaimer</a>
  </nav>
  <div class="footer-copy">© <span>2026</span> MASTERTOOLS</div>
</div></footer>
</body>
</html>"""

# ---- write per-tool pages ----
tools_dir = HERE / "tools"
count = 0
for t in ALL:
    d = tools_dir / t["id"]
    d.mkdir(parents=True, exist_ok=True)
    (d / "index.html").write_text(page(t, "../../"), encoding="utf-8")
    count += 1

# ---- all-tools hub page at /tools/ ----
hub_cards = ""
for c in categories:
    hub_cards += f'<div class="section-title">{c["icon"]} {esc(c["name"])}</div><div class="cat-grid">'
    for t in c["tools"]:
        hub_cards += (f'<a class="tool-card" href="{t["id"]}/"><div class="tc-icon">{t["icon"]}</div>'
                      f'<div class="tc-name">{esc(t["name"])}</div><div class="tc-desc">{esc(t["desc"])}</div></a>')
    hub_cards += "</div>"
hub = f"""<!DOCTYPE html><html lang="en" data-theme="dark"><head>
<meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>All Tools — MasterTools (200+ Free Online Tools)</title>
<meta name="description" content="Browse all {len(ALL)}+ free online tools on MasterTools: PDF, image, video, text, converters, calculators, developer, SEO and security tools.">
<link rel="canonical" href="{SITE}/tools/">
{ICON}{FONTS}
<link rel="stylesheet" href="../css/styles.css"></head>
<body>
<header class="topbar"><div class="topbar-inner"><a href="../" class="brand"><span class="brand-icon">🛸</span><span class="brand-name">Master<span class="brand-accent">Tools</span></span></a></div></header>
<main class="app">
  <div class="breadcrumb"><a href="../">Home</a> / All tools</div>
  <section class="hero"><h1>All Tools</h1><p>Every one of our {len(ALL)}+ free, private, in-browser tools — pick one to get started.</p></section>
  {hub_cards}
</main>
<footer class="footer"><div class="footer-inner"><div><strong>MasterTools</strong></div>
<nav class="footer-links"><a href="../">Home</a><a href="../#/page/about">About</a><a href="../#/page/privacy">Privacy</a><a href="../#/page/terms">Terms</a></nav>
<div class="footer-copy">© 2026 MASTERTOOLS</div></div></footer>
</body></html>"""
(tools_dir / "index.html").write_text(hub, encoding="utf-8")

# ---- sitemap.xml with every page ----
urls = [f"{SITE}/", f"{SITE}/tools/"] + [f"{SITE}/tools/{t['id']}/" for t in ALL]
sm = ['<?xml version="1.0" encoding="UTF-8"?>',
      '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">']
for i, u in enumerate(urls):
    pri = "1.0" if i == 0 else "0.8"
    sm.append(f"  <url><loc>{u}</loc><changefreq>weekly</changefreq><priority>{pri}</priority></url>")
sm.append("</urlset>")
(HERE / "sitemap.xml").write_text("\n".join(sm), encoding="utf-8")

print(f"wrote {count} tool pages + hub + sitemap ({len(urls)} urls)")
print("SITE base:", SITE, "(edit build_seo_pages.py to change it, then re-run)")
