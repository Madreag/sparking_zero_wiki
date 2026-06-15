"""Agent 3 skills follow-up: no-user skills, enrichment-only costs, confidence honesty,
enrichment-sourced users validity, trailing-space names."""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
CONTENT = ROOT / "content"

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

skills_catalog = load(DM / "skills_catalog.json")
chars = load(DM / "characters.json")
skill_enrich = load(DM / "enrichment" / "skills.json") or {}
skill_fx = load(DM / "enrichment" / "skill_effects.json") or {}

byname = defaultdict(list)
game_desc = {}
for sk in skills_catalog:
    if sk["name"] and sk["name"] != "None":
        byname[sk["name"]].append(sk["index"])
        if sk.get("descDatamined") and sk["name"] not in game_desc:
            game_desc[sk["name"]] = sk["descDatamined"]

skill_users = defaultdict(list)
for cid, c in sorted(chars.items()):
    if not c["name"]:
        continue
    for sk in c.get("s1Skills") or []:
        if sk.get("name"):
            skill_users[sk["name"]].append((cid, c["fullName"] or c["name"], sk.get("cost") if False else sk.get("skillCost")))

def expected(name):
    e = dict(skill_fx.get(name, {}))
    e.update({k: v for k, v in (skill_enrich.get(name) or {}).items() if v})
    users = skill_users.get(name, [])
    mined = sorted({u[2] for u in users if u[2] is not None})
    cost = (mined[0] if len(mined) == 1 else e.get("skillCost") if not mined else None)
    fc = cost if cost is not None else e.get("skillCost")
    return e, users, mined, fc

print("=== 2 skills with 0 datamined users ===")
for name in sorted(byname):
    if not skill_users.get(name):
        e, users, mined, fc = expected(name)
        print(f"  '{name}': enrich_users={e.get('users')} cost={fc} conf={e.get('confidence','datamined(DEFAULT)')} "
              f"effect={'Y' if (e.get('effect') or game_desc.get(name)) else 'NONE'} game_desc={'Y' if game_desc.get(name) else 'N'}")

print("\n=== enrichment-only cost skills (0 datamined cost, enrichment provides) ===")
for name in sorted(byname):
    e, users, mined, fc = expected(name)
    if not mined and fc is not None:
        conf = (skill_enrich.get(name) or {}).get("confidence") or skill_fx.get(name, {}).get("confidence") or "datamined(DEFAULT)"
        print(f"  '{name}': cost={fc} users(datamined)={len(users)} conf={conf}")

print("\n=== confidence honesty: confidence=='datamined' but NO datamined substance ===")
# datamined substance = has datamined users OR datamined game_desc
flagged = 0
for f in sorted((CONTENT / "skills").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    name = fm.get("name")
    conf = fm.get("confidence")
    has_users = bool(skill_users.get(name))
    has_desc = bool(game_desc.get(name))
    if conf == "datamined" and not has_users and not has_desc:
        flagged += 1
        print(f"  {f.stem}: confidence=datamined but 0 datamined users & no game_desc")
print(f"  flagged={flagged}")

print("\n=== userCount vs len(users) across ALL skill pages ===")
bad = 0
for f in sorted((CONTENT / "skills").glob("*.md")):
    txt = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", txt, re.S)
    fm = yaml.safe_load(m.group(1)) if m else {}
    uc = fm.get("userCount")
    nu = len(fm.get("users", []) or [])
    if (uc is None and nu > 0) or (uc is not None and uc != nu):
        bad += 1
        print(f"  {f.stem}: userCount={uc} len(users)={nu}")
print(f"  inconsistent userCount pages: {bad}")

print("\n=== Validate 'Fury' enrichment users vs game data ===")
for cid in ("0031_00", "0031_01", "0031_02", "0032_00", "0032_01", "0032_10"):
    c = chars.get(cid)
    if c:
        s1 = [(sk.get("slot"), sk.get("name")) for sk in c.get("s1Skills") or []]
        print(f"  {cid} {c.get('fullName') or c.get('name')}: s1Skills={s1}")
# any character whose s1 skill name contains 'Fury' or anger?
hits = []
for cid, c in chars.items():
    for sk in c.get("s1Skills") or []:
        if sk.get("name") and "fury" in sk["name"].lower():
            hits.append((cid, c.get("fullName") or c.get("name"), sk["name"]))
print(f"  any s1Skill named like 'Fury': {hits}")

print("\n=== trailing-space character names (source of cosmetic NIT) ===")
ts = [(cid, repr(c.get("fullName") or c.get("name"))) for cid, c in chars.items()
      if (c.get("fullName") or c.get("name") or "") != (c.get("fullName") or c.get("name") or "").strip()]
for cid, nm in ts:
    print(f"  {cid}: {nm}")
print(f"  total trailing/leading-space names: {len(ts)}")
