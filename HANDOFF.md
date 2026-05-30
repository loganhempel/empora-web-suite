# Empora Group web suite — HANDOFF
_Last updated: 2026-05-30 (round 2). Read this first when resuming._

## What this is
Four marketing sites for **Empora Group** and its three ventures, built as standalone HTML/CSS/JS in `~/Agency & Website (V1)/`. No build step, no framework. The Emporom Media *agency* site is a separate React app (see below).

## Run & view
Start the local server (a real browser is required — opening raw `.html` in chat-preview/Quick Look strips the CSS and looks broken):
```
python3 -m http.server 8090 --directory "/Users/loganhempel/Agency & Website (V1)"
```
- Group hub → http://localhost:8090/
- Emporom (standalone donor) → http://localhost:8090/emporom/
- H² → http://localhost:8090/h2/
- Empora Intelligence → http://localhost:8090/intelligence/
- Demos → /_demos/group-map.html · group-globe.html · group-system.html · intel-lime.html
- **Emporom Media (the REAL agency site, React)** → `cd ~/Documents/GitHub/empwebv2 && npm run dev` then http://localhost:8081/redesign

## Structure
```
Agency & Website (V1)/
  index.html                 Empora Group hub (light cream editorial)
  emporom/index.html         Emporom Media STANDALONE (cobalt+orange) — a DONOR, not the live agency site
  h2/index.html              H² (cobalt/blue + orange, light, shared system)
  intelligence/index.html    Empora Intelligence (lime on near-black, SELF-CONTAINED own CSS/JS)
  _shared/system.css|js      shared design system (used by hub + emporom + h2; NOT intelligence)
  assets/worlddots.js        precomputed land-dot coords for the hub's dotted world map
  review/                    self-contained copies (regenerate via /tmp/standalone.py)
  _demos/                    map/globe/scrollytelling/lime experiments
  _backup-original-2026-05-28/  earlier versions incl index-dark-globe.html
  _archive/                  old off-brand drafts (ignore)
  README.md · MORE-REFERENCES.md
```

## Each site — current state
- **Empora Group** (`index.html`): light editorial — cream `#F4F1EA` / ink `#15140F` / orange `#E8550F`. **ROUND 2 PATTERNS APPLIED 2026-05-30** (in light editorial style, NOT Framer-dark):
  - Hero: flat dotted world map (orange flight-arcs; Wellington + Cape Town primary hubs) — unchanged.
  - **TRUST v2** (NEW): replaced thin client marquee with weighted band — eyebrow + meta on top, marquee with brand-coloured logo squares + name + tag ("FN / Fantail · HVAC marketing + site"), 4-column stat row below ("5 active retainers · 3 ventures · One team · NZ-owned").
  - 3 venture cards — unchanged.
  - "The engines, in depth" 3 deep-dive blocks (H² leads with free-demo $0 hook) — unchanged.
  - "One view across all three" dashboard mock + benefits — unchanged.
  - **EDU v2** (NEW): "Where most growth stacks leak." Split-screen ("Three vendors" muted cream vs "Empora Group" cream + orange-tint), centered ink "vs" badge.
  - **STATS v2** (NEW): "Built in Wellington. Run like it matters." Pain-point led on the dark band — featured "1 team" (bar chart), "100% tracked" (line chart), "1 at a time" (Acquire/Build/Compound pill row), "2024 founded" (timeline). All preceded by "Pain · '...'" eyebrows.
  - CTA + lead form + footer — unchanged.
