"""Audit Agent 3 — transformations probe (READ-ONLY).

Cross-checks content/transformations/*.md against:
  - data-mined/transformations.json        (parsed edges)
  - data-mined/raw/masterdata/CharacterData.json  (ULTIMATE source)
  - data-mined/characters.json             (stat deltas + moveset diff)
  - data-mined/enrichment/characters.json  (dp)

Replicates gen_content.py slug/stat/kit logic so a "match" means the page is
faithful to its generator inputs; raw-vs-parsed catches stale tables.
Writes audit/a3_tf_out.txt and prints a summary.
"""
from __future__ import annotations
import json, re, sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RAW = DM / "raw" / "masterdata"
CONTENT = ROOT / "content"
OUT = ROOT / "audit" / "a3_tf_out.txt"

out_lines: list[str] = []
def log(*a):
    out_lines.append(" ".join(str(x) for x in a))

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

def fmt(n) -> str:
    if n is None:
        return "—"
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if isinstance(n, int):
        return f"{n:,}"
    return str(n)

def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")

def props(entry) -> dict:
    if not entry:
        return {}
    return entry[0].get("Properties") or {}

# ---------- load sources ----------
transforms = load(DM / "transformations.json")
chars = load(DM / "characters.json")
enrich = load(DM / "enrichment" / "characters.json")
chardata = load(RAW / "CharacterData.json")

# ---------- frontmatter parsing for content pages ----------
def parse_md(path: Path):
    txt = path.read_text(encoding="utf-8")
    import yaml
    m = re.match(r"^---\n(.*?)\n---\n?(.*)$", txt, re.S)
    if not m:
        return {}, txt
    fm = yaml.safe_load(m.group(1)) or {}
    return fm, m.group(2)

# ---------- global slug index (for wikilink resolution) ----------
all_slugs: set[str] = set()
for sub in CONTENT.iterdir():
    if sub.is_dir():
        for f in sub.glob("*.md"):
            all_slugs.add(f.stem)
char_slugs = {f.stem for f in (CONTENT / "characters").glob("*.md")}

# ---------- replicate parse_data raw edge extraction ----------
def raw_edges():
    edges = []
    for key, val in chardata.items():
        if not key.startswith("CharacterData_"):
            continue
        cid = key[len("CharacterData_"):]
        rec = props(val).get("CharacterDataAssetRecord") or {}
        battle = rec.get("BattleAssets") or {}
        def edge(entry, kind):
            tgt = (entry.get("ChangeCharacter") or {}).get("Key")
            if not tgt:
                return None
            stock = entry.get("ConsumeBlastStock")
            same_base = tgt.split("_")[0] == cid.split("_")[0]
            rk = "revert" if (kind == "transform" and stock == 0 and same_base) else kind
            return {
                "from": cid, "to": tgt, "kind": rk,
                "consumeBlastStock": stock,
                "hpRecovery": entry.get("HpRecovery"),
                "addMaxHp": entry.get("AddMaxHP"),
                "coolTimeSec": entry.get("CoolTime"),
                "noHealAfterSecondUse": entry.get("bDisableRecoveryAfterTheSecondTime"),
            }
        for fld, knd in (("FormChange", "transform"), ("Fusion", "fusion"), ("Potara", "potara")):
            v = battle.get(fld)
            vs = v if isinstance(v, list) else ([v] if v else [])
            for x in vs:
                if x:
                    e = edge(x, knd)
                    if e:
                        edges.append(e)
    return edges

raw = raw_edges()
raw_by_pair = {(e["from"], e["to"]): e for e in raw}
parsed_by_pair = {(e["from"], e["to"]): e for e in transforms}

log("=" * 70)
log("RAW vs PARSED transformations.json")
log("=" * 70)
log(f"raw edges: {len(raw)}  parsed edges: {len(transforms)}")

# heal counts in parsed table
heal_zero = sum(1 for e in transforms if (e.get("hpRecovery") or 0) == 0)
heal_pos = sum(1 for e in transforms if (e.get("hpRecovery") or 0) > 0)
log(f"PARSED transformations.json hpRecovery: zero={heal_zero}  positive={heal_pos}  total={len(transforms)}")
raw_zero = sum(1 for e in raw if (e.get("hpRecovery") or 0) == 0)
raw_pos = sum(1 for e in raw if (e.get("hpRecovery") or 0) > 0)
log(f"RAW CharacterData.json   hpRecovery: zero={raw_zero}  positive={raw_pos}  total={len(raw)}")

