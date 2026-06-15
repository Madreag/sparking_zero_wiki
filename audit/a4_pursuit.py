"""Check the datamined distribution of PursuitLimitLightningAttack in Numeric.json."""
import json, re, collections, os
ROOT = r"c:\vaults\sparking_zero"
p = os.path.join(ROOT, "data-mined", "raw", "masterdata", "Numeric.json")
txt = open(p, encoding="utf-8").read()
vals = collections.Counter(int(m) for m in re.findall(r'"PursuitLimitLightningAttack":\s*(-?\d+)', txt))
print("PursuitLimitLightningAttack value distribution:", dict(vals))
valsadd = collections.Counter(int(m) for m in re.findall(r'"PursuitLimitLightningAttackAddAtSparking":\s*(-?\d+)', txt))
print("PursuitLimitLightningAttackAddAtSparking distribution:", dict(valsadd))
# any 6 anywhere near Pursuit?
for m in re.finditer(r'"(\w*Pursuit\w*)":\s*(-?\d+(?:\.\d+)?)', txt):
    pass
keys = collections.Counter(re.findall(r'"(\w*Pursuit\w*)":', txt))
print("all Pursuit* keys:", dict(keys))
# show one full sample value set for the 6 question
for m in re.finditer(r'"PursuitLimitLightningAttack":\s*(-?\d+)', txt):
    pass
