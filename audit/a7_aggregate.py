"""Final aggregation for the report: collection breakdowns + full lost-page list."""
from __future__ import annotations

import re
from collections import Counter, defaultdict

from a7_lib import (BUILT, CONTENT, build_index, build_name_index, STOP_MARKDOWN,
                    iter_files, normalize_slug, WIKILINK_RE)

idx, owners, aliases = build_index()

# escaped-pipe victims by source collection
victims_by_coll = Counter()
victims_total = 0
for f in sorted(CONTENT.rglob("*.md")):
    coll = f.parent.name
    for line in f.read_text(encoding="utf-8").splitlines():
        for m in WIKILINK_RE.finditer(line):
            t = m.group(1)
            if t.endswith("\\") and normalize_slug(t.rstrip("\\")) in idx:
                victims_by_coll[coll] += 1
                victims_total += 1
print(f"=== escaped-pipe victim wikilinks by SOURCE collection (total {victims_total}) ===")
for coll, c in victims_by_coll.most_common():
    print(f"   {coll}: {c}")

# self-links by collection
A_RE = re.compile(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)
strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)
NO_EXCLUDE = ["mechanics", "game-modes", "episode-battles", "patches", "dlc",
              "guides", "transformations", "skills", "stages", "shop"]
self_by_coll = Counter()
for coll in NO_EXCLUDE:
    for f in iter_files(coll):
        bp = BUILT / coll / f"{f.stem}.html"
        if not bp.exists():
            continue
        own = f"/{coll}/{f.stem}"
        html = strip_scripts(bp.read_text(encoding="utf-8", errors="ignore"))
        for href, inner in A_RE.findall(html):
            if (href.rstrip("/") or "/") == own and "\u2190" not in inner and "←" not in inner:
                self_by_coll[coll] += 1
print(f"\n=== self-links by collection (total {sum(self_by_coll.values())}) ===")
for coll, c in self_by_coll.most_common():
    print(f"   {coll}: {c}")

# glossary-body wikilinks that never render (glossary page shows definition only)
gloss_body_links = 0
for f in iter_files("glossary"):
    raw = f.read_text(encoding="utf-8")
    parts = raw.split("---", 2)
    body = parts[2] if len(parts) >= 3 else ""
    gloss_body_links += len(WIKILINK_RE.findall(body))
print(f"\n=== wikilinks inside glossary BODIES (never rendered; page shows 'definition' only): {gloss_body_links}")
