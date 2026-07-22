# NourDoc — Marketing Website

A production-ready, static HTML5 marketing site for **NourDoc**, an AI-powered Ambient Clinical Intelligence platform. Built with pure HTML, CSS and vanilla JavaScript — no build step, no framework required.

---

## Project Structure

```
files Nourdoc/
├── index.html                  Home
├── product.html                Product / platform overview
├── why-nourdoc.html            Why NourDoc (comparison table)
├── healthcare-impact.html      Clinical / financial / operational / patient impact
├── security-compliance.html    Security & compliance (HIPAA, GDPR, Zero Trust)
├── pricing.html                Pricing + interactive ROI calculator
├── partners.html               Partner ecosystem
├── about.html                  Mission, team, timeline, roadmap
├── contact.html                Contact form, FAQ, direct contacts
├── css/
│   └── style.css               Full design system (tokens, components, layout)
├── js/
│   └── script.js               Nav, scroll-reveal, counters, accordion, ROI
│                                calculator, and form validation
├── pages_about.py              Python generator for about.html
├── pages_contact.py            Python generator for contact.html
├── pages_partners.py           Python generator for partners.html
├── pages_security.py           Python generator for security-compliance.html
└── README.md
```

---

## How to Run Locally

This is a **fully static site** — no installation, no build step, no framework needed.

### Option 1 — Python HTTP Server (Recommended)

Ensure Python 3 is installed. Open a terminal in the project folder and run:

**Windows PowerShell / Command Prompt:**
```powershell
cd "C:\Users\mnoum\Downloads\files Nourdoc"
python -m http.server 8000
```

Then open your browser and go to:
```
http://localhost:8000
```

**macOS / Linux:**
```bash
cd "/path/to/files Nourdoc"
python3 -m http.server 8000
# visit http://localhost:8000
```

### Option 2 — VS Code Live Server

1. Open the `files Nourdoc` folder in **VS Code**.
2. Install the **Live Server** extension (by Ritwick Dey).
3. Right-click `index.html` → **Open with Live Server**.
4. The site opens automatically at `http://127.0.0.1:5500`.

### Option 3 — Open Directly in Browser

Double-click `index.html` to open it in your browser.

> ⚠️ Note: Opening via `file://` may block Google Fonts (requires internet). Use a local server for the full experience.

---

## Deploy to Production

**Netlify (Drag & Drop)**
1. Go to [netlify.com](https://netlify.com) and log in.
2. Drag-and-drop the entire `files Nourdoc` folder onto the deploy area.
3. No build command needed — publish directory is the project root.

**Vercel**
1. Push the folder to a GitHub repository.
2. Import the repo in [vercel.com](https://vercel.com).
3. Set the **Output Directory** to `./` (project root).

**Apache / Nginx / S3 / CloudFront**
Upload all files to your web root. `index.html` is the entry point; all internal links are relative, so the site works from any subpath.

---

## Design System

| Token | Value |
|-------|-------|
| Ink Navy | `#0A1F33` |
| Clinical Blue | `#1D6FE0` |
| Signal Emerald | `#0EA672` |
| Paper | `#FAFBFC` |
| Mist | `#EEF3FA` |
| Slate | `#5B6B79` |

**Typography:** Fraunces (display/headlines), Inter (body/UI), JetBrains Mono (data labels, eyebrows, stats) — loaded from Google Fonts.

**Signature motif:** an animated waveform-to-transcript visualization in the hero, representing the product's core value: conversation → structured documentation.

All interactivity (scroll reveal, counters, accordion, ROI calculator, form validation, mobile nav) is written in dependency-free vanilla JavaScript in `js/script.js`.

---

## Editing Content

Each page was generated from a small Python script that assembles shared nav/footer markup with page-specific HTML, then writes the final static `.html` file. To make a content change:

1. Edit the relevant `pages_*.py` file (or edit the generated `.html` file directly — both are plain HTML).
2. If you edited a `.py` file, regenerate with:
   ```bash
   python3 pages_about.py
   ```
3. Shared header/footer/nav changes go in `build.py` and require regenerating **all** pages:
   ```bash
   python3 -c "import pages_about, pages_contact, pages_partners, pages_security"
   ```

---

## Pre-Launch Notes

- **Images:** `about.html` and `contact.html` use Unsplash placeholder images. Replace with real photography before publishing.
- **Statistics:** Numeric claims (e.g., documentation time ratios) are illustrative industry figures. Substitute with your own validated data before publishing externally.
- **ROI Calculator:** Uses an illustrative blended per-minute rate. Update the `costPerMinute` constant in `js/script.js` to match actual pricing.
- **Contact Form:** The form is client-side only (validates and shows a success state). Wire the `<form data-validate>` submit handler in `js/script.js` to your backend, CRM, or a service like Formspree/HubSpot to actually receive submissions.

---

## Browser Support

Works in all modern browsers: Chrome, Firefox, Safari, Edge. Scroll-reveal animations degrade gracefully where `IntersectionObserver` is not supported.