# direct field mismatches raw vs parsed
mismatch = []
for pair, pe in parsed_by_pair.items():
    re_ = raw_by_pair.get(pair)
    if not re_:
        mismatch.append((pair, "MISSING IN RAW", pe.get("hpRecovery"), None))
        continue
    for fld in ("hpRecovery", "consumeBlastStock", "addMaxHp", "coolTimeSec", "kind"):
        pv, rv = pe.get(fld), re_.get(fld)
        if (pv or 0) != (rv or 0) if fld in ("hpRecovery", "addMaxHp", "coolTimeSec", "consumeBlastStock") else pv != rv:
            mismatch.append((pair, fld, pv, rv))
log(f"raw-vs-parsed field mismatches: {len(mismatch)}")
for pair, fld, pv, rv in mismatch[:60]:
    fn = chars.get(pair[0], {}).get("fullName") or chars.get(pair[0], {}).get("name") or pair[0]
    tn = chars.get(pair[1], {}).get("fullName") or chars.get(pair[1], {}).get("name") or pair[1]
    log(f"  {pair} {fn}->{tn}: {fld} parsed={pv} raw={rv}")

# list every positive-heal transform with raw confirmation
log("")
log("Positive-heal transforms (parsed) and raw confirmation:")
for e in transforms:
    if (e.get("hpRecovery") or 0) > 0:
        r = raw_by_pair.get((e["from"], e["to"]), {})
        ok = "OK" if (r.get("hpRecovery") or 0) == e["hpRecovery"] else f"RAW={r.get('hpRecovery')}"
        log(f"  {e['fromName']} -> {e['toName']}: parsed hpRecovery={fmt(e['hpRecovery'])} kind={e['kind']} [{ok}]")

# ---------- replicate gen_content slug assignment ----------
groups = defaultdict(list)
for cid, c in chars.items():
    groups[c.get("baseId")].append(c)

def resolved_hp(c):
    if c.get("hp") is not None:
        return c["hp"], False
    for sib in groups.get(c.get("baseId"), []):
        if sib.get("hp") is not None:
            return sib["hp"], True
    return None, False

slugs = {cid: f.stem for cid in chars}  # placeholder; real char slug below
# real char slug map: read character pages charId frontmatter
charid_to_slug = {}
for f in (CONTENT / "characters").glob("*.md"):
    fm, _ = parse_md(f)
    if fm.get("charId"):
        charid_to_slug[fm["charId"]] = fm["slug"]

# assign transformation slug -> edge, replicating gen_content loop order
edge_by_slug = {}
tr_used = set()
for t in transforms:
    if t["kind"] == "revert" or not t.get("toName") or not t.get("fromName"):
        continue
    s = slugify(f"{t['fromName']}-to-{t['toName']}")
    if s in tr_used:
        s2 = f"{s}-{t['kind']}"
        if s2 in tr_used:
            continue
        s = s2
    tr_used.add(s)
    edge_by_slug[s] = t

log("")
log("=" * 70)
log("PAGE-LEVEL CHECKS")
log("=" * 70)
pages = sorted((CONTENT / "transformations").glob("*.md"))
log(f"content/transformations pages: {len(pages)}  generator non-revert slugs: {len(edge_by_slug)}")

# revert leak: any page whose slug maps to a revert edge?
revert_pairs = {(e["from"], e["to"]) for e in transforms if e["kind"] == "revert"}

findings = defaultdict(list)
recomputed = 0
heal_pages_pos = 0
heal_pages_zero = 0

def kit(c):
    out = []
    for sk in c.get("s1Skills") or []:
        if sk.get("name"):
            cost = f" ({fmt(sk['skillCost'])} stocks)" if sk.get("skillCost") is not None else ""
            out.append(f"S{1 if sk['slot']=='S1' else 2}: {sk['name']}{cost}")
    for sp in c.get("supers") or []:
        if sp.get("name"):
            out.append(f"{sp['slot']}: {sp['name']} ({fmt(sp['kiCost'])} ki)")
    u = c.get("ultimate") or {}
    if u.get("name"):
        out.append(f"ULT: {u['name']} ({fmt(u.get('kiCost'))} ki)")
    return out

