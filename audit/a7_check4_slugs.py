"""Check 4: missing link slugs in structured frontmatter/body.

(a) characters transformsTo[] missing targetSlug -> renders href="#" (dead anchor)
(b) blasts users[] missing characterSlug        -> renders plain text (unlinked)
(c) skills body-table users missing slug        -> renders plain text (unlinked)
"""
from __future__ import annotations

import re
from collections import defaultdict

from a7_lib import iter_files, load_fm

# (a) transformsTo missing targetSlug
tt_missing = []          # (char, target)
tt_total = 0
char_slugs = {f.stem for f in iter_files("characters")}
for f in iter_files("characters"):
    fm = load_fm(f)
    for t in fm.get("transformsTo") or []:
        if not isinstance(t, dict):
            continue
        tt_total += 1
        ts = t.get("targetSlug")
        if not ts:
            tt_missing.append((f.stem, t.get("target")))
print(f"=== (a) transformsTo entries: {tt_total}; missing targetSlug (href='#'): {len(tt_missing)}")
for char, tgt in tt_missing[:40]:
    print(f"   {char}: target={tgt!r} (no targetSlug -> '#')")

# also: targetSlug present but points to a non-existent character page
tt_dead = []
for f in iter_files("characters"):
    fm = load_fm(f)
    for t in fm.get("transformsTo") or []:
        if isinstance(t, dict) and t.get("targetSlug") and t["targetSlug"] not in char_slugs:
            tt_dead.append((f.stem, t["targetSlug"]))
print(f"=== (a2) transformsTo targetSlug pointing to MISSING character page: {len(tt_dead)}")
for char, ts in tt_dead[:30]:
    print(f"   {char}: targetSlug={ts!r} -> /characters/{ts} (MISSING)")

# (b) blasts users missing characterSlug
bu_missing = defaultdict(list)
bu_total = 0
bu_dead = []   # characterSlug present but page missing
for f in iter_files("blasts"):
    fm = load_fm(f)
    for u in fm.get("users") or []:
        if not isinstance(u, dict):
            continue
        bu_total += 1
        cs = u.get("characterSlug")
        if not cs:
            bu_missing[f.stem].append(u.get("character"))
        elif cs not in char_slugs:
            bu_dead.append((f.stem, u.get("character"), cs))
print(f"\n=== (b) blast user rows: {bu_total}; missing characterSlug (unlinked): "
      f"{sum(len(v) for v in bu_missing.values())} across {len(bu_missing)} blast pages")
for page, chars in list(bu_missing.items())[:30]:
    print(f"   blasts/{page}: {chars}")
print(f"=== (b2) blast user characterSlug pointing to MISSING character page: {len(bu_dead)}")
for page, ch, cs in bu_dead[:30]:
    print(f"   blasts/{page}: {ch!r} -> /characters/{cs} (MISSING)")

# (c) skills body-table users with plain text (no [[...]]) -> unlinked user
sk_plain = defaultdict(list)
row_re = re.compile(r"^\|\s*([^|]+?)\s*\|\s*(?:—|\d|-).*\|\s*.*\|\s*$")
for f in iter_files("skills"):
    text = f.read_text(encoding="utf-8")
    in_users = False
    for line in text.splitlines():
        if line.startswith("| Character | Cost"):
            in_users = True
            continue
        if in_users:
            if not line.startswith("|"):
                in_users = False
                continue
            if line.startswith("|---") or line.startswith("| ---"):
                continue
            cell = line.split("|")[1].strip() if "|" in line else ""
            if cell and "[[" not in cell and cell != "Character":
                sk_plain[f.stem].append(cell)
print(f"\n=== (c) skill body-table user rows with NO wikilink (plain, unlinked): "
      f"{sum(len(v) for v in sk_plain.values())} across {len(sk_plain)} skill pages")
for page, chars in list(sk_plain.items())[:20]:
    print(f"   skills/{page}: {chars[:6]}")
