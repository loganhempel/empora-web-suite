# Empora Group — web suite

Four sites, one repo, four Vercel projects. Edit the source files at the natural paths; `./build.sh` generates self-contained `deploy/{group,h2,intelligence,emporom}/` artefacts that Vercel ships.

## Sites

| Path | What | Aesthetic |
|---|---|---|
| `index.html` | Empora Group hub | Cream / ink / orange · light editorial |
| `h2/index.html` | H² · Hempel & Howell | Cobalt + orange · Framer monumental wordmark |
| `intelligence/index.html` | Empora Intelligence | Lime on near-black · AI Supply atmospheric |
| `emporom/index.html` | Emporom Media (standalone donor) | Cobalt + orange · the real agency site is the React `empwebv2/redesign` |

## Quick start

```bash
# local dev server (live edit feedback)
python3 -m http.server 8090 --directory .

# build deploy artefacts (after editing source)
./build.sh

# preview deploy artefacts (matches what Vercel will ship)
python3 -m http.server 8091 --directory deploy
```

## Deploy

See **DEPLOY.md** for the full GitHub + Vercel setup. Once configured:

```bash
./build.sh
git add -A
git commit -m "deploy: <summary>"
git push
```

Vercel auto-deploys all four projects.

## Source of truth

- **DEPLOY.md** — hosting setup + the 4 demo URLs
- **HANDOFF.md** — per-site current state + Framer DNA tokens
- **build.sh** — inlines `_shared/` into each subsite for standalone deployment
- **`_shared/system.css`** — shared design system (edit once, H² + Emporom update)
- **`_shared/system.js`** — shared behaviour
