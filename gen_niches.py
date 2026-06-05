#!/usr/bin/env python3
"""
Emporom Media — niche landing-page generator.
One conversion-first page per sprint niche, self-contained (inline CSS),
cobalt + orange suite brand. Output → emporom/niches/<slug>.html + index.html.
Add a niche to NICHES and re-run:  python3 gen_niches.py
"""
import pathlib, html

OUT = pathlib.Path(__file__).parent / "emporom" / "niches"
OUT.mkdir(parents=True, exist_ok=True)
EMAIL = "logan@emporom.org"

# Each niche: slug, label(plural), eyebrow, head, sub, three problems, cta, offer line
NICHES = [
    dict(slug="dentists", label="Private dental practices", eyebrow="For dental practices",
         head="Fill more chairs from the ad spend you already have.",
         sub="Most private practices pay for Google clicks that never get tied back to a booked appointment. We fix the tracking first, then the spend — so you can see what actually fills the diary.",
         problems=[
            ("Phone bookings vanish", "Most patients book by phone, and those calls never get connected to the ad or keyword that earned them."),
            ("Your priciest searches go untracked", "Implants, ortho, Invisalign — the high-value clicks you pay most for are the ones you can measure least."),
            ("“Conversions” that aren’t", "Google reports form-fills as conversions. A form-fill isn’t a booked chair — so the numbers lie."),
         ],
         offer="A free 15-minute read on how your practice’s leads are actually tracked. You keep whatever we find."),
    dict(slug="cosmetic-clinics", label="Skin & appearance clinics", eyebrow="For skin & appearance clinics",
         head="See which ads actually fill your consult diary.",
         sub="Demand isn’t your problem — visibility is. We wire up the consult-to-treatment funnel before touching the budget, so every dollar of spend is legible.",
         problems=[
            ("You can’t tell a $20 lead from a $200 one", "Without tracking, every enquiry looks the same — so you can’t cut the spend that isn’t working."),
            ("The consult-to-treatment funnel leaks", "A consult books, but nothing connects it back to the ad that caused it. The money leaks where you can’t see."),
            ("Spend rises, clarity doesn’t", "More budget, same fog. Usually 20–30% of spend carries the whole result and the rest is noise."),
         ],
         offer="A free 15-minute walkthrough of how your enquiries are tracked today. Honest read, no pitch."),
    dict(slug="law-firms", label="Boutique law firms", eyebrow="For boutique law firms",
         head="Know exactly which marketing brings in new matters.",
         sub="You’re bidding on the same expensive keywords as the national firms, with almost every enquiry coming by phone — and none of it traced. We fix that before scaling a cent.",
         problems=[
            ("Bidding blind against the big firms", "Same costly keywords, no idea which ones produce actual matters — so you’re paying their prices for invisible results."),
            ("Every enquiry is a call you can’t trace", "One matter is worth thousands, which is exactly why not knowing its source is so expensive."),
            ("Budget by guesswork", "Without attribution you’re moving spend on a hunch instead of on what works."),
         ],
         offer="A free 15-minute read on how your firm’s enquiries are tracked. No pitch."),
    dict(slug="accountants", label="Accounting & bookkeeping firms", eyebrow="For accounting & bookkeeping firms",
         head="Turn referrals and traffic into booked discovery calls.",
         sub="Referral-fed is great until you want to grow on purpose. Your site gets traffic but isn’t built to convert it — so warm leads go cold on the page. We fix the path first.",
         problems=[
            ("Referrals look you up — then leave", "They land on the site, find no clear next step, and a warm lead quietly goes cold."),
            ("No predictable lead flow", "Growth depends entirely on who happens to refer you this month."),
            ("Traffic with nowhere to go", "You attract visitors but the site doesn’t turn them into booked calls."),
         ],
         offer="A free 15-minute read on your site and tracking. Honest, no pitch."),
    dict(slug="consultants", label="Independent consultants", eyebrow="For independent consultants",
         head="A 90-day growth plan for the people who build them for everyone else.",
         sub="You’re sharp on your clients’ growth and run your own pipeline on referrals. The Growth Map turns “I should market myself” into a prioritised plan you can actually run — flat fee, no retainer.",
         problems=[
            ("You grow everyone’s business but your own", "Your pipeline runs on referrals and network, with no system underneath it."),
            ("No plan, just hustle", "Marketing happens in spare moments and never compounds into anything."),
            ("Quiet quarters hurt", "When the network goes quiet, there’s nothing to fall back on."),
         ],
         offer="A 15-minute call to see if the Growth Map fits. I’ll tell you straight if it doesn’t.",
         cta="See if the Growth Map fits"),
    dict(slug="electricians", label="Electricians & solar installers", eyebrow="For electricians & solar installers",
         head="Stop judging your Google leads on vibes.",
         sub="You generate real leads off Google — until the site gets touched and the call and form tracking quietly breaks. We check that first, not last.",
         problems=[
            ("Tracking breaks every site change", "A rebuild or tweak silently kills your conversion tracking, and the numbers go to fiction."),
            ("Cost-per-lead is a guess", "One install is worth thousands, so not knowing which ad produced it costs real money."),
            ("You can’t double down", "If you can’t see what works, you can’t put more behind it."),
         ],
         offer="A free 15-minute read on how your leads are tracked. No pitch."),
    dict(slug="vets", label="Independent vet clinics", eyebrow="For independent vet clinics",
         head="Win new-client registrations back from the chains.",
         sub="The corporate groups outspend everyone on ads. We fix your tracking and booking path first, so a local clinic’s smaller budget actually competes instead of disappearing into “boosts”.",
         problems=[
            ("Losing registrations to the chains", "Corporate groups outspend you, and your marketing is mostly boosted posts you can’t measure."),
            ("Boosted posts you can’t track", "No idea which post brought a new pet through the door."),
            ("A new client is years of value", "— and right now you can’t trace where they came from, so you can’t grow it on purpose."),
         ],
         offer="A free 15-minute read on how your new-client enquiries are tracked. Honest, no pitch."),
    dict(slug="renovations", label="Kitchen, bathroom & renovation companies", eyebrow="For renovation companies",
         head="Turn more enquiries into booked quotes.",
         sub="High job value, a long decision, leads trickling in from Houzz, Meta and referrals — with nothing tying it together. We fix the enquiry-to-quote path and the tracking behind it.",
         problems=[
            ("Enquiries go cold mid-decision", "Good leads slip away between “interested” and “booked a quote” with no follow-up."),
            ("No nurture, no system", "A long sales cycle with nothing holding the lead’s hand through it."),
            ("A $30k job slips away", "— and nobody knows why, because none of it is tracked."),
         ],
         offer="A free 15-minute read on how your enquiries are handled today. No pitch."),
]

