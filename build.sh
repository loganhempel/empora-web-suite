#!/usr/bin/env bash
# ============================================================
#  Empora web suite · build.sh
#  Generates `deploy/{group,h2,intelligence,emporom}/` — each a
#  self-contained, deploy-ready site. Run after any source edit:
#
#      ./build.sh
#
#  Then commit + push; Vercel auto-deploys each project from its
#  configured Root Directory (`deploy/<site>`).
# ============================================================

set -euo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
DEPLOY="$ROOT/deploy"
SHARED_CSS="$ROOT/_shared/system.css"
SHARED_JS="$ROOT/_shared/system.js"

[ -f "$SHARED_CSS" ] || { echo "✗ missing $SHARED_CSS"; exit 1; }
[ -f "$SHARED_JS"  ] || { echo "✗ missing $SHARED_JS";  exit 1; }

echo "→ wiping $DEPLOY"
rm -rf "$DEPLOY"
mkdir -p "$DEPLOY/group/assets" "$DEPLOY/h2" "$DEPLOY/intelligence"
# Emporom Media is deployed separately — the React app at
# ~/Documents/GitHub/empwebv2 (the /redesign route). The standalone
# emporom/ in this repo is kept as a donor reference only and is NOT
# built into deploy/. See DEPLOY.md for the empwebv2 Vercel setup.

# ---------- Group hub ------------------------------------------
# Already self-contained inline (no _shared/ refs). Needs only the
# worlddots map data. Copy as-is.
echo "→ group/"
cp "$ROOT/index.html"             "$DEPLOY/group/index.html"
cp "$ROOT/assets/worlddots.js"    "$DEPLOY/group/assets/worlddots.js"

# ---------- Intelligence ---------------------------------------
# Already self-contained (own inline CSS + JS, no _shared/ refs).
echo "→ intelligence/"
cp "$ROOT/intelligence/index.html" "$DEPLOY/intelligence/index.html"

# ---------- H² and Emporom -------------------------------------
# Both reference  <link href="../_shared/system.css">  and
# <script src="../_shared/system.js"></script>. Inline both so the
# subdir is self-contained when deployed at Root Directory = h2/ etc.
inline_shared() {
  local SRC="$1"
  local DST="$2"
  python3 - "$SRC" "$DST" "$SHARED_CSS" "$SHARED_JS" <<'PY'
import sys, re, pathlib
src, dst, css_path, js_path = sys.argv[1:5]
html = pathlib.Path(src).read_text()
css  = pathlib.Path(css_path).read_text()
js   = pathlib.Path(js_path).read_text()
# replace the external <link> with an inline <style>
html = re.sub(
    r'<link[^>]*href="\.\./_shared/system\.css"[^>]*/?>',
    f'<style>\n/* inlined from _shared/system.css */\n{css}\n</style>',
    html, count=1,
)
# replace the external <script src> with an inline <script>
html = re.sub(
    r'<script[^>]*src="\.\./_shared/system\.js"[^>]*></script>',
    f'<script>\n/* inlined from _shared/system.js */\n{js}\n</script>',
    html, count=1,
)
# rewrite the "Back to Group" switch link from ../index.html to /
# (each site is now its own root in its Vercel project)
html = html.replace('href="../index.html"', 'href="https://empora-group.vercel.app/"')
html = html.replace('href="../h2/index.html"',           'href="https://h2-empora.vercel.app/"')
html = html.replace('href="../intelligence/index.html"', 'href="https://intelligence-empora.vercel.app/"')
html = html.replace('href="../emporom/index.html"',      'href="https://emporom-empora.vercel.app/"')
pathlib.Path(dst).write_text(html)
print(f"   inlined → {dst}")
PY
}

echo "→ h2/"
inline_shared "$ROOT/h2/index.html"       "$DEPLOY/h2/index.html"
# emporom/ standalone is the donor — NOT built. Real Emporom Media =
# empwebv2 React app at ~/Documents/GitHub/empwebv2 (its own deploy).

# ---------- per-site vercel.json (clean config) ----------------
for site in group h2 intelligence; do
  cat > "$DEPLOY/$site/vercel.json" <<JSON
{
  "\$schema": "https://openapi.vercel.sh/vercel.json",
  "cleanUrls": true,
  "trailingSlash": false,
  "headers": [
    {
      "source": "/(.*)",
      "headers": [
        { "key": "X-Content-Type-Options", "value": "nosniff" },
        { "key": "Referrer-Policy", "value": "strict-origin-when-cross-origin" }
      ]
    }
  ]
}
JSON
done

echo ""
echo "✓ Build complete. Deploy artefacts in:"
echo "    $DEPLOY/group/"
echo "    $DEPLOY/h2/"
echo "    $DEPLOY/intelligence/"
echo ""
echo "    [Emporom Media] deploys separately from ~/Documents/GitHub/empwebv2"
