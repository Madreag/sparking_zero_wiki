"""Audit Agent 1 — exhaustive character-page vs source-of-truth probe.

READ-ONLY. Writes only audit/a1_out.json + prints a summary.
Compares every content/characters/*.md against data-mined/characters.json
(+ enrichment) and replicates gen_content.py's transforms so we can flag any
field the generator would NOT round-trip (stale pages, hand-edits, gen bugs).
"""
from __future__ import annotations
import json, re, glob, os
from collections import defaultdict, Counter

ROOT = r"C:\vaults\sparking_zero"
DM = os.path.join(ROOT, "data-mined")
CHARDIR = os.path.join(ROOT, "content", "characters")

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

chars = load(os.path.join(DM, "characters.json"))
enrich = load(os.path.join(DM, "enrichment", "characters.json"))
sw_a = load(os.path.join(DM, "enrichment", "sw_a.json"))
sw_b = load(os.path.join(DM, "enrichment", "sw_b.json"))

import yaml

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)

def read_page(path):
    raw = open(path, encoding="utf-8").read()
    m = FM_RE.match(raw)
    if not m:
        return None, "", raw
    fm = yaml.safe_load(m.group(1))
    return fm, m.group(2), raw

def norm(v):
    if isinstance(v, bool):
        return v
    if isinstance(v, float) and v.is_integer():
        return int(v)
    return v

def numeq(a, b):
    a, b = norm(a), norm(b)
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return abs(a - b) < 1e-9
    return a == b

# ---- replicate gen_content slug + hp logic ----
groups = defaultdict(list)
for c in chars.values():
    if c["name"]:
        groups[c["baseId"]].append(c)
for bid, members in groups.items():
    members.sort(key=lambda c: c["formCode"])

def resolved_hp(c):
    if c["hp"] is not None:
        return c["hp"], False
    for sib in groups.get(c["baseId"], []):
        if sib["hp"] is not None:
            return sib["hp"], True
    return None, False

# slug map exactly like gen_content
slugify_re1 = re.compile(r"['’!.]")
slugify_re2 = re.compile(r"[^a-z0-9]+")
def slugify(s):
    s = s.lower(); s = slugify_re1.sub("", s); s = slugify_re2.sub("-", s)
    return s.strip("-")

gen_slugs = {}
used = {}
for cid, c in sorted(chars.items()):
    if not c["name"]:
        continue
    label = c["fullName"] or c["name"]
    s = slugify(label)
    if s in used and used[s] != cid:
        s = f"{s}-{cid.replace('_','-')}"
    used[s] = cid
    gen_slugs[cid] = s

def best_damage(move):
    dmg = chip = hits = None
    for b in move.get("bullets") or []:
        cand = max(x for x in (b.get("beamPower"), b.get("power"), 0) if x is not None)
        if cand and (dmg is None or cand > dmg):
            dmg = cand; chip = b.get("beamChip") or b.get("chip"); hits = b.get("multiHit")
    melee = [p for p in (move.get("combatives") or {}).get("meleePowers", []) if p]
    if melee and (dmg is None or max(melee) > dmg):
        dmg = max(melee); chip = None; hits = None
    return dmg, chip, hits

# ---- load all pages, map cid<->slug ----
pages = {}            # slug -> (fm, body, path)
slug_by_cid = {}      # charId -> slug(stem)
cid_by_slug = {}
for path in glob.glob(os.path.join(CHARDIR, "*.md")):
    slug = os.path.splitext(os.path.basename(path))[0]
    fm, body, raw = read_page(path)
    pages[slug] = (fm, body, path, raw)
    if fm and fm.get("charId"):
        slug_by_cid[fm["charId"]] = slug
        cid_by_slug[slug] = fm["charId"]

all_slugs = set(pages.keys())

findings = []
def add(sev, check, cid, slug, field, page_val, src_val, note=""):
    findings.append({"sev": sev, "check": check, "cid": cid, "slug": slug,
                     "field": field, "page": page_val, "src": src_val, "note": note})

NUM_FIELDS = ["kiChargeSpeed","kiAutoRecovery","kiAutoRecoveryLimit","initialKi",
              "maxSkillStock","initialSkillStock","sparkingDrainPerSec","kiBlastShots"]
