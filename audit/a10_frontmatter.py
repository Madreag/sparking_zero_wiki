"""
Agent 10 cross-cutting probe: frontmatter / schema conformance at scale.
READ-ONLY. Parses every content/**/*.md, runs confidence-honesty, enum,
numeric, date/version, duplicate and body checks. Emits a structured report
to stdout and audit/a10_frontmatter.json for reference.
"""
import json
import re
import datetime as dt
from pathlib import Path
from collections import Counter, defaultdict

import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
CONTENT = ROOT / "content"
TODAY = dt.date(2026, 6, 15)
CANON_VERSION = "v2.2 (2026-05-26 update)"
CANON_DATE = "2026-05-26"
STALE_AFTER_DAYS = 240

# ---- schema enums (mirror lib/schemas.ts) ----
CONFIDENCE = {"confirmed", "datamined", "community", "unverified"}
NUMERIC_TAG = {"official", "datamined", "community"}
MOVE_TYPE = {"rush", "smash", "throw", "blast1", "blast2", "ultimate", "evasive", "special"}
TRANSFORMS_TO_KIND = {"transform", "fusion", "revert"}          # characterSchema.transformsTo[].kind
TRANSFORMATION_KIND = {"transform", "fusion", "awaken", "revert"}  # transformationSchema.kind
CHAR_TIER = {"S", "A", "B", "C", "D", "unranked"}
SKILLBLAST_TIER = {"S", "A", "B", "C", "D", "situational"}
BLAST_CLASS = {"super", "ultimate"}
MECH_CAT = {"offense", "defense", "movement", "resource", "system", "status"}
GAMEMODE_CAT = {"offline", "online", "pve", "pvp", "hub", "training"}
PATCH_TYPE = {"launch", "major", "balance", "content", "hotfix"}
DLC_TYPE = {"paid", "free", "preorder", "season-pass"}
GUIDE_CAT = {"meta", "pvp", "pve", "beginner", "tech", "economy", "tier-list"}

HP_TIERS = {30000, 35000, 40000, 45000}
HP_DIST_EXPECTED = {30000: 9, 35000: 14, 40000: 147, 45000: 16}


def split_fm(text):
    """Return (frontmatter_str, body_str, fm_start_lineno_1based)."""
    if not text.startswith("---"):
        return None, text, 0
    # split on the first two '---' fences
    parts = text.split("\n")
    # find closing fence
    end = None
    for i in range(1, len(parts)):
        if parts[i].strip() == "---":
            end = i
            break
    if end is None:
        return None, text, 0
    fm = "\n".join(parts[1:end])
    body = "\n".join(parts[end + 1:])
    return fm, body, 2  # frontmatter content begins on line 2


def key_line(lines, key):
    """1-based line number of first top-level `key:` in the whole file lines."""
    pat = re.compile(r"^" + re.escape(key) + r":")
    for i, ln in enumerate(lines):
        if pat.match(ln):
            return i + 1
    return None


def parse_date(s):
    if not isinstance(s, str):
        return None
    s = s.strip()
    m = re.match(r"^(\d{4})-(\d{2})-(\d{2})$", s)
    if not m:
        return None
    try:
        return dt.date(int(m.group(1)), int(m.group(2)), int(m.group(3)))
    except ValueError:
        return None


# ---- load everything ----
records = []  # list of dicts: collection, slug(file), fm(dict), body, path, lines, parse_error
for d in sorted(CONTENT.iterdir()):
    if not d.is_dir():
        continue
    for f in sorted(d.glob("*.md")):
        text = f.read_text(encoding="utf-8")
        lines = text.split("\n")
        fm_str, body, _ = split_fm(text)
        rec = {
            "collection": d.name,
            "file": f.stem,
            "path": str(f.relative_to(ROOT)).replace("\\", "/"),
            "lines": lines,
            "body": body,
            "fm": {},
            "parse_error": None,
        }
        if fm_str is None:
            rec["parse_error"] = "no-frontmatter"
        else:
            try:
                rec["fm"] = yaml.safe_load(fm_str) or {}
            except Exception as e:  # noqa
                rec["parse_error"] = f"yaml: {e}"
        records.append(rec)

by_coll = defaultdict(list)
for r in records:
    by_coll[r["collection"]].append(r)

print("=" * 70)
print("CORPUS:", len(records), "files across", len(by_coll), "collections")
for c in sorted(by_coll):
    print(f"  {c:18} {len(by_coll[c])}")
parse_errs = [r for r in records if r["parse_error"]]
print("PARSE ERRORS:", len(parse_errs))
for r in parse_errs:
    print("   ", r["path"], "->", r["parse_error"])

