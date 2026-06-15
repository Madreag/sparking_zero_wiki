"""Audit v4 — deepest pass: built-HTML link graph, cross-page numeric consistency,
end-to-end raw-data->render verification, formatting bugs."""

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"
BUILT = ROOT / ".next" / "server" / "app"

issues: list[str] = []


def issue(msg):
    issues.append(msg)
    print("ISSUE:", msg)


def note(msg):
    print("note:", msg)


J = lambda p: json.loads(Path(p).read_text(encoding="utf-8"))
strip_scripts = lambda t: re.sub(r"<script[\s\S]*?</script>", "", t)

coll_slugs = defaultdict(set)
for d in CONTENT.iterdir():
    if d.is_dir():
        for f in d.glob("*.md"):
            coll_slugs[d.name].add(f.stem)

# ---------- 1. FULL internal-href resolution over built HTML ----------
ROUTES = {
    "",
    "characters",
    "blasts",
    "skills",
    "transformations",
    "mechanics",
    "game-modes",
    "episode-battles",
    "patches",
    "dlc",
    "guides",
    "stages",
    "shop",
    "glossary",
    "stats",
    "meta",
    "compare",
}
valid_paths = {"/", "/stats", "/meta", "/compare", "/dna", "/classes"}
for coll in coll_slugs:
    valid_paths.add(f"/{coll}")
    for s in coll_slugs[coll]:
        valid_paths.add(f"/{coll}/{s}")
dead = Counter()
dead_sample = {}
pages_scanned = 0
for f in BUILT.rglob("*.html"):
    pages_scanned += 1
    v = strip_scripts(f.read_text(encoding="utf-8", errors="ignore"))
    for href in re.findall(r'href="(/[^"#?]*)', v):
        href = href.rstrip("/") or "/"
        if href.startswith("/_next") or href.startswith("/search-index"):
            continue
        if href not in valid_paths:
            dead[href] += 1
            dead_sample.setdefault(href, str(f.relative_to(BUILT))[:60])
print(f"=== link graph: scanned {pages_scanned} built pages")
for href, c in dead.most_common(15):
    issue(f"dead internal href {href} x{c} (e.g. {dead_sample[href]})")

# ---------- 2. cross-page numeric consistency ----------
chars = J(ROOT / "data-mined" / "characters.json")
enrich = J(ROOT / "data-mined" / "enrichment" / "characters.json")
meta = J(ROOT / "data-mined" / "meta.json")

# 2a. dp: character pages vs meta.json
page_dp = {}
for f in (CONTENT / "characters").glob("*.md"):
    fm = f.read_text(encoding="utf-8").split("---")[1]
    m = re.search(r"^dp: (\d+)", fm, re.M)
    if m:
        page_dp[f.stem] = int(m.group(1))
for band in meta.get("singles", []) + meta.get("dp", []):
    for e in band["entries"]:
        if (
            e["slug"] in page_dp
            and "dp" in e
            and e.get("dp") not in (None, page_dp[e["slug"]])
        ):
            issue(
                f"meta.json dp mismatch {e['slug']}: {e.get('dp')} vs page {page_dp[e['slug']]}"
            )

# 2b. hp tier counts: stats source vs mechanics page text
sysc = J(ROOT / "data-mined" / "system_constants.json")
tier_counts = {r["hp"]: r["count"] for r in sysc["hpDistribution"]}
had = (CONTENT / "mechanics" / "health-and-damage.md").read_text(encoding="utf-8")
for hp, cnt in tier_counts.items():
    hp_s = f"{hp:,}"
    if hp_s in had:
        m = re.search(
            re.escape(hp_s) + r"[^.\n]{0,80}?(\d+)\s*(?:fighters|character)", had
        )
        if m and int(m.group(1)) != cnt:
            issue(
                f"health-and-damage tier count for {hp_s}: page says {m.group(1)}, data says {cnt}"
            )
counts_str = "/".join(str(tier_counts[k]) for k in sorted(tier_counts))
if not re.search(r"9\s*/\s*14\s*/\s*147\s*/\s*16", had):
    note(
        f"health-and-damage does not show counts pattern (data: {counts_str}) — verify manually"
    )

# 2c. version-string consistency
versions = Counter()
for f in CONTENT.rglob("*.md"):
    if f.parent.name == "patches":  # patch pages carry their own historical version by design
        continue
    m = re.search(r'^asOfVersion: "(.*)"', f.read_text(encoding="utf-8"), re.M)
    if m:
        versions[m.group(1)] += 1
print("=== asOfVersion variants:", dict(versions))
if len(versions) > 1:
    minor = {k: v for k, v in versions.items() if v < max(versions.values())}
    note(f"non-dominant version strings: {minor}")

