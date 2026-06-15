#!/usr/bin/env python3
"""Comprehensive slug-collision check for game-mode (and other in-scope) slugs
across ALL collections, honoring the resolution priority order."""
import yaml
from pathlib import Path
R = Path(r"c:\vaults\sparking_zero")

ORDER = ["characters","skills","blasts","transformations","mechanics","game-modes",
         "episode-battles","patches","dlc","guides","stages","glossary","shop"]

def fm(p):
    t = p.read_text(encoding="utf-8")
    try: return yaml.safe_load(t[3:t.find("\n---", 3)])
    except Exception: return None

slug_to_colls = {}
for coll in ORDER:
    d = R/"content"/coll
    if not d.exists(): continue
    for p in d.glob("*.md"):
        f = fm(p)
        if not f: continue
        s = f.get("slug")
        if s: slug_to_colls.setdefault(s, []).append(coll)

print("ALL cross-collection slug collisions:")
any_c=False
for s,colls in sorted(slug_to_colls.items()):
    if len(colls)>1:
        any_c=True
        winner = min(colls, key=lambda c: ORDER.index(c))
        print("  '%s' in %s  -> wikilinks resolve to '%s'" % (s, colls, winner))
if not any_c: print("  none")

# focus: do my 4 in-scope collections' slugs get shadowed by higher-priority collections?
print("\nIn-scope slugs shadowed by a higher-priority collection:")
for coll in ["game-modes","episode-battles","patches","dlc"]:
    for p in (R/"content"/coll).glob("*.md"):
        f=fm(p)
        if not f: continue
        s=f.get("slug")
        colls=slug_to_colls.get(s,[])
        if len(colls)>1:
            winner=min(colls, key=lambda c: ORDER.index(c))
            if winner!=coll:
                print("  %-16s slug '%s' SHADOWED by %s" % (coll, s, winner))
print("done")
