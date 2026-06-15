import json, re
from collections import Counter
from pathlib import Path
import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content" / "blasts"
pages = []
for f in sorted(CONTENT.glob("*.md")):
    raw = f.read_text(encoding="utf-8")
    fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", raw, re.S).group(1))
    pages.append((f.stem, fm))

n = len(pages)
supers = sum(1 for s, fm in pages if fm.get("class") == "super")
ults = sum(1 for s, fm in pages if fm.get("class") == "ultimate")
with_cat = sum(1 for s, fm in pages if fm.get("category"))
dmg_pages = [s for s, fm in pages if any(u.get("damage") for u in fm.get("users") or [])]
multihit_pages = [s for s, fm in pages if any(u.get("hits") for u in fm.get("users") or [])]
chip_pages = [s for s, fm in pages if any(u.get("chip") for u in fm.get("users") or [])]
total_users = sum(len(fm.get("users") or []) for s, fm in pages)
cat_counter = Counter(fm.get("category") for s, fm in pages if fm.get("category"))

print(f"pages={n} supers={supers} ults={ults}")
print(f"pages with category={with_cat} ({n-with_cat} without)")
print(f"pages asserting datamined damage={len(dmg_pages)}")
print(f"pages with multi-hit={len(multihit_pages)}")
print(f"pages with chip={len(chip_pages)}")
print(f"total user rows across all pages={total_users}")
print("category distribution (page-level):")
for c, k in cat_counter.most_common():
    print(f"   {k:4} {c}")