SGG_KEYS = ["vanishExchangeRate","attackBreak","fastAvoid","throwBreak","hitFromBehind","lastHPGauge","impactStart"]

stats = Counter()
playable_cids = []
nonplayable = []
hp_dist = Counter()

for slug, (fm, body, path, raw) in sorted(pages.items()):
    if not fm:
        add("BLOCKER","parse",None,slug,"frontmatter","unparseable","-"); continue
    cid = fm.get("charId")
    stats["pages"] += 1
    if cid not in chars:
        add("BLOCKER","check1",cid,slug,"charId","present","missing in characters.json",
            "page charId not found in data"); continue
    c = chars[cid]
    e = enrich.get(cid, {})
    stats["pages_with_cid"] += 1

    # playable accounting
    if fm.get("playable"):
        playable_cids.append(cid)
    else:
        nonplayable.append((cid, slug, c.get("name")))

    # ---- CHECK 1: numeric fields direct compare ----
    for field in NUM_FIELDS:
        src = c.get(field)
        has = field in fm
        stats["num_fields_checked"] += 1
        if src is None:
            if has and fm[field] is not None:
                add("HIGH","check1",cid,slug,field,fm[field],"null (absent in data)",
                    "page has value but data is null")
        else:
            if not has:
                add("HIGH","check1",cid,slug,field,"(absent)",norm(src),
                    "data has value but page omits field")
            elif not numeq(fm[field], src):
                add("HIGH","check1",cid,slug,field,fm[field],norm(src),"value mismatch")
    # skillGaugeGains
    src_sgg = {k:v for k,v in (c.get("skillGaugeGains") or {}).items() if v is not None}
    page_sgg = fm.get("skillGaugeGains") or {}
    for k in SGG_KEYS:
        stats["sgg_checked"] += 1
        if k in src_sgg:
            if k not in page_sgg:
                add("MEDIUM","check1",cid,slug,f"skillGaugeGains.{k}","(absent)",norm(src_sgg[k]),"data has value, page omits")
            elif not numeq(page_sgg[k], src_sgg[k]):
                add("HIGH","check1",cid,slug,f"skillGaugeGains.{k}",page_sgg[k],norm(src_sgg[k]),"value mismatch")
        else:
            if k in page_sgg:
                add("MEDIUM","check1",cid,slug,f"skillGaugeGains.{k}",page_sgg[k],"null","page has value, data null")
    # stray sgg keys
    for k in page_sgg:
        if k not in SGG_KEYS:
            add("LOW","check1",cid,slug,f"skillGaugeGains.{k}",page_sgg[k],"-","unexpected sgg key")

    # ---- CHECK 6: hp + hpInherited ----
    exp_hp, exp_inh = resolved_hp(c)
    stats["hp_checked"] += 1
    if exp_hp is None:
        if fm.get("hp") is not None:
            add("MEDIUM","check6",cid,slug,"hp",fm.get("hp"),"null (no sibling hp)","page hp set but data+siblings null")
    else:
        if not numeq(fm.get("hp"), exp_hp):
            add("HIGH","check6",cid,slug,"hp",fm.get("hp"),norm(exp_hp),"hp mismatch vs resolved")
        if bool(fm.get("hpInherited")) != exp_inh:
            add("MEDIUM","check6",cid,slug,"hpInherited",fm.get("hpInherited"),exp_inh,
                f"data.hp={'null' if c['hp'] is None else norm(c['hp'])}")
    if fm.get("hp") is not None:
        hp_dist[norm(fm["hp"])] += 1

    # ---- CHECK 9: sparkingDrainPerSec ----
    sd = c.get("sparkingDrainPerSec")
    if sd is not None and norm(sd) != 2800:
        add("LOW","check9",cid,slug,"sparkingDrainPerSec",norm(sd),"2800 (typical)","non-2800 drain (note, may be legit)")

    # ---- CHECK 2: moveset fidelity ----
    mv = fm.get("moveset") or []
    page_b1 = [m for m in mv if m.get("type")=="blast1"]
    page_b2 = [m for m in mv if m.get("type")=="blast2"]
    page_ult = [m for m in mv if m.get("type")=="ultimate"]
    # supers
    data_supers = [s for s in c.get("supers",[]) if s.get("name")]
    data_s1 = [s for s in (c.get("s1Skills") or []) if s.get("name")]
    data_ult = c.get("ultimate") if (c.get("ultimate") and c["ultimate"].get("name")) else None
    stats["movesets_checked"] += 1
    # counts
    if len(page_b2) != len(data_supers):
        add("HIGH","check2",cid,slug,"moveset.blast2.count",len(page_b2),len(data_supers),"super count mismatch")
    if len(page_b1) != len(data_s1):
        add("HIGH","check2",cid,slug,"moveset.blast1.count",len(page_b1),len(data_s1),"S1 count mismatch")
    if len(page_ult) != (1 if data_ult else 0):
        add("HIGH","check2",cid,slug,"moveset.ultimate.count",len(page_ult),1 if data_ult else 0,"ult presence mismatch")
    # match supers by name
    dsupers_by_name = {s["name"]: s for s in data_supers}
    for pm in page_b2:
        stats["super_moves"] += 1
        ds = dsupers_by_name.get(pm.get("name"))
        if not ds:
            add("HIGH","check2",cid,slug,f"super:{pm.get('name')}",pm.get("name"),"(no matching super in data)","wrong/fabricated super name")
            continue
        if not numeq(pm.get("kiCost"), ds.get("kiCost")):
            add("HIGH","check2",cid,slug,f"super:{pm.get('name')}.kiCost",pm.get("kiCost"),ds.get("kiCost"),"kiCost mismatch")
        edmg, echip, ehits = best_damage(ds)
        if norm(pm.get("damage")) != norm(edmg):
            add("MEDIUM","check2",cid,slug,f"super:{pm.get('name')}.damage",pm.get("damage"),edmg,"damage != datamined best_damage")
        if norm(pm.get("hits")) != norm(ehits):
            add("LOW","check2",cid,slug,f"super:{pm.get('name')}.hits",pm.get("hits"),ehits,"hits != datamined multiHit")
    # ultimate
    if data_ult and page_ult:
        pm = page_ult[0]
        if pm.get("name") != data_ult.get("name"):
            add("HIGH","check2",cid,slug,"ultimate.name",pm.get("name"),data_ult.get("name"),"ult name mismatch")
        if not numeq(pm.get("kiCost"), data_ult.get("kiCost")):
            add("HIGH","check2",cid,slug,"ultimate.kiCost",pm.get("kiCost"),data_ult.get("kiCost"),"ult kiCost mismatch")
        edmg, echip, ehits = best_damage(data_ult)
        if norm(pm.get("damage")) != norm(edmg):
            add("MEDIUM","check2",cid,slug,"ultimate.damage",pm.get("damage"),edmg,"ult damage != datamined")
    # s1 skills (names + skillCost)
    ds1_by_name = {s["name"]: s for s in data_s1}
    for pm in page_b1:
        stats["s1_moves"] += 1
        ds = ds1_by_name.get(pm.get("name"))
        if not ds:
            add("HIGH","check2",cid,slug,f"blast1:{pm.get('name')}",pm.get("name"),"(no matching s1 in data)","wrong/fabricated S1 name")
            continue
        if not numeq(pm.get("skillCost"), ds.get("skillCost")):
            add("MEDIUM","check2",cid,slug,f"blast1:{pm.get('name')}.skillCost",pm.get("skillCost"),ds.get("skillCost"),"S1 skillCost mismatch")

    # ---- CHECK 3: transformsTo ----
    data_edges = []
    for t in (c.get("formChanges") or []) + (c.get("fusions") or []):
        if not t or not t.get("toName") or t["kind"] == "revert":
            continue
        data_edges.append(t)
    page_tt = fm.get("transformsTo") or []
    stats["transform_pages"] += 1 if page_tt else 0
    # build expected
    exp_edges = []
    for t in data_edges:
        exp_edges.append({
            "target": t["toName"],
            "targetSlug": gen_slugs.get(t["to"]),
            "cost": t.get("consumeBlastStock"),
            "kind": "fusion" if t["kind"] in ("fusion","potara") else "transform",
            "to_cid": t["to"],
        })
    if len(page_tt) != len(exp_edges):
        add("MEDIUM","check3",cid,slug,"transformsTo.count",len(page_tt),len(exp_edges),"edge count mismatch vs data")
    # match by target name
    exp_by_target = { e["target"]: e for e in exp_edges}
    for pe in page_tt:
        stats["transform_edges"] += 1
        ee = exp_by_target.get(pe.get("target"))
        ts = pe.get("targetSlug")
        if ts is None:
            add("HIGH","check3",cid,slug,f"transformsTo:{pe.get('target')}.targetSlug","(absent → renders #)",
                gen_slugs.get(ee["to_cid"]) if ee else "?","missing targetSlug")
        elif ts not in all_slugs:
            add("HIGH","check3",cid,slug,f"transformsTo:{pe.get('target')}.targetSlug",ts,"(no such page)","dangling targetSlug → 404/#")
        if ee:
            if not numeq(pe.get("cost"), ee["cost"]):
                add("MEDIUM","check3",cid,slug,f"transformsTo:{pe.get('target')}.cost",pe.get("cost"),ee["cost"],"cost mismatch")
            if pe.get("kind") != ee["kind"]:
                add("MEDIUM","check3",cid,slug,f"transformsTo:{pe.get('target')}.kind",pe.get("kind"),ee["kind"],"kind mismatch")
            if ts is not None and ee["targetSlug"] is not None and ts != ee["targetSlug"]:
                add("MEDIUM","check3",cid,slug,f"transformsTo:{pe.get('target')}.targetSlug",ts,ee["targetSlug"],"slug differs from gen expectation")
        else:
            add("MEDIUM","check3",cid,slug,f"transformsTo:{pe.get('target')}",pe.get("target"),"(no matching data edge)","page transform not in data (formChanges+fusions)")

    # ---- CHECK 4: DP ----
    dp = fm.get("dp")
    if fm.get("playable"):
        if dp is None:
            add("HIGH","check4",cid,slug,"dp","null","expected 1..15 (community)","playable missing DP")
        elif not isinstance(dp,(int,float)) or dp < 0 or dp > 15:
            add("MEDIUM","check4",cid,slug,"dp",dp,"plausible 1..15","DP out of plausible range")
    else:
        if dp is not None:
            add("LOW","check4",cid,slug,"dp",dp,"null (non-playable)","non-playable has DP")

