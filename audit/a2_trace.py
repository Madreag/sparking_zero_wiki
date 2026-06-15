"""Agent-2 deep trace: collisions, kiCost vs raw ExpendEnergy, 20+ damage traces to raw."""
import json
import re
from collections import defaultdict
from pathlib import Path

import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RAW = DM / "raw" / "masterdata"
CONTENT = ROOT / "content"


def props(entry):
    if not entry:
        return {}
    return entry[0].get("Properties") or {}


def slot_of_action(a):
    if "SPM1" in a:
        return "SPM1"
    if "SPM2" in a:
        return "SPM2"
    if "ULT" in a or "UB" in a:
        return "ULT"
    return None


blast_index = json.load(open(DM / "blast_index.json", encoding="utf-8"))
blastskill = json.load(open(RAW / "BlastSkill.json", encoding="utf-8"))
blastult = json.load(open(RAW / "BlastUltimate.json", encoding="utf-8"))
raw_bullets = json.load(open(RAW / "BulletSetting" / "BulletParam.json", encoding="utf-8"))

# index raw bullets per cid+slot with key
bullets_by = defaultdict(lambda: defaultdict(list))
for k, v in raw_bullets.items():
    m = re.match(r"BulletParam_(\d{4}_\d{2})_(act.+)$", k)
    if not m:
        continue
    cid, action = m.group(1), m.group(2)
    slot = slot_of_action(action)
    if not slot:
        continue
    p = props(v)
    if not any(p.get(x) for x in ("Power", "BeamPower", "Shave", "BeamShave")):
        continue
    bullets_by[cid][slot].append((k, p.get("Power"), p.get("BeamPower"), p.get("Shave"), p.get("BeamShave"), p.get("CollisionRevibeNum")))


def melee_keys(cid, slot):
    f = RAW / "Combatives" / f"{cid}.json"
    out = []
    if f.exists():
        d = json.load(open(f, encoding="utf-8"))
        for k, v in d.items():
            m = re.match(r"Combatives(?:SubParam)?_\d{4}_\d{2}_(act.+)$", k)
            if not m:
                continue
            if slot_of_action(m.group(1)) != slot:
                continue
            p = props(v)
            if p.get("Power"):
                out.append((k, p.get("Power")))
    return out


# ---------- 1. collisions ----------
print("=" * 70)
print("1. SLUG COLLISIONS IN blast_index (name+class -> same slug)")
print("=" * 70)


def slugify(s):
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


by_slug = defaultdict(list)
for b in blast_index:
    by_slug[f"{slugify(b['name'])}-{b['class']}"].append(b)
for slug, bs in by_slug.items():
    if len(bs) > 1:
        print(f"\nSLUG {slug}:")
        for b in bs:
            us = [u["character"] for u in b["users"]]
            print(f"   name={b['name']!r}  class={b['class']}  users({len(us)})={us}")

# ---------- 2. kiCost vs raw ExpendEnergy ----------
print("\n" + "=" * 70)
print("2. kiCost SAMPLE vs raw BlastSkill/BlastUltimate ExpendEnergy")
print("=" * 70)
SLOT_TO_BS = {"SPM1": "BlastSkill1_{}", "SPM2": "BlastSkill2_{}"}
# pick a spread of samples by (blast name, class, character, expected ki)
samples = [
    ("Final Flash", "super"), ("Final Kamehameha", "super"), ("Wolf Fang Fist", "super"),
    ("High Speed Rush", "super"), ("Kamehameha", "super"), ("Spirit Bomb", "ultimate"),
    ("Big Bang Attack", "ultimate"), ("Planet Geyser", "ultimate"), ("Blaster Meteor", "super"),
    ("Death Storm", "super"), ("Body Change", "ultimate"),
]
idx_by = {(b["name"], b["class"]): b for b in blast_index}
for nm, cl in samples:
    b = idx_by.get((nm, cl))
    if not b:
        print(f"  [{nm} / {cl}] not in index")
        continue
    for u in b["users"][:2]:
        cid = u["charId"]
        slot = u["slot"]
        page_ki = u.get("kiCost")
        if cl == "super":
            asset = props(blastskill.get(SLOT_TO_BS[slot].format(cid)))
            raw_ki = asset.get("ExpendEnergy")
            raw_trig = asset.get("TriggerExpendEnergy")
            tag = "OK" if raw_ki == page_ki else "MISMATCH"
            print(f"  [{tag}] {nm:24} {u['character']:22} {cid}/{slot} page_ki={page_ki} raw ExpendEnergy={raw_ki} trig={raw_trig}")
        else:
            asset = props(blastult.get(f"BlastUltimate_{cid}")) or props(blastult.get(f"BlastUltimate2_{cid}"))
            raw_ki = asset.get("ExpendEnergy")
            tag = "OK" if raw_ki == page_ki else "MISMATCH"
            print(f"  [{tag}] {nm:24} {u['character']:22} {cid}/ULT page_ki={page_ki} raw ExpendEnergy={raw_ki}")

# ---------- 3. damage traces ----------
print("\n" + "=" * 70)
print("3. DAMAGE TRACE: every blast page user with damage -> raw entry")
print("=" * 70)

# read all blast pages, collect users with damage
rows = []
for f in sorted((CONTENT / "blasts").glob("*.md")):
    raw = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    fm = yaml.safe_load(m.group(1))
    for u in fm.get("users") or []:
        if u.get("damage"):
            rows.append((f.stem, fm.get("category"), fm.get("class"), u))

# map characterSlug+name -> charId via blast_index
slug_name_to_cid = {}
for b in blast_index:
    for u in b["users"]:
        slug_name_to_cid[(u["character"], b["name"], b["class"])] = u["charId"]

print(f"\nTotal page-user rows with damage: {len(rows)}\n")
for slug, cat, cls, u in rows:
    # recover name/class from slug page
    nm = None
    for b in blast_index:
        if f"{slugify(b['name'])}-{b['class']}" == slug:
            nm = b["name"]
            break
    cid = slug_name_to_cid.get((u["character"], nm, cls))
    slot = u.get("notes")
    bl = bullets_by.get(cid, {}).get(slot, [])
    me = melee_keys(cid, slot)
    src = "?"
    detail = ""
    bull_max = 0
    for (k, pw, bpw, sh, bsh, mh) in bl:
        cand = max(x for x in (bpw, pw, 0) if x is not None)
        bull_max = max(bull_max, cand)
    melee_max = max([p for (_, p) in me], default=0)
    if melee_max and (bull_max == 0 or melee_max > bull_max):
        src = "Combatives"
        mk = [k for (k, p) in me if p == melee_max]
        detail = f"{mk[0]} Power={melee_max}"
    else:
        src = "BulletParam"
        best = max(bl, key=lambda t: max(x for x in (t[2], t[1], 0) if x is not None), default=None)
        if best:
            k, pw, bpw, sh, bsh, mh = best
            detail = f"{k} Power={pw} BeamPower={bpw} Shave={sh} BeamShave={bsh} Revibe={mh}"
    print(f"  {slug:42} {u['character']:20} {cid}/{slot} cat={cat!r:14} page(d={u.get('damage')},chip={u.get('chip')},hits={u.get('hits')}) <- {src}: {detail}")
