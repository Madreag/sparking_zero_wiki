"""Check 6: public/search-index.json integrity.

- every entry `h` resolves to a built page / valid route (glossary -> /glossary#slug)
- no duplicate hrefs
- entry count vs total content pages
- every entry has title `t` and group `g`
"""
from __future__ import annotations

import json
from collections import Counter

from a7_lib import BUILT, ROOT, iter_files

idx = json.loads((ROOT / "public" / "search-index.json").read_text(encoding="utf-8"))

UTILITY = {"/", "/stats", "/meta", "/compare", "/dna", "/classes"}
COLLECTIONS = ["characters", "blasts", "skills", "transformations", "mechanics",
               "game-modes", "episode-battles", "patches", "dlc", "guides",
               "stages", "shop", "glossary"]
valid_paths = set(UTILITY)
glossary_slugs = set()
content_total = 0
for coll in COLLECTIONS:
    valid_paths.add(f"/{coll}")
    for f in iter_files(coll):
        content_total += 1
        if coll == "glossary":
            glossary_slugs.add(f.stem)
        else:
            valid_paths.add(f"/{coll}/{f.stem}")

def built_exists(href: str) -> bool:
    base, _, frag = href.partition("#")
    base = base.rstrip("/") or "/"
    if base == "/glossary" and frag:
        return frag in glossary_slugs
    return base in valid_paths

print(f"=== search-index entries: {len(idx)}  | content files: {content_total}")

# field presence
miss_t = [e for e in idx if not e.get("t")]
miss_g = [e for e in idx if not e.get("g")]
miss_h = [e for e in idx if not e.get("h")]
no_x = [e for e in idx if not e.get("x")]
print(f"=== missing title t: {len(miss_t)}; missing group g: {len(miss_g)}; missing href h: {len(miss_h)}")
print(f"=== entries with empty hint x (informational): {len(no_x)}")
for e in miss_t[:10]:
    print("   missing t:", e)
for e in miss_g[:10]:
    print("   missing g:", e)

# dead hrefs
dead = [e for e in idx if not built_exists(e["h"])]
print(f"\n=== entries whose href does NOT resolve to a built page: {len(dead)}")
for e in dead[:30]:
    print(f"   {e['h']}  (t={e.get('t')!r} g={e.get('g')!r})")

# duplicates
hrefs = Counter(e["h"] for e in idx)
dups = {h: c for h, c in hrefs.items() if c > 1}
print(f"\n=== duplicate hrefs: {len(dups)}")
for h, c in list(dups.items())[:30]:
    print(f"   {h} x{c}")

# coverage: built detail pages missing from index
indexed = {e["h"].rstrip("/") or "/" for e in idx}
indexed_bases = {h.partition('#')[0].rstrip('/') or '/' for h in indexed}
missing_from_index = []
for p in sorted(valid_paths):
    if p in UTILITY or p in {f"/{c}" for c in COLLECTIONS}:
        continue  # listing/utility pages aren't indexed as content entries
    if p not in indexed_bases:
        missing_from_index.append(p)
print(f"\n=== detail pages absent from search index: {len(missing_from_index)}")
for p in missing_from_index[:30]:
    print("   ", p)

# group distribution
print("\n=== group distribution:", dict(Counter(e.get("g") for e in idx)))