# ---- CHECK 5: playable count ----
stats["playable"] = len(playable_cids)
stats["nonplayable"] = len(nonplayable)

# ---- CHECK 4b: confidence honesty (all pages datamined despite community DP) ----
conf_counter = Counter()
dp_with_research_source = 0
for slug,(fm,body,path,raw) in pages.items():
    if not fm: continue
    conf_counter[fm.get("confidence")] += 1

# ---- CHECK 8: duplication of S/W/howToFight/summary/playstyle across unrelated baseIds ----
text_fields = ["playstyle","howToFight","summary"]
list_fields = ["strengths","weaknesses"]
text_owners = defaultdict(list)  # text -> [(cid, slug, field)]
for slug,(fm,body,path,raw) in pages.items():
    if not fm or not fm.get("playable"): continue
    cid = fm.get("charId")
    for f in text_fields:
        v = fm.get(f)
        if isinstance(v,str) and len(v.strip()) >= 25:
            text_owners[("T:"+f, v.strip())].append((cid, slug))
    for f in list_fields:
        for item in fm.get(f) or []:
            if isinstance(item,str) and len(item.strip()) >= 25:
                text_owners[("L:"+f, item.strip())].append((cid, slug))

dup_findings = []
for (kind, text), owners in text_owners.items():
    base_ids = {cid.split("_")[0] for cid,_ in owners}
    if len(owners) >= 2 and len(base_ids) >= 2:
        dup_findings.append((kind, text, owners))