PAGE = """<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>Emporom Media · {label}</title>
<meta name="description" content="{sub_meta}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;500;600;700;800;900&family=Space+Mono:wght@400;700&display=swap" rel="stylesheet">
<style>
:root{{--brand:#2536E6;--brand-d:#1a27c4;--brand-deep:#0c1487;--brand-rgb:37,54,230;
--accent:#FF6A1F;--accent-d:#F2540A;--ink:#0D0D0F;--bg:#F4F1EA;--surface:#fff;
--muted:#6C6B66;--line:rgba(13,13,15,.10);--on-dark-muted:rgba(255,255,255,.62);--line-lt:rgba(255,255,255,.16);
--display:'Hanken Grotesk',-apple-system,system-ui,sans-serif;--mono:'Space Mono',monospace;--ease:cubic-bezier(.16,1,.3,1)}}
*,*::before,*::after{{box-sizing:border-box;margin:0;padding:0}}
html{{scroll-behavior:smooth;-webkit-font-smoothing:antialiased}}
body{{font-family:var(--display);background:var(--bg);color:var(--ink);line-height:1.6;overflow-x:hidden}}
a{{text-decoration:none;color:inherit}}
.wrap{{max-width:1140px;margin:0 auto;padding:0 28px;position:relative;z-index:2}}
.eyebrow{{font-family:var(--mono);font-size:.72rem;letter-spacing:.2em;text-transform:uppercase;font-weight:700;color:var(--accent)}}
.btn{{display:inline-flex;align-items:center;gap:9px;font-weight:700;font-size:.95rem;padding:15px 28px;border-radius:60px;border:none;cursor:pointer;transition:transform .35s var(--ease),background .3s,box-shadow .3s;white-space:nowrap}}
.btn svg{{width:15px;height:15px;transition:transform .35s var(--ease)}}.btn:hover svg{{transform:translateX(4px)}}
.btn-orange{{background:var(--accent);color:#fff;box-shadow:0 10px 30px rgba(var(--accent-rgb),.4)}}.btn-orange:hover{{background:var(--accent-d);transform:translateY(-2px)}}
.btn-ghost{{background:rgba(255,255,255,.1);color:#fff;border:1px solid var(--line-lt);backdrop-filter:blur(8px)}}.btn-ghost:hover{{background:rgba(255,255,255,.2)}}
nav{{position:fixed;inset:0 0 auto;z-index:1000;padding:18px 0;transition:background .4s,box-shadow .4s,padding .4s}}
nav.s{{background:rgba(244,241,234,.86);backdrop-filter:blur(14px);box-shadow:0 1px 0 var(--line);padding:12px 0}}
.nrow{{display:flex;align-items:center;justify-content:space-between}}
.brand{{display:flex;align-items:center;gap:9px;font-weight:900;letter-spacing:-.02em;font-size:1.05rem}}
.brand .dot{{width:12px;height:12px;border-radius:50%;background:var(--accent)}}
.brand small{{font-weight:600;font-size:.66rem;color:var(--muted);letter-spacing:.04em}}
.ncta{{padding:10px 20px;font-size:.85rem}}
.hero{{position:relative;background:var(--brand);color:#fff;padding:150px 0 96px;overflow:hidden}}
.hero::before{{content:'';position:absolute;inset:0;background:radial-gradient(115% 90% at 88% 8%,rgba(123,131,255,.4),transparent 55%),linear-gradient(160deg,var(--brand),var(--brand-deep));z-index:0}}
.hero .eyebrow{{color:#fff;opacity:.85}}
.hero h1{{font-size:clamp(2.3rem,5.5vw,4rem);font-weight:900;letter-spacing:-.03em;line-height:1.04;margin:18px 0 20px;max-width:18ch}}
.hero p{{font-size:clamp(1.02rem,1.5vw,1.2rem);color:rgba(255,255,255,.86);max-width:54ch;margin-bottom:30px;font-weight:500}}
.hero .trust{{margin-top:22px;font-size:.82rem;color:var(--on-dark-muted)}}.hero .trust b{{color:#fff}}
section{{padding:96px 0}}
.sec-head{{max-width:48ch;margin-bottom:46px}}
.sec-head h2{{font-size:clamp(1.8rem,4vw,2.8rem);font-weight:900;letter-spacing:-.025em;color:var(--brand);line-height:1.06}}
.sec-head h2.lt{{color:#fff}}
.cards{{display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.card{{background:var(--surface);border:1.5px solid var(--line);border-radius:18px;padding:28px 26px}}
.card .k{{font-family:var(--mono);font-weight:700;color:var(--accent);font-size:1.4rem}}
.card h3{{font-size:1.1rem;font-weight:800;margin:12px 0 8px}}
.card p{{color:var(--muted);font-size:.96rem}}
.band{{background:var(--ink);color:#fff}}
.stats{{display:grid;grid-template-columns:repeat(3,1fr);gap:36px;margin-top:10px}}
.stat .n{{font-size:clamp(2.2rem,4.5vw,3.4rem);font-weight:900;letter-spacing:-.03em;line-height:1;background:linear-gradient(120deg,#fff,#9aa3ff);-webkit-background-clip:text;background-clip:text;-webkit-text-fill-color:transparent}}
.stat .l{{color:var(--on-dark-muted);margin-top:10px;font-size:.95rem;max-width:26ch}}
.steps{{counter-reset:s;display:grid;grid-template-columns:repeat(3,1fr);gap:22px}}
.step{{position:relative;padding-top:14px;border-top:3px solid var(--brand)}}
.step::before{{counter-increment:s;content:counter(s);font-family:var(--mono);font-weight:700;color:var(--brand);font-size:.9rem}}
.step h3{{font-size:1.1rem;font-weight:800;margin:8px 0 6px}}.step p{{color:var(--muted);font-size:.96rem}}
.cta{{background:var(--brand);color:#fff;text-align:center;position:relative;overflow:hidden}}
.cta::before{{content:'';position:absolute;inset:0;background:radial-gradient(80% 120% at 50% 0%,rgba(123,131,255,.4),transparent 60%)}}
.cta h2{{font-size:clamp(2rem,5vw,3.2rem);font-weight:900;letter-spacing:-.03em;line-height:1.05;max-width:18ch;margin:0 auto 16px}}
.cta p{{color:rgba(255,255,255,.85);max-width:46ch;margin:0 auto 30px;font-size:1.05rem}}
footer{{background:var(--ink);color:#fff;padding:46px 0;text-align:center}}
footer a{{font-weight:700}}footer a:hover{{color:var(--accent)}}
footer small{{color:var(--on-dark-muted);display:block;margin-top:8px}}
@media(max-width:780px){{.cards,.stats,.steps{{grid-template-columns:1fr;gap:16px}}}}
</style>
</head>
<body>
<nav id="nav"><div class="wrap nrow">
  <a class="brand" href="https://emporom.media/"><span class="dot"></span>Emporom Media <small>&nbsp;· Wellington</small></a>
  <a class="btn btn-orange ncta" href="{mailto}">{cta} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div></nav>

<header class="hero"><div class="wrap">
  <span class="eyebrow">{eyebrow}</span>
  <h1>{head}</h1>
  <p>{sub}</p>
  <a class="btn btn-orange" href="{mailto}">{cta} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
  <div class="trust">We fix the <b>tracking</b> before we touch the budget · the build &amp; ads arm of <b>Empora Group</b></div>
</div></header>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">The problem</span>
  <h2>What’s quietly costing you.</h2></div>
  <div class="cards">{problem_cards}</div>
</div></section>

<section class="band"><div class="wrap">
  <div class="sec-head"><span class="eyebrow">Same spend, more clarity</span>
  <h2 class="lt">We make the marketing you already pay for legible.</h2></div>
  <div class="stats">
    <div class="stat"><div class="n">1st</div><div class="l">thing we audit is your tracking — most agencies check it last, if ever.</div></div>
    <div class="stat"><div class="n">100%</div><div class="l">of leads tracked end-to-end: calls, forms, bookings, pixels.</div></div>
    <div class="stat"><div class="n">20–30%</div><div class="l">of ad spend is usually carrying the whole result — the rest is cuttable noise.</div></div>
  </div>
</div></section>

<section><div class="wrap">
  <div class="sec-head"><span class="eyebrow">How it works</span>
  <h2>Three steps, no jargon.</h2></div>
  <div class="steps">
    <div class="step"><h3>Audit the tracking</h3><p>We map exactly how leads reach you today and where the measurement breaks.</p></div>
    <div class="step"><h3>Fix the leaks</h3><p>Calls, forms and pixels wired up properly — usually a half-day, not a bigger budget.</p></div>
    <div class="step"><h3>Scale what works</h3><p>Now that it’s visible, we put more behind the campaigns that actually pay.</p></div>
  </div>
</div></section>

<section class="cta" id="book"><div class="wrap">
  <span class="eyebrow" style="color:#fff;opacity:.85">No pitch, no obligation</span>
  <h2 style="margin-top:14px">{cta}.</h2>
  <p>{offer}</p>
  <a class="btn btn-orange" href="{mailto}">{cta} <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.4"><path d="M5 12h14M13 6l6 6-6 6"/></svg></a>
</div></section>

<footer><div class="wrap">
  <a href="https://emporom.media/">Emporom Media</a>
  <small><a href="mailto:{email}">{email}</a> · emporom.org · Meta &amp; Google Ads · Tracking · CRO · Web</small>
</div></footer>
<script>addEventListener('scroll',()=>document.getElementById('nav').classList.toggle('s',scrollY>40),{{passive:true}});</script>
</body>
</html>"""

