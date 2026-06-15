"""Check 8 (corrected): autolink integrity in the BUILT HTML.

8a CONTROL: stray NUL (\\x00) leakage (would indicate an unrestored placeholder).
8b self-links: detail pages (all collections EXCEPT characters/blasts, which pass
   excludeHref) whose rendered body links to themselves.
8c wrong-target risk: duplicate display-name labels (autolink first-wins) and
   common-word/short labels that can mis-link; verified against built HTML.
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict

from a7_lib import BUILT, build_index, build_name_index, STOP_MARKDOWN, iter_files

idx, owners, aliases = build_index()
name_map = build_name_index(idx, STOP_MARKDOWN)

strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)
A_RE = re.compile(r'<a [^>]*href="([^"]+)"[^>]*>(.*?)</a>', re.S)

# ---- 8a: stray NUL ----
nul_pages = []
for f in BUILT.rglob("*.html"):
    t = f.read_text(encoding="utf-8", errors="ignore")
    if "\x00" in t:
        nul_pages.append(str(f.relative_to(BUILT)))
print(f"=== stray NUL (\\x00) in built HTML: {len(nul_pages)} pages")
for p in nul_pages[:10]:
    print("   ", p)

# ---- 8b: self-links ----
NO_EXCLUDE = ["mechanics", "game-modes", "episode-battles", "patches", "dlc",
              "guides", "transformations", "skills", "stages", "shop"]
self_links = []
for coll in NO_EXCLUDE:
    for f in iter_files(coll):
        bp = BUILT / coll / f"{f.stem}.html"
        if not bp.exists():
            continue
        own = f"/{coll}/{f.stem}"
        html = strip_scripts(bp.read_text(encoding="utf-8", errors="ignore"))
        # count <a href="own"> that are inside prose (heuristic: not the breadcrumb back-link,
        # which uses text starting with the left-arrow)
        for href, inner in A_RE.findall(html):
            if (href.rstrip("/") or "/") == own and "\u2190" not in inner and "←" not in inner:
                self_links.append((coll, f.stem, inner.strip()[:40]))
print(f"\n=== self-links (page body links to itself): {len(self_links)}")
for coll, stem, inner in self_links[:40]:
    print(f"   {coll}/{stem}: link text={inner!r}")

# ---- 8c: duplicate display-name labels (autolink first-wins ambiguity) ----
label_targets = defaultdict(list)   # lower label -> list of (href, collection, slug)
for key, e in idx.items():
    lab = e["label"]
    if not lab or len(lab) < 4 or "\u2192" in lab:
        continue
    if e["kind"] == "alias":
        continue
    label_targets[lab.lower()].append((e["href"], e["collection"], key))
dup_labels = {l: ts for l, ts in label_targets.items() if len({t[0] for t in ts}) > 1}
print(f"\n=== duplicate display-name labels (>1 distinct href; autolink picks first-wins): {len(dup_labels)}")
for lab, ts in sorted(dup_labels.items()):
    winner = name_map.get(lab)
    print(f"   {lab!r} -> autolinks to {winner}; candidates: {[(t[1], t[0]) for t in ts]}")

# ---- 8c2: common English words that are autolink labels (over-link risk) ----
COMMON = {"cell","beam","time","base","story","standard","wish","rush","smash","kid",
          "future","hero","power","light","dragon","giant","perception","shop","training",
          "versus","fusion","android","frieza","trunks","goku","gohan","gods","fusions",
          "instant","custom","whis","beast","kale","hit","broly"}
common_labels = sorted(l for l in name_map if l in COMMON)
print(f"\n=== autolink labels that are common words (potential mis-link, case-insensitive match): {len(common_labels)}")
for l in common_labels:
    print(f"   {l!r} -> {name_map[l]}")
