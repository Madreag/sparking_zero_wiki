"""READ-ONLY probe (Audit Agent 8): quantify slugify (gen_content.py) vs
normalizeSlug (lib/content.ts) drift and its impact on [[wikilink]] reachability.

Does NOT mutate anything. Reads content/*.md frontmatter + glossary aliases,
rebuilds the TS slug index (priority/first-wins), and reports:
  1. pages whose display name does NOT round-trip through normalizeSlug to its
     own file slug (un-reachable by a naive [[Display Name]] link)
  2. per-character/blast/etc names where slugify(name) != normalizeSlug(name)
  3. actual [[wikilinks]] present in content that fail normalizeSlug resolution
"""
from __future__ import annotations

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"


# ---- replicate the two slug functions EXACTLY ----
def slugify_gen(s: str) -> str:
    """gen_content.py slugify"""
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def normalize_slug_ts(s: str) -> str:
    """lib/content.ts normalizeSlug: trim + lower + \\s+ -> '-' (strips NOTHING else)"""
    return re.sub(r"\s+", "-", s.strip().lower())


# priority order used by getSlugIndex (first-wins)
PRIORITY = [
    "characters", "skills", "blasts", "transformations", "mechanics",
    "game-modes", "episode-battles", "patches", "dlc", "guides",
    "stages", "shop", "glossary",
]
DISPLAY_FIELD = defaultdict(lambda: "name", {
    "patches": "version", "guides": "title", "glossary": "term",
})


def grab(fm: str, field: str) -> str | None:
    m = re.search(rf'^{field}:\s*(.+?)\s*$', fm, re.M)
    if not m:
        return None
    v = m.group(1).strip()
    if len(v) >= 2 and v[0] in "\"'" and v[-1] == v[0]:
        v = v[1:-1]
    return v


def get_aliases(fm: str) -> list[str]:
    m = re.search(r'^aliases:\s*$((?:\n[ \t]+-.*)+)', fm, re.M)
    if not m:
        # inline form aliases: ["a","b"]
        m2 = re.search(r'^aliases:\s*\[(.*)\]', fm, re.M)
        if m2:
            return [x.strip().strip('"\'') for x in m2.group(1).split(",") if x.strip()]
        return []
    out = []
    for line in m.group(1).splitlines():
        line = line.strip()
        if line.startswith("-"):
            out.append(line[1:].strip().strip('"\''))
    return out


# ---- collect pages ----
pages = []  # (coll, slug, display_name)
slug_owner: dict[str, str] = {}   # slug -> coll (first by priority)
index_keys: dict[str, tuple[str, str]] = {}  # normalizeSlug key -> (href-ish coll, slug)

coll_files: dict[str, list[Path]] = defaultdict(list)
for d in sorted(CONTENT.iterdir()):
    if d.is_dir():
        for f in sorted(d.glob("*.md")):
            coll_files[d.name].append(f)

# build index in priority order (first-wins), matching getSlugIndex
glossary_alias_keys: dict[str, str] = {}
for coll in PRIORITY:
    for f in coll_files.get(coll, []):
        slug = f.stem
        parts = f.read_text(encoding="utf-8").split("---")
        fm = parts[1] if len(parts) >= 3 else ""
        name = grab(fm, DISPLAY_FIELD[coll]) or slug
        pages.append((coll, slug, name))
        if slug not in slug_owner:
            slug_owner[slug] = coll
            index_keys[slug] = (coll, slug)
        if coll == "glossary":
            for a in get_aliases(fm):
                k = normalize_slug_ts(a)
                index_keys.setdefault(k, (coll, slug))

print(f"=== pages scanned: {len(pages)} across {len(coll_files)} collections")
print("    per-collection:", {k: len(v) for k, v in sorted(coll_files.items())})

