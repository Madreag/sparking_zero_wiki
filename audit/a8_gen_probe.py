"""READ-ONLY probe (Audit Agent 8): gen_content.py correctness checks."""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
CONTENT = ROOT / "content"
RAW = DM / "raw" / "masterdata"


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


chars = load(DM / "characters.json")
enrich = load(DM / "enrichment" / "characters.json")
sw_a = load(DM / "enrichment" / "sw_a.json")
sw_b = load(DM / "enrichment" / "sw_b.json")

print("=" * 70)
print("1. playable = bool(merged enrich). enrich entries =", len(enrich))
print("=" * 70)
# replicate the merge: sw_*.json only update cids ALREADY in enrich
merged = {k: dict(v) for k, v in enrich.items()}
sw_total_cids = set(sw_a) | set(sw_b)
dropped_sw = []
for swname, sw in (("sw_a", sw_a), ("sw_b", sw_b)):
    for cid, v in sw.items():
        if cid not in enrich:
            dropped_sw.append((swname, cid, v.get("summary", "")[:50] if isinstance(v, dict) else ""))
print(f"sw_a cids={len(sw_a)}, sw_b cids={len(sw_b)}, union={len(sw_total_cids)}")
print(f"sw_* cids NOT in enrichment/characters.json (S/W SILENTLY DROPPED): {len(dropped_sw)}")
for swname, cid, summ in dropped_sw[:25]:
    nm = chars.get(cid, {}).get("name")
    print(f"   {swname} {cid} ({nm}) dropped: {summ!r}")

# playable:true count in generated content
play_true = 0
play_files = []
for f in (CONTENT / "characters").glob("*.md"):
    fm = f.read_text(encoding="utf-8").split("---")[1]
    if "playable: true" in fm:
        play_true += 1
        play_files.append(f.stem)
print(f"\ncontent characters with playable:true = {play_true}")
# cids in enrich but missing from chars.json (enrichment present for non-existent char)
enrich_not_in_chars = [cid for cid in enrich if cid not in chars]
print(f"enrich cids absent from characters.json: {enrich_not_in_chars}")
# cids in enrich that map to an UNNAMED char (would not get a page even though 'playable')
enrich_unnamed = [cid for cid in enrich if cid in chars and not chars[cid].get("name")]
print(f"enrich cids whose char has no name (no page generated): {enrich_unnamed}")

print()
print("=" * 70)
print("2. search-index title regex vs embedded-quote names")
print("=" * 70)
idx = load(ROOT / "public" / "search-index.json")
by_href = {e["h"]: e for e in idx}
# the blast with embedded quotes
for needle in ["no-hard-feelings-hit", "flash-sign", "kamehameha-sign"]:
    hit = [e for e in idx if e["h"].endswith(needle)]
    for e in hit:
        print(f"   {e['h']}: title t={e['t']!r}")
# how many search entries fell back to slug as title (t looks like a slug)?
slugish = [e for e in idx if re.fullmatch(r"[a-z0-9-]+", e["t"]) and "-" in e["t"]]
print(f"   search entries whose title is slug-like (regex fell back to f.stem?): {len(slugish)}")
for e in slugish[:15]:
    print(f"      {e['h']}  t={e['t']!r}")

print()
print("=" * 70)
print("3. audit_v4 2d coverage: blast1 moves WITH a skillCost line")
print("=" * 70)
with_sc = 0
total_b1 = 0
for f in (CONTENT / "characters").glob("*.md"):
    fm = f.read_text(encoding="utf-8").split("---")[1]
    total_b1 += len(re.findall(r'type: "blast1"', fm))
    with_sc += len(re.findall(r'type: "blast1"\n    skillCost: (\d+)', fm))
print(f"   blast1 moves total={total_b1}, with explicit skillCost line={with_sc}")
print(f"   => audit_v4 skill-cost cross-check exercises {with_sc} of {total_b1} blast1 moves")

print()
print("=" * 70)
print("4. zCounterType extraction: SuperZCounterType null/missing risk")
print("=" * 70)
bs = load(RAW / "BlastSkill.json")
null_szc = 0
present = Counter()
for k, v in bs.items():
    if not isinstance(v, list) or not v:
        continue
    p = v[0].get("Properties") or {}
    pd = p.get("BlastSkillParamData")
    if isinstance(pd, dict):
        if "SuperZCounterType" in pd:
            present[pd["SuperZCounterType"] if pd["SuperZCounterType"] is not None else "<null>"] += 1
            if pd["SuperZCounterType"] is None:
                null_szc += 1
print(f"   BlastSkillParamData with explicit SuperZCounterType=null: {null_szc} (would crash .split)")
print(f"   value tally (top): {present.most_common(6)}")

print()
print("=" * 70)
print("5. duplicate display-name collision pairs (gen slug suffixing)")
print("=" * 70)
name_to_files = {}
for f in (CONTENT / "characters").glob("*.md"):
    raw = f.read_text(encoding="utf-8")
    m = re.search(r'^name: "(.*)"', raw, re.M)
    cidm = re.search(r'^charId: "(.*)"', raw, re.M)
    if m:
        name_to_files.setdefault(m.group(1), []).append((f.stem, cidm.group(1) if cidm else "?"))
for name, files in name_to_files.items():
    if len(files) > 1:
        print(f"   {name!r}: {files}")
