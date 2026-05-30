# Empora web suite — DEPLOY

Four sites, one repo, four Vercel projects. Each site is deployed independently from a self-contained subdirectory under `deploy/`.

## The 4 demo URLs

| Site | Source | Vercel project | URL |
|---|---|---|---|
| Empora Group hub | this repo · `deploy/group/` | `empora-group` | https://empora-group.vercel.app |
| H² · Hempel & Howell | this repo · `deploy/h2/` | `h2-empora` | https://h2-empora.vercel.app |
| Empora Intelligence | this repo · `deploy/intelligence/` | `intelligence-empora` | https://intelligence-empora.vercel.app |
| **Emporom Media** | **`Bylo24/empwebv2`** (React app, separate repo) | `emporom-empora` | https://emporom-empora.vercel.app |

> **Heads up:** Emporom Media is the React/Vite app at `~/Documents/GitHub/empwebv2`, branch `main-redesign-sandbox`, GitHub remote `Bylo24/empwebv2`. The `/` route there now renders `IndexRedesign` (originally only at `/redesign`); the old site is preserved at `/old`. Vercel will auto-detect Vite and use the existing `vercel.json`. The standalone `emporom/` folder in *this* repo is kept only as a donor reference (no longer built into `deploy/`).

## How a deploy works

1. **Edit source** files in the repo's natural structure (`index.html`, `h2/index.html`, `intelligence/index.html`, `emporom/index.html`, `_shared/system.css`, `_shared/system.js`, `assets/worlddots.js`).
2. **Run `./build.sh`** to regenerate `deploy/{group,h2,intelligence,emporom}/`. The script:
   - Copies the Group hub + worlddots asset into `deploy/group/`.
   - Copies the Intelligence file as-is (already self-contained).
   - Inlines `_shared/system.css` + `_shared/system.js` into `deploy/h2/index.html` and `deploy/emporom/index.html`.
   - Rewrites the cross-site `../<site>/index.html` switch links to the live Vercel URLs.
   - Writes a per-site `vercel.json` with sane defaults (clean URLs, security headers).
3. **Commit + push**:
   ```bash
   git add -A && git commit -m "deploy: <summary>" && git push
   ```
4. Vercel auto-deploys each project from its configured Root Directory.

## One-time setup

### GitHub
1. Create an empty repo at https://github.com/new — name: `empora-web-suite`, owner: `loganhempel`, public or private.
2. Locally:
   ```bash
   cd "/Users/loganhempel/Agency & Website (V1)"
   git remote add origin https://github.com/loganhempel/empora-web-suite.git
   git branch -M main
   git push -u origin main
   ```

### Vercel (uses `npx vercel`, no global install needed)
1. One-time login:
   ```bash
   npx vercel login
   ```
2. **Three projects from this repo** — create + link each pointing at its `deploy/<site>` directory:
   ```bash
   cd "/Users/loganhempel/Agency & Website (V1)/deploy/group"
   npx vercel --name empora-group --yes
   npx vercel --prod --yes

   cd "/Users/loganhempel/Agency & Website (V1)/deploy/h2"
   npx vercel --name h2-empora --yes
   npx vercel --prod --yes

   cd "/Users/loganhempel/Agency & Website (V1)/deploy/intelligence"
   npx vercel --name intelligence-empora --yes
   npx vercel --prod --yes
   ```
3. **Emporom Media** — separate project from the React repo:
   ```bash
   cd ~/Documents/GitHub/empwebv2
   npx vercel --name emporom-empora --yes
   npx vercel --prod --yes
   ```
   Vercel auto-detects Vite. Uses the existing `vercel.json` with SPA fallback rewrites. The `/` route renders `IndexRedesign` (per the App.tsx change); old site preserved at `/old`.
4. **Connect each Vercel project to its Git repo** so future pushes auto-deploy:
   - `empora-group`, `h2-empora`, `intelligence-empora` → connect to `loganhempel/empora-web-suite`, set Root Directory to the appropriate `deploy/<site>` path.
   - `emporom-empora` → connect to `Bylo24/empwebv2`, branch `main-redesign-sandbox`, leave Root Directory blank (repo root).
   - From this point on, `git push` to either repo auto-deploys the affected projects.

## Verifying changes before push

Run the local deploy server to preview all 4 standalone sites:
```bash
python3 -m http.server 8091 --directory deploy
# → http://127.0.0.1:8091/group/
# → http://127.0.0.1:8091/h2/
# → http://127.0.0.1:8091/intelligence/
# → http://127.0.0.1:8091/emporom/
```

This serves the *built* artefacts exactly as Vercel will. For source-edit feedback, keep using the existing local server:
```bash
python3 -m http.server 8090 --directory .
```

## Custom domains (later)

When ready to move off `*.vercel.app`:

1. Buy domain (e.g. `empora.group`, `hempelhowell.co.nz`, `emporaintel.ai`).
2. In each Vercel project → Settings → Domains → add the custom domain.
3. Update Squarespace/Cloudflare/etc DNS to point to Vercel (instructions shown in-dashboard).
4. Re-run `./build.sh` to rewrite the cross-site switch links if domains change (edit `build.sh`'s `vercel.app` replacements).

## What's *not* in this deploy

- Real testimonials (still placeholders — flagged inline in each site)
- Final logos (Logan to supply marked-up files)
- The Emporom Media React app (separate repo: `empwebv2`)

## Source of truth

- **HANDOFF.md** — per-site current state + Framer DNA tokens
- **README.md** — repo overview
- **DEPLOY.md** — this file
- **`~/.claude/projects/-Users-loganhempel/memory/project_empora_suite.md`** — full project history
