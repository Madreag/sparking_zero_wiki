"""Check 3: moveset move-link target existence + slugify/normalizeSlug divergence.

(a) For every character's blast1/blast2/ultimate move, compute the implied move-page slug
    with the EXACT app/characters/[slug]/page.tsx slugifyName (which equals gen_content.py
    slugify) and verify the /blasts or /skills target file exists.
(b) Show where gen slugify() and TS normalizeSlug() DISAGREE (apostrophes/punctuation) and
    whether any actual wikilink relies on the display-name form (latent break).
"""
from __future__ import annotations

import re
from collections import defaultdict

from a7_lib import (CONTENT, build_index, collection_items, iter_files,
                    load_fm, normalize_slug, WIKILINK_RE)


def slugify(s: str) -> str:
    """gen_content.py slugify == app/characters/[slug]/page.tsx slugifyName."""
    s = s.lower()
    s = re.sub(r"['\u2019!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


blast_slugs = {f.stem for f in iter_files("blasts")}
skill_slugs = {f.stem for f in iter_files("skills")}

dead = []          # (char_slug, move_name, type, target_href)
total_moves = 0
by_type = defaultdict(int)
for f in iter_files("characters"):
    fm = load_fm(f)
    for mv in fm.get("moveset") or []:
        if not isinstance(mv, dict):
            continue
        typ = mv.get("type")
        name = mv.get("name")
        if typ not in ("blast1", "blast2", "ultimate") or not name:
            continue
        total_moves += 1
        by_type[typ] += 1
        s = slugify(str(name))
        if typ == "blast2":
            target, coll, ok = f"{s}-super", "blasts", f"{s}-super" in blast_slugs
        elif typ == "ultimate":
            target, coll, ok = f"{s}-ultimate", "blasts", f"{s}-ultimate" in blast_slugs
        else:
            target, coll, ok = s, "skills", s in skill_slugs
        if not ok:
            dead.append((f.stem, str(name), typ, f"/{coll}/{target}"))

print(f"=== moveset move-links checked: {total_moves}  by type: {dict(by_type)}")
print(f"=== DEAD moveset move-links (target page missing): {len(dead)}")
for char_slug, name, typ, href in dead[:60]:
    print(f"  {char_slug}: [{typ}] {name!r} -> {href} (MISSING)")
if len(dead) > 60:
    print(f"  ... and {len(dead) - 60} more")

# ---- (b) slugify vs normalizeSlug divergence ----
print("\n=== slugify() vs normalizeSlug() divergence on page display names ===")
idx, owners, aliases = build_index()
diverge = []
for coll in ["characters", "skills", "blasts", "transformations", "mechanics",
             "game-modes", "episode-battles", "dlc", "guides", "stages"]:
    for it in collection_items(coll):
        label = it["label"]
        if not label:
            continue
        nz = normalize_slug(label)
        sg = slugify(label)
        if nz != sg and sg == it["slug"]:
            # wikilinking by display name would fail (normalizeSlug keeps punctuation)
            diverge.append((coll, it["slug"], label, nz))
print(f"page names whose [[Display Name]] would NOT resolve (slug uses slugify, not normalizeSlug): {len(diverge)}")
for coll, slug, label, nz in diverge[:25]:
    print(f"  {coll}/{slug}: name={label!r}  normalizeSlug->{nz!r}  (no such key)")

# does any ACTUAL wikilink rely on the divergence (target has punctuation slugify strips)?
latent = []
for f in sorted(CONTENT.rglob("*.md")):
    rel = str(f.relative_to(CONTENT)).replace("\\", "/")
    for i, line in enumerate(f.read_text(encoding="utf-8").splitlines(), 1):
        for m in WIKILINK_RE.finditer(line):
            tgt = m.group(1).rstrip("\\")
            nz = normalize_slug(tgt)
            sg = slugify(tgt)
            if nz != sg and nz not in idx and sg in idx:
                latent.append((rel, i, tgt, sg))
print(f"\nactual wikilinks broken by divergence (normalizeSlug fails, slugify would hit): {len(latent)}")
for rel, i, tgt, sg in latent[:20]:
    print(f"  {rel}:{i}  [[{tgt}]] -> normalizeSlug miss; slugify would be {sg!r}")