out = {"corpus": {c: len(by_coll[c]) for c in sorted(by_coll)}, "parse_errors": [(r["path"], r["parse_error"]) for r in parse_errs]}


def conf_of(r):
    """Effective confidence (schema default community)."""
    v = r["fm"].get("confidence")
    return v if v is not None else "community"


# ============================================================
# CHECK 1 — CONFIDENCE HONESTY AT SCALE
# ============================================================
print("\n" + "=" * 70)
print("CHECK 1 — CONFIDENCE HONESTY")
conf_table = defaultdict(Counter)
for r in records:
    raw = r["fm"].get("confidence")
    key = raw if raw is not None else "(absent→community)"
    conf_table[r["collection"]][key] += 1
out["confidence_by_collection"] = {c: dict(conf_table[c]) for c in sorted(conf_table)}
print("confidence counts per collection:")
for c in sorted(conf_table):
    print(f"  {c:18}", dict(conf_table[c]))

# 1a. datamined character pages that carry a DP value (community-only)
dm_char_with_dp = []
for r in by_coll["characters"]:
    if conf_of(r) == "datamined":
        dp = r["fm"].get("dp")
        if dp is not None:
            dm_char_with_dp.append((r, dp))
print(f"\n[1a] characters confidence=datamined WITH dp (community-only): {len(dm_char_with_dp)}")
for r, dp in dm_char_with_dp[:8]:
    ln = key_line(r["lines"], "dp")
    cln = key_line(r["lines"], "confidence")
    print(f"    {r['path']}:{ln} dp={dp}  (confidence@L{cln})")
out["datamined_char_with_dp"] = {
    "count": len(dm_char_with_dp),
    "examples": [
        {"path": r["path"], "dp": dp, "dp_line": key_line(r["lines"], "dp"),
         "confidence_line": key_line(r["lines"], "confidence")}
        for r, dp in dm_char_with_dp
    ],
}

# 1b. transformation pages with dpFrom/dpTo under datamined stamp
dm_tf_with_dp = []
for r in by_coll["transformations"]:
    if conf_of(r) == "datamined":
        if r["fm"].get("dpFrom") is not None or r["fm"].get("dpTo") is not None:
            dm_tf_with_dp.append(r)
print(f"\n[1b] transformations confidence=datamined WITH dpFrom/dpTo: {len(dm_tf_with_dp)} of {len(by_coll['transformations'])}")
for r in dm_tf_with_dp[:8]:
    ln = key_line(r["lines"], "dpFrom") or key_line(r["lines"], "dpTo")
    print(f"    {r['path']}:{ln} dpFrom={r['fm'].get('dpFrom')} dpTo={r['fm'].get('dpTo')}")
out["datamined_tf_with_dp"] = {
    "count": len(dm_tf_with_dp),
    "total_transformations": len(by_coll["transformations"]),
    "examples": [
        {"path": r["path"], "dpFrom": r["fm"].get("dpFrom"), "dpTo": r["fm"].get("dpTo"),
         "line": key_line(r["lines"], "dpFrom") or key_line(r["lines"], "dpTo")}
        for r in dm_tf_with_dp
    ],
}

# 1c. datamined character pages carrying any moveset damage (class-default risk)
dm_char_with_movedmg = []
for r in by_coll["characters"]:
    if conf_of(r) == "datamined":
        ms = r["fm"].get("moveset") or []
        dmg_moves = [m for m in ms if isinstance(m, dict) and m.get("damage") is not None]
        if dmg_moves:
            dm_char_with_movedmg.append((r, len(dmg_moves)))
print(f"\n[1c] characters confidence=datamined WITH moveset damage values: {len(dm_char_with_movedmg)}")
out["datamined_char_with_movedamage"] = {
    "count": len(dm_char_with_movedmg),
    "examples": [{"path": r["path"], "moves_with_damage": n} for r, n in dm_char_with_movedmg[:15]],
}

# 1d. blasts datamined with class-default (—) per-user damage: count datamined blasts where users lack damage
dm_blast_no_dmg = 0
dm_blast_total = 0
for r in by_coll["blasts"]:
    if conf_of(r) == "datamined":
        dm_blast_total += 1
        users = r["fm"].get("users") or []
        if all((not isinstance(u, dict)) or u.get("damage") is None for u in users):
            dm_blast_no_dmg += 1
print(f"[1d] blasts datamined={dm_blast_total}; of those with NO per-user datamined damage (all class-default): {dm_blast_no_dmg}")
out["datamined_blast_no_damage"] = {"datamined_total": dm_blast_total, "all_classdefault": dm_blast_no_dmg}

