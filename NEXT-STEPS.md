# Next steps — the 2 interactive bits I can't do for you

Everything else is done: build pipeline (`build.sh`) wired, deploy artefacts generated and verified standalone, `.gitignore` set, initial commit made, all docs written.

What's left = 2 browser-auth steps. Each takes ~30 seconds.

## Step 1 — Create the empty GitHub repo

1. Go to **https://github.com/new**
2. **Owner:** `loganhempel`
3. **Repository name:** `empora-web-suite`
4. **Visibility:** private recommended (client demos via Vercel preview links — no need to expose source)
5. **Do NOT** check "Add a README", "Add .gitignore", or "Add license" — the local repo already has them
6. Click **Create repository**

Then back here, run:

```bash
cd "/Users/loganhempel/Agency & Website (V1)" && git push -u origin main
```

(remote is already configured)

## Step 2 — Log into Vercel

```bash
cd "/Users/loganhempel/Agency & Website (V1)" && npx -y vercel login
```

This opens a browser tab. Pick whatever account/SSO you use. Confirm. Done.

## Step 3 — Deploy (I run this, just give the OK)

Once Steps 1 & 2 are done, paste in this room:

> deploy ready

…and I'll run the 4 `vercel` commands in sequence to ship each site:

```bash
cd deploy/group         && npx vercel --name empora-group         --yes --prod
cd deploy/h2            && npx vercel --name h2-empora            --yes --prod
cd deploy/intelligence  && npx vercel --name intelligence-empora  --yes --prod
cd deploy/emporom       && npx vercel --name emporom-empora       --yes --prod
```

Each takes ~30 seconds. End state = 4 live demo URLs.

## After the first deploy — connect GitHub for auto-deploys

For each of the 4 Vercel projects:
1. Project dashboard → **Settings → Git → Connect Git Repository** → pick `loganhempel/empora-web-suite`.
2. **Settings → General → Root Directory** → set to `deploy/group`, `deploy/h2`, `deploy/intelligence`, or `deploy/emporom`.
3. After this, every `git push` auto-deploys all 4. No manual `vercel --prod` needed.
