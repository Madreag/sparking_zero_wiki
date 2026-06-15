"""Audit Agent 3 — skills probe (READ-ONLY).

Cross-checks content/skills/*.md against:
  - data-mined/skills_catalog.json            (names + datamined descs)
  - data-mined/characters.json  s1Skills      (datamined users / costs / flags)
  - data-mined/enrichment/skills.json         (skill_enrich)
  - data-mined/enrichment/skill_effects.json  (skill_fx)
  - data-mined/raw/masterdata/BlastForte.json (ULTIMATE: ExpendBlastStock/flags)
  - content/characters/*.md                   (cross-collection user consistency)

Replicates gen_content.py skill aggregation so a "match" = page faithful to inputs.
Writes audit/a3_skills_out.txt.
"""
from __future__ import annotations
import json, re
from collections import defaultdict
from pathlib import Path
import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RAW = DM / "raw" / "masterdata"
CONTENT = ROOT / "content"
OUT = ROOT / "audit" / "a3_skills_out.txt"

out = []
def log(*a): out.append(" ".join(str(x) for x in a))

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def fmt(n):
    if n is None: return "—"
    if isinstance(n, float) and n.is_integer(): n = int(n)
    if isinstance(n, int): return f"{n:,}"
    return str(n)

def slugify(s):
    s = s.lower(); s = re.sub(r"['’!.]", "", s); s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def props(entry): return entry[0].get("Properties") or {} if entry else {}

def parse_md(path):
    txt = path.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    if not m: return {}, txt
    return (yaml.safe_load(m.group(1)) or {}), m.group(2)

skills_catalog = load(DM / "skills_catalog.json")
chars = load(DM / "characters.json")
skill_enrich = load(DM / "enrichment" / "skills.json") or {}
skill_fx = load(DM / "enrichment" / "skill_effects.json") or {}
blastforte = load(RAW / "BlastForte.json")

# ---------- replicate gen_content aggregation ----------
byname = defaultdict(list)
skill_game_desc = {}
for sk in skills_catalog:
    if sk["name"] and sk["name"] != "None":
        byname[sk["name"]].append(sk["index"])
        if sk.get("descDatamined") and sk["name"] not in skill_game_desc:
            skill_game_desc[sk["name"]] = sk["descDatamined"]

skill_users = defaultdict(list)
for cid, c in sorted(chars.items()):
    if not c["name"]:
        continue
    for sk in c.get("s1Skills") or []:
        if sk.get("name"):
            skill_users[sk["name"]].append({
                "cid": cid,
                "character": c["fullName"] or c["name"],
                "slug": None,  # filled from char pages below
                "cost": sk.get("skillCost"),
                "flags": sk.get("flags", []),
                "slot": sk.get("slot"),
                "playable": None,
            })

# char page slug + playable map
charid_to_slug = {}
char_pages_by_name = defaultdict(set)   # display name -> set of blast1 skill names
char_playable = {}
name_to_cid = defaultdict(list)
for f in (CONTENT / "characters").glob("*.md"):
    fm, _ = parse_md(f)
    cid = fm.get("charId")
    if cid:
        charid_to_slug[cid] = fm["slug"]
        char_playable[cid] = fm.get("playable", True)
    nm = fm.get("name")
    for mv in fm.get("moveset", []) or []:
        if mv.get("type") == "blast1" and mv.get("name"):
            char_pages_by_name[nm].add(mv["name"])
for u_list in skill_users.values():
    for u in u_list:
        u["slug"] = charid_to_slug.get(u["cid"])
        u["playable"] = char_playable.get(u["cid"])

log("=" * 70)
log("SKILLS SUMMARY")
log("=" * 70)
log(f"catalog entries: {len(skills_catalog)}  unique valid names: {len(byname)}")
pages = sorted((CONTENT / "skills").glob("*.md"))
log(f"content/skills pages: {len(pages)}")
log(f"skills with >=1 datamined user: {sum(1 for n in byname if skill_users.get(n))}")
log(f"skills with 0 datamined users: {sum(1 for n in byname if not skill_users.get(n))}")

