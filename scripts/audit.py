"""Wiki audit v2: link integrity, data coverage, stale text, thin pages."""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"

issues: list[str] = []


def issue(msg: str):
    issues.append(msg)
    print("ISSUE:", msg)


slug_set = set()
coll_slugs = defaultdict(set)
for d in CONTENT.iterdir():
    if d.is_dir():
        for f in d.glob("*.md"):
            slug_set.add(f.stem)
            coll_slugs[d.name].add(f.stem)
print("=== collections:", {k: len(v) for k, v in sorted(coll_slugs.items())})

# 1. wikilinks
wl = re.compile(r"\[\[([^\]|\\]+)")
broken = Counter()
total_links = 0
for f in CONTENT.rglob("*.md"):
    for m in wl.finditer(f.read_text(encoding="utf-8")):
        t = m.group(1).strip().lower().replace(" ", "-")
        total_links += 1
        if t not in slug_set:
            broken[t] += 1
print(f"=== wikilinks: {total_links} total, {sum(broken.values())} broken")
for t, c in broken.most_common(10):
    if t != "super-17":  # unreleased S2 character, intentionally plain text
        issue(f"broken link [[{t}]] x{c}")

# 2. stale text
for pat in ["pending fresh", "schema dump", "TODO", "TBD", '"Unsorted"']:
    hits = [f for f in CONTENT.rglob("*.md") if pat in f.read_text(encoding="utf-8")]
    if hits:
        issue(f"stale text {pat!r} in {len(hits)} files e.g. {hits[0].name}")

# 3. false vanish-cost claims
for f in CONTENT.rglob("*.md"):
    t = f.read_text(encoding="utf-8")
    for m in re.finditer(r".{40}2,800.{40}", t):
        ctx = m.group(0).lower()
        if not any(w in ctx for w in ["drain", "sparking", "gauge"]):
            issue(f"suspect 2,800 in {f.relative_to(CONTENT)}: …{m.group(0)[30:90]}…")

# 4. characters coverage
play_no_dp = play_no_sw = no_stock = 0
for f in (CONTENT / "characters").glob("*.md"):
    fm = f.read_text(encoding="utf-8").split("---")[1]
    playable = "playable: true" in fm
    if playable:
        if not re.search(r"^dp: \d", fm, re.M):
            play_no_dp += 1
            issue(f"playable without dp: {f.stem}")
        if "strengths:" not in fm:
            play_no_sw += 1
        if "maxSkillStock" not in fm and "initialSkillStock" not in fm:
            no_stock += 1
print(
    f"=== characters: playable-without-S/W={play_no_sw}, without-stock-fields={no_stock}"
)
if play_no_sw:
    issue(f"{play_no_sw} playable characters missing strengths/weaknesses")

# 5. skills effects coverage
no_eff = [
    f.stem
    for f in (CONTENT / "skills").glob("*.md")
    if "effect:" not in f.read_text(encoding="utf-8")
]
if no_eff:
    issue(f"{len(no_eff)} skills without effect: {no_eff[:6]}")

# 6. blasts category & damage coverage
no_cat = dmg_pages = 0
for f in (CONTENT / "blasts").glob("*.md"):
    t = f.read_text(encoding="utf-8")
    if "category:" not in t.split("---")[1]:
        no_cat += 1
    if re.search(r"^\s+damage: \d", t, re.M):
        dmg_pages += 1
print(
    f"=== blasts: {len(coll_slugs['blasts'])} pages, {no_cat} without category, {dmg_pages} with datamined damage"
)

# 7. thin curated pages
for coll, minlen in [
    ("mechanics", 1500),
    ("guides", 3000),
    ("episode-battles", 5000),
    ("patches", 1200),
]:
    for f in (CONTENT / coll).glob("*.md"):
        n = len(f.read_text(encoding="utf-8"))
        if n < minlen:
            issue(f"thin page {coll}/{f.stem} ({n} chars)")

# 8. transformations statChanges
no_sc = [
    f.stem
    for f in (CONTENT / "transformations").glob("*.md")
    if "statChanges:" not in f.read_text(encoding="utf-8")
]
if no_sc:
    issue(f"{len(no_sc)} transformations without statChanges: {no_sc[:4]}")

# 9. meta.json slug validity
meta = json.loads((ROOT / "data-mined" / "meta.json").read_text(encoding="utf-8"))
bad = []
for band in meta.get("singles", []) + meta.get("dp", []):
    for e in band["entries"]:
        if e["slug"] not in coll_slugs["characters"]:
            bad.append(e["slug"])
for c in meta.get("counters", []):
    for s in [c["slug"], *c.get("beats", []), *c.get("losesTo", [])]:
        if s not in coll_slugs["characters"]:
            bad.append(s)
if bad:
    issue(f"meta.json dead slugs: {sorted(set(bad))[:8]}")

# 10. search index
idx = json.loads((ROOT / "public" / "search-index.json").read_text(encoding="utf-8"))
total_pages = sum(len(v) for v in coll_slugs.values())
print(f"=== search index {len(idx)} entries vs {total_pages} pages")
if len(idx) < total_pages - 5:
    issue(f"search index missing entries ({len(idx)} < {total_pages})")

print(f"\n==== AUDIT {'CLEAN' if not issues else f'FOUND {len(issues)} ISSUES'} ====")
