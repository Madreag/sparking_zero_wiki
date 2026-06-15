#!/usr/bin/env python3
"""Verify DLC character DP == enrichment/characters.json dp (via content charId)."""
import json, yaml
from pathlib import Path
R = Path(r"c:\vaults\sparking_zero")

def fm(p):
    t = p.read_text(encoding="utf-8")
    return yaml.safe_load(t[3:t.find("\n---", 3)])

# slug -> (charId, content_dp)
cc = {}
for p in (R/"content/characters").glob("*.md"):
    f = fm(p); cc[f.get("slug")] = (f.get("charId"), f.get("dp"))

enr = json.loads((R/"data-mined/enrichment/characters.json").read_text(encoding="utf-8"))

print("DLC | char-slug | DLC.dp | content.dp | charId | enrichment.dp | verdict")
bad = 0
for p in sorted((R/"content/dlc").glob("*.md")):
    f = fm(p)
    if f.get("upcoming"): continue
    for c in f.get("characters", []):
        slug = c.get("slug"); dlcdp = c.get("dp")
        cid, cdp = cc.get(slug, (None, None))
        edp = enr.get(cid, {}).get("dp") if cid else None
        ok = (dlcdp == cdp == edp)
        if not ok: bad += 1
        print("  %-24s %-42s %-4s %-4s %-9s %-4s %s" % (
            f["slug"], slug, dlcdp, cdp, cid, edp,
            "OK" if ok else "*** MISMATCH ***"))
print("\nMISMATCHES:", bad)