- **Emporom Media** (`emporom/`): cobalt `#2536E6` + orange, light. Demand-engine animated flow, tracking-audit toggle, cases, pricing, educational, kinetic headline. ⚠️ This standalone is a **donor**; the live agency site is the React `/redesign`.
- **H²** (`h2/`): **FRAMER REBUILD 2026-05-30 → ROUND 2 SAME DAY** — every page section rebuilt per Logan's section-by-section review.
  - **HERO**: monumental wordmark moved UP (H² + Hempel & Howell are now first, eyebrow + headline below for breath), copy tightened ("Your new site, built before you pay a dollar" → 2-line lede, sub cut to one line). Cobalt atmospheric backdrop unchanged.
  - **REEL** (hero right): rebuilt the 6 cards as a mix of REAL product mockups, not lookalike templates: (1) `dash` SaaS analytics dashboard with KPIs + line chart, (2) `shop` e-commerce product page with image+price+rating, (3) `book` booking calendar with slot picker, (4) `estate` real-estate listing with hero photo + 3 mini cards, (5) `cafe` atmospheric café hero, (6) `land` lead-gen landing page with form. Each visually distinct, looks like a real product screenshot, not a wireframe.
  - **TRUST BAND v2** (`.trust2`): replaced thin marquee with a weighted band — eyebrow + meta on top, marquee with brand-coloured logo squares + name + tag ("100 / Lead capture · SPA"), 4-column stat row below ("0 deposits lost / 2 weeks avg / 100% tracked / Same team").
  - **STATS v2** (`.stats-v2`): replaced generic Lighthouse/load-time stats with PAIN-POINT focused: each card prefixed with "Pain · '...'" eyebrow + big outcome number + lead label + supporting context + embedded data-viz (bar chart / line chart / pie group / week timeline). Hero stat = "3.4× more enquiries from the same ad spend".
  - **AUDIT v2** (`.audit-v2`): scrapped the single chart-line toggle. New layout = toggle (Template / Your H² demo) flipping a side-by-side: left = site preview (wireframe vs polished demo browser), right = 4-metric audit list (Monthly enquiries, Mobile speed, Conversion rate, Tracking coverage) each with before/after numbers + animated bar fills. Bottom footer shows "▲ +29 more enquiries / month".
  - **BUILDER v2** (`.bb` phase-driven): rebuilt as a JS-driven state machine instead of a 6.5s CSS loop. Each rail click/auto-step pushes `data-phase` 1→6 on the `.bb` which progressively reveals: scoping (wireframe scaffold) → wireframe (solid dashed) → brand applied (cobalt fill) → real copy in (text appears) → tracking wired (tracking pixel badge) → live link delivered (URL goes green + CTA pulses + "Live" badge). 3s per phase, 4.5s dwell on phase 6. Bottom `bb-body::before` shows the current narration ("Scoping the brief…", "Wireframe drawn · structure locked", etc).
  - **PROCESS v2** (`.proc-v2`): replaced ordered-list + side card with a 4-card horizontal stepper, dashed connecting line, big "00 01 02 03" circle badges (Stage 00 highlighted in orange = featured), each card has Week label + title + body + "You / Us" responsibility split, bottom summary block "Demo to live site in about three weeks" with big number on the right.
  - **EDU v2** (`.edu-v2`): replaced 2-row alternating layout with a split-screen side-by-side ("The template build" left in muted cream vs "The H² build" right in cobalt-tinted), centered "vs" badge between them.
  - Unchanged: How-the-demo-works 3-step, services grid, cases, pricing, FAQ, CTA — all still in place.
  - All CTAs across the page = "Get my free demo".
