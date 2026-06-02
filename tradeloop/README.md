# TradeLoop

The automated back office for NZ trades businesses — the flagship prospect demo for **Empora Intelligence**, built by **Emporom Media**. Static, self-contained, deployed on Vercel.

> Start here: open **`hub.html`** — it links every page and asset.

## Pages
| File | URL | What it is |
|---|---|---|
| `index.html` | `/` | Marketing site (light) **+** dashboard app (dark, `#app`) in one file. View-switch via `data-view` + hash routing (`#app`, `#login`). |
| `demo.html` | `/demo` | 60-sec auto-playing launch explainer. |
| `calculator.html` | `/calculator` | Missed-call lost-revenue calculator (lead magnet). |
| `heroes.html` | `/heroes` | 5 hero directions (angle + brand each). |
| `creatives.html` | `/creatives` | 4 paid-social ad creatives. |
| `privacy.html` `terms.html` | `/privacy` `/terms` | NZ legal templates — review with a lawyer. |
| `404.html` | — | Branded not-found. |
| `hub.html` | — | Internal index of everything. |

## Assets / config
- `og.png` — 1200×630 social share card (regenerate from `og.html` with headless Chrome).
- `vercel.json` — clean URLs + security headers.
- `robots.txt`, `sitemap.xml` — SEO.
- Favicon is an inline SVG data-URI in each page's `<head>`.

## Stack
Plain HTML/CSS/JS. Fonts: Hanken Grotesk + Space Mono. Charts: Chart.js (CDN). **No build, no React, no shadcn** — do not run `npx shadcn init` here (it would break the static deploy).

## Deploy
Vercel project `tradeloop` (alias `tradeloop-eight.vercel.app`), git-connected to `loganhempel/empora-web-suite` with **Root Directory = `tradeloop`**. Work is on branch `tradeloop-clean-path` (PR #2). Set the Root Directory and merge to ship.

## Brand
Dark graphite `#14161b` + electric-blue `#5b8cff` for the app; light `#f6f7f9` marketing. Pricing: Solo $149/mo · Pro $249/mo · Built-for-you $1,200 + $200/mo (all + GST).

## Off-repo
- Strategy: `~/Downloads/TradeLoop-Business-Map.pdf`
- Sales: `~/Downloads/TradeLoop-One-Pager.pdf`
- GTM: `~/Downloads/TradeLoop-Outreach-Pack.pdf`
- Miro business map: board `uXjVG_SwN0c=`
