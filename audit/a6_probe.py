"""
Audit Agent 6 probe — guides / research / meta tier consistency.

Read-only. Does NOT modify any content/data/code. Cross-checks:
  1. TIER CONSISTENCY: meta.json (singles[] + dp[] bands) vs content/characters/*.md frontmatter `tier`.
     The character `tier` enum is S/A/B/C/D/unranked (no Z); the board uses Z/S/A/B/D (singles) and
     Z/S/A/C/D (dp). The page tier tracks the SINGLES board under a documented relabel:
        board Z -> page S, board S -> page A, board A -> page B, board B -> page C, board D -> page D.
  2. COUNTERS RESOLVE: every meta.json counters[].slug / beats[] / losesTo[] must be a real character slug.
  3. DP MATH: recompute hpPerDp = round(hp/dp) from the character pages for the dp-team-value-math table
     rows and flag divergence from the guide's printed values.
Run:  python audit/a6_probe.py
"""
import json, os, re, glob

ROOT = r"c:\vaults\sparking_zero"
CHARDIR = os.path.join(ROOT, "content", "characters")
META = os.path.join(ROOT, "data-mined", "meta.json")

# board(singles) -> expected page tier
RELABEL = {"Z": "S", "S": "A", "A": "B", "B": "C", "D": "D"}

def parse_frontmatter(path):
    with open(path, encoding="utf-8") as f:
        txt = f.read()
    if not txt.startswith("---"):
        return {}
    end = txt.find("\n---", 3)
    fm = txt[3:end]
    out = {}
    for key in ("slug", "name", "tier", "dp", "hp", "hpInherited", "playable"):
        m = re.search(r'^%s:\s*"?([^"\n]+?)"?\s*$' % key, fm, re.M)
        if m:
            out[key] = m.group(1).strip()
    return out

# ---- load character pages ----
chars = {}
for p in glob.glob(os.path.join(CHARDIR, "*.md")):
    fm = parse_frontmatter(p)
    if "slug" in fm:
        chars[fm["slug"]] = fm

print(f"[chars] parsed {len(chars)} character pages\n")

# ---- load meta.json ----
meta = json.load(open(META, encoding="utf-8"))
singles = {}  # slug -> tier
dp = {}
for band in meta["singles"]:
    for e in band["entries"]:
        singles[e["slug"]] = band["tier"]
for band in meta["dp"]:
    for e in band["entries"]:
        dp[e["slug"]] = band["tier"]

print(f"[meta] singles entries={len(singles)}  dp entries={len(dp)}")
print(f"[meta] singles tiers={[b['tier'] for b in meta['singles']]}  dp tiers={[b['tier'] for b in meta['dp']]}\n")

# ===== CHECK 1: tier consistency =====
print("="*70)
print("CHECK 1  TIER TABLE  (board singles / board dp / page tier / verdict)")
print("="*70)
allslugs = sorted(set(singles) | set(dp))
mismatch = 0
missing = 0
for slug in allslugs:
    s = singles.get(slug, "-")
    d = dp.get(slug, "-")
    page = chars.get(slug, {}).get("tier", None)
    if slug not in chars:
        missing += 1
        verdict = "NO PAGE (slug unresolved!)"
    elif page is None:
        verdict = "page has NO tier"
    else:
        exp = RELABEL.get(s) if s != "-" else None
        if s == "-":
            verdict = f"page={page} (singles-unranked; dp={d})"
        elif page == exp:
            verdict = f"OK (page {page} == singles {s})"
        else:
            verdict = f"** MISMATCH page={page} expected={exp} (board singles {s})"
            mismatch += 1
    print(f"  {slug:42s} S={s:2s} DP={d:2s} page={str(page):4s} | {verdict}")
print(f"\n  --> singles->page mismatches: {mismatch}; unresolved slugs: {missing}")

# ===== CHECK 2: counters resolve =====
print("\n" + "="*70)
print("CHECK 2  COUNTERS[] SLUG RESOLUTION")
print("="*70)
bad = 0
for c in meta["counters"]:
    for slot in ("slug",):
        if c[slug_key := "slug"] not in chars:
            print(f"  ** counter.slug not a char page: {c['slug']}")
            bad += 1
    for rel in ("beats", "losesTo"):
        for t in c.get(rel, []):
            if t not in chars:
                print(f"  ** {c['slug']} {rel} -> unresolved slug: {t}")
                bad += 1
# also check singles/dp entry slugs resolve
entry_unres = sorted(s for s in allslugs if s not in chars)
print(f"\n  counters[] unresolved refs: {bad}")
print(f"  meta singles/dp entry slugs not resolving to a char page: {entry_unres}")

# ===== CHECK 3: DP math (dp-team-value-math.md HP/DP table) =====
print("\n" + "="*70)
print("CHECK 3  DP MATH  hpPerDp = round(hp/dp)  vs guide's printed values")
print("="*70)
# (slug, guide_hp, guide_dp, guide_hpdp)  -- from content/guides/dp-team-value-math.md
GUIDE = [
    ("master-roshi", 30000, 2, 15000),
    ("mr-satan", 30000, 1, 30000),
    ("saibaman", 35000, 1, 35000),
    ("yajirobe", 35000, 2, 17500),
    ("spopovich", 35000, 2, 17500),
    ("nappa", 40000, 3, 13333),
    ("recoome", 40000, 3, 13333),
    ("master-roshi-max-power", 40000, 2, 20000),
    ("broly-z-legendary-super-saiyan", 45000, 9, 5000),
    ("broly-super-super-saiyan-full-power", 45000, 9, 5000),
    ("kale-super-saiyan-berserk", 45000, 7, 6429),
    ("beerus", 45000, 10, 4500),
    ("whis", 45000, 10, 4500),
    ("orange-piccolo", 45000, 8, 5625),
    ("fusion-android-13", 45000, 7, 6429),
    ("android-16", 40000, 5, 8000),
    ("android-19", 40000, 4, 10000),
    ("vegeta-mini-super-saiyan-3", 40000, 7, 5714),
    ("vegeta-mini-super-saiyan-2", 40000, 6, 6667),
    ("gohan-beast", 40000, 9, 4444),   # guide: "40,000 (est., null)"
    ("vegito-super-saiyan-god-super-saiyan", 40000, 10, 4000),
    ("gogeta-gt-super-saiyan-4", 40000, 10, 4000),
    ("jiren-full-power", 40000, 9, 4444),
    ("cell-max", 40000, 9, 4444),
]
for slug, ghp, gdp, ghpdp in GUIDE:
    pg = chars.get(slug, {})
    php = pg.get("hp")
    pdp = pg.get("dp")
    pinh = pg.get("hpInherited")
    note = []
    if pdp is not None and int(pdp) != gdp:
        note.append(f"DP DIFF page={pdp} guide={gdp}")
    if php is None:
        note.append(f"page hp=NULL (guide used {ghp})")
    else:
        if int(php) != ghp:
            note.append(f"HP DIFF page={php} guide={ghp}")
        truehpdp = round(int(php) / int(pdp)) if pdp else None
        if truehpdp != ghpdp:
            note.append(f"HP/DP DIFF true={truehpdp} guide={ghpdp}")
    flag = "  ** " if note else "  ok  "
    print(f"{flag}{slug:42s} page(hp={php},dp={pdp},inh={pinh}) :: {'; '.join(note) if note else 'matches'}")

print("\n[done]")
