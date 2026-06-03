# Offsider — Business Map

Offsider is the trades vertical of **Empora Intelligence** — a productised "automated back office" for Kiwi trades businesses, built and delivered by **Emporom Media**. This document maps the whole business: product, market, ICP, pricing, messaging, features, go-to-market, and the numbers — plus everything built in this session and the decisions waiting for you.

Prepared autonomously, 2026-06-03. Market figures are from verified NZ research (sources at the end); $ are NZD unless noted.

---

## 1. What I shipped this session

While you were away I treated this like a startup and moved on every front. All committed to the `tradeloop` site (PR #2, branch `tradeloop-clean-path`).

- **Dashboard upgrades live** — area revenue chart + time-range toggle, recovery-source donut, Quick Actions panel, Cash-flow Health widget (adapted from the Efferd dashboard-2/4 blocks; they're React, our app is static, so I rebuilt the designs in our stack rather than breaking the build).
- **Dashboard light/dark toggle** — sun/moon in the top-right.
- **Pricing corrected to market** (see §5) — the old $1,497/mo was 6–10× above what NZ tradies pay.
- **Emporom Media logo + Empora family links** added to the footer (→ Empora Intelligence, Empora Group).
- **5 hero directions** built as a real page: `/heroes.html` — five different angles + brand systems to choose from (§7).
- **4 ad creatives** built: `/creatives.html` — paid-social ready, across the strongest angles.
- **Launch explainer video**: `/demo.html` (from the prior session).
- **Reusable skill saved**: `efferd-shadcn-blocks` for installing/adapting those blocks on future projects.

**Where to look:** open `tradeloop/index.html` (site + dashboard), `tradeloop/heroes.html` (the 5 directions), `tradeloop/creatives.html` (ads), `tradeloop/demo.html` (video).

---

## 2. The product in one line

> **Offsider catches every missed call, chases every invoice, and revives every dead lead — automatically. You just approve the two-minute morning digest.**

It runs one loop for every job: **missed call → instant SMS (47s) → booked → job done → same-day invoice → Xero sync → paid → revive past customers → repeat.** Six modules: Missed-Call Responder, Lead Revival, Same-Day Invoicing, Xero/MYOB Sync, Pricing Guard, Daily Digest.

---

## 3. The market & competitors

NZ has ~605,000 businesses, **97% small**. Trades miss **28–35% of calls**; ~**85%** of people who hit voicemail hang up and ring the next tradie; ~**78%** book with whoever replies first. Late payments cost NZ SMEs **$827m/year** (Xero). HVAC alone is a **$2.3bn** market with no player above 5% share — a long tail of small contractors.

### Who tradies already pay

| Tool | Origin | What it is | Price (NZD/mo unless noted) |
|---|---|---|---|
| **Tradify** | NZ | Field-service mgmt (jobs/quotes/invoicing) | $48–62 /user + GST; SMS $0.20/msg |
| **Fergus** | NZ | Field-service mgmt | $44–49 /user + GST |
| **ServiceM8** | AU | Job mgmt, job-volume pricing | Free ≤30 jobs; ~$65 + tiers |
| **Jobber / Housecall Pro** | US | Home-services SMB | USD $29–249 / $59–169+ |
| **simPRO / AroFlo** | AU | Mid-large multi-crew | Custom, ~$ hundreds–$1,000+ |
| **Rosie / LeadTruffle / NextPhone** | US | AI receptionist / missed-call text-back | USD $49–629 + setup |
| **Talkify / automateai / voice-ai** | NZ | AI voice agents for tradies | $59–70 + GST |
| **GoHighLevel** (agencies resell) | US | Missed-call text-back built-in | $97–497 + SMS. **NZ gotcha:** custom SMS (TNZ) not supported for MCTB |

### The whitespace (why Offsider wins)

- The two NZ incumbents (**Tradify, Fergus**) do jobs + invoicing but treat missed-call text-back as a **bolt-on SMS add-on** — they don't *capture the lead* or run the back office for you.
- The new NZ AI-voice startups (**Talkify, automateai, voice-ai**) are **capture-only and shallow** — no invoicing, no Xero sync, no lead revival, no margin guard.
- **Nobody in NZ bundles capture + revival + same-day invoicing + accounting sync + margin guard as one "back office that runs itself."** That seam is Offsider's position.
- **Lead Revival** (auto re-text cold quotes/past customers) and **Pricing Guard** (flag below-margin quotes) are genuinely unmarketed in this segment. Quoting tradies sit on a graveyard of dead quotes — reviving them is near-pure upside and the killer demo.
- **NZ-native plumbing is a moat**: native NZ SMS sender, Xero-first + GST-correct, NZ number provisioning — sidesteps the GHL/US tooling limitations.

---

## 4. ICP — who to sell the first 10 to

**ICP 1 — "Phone-in-the-toolbelt sole trader" (the beachhead).** Owner-operator HVAC / plumber / sparky / gasfitter, **1–2 vans, ~$150k–400k revenue**, no admin staff. Misses a third of calls up a ladder, invoices at night. Feels the pain hardest — every missed call is *his* money. Found in local trade Facebook groups, supplier counters (Plumbing World, Mico, Corys, Ideal Electrical), word of mouth. **Sell the first 10 here.**

**ICP 2 — "Just hired a second hand" small team (best LTV).** 2–6 staff, **$400k–1.5m**, owner half on-tools/half managing. Already on Tradify/Fergus but drowning in quote follow-up and chasing payment. Wants to grow without hiring a $60k+ office person. Highest willingness to pay; best fit for **Built-for-you**.

**ICP 3 — "After-hours emergency trade."** Plumbers / drainage / HVAC doing urgent call-outs worth **$450–600** each, 8–12 after-hours calls/week. The 24/7 capture story sells itself.

**De-prioritise:** large multi-crew firms (need simPRO, have admin staff) and new-build subbies (low inbound calls).

---

## 5. Pricing — two models, both grounded in research

The willingness-to-pay anchors are a **human receptionist ($1,500–3,000/mo)** and **one lost job ($450–600)**. One recovered job pays for the tool. The defensible software band is **$99–249/mo + GST + a modest setup fee**. I've set the site to:

**A) Productised (MRR engine — ICP 1 & 3)**

| Plan | Price | For |
|---|---|---|
| **Solo** | **$149/mo + GST**, $149 setup | Owner-operators, 1–2 vans |
| **Pro** | **$249/mo + GST**, $149 setup | Small teams 2–6, full back office |

Month-to-month, no lock-in (tradies have been burned). Sits above the $59–70 voice toys (it does the *whole* back office) and far under a receptionist.

**B) Built-for-you (done-with-you — ICP 2, your idea)**

