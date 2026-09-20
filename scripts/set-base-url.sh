#!/usr/bin/env bash
# Rewrite every absolute site URL (canonicals, OG tags, JSON-LD, sitemap, robots, llms.txt)
# to a new base. Use it to point the build at a staging host and back at production.
#
#   ./scripts/set-base-url.sh https://ryankolean.github.io/meantime
#   ./scripts/set-base-url.sh https://www.meantimeoncass.com
#
# Umbo precedent: doing this by hand leaves half the tags pointing at the old host.

set -euo pipefail

if [ $# -ne 1 ]; then
  echo "usage: $0 <new-base-url>   (no trailing slash)" >&2
  exit 1
fi

NEW="${1%/}"
ROOT="$(cd "$(dirname "$0")/.." && pwd)"

# Find whatever base is currently in the canonical tag on the homepage.
CURRENT=$(grep -oE '<link rel="canonical" href="https?://[^/"]+' "$ROOT/index.html" | head -1 | sed 's|.*href="||')

if [ -z "$CURRENT" ]; then
  echo "could not read the current base url from index.html" >&2
  exit 1
fi

if [ "$CURRENT" = "$NEW" ]; then
  echo "already set to $NEW"
  exit 0
fi

echo "rewriting $CURRENT -> $NEW"

find "$ROOT" -maxdepth 1 -type f \( -name '*.html' -o -name '*.xml' -o -name '*.txt' -o -name '*.webmanifest' \) -print0 |
  while IFS= read -r -d '' f; do
    if grep -q "$CURRENT" "$f"; then
      sed -i '' "s|$CURRENT|$NEW|g" "$f"
      echo "  $(basename "$f")"
    fi
  done

echo "done. Check: grep -rn '$CURRENT' $ROOT --include='*.html' --include='*.xml' --include='*.txt'"