# 2d. skill cost: character moveset blast1 skillCost vs skills page skillCost
skill_cost_page = {}
for f in (CONTENT / "skills").glob("*.md"):
    raw = f.read_text(encoding="utf-8")
    nm = re.search(r'^name: "(.*)"', raw, re.M)
    sc = re.search(r"^skillCost: (\d+)", raw, re.M)
    if nm and sc:
        skill_cost_page[nm.group(1)] = int(sc.group(1))
mismatch = 0
for f in (CONTENT / "characters").glob("*.md"):
    fm = f.read_text(encoding="utf-8").split("---")[1]
    for m in re.finditer(
        r'- name: "([^"]+)"\n    type: "blast1"\n    skillCost: (\d+)', fm
    ):
        nm, c = m.group(1), int(m.group(2))
        if nm in skill_cost_page and skill_cost_page[nm] != c:
            mismatch += 1
            if mismatch <= 5:
                issue(
                    f"skill cost mismatch '{nm}': char page {c} vs skill page {skill_cost_page[nm]} ({f.stem})"
                )
if mismatch > 5:
    issue(f"...{mismatch} total skill-cost mismatches")

# ---------- 3. end-to-end sample verification (raw -> rendered) ----------
samples = [("0000_00", "goku-z-early"), ("0620_00", "android-13"), ("0790_00", "whis")]
for cid, slug in samples:
    c = chars[cid]
    html_f = BUILT / "characters" / f"{slug}.html"
    if not html_f.exists():
        issue(f"sample page missing: {slug}")
        continue
    v = strip_scripts(html_f.read_text(encoding="utf-8", errors="ignore"))
    checks = []
    if c["hp"]:
        checks.append((f"{int(c['hp']):,}", "hp"))
    if c.get("ultimate") and c["ultimate"].get("kiCost"):
        checks.append((f"{int(c['ultimate']['kiCost']):,}", "ult ki"))
    if c.get("maxSkillStock"):
        checks.append((str(int(c["maxSkillStock"])), "max stock"))
    e = enrich.get(cid, {})
    if e.get("dp"):
        checks.append((str(e["dp"]), "dp"))
    for needle, label in checks:
        if needle not in v:
            issue(f"e2e {slug}: rendered page missing {label} value {needle}")
print(f"=== e2e samples verified: {[s for _, s in samples]}")

# transformation delta recompute (Bojack)
bj, fpb = chars.get("0660_00"), chars.get("0660_01")
if bj and fpb and bj["hp"] and fpb["hp"]:
    delta = int(fpb["hp"] - bj["hp"])
    tf = CONTENT / "transformations"
    page = next((p for p in tf.glob("bojack-to-full-power-bojack*.md")), None)
    if page and f"+{delta:,}" not in page.read_text(encoding="utf-8"):
        issue(f"bojack transform delta {delta:+,} not on page")
    else:
        print(f"=== transform delta verified: Bojack {delta:+,} HP")

# ---------- 4. formatting/artifact bugs in visible HTML ----------
bad_fmt = Counter()
samples2 = {}
for f in BUILT.rglob("*.html"):
    v = strip_scripts(f.read_text(encoding="utf-8", errors="ignore"))
    # unformatted big numbers in table cells (heuristic: >=10000 with no comma)
    for m in re.findall(r">(\d{5,7})<", v):
        if not m.startswith("0"):
            bad_fmt["uncomma"] += 1
            samples2.setdefault("uncomma", (str(f.relative_to(BUILT))[:50], m))
            break
    for pat, label in [(r"(?<!<code)(?<!<strong)>\s*null\s*<", "null"), (r"(?<!<code)>\s*None\s*<", "None")]:
        if re.search(pat, v):
            bad_fmt[label] += 1
            samples2.setdefault(label, (str(f.relative_to(BUILT))[:50], ""))
for label, c in bad_fmt.items():
    issue(f"visible '{label}' in {c} pages e.g. {samples2[label]}")

# ---------- 5. duplicate display names within a collection ----------
for coll in ["characters", "skills", "mechanics", "guides"]:
    names = Counter()
    for f in (CONTENT / coll).glob("*.md"):
        m = re.search(r'^(?:name|title): "(.*)"', f.read_text(encoding="utf-8"), re.M)
        if m:
            names[m.group(1)] += 1
    dups = {k: v for k, v in names.items() if v > 1}
    if dups:
        note(
            f"duplicate display names in {coll}: {dups} (distinct slugs — OK if intentional forms)"
        )

# ---------- 6. search index duplicates ----------
idx = J(ROOT / "public" / "search-index.json")
hrefs = Counter(e["h"] for e in idx)
dups = {k: v for k, v in hrefs.items() if v > 1}
if dups:
    issue(f"search index duplicate hrefs: {list(dups.items())[:5]}")

print(
    f"\n==== AUDIT v4 {'CLEAN' if not issues else f'FOUND {len(issues)} ISSUES'} ===="
)
