# TradeLoop — Technical Architecture & Backend Build Plan

How TradeLoop goes from a static demo to a real, multi-tenant SaaS that's efficient and scalable. Written for Logan + Liam (technical). The headline call is in §1 — **validate with a thin stack before building custom.**

---

## 1. The strategic call: validate thin, then build custom

Don't build the full custom platform first. The loop is unproven with paying clients, and a from-scratch build is 3+ months. Two phases:

- **Phase A — "Concierge stack" (weeks, not months).** Wire the loop together with off-the-shelf parts and deliver it *done-for-you* to the first 3–5 clients (the $1,200 + $200/mo offer). Proves the loop converts, banks cash, and teaches you exactly what to build. Stack: **Twilio (or NZ TNZ/MessageBird) + n8n/Make + Xero API + Claude + a Google Sheet/Airtable**. You operate it; the client just sees results.
- **Phase B — Custom product.** Once the loop is proven and you have ~5 paying clients and real usage data, build the multi-tenant product below for scale and margin.

This sequence is the difference between cooking and stalling. Everything past §3 is Phase B.

---

## 2. Phase A concierge stack (build this week)

| Need | Tool | Why |
|---|---|---|
| Inbound number + missed-call detection + SMS | **Twilio** (global) or **TNZ / MessageBird** (NZ-native, better deliverability) | Forward the tradie's number; fire a webhook on missed call |
| Orchestration | **n8n** (self-host, cheap) or **Make** | Webhook → AI → SMS → log, no code |
| The reply brain | **Claude (Anthropic API)** | Drafts the SMS in the tradie's voice, detects booking intent |
| Invoicing | **Xero API** | Draft + send + reconcile |
| Lead store + digest | **Airtable / Google Sheet** | Pipeline + the morning digest, zero build |
| Notifications | **Slack / email** | Owner approves from their phone |

Cost to run per client ≈ SMS + a few cents of LLM + number rental — comfortably inside $200/mo.

---

## 3. Phase B — recommended production stack

Keep it on the infra you already use (Vercel) and lean serverless — the workload is webhook-driven and bursty, which is exactly what serverless is cheap and scalable for.

- **App + API:** Next.js (App Router) on **Vercel**, TypeScript. API routes / route handlers for webhooks.
- **DB:** Postgres (**Neon** or Vercel Postgres) + **Prisma** ORM. Row-level multi-tenancy.
- **Queue + schedule:** **Upstash QStash** (HTTP queue + cron) for sequences, digest, retries — serverless-friendly, no always-on worker.
- **SMS/voice:** **Twilio** + an NZ sender (**TNZ/MessageBird**) for deliverability.
- **Accounting:** **Xero** OAuth2 (MYOB later).
- **AI:** **Claude** (Anthropic) with tool-use for booking/quote actions.
- **Auth:** Auth.js or Clerk. **Billing:** **Stripe** (NZD, GST).
- **Email:** Resend or Postmark. **Errors:** Sentry. **Analytics:** Plausible (privacy-friendly).

---

## 4. Data model (multi-tenant — every row carries `businessId`)

```
Business      id, name, trade, phone, xeroTokenId, tone, marginTarget, invoiceTerms, plan, status
User          id, businessId, name, email, role
PhoneNumber   id, businessId, e164, provider
Contact       id, businessId, name, phone, email, lastSeenAt
Call          id, businessId, contactId, direction, status(missed/answered), at
Message       id, businessId, contactId, channel(sms), direction, body, at      // the thread
Lead          id, businessId, contactId, stage(hot/warm/reactivation/won), valueEst, source
Job           id, businessId, leadId, status, completedAt
Quote         id, businessId, jobId, quoted, estCost, marginPct, flagged
Invoice       id, businessId, jobId, xeroInvoiceId, amount, status, sentAt, paidAt
Sequence      id, businessId, type(revival/followup), name
SeqStep       id, sequenceId, offsetDays, channel, template
Enrolment     id, businessId, contactId, sequenceId, step, nextRunAt, status
DigestItem    id, businessId, type, payload, status(pending/approved/denied), date
Event         id, businessId, kind, payload, at     // audit log of everything the system did
Setting       id, businessId, key, value
```

