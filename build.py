# -*- coding: utf-8 -*-
"""
build.py — NourDoc shared page generator
Provides the shared nav, footer, and page() helper used by all pages_*.py scripts.
"""

NAV_LINKS = [
    ("index.html",               "Home"),
    ("product.html",             "Product"),
    ("why-nourdoc.html",         "Why NourDoc"),
    ("healthcare-impact.html",   "Impact"),
    ("security-compliance.html", "Security"),
    ("pricing.html",             "Pricing"),
    ("partners.html",            "Partners"),
    ("about.html",               "About"),
]

LOGO_IMG = '<img src="assets/images/logo.png" alt="NourDoc" class="mark" width="30" height="30">'

FONTS = '<link href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,560;9..144,620&family=Inter:wght@400;500;600;700&family=JetBrains+Mono:wght@500;600&display=swap" rel="stylesheet">'

SCHEMA = '''{
  "@context": "https://schema.org",
  "@type": "MedicalOrganization",
  "name": "NourDoc",
  "description": "AI-powered Ambient Clinical Intelligence platform that converts doctor-patient conversations into structured clinical documentation.",
  "url": "https://www.nourdoc.ai"
}'''

FOOTER = '''<footer class="site-footer">
  <div class="container">
    <div class="footer-grid">
      <div class="footer-brand">
        <a href="index.html" class="brand">{logo}NourDoc</a>
        <p>Ambient Clinical Intelligence that turns patient conversations into structured, EMR-ready documentation &mdash; so clinicians can return to the exam room, not the keyboard.</p>
      </div>
      <div>
        <h5>Product</h5>
        <ul>
          <li><a href="product.html">Platform Overview</a></li>
          <li><a href="product.html#ambient">Ambient Listening</a></li>
          <li><a href="product.html#emr">EMR Integration</a></li>
          <li><a href="product.html#api">Developer API</a></li>
          <li><a href="pricing.html">Pricing</a></li>
        </ul>
      </div>
      <div>
        <h5>Company</h5>
        <ul>
          <li><a href="about.html">About Us</a></li>
          <li><a href="why-nourdoc.html">Why NourDoc</a></li>
          <li><a href="healthcare-impact.html">Healthcare Impact</a></li>
          <li><a href="partners.html">Partners</a></li>
          <li><a href="contact.html#investors">Investor Relations</a></li>
        </ul>
      </div>
      <div>
        <h5>Trust</h5>
        <ul>
          <li><a href="security-compliance.html">Security &amp; Compliance</a></li>
          <li><a href="security-compliance.html#hipaa">HIPAA</a></li>
          <li><a href="security-compliance.html#gdpr">GDPR</a></li>
          <li><a href="security-compliance.html#architecture">Zero Trust Architecture</a></li>
        </ul>
      </div>
      <div>
        <h5>Get Started</h5>
        <ul>
          <li><a href="contact.html">Book a Demo</a></li>
          <li><a href="contact.html">Request a Trial</a></li>
          <li><a href="contact.html#support">Support</a></li>
          <li><a href="contact.html#partner">Partner With Us</a></li>
        </ul>
      </div>
    </div>
    <div class="footer-bottom">
      <div class="footer-bottom-info">
        <span>&copy; 2026 NourDoc, Inc. All rights reserved. NourDoc is not a substitute for clinical judgment.</span>
        <span class="powered-by">Powered by <a href="https://m3hive.com" target="_blank" rel="noopener noreferrer" class="m3hive-badge">M3hive</a></span>
      </div>
      <div class="footer-social">
        <a href="https://www.linkedin.com/company/m3-hive/?originalSubdomain=ca" target="_blank" rel="noopener noreferrer" aria-label="LinkedIn"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 9h3v11H4zM5.5 4a1.8 1.8 0 110 3.6A1.8 1.8 0 015.5 4zM10.5 9H13.4V10.6C13.9 9.7 15 9 16.6 9C19.7 9 20 11 20 13.3V20H17V13.9C17 12.5 17 10.7 15 10.7C13 10.7 13.5 12.4 13.5 13.9V20H10.5z"/></svg></a>
        <a href="#" aria-label="X"><svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6"><path d="M4 4l16 16M20 4L4 20"/></svg></a>
      </div>
    </div>
  </div>
</footer>'''


def nav(active_href):
    """Build the shared navigation bar. active_href is the filename of the current page."""
    items = ""
    for href, label in NAV_LINKS:
        active = ' class="active" aria-current="page"' if href == active_href else ''
        items += f'<li><a href="{href}"{active}>{label}</a></li>\n'
    return f'''<nav class="nav" role="navigation" aria-label="Main navigation">
  <div class="nav-inner">
    <a href="index.html" class="brand" aria-label="NourDoc Home">{LOGO_IMG}NourDoc</a>
    <ul class="nav-links" id="nav-menu">
      {items}
    </ul>
    <div class="nav-cta">
      <a href="contact.html" class="btn btn-primary btn-sm">Book a Demo</a>
      <a href="pricing.html" class="btn btn-ghost btn-sm">Start Free Trial</a>
    </div>
    <button class="nav-toggle" aria-label="Toggle menu" aria-expanded="false" aria-controls="nav-menu"><span></span><span></span><span></span></button>
  </div>
</nav>'''


def page(filename, title_prefix, description, main_html):
    """Write a complete HTML page to disk."""
    nav_html = nav(filename)
    footer_html = FOOTER.format(logo=LOGO_IMG)

    html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>{title_prefix} | NourDoc &mdash; Ambient Clinical Intelligence</title>
<meta name="description" content="{description}">
<meta property="og:title" content="{title_prefix} | NourDoc">
<meta property="og:description" content="{description}">
<meta property="og:type" content="website">
<meta property="og:site_name" content="NourDoc">
<meta name="theme-color" content="#0A1F33">
<link rel="icon" href="assets/images/favicon.ico" type="image/x-icon">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
{FONTS}
<link rel="stylesheet" href="css/style.css">
<script type="application/ld+json">
{SCHEMA}
</script>
</head>
<body>
{nav_html}
{main_html}
{footer_html}
<script src="js/script.js"></script>
</body>
</html>'''

    with open(filename, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"Written: {filename}")
