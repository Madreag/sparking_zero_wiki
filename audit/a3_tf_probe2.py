"""Agent 3 TF follow-up: raw-only edges, dropped collisions, independent HP deltas."""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RAW = DM / "raw" / "masterdata"
CONTENT = ROOT / "content"

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def props(entry):
    return entry[0].get("Properties") or {} if entry else {}

transforms = load(DM / "transformations.json")
chars = load(DM / "characters.json")
enrich = load(DM / "enrichment" / "characters.json")
chardata = load(RAW / "CharacterData.json")

parsed_pairs = {(e["from"], e["to"]) for e in transforms}

# raw edges (all CharacterData entries)
raw = []
for key, val in chardata.items():
    if not key.startswith("CharacterData_"):
        continue
    cid = key[len("CharacterData_"):]
    battle = (props(val).get("CharacterDataAssetRecord") or {}).get("BattleAssets") or {}
    for fld, knd in (("FormChange", "transform"), ("Fusion", "fusion"), ("Potara", "potara")):
        v = battle.get(fld)
        vs = v if isinstance(v, list) else ([v] if v else [])
        for x in vs:
            if not x:
                continue
            tgt = (x.get("ChangeCharacter") or {}).get("Key")
            if not tgt:
                continue
            raw.append({"from": cid, "to": tgt, "kind": knd,
                        "hpRecovery": x.get("HpRecovery"),
                        "consumeBlastStock": x.get("ConsumeBlastStock")})

print("=== RAW-ONLY edges (in CharacterData but NOT in transformations.json) ===")
playable_cids = set(enrich.keys())  # enrichment only covers playable roster
for e in raw:
    if (e["from"], e["to"]) not in parsed_pairs:
        fn = chars.get(e["from"], {}).get("fullName") or chars.get(e["from"], {}).get("name") or "?"
        tn = chars.get(e["to"], {}).get("fullName") or chars.get(e["to"], {}).get("name") or "?"
        fp = "PLAYABLE" if e["from"] in playable_cids else "non-playable"
        tp = "PLAYABLE" if e["to"] in playable_cids else "non-playable"
        print(f"  {e['from']}({fp}) -> {e['to']}({tp}) | {fn} -> {tn} | kind={e['kind']} hp={e['hpRecovery']} stock={e['consumeBlastStock']}")

print("\n=== non-revert named edges vs 164 pages (dropped-by-collision check) ===")
nonrev = [t for t in transforms if t["kind"] != "revert" and t.get("toName") and t.get("fromName")]
print(f"non-revert named parsed edges: {len(nonrev)}")

def slugify(s):
    s = s.lower(); s = re.sub(r"['’!.]", "", s); s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

tr_used = set(); assigned = {}; dropped = []
for t in transforms:
    if t["kind"] == "revert" or not t.get("toName") or not t.get("fromName"):
        continue
    s = slugify(f"{t['fromName']}-to-{t['toName']}")
    if s in tr_used:
        s2 = f"{s}-{t['kind']}"
        if s2 in tr_used:
            dropped.append((t["from"], t["to"], t["fromName"], t["toName"], s))
            continue
        s = s2
    tr_used.add(s); assigned[s] = t
print(f"assigned slugs: {len(assigned)}  dropped (double-collision): {len(dropped)}")
for d in dropped:
    print(f"  DROPPED {d}")
pages = {f.stem for f in (CONTENT / "transformations").glob("*.md")}
print(f"slugs assigned but no page: {sorted(set(assigned)-pages)}")
print(f"pages with no assigned slug: {sorted(pages-set(assigned))}")

print("\n=== INDEPENDENT HP-delta recompute (all transforms with HP change) ===")
groups = defaultdict(list)
for cid, c in chars.items():
    groups[c.get("baseId")].append(c)
def rhp(c):
    if c.get("hp") is not None:
        return c["hp"]
    for sib in groups.get(c.get("baseId"), []):
        if sib.get("hp") is not None:
            return sib["hp"]
    return None
cnt = 0
for t in transforms:
    if t["kind"] == "revert":
        continue
    a, b = rhp(chars.get(t["from"], {})), rhp(chars.get(t["to"], {}))
    if a is not None and b is not None and a != b:
        cnt += 1
        print(f"  {t['fromName']} -> {t['toName']}: HP {int(a):,} -> {int(b):,} (delta {int(b-a):+,})")
print(f"total transforms with HP delta: {cnt}")
