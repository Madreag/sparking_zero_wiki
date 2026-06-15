"""Check 1b: measure REAL impact of the escaped-pipe bug in the built HTML.

For every content page that contains escaped-pipe victim wikilinks, compute the set of
INTENDED hrefs (what they'd resolve to if fixed) and compare against the hrefs actually
present in the built HTML for that page. A missing intended href == a lost cross-reference
that autolink did NOT rescue.
"""
from __future__ import annotations

import re
from collections import defaultdict

from a7_lib import (BUILT, CONTENT, build_index, normalize_slug, WIKILINK_RE)

idx, owners, aliases = build_index()

# content page (coll, slug) -> built html path
def built_path(coll: str, stem: str):
    if coll == "glossary":
        return BUILT / "glossary.html"  # single page w/ anchors
    return BUILT / coll / f"{stem}.html"

HREF_RE = re.compile(r'href="(/[^"]*)"')

# gather victim intended hrefs per page
page_intended = defaultdict(set)   # (coll,stem) -> set(intended href)
page_victims = defaultdict(list)   # (coll,stem) -> [(target, line)]
for f in sorted(CONTENT.rglob("*.md")):
    coll = f.parent.name
    text = f.read_text(encoding="utf-8")
    for i, line in enumerate(text.splitlines(), 1):
        for m in WIKILINK_RE.finditer(line):
            target = m.group(1)
            if not target.endswith("\\"):
                continue
            clean = normalize_slug(target.rstrip("\\"))
            if clean in idx:
                page_intended[(coll, f.stem)].add(idx[clean]["href"])
                page_victims[(coll, f.stem)].append((clean, i))

total_pages = len(page_intended)
total_intended = sum(len(v) for v in page_intended.values())
lost_total = 0
rescued_total = 0
pages_with_loss = []

for (coll, stem), intended in sorted(page_intended.items()):
    bp = built_path(coll, stem)
    if not bp.exists():
        continue
    html = bp.read_text(encoding="utf-8", errors="ignore")
    html = re.sub(r"<script[\s\S]*?</script>", "", html)
    present = set(HREF_RE.findall(html))
    # normalize trailing slash
    present = {h.rstrip("/") or "/" for h in present}
    lost = {h for h in intended if (h.rstrip("/") or "/") not in present}
    rescued = intended - lost
    lost_total += len(lost)
    rescued_total += len(rescued)
    if lost:
        pages_with_loss.append((coll, stem, sorted(lost)))

print(f"=== pages with escaped-pipe victim links: {total_pages}")
print(f"=== distinct intended targets across those pages: {total_intended}")
print(f"=== intended targets RESCUED by autolink (href present): {rescued_total}")
print(f"=== intended targets LOST (href absent from rendered page): {lost_total}")
print(f"=== pages with >=1 lost cross-reference: {len(pages_with_loss)}")
print("\n----- PAGES WITH LOST CROSS-REFERENCES (top 40 by count) -----")
for coll, stem, lost in sorted(pages_with_loss, key=lambda x: -len(x[2]))[:40]:
    print(f"{coll}/{stem}: {len(lost)} lost -> {', '.join(lost[:8])}{' ...' if len(lost) > 8 else ''}")
