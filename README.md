# Empora Group — web suite

Four sites on one shared design system. Same fonts, components and motion across all of them; each brand reskins it by flipping a few CSS tokens.

## Structure

```
_shared/system.css      ← the design system (tokens + components). Edit once, all four update.
_shared/system.js       ← shared behaviour (nav, reveal, count-up, FAQ, toggles)

index.html              Empora Group hub     navy + amber · dark
emporom/index.html      Emporom Media        cobalt + orange · light
h2/index.html           H² · Hempel & Howell deep-blue + mint · light
intelligence/index.html Empora Intelligence  indigo + cyan · dark

review/                 ← standalone, self-contained copies for review/sharing
  index.html              (CSS + JS inlined into each file — open any one on its own,
  emporom-media.html       no folder or server needed; cross-links work between them)
  h2.html
  empora-intelligence.html
```

**Two copies, on purpose:** the top-level folders are the *editable source* (DRY — change a token in `_shared/system.css` and every site updates). The `review/` folder holds *built, self-contained* copies you can open, email or upload anywhere with nothing attached. Regenerate them with `python3 /tmp/standalone.py` after editing source (script lives with the project notes).

## Reskinning a brand

Each site sets its colours in a small `:root` block in its own `<style>`:

- `--brand` / `--brand-d` / `--brand-deep` / `--brand-rgb` — the dominant (hero) colour
- `--accent` / `--accent-d` / `--accent-lt` / `--accent-rgb` — the action (CTA / highlight) colour
- `--on-accent` — text colour on a solid accent fill (dark for light accents like mint/cyan)
- `--accent-ink` / `--brand-ink` — accent/brand tuned for text legibility on that skin
- dark-skin sites also override the surface tokens (`--bg`, `--surface`, `--band`, `--text`, …)

## Before launch (needs Logan)

- Real pricing on H² and Empora Intelligence (current numbers are indicative).
- Real testimonials (all four carry `replace with a real quote` placeholders).
- Domains + deploy (static directory — drops straight onto Vercel).

Original `emporom-redesign/` (light + dark) kept as the approved backup. `h2-website/` and `empora-group/` are old off-brand drafts, superseded by this suite.