dup_findings.sort(key=lambda x: -len(x[2]))

# ---- CHECK 8b: number-vs-moveset contradiction in S/W text ----
num_re = re.compile(r"(\d{2},?\d{3})\s*[- ]?\s*ki", re.I)
contradictions = []
for slug,(fm,body,path,raw) in pages.items():
    if not fm or not fm.get("playable"): continue
    cid = fm.get("charId")
    # gather super/ult ki costs from moveset
    kicosts = set()
    for m in fm.get("moveset") or []:
        if m.get("type") in ("blast2","ultimate") and m.get("kiCost") is not None:
            kicosts.add(norm(m["kiCost"]))
    blob = " ".join([str(fm.get("playstyle") or ""), str(fm.get("howToFight") or ""),
                     str(fm.get("summary") or "")] + list(fm.get("strengths") or []) + list(fm.get("weaknesses") or []))
    for mt in num_re.finditer(blob):
        val = int(mt.group(1).replace(",",""))
        # only consider "super"/"ultimate" mentions near it
        ctx = blob[max(0,mt.start()-40):mt.end()+40].lower()
        if "super" in ctx or "ultimate" in ctx or "ult" in ctx:
            if kicosts and val not in kicosts and val >= 10000:
                contradictions.append((cid, slug, val, sorted(kicosts), ctx.strip()))