# ---------- independent: verify s1Skills cost/flags vs raw BlastForte ----------
log("")
log("Independent s1Skills vs raw BlastForte (ExpendBlastStock/flags) check:")
bf_mismatch = 0
bf_checked = 0
for cid, c in chars.items():
    for sk in c.get("s1Skills") or []:
        slot = sk.get("slot")  # 'S1'/'S2'
        slot_i = 1 if slot == "S1" else 2
        raw = props(blastforte.get(f"BlastForte{slot_i}_{cid}"))
        if not raw:
            continue
        bf_checked += 1
        raw_cost = raw.get("ExpendBlastStock")
        pd = raw.get("BlastForteParamData") or {}
        raw_flags = []
        if pd.get("bIsImpossileGuard"): raw_flags.append("unblockable")
        if pd.get("bNoAutoGuard"): raw_flags.append("no-auto-guard")
        if pd.get("bNonLockUsable"): raw_flags.append("usable-unlocked")
        if (sk.get("skillCost") or None) != (raw_cost or None) or set(sk.get("flags", [])) != set(raw_flags):
            bf_mismatch += 1
            if bf_mismatch <= 25:
                log(f"  {cid} {slot} {sk.get('name')}: parsed cost={sk.get('skillCost')} flags={sk.get('flags')} | raw cost={raw_cost} flags={raw_flags}")
log(f"  checked={bf_checked} mismatches={bf_mismatch}")

# ---------- per-skill expected values (mirror gen_content) ----------
def expected(name):
    e = dict(skill_fx.get(name, {}))
    e.update({k: v for k, v in (skill_enrich.get(name) or {}).items() if v})
    users = skill_users.get(name, [])
    mined_costs = sorted({u["cost"] for u in users if u["cost"] is not None})
    cost = (mined_costs[0] if len(mined_costs) == 1
            else e.get("skillCost") if not mined_costs else None)
    game_desc = skill_game_desc.get(name)
    front_cost = cost if cost is not None else e.get("skillCost")
    return {
        "skillCost": front_cost,
        "effect": e.get("effect") or game_desc,
        "durationSec": e.get("durationSec"),
        "users": [u["character"] for u in users] or e.get("users", []),
        "userCount": len(users) or None,
        "tier": e.get("tier"),
        "confidence": e.get("confidence", "datamined"),
        "_mined_costs": mined_costs,
        "_users_obj": users,
        "_game_desc": game_desc,
        "_e_effect": e.get("effect"),
        "_e_users": e.get("users", []),
        "_has_body": bool(e.get("body")),
    }

findings = defaultdict(list)
TIERS = {"S", "A", "B", "C", "D", "situational"}

