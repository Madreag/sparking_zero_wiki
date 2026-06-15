"""Audit Agent 1 — deeper probes: dropped moves, named-move-in-kit, distributions."""
from __future__ import annotations
import json, re, glob, os
from collections import defaultdict, Counter
import yaml

ROOT = r"C:\vaults\sparking_zero"
DM = os.path.join(ROOT, "data-mined")
CHARDIR = os.path.join(ROOT, "content", "characters")

def load(p):
    with open(p, encoding="utf-8") as f:
        return json.load(f)

chars = load(os.path.join(DM, "characters.json"))
FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
def read_page(path):
    raw = open(path, encoding="utf-8").read()
    m = FM_RE.match(raw)
    if not m: return None, "", raw
    return yaml.safe_load(m.group(1)), m.group(2), raw

pages = {}
for path in glob.glob(os.path.join(CHARDIR, "*.md")):
    slug = os.path.splitext(os.path.basename(path))[0]
    fm, body, raw = read_page(path)
    pages[slug] = fm
cid2page = {fm["charId"]: (slug, fm) for slug,fm in pages.items() if fm and fm.get("charId")}

def norm(v):
    if isinstance(v, bool): return v
    if isinstance(v, float) and v.is_integer(): return int(v)
    return v

print("=" * 70)
print("A) DROPPED MOVES: data has a super/ult with kiCost but name=None (skipped by gen)")
print("=" * 70)
dropped = []
for cid, c in sorted(chars.items()):
    slug = cid2page.get(cid, (None,None))[0]
    fm = cid2page.get(cid, (None,None))[1]
    if not fm: continue
    playable = fm.get("playable")
    for s in c.get("supers", []):
        if s.get("name") is None and (s.get("kiCost") is not None or s.get("category") or s.get("bullets")):
            dropped.append((cid, slug, playable, s.get("slot"), "super", s.get("kiCost"), s.get("category")))
    u = c.get("ultimate")
    if u and u.get("name") is None and (u.get("kiCost") is not None or u.get("category") or u.get("bullets")):
        dropped.append((cid, slug, playable, "ULT", "ult", u.get("kiCost"), u.get("category")))
print(f"total dropped move entries: {len(dropped)}  (playable: {sum(1 for d in dropped if d[2])})")
for cid, slug, pl, slot, kind, ki, cat in dropped:
    print(f"  {cid} {slug} playable={pl} {slot} {kind} ki={ki} cat={cat!r}")

print()
print("=" * 70)
print("B) PLAYABLE with 0 supers in moveset (page)")
print("=" * 70)
zero_supers = []
for cid,(slug,fm) in sorted(cid2page.items()):
    if not fm.get("playable"): continue
    nb2 = sum(1 for m in (fm.get("moveset") or []) if m.get("type")=="blast2")
    data_supers_named = [s for s in chars[cid].get("supers",[]) if s.get("name")]
    data_supers_any = [s for s in chars[cid].get("supers",[]) if (s.get("kiCost") is not None or s.get("category"))]
    if nb2 == 0:
        zero_supers.append((cid, slug, nb2, len(data_supers_named), len(data_supers_any)))
print(f"playable with 0 blast2 in moveset: {len(zero_supers)}")
for cid, slug, nb2, dn, da in zero_supers:
    print(f"  {cid} {slug}  page_supers={nb2} data_named_supers={dn} data_any_super_entries={da}")

print()
print("=" * 70)
print("C) PLAYABLE with 0 ultimate in moveset (page) but data has ult entry")
print("=" * 70)
for cid,(slug,fm) in sorted(cid2page.items()):
    if not fm.get("playable"): continue
    nult = sum(1 for m in (fm.get("moveset") or []) if m.get("type")=="ultimate")
    u = chars[cid].get("ultimate")
    if nult == 0 and u and (u.get("kiCost") is not None or u.get("category")):
        print(f"  {cid} {slug} page_ult=0 data_ult_name={u.get('name')!r} ki={u.get('kiCost')}")

print()
print("=" * 70)
print("D) REFINED S/W number contradictions (allow kiCost + triggerKiCost from data)")
print("=" * 70)
num_re = re.compile(r"(\d{2},?\d{3})\s*[- ]?\s*ki", re.I)
real_contra = []
for cid,(slug,fm) in sorted(cid2page.items()):
    if not fm.get("playable"): continue
    allowed = set()
    for s in chars[cid].get("supers", []):
        for k in ("kiCost","triggerKiCost"):
            if s.get(k) is not None: allowed.add(norm(s[k]))
    u = chars[cid].get("ultimate") or {}
    if u.get("kiCost") is not None: allowed.add(norm(u["kiCost"]))
    blob = " ".join([str(fm.get("playstyle") or ""), str(fm.get("howToFight") or ""),
                     str(fm.get("summary") or "")] + list(fm.get("strengths") or []) + list(fm.get("weaknesses") or []))
    for mt in num_re.finditer(blob):
        val = int(mt.group(1).replace(",",""))
        ctx = blob[max(0,mt.start()-45):mt.end()+30].lower()
        if ("super" in ctx or "ult" in ctx) and val >= 10000:
            if allowed and val not in allowed:
                real_contra.append((cid, slug, val, sorted(allowed), ctx.strip()))
