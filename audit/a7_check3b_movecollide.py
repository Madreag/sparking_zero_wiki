"""Check 3b: do DISTINCT move names collide onto the same blast/skill page?

gen_content.py drops a blast whose `{slugify(name)}-{class}` slug already exists
(`if s in bslugs: continue`). If two distinct super/ultimate names slugify identically,
the second character's moveHref silently points to the FIRST blast's page (mis-target,
not a 404). Enumerate such collisions.
"""
from __future__ import annotations

import re
from collections import defaultdict

from a7_lib import iter_files, load_fm


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['\u2019!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


# map move-target-slug -> set of distinct source move names (per type/class)
target_names = defaultdict(set)
target_chars = defaultdict(set)
for f in iter_files("characters"):
    fm = load_fm(f)
    for mv in fm.get("moveset") or []:
        if not isinstance(mv, dict):
            continue
        typ, name = mv.get("type"), mv.get("name")
        if typ not in ("blast1", "blast2", "ultimate") or not name:
            continue
        s = slugify(str(name))
        tgt = {"blast2": f"/blasts/{s}-super",
               "ultimate": f"/blasts/{s}-ultimate",
               "blast1": f"/skills/{s}"}[typ]
        target_names[tgt].add(str(name))
        target_chars[tgt].add(f.stem)

collide = {t: ns for t, ns in target_names.items() if len(ns) > 1}
print(f"=== move-target slugs reached by >1 DISTINCT move name: {len(collide)}")
for tgt, names in sorted(collide.items()):
    print(f"  {tgt}  <-  {sorted(names)}")
    print(f"       chars: {sorted(target_chars[tgt])[:8]}")