def expected_hprule(t):
    s = f"HP recovery on change: {fmt(t.get('hpRecovery'))}"
    if t.get("addMaxHp"):
        s += f" · adds max HP: {fmt(t.get('addMaxHp'))}"
    if t.get("coolTimeSec") is not None:
        s += f" · cooldown {fmt(t.get('coolTimeSec'))}s"
    if t.get("noHealAfterSecondUse"):
        s += " · no HP recovery after 2nd use"
    return s

def expected_statchanges(t):
    cf, ct = chars.get(t["from"]) or {}, chars.get(t["to"]) or {}
    hp_f, _ = resolved_hp(cf) if cf else (None, False)
    hp_t, _ = resolved_hp(ct) if ct else (None, False)
    rows = []
    def dr(label, a, b, unit=""):
        if a is None or b is None:
            return
        if a == b:
            rows.append((label, f"{fmt(a)}{unit}", f"{fmt(b)}{unit}", "no change"))
        else:
            sign = "+" if (b - a) > 0 else ""
            rows.append((label, f"{fmt(a)}{unit}", f"{fmt(b)}{unit}", f"{sign}{fmt(b-a)}{unit}"))
    dr("Health (max)", hp_f, hp_t)
    dr("Ki charge speed", cf.get("kiChargeSpeed"), ct.get("kiChargeSpeed"))
    dr("Ki auto-recovery", cf.get("kiAutoRecovery"), ct.get("kiAutoRecovery"), "/s")
    dr("Sparking gauge charge", cf.get("sparkingGaugeChargeSpeed"), ct.get("sparkingGaugeChargeSpeed"))
    dr("Pre-Sparking gauge decay", cf.get("preSparkingGaugeDecreaseSpeed"), ct.get("preSparkingGaugeDecreaseSpeed"), "/s")
    sc = "; ".join(f"{a}: {b} → {c2} ({d})" for a, b, c2, d in rows if d != "no change") \
        or "No flat stat changes — this change is moveset/property-based"
    return sc, rows

for f in pages:
    slug = f.stem
    fm, body = parse_md(f)
    t = edge_by_slug.get(slug)
    if not t:
        findings["page_no_edge"].append(f"{slug}: no matching non-revert edge in transformations.json")
        continue
    if (t["from"], t["to"]) in revert_pairs:
        findings["revert_leak"].append(f"{slug}: maps to a REVERT edge")
    # cost
    if fm.get("cost") != t.get("consumeBlastStock"):
        findings["cost"].append(f"{slug}: page cost={fm.get('cost')} vs data consumeBlastStock={t.get('consumeBlastStock')}")
    # hpRule
    exp_hr = expected_hprule(t)
    if (fm.get("hpRule") or "") != exp_hr:
        findings["hpRule"].append(f"{slug}: page hpRule='{fm.get('hpRule')}' vs expected '{exp_hr}'")
    # body HP recovery line
    mhp = re.search(r"HP recovery on change \| ([^|]+) \|", body)
    body_hp = mhp.group(1).strip() if mhp else None
    if body_hp is not None:
        if body_hp != fmt(t.get("hpRecovery")):
            findings["body_hp"].append(f"{slug}: body HP recovery='{body_hp}' vs data={fmt(t.get('hpRecovery'))}")
    if (t.get("hpRecovery") or 0) > 0:
        heal_pages_pos += 1
    else:
        heal_pages_zero += 1
    # statChanges recompute
    exp_sc, rows = expected_statchanges(t)
    recomputed += 1
    if (fm.get("statChanges") or "") != exp_sc:
        findings["statChanges"].append(f"{slug}: page='{fm.get('statChanges')}' vs recomputed='{exp_sc}'")
    # dp
    if fm.get("dpFrom") != enrich.get(t["from"], {}).get("dp"):
        findings["dpFrom"].append(f"{slug}: dpFrom page={fm.get('dpFrom')} vs enrich={enrich.get(t['from'],{}).get('dp')}")
    if fm.get("dpTo") != enrich.get(t["to"], {}).get("dp"):
        findings["dpTo"].append(f"{slug}: dpTo page={fm.get('dpTo')} vs enrich={enrich.get(t['to'],{}).get('dp')}")
    # kind
    exp_kind = "fusion" if t["kind"] in ("fusion", "potara") else "transform"
    if fm.get("kind") != exp_kind:
        findings["kind"].append(f"{slug}: kind page={fm.get('kind')} vs expected {exp_kind}")
    # partners for fusion/potara
    if t["kind"] in ("fusion", "potara"):
        pnames = [p for p in (t.get("partnerNames") or []) if p]
        if not pnames:
            findings["partners_missing"].append(f"{slug}: fusion/potara but no partnerNames in data")
        else:
            # resolve partner names to real characters
            allnames = {c.get("fullName") for c in chars.values()} | {c.get("name") for c in chars.values()}
            for p in pnames:
                if p not in allnames:
                    findings["partner_unresolved"].append(f"{slug}: partner '{p}' not a known character name")
            # check listed in summary or body
            if not any(p in (fm.get("summary") or "") for p in pnames) and "Required partner" not in body:
                findings["partner_not_listed"].append(f"{slug}: partners {pnames} not shown in summary/body")
    # wikilink resolution in body
    for m in re.finditer(r"\[\[([^\]\|]+)\\?\|", body):
        tgt = m.group(1).strip().rstrip("\\")
        if tgt not in all_slugs:
            findings["dead_wikilink"].append(f"{slug}: body wikilink [[{tgt}]] does not resolve")
    for m in re.finditer(r"\[\[([^\]\|]+)\]\]", body):
        tgt = m.group(1).strip()
        if tgt not in all_slugs:
            findings["dead_wikilink"].append(f"{slug}: body wikilink [[{tgt}]] does not resolve")
    # moveset diff spot (compare body table to recomputed kit)
    cf, ct = chars.get(t["from"]) or {}, chars.get(t["to"]) or {}
    kit_f, kit_t = kit(cf), kit(ct)
    # confidence must be datamined
    if fm.get("confidence") != "datamined":
        findings["confidence"].append(f"{slug}: confidence={fm.get('confidence')} (gen sets datamined)")

