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
mkdir -p "$DEPLOY/group/assets" "$DEPLOY/h2" "$DEPLOY/intelligence" "$DEPLOY/emporom"
# Emporom Media now ships from THIS repo: the standalone cobalt/Southern-Cross
# site (emporom/index.html, Group-branded + schematics) is the emporom.media
# homepage, plus per-niche landing pages under emporom/niches/. The empwebv2
# React app is retired as the public front-end.

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
# end-state cross-site links = emporom.media subdomains (live once DNS is configured)
html = html.replace('href="../index.html"', 'href="https://group.emporom.media/"')
html = html.replace('href="../h2/index.html"',           'href="https://h2.emporom.media/"')
html = html.replace('href="../intelligence/index.html"', 'href="https://intelligence.emporom.media/"')
html = html.replace('href="../emporom/index.html"',      'href="https://emporom.media/"')
pathlib.Path(dst).write_text(html)
print(f"   inlined → {dst}")
PY
}

echo "→ h2/"
inline_shared "$ROOT/h2/index.html"       "$DEPLOY/h2/index.html"

echo "→ emporom/ (homepage + niche landing pages)"
inline_shared "$ROOT/emporom/index.html"  "$DEPLOY/emporom/index.html"
# Niche landing pages are self-contained (inline CSS) — copy as-is.
if [ -d "$ROOT/emporom/niches" ]; then
  cp -R "$ROOT/emporom/niches" "$DEPLOY/emporom/niches"
fi

# ---------- per-site vercel.json (clean config) ----------------
for site in group h2 intelligence emporom; do
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
echo "    $DEPLOY/emporom/   (+ /niches/*)"