print(f"real contradictions (after trigger-cost allowance): {len(real_contra)}")
for cid, slug, val, allowed, ctx in real_contra:
    print(f"  {cid} {slug}: text={val} allowed={allowed} :: ...{ctx}...")

print()
print("=" * 70)
print("E) NAMED-MOVE-IN-KIT: strengths/weaknesses naming a move the kit lacks")
print("=" * 70)
# registry of all known move names (super/ult/s1) across roster
all_move_names = set()
for c in chars.values():
    for s in c.get("supers",[]):
        if s.get("name"): all_move_names.add(s["name"])
    u = c.get("ultimate")
    if u and u.get("name"): all_move_names.add(u["name"])
    for s in (c.get("s1Skills") or []):
        if s.get("name"): all_move_names.add(s["name"])
# move names that are reasonably specific (>= 6 chars, multiword or distinctive)
specific = sorted([n for n in all_move_names if len(n) >= 6], key=lambda s:-len(s))

def kit_names(cid):
    names = set()
    for s in chars[cid].get("supers",[]):
        if s.get("name"): names.add(s["name"])
    u = chars[cid].get("ultimate")
    if u and u.get("name"): names.add(u["name"])
    for s in (chars[cid].get("s1Skills") or []):
        if s.get("name"): names.add(s["name"])
    return names

# patterns that strongly assert the fighter HAS the move
assert_pat = re.compile(r'([A-Z][\w\'!.\- ]{4,40}?)\s*(?:S1|S2|\(free\)|\(\d[^)]*ki[^)]*\)|\(\d+ stock)', )
mismatches = []
for cid,(slug,fm) in sorted(cid2page.items()):
    if not fm.get("playable"): continue
    kn = kit_names(cid)
    items = list(fm.get("strengths") or []) + list(fm.get("weaknesses") or [])
    for it in items:
        for mt in assert_pat.finditer(it):
            cand = mt.group(1).strip(" -—·")
            # normalize: find any known move name that the candidate ends with / equals
            matched_known = None
            for mn in specific:
                if cand.lower().endswith(mn.lower()) or cand.lower()==mn.lower():
                    matched_known = mn; break
            if matched_known and matched_known not in kn:
                # exclude generic ki-blast-ish / cross-form (skill may be on sibling)
                mismatches.append((cid, slug, matched_known, it[:70]))
# dedupe
seen=set(); uniq=[]
for m in mismatches:
    k=(m[0],m[2])
    if k in seen: continue
    seen.add(k); uniq.append(m)
print(f"named-move-not-in-own-kit candidates: {len(uniq)} (NOTE: skill may exist on a sibling form / be a class default)")
for cid, slug, mv, ctx in uniq[:80]:
    print(f"  {cid} {slug}: claims {mv!r} :: {ctx!r}")

print()
print("=" * 70)
print("F) DISTRIBUTIONS (playable only)")
print("=" * 70)
hp_pl = Counter(); dp_pl = Counter(); era_pl = Counter(); src_pl = Counter()
hp_all = Counter()
no_hp_pl = []
for cid,(slug,fm) in cid2page.items():
    if fm.get("hp") is not None: hp_all[norm(fm["hp"])]+=1
    if fm.get("playable"):
        if fm.get("hp") is not None: hp_pl[norm(fm["hp"])]+=1
        else: no_hp_pl.append((cid,slug))
        dp_pl[fm.get("dp")]+=1
        era_pl[fm.get("era")]+=1
        src_pl[fm.get("source")]+=1
print("playable HP dist:", dict(sorted(hp_pl.items())), "sum", sum(hp_pl.values()))
print("ALL-pages HP dist:", dict(sorted(hp_all.items())), "sum", sum(hp_all.values()))
print("playable without HP:", no_hp_pl)
print("playable DP dist:", dict(sorted((k if k is not None else -1, v) for k,v in dp_pl.items())))
print("playable era dist:", dict(era_pl))
print("playable source dist:", dict(src_pl))

print()
print("=" * 70)
print("G) supers/ult with NULL kiCost but a NAME (page will show blank ki)")
print("=" * 70)
nullki = []
for cid,(slug,fm) in sorted(cid2page.items()):
    for s in chars[cid].get("supers",[]):
        if s.get("name") and s.get("kiCost") is None:
            nullki.append((cid,slug,s.get("slot"),"super",s["name"]))
    u = chars[cid].get("ultimate")
    if u and u.get("name") and u.get("kiCost") is None:
        nullki.append((cid,slug,"ULT","ult",u["name"]))
print(f"named moves with null kiCost: {len(nullki)}")
for cid,slug,slot,kind,nm in nullki[:60]:
    print(f"  {cid} {slug} {slot} {kind} {nm!r}")