# ============================================================
# CHECK 2 — ENUM CONFORMANCE
# ============================================================
print("\n" + "=" * 70)
print("CHECK 2 — ENUM CONFORMANCE")
enum_viol = []


def check_enum(r, value, allowed, label):
    if value is None:
        return
    if value not in allowed:
        enum_viol.append((r["path"], label, value))


for r in records:
    fm = r["fm"]
    # confidence on every collection
    check_enum(r, fm.get("confidence"), CONFIDENCE, "confidence")
    coll = r["collection"]
    if coll == "characters":
        check_enum(r, fm.get("tier"), CHAR_TIER, "tier")
        for m in (fm.get("moveset") or []):
            if isinstance(m, dict):
                check_enum(r, m.get("type"), MOVE_TYPE, f"moveset.type[{m.get('name')!r}]")
        for t in (fm.get("transformsTo") or []):
            if isinstance(t, dict):
                check_enum(r, t.get("kind"), TRANSFORMS_TO_KIND, f"transformsTo.kind[{t.get('target')!r}]")
    elif coll == "skills":
        check_enum(r, fm.get("tier"), SKILLBLAST_TIER, "tier")
    elif coll == "blasts":
        check_enum(r, fm.get("class"), BLAST_CLASS, "class")
        check_enum(r, fm.get("tier"), SKILLBLAST_TIER, "tier")
    elif coll == "transformations":
        check_enum(r, fm.get("kind"), TRANSFORMATION_KIND, "kind")
    elif coll == "mechanics":
        check_enum(r, fm.get("category"), MECH_CAT, "category")
        for v in (fm.get("values") or []):
            if isinstance(v, dict):
                check_enum(r, v.get("tag"), NUMERIC_TAG, f"values.tag[{v.get('label')!r}]")
    elif coll == "game-modes":
        check_enum(r, fm.get("category"), GAMEMODE_CAT, "category")
        for v in (fm.get("values") or []):
            if isinstance(v, dict):
                check_enum(r, v.get("tag"), NUMERIC_TAG, f"values.tag[{v.get('label')!r}]")
    elif coll == "patches":
        check_enum(r, fm.get("type"), PATCH_TYPE, "type")
    elif coll == "dlc":
        check_enum(r, fm.get("type"), DLC_TYPE, "type")
    elif coll == "guides":
        check_enum(r, fm.get("category"), GUIDE_CAT, "category")
    # glossary.category is free string -> no enum

print(f"enum violations: {len(enum_viol)}")
for p, lbl, val in enum_viol[:40]:
    print(f"    {p}  {lbl} = {val!r}")
out["enum_violations"] = [{"path": p, "field": lbl, "value": v} for p, lbl, v in enum_viol]

# ============================================================
# CHECK 3 — NUMERIC SANITY
# ============================================================
print("\n" + "=" * 70)
print("CHECK 3 — NUMERIC SANITY")
num = {"hp_bad": [], "dp_bad": [], "move_ki_bad": [], "super_out": [], "ult_out": [],
       "maxstock_bad": [], "initstock_bad": [], "gauge_bad": []}
hp_counter = Counter()

for r in by_coll["characters"]:
    fm = r["fm"]
    slug = fm.get("slug", r["file"])
    hp = fm.get("hp")
    if hp is not None:
        hp_counter[hp] += 1
        if hp not in HP_TIERS:
            num["hp_bad"].append((r["path"], key_line(r["lines"], "hp"), slug, hp))
    dp = fm.get("dp")
    if dp is not None and (dp < 1 or dp > 10):
        num["dp_bad"].append((r["path"], key_line(r["lines"], "dp"), slug, dp))
    mx = fm.get("maxSkillStock")
    ini = fm.get("initialSkillStock")
    if mx is not None and mx > 10:
        num["maxstock_bad"].append((r["path"], slug, mx))
    if mx is not None and ini is not None and ini > mx:
        num["initstock_bad"].append((r["path"], slug, ini, mx))
    sg = fm.get("skillGaugeGains")
    if isinstance(sg, dict):
        for k, v in sg.items():
            if isinstance(v, (int, float)) and (v < 0 or v > 2):
                num["gauge_bad"].append((r["path"], slug, k, v))
    for m in (fm.get("moveset") or []):
        if not isinstance(m, dict):
            continue
        ki = m.get("kiCost")
        typ = m.get("type")
        if ki is not None:
            if ki < 1000 or ki > 60000:
                num["move_ki_bad"].append((r["path"], slug, m.get("name"), typ, ki))
            if typ == "blast2" and not (10000 <= ki <= 30000):
                num["super_out"].append((r["path"], slug, m.get("name"), ki))
            if typ == "ultimate" and not (40000 <= ki <= 60000):
                num["ult_out"].append((r["path"], slug, m.get("name"), ki))