# ---- 1. reachability by naive [[Display Name]] ----
unreachable = []        # normalizeSlug(name) not a key at all
wrong_target = []       # resolves, but to a different slug (collision/shape)
reachable = 0
for coll, slug, name in pages:
    key = normalize_slug_ts(name)
    hit = index_keys.get(key)
    if hit is None:
        unreachable.append((coll, slug, name, key))
    elif hit[1] != slug:
        wrong_target.append((coll, slug, name, key, hit))
    else:
        reachable += 1

print(f"\n=== [[Display Name]] reachability over {len(pages)} pages")
print(f"    reachable (normalizeSlug(name)==own slug): {reachable}")
print(f"    UNREACHABLE (no index key):                {len(unreachable)}")
print(f"    resolves to WRONG page:                    {len(wrong_target)}")

by_coll = Counter(c for c, *_ in unreachable)
print("    unreachable by collection:", dict(by_coll))

# ---- 2. slugify(name) vs normalizeSlug(name) divergence, by char class ----
def reasons(name: str) -> list[str]:
    r = []
    if re.search(r"['’]", name): r.append("apostrophe")
    if "!" in name: r.append("bang")
    if "." in name: r.append("period")
    if re.search(r"[()]", name): r.append("parens")
    if ":" in name: r.append("colon")
    if "," in name: r.append("comma")
    if "&" in name: r.append("ampersand")
    if "/" in name: r.append("slash")
    if re.search(r"[^\x00-\x7f]", name): r.append("non-ascii")
    return r or ["other"]

diverge = []
for coll, slug, name in pages:
    g, n = slugify_gen(name), normalize_slug_ts(name)
    if g != n:
        diverge.append((coll, slug, name, g, n, reasons(name)))

reason_ct = Counter(r for *_, rs in diverge for r in rs)
print(f"\n=== slugify(name) != normalizeSlug(name): {len(diverge)} pages")
print("    reason tally:", dict(reason_ct.most_common()))

# show concrete examples grouped by reason, focusing on the punctuation classes
print("\n--- concrete drift examples (gen file-slug  vs  normalizeSlug(name)) ---")
shown = defaultdict(int)
for coll, slug, name, g, n, rs in diverge:
    key_r = rs[0]
    if shown[key_r] >= 6:
        continue
    shown[key_r] += 1
    flag = "" if g == slug else "  [NOTE gen!=stem]"
    print(f"  [{','.join(rs):<22}] {coll:<10} {name!r}\n       gen/file = {g!r}{flag}\n       normSlug = {n!r}")

# ---- 3. real [[wikilinks]] in content that fail to resolve ----
wl = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
broken_links = Counter()
broken_examples: dict[str, str] = {}
total_wl = 0
for f in CONTENT.rglob("*.md"):
    txt = f.read_text(encoding="utf-8")
    for m in wl.finditer(txt):
        target = m.group(1)
        total_wl += 1
        key = normalize_slug_ts(target)
        if key not in index_keys:
            broken_links[target] += 1
            broken_examples.setdefault(target, str(f.relative_to(CONTENT)))

print(f"\n=== real [[wikilinks]]: {total_wl} total, {sum(broken_links.values())} fail normalizeSlug resolution")
for tgt, c in broken_links.most_common(25):
    print(f"  BROKEN [[{tgt}]] x{c}  e.g. {broken_examples[tgt]}  (normSlug={normalize_slug_ts(tgt)!r})")

# ---- 4. specifically: names with chars slugify strips, listing affected slugs ----
print("\n=== character/blast/skill/transformation names containing apostrophe/é/!/&/: ===")
for coll in ("characters", "blasts", "skills", "transformations"):
    hits = [(slug, name) for c, slug, name in pages if c == coll and re.search(r"['’!&:éūō.]", name)]
    if hits:
        print(f"  {coll}: {len(hits)} names")
        for slug, name in hits[:12]:
            print(f"     {name!r:50} -> file {slug!r} ; [[name]]->{normalize_slug_ts(name)!r}")
