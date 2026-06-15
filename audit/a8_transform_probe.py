"""READ-ONLY probe: transformation slug-collision drops + dead stat-delta fields."""
import json
import re
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
CONTENT = ROOT / "content"

transforms = json.load(open(DM / "transformations.json", encoding="utf-8"))
chars = json.load(open(DM / "characters.json", encoding="utf-8"))


def slugify(s):
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


print("=" * 70)
print("A. transformation page generation: collisions & silent drops")
print("=" * 70)
tr_used = set()
emitted = 0
dropped_double = []
skipped_norevert = 0
for t in transforms:
    if t["kind"] == "revert" or not t.get("toName") or not t.get("fromName"):
        skipped_norevert += 1
        continue
    s = slugify(f"{t['fromName']}-to-{t['toName']}")
    if s in tr_used:
        s2 = f"{s}-{t['kind']}"
        if s2 in tr_used:
            dropped_double.append((t["from"], t["to"], t["fromName"], t["toName"], t["kind"], s))
            continue
        s = s2
    tr_used.add(s)
    emitted += 1
print(f"edges total={len(transforms)} ; skipped(revert/missing name)={skipped_norevert}")
print(f"emitted pages={emitted} ; SILENTLY DROPPED on double slug-collision={len(dropped_double)}")
for fr, to, frn, ton, k, s in dropped_double:
    print(f"   DROPPED {fr}->{to}  {frn!r} -> {ton!r}  kind={k}  slug={s!r}")

actual = len(list((CONTENT / "transformations").glob("*.md")))
print(f"actual transformation .md files on disk = {actual}")

print()
print("=" * 70)
print("B. dead stat-delta fields in gen_content (wrong key names)")
print("=" * 70)
# gen_content delta_row uses these source keys:
USED = ["kiChargeSpeed", "kiAutoRecovery", "sparkingGaugeChargeSpeed",
        "preSparkingGaugeDecreaseSpeed"]
allkeys = set()
for c in chars.values():
    allkeys.update(c.keys())
for k in USED:
    print(f"   delta_row source key {k!r}: present in characters.json? {k in allkeys}")
print("   (sparkingDrainPerSec present?:", "sparkingDrainPerSec" in allkeys, ")")

# verify NO transformation page ever shows those two rows
hits_scz = hits_psd = 0
for f in (CONTENT / "transformations").glob("*.md"):
    txt = f.read_text(encoding="utf-8")
    if "Sparking gauge charge" in txt:
        hits_scz += 1
    if "Pre-Sparking gauge decay" in txt:
        hits_psd += 1
print(f"   transformation pages showing 'Sparking gauge charge' row: {hits_scz}")
print(f"   transformation pages showing 'Pre-Sparking gauge decay' row: {hits_psd}")