# blasts per-user ki cost clustering
for r in by_coll["blasts"]:
    fm = r["fm"]
    slug = fm.get("slug", r["file"])
    cls = fm.get("class")
    for u in (fm.get("users") or []):
        if not isinstance(u, dict):
            continue
        ki = u.get("kiCost")
        if ki is None:
            continue
        if ki < 1000 or ki > 60000:
            num["move_ki_bad"].append((r["path"], slug, u.get("character"), cls, ki))
        if cls == "super" and not (10000 <= ki <= 30000):
            num["super_out"].append((r["path"], slug, u.get("character"), ki))
        if cls == "ultimate" and not (40000 <= ki <= 60000):
            num["ult_out"].append((r["path"], slug, u.get("character"), ki))

print("HP distribution (frontmatter):", dict(sorted(hp_counter.items())))
print("HP expected (system_constants):", HP_DIST_EXPECTED)
for k in num:
    print(f"  {k}: {len(num[k])}")
    for item in num[k][:6]:
        print("      ", item)
out["numeric"] = {
    "hp_distribution_frontmatter": {str(k): v for k, v in sorted(hp_counter.items())},
    "hp_distribution_expected": {str(k): v for k, v in HP_DIST_EXPECTED.items()},
    **{k: num[k] for k in num},
    "counts": {k: len(num[k]) for k in num},
}

# ============================================================
# CHECK 4 — DATE / VERSION CONSISTENCY
# ============================================================
print("\n" + "=" * 70)
print("CHECK 4 — DATE/VERSION")
date_issues = {"asOfVersion_dev": [], "asOfDate_dev": [], "stale": [], "future": [],
               "malformed": [], "no_sources": [], "datamined_no_gamebuild": [], "no_lastVerified": []}
for r in records:
    fm = r["fm"]
    coll = r["collection"]
    aov = fm.get("asOfVersion")
    aod = fm.get("asOfDate")
    lv = fm.get("lastVerified")
    # asOfVersion / asOfDate — patches legitimately differ
    if coll != "patches":
        if aov is not None and aov != CANON_VERSION:
            date_issues["asOfVersion_dev"].append((r["path"], key_line(r["lines"], "asOfVersion"), aov))
        if aod is not None and aod != CANON_DATE:
            date_issues["asOfDate_dev"].append((r["path"], key_line(r["lines"], "asOfDate"), aod))
    # lastVerified date math
    if lv is None:
        date_issues["no_lastVerified"].append((r["path"], coll))
    else:
        d = parse_date(lv)
        if d is None:
            date_issues["malformed"].append((r["path"], lv))
        else:
            if d > TODAY:
                date_issues["future"].append((r["path"], key_line(r["lines"], "lastVerified"), lv))
            days = (TODAY - d).days
            if days > STALE_AFTER_DAYS:
                date_issues["stale"].append((r["path"], lv, days))
    # sources non-empty
    srcs = fm.get("sources") or []
    if not srcs:
        date_issues["no_sources"].append((r["path"], coll, conf_of(r)))
    elif conf_of(r) == "datamined":
        joined = " ".join(str(s).lower() for s in srcs)
        if not any(w in joined for w in ["game file", "steam build", "cue4parse", "characterdata", "masterdata", "data-mined", "datamine"]):
            date_issues["datamined_no_gamebuild"].append((r["path"], srcs))

for k in date_issues:
    print(f"  {k}: {len(date_issues[k])}")
    for item in date_issues[k][:6]:
        print("      ", item)
out["dates"] = {k: date_issues[k] for k in date_issues}
out["dates_counts"] = {k: len(v) for k, v in date_issues.items()}

# ============================================================
# CHECK 5 — DUPLICATES
# ============================================================
print("\n" + "=" * 70)
print("CHECK 5 — DUPLICATES")
dup = {"slug_dupe": [], "name_dupe": [], "array_dupe": []}
for coll, recs in by_coll.items():
    slugs = Counter()
    names = defaultdict(list)
    for r in recs:
        s = r["fm"].get("slug")
        if s:
            slugs[s] += 1
        nm = r["fm"].get("name") or r["fm"].get("term") or r["fm"].get("title")
        if nm:
            names[nm].append(r["file"])
    for s, c in slugs.items():
        if c > 1:
            dup["slug_dupe"].append((coll, s, c))
    for nm, files in names.items():
        if len(files) > 1:
            dup["name_dupe"].append((coll, nm, files))

