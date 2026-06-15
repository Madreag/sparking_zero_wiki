"""Audit Agent 1 — verify hard NUMBERS embedded in S/W/summary/playstyle text
match the fighter's own frontmatter stats (catch copy-paste numeric errors)."""
from __future__ import annotations
import json, glob, os, re
import yaml
from collections import Counter

FM = re.compile(r"^---\n(.*?)\n---", re.S)
pages = {}
for p in glob.glob(r"content/characters/*.md"):
    fm = yaml.safe_load(FM.match(open(p, encoding="utf-8").read()).group(1))
    pages[os.path.splitext(os.path.basename(p))[0]] = fm

def norm(v):
    if isinstance(v, float) and v.is_integer(): return int(v)
    return v

# claim patterns: (regex, frontmatter field, expected-value extractor)
def textblob(fm):
    return " ".join([str(fm.get("playstyle") or ""), str(fm.get("howToFight") or ""),
                     str(fm.get("summary") or "")] + list(fm.get("strengths") or []) + list(fm.get("weaknesses") or []))

mismatches = []
# recovery claims: "1,750 recovery", "1,500 ki recovery", "1,500/s recovery", "2,250 recovery"
rec_re = re.compile(r"([12],[0-9]{3})\s*(?:/s)?\s*(?:ki )?recovery", re.I)
chg_re = re.compile(r"([0-9]{1,2}(?:\.[0-9])?)\s*(?:ki )?charge", re.I)
hp_re  = re.compile(r"([3-4][05],000)\s*HP", re.I)

stat_claim_counter = Counter()
for slug, fm in pages.items():
    if not fm.get("playable"): continue
    blob = textblob(fm)
    rec = norm(fm.get("kiAutoRecovery"))
    chg = norm(fm.get("kiChargeSpeed"))
    hp  = norm(fm.get("hp"))
    for mt in rec_re.finditer(blob):
        claim = int(mt.group(1).replace(",", "")); stat_claim_counter["recovery"] += 1
        if rec is not None and claim != rec:
            mismatches.append((slug, "kiAutoRecovery", claim, rec, mt.group(0)))
    for mt in chg_re.finditer(blob):
        # avoid matching "charge" without a number context like "ki charge speed"
        claim = float(mt.group(1)); stat_claim_counter["charge"] += 1
        if chg is not None and abs(claim - chg) > 1e-9:
            # only flag if claim looks like a charge-speed value (<=12)
            if claim <= 12:
                mismatches.append((slug, "kiChargeSpeed", claim, chg, mt.group(0)))
    for mt in hp_re.finditer(blob):
        claim = int(mt.group(1).replace(",", "")); stat_claim_counter["hp"] += 1
        if hp is not None and claim != hp:
            mismatches.append((slug, "hp", claim, hp, mt.group(0)))

print("stat-claim occurrences scanned:", dict(stat_claim_counter))
print(f"NUMERIC STAT-CLAIM MISMATCHES vs own frontmatter: {len(mismatches)}")
for slug, field, claim, actual, frag in mismatches:
    print(f"  {slug}: text says {frag!r} ({claim}) but {field}={actual}")

# DP claims in text: "DP4", "DP6 with", "DP8 —"
dp_re = re.compile(r"\bDP\s?([0-9]{1,2})\b")
dpm = []
for slug, fm in pages.items():
    if not fm.get("playable"): continue
    dp = fm.get("dp")
    for mt in dp_re.finditer(textblob(fm)):
        claim = int(mt.group(1))
        if dp is not None and claim != dp:
            dpm.append((slug, claim, dp, mt.group(0)))
print(f"\nDP TEXT-vs-FRONTMATTER mismatches: {len(dpm)}")
for slug, claim, dp, frag in dpm[:40]:
    print(f"  {slug}: text {frag!r} but dp={dp}")
