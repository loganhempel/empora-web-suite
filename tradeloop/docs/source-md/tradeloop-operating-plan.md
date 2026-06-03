# TradeLoop — Operating & Scaling Plan

Every function of the business: model, economics, sales, marketing, ops, finance, team, risk, and the metrics that matter. Built on the verified NZ research. This is the plan to make TradeLoop cook — efficiently and at scale.

---

## 1. Business model

- **What:** productised "back office that runs itself" for NZ trades. Software + (early) done-for-you setup.
- **Who:** sole traders (1–2 vans, $150k–400k) → small teams (2–6 staff). HVAC, plumbing, electrical, drainage, gasfitting.
- **How it makes money:** recurring monthly subscription (MRR), plus one-time setup/build fees. Sits inside **Empora Intelligence** (the AI arm), delivered by **Emporom Media** + the SA pod.
- **Why it wins:** nobody in NZ bundles capture + revival + same-day invoicing + Xero + margin-guard. Incumbents (Tradify/Fergus) do jobs; AI-voice startups only answer. TradeLoop runs the whole loop.

## 2. Pricing (set, research-backed)
- **Solo** $149/mo + GST · **Pro** $249/mo + GST (+$149 setup) · **Built-for-you** $1,200 build + $200/mo.
- Anchors: a receptionist is $1,500–3,000/mo; one lost job is $450–600. One recovered job pays for it.
- **Lead with Built-for-you** for the first cohort (cash up front, kills the "no time" objection), then drive the productised plans for scale.

## 3. Unit economics (targets)
- **Cost-to-serve:** ~$20–55/client/mo (SMS + LLM + number + infra) → **~75–85% gross margin.**
- **CAC:** near-zero early (founder-led, local, referral). Assume ~$150–300 blended once paid/partnerships kick in.
- **LTV:** at $200 blended ARPU × ~80% margin × ~24-mo life ≈ **$3,800 gross profit/client.** LTV:CAC comfortably >10:1 early.
- **Payback:** setup fee + first month ≈ immediate. Software-only payback < 2 months.
- **The lever that matters:** churn. Trades stick if the loop visibly books jobs and gets them paid — so onboarding + first-30-day proof is everything.

## 4. Revenue plan (12 months, illustrative)
- **M1–2:** 3–5 Built-for-you clients (warm list). ~$1k MRR + $4–6k setup cash.
- **M3–4:** first case study live; 10 clients total. **~$2k MRR.**
- **M6:** 20–25 clients. **~$5k MRR.**
- **M12:** 50 clients blended ~$200. **~$10k MRR / ~$120k ARR** + ongoing setup fees.
- Detailed model in `TradeLoop-Financial-Model.csv` — change the assumptions and it recalculates.

## 5. Sales (the playbook)
- **Pipeline:** Audit → Demo → Proposal (deposit) → Onboard → Live → Case study/referral.
- **The opener:** the **missed-call audit** — ring their number twice; voicemail = the pitch. (Scripts in the Outreach Pack.)
- **The demo:** show the live dashboard + the calculator on *their* numbers. Make them feel the lost money.
- **The close:** Built-for-you, live in a week, deposit up front (hard rule — no work before deposit).
- **Objections:** "no time" → we set it up for you. "sounds robotic" → read the real threads, you can take over anytime. "already on Tradify" → great, we plug in around it and do the bit it doesn't (capture + revival). "lock-in?" → month-to-month.
- **Targets:** ≥2 audits/day, 1 signed client/week from week 3 (ties to the Emporom sprint cadence).

## 6. Marketing (demand engine)
- **Hero angle:** #2 "Never miss a job" (money) + #4 pricing reframe ("a receptionist costs $52k/yr"). #5 (evenings back) for organic/social.
- **Engineering-as-marketing:** the **missed-call calculator** is the top-of-funnel magnet — gate a "email me my number + demo" (now wired to /api/lead). Put it everywhere.
- **Channels (in priority):** 1) warm/local + referrals, 2) supplier-counter + trade-FB-group partnerships, 3) bookkeeper/Xero-partner referrals, 4) short-form social (the demo video + ad creatives), 5) light paid (Meta/Google) once a case study exists.
- **Content:** the 60-sec demo, the 4 ad creatives, one flagship case study with hard numbers, then a steady drip of "missed-call horror stories / $ recovered" posts. NZ vernacular, jobs-and-dollars, no SaaS-slop.
- **Proof assets to build:** named local testimonial w/ numbers, Xero logo trust, a live "ring this number" demo line.

## 7. Operations & delivery
- **Onboarding SOP (target < 1 week):** connect number + Xero → set tone/margin/terms → load services + pricing bands → test the loop live → go live + 7-day check-in. Templatise into a checklist so it's repeatable and pod-deliverable.
- **Support:** 24/7 promise on Built-for-you → SA pod handles tier-1; escalation path for anything the AI flags. Weekly "what did TradeLoop do for you" value report to reduce churn.
- **Quality:** every AI thread logged + sampled; guardrails + human handoff; monthly tone tune per client.

## 8. Finance
- **Billing:** Stripe (NZD, GST-inclusive display + GST line). Setup fee as deposit invoice; subscription monthly.
- **Watch:** SMS/LLM cost per tenant (the only real variable) — usage caps + an upsell tier for heavy after-hours users.
- **Runway/discipline:** bootstrap; setup fees fund delivery; keep cost-to-serve <30% of ARPU. Deposit-before-work, always.

## 9. Team & roles
- **Logan:** sales, brand, GTM, first-client delivery, founder face.
- **Liam:** technical — owns Phase A concierge then Phase B build.
- **SA pod:** onboarding execution + tier-1 support (the scale engine).
- **First hires (post ~25 clients):** a part-time onboarding/support specialist; later a salesperson once the playbook converts repeatably.

## 10. Risks & mitigations
- **Tech overbuild before proof** → validate with the concierge stack first (architecture §1).
- **Churn from no visible value** → first-30-day proof + weekly value report.
- **SMS deliverability/compliance (NZ)** → NZ-native sender, UEMA opt-out, before first paid client.
- **AI overpromise** → honest "assisted, you're in control" positioning + human handoff.
- **Empora Intelligence naming/domain + Liam sign-off** still open — TradeLoop depends on it; close it.
- **Key-person/time** → productise onboarding so growth isn't capped by Logan's hours.

## 11. KPIs — the dashboard to run the business
- **Acquisition:** audits done/wk, demos/wk, demo→close %, CAC.
- **Revenue:** MRR, new MRR, ARPU, setup cash, ARR.
- **Retention:** logo churn %, net revenue retention, 30-day activation (did the loop book a job?).
- **Product value (per client):** missed calls captured, jobs booked, $ recovered, invoice turnaround, % paid on time.
- **Unit econ:** gross margin, cost-to-serve/client, LTV:CAC, payback.
- **North-star:** **$ recovered for clients per month** — when that's up and to the right, everything else follows.

---

*Companion docs: Technical Architecture & Build Plan, Business Map, One-Pager, Outreach Pack, Financial Model (CSV). All in ~/Downloads. TradeLoop — Emporom Media × Empora Intelligence.*
