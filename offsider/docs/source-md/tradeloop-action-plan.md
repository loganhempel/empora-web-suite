# Offsider — Action Plan

What to do tomorrow morning, then 30/60/90. Ordered so each step unblocks the next. Everything I could build autonomously is done and committed; this is the human-only list.

---

## ☀️ Tomorrow morning (in order, ~90 min total)

1. **[10 min] Ship the site.** In Vercel → project `tradeloop` → Settings → Build & Deployment → set **Root Directory = `tradeloop`** → Save. Then merge **PR #2** on GitHub. The whole thing goes live at `tradeloop-eight.vercel.app` (+ `/demo`, `/calculator`, `/heroes`).
2. **[5 min] Open the hub.** `tradeloop/hub.html` — click through every page once on the live URL; confirm it all renders.
3. **[10 min] Pick the hero direction.** Open `/heroes` — decide primary (rec: #2 "Never miss a job") + secondary (#4 pricing reframe). Tell me and I'll set the live site to it.
4. **[10 min] Turn on lead capture.** Make a Slack incoming webhook (or Zapier/Google-Apps-Script) → in Vercel set env var **`LEAD_WEBHOOK_URL`** to it. Now every form + calculator submission pings you. Test it once.
5. **[15 min] Read the two key docs.** `Offsider-Operating-Plan.pdf` and `Offsider-Tech-Architecture.pdf` (esp. §1 — validate thin before building). Decide with Liam: concierge stack first.
6. **[30 min] Start selling.** Run the **missed-call audit** on your 4 warm clients — Fantail (Chris), Ultra Fast, Singh, 2in1/Welly Lawns. Script in `Offsider-Outreach-Pack.pdf`. Aim: book 2 demos today.
7. **[10 min] Domain.** Check/grab **offsider.co.nz**; point it at the Vercel project.

---

## 30 days — prove the loop
- Close **2–3 Built-for-you clients** (deposit up front). Start with warm list.
- Liam stands up the **Phase A concierge stack** (Twilio/TNZ + n8n + Xero + Claude) and runs the first client live.
- Land one **flagship case study** ("booked N jobs / $X recovered in 30 days").
- Confirm **NZ SMS sender + number provisioning** + UEMA opt-out.
- Get **legal templates reviewed** (privacy/terms) and stand up **Stripe** (NZD) billing.
- Put the **calculator everywhere** — link in your email signature, FB groups, supplier counters.

## 60 days — make it repeatable
- 10 paying clients (~$2k MRR). Templatise the **onboarding SOP** so the SA pod can deliver it.
- Publish the case study; turn it into the **ad creatives** + the demo video for light paid tests.
- Start the **bookkeeper/Xero-partner referral** channel.
- Begin **Phase B MVP** build (multi-tenant missed-call→SMS→book + invoice + digest).
- Stand up the **KPI dashboard** (MRR, activation, $ recovered, churn).

## 90 days — scale the engine
- 20–25 clients (~$5k MRR). Self-serve onboarding wizard live.
- Productised **Solo/Pro** plans selling alongside Built-for-you.
- Supplier-counter + trade-group partnerships running.
- Decide first **part-time onboarding/support hire**.
- Review unit economics; cap heavy-SMS tenants or upsell.

---

## Decisions only you can make
- Primary hero/brand angle.
- Concierge-first vs build-first (rec: concierge — see architecture §1).
- Empora Intelligence name/domain + sign Liam (Offsider sits under EI).
- Final pricing confirm ($149 / $249 / $1,200+$200).
- Which warm client becomes the flagship case study.

## Already done (so you don't redo it)
Live site + dark dashboard, demo video, calculator (with lead capture), 5 hero directions, 4 ad creatives, legal pages, 404, OG/SEO/favicon, vercel.json, **working /api/lead endpoint**, hub, README. Docs: Business Map, Operating Plan, Tech Architecture, One-Pager, Outreach Pack, Financial Model. Miro: strategy doc + flow diagram. All committed on PR #2.
