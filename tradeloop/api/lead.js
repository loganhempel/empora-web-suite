// Offsider — lead capture (Vercel serverless, zero dependencies).
// Forwards leads to LEAD_WEBHOOK_URL (Slack / Zapier / Make / Google Apps Script).
// If no webhook is configured it logs the lead and still succeeds, so the form never breaks.
// Set the env var in Vercel: Project → Settings → Environment Variables → LEAD_WEBHOOK_URL

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ ok: false, error: 'Method not allowed' });
    return;
  }

  let body = req.body;
  if (typeof body === 'string') { try { body = JSON.parse(body); } catch { body = {}; } }
  if (!body || typeof body !== 'object') body = {};

  const clean = (v, max = 300) => String(v == null ? '' : v).slice(0, max).trim();
  const lead = {
    name: clean(body.name, 120),
    email: clean(body.email, 200),
    phone: clean(body.phone, 40),
    trade: clean(body.trade, 80),
    source: clean(body.source, 60) || 'site',
    message: clean(body.message, 600),
    ts: new Date().toISOString(),
    ua: clean(req.headers['user-agent'], 300)
  };

  if (!/^[^@\s]+@[^@\s]+\.[^@\s]+$/.test(lead.email)) {
    res.status(400).json({ ok: false, error: 'A valid email is required' });
    return;
  }

  const hook = process.env.LEAD_WEBHOOK_URL;
  try {
    if (hook) {
      await fetch(hook, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({
          text: `🔧 New Offsider lead — ${lead.name || '(no name)'} <${lead.email}> · via ${lead.source}`,
          lead
        })
      });
    } else {
      console.log('[Offsider lead] (set LEAD_WEBHOOK_URL to forward):', JSON.stringify(lead));
    }
    res.status(200).json({ ok: true });
  } catch (err) {
    console.error('[Offsider lead] forward failed:', err);
    res.status(200).json({ ok: true, warning: 'captured' }); // never fail the visitor
  }
};