- **Empora Intelligence** (`intelligence/`): **AI SUPPLY FRAMER REBUILD 2026-05-30 → ROUND 2 SAME DAY** — H² round-2 patterns applied where they fit:
  - **HERO** (unchanged): atmospheric near-black hero (#06070A → #0A0B10 + lime ambient glows + faint vertical column guides + animated lime light-leak), centered massive headline ("Reimagine work with autonomous AI agents" — autonomous in lime), small mono "✦ Introducing Empora Intelligence" eyebrow, two pill CTAs (lime "Book a discovery call" + ghost "Watch an agent work"), use-case tray under hero.
  - **"Watch an agent work" signature** (unchanged): "One enquiry in. One booking out. 21 seconds." A live agent-activity stream (Mia Williams books a naturopath consult after hours). 6-step reveal sync'd to right-column input/output cards. Auto-plays on scroll, Replay button.
  - **STATS v2** (NEW): "Why it matters · Software that works. Work that compounds." Pain-point led cards with embedded data-viz: "we're burnt out → 10+ hrs/week back" (bar chart), "leads slip after hours → 24/7" (filled hour dots), "I want to see it working → 2wks" (timeline), "I don't trust where my data goes → 100%" (line chart).
  - **SHIFT v2** (NEW): replaced single-chart-line toggle with "One business, one week. By hand vs by agents." A toggle (Manual / With agents) flips a side-by-side: left = "Day in the life" of a reception person (5 events shown queued/missed in Manual, handled +Ns in Auto), right = 4-metric audit list (Tasks/week, Response time, Coverage, Hours/person/week) with before/after counts + animated bars.
  - **PROCESS v2** (NEW): "From messy to running · Four stages. No black box." 4-card horizontal stepper with dashed connector, 01–04 badges (01 = Audit, featured in lime), each card has Week + You/Us split. Bottom summary "Most workflows go live within three weeks of the audit."
  - **EDU v2** (NEW): "The problem we keep solving · The repetitive work that quietly never ends." Split-screen: "Without agents" (muted dark) vs "With Empora Intelligence" (lime-tinted), centered lime "vs" badge between them.
  - Unchanged: services grid, integration hub (SVG pulses), cases, pricing, FAQ, CTA. Self-contained file (own CSS/JS).

## Shared system (`_shared/`)
Tokens are `--brand*` / `--accent*` pairs + `--on-accent` (text on accent fills) + `--accent-ink`/`--brand-ink` (accent/brand tuned for text legibility per skin). Components: reveal (`.rv`), count-up, FAQ, magnetic buttons, cursor-glow (`.cglow`), kinetic rotating headline (`.kw`), educational problem/solution (`.edu`), FormSubmit lead form (`.lead-form` → posts to logan@emporom.org). Fonts: Hanken Grotesk + Space Mono.

## Branding (target)
Group cream/ink/orange · Emporom agency = the React white/orange/black redesign · H² blue/orange/white · Intelligence lime on near-black. Logan to supply marked-up logos to drop in.

## Verifying changes — GOTCHAS
- Screenshot headless: `"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome" --headless=new --window-size=1280,H --virtual-time-budget=4000 --screenshot=/tmp/x.png URL`
- **Heroes are `min-height:100vh`** → a full-page static shot only shows the hero. To check below-fold sections, build a tiny isolated test in `_demos/` and screenshot that.
- **Sections use scroll-reveal** (`.rv` starts opacity:0) → blank in static shots; they appear on real scroll.
- **A JS error halts the whole `<script>`** — orphaned code whose markup was removed will throw and break everything after it (this silently killed the hub map once; fixed with a guard). Remove/guard dead scripts.
- Regenerate `review/` copies with `python3 /tmp/standalone.py` (recreate the script if /tmp was cleared — it inlines `_shared` and rewrites links).
- FormSubmit needs a one-time activation: the first real form submission emails logan@emporom.org a confirm link.

## OPEN TODOs (the live brief)
1. ~~**H² ↔ Intelligence split**~~ — DONE 2026-05-30. H² leads with the free-demo hook + auto-scroll demo reel. Intel rebuilt in AI Supply Framer style with "Watch an agent work" signature.
2. ~~**Sophistication pass on H² + Intelligence**~~ — DONE 2026-05-30. Both rebuilt to "Framer feel" — atmospheric backdrops, vertical column guides, monumental type, restrained accents, cinematic interactive moments.
3. **Group bundle/partnership offer** — add a "couple two or more engines → partnership rate + one team" section (Logan to finalise the numbers).
4. **Logos** — Logan sends marked-up logos → place in each site.
5. **Real pricing + testimonials** — placeholders everywhere; Logan to supply.
6. **Apply Framer feel to Group hub** — hub is currently light editorial ecomflow style; consider whether to push it toward the same Framer DNA (atmospheric backdrop, column guides) or keep as-is for differentiation. Logan's call.
7. ~~**Deploy** — Vercel.~~ **PIPELINE BUILT 2026-05-30 (round 3)**. See `DEPLOY.md`. `build.sh` generates `deploy/{group,h2,intelligence,emporom}/` — each self-contained with `_shared/` inlined. Git repo initialised + initial commit made. Remote points at `https://github.com/loganhempel/empora-web-suite.git` (repo needs creation at github.com/new — see `NEXT-STEPS.md`). Vercel CLI uses `npx vercel`, no global install. Target URLs: `empora-group.vercel.app`, `h2-empora.vercel.app`, `intelligence-empora.vercel.app`, `emporom-empora.vercel.app`. Emporom React still deploys separately from empwebv2.
8. Imagery — Unsplash (verified URLs already in the dives); Canva stock isn't directly pullable via the connector, so use Unsplash + Logan's Canva logos.

## Framer DNA (lifted from aisupply.framer.website — apply consistently)
- **Atmospheric backdrop**: radial-gradient orbs in brand colours, near-black or deep-brand-tinted base, soft animated light-leak orb that drifts on 12-22s loop.
- **Vertical column guides**: ultra-faint 1px lines at `background-size:calc(100%/6) 100%`, opacity .18-.45, mask-faded top/bottom.
- **Monumental display type**: clamp() going up to 13-22vw, weight 900, letter-spacing -.05 to -.07em, line-height .82-.98.
- **Eyebrow style**: small mono pill, blink-dot or ✦ glyph, backdrop-blur, restrained.
- **Pill CTAs**: solid brand-accent + ghost outlined, both ~60px border-radius, magnetic on hover.
- **Cinematic interactive moment**: every site has ONE killer interactive element (H² = scroll-reel; Intel = agent-stream).
- **Self-running animation**: prefer always-on subtle motion (drifting glows, infinite scrolls, light shimmers) over hover-triggered.
- **Section padding**: bumped to 140px for breath.
- **Restrained accent use**: lime/orange/etc only on key moments (CTAs, key words, active states), not everywhere.

## Writing rules (Logan's)
No em-dashes in prose. No AI vocab (leverage/synergy/seamless/streamline/etc.). NZ-direct peer tone. Real numbers only (5 active retainers — never inflate).

## Reference
- Inspiration: `~/Downloads/Agency Website Inspiration/` + its `MORE-REFERENCES.md` (Wise/Robinhood lime, Linear/Cursor/Stripe motion, COBE globe).
- Funnel reference: ecomflow.com + /about (hook → problem → solution → process → before/after → proof → FAQ → CTA).
- Skills: `~/.claude/skills/` — used scroll-experience, schematic-animation, 3d-web-experience; also relevant: premium-web-design, ui-ux-pro-max, premium-service-business-marketing-site, design-mirror.
- Persistent memory: `~/.claude/projects/-Users-loganhempel/memory/project_empora_suite.md`.

## Starter prompt for the next chat
> Resume the Empora Group web suite. First read `~/Agency & Website (V1)/HANDOFF.md`, then start the local server (`python3 -m http.server 8090 --directory "~/Agency & Website (V1)"`). H² + Intelligence have just been rebuilt to Framer/AI-Supply feel — DO NOT redo the heroes. Likely next: Group bundle/partnership offer, real pricing & testimonials, OR apply the same Framer DNA to the Group hub. Check the "Framer DNA" section at the bottom of this file for the design tokens lifted from aisupply.framer.website.