> **$1,200 one-time tailored build + $200/mo** (24/7 support, custom scripts in their voice, multi-van).

This is the right wedge to **lead with for the first clients** — concierge setup removes the tradie's #1 objection ("no time to configure it"), b?lands cash up front (deposit-first, per your hard rule), and is squarely Emporom's wheelhouse. Productise it into self-serve Solo/Pro once you have a repeatable setup.

**Recommendation:** open with **Built-for-you** to land 3–5 flagship clients fast and bank setup fees, then push the **$149/$249 productised** plans for scale once onboarding is templated.

---

## 6. The numbers (targets, not promises)

- **Software gross margin is high** — main variable costs are SMS (~$0.20/msg via TNZ/Twilio), LLM tokens per conversation, NZ number provisioning, Xero API, hosting. Comfortably 80%+ at the $149–249 price.
- **Milestone ladder:** 10 clients @ ~$200 blended = **$2,000 MRR**; 50 clients = **$10k MRR / ~$120k ARR**. Built-for-you adds **$1,200 cash per client** on top.
- **CAC is near-zero early** — concierge onboarding + local outreach + referrals (§8). The constraint is your time per setup; productising onboarding is the unlock.
- **Delivery:** the SA pod can run setup + support so this doesn't eat your week.

---

## 7. Messaging & the 5 hero directions

Tradies don't buy "automation platforms" — they buy **more jobs** and **less paperwork**. Talk in jobs and dollars, NZ vernacular (tradie, ute, on the tools, sparky, chippie). **Never** use SaaS-slop ("streamline", "leverage", "seamless").

The 5 hero directions in `/heroes.html` (each a different angle + brand system):

1. **Operations layer** — graphite + electric blue — *"The back office that runs itself."* (current site brand)
2. **Never miss a job** — light + emerald — *"Never lose another job to voicemail."* (strongest money angle)
3. **Get paid faster** — cream + coral, serif — *"Job done by 3. Invoiced by 3:30."* (cash-flow / $827m late-payment pain)
4. **24/7 office manager** — navy + gold, premium — *"Hire the office manager you can't afford."* (reframes $249 as a bargain vs a receptionist)
5. **Get your evenings back** — bold black + neon — *"You didn't start a business to do paperwork at 9pm."* (lifestyle/founder pain)

**My pick:** lead with **#2 (Never miss a job)** as the primary acquisition angle — it's the sharpest money story and what the research says converts — backed by **#4's pricing reframe**. Keep **#1's** graphite/blue as the product/dashboard brand. The 4 ad creatives in `/creatives.html` already cover angles #2, #3, #4, #5.

**Proof tradies need:** named local testimonials with real numbers; a free *missed-call / lost-revenue calculator* (engineering-as-marketing); Xero/MYOB logos; no lock-in; a number they can ring and hear it work.

---

## 8. Go-to-market — first 10 clients (cheap, concrete)