---

## 5. Core pipelines (the product)

**A. Missed call → booked job (the magic)**
```
Twilio webhook (missed call)
 → upsert Contact, create Call(status=missed)
 → enqueue respondToMissedCall(businessId, contactId)
      → load Business context (tone, services, pricing bands, booking rules)
      → Claude drafts SMS in the owner's voice  (tools: proposeBooking, quoteRange)
      → send SMS via provider; store Message(out)
 inbound SMS webhook → store Message(in) → Claude continues thread
      → on booking intent: create Lead(stage=hot) + DigestItem(type=booking)
      → optional: write to calendar
```

**B. Job done → paid**
```
Job.completedAt set
 → draft Invoice from parts+labour → Xero draft → DigestItem(type=invoice)
 → owner approves in digest → send via Xero + payment link
 → Xero payment webhook → Invoice.paidAt → reconcile → Event
```

**C. Lead revival** — QStash cron enrols cold quotes / past customers, fires timed SeqSteps (SMS/email), exits on reply.
**D. Pricing guard** — on Quote create, `marginPct = (quoted-estCost)/quoted`; if `< marginTarget` → flag + DigestItem.
**E. Daily digest** — QStash cron 6:00 NZT → assemble pending DigestItems → push to owner (app + SMS/email). Owner taps approve → actions fire.

---

## 6. The AI layer (do this carefully — it's the product)

- **Per-business system prompt:** voice/tone, services, pricing bands, service area, booking rules, what to never promise.
- **Tool-use** for real actions (proposeBooking, createQuote, escalateToHuman) — don't let the model free-text commitments.
- **Guardrails:** confidence threshold → hand to human; always allow the owner to take over a thread; never quote outside configured bands.
- **Log every message** for trust, debugging, and tuning. Honest marketing — easy human handoff, no "fully human" overclaim.

## 7. Security & NZ compliance
- Privacy Act 2020: data minimisation, access/delete, encrypted Xero tokens, secrets in Vercel env (never in repo).
- **UEMA 2007:** honour STOP/opt-out on every outbound message; record consent basis.
- SMS sender compliance + NZ number provisioning. Audit log (Event) of all automated actions.

## 8. Cost-to-serve & margin (per client / month)
- SMS: ~$0.10–0.25/msg × ~80–200 msgs ≈ **$10–40**
- LLM: cents per conversation ≈ **$2–10**
- Number rental + infra share ≈ **$3–8**
- **Total ≈ $20–55/client.** At $149–249/mo that's **~75–85% gross margin.** Scales well; watch SMS volume on heavy after-hours tenants (cap/upsell).

## 9. Scaling — what breaks and the fix
| Clients | What breaks | Fix |
|---|---|---|
| 1–5 | Your time (concierge setup) | Templatise onboarding; checklist + scripts |
| 5–25 | Manual setup, support load | Self-serve onboarding wizard; SA pod runs support |
| 25–100 | SMS/LLM cost variance, Xero rate limits | Queues, batching, per-tenant usage caps, caching |
| 100+ | Multi-region, voice volume, reporting | Dedicated number pools, voice tier, data warehouse |

## 10. Build phases & rough effort
- **Phase A concierge:** ~1 week (Liam) — proves the loop, first revenue.
- **Phase B MVP:** ~4–6 weeks — single→multi-tenant, missed-call→SMS→book, same-day invoice + Xero, digest, basic dashboard.
- **Phase C:** billing + self-serve onboarding + lead revival + pricing guard.
- **Phase D:** voice answering, full dashboard parity with the demo, MYOB, analytics.

*The static demo (this site) is the sales asset that funds Phase A. Sell first, build second.*