def card(k, h, p):
    return f'<div class="card"><div class="k">0{k}</div><h3>{html.escape(h)}</h3><p>{html.escape(p)}</p></div>'

idx_rows = []
for n in NICHES:
    cta = n.get("cta", "Book my free 15-minute tracking read")
    subj = f"Emporom — {n['label']} ({cta})"
    mailto = f"mailto:{EMAIL}?subject={subj.replace(' ', '%20').replace('—','-')}"
    cards = "".join(card(i+1, h, p) for i, (h, p) in enumerate(n["problems"]))
    pagehtml = PAGE.format(label=html.escape(n["label"]), sub_meta=html.escape(n["sub"][:150]),
        eyebrow=html.escape(n["eyebrow"]), head=html.escape(n["head"]), sub=html.escape(n["sub"]),
        problem_cards=cards, cta=html.escape(cta), offer=html.escape(n["offer"]),
        mailto=mailto, email=EMAIL)
    (OUT / f"{n['slug']}.html").write_text(pagehtml)
    idx_rows.append(f'<a class="nl" href="{n["slug"]}.html"><span>{html.escape(n["label"])}</span><em>{html.escape(n["head"])}</em></a>')
    print("wrote", n["slug"] + ".html")

# simple index of all niche pages
INDEX = """<!doctype html><html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Emporom Media · Who we help</title>
<link href="https://fonts.googleapis.com/css2?family=Hanken+Grotesk:wght@400;600;700;800;900&display=swap" rel="stylesheet">
<style>body{{font-family:'Hanken Grotesk',sans-serif;background:#F4F1EA;color:#0D0D0F;margin:0;line-height:1.5}}
.wrap{{max-width:840px;margin:0 auto;padding:80px 28px}}h1{{font-size:2.4rem;font-weight:900;letter-spacing:-.03em;color:#2536E6}}
p.s{{color:#6C6B66;margin:10px 0 36px}}.nl{{display:block;padding:22px 24px;background:#fff;border:1.5px solid rgba(13,13,15,.1);border-radius:16px;margin-bottom:14px;transition:transform .25s,box-shadow .25s}}
.nl:hover{{transform:translateY(-2px);box-shadow:0 14px 34px rgba(37,54,230,.12)}}.nl span{{font-weight:800;display:block;color:#2536E6}}.nl em{{font-style:normal;color:#0D0D0F}}
a{{text-decoration:none;color:inherit}}</style></head><body><div class="wrap">
<h1>Who we help</h1><p class="s">Same wedge, every time: we fix the tracking before we touch the budget. Pick your world.</p>
{rows}
</div></body></html>""".format(rows="\n".join(idx_rows))
(OUT / "index.html").write_text(INDEX)
print("wrote index.html ·", len(NICHES), "niche pages")