for f in pages:
    slug = f.stem
    fm, body = parse_md(f)
    name = fm.get("name")
    if name not in byname:
        findings["unknown_skill"].append(f"{slug}: name '{name}' not in catalog byname")
        continue
    exp = expected(name)
    # slug check
    if slug != slugify(name):
        findings["slug"].append(f"{slug}: slug != slugify('{name}')={slugify(name)}")
    # skillCost
    if (fm.get("skillCost") if fm.get("skillCost") is not None else None) != (exp["skillCost"] if exp["skillCost"] is not None else None):
        findings["skillCost"].append(f"{slug}: page={fm.get('skillCost')} expected={exp['skillCost']} (mined={exp['_mined_costs']})")
    # effect provenance
    pe = fm.get("effect")
    if pe != exp["effect"]:
        findings["effect_mismatch"].append(f"{slug}: page effect != expected (e_effect/game_desc)")
    if pe and not exp["_e_effect"] and not exp["_game_desc"]:
        findings["effect_fabricated"].append(f"{slug}: effect present but NO enrichment.effect and NO datamined game_desc")
    # durationSec
    if (fm.get("durationSec")) != exp["durationSec"]:
        findings["durationSec"].append(f"{slug}: page={fm.get('durationSec')} expected={exp['durationSec']}")
    # users
    pu = fm.get("users", []) or []
    if list(pu) != list(exp["users"]):
        findings["users"].append(f"{slug}: page users({len(pu)})={pu} expected({len(exp['users'])})={exp['users']}")
    # userCount correctness + internal consistency
    if fm.get("userCount") != exp["userCount"]:
        findings["userCount_vs_expected"].append(f"{slug}: page userCount={fm.get('userCount')} expected={exp['userCount']}")
    # consistency: userCount vs len(users) shown on the page
    if pu and fm.get("userCount") is None:
        findings["userCount_none_but_users"].append(f"{slug}: userCount absent but users[] has {len(pu)} entries ({'enrichment-sourced' if not exp['_users_obj'] else 'datamined'})")
    if fm.get("userCount") is not None and fm.get("userCount") != len(pu):
        findings["userCount_neq_len"].append(f"{slug}: userCount={fm.get('userCount')} != len(users)={len(pu)}")
    # duplicate datamined users (same char in S1 & S2)
    cids = [u["cid"] for u in exp["_users_obj"]]
    if len(cids) != len(set(cids)):
        dup = [c for c in set(cids) if cids.count(c) > 1]
        findings["duplicate_user"].append(f"{slug}: same character listed twice (S1+S2): {dup}")
    # non-playable users counted
    npl = [u["character"] for u in exp["_users_obj"] if u["playable"] is False]
    if npl:
        findings["nonplayable_user"].append(f"{slug}: non-playable entries counted as users: {npl}")
    # tier validity
    t = fm.get("tier")
    if t is not None and t not in TIERS:
        findings["tier_invalid"].append(f"{slug}: tier='{t}' not in {TIERS}")
    if t != exp["tier"]:
        findings["tier_mismatch"].append(f"{slug}: page tier={t} expected={exp['tier']}")
    # confidence
    if fm.get("confidence") != exp["confidence"]:
        findings["confidence"].append(f"{slug}: page={fm.get('confidence')} expected={exp['confidence']}")
    # per-user table vs datamined users
    tbl_rows = re.findall(r"^\| (.+?) \| (.+?) \| (.+?) \|$", body, re.M)
    tbl_rows = [r for r in tbl_rows if r[0] not in ("Character",) and not set(r[0]) <= {"-"}]
    if exp["_users_obj"]:
        exp_rows = []
        for u in exp["_users_obj"]:
            disp = u["character"]
            exp_rows.append((disp, fmt(u["cost"]), ", ".join(u["flags"]) or "—"))
        # compare names/costs/flags (strip wikilink syntax from page cell)
        got = []
        for r in tbl_rows:
            cn = re.sub(r"\[\[[^\|\]]*\\?\|?", "", r[0]).replace("]]", "").strip()
            got.append((cn, r[1].strip(), r[2].strip()))
        if got != exp_rows:
            findings["user_table"].append(f"{slug}: per-user table mismatch\n      exp={exp_rows}\n      got={got}")
    else:
        # no datamined users: expect story/legacy note OR enrichment body
        if "no current roster user" not in body and not exp["_has_body"] and "## " not in body:
            findings["nouser_unhandled"].append(f"{slug}: 0 users, no story/legacy note and no enrichment body")
    # cross-collection: datamined users' char pages list this skill
    if exp["_users_obj"]:
        for u in exp["_users_obj"]:
            if name not in char_pages_by_name.get(u["character"], set()):
                findings["char_page_missing_skill"].append(f"{slug}: user '{u['character']}' char page has no blast1 '{name}'")

log("")
log("FINDINGS BY CATEGORY:")
for k, v in sorted(findings.items(), key=lambda x: -len(x[1])):
    log(f"  [{k}] count={len(v)}")
    for line in v[:30]:
        log(f"      {line}")

# distributions
log("")
log("skillCost provenance distribution:")
prov = defaultdict(int)
for name in byname:
    exp = expected(name)
    mc = exp["_mined_costs"]
    if len(mc) == 1: prov["datamined_single"] += 1
    elif len(mc) >= 2: prov["conflicting_mined->enrichment_fallback"] += 1
    elif exp["skillCost"] is not None: prov["enrichment_only"] += 1
    else: prov["null"] += 1
for k, v in prov.items():
    log(f"  {k}: {v}")

# list conflicting-mined-cost skills (cost shown may be misleading)
log("")
log("Skills with CONFLICTING datamined costs (page falls back to enrichment/null):")
for name in sorted(byname):
    exp = expected(name)
    if len(exp["_mined_costs"]) >= 2:
        per = [(u["character"], u["cost"]) for u in exp["_users_obj"]]
        log(f"  {name}: mined_costs={exp['_mined_costs']} page_skillCost={exp['skillCost']} conf={exp['confidence']}")

OUT.write_text("\n".join(out), encoding="utf-8")
print("\n".join(out))
print(f"\n[full output -> {OUT}]")
