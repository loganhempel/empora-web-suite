# Offsider — Project Handoff

**Last updated:** 2026-06-03
**Owner:** Logan Hempel (Emporom Media / Empora Group) · technical: Liam Pullen
**Repo:** `loganhempel/empora-web-suite` · branch `tradeloop-clean-path` (PR #2) · folder `tradeloop/`
**Live:** https://tradeloop-eight.vercel.app · everything index → **/start**

> Read this top-to-bottom before changing anything. The "Gotchas" section will save you an hour.

---

## 1. What Offsider is

**Offsider** (renamed from "TradeLoop" on 2026-06-03) is the flagship prospect-demo SaaS for **Empora Intelligence**, built by **Emporom Media**. It's an "automated back office" for NZ trades businesses:

> Catches every missed call (texts back in ~47s and books the job), revives dead quotes, sends same-day invoices, syncs Xero, guards margins — you just approve a 2-minute morning digest.

Demo persona throughout: **"Pacific Climate Solutions / Mike Thompson"** (Wellington HVAC). Name = NZ/AU slang for a trusted right-hand. Brand mark: a ring (your business) + a companion dot (the offsider alongside it).

---

## 2. Current state

- **Built and LIVE** (production, via Vercel CLI deploy): full marketing site + dark dashboard demo + launch video + calculator + onboarding wizard + comparison + 5 per-trade pages + brand guide + ad creatives + a working lead-capture API. ~19 HTML pages.
- **Committed** on branch `tradeloop-clean-path` = **PR #2** (open, not merged). The repo's `main` does NOT yet have this work.
- **Production is served by CLI deploys** (`vercel deploy --prod` from `tradeloop/`), not git auto-deploy. The live alias is `tradeloop-eight.vercel.app`.
- All strategy/sales docs exist as PDFs (in-repo at `tradeloop/docs/` and in `~/Downloads/Offsider/`).

---

## 3. Architecture (important)

- **Static single-file-ish site. NOT React/Next/shadcn.** No `package.json`, no build step. Plain HTML/CSS/JS. Fonts: Hanken Grotesk + Space Mono. Charts: Chart.js (CDN).
- `index.html` contains **both** the light marketing site **and** the dark dashboard "app" — toggled by `body[data-view="site|auth|app"]` + hash routing (`#app`, `#login`). One big inline `<script>` runs everything.
- One serverless function: `api/lead.js` (Vercel Node, zero-dep) — forwards form leads to `LEAD_WEBHOOK_URL` env var; logs + succeeds gracefully if unset.
- Brand colours: graphite `#14161b` + electric blue `#5b8cff` (dashboard/app); light `#f6f7f9` (marketing). Accent-on-light text uses `#2f55e0`.

---

## 4. File map (`tradeloop/`)

| File | What |
|---|---|
| `index.html` | Marketing site + dashboard app (one file) |
| `demo.html` | 60-sec auto-playing launch video |
| `onboarding.html` | Interactive "live in a week" setup wizard |
| `calculator.html` | Missed-call lost-revenue lead magnet (posts to /api/lead) |
| `compare.html` | Offsider vs receptionist / job software / nothing |
| `for-{plumbers,electricians,hvac,builders,cleaners}.html` | Per-trade SEO landing pages (generated from a template) |
| `heroes.html` | 5 hero direction concepts |
| `creatives.html` | 4 paid-social ad creatives |
| `brand.html` | Brand guide (mark + 3 alts, palette, type, usage) |
| `hub.html` / `start.html` | Internal indexes (`/start` is the Liam-facing "everything" page) |
| `privacy.html` / `terms.html` / `404.html` | Legal templates + branded 404 |
| `og.html` → `og.png` | Social share card (regenerate og.png from og.html via headless Chrome) |
| `assets/` | Logo SVGs (mark, dark/light lockups), `apple-touch-icon.png`, `icon-512.png` |
| `api/lead.js` | Lead-capture serverless function |
| `vercel.json` `robots.txt` `sitemap.xml` | Deploy + SEO config |
| `docs/` | All PDFs + `Offsider-Financial-Model.csv` + `source-md/` (editable markdown) |

**Dashboard modules** (in `index.html`, reached via the sidebar / ⌘K): Today (digest), Revenue (area chart + donut + range), Activity, Calls & SMS, Leads (kanban), Invoices (table), Xero Sync (flow), Pricing Guard (gauge), **Reviews** (auto review-requests), Settings (toggles). Light/dark toggle in the top bar.

---

## 5. Key decisions (with rationale)

- **Name = Offsider.** Generalist (works beyond trades), NZ/AU vernacular, distinctive. Chosen after a 40-domain availability sweep. Intended domain **offsider.co.nz** (not yet bought).
- **Light marketing → dark app.** Light builds trust for non-techy tradie owners; the dark dashboard feels like a premium "command centre" you step into.
- **Pricing (research-backed):** Solo **$149/mo** · Pro **$249/mo** (+$149 setup) · **Built-for-you $1,200 build + $200/mo**. NZ anchor is $45–65/user (Tradify/Fergus) + AI-voice $59–70; the old $1,497 was off-market. Lead with Built-for-you to bank cash + kill the "no time" objection.
- **Validate thin, then build custom** (see `docs/Offsider-Tech-Architecture.pdf` §1): run the first clients on a concierge stack (Twilio/TNZ + n8n + Xero + Claude) before building the multi-tenant product. Sell first, build second.
- **GitHub repo stays `empora-web-suite`** — it holds all 5 Empora sites, not just Offsider. Do not rename it.
- **Efferd shadcn blocks were NOT installed** — they're React; this is static. Their designs were adapted by hand instead. (See the `efferd-shadcn-blocks` skill.)

---

## 6. Gotchas (read these)

1. **The whole site runs on one inline `<script>`.** A single JS syntax error kills *everything* — the scroll-reveal stops and every section below the hero goes blank, and the dashboard dies. This already happened once (a missing brace in `initChart()`). **After any edit to index.html JS, run:**
   ```bash
   cd tradeloop && python3 -c "import re;s=open('index.html').read();b=re.findall(r'<script(?![^>]*src=)[^>]*>(.*?)</script>',s,re.S);open('/tmp/i.js','w').write(chr(10).join(b))" && node --check /tmp/i.js
   ```
2. **Vercel project Root Directory is pinned to `tradeloop`.** Renaming the folder `tradeloop/` → `offsider/` breaks deploys until that dashboard setting is changed. We tried and reverted. To rename later: update Root Directory in Vercel first, then `git mv`.
3. **Production = CLI deploys, not git.** To push changes live now: `cd tradeloop && npx vercel deploy --prod --yes`. Merging PR #2 only matters once git auto-deploy + Root Directory are sorted.
4. **Deploy URL is still `tradeloop-eight.vercel.app`** (project name unchanged). Rename the Vercel project to `offsider` when ready (cosmetic; will change the URL).
5. **`.vercel/` link lives in `tradeloop/`** (gitignored). If it goes missing: `npx vercel link --yes --project tradeloop`.
6. **Docs are committed as binary PDFs** in `tradeloop/docs/`. Regenerate from `docs/source-md/*.md` with `~/Downloads/Claude Storage Work/tools/md_to_pdf.py` (Chrome-headless, no pip deps).
7. **Logo/favicon** is an inline SVG data-URI in each page's `<head>` (ring + dot). Keep consistent if you change the mark.

---

## 7. How to deploy / regenerate things

```bash
# deploy to production
cd ~/"Agency & Website (V1)/tradeloop" && npx vercel deploy --prod --yes

# regenerate the OG image after editing og.html
"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless --disable-gpu \
  --screenshot="$PWD/og.png" --window-size=1200,630 --virtual-time-budget=2500 "file://$PWD/og.html"

# rebuild a PDF from its markdown source
python3 ~/"Downloads/Claude Storage Work/tools/md_to_pdf.py" \
  docs/source-md/<name>.md "Title" docs/Offsider-<Name>.pdf "Subtitle"

# add another per-trade SEO page: edit the TRADES dict in the generator (see git history) and re-run
```

---

## 8. Immediate next steps (human-only — accounts/decisions)

1. **Buy `offsider.co.nz`** (NZ registrar). Quick IPONZ trademark + Companies Register check on "Offsider" first.
2. **Rename the Vercel project** `tradeloop` → `offsider` (Settings → General); point the domain at it. Then update URL references in the code (canonical/og tags currently use `tradeloop-eight.vercel.app`).
3. **Set `LEAD_WEBHOOK_URL`** env var in Vercel (Slack/Zapier/Sheets) so the forms + calculator actually notify you.
4. **Get `/privacy` + `/terms` reviewed** by an NZ lawyer (they're templates).
5. **Merge PR #2** + sort Root Directory if you want git auto-deploy as the source of truth.
6. **Pick the hero direction** (`/heroes`; rec: #2 "Never miss a job" + #4 pricing reframe) and the logo concept (`/brand`; primary is set).
7. **Start selling:** run the missed-call audit on warm clients (Fantail, Ultra Fast, Singh) — script in `docs/Offsider-Outreach-Pack.pdf`. Land 2–3 Built-for-you clients + one flagship case study.

## 9. Next build steps (when picked back up)

- Phase A **concierge stack** (Twilio/TNZ + n8n + Xero + Claude) to run the first real client — see Tech Architecture PDF.
- Wire the lead form to a real CRM/Calendly; add basic analytics (Plausible).
- Then Phase B multi-tenant product (data model + pipelines in the Tech Architecture doc).
- Feature ideas already specced: after-hours call triage, more per-trade/city SEO pages, MYOB depth.

---

## 10. Resources

- **/start** (live) — clickable index of every page + doc.
- **Docs** (`tradeloop/docs/` and `~/Downloads/Offsider/docs/`): Business Map, Operating & Scaling Plan, Tech Architecture, Action Plan, One-Pager, Outreach Pack, Welcome Emails, Financial Model (CSV).
- **Miro** business map (strategy doc + flow diagram): board `uXjVG_SwN0c=`.
- **Skill** `efferd-shadcn-blocks` (in `~/.claude/skills/`) — for installing/adapting shadcn blocks on real React projects.
- Memory note: `project_tradeloop_demo.md`.

*Offsider — built by Emporom Media, an Empora Intelligence product. Made in Aotearoa.*
