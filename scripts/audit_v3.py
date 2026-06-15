"""Audit v3: deep checks — rendered artifacts, slug collisions, link drift, data sanity."""

import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"
BUILT = ROOT / ".next" / "server" / "app"

issues: list[str] = []


def issue(msg: str):
    issues.append(msg)
    print("ISSUE:", msg)


def fm_of(f: Path) -> str:
    parts = f.read_text(encoding="utf-8").split("---")
    return parts[1] if len(parts) >= 3 else ""


coll_slugs: dict[str, set] = defaultdict(set)
for d in CONTENT.iterdir():
    if d.is_dir():
        for f in d.glob("*.md"):
            coll_slugs[d.name].add(f.stem)

# A. cross-collection slug collisions (wikilink ambiguity)
owner: dict[str, list] = defaultdict(list)
for coll, slugs in coll_slugs.items():
    for s in slugs:
        owner[s].append(coll)
# resolution priority in content.ts getSlugIndex (first added wins):
PRIORITY = ["characters", "skills", "blasts", "transformations", "mechanics",
            "game-modes", "episode-battles", "patches", "dlc", "guides",
            "stages", "shop", "glossary"]
OK_PAIRS = {("glossary", "mechanics"), ("game-modes", "stages"),
            ("characters", "dlc"), ("game-modes", "mechanics"),
            ("glossary", "skills"), ("game-modes", "glossary")}
collisions = {s: cs for s, cs in owner.items() if len(cs) > 1}
unexpected = 0
for s, cs in sorted(collisions.items()):
    pair = tuple(sorted(cs))
    winner = min(cs, key=lambda c: PRIORITY.index(c))
    if pair not in OK_PAIRS:
        unexpected += 1
        issue(f"unexpected slug collision '{s}' in {cs} -> resolves to {winner}")
print(f"=== slug collisions: {len(collisions)} total, {unexpected} unexpected (rest resolve by design)")


# B. python-vs-TS slugify drift for moveset links (character page moveHref)
def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


dead_move_links = Counter()
for f in (CONTENT / "characters").glob("*.md"):
    fm = fm_of(f)
    for m in re.finditer(
        r'- name: "([^"]+)"\n    type: "(blast1|blast2|ultimate)"', fm
    ):
        name, typ = m.group(1), m.group(2)
        target = (
            f"{slugify(name)}-super"
            if typ == "blast2"
            else f"{slugify(name)}-ultimate"
            if typ == "ultimate"
            else slugify(name)
        )
        coll = "skills" if typ == "blast1" else "blasts"
        if target not in coll_slugs[coll]:
            dead_move_links[(f.stem, target, coll)] += 1
if dead_move_links:
    for (page, target, coll), _ in list(dead_move_links.items())[:10]:
        issue(f"dead moveset link on {page}: /{coll}/{target}")
    if len(dead_move_links) > 10:
        issue(f"...and {len(dead_move_links) - 10} more dead moveset links")

# C. transformsTo without targetSlug (renders href='#')
no_slug = 0
for f in (CONTENT / "characters").glob("*.md"):
    fm = fm_of(f)
    for m in re.finditer(r'- target: "[^"]+"\n(?!    targetSlug)', fm):
        no_slug += 1
if no_slug:
    issue(f"{no_slug} transformsTo entries missing targetSlug (render as '#')")

# D. data sanity
for f in (CONTENT / "characters").glob("*.md"):
    fm = fm_of(f)
    dp = re.search(r"^dp: (\d+)", fm, re.M)
    if dp and not (1 <= int(dp.group(1)) <= 10):
        issue(f"dp out of range on {f.stem}: {dp.group(1)}")
    hp = re.search(r"^hp: (\d+)", fm, re.M)
    if hp and int(hp.group(1)) not in (30000, 35000, 40000, 45000):
        issue(f"unexpected hp on {f.stem}: {hp.group(1)}")
    for m in re.finditer(r"kiCost: (\d+)", fm):
        v = int(m.group(1))
        if not (1000 <= v <= 60000):
            issue(f"suspicious kiCost on {f.stem}: {v}")

# E. summary coverage on playable
miss_sum = [
    f.stem
    for f in (CONTENT / "characters").glob("*.md")
    if "playable: true" in fm_of(f) and "summary:" not in fm_of(f)
]
if miss_sum:
    issue(f"{len(miss_sum)} playable chars without summary: {miss_sum[:5]}")

# F. episode battleCount vs battles[] length
for f in (CONTENT / "episode-battles").glob("*.md"):
    fm = fm_of(f)
    bc = re.search(r"^battleCount: (\d+)", fm, re.M)
    n = len(re.findall(r'^  - id: "', fm, re.M))
    if bc and int(bc.group(1)) != n:
        issue(f"battleCount mismatch {f.stem}: front={bc.group(1)} entries={n}")

# G. patches order uniqueness
orders = Counter()
for f in (CONTENT / "patches").glob("*.md"):
    m = re.search(r"^order: (\d+)", fm_of(f), re.M)
    if m:
        orders[m.group(1)] += 1
for o, c in orders.items():
    if c > 1:
        issue(f"duplicate patch order {o} x{c}")

# H. rendered-output artifact scan (built HTML)
if BUILT.exists():
    pats = {
        "[[": re.compile(r"\[\[(?!\d)"),  # unresolved wikilinks leaking
        "\\|": re.compile(r"\\\|"),
        "undefined": re.compile(r">undefined<"),
        "NaN": re.compile(r">NaN<"),
        "object Object": re.compile(r"\[object Object\]"),
        "(N)": None,  # info only
    }
    counts = Counter()
    sample = {}
    for f in BUILT.rglob("*.html"):
        t = f.read_text(encoding="utf-8", errors="ignore")
        t = re.sub(r"<script[\s\S]*?</script>", "", t)
        for label, rx in pats.items():
            if rx is None:
                continue
            if rx.search(t):
                counts[label] += 1
                sample.setdefault(label, str(f.relative_to(BUILT))[:70])
    for label, c in counts.items():
        issue(f"rendered artifact {label!r} in {c} built pages e.g. {sample[label]}")
else:
    print("note: no .next build output to scan")

# I. skills userCount consistency
for f in (CONTENT / "skills").glob("*.md"):
    fm = fm_of(f)
    uc = re.search(r"^userCount: (\d+)", fm, re.M)
    n = (
        len(re.findall(r"^users:\n((?:  - .*\n)+)", fm, re.M)[0].splitlines())
        if re.search(r"^users:", fm, re.M)
        else 0
    )
    if uc and n and int(uc.group(1)) != n:
        issue(f"userCount mismatch {f.stem}: {uc.group(1)} vs {n}")

# J. blasts: users without characterSlug (unlinked users)
unlinked = 0
for f in (CONTENT / "blasts").glob("*.md"):
    fm = fm_of(f)
    unlinked += len(re.findall(r'- character: "[^"]+"\n(?!    characterSlug)', fm))
if unlinked:
    issue(f"{unlinked} blast users without characterSlug (unlinked)")

print(
    f"\n==== AUDIT v3 {'CLEAN' if not issues else f'FOUND {len(issues)} ISSUES'} ===="
)
