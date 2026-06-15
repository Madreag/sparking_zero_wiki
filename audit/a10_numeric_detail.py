"""Agent 10 numeric drill-down: characterize super-ki 'outliers', HP-count
mismatch vs datamine, and verify name-duplicates are cross-class. READ-ONLY."""
import re
from pathlib import Path
from collections import Counter, defaultdict
import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"


def load(coll):
    recs = []
    for f in sorted((CONTENT / coll).glob("*.md")):
        t = f.read_text(encoding="utf-8")
        parts = t.split("\n")
        end = next((i for i in range(1, len(parts)) if parts[i].strip() == "---"), None)
        fm = yaml.safe_load("\n".join(parts[1:end])) or {}
        recs.append((f.stem, fm))
    return recs


# ---- super / ultimate ki cost distributions ----
print("=== blast2 (super) kiCost distribution — character moveset ===")
ms_super = Counter()
ms_ult = Counter()
for slug, fm in load("characters"):
    for m in (fm.get("moveset") or []):
        if not isinstance(m, dict):
            continue
        ki = m.get("kiCost")
        if ki is None:
            continue
        if m.get("type") == "blast2":
            ms_super[ki] += 1
        elif m.get("type") == "ultimate":
            ms_ult[ki] += 1
print(" super:", dict(sorted(ms_super.items())))
print(" ult  :", dict(sorted(ms_ult.items())))

print("\n=== blast pages per-user kiCost distribution by class ===")
b_super = Counter()
b_ult = Counter()
for slug, fm in load("blasts"):
    cls = fm.get("class")
    for u in (fm.get("users") or []):
        if not isinstance(u, dict):
            continue
        ki = u.get("kiCost")
        if ki is None:
            continue
        (b_super if cls == "super" else b_ult)[ki] += 1
print(" super:", dict(sorted(b_super.items())))
print(" ult  :", dict(sorted(b_ult.items())))

# anything truly anomalous (super >40k or <5k ; ult <40k or >60k)
print("\n=== TRULY anomalous (super outside 5k-40k, ult outside 40k-60k) ===")
anom = []
for slug, fm in load("characters"):
    for m in (fm.get("moveset") or []):
        if not isinstance(m, dict):
            continue
        ki = m.get("kiCost")
        if ki is None:
            continue
        if m.get("type") == "blast2" and not (5000 <= ki <= 40000):
            anom.append(("char", slug, m.get("name"), "super", ki))
        if m.get("type") == "ultimate" and not (40000 <= ki <= 60000):
            anom.append(("char", slug, m.get("name"), "ult", ki))
for slug, fm in load("blasts"):
    cls = fm.get("class")
    for u in (fm.get("users") or []):
        if not isinstance(u, dict):
            continue
        ki = u.get("kiCost")
        if ki is None:
            continue
        if cls == "super" and not (5000 <= ki <= 40000):
            anom.append(("blast", slug, u.get("character"), "super", ki))
        if cls == "ultimate" and not (40000 <= ki <= 60000):
            anom.append(("blast", slug, u.get("character"), "ult", ki))
print(" count:", len(anom))
for a in anom[:30]:
    print("   ", a)

# ---- HP distribution: split by playable, find the +4 vs datamine ----
print("\n=== HP distribution split by playable ===")
hp_play = Counter()
hp_nonplay = Counter()
hp_pages = defaultdict(list)
for slug, fm in load("characters"):
    hp = fm.get("hp")
    if hp is None:
        continue
    playable = fm.get("playable", True)
    (hp_play if playable else hp_nonplay)[hp] += 1
    hp_pages[hp].append((slug, playable, fm.get("hpInherited", False), fm.get("baseCharacter")))
print(" playable    :", dict(sorted(hp_play.items())))
print(" non-playable:", dict(sorted(hp_nonplay.items())))
total = Counter()
for hp in hp_pages:
    total[hp] = len(hp_pages[hp])
print(" total       :", dict(sorted(total.items())))
expected = {30000: 9, 35000: 14, 40000: 147, 45000: 16}
print(" datamine exp:", expected)
print(" DELTA (content - datamine):", {hp: total[hp] - expected.get(hp, 0) for hp in sorted(total)})

# how many playable have null HP?
null_play = [slug for slug, fm in load("characters") if fm.get("hp") is None and fm.get("playable", True)]
print(f"\n playable pages with NULL hp: {len(null_play)} e.g. {null_play[:10]}")
# non-playable with HP (candidates for the +extra)
nonplay_hp = [(slug, fm.get("hp")) for slug, fm in load("characters") if fm.get("hp") is not None and not fm.get("playable", True)]
print(f" non-playable pages WITH hp: {len(nonplay_hp)} -> {nonplay_hp}")

# ---- verify name dupes are cross-class super/ultimate ----
print("\n=== name-duplicate verification (blasts) ===")
names = defaultdict(list)
for slug, fm in load("blasts"):
    names[fm.get("name")].append((slug, fm.get("class")))
not_crossclass = []
for nm, lst in names.items():
    if len(lst) > 1:
        classes = sorted(set(c for _, c in lst))
        if classes != ["super", "ultimate"]:
            not_crossclass.append((nm, lst))
print(" blast name-dupes that are NOT a clean super+ultimate pair:", len(not_crossclass))
for x in not_crossclass[:20]:
    print("   ", x)

# transformations duplicate display names?
print("\n=== transformation name dupes ===")
tnames = defaultdict(list)
for slug, fm in load("transformations"):
    tnames[fm.get("name")].append(slug)
for nm, lst in tnames.items():
    if len(lst) > 1:
        print("   ", nm, lst)

# character display-name dupes
print("\n=== character name dupes ===")
cnames = defaultdict(list)
for slug, fm in load("characters"):
    cnames[fm.get("name")].append(slug)
for nm, lst in cnames.items():
    if len(lst) > 1:
        print("   ", nm, lst)