# duplicate entries inside arrays
for r in records:
    fm = r["fm"]
    # blast users (by characterSlug)
    if r["collection"] == "blasts":
        seen = Counter()
        for u in (fm.get("users") or []):
            if isinstance(u, dict):
                key = u.get("characterSlug") or u.get("character")
                if key:
                    seen[key] += 1
        for k, c in seen.items():
            if c > 1:
                dup["array_dupe"].append((r["path"], "users", k, c))
    # skill users (strings)
    if r["collection"] == "skills":
        seen = Counter(u for u in (fm.get("users") or []) if isinstance(u, str))
        for k, c in seen.items():
            if c > 1:
                dup["array_dupe"].append((r["path"], "users", k, c))
    # strengths / weaknesses / classes / transformsTo
    for arrkey in ("strengths", "weaknesses", "classes", "rewards", "adds", "variants", "aliases", "counters", "counteredBy"):
        arr = fm.get(arrkey)
        if isinstance(arr, list):
            seen = Counter(x for x in arr if isinstance(x, str))
            for k, c in seen.items():
                if c > 1:
                    dup["array_dupe"].append((r["path"], arrkey, k, c))

print(f"  slug_dupe: {len(dup['slug_dupe'])}", dup["slug_dupe"][:10])
print(f"  name_dupe: {len(dup['name_dupe'])} (forms expected; sample):")
for item in dup["name_dupe"][:12]:
    print("      ", item)
print(f"  array_dupe: {len(dup['array_dupe'])}")
for item in dup["array_dupe"][:12]:
    print("      ", item)
out["duplicates"] = dup
out["duplicates_counts"] = {k: len(v) for k, v in dup.items()}

# ============================================================
# CHECK 7 — EMPTY / THIN BODIES + placeholders
# ============================================================
print("\n" + "=" * 70)
print("CHECK 7 — BODIES")
body_stats = defaultdict(lambda: {"empty": 0, "total": 0})
placeholders = []
PLACEHOLDER_PATS = ["pending fresh", "schema dump", "lorem ipsum", "TKTK", "TODO", "TBD", "FIXME", "xxx placeholder"]
for r in records:
    b = (r["body"] or "").strip()
    body_stats[r["collection"]]["total"] += 1
    if not b:
        body_stats[r["collection"]]["empty"] += 1
    else:
        low = b.lower()
        for p in PLACEHOLDER_PATS:
            if p.lower() in low:
                placeholders.append((r["path"], p))
                break
print("empty-body counts per collection:")
for c in sorted(body_stats):
    s = body_stats[c]
    print(f"  {c:18} empty {s['empty']:4}/{s['total']}")
print("placeholder bodies:", len(placeholders), placeholders[:10])
out["bodies"] = {c: body_stats[c] for c in sorted(body_stats)}
out["placeholders"] = placeholders

# ============================================================
# CHECK 8 — MISC (playable, order, non-empty arrays)
# ============================================================
print("\n" + "=" * 70)
print("CHECK 8 — MISC")
misc = {"char_no_playable": [], "order_bad": [], "blast_no_users": [],
        "skill_count_no_users": [], "skill_users_no_count": [], "blast_user_count_mismatch": []}
for r in by_coll["characters"]:
    if "playable" not in (r["fm"] or {}):
        misc["char_no_playable"].append(r["path"])
for coll in ("episode-battles", "patches", "dlc"):
    for r in by_coll[coll]:
        o = r["fm"].get("order")
        if not isinstance(o, (int, float)):
            misc["order_bad"].append((r["path"], o))
for r in by_coll["blasts"]:
    users = r["fm"].get("users") or []
    if len(users) == 0:
        misc["blast_no_users"].append(r["path"])
for r in by_coll["skills"]:
    uc = r["fm"].get("userCount")
    users = r["fm"].get("users") or []
    if uc is not None and len(users) == 0:
        misc["skill_count_no_users"].append((r["path"], uc))
    if users and uc is None:
        misc["skill_users_no_count"].append((r["path"], len(users)))
    if uc is not None and users and uc != len(users):
        misc["blast_user_count_mismatch"].append((r["path"], uc, len(users)))
for k in misc:
    print(f"  {k}: {len(misc[k])}", misc[k][:8])
out["misc"] = misc
out["misc_counts"] = {k: len(v) for k, v in misc.items()}

# ---- write JSON ----
(ROOT / "audit" / "a10_frontmatter.json").write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
print("\nWROTE audit/a10_frontmatter.json")