# moveset spot-check: pick 12 pages, compare first row of before/after
spot = list(edge_by_slug.items())[:0]  # done inline below
log("")
log("FINDINGS BY CATEGORY:")
for k, v in findings.items():
    log(f"  [{k}] count={len(v)}")
    for line in v[:40]:
        log(f"      {line}")

log("")
log(f"recomputed statChanges for {recomputed} pages")
log(f"pages with positive heal in data: {heal_pages_pos}  zero heal: {heal_pages_zero}")

# explicit moveset diff verification for 12 pages
log("")
log("MOVESET DIFF spot-check (first 12 pages): page-table rows vs recomputed kit")
def body_moveset(body):
    rows = []
    m = re.search(r"## Moveset change\n\n\| Before \| After \|\n\|---\|---\|\n((?:\|.*\n)+)", body)
    if not m:
        return rows
    for line in m.group(1).strip().splitlines():
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) == 2:
            rows.append(tuple(cells))
    return rows

mismatch_ms = 0
checked_ms = 0
for slug, t in list(edge_by_slug.items()):
    fpath = CONTENT / "transformations" / f"{slug}.md"
    if not fpath.exists():
        continue
    _, body = parse_md(fpath)
    cf, ct = chars.get(t["from"]) or {}, chars.get(t["to"]) or {}
    kit_f, kit_t = kit(cf), kit(ct)
    exp_rows = []
    for i in range(max(len(kit_f), len(kit_t))):
        a = kit_f[i] if i < len(kit_f) else "—"
        b = kit_t[i] if i < len(kit_t) else "—"
        exp_rows.append((a, b))
    got = body_moveset(body)
    checked_ms += 1
    if got != exp_rows and (kit_f or kit_t):
        mismatch_ms += 1
        if mismatch_ms <= 12:
            log(f"  MISMATCH {slug}:")
            log(f"     expected={exp_rows}")
            log(f"     got     ={got}")
log(f"moveset diff: checked={checked_ms} mismatches={mismatch_ms}")

OUT.write_text("\n".join(out_lines), encoding="utf-8")
print("\n".join(out_lines[-80:]))
print(f"\n[full output -> {OUT}]")
