"""READ-ONLY probe (Audit Agent 8): verify parse_data.py against the raw masterdata.

Checks:
  A. Combatives/*.json json.load() failures (the silent `except Exception: continue`)
  B. Numeric field-mapping spot checks (10 cids) vs data-mined/characters.json
  C. CharacterData FormChange/Fusion/Potara ConsumeBlastStock/HpRecovery extraction
  D. revert-heuristic safety (stock==0 & same_base -> 'revert' relabel) — could it drop
     a legit forward transform?
  E. props() robustness: which masterdata values are NOT a non-empty list (entry[0] risk)
"""
from __future__ import annotations

import json
import re
from collections import Counter
from pathlib import Path

RAW = Path(r"C:\vaults\sparking_zero\data-mined\raw")
OUT = Path(r"C:\vaults\sparking_zero\data-mined")
MD = RAW / "masterdata"


def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def props(entry) -> dict:
    if not entry:
        return {}
    return entry[0].get("Properties") or {}


print("=" * 70)
print("A. Combatives json.load() failures")
print("=" * 70)
comb_dir = MD / "Combatives"
fail = []
ok = 0
lost_actions = 0
for f in sorted(comb_dir.glob("*.json")):
    if f.stem == "Common":
        continue
    try:
        d = load(f)
        ok += 1
    except Exception as ex:
        # count how many Power action entries would have been lost
        try:
            txt = f.read_text(encoding="utf-8", errors="ignore")
            n_power = len(re.findall(r'"Power"\s*:', txt))
        except Exception:
            n_power = "?"
        fail.append((f.name, type(ex).__name__, str(ex)[:80], n_power))
        lost_actions += n_power if isinstance(n_power, int) else 0
print(f"Combatives files: {ok} parsed OK, {len(fail)} FAILED to json.load")
for name, et, msg, npw in fail:
    print(f"  FAIL {name}: {et}: {msg}  (~{npw} Power entries lost)")
print(f"  => approx {lost_actions} per-action Power overrides silently dropped")

print()
print("=" * 70)
print("B. Numeric field-mapping spot checks vs characters.json")
print("=" * 70)
chars = load(OUT / "characters.json")
numeric = load(MD / "Numeric.json")
MAP = {
    "hp": "Life",
    "kiChargeSpeed": "SPChargeSpeed",
    "kiAutoRecovery": "SPAutoRecoverySpeed",
    "kiAutoRecoveryLimit": "SPAutoRecoveryLimit",
    "initialKi": "InitialSP",
    "maxSkillStock": "BlastStock",
    "initialSkillStock": "InitialBlastStock",
    "sparkingDrainPerSec": "SparkingModeGaugeDecreaseSpeed",
    "kiBlastShots": "BulletNum",
}
sample = ["0000_00", "0790_00", "0620_00", "0100_02", "0210_00",
          "0141_00", "0450_00", "0931_00", "3040_00", "0180_00"]
mismatches = 0
for cid in sample:
    c = chars.get(cid)
    num = props(numeric.get(f"Numeric_{cid}"))
    if not c:
        print(f"  {cid}: not in characters.json")
        continue
    bad = []
    for jf, rk in MAP.items():
        want = num.get(rk)
        got = c.get(jf)
        if want != got:
            bad.append(f"{jf}: parsed={got!r} raw.{rk}={want!r}")
    name = c.get("name")
    if bad:
        mismatches += 1
        print(f"  MISMATCH {cid} ({name}): " + "; ".join(bad))
    else:
        print(f"  OK {cid} ({name}): hp={c.get('hp')} ki={c.get('kiChargeSpeed')} stock={c.get('maxSkillStock')}")
print(f"  => {mismatches} mismatched cids out of {len(sample)}")

print()
print("=" * 70)
print("C+D. CharacterData edges + revert heuristic")
print("=" * 70)
chardata = load(MD / "CharacterData.json")
transforms = load(OUT / "transformations.json")


def base_of(cid):
    return cid.split("_")[0]


def formcode(cid):
    return cid.split("_")[1]


# recompute the resolved_kind logic and check for suspicious reverts
reverts = [t for t in transforms if t["kind"] == "revert"]
print(f"transformations.json: {len(transforms)} edges, {len(reverts)} labelled 'revert'")
# a 'revert' should go to a LOWER (or equal) formcode of the same base.
suspicious = []
for t in reverts:
    fc_from, fc_to = formcode(t["from"]), formcode(t["to"])
    # forward transform mis-tagged: target formcode strictly higher than source
    if base_of(t["from"]) == base_of(t["to"]) and fc_to > fc_from:
        suspicious.append(t)
print(f"  reverts whose target form-code is HIGHER than source (possible mis-tagged forward): {len(suspicious)}")
for t in suspicious[:15]:
    print(f"    {t['from']} -> {t['to']}  ({t['fromName']} -> {t['toName']})  stock={t['consumeBlastStock']} hpRec={t.get('hpRecovery')}")

# also: transform edges with stock 0 & same base that were NOT reverted (kept as transform)
kept = [t for t in transforms if t["kind"] == "transform" and t.get("consumeBlastStock") == 0
        and base_of(t["from"]) == base_of(t["to"])]
print(f"  transform edges stock==0 & same-base still kept as 'transform': {len(kept)}")

# how many distinct forward transforms have stock 0 (free transforms) total?
free = [t for t in transforms if t.get("consumeBlastStock") == 0]
print(f"  ALL edges with consumeBlastStock==0: {len(free)} (kinds: {Counter(t['kind'] for t in free)})")

# Recompute reverts and show those going to a DIFFERENT base (these should never be 'revert')
cross = [t for t in reverts if base_of(t["from"]) != base_of(t["to"])]
print(f"  'revert' edges crossing base id (should be impossible per heuristic): {len(cross)}")

print()
print("=" * 70)
print("E. props() robustness: masterdata top-level value shapes")
print("=" * 70)
for fname in ["Numeric.json", "CharacterData.json", "BlastSkill.json",
              "BlastUltimate.json", "BlastForte.json", "OperationGuide.json"]:
    try:
        d = load(MD / fname)
    except Exception as ex:
        print(f"  {fname}: load failed {ex}")
        continue
    shapes = Counter()
    empty_list = 0
    for k, v in d.items():
        if isinstance(v, list):
            shapes["list"] += 1
            if len(v) == 0:
                empty_list += 1
        else:
            shapes[type(v).__name__] += 1
    print(f"  {fname}: {dict(shapes)}  empty-lists={empty_list}")

# WishComeTrue: props() is called directly on .get('WishComeTrueContentsDataAsset')
wt = load(MD / "WishComeTrue.json")
v = wt.get("WishComeTrueContentsDataAsset")
print(f"  WishComeTrue['WishComeTrueContentsDataAsset'] type = {type(v).__name__}; "
      f"props() works = {isinstance(v, list) and len(v) > 0}")
