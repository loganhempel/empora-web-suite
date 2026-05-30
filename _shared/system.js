/* ============================================================
   EMPORA DESIGN SYSTEM  ·  system.js
   Shared behaviour for every brand page. All handlers guard on
   element existence, so a page only "activates" what it uses.
   ============================================================ */
(function(){
  const rm = window.matchMedia('(prefers-reduced-motion: reduce)').matches;

  /* scroll progress + nav state */
  const nav = document.getElementById('nav'), prog = document.getElementById('progress');
  if (nav || prog) {
    const onScroll = () => {
      if (nav) nav.classList.toggle('scrolled', window.scrollY > 40);
      if (prog) {
        const h = document.documentElement.scrollHeight - window.innerHeight;
        prog.style.width = (h > 0 ? (window.scrollY / h) * 100 : 0) + '%';
      }
    };
    window.addEventListener('scroll', onScroll, { passive: true });
    onScroll();
  }

  /* mobile menu */
  const menuBtn = document.getElementById('menuBtn'), mMenu = document.getElementById('mMenu');
  if (menuBtn && mMenu) {
    const toggleMenu = (open) => {
      document.body.classList.toggle('menu-open', open);
      menuBtn.setAttribute('aria-expanded', open);
      mMenu.setAttribute('aria-hidden', !open);
    };
    menuBtn.addEventListener('click', () => toggleMenu(!document.body.classList.contains('menu-open')));
    mMenu.querySelectorAll('a').forEach(a => a.addEventListener('click', () => toggleMenu(false)));
  }

  /* reveal on scroll */
  const io = new IntersectionObserver((es) => {
    es.forEach(e => { if (e.isIntersecting) { e.target.classList.add('in'); io.unobserve(e.target); } });
  }, { threshold: .14 });
  document.querySelectorAll('.rv').forEach(el => io.observe(el));

  /* count-up (exposed so per-page scripts can reuse it) */
  const fmt = (n, dec) => dec ? n.toFixed(dec) : Math.round(n).toString();
  const runCount = (el, end, dec, pre, suf, dur) => {
    if (rm) { el.textContent = pre + fmt(end, dec) + suf; return; }
    let t0 = null;
    const step = (ts) => {
      if (!t0) t0 = ts;
      const p = Math.min((ts - t0) / dur, 1), eased = 1 - Math.pow(1 - p, 3);
      el.textContent = pre + fmt(end * eased, dec) + suf;
      if (p < 1) requestAnimationFrame(step);
    };
    requestAnimationFrame(step);
  };
  window.EmporaCountUp = runCount;
  const counters = new IntersectionObserver((es) => {
    es.forEach(e => {
      if (!e.isIntersecting) return;
      const el = e.target; counters.unobserve(el);
      runCount(el, parseFloat(el.dataset.count), parseInt(el.dataset.dec || 0), el.dataset.prefix || '', el.dataset.suffix || '', 1400);
    });
  }, { threshold: .5 });
  document.querySelectorAll('[data-count]').forEach(el => counters.observe(el));

  /* FAQ accordion */
  document.querySelectorAll('.q-head').forEach(b => {
    b.addEventListener('click', () => {
      const item = b.parentElement, body = item.querySelector('.q-body'), open = item.classList.contains('open');
      document.querySelectorAll('.q-item.open').forEach(i => {
        i.classList.remove('open'); i.querySelector('.q-body').style.maxHeight = null; i.querySelector('.q-head').setAttribute('aria-expanded', 'false');
      });
      if (!open) { item.classList.add('open'); body.style.maxHeight = body.scrollHeight + 'px'; b.setAttribute('aria-expanded', 'true'); }
    });
  });

  /* interactive before/after toggle (Emporom tracking audit) */
  (function () {
    const card = document.getElementById('auditCard'); if (!card) return;
    const fig = document.getElementById('auditFigure'); if (!fig) return; /* H² uses audit-v2 below */
    const before = card.querySelector('.t-before'), after = card.querySelector('.t-after');
    const lead = document.getElementById('auditLead'),
          sub = document.getElementById('auditSub'), rec = document.getElementById('auditRecovered');
    const vB = +fig.dataset.before, vA = +fig.dataset.after; rec.textContent = vA - vB;
    const setState = (audited) => {
      card.classList.toggle('audited', audited);
      before.classList.toggle('on', !audited); after.classList.toggle('on', audited);
      before.setAttribute('aria-selected', !audited); after.setAttribute('aria-selected', audited);
      lead.textContent = audited
        ? (card.dataset.leadAfter || 'Conversions actually happening')
        : (card.dataset.leadBefore || 'Conversions reported');
      sub.textContent = audited
        ? (card.dataset.subAfter || 'What was really converting once the tracking was fixed.')
        : (card.dataset.subBefore || 'What the platform credited before we touched the tracking.');
      runCount(fig, audited ? vA : vB, 0, '', '', 900);
    };
    before.addEventListener('click', () => setState(false));
    after.addEventListener('click', () => setState(true));
    const aio = new IntersectionObserver((es) => {
      es.forEach(e => { if (e.isIntersecting) { aio.unobserve(e.target); setTimeout(() => setState(true), 650); } });
    }, { threshold: .45 });
    aio.observe(card);
  })();

  /* magnetic CTA (desktop, motion-safe) */
  if (!rm && window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.magnetic').forEach(btn => {
      btn.addEventListener('mousemove', (e) => {
        const r = btn.getBoundingClientRect();
        btn.style.transform = `translate(${(e.clientX - r.left - r.width / 2) * .25}px,${(e.clientY - r.top - r.height / 2) * .35}px)`;
      });
      btn.addEventListener('mouseleave', () => { btn.style.transform = ''; });
    });
  }

  /* year stamp */
  const yr = document.getElementById('yr'); if (yr) yr.textContent = new Date().getFullYear();

  /* lead capture — FormSubmit AJAX (no backend; emails logan@emporom.org) */
  document.querySelectorAll('.lead-form').forEach((form) => {
    form.addEventListener('submit', async (e) => {
      e.preventDefault();
      const status = form.querySelector('.lead-status');
      const btn = form.querySelector('button');
      const payload = Object.fromEntries(new FormData(form));
      payload._subject = 'New enquiry · ' + document.title;
      if (btn) btn.disabled = true;
      if (status) status.textContent = 'Sending…';
      try {
        const res = await fetch('https://formsubmit.co/ajax/logan@emporom.org', {
          method: 'POST',
          headers: { 'Content-Type': 'application/json', Accept: 'application/json' },
          body: JSON.stringify(payload),
        });
        if (!res.ok) throw new Error('bad response');
        form.reset();
        if (status) status.textContent = "Got it. We'll be in touch within a day.";
      } catch (_) {
        if (status) status.textContent = 'Something went wrong. Email logan@emporom.org directly.';
      } finally {
        if (btn) btn.disabled = false;
      }
    });
  });

  /* cursor-follow glow on heroes */
  if (window.matchMedia('(pointer:fine)').matches) {
    document.querySelectorAll('.hero').forEach((hero) => {
      if (getComputedStyle(hero).position === 'static') hero.style.position = 'relative';
      const g = document.createElement('div'); g.className = 'cglow'; hero.prepend(g);
      hero.addEventListener('pointermove', (e) => {
        const r = hero.getBoundingClientRect();
        g.style.setProperty('--mx', (e.clientX - r.left) + 'px');
        g.style.setProperty('--my', (e.clientY - r.top) + 'px');
        g.style.opacity = '1';
      });
      hero.addEventListener('pointerleave', () => { g.style.opacity = '0'; });
    });
  }

  /* kinetic rotating headline words */
  document.querySelectorAll('.kw').forEach((kw) => {
    const words = kw.querySelectorAll('.kw-w'); if (words.length < 2) return;
    let i = 0;
    setInterval(() => { words[i].dataset.active = 'false'; i = (i + 1) % words.length; words[i].dataset.active = 'true'; }, 2600);
  });
})();