1. **Lead with service, not software.** Sell **Built-for-you** ($1,200 + $200/mo) to 3–5 warm/local tradies; you set it up in a week. Removes the time objection, banks cash.
2. **Wellington / Porirua trade circles first.** Your existing clients are *exactly* the ICP and warm referral routes — **Fantail HVAC, Ultra Fast Pest, Singh Pest, 2in1/Welly Lawns**. Start there.
3. **The "missed-call audit" cold play.** Ring a tradie's number twice in work hours; if it rings out, *that's* the pitch: "I just rang twice and got voicemail — that's how your customers feel. Want it fixed by Friday?" Costs nothing, brutally effective.
4. **Supplier-counter + trade-group partnerships** — Plumbing World, Mico, Corys, Ideal Electrical counters; regional trade Facebook groups. Lead with the lost-revenue calculator.
5. **Accountant/bookkeeper referrals** — Xero-partner bookkeepers feel the late-invoice pain for their tradie clients; rev-share for warm intros to ICP 2.
6. **Industry bodies** — Master Plumbers, Master Electricians (ECANZ), Master Builders — member-newsletter mention + member discount.
7. **One flagship case study, fast** — get a Porirua plumber live, capture "booked N extra jobs / $X recovered in 30 days," turn it into the single proof asset that unlocks everything else.

**Sequence:** concierge-onboard 2–3 locals → one hard-numbers case study → run the missed-call-audit + supplier partnerships to fill the next 7. Deposit/setup fee up front, always (your no-work-before-deposit rule).

---

## 9. Feature roadmap

**Now (built / in the demo):** missed-call SMS responder, lead pipeline, same-day invoicing, Xero sync flow, pricing guard, daily digest, revenue dashboard.

**Next (build to win deals):**
- **After-hours triage** — AI that tells emergency from routine, quotes a call-out fee, and books it (vs a dumb "sorry we missed you" text). Charges the premium rate automatically.
- **Free lost-revenue calculator** — public lead magnet + the core sales prop.
- **Native NZ SMS sender + number provisioning** (TNZ/Twilio) — the moat vs US tools.
- **Lead Revival sequences** productised with templates per trade.

**Later:** voice (not just SMS) answering; MYOB depth; review-request automation after paid jobs; team/role permissions; multi-location; reporting for ICP 2.

---

## 10. Risks & open decisions

- **Brand direction** — pick the primary hero angle (my pick: #2 + #4). *Your call.*
- **Empora Intelligence naming/domain** still open (emporaintel.ai) and Liam not yet signed — Offsider sits under EI, so this is a dependency.
- **SMS deliverability/compliance in NZ** — must use a compliant NZ sender; confirm before first paid client.
- **"Sounds like a human" claim** — keep an easy human-handoff and be honest in marketing; don't overpromise the AI.
- **Delivery capacity** — productise onboarding early so Built-for-you doesn't cap growth at your personal hours.

---

## 11. Recommended next steps (prioritised)

1. **Set Vercel Root Directory = `tradeloop` and merge PR #2** so all of this goes live at `tradeloop-eight.vercel.app`.
2. **Pick the hero direction** from `/heroes.html` (recommend #2 primary, #4 secondary).
3. **Build the free lost-revenue calculator** as the lead magnet (engineering-as-marketing).
4. **Run the missed-call-audit play on your 4 existing clients** this week → land the first Built-for-you deal.
5. **Stand up one flagship case study** within 30 days.
6. **Confirm NZ SMS provider + number provisioning** before first paid go-live.
7. **Push this map to Miro** (board auto-create failed headlessly — do it together when you're back, or I'll retry).

---

## 12. Assets & links

- **Live site / dashboard:** `tradeloop/index.html` → deploys to https://tradeloop-eight.vercel.app
- **Launch video:** `tradeloop/demo.html` → `/demo`
- **5 hero directions:** `tradeloop/heroes.html` → `/heroes`
- **Ad creatives:** `tradeloop/creatives.html` → `/creatives`
- **Repo:** github.com/loganhempel/empora-web-suite · branch `tradeloop-clean-path` (PR #2)
- **Family:** Emporom Media · Empora Intelligence · Empora Group (linked in footer)

---

### Sources (NZ market research, 2026-06-03)
Tradify NZ pricing · Fergus NZ pricing · ServiceM8 NZ · Jobber/Housecall Pro · Simpro · Rosie · LeadTruffle · GoHighLevel TNZ limitation · Talkify NZ · automateai.co.nz · voice-ai.co.nz · Doris.ai (missed-call cost NZ) · Stats NZ business demography · IBISWorld NZ HVAC ($2.3bn) · NZ Herald/Xero ($827m late-payment crisis) · CallCare NZ. Figures verified where cited; vendor-blog stats (call-miss %, first-responder %) are directionally reliable, treat as indicative.
