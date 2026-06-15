"""Check 5: built-HTML internal href graph + glossary anchor validation.

Scans every .next/server/app/**/*.html, extracts internal href="/..." (and #fragments),
verifies each resolves to a real static route/page, validates /glossary#slug anchors against
real glossary ids, and flags href="#" dead anchors.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict

from a7_lib import BUILT, CONTENT, iter_files

# ---- valid path set ----
UTILITY = {"/", "/stats", "/meta", "/compare", "/dna", "/classes"}
COLLECTIONS = ["characters", "blasts", "skills", "transformations", "mechanics",
               "game-modes", "episode-battles", "patches", "dlc", "guides",
               "stages", "shop", "glossary"]
valid_paths = set(UTILITY)
glossary_slugs = set()
for coll in COLLECTIONS:
    valid_paths.add(f"/{coll}")
    for f in iter_files(coll):
        if coll == "glossary":
            glossary_slugs.add(f.stem)
        else:
            valid_paths.add(f"/{coll}/{f.stem}")

HREF_RE = re.compile(r'href="([^"]+)"')
strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)

dead_base = Counter()
dead_base_sample = {}
dead_anchor = Counter()          # /glossary#badfrag
dead_anchor_sample = {}
hash_only = Counter()            # href="#"
hash_only_sample = {}
other_frag = Counter()           # non-glossary fragment hrefs (informational)
pages = 0
all_internal = Counter()

for f in BUILT.rglob("*.html"):
    pages += 1
    rel = str(f.relative_to(BUILT)).replace("\\", "/")
    html = strip_scripts(f.read_text(encoding="utf-8", errors="ignore"))
    for href in HREF_RE.findall(html):
        if href.startswith(("http://", "https://", "mailto:")):
            continue
        if href == "#":
            hash_only[rel] += 1
            hash_only_sample.setdefault("x", rel)
            continue
        if not href.startswith(("/", "#")):
            continue
        if href.startswith("/_next") or href.startswith("/search-index"):
            continue
        base, _, frag = href.partition("#")
        base = (base.rstrip("/") or "/") if base else ""
        all_internal[base + ("#" + frag if frag else "")] += 1
        if frag and base == "/glossary":
            if frag not in glossary_slugs:
                dead_anchor[href] += 1
                dead_anchor_sample.setdefault(href, rel)
            continue
        if frag and base != "/glossary":
            other_frag[href] += 1
            # still validate the base
        if base and base not in valid_paths:
            dead_base[base] += 1
            dead_base_sample.setdefault(base, rel)

print(f"=== scanned {pages} built HTML pages")
print(f"=== valid paths: {len(valid_paths)} (+{len(glossary_slugs)} glossary anchors)")
print(f"=== distinct internal href targets seen: {len(all_internal)}")

print(f"\n--- DEAD internal href bases: {len(dead_base)} distinct ---")
for base, c in dead_base.most_common(40):
    print(f"   {base}  x{c}  e.g. {dead_base_sample[base]}")

print(f"\n--- DEAD /glossary#anchor (no such glossary id): {len(dead_anchor)} distinct ---")
for href, c in dead_anchor.most_common(40):
    print(f"   {href}  x{c}  e.g. {dead_anchor_sample[href]}")

print(f"\n--- href=\"#\" dead anchors: {sum(hash_only.values())} occurrences on {len(hash_only)} pages ---")
for rel, c in hash_only.most_common(20):
    print(f"   {rel}  x{c}")

print(f"\n--- non-glossary #fragment hrefs (informational): {len(other_frag)} distinct ---")
for href, c in other_frag.most_common(20):
    print(f"   {href}  x{c}")
