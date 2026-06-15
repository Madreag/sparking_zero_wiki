"""READ-ONLY probe: gender-null crash risk, cooldown '—s', missing-name transform edge."""
import json
import re
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
CONTENT = ROOT / "content"
MD = DM / "raw" / "masterdata"

chardata = json.load(open(MD / "CharacterData.json", encoding="utf-8"))

print("A. StorySettingParameter shape (gender extraction crash risk)")
null_ssp = absent = dict_ssp = 0
for k, v in chardata.items():
    if not isinstance(v, list) or not v:
        continue
    rec = (v[0].get("Properties") or {}).get("CharacterDataAssetRecord") or {}
    if "StorySettingParameter" not in rec:
        absent += 1
    elif rec["StorySettingParameter"] is None:
        null_ssp += 1
    elif isinstance(rec["StorySettingParameter"], dict):
        dict_ssp += 1
print(f"   StorySettingParameter: dict={dict_ssp}, absent={absent}, EXPLICIT NULL={null_ssp}")
print(f"   -> redundant 2nd operand `rec.get('StorySettingParameter',{{}}).get('Gender')` "
      f"crashes iff null present AND 1st operand falsy: risk now = {null_ssp>0}")

print("\nB. transformation body: cooldown '—s' (coolTimeSec None) cosmetic")
dash_s = 0
ex = []
for f in (CONTENT / "transformations").glob("*.md"):
    txt = f.read_text(encoding="utf-8")
    if "| Cooldown | —s |" in txt:
        dash_s += 1
        if len(ex) < 5:
            ex.append(f.stem)
print(f"   pages rendering '| Cooldown | —s |': {dash_s}  e.g. {ex}")

print("\nC. HP-rule 'HP recovery on change: —' (hpRecovery None)")
dash_hp = 0
for f in (CONTENT / "transformations").glob("*.md"):
    if "recovery on change: —" in f.read_text(encoding="utf-8"):
        dash_hp += 1
print(f"   pages with 'HP recovery on change: —': {dash_hp}")

print("\nD. non-revert transform edges dropped for missing from/to name")
transforms = json.load(open(DM / "transformations.json", encoding="utf-8"))
miss = [t for t in transforms if t["kind"] != "revert" and (not t.get("toName") or not t.get("fromName"))]
print(f"   dropped (non-revert, missing name): {len(miss)}")
for t in miss:
    print(f"      {t['from']}({t.get('fromName')!r}) -> {t['to']}({t.get('toName')!r}) kind={t['kind']}")
