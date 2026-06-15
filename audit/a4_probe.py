"""Agent-04 probe: verify mechanics/glossary numeric claims against datamined character frontmatter.
Read-only. Writes nothing to content/. Prints findings to stdout."""
import os, re, json, glob
from collections import Counter, defaultdict

ROOT = r"c:\vaults\sparking_zero"
CHARS = os.path.join(ROOT, "content", "characters")

def parse_front(path):
    txt = open(path, encoding="utf-8").read()
    m = re.search(r"^---\n(.*?)\n---", txt, re.S)
    if not m:
        return {}
    fm = {}
    for line in m.group(1).splitlines():
        mm = re.match(r"^([A-Za-z0-9_]+):\s*(.*)$", line)
        if mm:
            k, v = mm.group(1), mm.group(2).strip()
            fm[k] = v
    return fm

def num(v):
    if v is None: return None
    v = v.strip().strip('"')
    if v in ("", "null", "~"): return None
    try:
        return float(v) if "." in v else int(v)
    except ValueError:
        return v

rows = []
for p in glob.glob(os.path.join(CHARS, "*.md")):
    fm = parse_front(p)
    rows.append({
        "slug": fm.get("slug", os.path.basename(p)[:-3]).strip('"'),
        "name": fm.get("name", "").strip('"'),
        "playable": fm.get("playable", "true"),
        "maxSkillStock": num(fm.get("maxSkillStock")),
        "initialSkillStock": num(fm.get("initialSkillStock")),
        "kiChargeSpeed": num(fm.get("kiChargeSpeed")),
        "initialKi": num(fm.get("initialKi")),
        "hp": num(fm.get("hp")),
        "sparkingDrainPerSec": num(fm.get("sparkingDrainPerSec")),
    })

print(f"total character files: {len(rows)}")

def dist(field):
    c = Counter()
    for r in rows:
        c[r[field]] += 1
    return dict(sorted((str(k), v) for k, v in c.items()))

for f in ["maxSkillStock", "initialSkillStock", "kiChargeSpeed", "sparkingDrainPerSec", "hp"]:
    print(f"\n== {f} distribution (all files) ==")
    print(json.dumps(dist(f), indent=1))

# specific lookups referenced in mechanics pages
targets = ["cell", "perfect-cell", "cell-perfect-form", "piccolo", "piccolo-fused-with-kami",
           "android-19", "dr-gero", "android-16", "android-18", "android-17-z", "android-17-super",
           "master-roshi", "master-roshi-max-power", "vegeta-super", "super-vegeta", "yajirobe",
           "babidi", "mr-satan"]
print("\n== specific lookups ==")
by_slug = {r["slug"]: r for r in rows}
for t in targets:
    r = by_slug.get(t)
    if r:
        print(f"{t:28s} maxStock={r['maxSkillStock']} initStock={r['initialSkillStock']} "
              f"kiCharge={r['kiChargeSpeed']} initKi={r['initialKi']} hp={r['hp']}")
    else:
        print(f"{t:28s} (no such slug)")

# cross-check vs system_constants.json
sc = json.load(open(os.path.join(ROOT, "data-mined", "system_constants.json"), encoding="utf-8"))
print("\n== system_constants maxSkillStockDistribution ==")
for d in sc.get("maxSkillStockDistribution", []):
    print(f"  value={d['value']} count={d['count']}")
print("== system_constants initialSkillStockDistribution ==")
for d in sc.get("initialSkillStockDistribution", []):
    print(f"  value={d['value']} count={d['count']} examples={d['examples'][:6]}")
print("== system_constants kiChargeSpeedDistribution ==")
for d in sc.get("kiChargeSpeedDistribution", []):
    print(f"  value={d['value']} count={d['count']}")
