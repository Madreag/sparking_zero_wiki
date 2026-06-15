"""Audit Agent 2 — blasts data-accuracy probe (READ ONLY).

Cross-checks all 453 content/blasts/*.md against the source of truth:
  data-mined/blast_index.json  (parsed) ->  re-derived expected page
  data-mined/raw/masterdata/BulletSetting/BulletParam.json + Combatives/<cid>.json (raw) -> damage honesty
  content/characters/*.md moveset  -> cross-collection consistency

Does NOT modify any wiki file. Writes only audit/a2_findings.json + prints a report.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path

import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RAW = DM / "raw" / "masterdata"
CONTENT = ROOT / "content"

findings: list[dict] = []


def add(sev: str, check: str, slug: str, msg: str, evidence: str = ""):
    findings.append(
        {"sev": sev, "check": check, "slug": slug, "msg": msg, "evidence": evidence}
    )


# ---------- replicate generator helpers exactly ----------
def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def slot_of_action(action: str) -> str | None:
    if "SPM1" in action:
        return "SPM1"
    if "SPM2" in action:
        return "SPM2"
    if "ULT" in action or "UB" in action:
        return "ULT"
    return None


def best_damage(move: dict):
    dmg = chip = hits = None
    for b in move.get("bullets") or []:
        cand = max(x for x in (b.get("beamPower"), b.get("power"), 0) if x is not None)
        if cand and (dmg is None or cand > dmg):
            dmg = cand
            chip = b.get("beamChip") or b.get("chip")
            hits = b.get("multiHit")
    melee = [p for p in (move.get("combatives") or {}).get("meleePowers", []) if p]
    if melee and (dmg is None or max(melee) > dmg):
        dmg = max(melee)
        chip = None
        hits = None
    return dmg, chip, hits


def fmt(n) -> str:
    if n is None:
        return "—"
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if isinstance(n, int):
        return f"{n:,}"
    return str(n)


def props(entry) -> dict:
    if not entry:
        return {}
    return entry[0].get("Properties") or {}


# ---------- load source-of-truth ----------
blast_index = json.load(open(DM / "blast_index.json", encoding="utf-8"))
chars = json.load(open(DM / "characters.json", encoding="utf-8"))

# rebuild cid->slug exactly like gen_content.py
slugs: dict[str, str] = {}
used: dict[str, str] = {}
for cid, c in sorted(chars.items()):
    if not c["name"]:
        continue
    label = c["fullName"] or c["name"]
    s = slugify(label)
    if s in used and used[s] != cid:
        s = f"{s}-{cid.replace('_', '-')}"
    used[s] = cid
    slugs[cid] = s

# ---------- read all blast pages ----------
blast_files = sorted((CONTENT / "blasts").glob("*.md"))
pages: dict[str, dict] = {}
for f in blast_files:
    raw = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---\n(.*)$", raw, re.S)
    if not m:
        add("HIGH", "frontmatter", f.stem, "no parseable frontmatter")
        continue
    fm = yaml.safe_load(m.group(1))
    pages[f.stem] = {"front": fm, "body": m.group(2), "file": f.name}

# ---------- read all character pages (ground-truth slugs + movesets) ----------
char_pages: dict[str, dict] = {}  # slug -> {name, charId, moveset}
cid_to_charpage: dict[str, str] = {}
for f in sorted((CONTENT / "characters").glob("*.md")):
    raw = f.read_text(encoding="utf-8")
    m = re.match(r"^---\n(.*?)\n---", raw, re.S)
    if not m:
        continue
    fm = yaml.safe_load(m.group(1))
    char_pages[fm["slug"]] = fm
    if fm.get("charId"):
        cid_to_charpage[fm["charId"]] = fm["slug"]

# ---------- raw bullets index (replicate parse_data char_bullets) ----------
raw_bullets = json.load(
    open(RAW / "BulletSetting" / "BulletParam.json", encoding="utf-8")
)
char_bullets: dict[str, dict[str, list[dict]]] = defaultdict(lambda: defaultdict(list))
for k, v in raw_bullets.items():
    mm = re.match(r"BulletParam_(\d{4}_\d{2})_(act.+)$", k)
    if not mm:
        continue
    cid, action = mm.group(1), mm.group(2)
    slot = slot_of_action(action)
    if not slot:
        continue
    p = props(v)
    if not any(p.get(x) for x in ("Power", "BeamPower", "Shave", "BeamShave")):
        continue
    char_bullets[cid][slot].append(
        {
            "action": action,
            "power": p.get("Power"),
            "chip": p.get("Shave"),
            "beamPower": p.get("BeamPower"),
            "beamChip": p.get("BeamShave"),
            "multiHit": p.get("CollisionRevibeNum"),
        }
    )

# ---------- raw combatives meleePowers per cid+slot (replicate comb_for) ----------
_comb_cache: dict[str, dict[str, list[int]]] = {}


def raw_melee(cid: str) -> dict[str, list[int]]:
    if cid in _comb_cache:
        return _comb_cache[cid]
    out: dict[str, list[int]] = defaultdict(list)
    f = RAW / "Combatives" / f"{cid}.json"
    if f.exists():
        d = json.load(open(f, encoding="utf-8"))
        for k, v in d.items():
            mm = re.match(r"Combatives(?:SubParam)?_\d{4}_\d{2}_(act.+)$", k)
            if not mm:
                continue
            action = mm.group(1)
            slot = slot_of_action(action)
            if not slot:
                continue
            p = props(v)
            if "Power" in p:
                out[slot].append(p["Power"])
    _comb_cache[cid] = out
    return out


def raw_best_damage(cid: str, slot: str):
    """Recompute (dmg, chip, hits, source) directly from RAW files."""
    move = {
        "bullets": char_bullets.get(cid, {}).get(slot, []),
        "combatives": {"meleePowers": raw_melee(cid).get(slot, [])},
    }
    dmg, chip, hits = best_damage(move)
    # determine source EXACTLY as the generator decides (melee overrides only on strict >)
    src = None
    if dmg is not None:
        bull_max = 0
        for b in move["bullets"]:
            c = max(x for x in (b.get("beamPower"), b.get("power"), 0) if x is not None)
            bull_max = max(bull_max, c)
        melee_nz = [p for p in move["combatives"]["meleePowers"] if p]
        melee_overrides = bool(melee_nz) and (bull_max == 0 or max(melee_nz) > bull_max)
        src = "combatives/melee" if melee_overrides else "bulletparam"
    return dmg, chip, hits, src


# ============================================================
# PART A: regenerate each blast page from blast_index and diff
# ============================================================
name_class_pairs = {(b["name"], b["class"]) for b in blast_index}
bslugs_seen: dict[str, str] = {}
dropped: list[tuple[str, str, str]] = []  # (slug, name, class) dropped by dedup
expected_pages: dict[str, dict] = {}

for b in blast_index:
    s = f"{slugify(b['name'])}-{b['class']}"
    if s in bslugs_seen:
        dropped.append((s, b["name"], b["class"]))
        continue
    bslugs_seen[s] = b["name"]

    users = []
    for u in sorted(b["users"], key=lambda x: x["character"]):
        dmg, chip, hits = best_damage(u)
        ue = {
            "character": u["character"],
            "characterSlug": slugs.get(u["charId"]),
            "kiCost": u.get("kiCost"),
            "triggerKiCost": u.get("triggerKiCost"),
            "damage": dmg,
            "chip": chip,
            "hits": hits,
            "category": u.get("category"),
            "tags": [t for t in (u.get("tags") or []) if t != "Ki Required"],
            "notes": u.get("slot"),
            "_charId": u["charId"],
        }
        users.append(ue)
    costs = sorted({u["kiCost"] for u in b["users"] if u.get("kiCost") is not None})
    cats = Counter(u["category"] for u in users if u["category"])
    page_cat = cats.most_common(1)[0][0] if cats else None
    all_tags = sorted({t for u in users for t in u["tags"]})
    dmgs = sorted({u["damage"] for u in users if u["damage"]})
    other_class = "ultimate" if b["class"] == "super" else "super"
    sibling = (
        f"{slugify(b['name'])}-{other_class}"
        if (b["name"], other_class) in name_class_pairs
        else None
    )
    expected_pages[s] = {
        "name": b["name"],
        "class": b["class"],
        "category": page_cat,
        "users": users,
        "costs": costs,
        "all_tags": all_tags,
        "dmgs": dmgs,
        "sibling": sibling,
    }

# Coverage: pages present vs expected
exp_slugs = set(expected_pages)
got_slugs = set(pages)
missing = exp_slugs - got_slugs
extra = got_slugs - exp_slugs
for s in sorted(missing):
    add("HIGH", "coverage", s, "blast_index has entry but no content page (dedup-dropped or unwritten)")
for s in sorted(extra):
    add("HIGH", "coverage", s, "content page has no matching blast_index entry (orphan/hand-added)")

# dedup-drop detail
for s, nm, cl in dropped:
    keeper = bslugs_seen.get(s)
    add(
        "HIGH",
        "slug-dedup",
        s,
        f"blast '{nm}' ({cl}) collides on slug with kept '{keeper}' -> page dropped, its users orphaned",
        evidence=f"slug={s}",
    )

USER_FIELDS = ["character", "characterSlug", "kiCost", "triggerKiCost", "damage", "chip", "hits", "category", "tags", "notes"]

def norm_user(u: dict) -> dict:
    out = {}
    for k in USER_FIELDS:
        v = u.get(k)
        if v is None:
            continue
        if k == "tags" and not v:
            continue
        out[k] = v
    return out


damage_users = 0  # count of user rows asserting damage on pages
traced_ok = 0
honesty_violations = 0
melee_label_pages = set()

for s, exp in expected_pages.items():
    if s not in pages:
        continue
    pg = pages[s]
    front = pg["front"]
    body = pg["body"]

    # class / name
    if front.get("name") != exp["name"]:
        add("MEDIUM", "field", s, f"name mismatch: page={front.get('name')!r} idx={exp['name']!r}")
    if front.get("class") != exp["class"]:
        add("HIGH", "field", s, f"class mismatch: page={front.get('class')!r} idx={exp['class']!r}")

    # category (most-common among users)
    if front.get("category") != exp["category"]:
        add("MEDIUM", "category", s, f"page category={front.get('category')!r} expected most-common={exp['category']!r}")

    # users
    pg_users = front.get("users") or []
    exp_users = [norm_user(u) for u in exp["users"]]
    if len(pg_users) != len(exp_users):
        add("HIGH", "users", s, f"user count {len(pg_users)} != expected {len(exp_users)}")
    for i, (pu, eu) in enumerate(zip(pg_users, exp_users)):
        pun = {k: pu.get(k) for k in USER_FIELDS if pu.get(k) is not None and not (k == "tags" and not pu.get(k))}
        if pun != eu:
            diffs = []
            allk = set(pun) | set(eu)
            for k in allk:
                if pun.get(k) != eu.get(k):
                    diffs.append(f"{k}: page={pun.get(k)!r} exp={eu.get(k)!r}")
            add("HIGH", "users", s, f"user#{i} ({eu.get('character')}) mismatch: " + "; ".join(diffs))

    # "Ki Required" must never appear
    for u in pg_users:
        if "Ki Required" in (u.get("tags") or []):
            add("HIGH", "ki-required", s, f"user {u.get('character')} still has 'Ki Required' tag")
    if "Ki Required" in body:
        add("MEDIUM", "ki-required", s, "body text contains 'Ki Required'")

    # body datamined-power line vs dmgs
    has_dp_line = "Datamined power:" in body
    if exp["dmgs"] and not has_dp_line:
        add("MEDIUM", "body", s, f"expected Datamined power line for {exp['dmgs']} but missing")
    if not exp["dmgs"] and has_dp_line:
        add("HIGH", "body-honesty", s, "body asserts 'Datamined power' but no user has datamined damage")
    if exp["dmgs"]:
        want = f"**Datamined power: {', '.join(fmt(d) for d in exp['dmgs'])}**"
        if want not in body:
            add("MEDIUM", "body", s, f"Datamined power value mismatch; expected {want!r}")

    # sibling line
    if exp["sibling"]:
        if exp["sibling"] not in body:
            add("MEDIUM", "sibling", s, f"expected sibling link [[{exp['sibling']}]] missing in body")
        elif exp["sibling"] not in expected_pages and exp["sibling"] not in pages:
            add("HIGH", "sibling", s, f"sibling link target {exp['sibling']} does not exist as a page")
    # sibling target existence (independent)
    if exp["sibling"] and exp["sibling"] not in pages:
        add("HIGH", "sibling", s, f"sibling target page {exp['sibling']}.md not found on disk")

    # tag bullets in body
    for t in exp["all_tags"]:
        if f"**{t}**" not in body:
            add("LOW", "body", s, f"tag '{t}' missing from body bullet list")

    # ---- damage honesty trace to RAW ----
    for u in pg_users:
        d = u.get("damage")
        if not d:
            continue
        damage_users += 1
        cid = None
        # find charId from expected (we attached _charId)
        for eu in exp["users"]:
            if eu["character"] == u.get("character") and eu.get("characterSlug") == u.get("characterSlug"):
                cid = eu["_charId"]
                break
        if not cid:
            add("MEDIUM", "honesty", s, f"cannot resolve charId for user {u.get('character')} to trace damage {d}")
            continue
        slot = u.get("notes")  # slot stored in notes
        rdmg, rchip, rhits, rsrc = raw_best_damage(cid, slot)
        if rdmg is None:
            honesty_violations += 1
            add("BLOCKER", "honesty", s, f"user {u.get('character')} ({cid}/{slot}) page damage={d} but RAW has NO override (inherits class default)")
        elif rdmg != d:
            add("HIGH", "honesty", s, f"user {u.get('character')} ({cid}/{slot}) page damage={d} != raw recompute={rdmg} (src {rsrc})")
        else:
            traced_ok += 1
            if rsrc == "combatives/melee":
                melee_label_pages.add(s)
        # hits/chip rule: melee-derived must have no hits/chip
        if rsrc == "combatives/melee":
            if u.get("hits") is not None:
                add("MEDIUM", "hits", s, f"user {u.get('character')} melee-derived dmg but hits={u.get('hits')} present")
            if u.get("chip") is not None:
                add("MEDIUM", "chip", s, f"user {u.get('character')} melee-derived dmg but chip={u.get('chip')} present")
        # hits must equal a bullet multiHit when present
        if u.get("hits") is not None:
            mhs = {b.get("multiHit") for b in char_bullets.get(cid, {}).get(slot, [])}
            if u.get("hits") not in mhs:
                add("MEDIUM", "hits", s, f"user {u.get('character')} hits={u.get('hits')} not found among raw multiHit {mhs}")

# body "projectile/beam values" wording on melee-only pages
for s in sorted(melee_label_pages):
    # only flag if the page's datamined dmg is purely melee-derived (rush/melee)
    cat = pages[s]["front"].get("category")
    add("LOW", "wording", s, f"datamined power is melee/Combatives-derived (category {cat!r}) but body calls it 'projectile/beam values'")

# ============================================================
# PART C: cross-collection (blast users <-> character movesets)
# ============================================================
# Build character moveset index: slug -> {(name, type)} for blast2/ultimate
char_moves: dict[str, set] = {}
char_move_names: dict[str, list] = {}
for slug, fm in char_pages.items():
    ms = set()
    names = []
    for mv in fm.get("moveset") or []:
        if mv.get("type") in ("blast2", "ultimate"):
            ms.add((mv["name"], mv["type"]))
            names.append((mv["name"], mv["type"]))
    char_moves[slug] = ms
    char_move_names[slug] = names

CLS_TO_TYPE = {"super": "blast2", "ultimate": "ultimate"}
xcoll_user_missing = 0  # blast lists a user whose char page lacks the move
xcoll_char_missing = 0  # char move with no blast page / not a user

# (a) every blast page user must appear in that character's moveset
for s, pg in pages.items():
    front = pg["front"]
    cls = front.get("class")
    mname = front.get("name")
    mtype = CLS_TO_TYPE.get(cls)
    for u in front.get("users") or []:
        cslug = u.get("characterSlug")
        if cslug not in char_pages:
            add("HIGH", "xcoll", s, f"user {u.get('character')} -> characterSlug '{cslug}' has NO character page")
            continue
        if (mname, mtype) not in char_moves.get(cslug, set()):
            xcoll_user_missing += 1
            add("MEDIUM", "xcoll", s, f"user {u.get('character')} ({cslug}) listed but char page moveset lacks {mtype} '{mname}'")

# (b) every character blast2/ultimate must have a blast page listing them
blast_user_set: dict[tuple, set] = defaultdict(set)  # (name, class) -> set(charSlug)
for s, pg in pages.items():
    front = pg["front"]
    cls = front.get("class")
    for u in front.get("users") or []:
        blast_user_set[(front.get("name"), cls)].add(u.get("characterSlug"))

TYPE_TO_CLS = {"blast2": "super", "ultimate": "ultimate"}
for slug, names in char_move_names.items():
    for (mname, mtype) in names:
        cls = TYPE_TO_CLS[mtype]
        exp_slug = f"{slugify(mname)}-{cls}"
        if exp_slug not in pages:
            xcoll_char_missing += 1
            add("HIGH", "xcoll", slug, f"char has {mtype} '{mname}' but no blast page '{exp_slug}' exists")
        elif slug not in blast_user_set.get((mname, cls), set()):
            # maybe name differs (short vs full) - check by slug membership
            xcoll_char_missing += 1
            add("MEDIUM", "xcoll", slug, f"char has {mtype} '{mname}' but is not listed as a user on '{exp_slug}'")

# ============================================================
# PART D: kiCost sanity
# ============================================================
SUPER_OK = {10000, 20000, 30000}
for s, pg in pages.items():
    front = pg["front"]
    cls = front.get("class")
    for u in front.get("users") or []:
        ki = u.get("kiCost")
        if ki is None:
            add("LOW", "kicost", s, f"user {u.get('character')} has no kiCost")
            continue
        if cls == "super" and ki not in SUPER_OK:
            add("LOW", "kicost", s, f"super user {u.get('character')} kiCost={ki} outside 10k/20k/30k")
        if cls == "ultimate" and ki != 50000:
            add("LOW", "kicost", s, f"ultimate user {u.get('character')} kiCost={ki} != 50,000")

# ============================================================
# SUMMARY
# ============================================================
sev_order = ["BLOCKER", "HIGH", "MEDIUM", "LOW", "NIT"]
counts = Counter(f["sev"] for f in findings)
print("=" * 70)
print("AUDIT AGENT 2 — BLASTS PROBE RESULTS")
print("=" * 70)
print(f"blast pages on disk        : {len(pages)}")
print(f"blast_index entries        : {len(blast_index)}")
print(f"expected pages (post-dedup): {len(expected_pages)}")
print(f"dedup-dropped blasts       : {len(dropped)}")
print(f"user rows asserting damage : {damage_users}")
print(f"  traced OK to raw override: {traced_ok}")
print(f"  HONESTY VIOLATIONS       : {honesty_violations}")
print(f"melee-derived dmg pages    : {len(melee_label_pages)}")
print(f"xcoll user->char missing   : {xcoll_user_missing}")
print(f"xcoll char->blast missing  : {xcoll_char_missing}")
print("-" * 70)
for sev in sev_order:
    print(f"{sev:8}: {counts.get(sev,0)}")
print("-" * 70)
by_check = Counter((f["sev"], f["check"]) for f in findings)
for (sev, check), n in sorted(by_check.items(), key=lambda x: (sev_order.index(x[0][0]), -x[1])):
    print(f"  {sev:8} {check:14} {n}")

json.dump(
    {"counts": counts, "findings": findings,
     "stats": {"pages": len(pages), "idx": len(blast_index), "expected": len(expected_pages),
               "dropped": dropped, "damage_users": damage_users, "traced_ok": traced_ok,
               "honesty_violations": honesty_violations, "melee_pages": sorted(melee_label_pages),
               "xcoll_user_missing": xcoll_user_missing, "xcoll_char_missing": xcoll_char_missing}},
    open(ROOT / "audit" / "a2_findings.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False,
)
print("\nwrote audit/a2_findings.json")