# ---- CHECK 9b: vanish-cost mislabel scan (2800 described as vanish/Z-counter) ----
vanish_mislabel = []
vc_re = re.compile(r"2[,.]?800")
for slug,(fm,body,path,raw) in pages.items():
    if not fm: continue
    cid = fm.get("charId")
    blob = " ".join([str(fm.get("playstyle") or ""), str(fm.get("howToFight") or ""),
                     str(fm.get("summary") or "")] + list(fm.get("strengths") or []) + list(fm.get("weaknesses") or []) ) + " " + (body or "")
    for mt in vc_re.finditer(blob):
        ctx = blob[max(0,mt.start()-50):mt.end()+50].lower()
        if "vanish" in ctx or "z-counter" in ctx or "zcounter" in ctx or "z counter" in ctx:
            vanish_mislabel.append((cid, slug, ctx.strip()))

# ---- summarize ----
sev_order = ["BLOCKER","HIGH","MEDIUM","LOW","NIT"]
by_sev = Counter(f["sev"] for f in findings)
by_check = Counter(f["check"] for f in findings)

out = {
    "stats": dict(stats),
    "by_sev": dict(by_sev),
    "by_check": dict(by_check),
    "hp_dist": dict(sorted(hp_dist.items())),
    "conf_counter": dict(conf_counter),
    "nonplayable": nonplayable,
    "findings": findings,
    "dup_findings": [{"kind":k,"text":t,"owners":o} for k,t,o in dup_findings],
    "contradictions": contradictions,
    "vanish_mislabel": vanish_mislabel,
}
with open(os.path.join(ROOT,"audit","a1_out.json"),"w",encoding="utf-8") as f:
    json.dump(out, f, indent=1, ensure_ascii=False)

print("=== STATS ===")
for k,v in stats.items():
    print(f"  {k}: {v}")
print(f"  playable: {len(playable_cids)}  nonplayable: {len(nonplayable)}")
print("=== HP DIST (pages) ===", dict(sorted(hp_dist.items())))
print("=== CONFIDENCE DIST ===", dict(conf_counter))
print("=== FINDINGS BY SEV ===", {s:by_sev.get(s,0) for s in sev_order})
print("=== FINDINGS BY CHECK ===", dict(sorted(by_check.items())))
print(f"=== NONPLAYABLE ({len(nonplayable)}) ===")
for cid,slug,nm in sorted(nonplayable):
    print(f"  {cid}  {slug}  {nm!r}")
print(f"=== DUP TEXT GROUPS (cross-baseId) : {len(dup_findings)} ===")
for k,t,o in dup_findings[:40]:
    print(f"  [{k}] x{len(o)} {sorted(set(s for _,s in o))} :: {t[:90]!r}")
print(f"=== S/W NUMBER CONTRADICTIONS : {len(contradictions)} ===")
for cid,slug,val,kc,ctx in contradictions[:40]:
    print(f"  {cid} {slug}: text={val} moveset_ki={kc} :: ...{ctx[:80]}...")
print(f"=== VANISH 2800 MISLABEL : {len(vanish_mislabel)} ===")
for cid,slug,ctx in vanish_mislabel[:40]:
    print(f"  {cid} {slug}: ...{ctx}...")

# detailed findings dump (first N per check)
print("\n=== DETAILED FINDINGS (grouped) ===")
for chk in sorted(by_check):
    fs = [f for f in findings if f["check"]==chk]
    print(f"\n--- {chk}: {len(fs)} ---")
    for f in fs[:60]:
        print(f"  [{f['sev']}] {f['cid']} {f['slug']} {f['field']}: page={f['page']!r} src={f['src']!r} ({f['note']})")
    if len(fs) > 60:
        print(f"  ... +{len(fs)-60} more")
