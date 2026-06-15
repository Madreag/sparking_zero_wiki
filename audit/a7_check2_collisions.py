"""Check 2: slug-collision mis-resolution from first-wins priority.

For every slug owned by >1 collection, report owners (priority order), the winner, the
shadowed loser(s), and how many wikilinks actually target that slug (+ where), so we can
judge whether the likely link intent is satisfied by the winner.
"""
from __future__ import annotations

import re
from collections import defaultdict

from a7_lib import (CONTENT, PRIORITY, build_index, collection_items,
                    normalize_slug, WIKILINK_RE)

idx, owners, aliases = build_index()

# label/href per (collection, slug)
detail = {}
for coll in PRIORITY:
    for it in collection_items(coll):
        href = f"/glossary#{it['slug']}" if coll == "glossary" else f"/{coll}/{it['slug']}"
        detail[(coll, it["slug"])] = {"label": it["label"], "href": href}

# count wikilink targets (clean, ignoring escaped-pipe backslash) per slug
target_hits = defaultdict(list)
for f in sorted(CONTENT.rglob("*.md")):
    rel = str(f.relative_to(CONTENT)).replace("\\", "/")
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for m in WIKILINK_RE.finditer(line):
            key = normalize_slug(m.group(1).rstrip("\\"))
            target_hits[key].append((rel, i))

collisions = {s: cs for s, cs in owners.items() if len(cs) > 1}
# also glossary-alias vs slug collisions (alias shadowed by a real slug)
alias_shadowed = []
for k, (gslug, term) in aliases.items():
    e = idx.get(k)
    if e and e["kind"] != "alias":
        alias_shadowed.append((k, gslug, term, e["collection"], e["href"]))

print(f"=== SLUG COLLISIONS (same slug, >1 collection): {len(collisions)}")
print("priority order:", " > ".join(PRIORITY))
print()
for s, cs in sorted(collisions.items()):
    cs_sorted = sorted(cs, key=lambda c: PRIORITY.index(c))
    winner = cs_sorted[0]
    losers = cs_sorted[1:]
    hits = target_hits.get(s, [])
    print(f"[[{s}]]  owners={cs_sorted}")
    for c in cs_sorted:
        d = detail[(c, s)]
        tag = "WINNER" if c == winner else "shadowed"
        print(f"     - {c:16} {tag:8} label={d['label']!r} -> {d['href']}")
    if hits:
        print(f"     wikilink targets: {len(hits)} occurrence(s) e.g. {hits[0][0]}:{hits[0][1]}")
    else:
        print(f"     wikilink targets: 0 (no [[{s}]] in content)")
    print()

print(f"\n=== GLOSSARY ALIASES SHADOWED BY A REAL SLUG: {len(alias_shadowed)}")
for k, gslug, term, coll, href in sorted(alias_shadowed):
    hits = target_hits.get(k, [])
    print(f"  alias '{k}' (would->glossary#{gslug} '{term}') shadowed by {coll} {href}"
          f"  | wikilink hits: {len(hits)}")
