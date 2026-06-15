#!/usr/bin/env python3
"""
Audit Agent 5 probe: patches / dlc / episode-battles / game-modes.
Read-only. Verifies countable checks against source-of-truth data.
"""
import json, sys, re, datetime
from pathlib import Path

ROOT = Path(r"c:\vaults\sparking_zero")
import yaml

TODAY = datetime.date(2026, 6, 15)

def load_fm(path):
    txt = path.read_text(encoding="utf-8")
    if not txt.startswith("---"):
        return None, txt
    end = txt.find("\n---", 3)
    fm = txt[3:end]
    body = txt[end+4:]
    return yaml.safe_load(fm), body

def md_files(sub):
    return sorted((ROOT/"content"/sub).glob("*.md"))

# ---------- build character resolution tables ----------
char_slugs = {}      # slug -> {name, dp, playable, charId}
char_names = {}      # exact name -> slug
norm_names = {}      # normalized name -> [slugs]
def norm(s):
    return re.sub(r"[^a-z0-9]", "", (s or "").lower())

for p in md_files("characters"):
    fm,_ = load_fm(p)
    if not fm: continue
    slug = fm.get("slug")
    nm = fm.get("name")
    char_slugs[slug] = {"name":nm, "dp":fm.get("dp"),
                        "playable":fm.get("playable", True),
                        "charId":fm.get("charId")}
    if nm:
        char_names[nm] = slug
        norm_names.setdefault(norm(nm), []).append(slug)

# datamined names
dm = json.loads((ROOT/"data-mined"/"characters.json").read_text(encoding="utf-8"))
dm_names = set()
for cid,rec in dm.items():
    n = rec.get("name")
    if n:
        dm_names.add(n.strip())
        norm_names.setdefault(norm(n), []).append("dm:"+cid)

enr = json.loads((ROOT/"data-mined"/"enrichment"/"characters.json").read_text(encoding="utf-8"))

def name_resolves(nm):
    if nm in char_names: return "exact-content"
    if nm in dm_names: return "exact-datamined"
    if norm(nm) in norm_names: return "normalized"
    return None

print("="*70)
print("CHARACTER TABLES: %d content character pages, %d datamined names" % (len(char_slugs), len(dm_names)))

# ---------- PATCHES ----------
print("\n" + "="*70 + "\nPATCHES\n" + "="*70)
patches = []
for p in md_files("patches"):
    fm,_ = load_fm(p)
    patches.append((p.name, fm))

orders = [fm["order"] for _,fm in patches]
print("patch count:", len(patches))
dups = {o for o in orders if orders.count(o)>1}
print("duplicate orders:", dups or "NONE")
by_order = sorted(patches, key=lambda x:x[1]["order"])
by_date  = sorted(patches, key=lambda x:x[1]["releaseDate"])
print("order-sort == date-sort:", [n for n,_ in by_order]==[n for n,_ in by_date])
if [n for n,_ in by_order]!=[n for n,_ in by_date]:
    print("  ORDER:", [n for n,_ in by_order])
    print("  DATE :", [n for n,_ in by_date])

PT_ENUM={"launch","major","balance","content","hotfix"}
for n,fm in patches:
    t=fm.get("type","content")
    if t not in PT_ENUM: print("  BAD type:", n, t)
    # date sanity
    try:
        d=datetime.date.fromisoformat(fm["releaseDate"])
        if d>TODAY: print("  FUTURE date:", n, fm["releaseDate"])
        # order should equal YYYYMMDD
        exp=int(fm["releaseDate"].replace("-",""))
        if fm["order"]!=exp: print("  order!=YYYYMMDD:", n, fm["order"], "vs", exp)
    except Exception as e:
        print("  BAD date:", n, fm.get("releaseDate"), e)
    # measured entries
    for m in fm.get("measured",[]):
        if "target" not in m or "metric" not in m:
            print("  measured missing target/metric:", n, m)

print("\npatch [slug | date | order | type | confidence | #measured]")
for n,fm in by_order:
    print("  %-26s %s  %-9s %-8s %-10s m=%d" % (
        fm["slug"], fm["releaseDate"], fm["order"], fm["type"],
        fm.get("confidence"), len(fm.get("measured",[]))))

# grep datamined tag usage in patches
print("\npatches mentioning 'datamined':")
for p in md_files("patches"):
    t=p.read_text(encoding="utf-8")
    if "datamined" in t.lower():
        print("  ", p.name, "-> count", t.lower().count("datamined"))

# ---------- DLC ----------
print("\n" + "="*70 + "\nDLC\n" + "="*70)
dlcs=[]
for p in md_files("dlc"):
    fm,_=load_fm(p)
    dlcs.append((p.name,fm))
orders=[fm["order"] for _,fm in dlcs]
print("dlc count:", len(dlcs), "| duplicate orders:",
      {o for o in orders if orders.count(o)>1} or "NONE")
DT={"paid","free","preorder","season-pass"}
for n,fm in dlcs:
    if fm.get("type") not in DT: print("  BAD type:",n,fm.get("type"))
    if not isinstance(fm.get("upcoming",False),bool): print("  upcoming not bool:",n)
print("\ndlc [slug | date | order | type | priceUSD | upcoming | conf | #chars]")
for n,fm in sorted(dlcs,key=lambda x:x[1]["order"]):
    print("  %-26s %s  o=%-2s %-12s $%-7s up=%-5s %-10s c=%d" % (
        fm["slug"], fm.get("releaseDate"), fm["order"], fm.get("type"),
        fm.get("priceUSD"), str(fm.get("upcoming",False)),
        fm.get("confidence"), len(fm.get("characters",[]))))

print("\nDLC character slug/name/DP resolution:")
for n,fm in dlcs:
    for c in fm.get("characters",[]):
        cn=c.get("name"); cs=c.get("slug"); cdp=c.get("dp")
        problems=[]
        if cs is not None:
            if cs not in char_slugs:
                problems.append("slug-missing")
            else:
                real=char_slugs[cs]["dp"]
                if cdp is not None and real!=cdp:
                    problems.append("DP %s!=content %s"%(cdp,real))
        else:
            if not fm.get("upcoming"):
                problems.append("no-slug")
        if cn and name_resolves(cn) is None:
            problems.append("name-unresolved")
        if problems:
            print("  [%s] %-40s slug=%-40s dp=%s -> %s" % (
                fm["slug"], cn, cs, cdp, ", ".join(problems)))
print("(blank above = all DLC chars resolve & DP matches)")

# upcoming check
print("\nupcoming DLC:")
for n,fm in dlcs:
    if fm.get("upcoming"):
        print("  ", fm["slug"], "upcoming=True date=",fm.get("releaseDate"),
              "conf=",fm.get("confidence"))

# ---------- EPISODE BATTLES ----------
print("\n" + "="*70 + "\nEPISODE BATTLES\n" + "="*70)
eps=[]
for p in md_files("episode-battles"):
    fm,_=load_fm(p)
    eps.append((p.name,fm))
orders=[fm["order"] for _,fm in eps]
print("episode count:", len(eps), "| duplicate orders:",
      {o for o in orders if orders.count(o)>1} or "NONE")
total_se=0
print("\n[slug | order | battleCount | len(battles) | match | sparkingEpisodes]")
for n,fm in sorted(eps,key=lambda x:x[1]["order"]):
    bc=fm.get("battleCount"); actual=len(fm.get("battles",[]))
    se=fm.get("sparkingEpisodes")
    total_se += se or 0
    print("  %-24s o=%-2s bc=%-3s actual=%-3s %s se=%s" % (
        fm["slug"], fm["order"], bc, actual,
        "OK" if bc==actual else "*** MISMATCH ***", se))
print("TOTAL sparkingEpisodes across campaigns:", total_se)

# vs opponent resolution
print("\nUNRESOLVED opponents (name not in content or datamined):")
unresolved={}
empty_vs=[]
for n,fm in eps:
    for b in fm.get("battles",[]):
        vs=b.get("vs",[]) or []
        if not vs:
            empty_vs.append((fm["slug"], b.get("id"), b.get("name")))
        for opp in vs:
            if name_resolves(opp) is None:
                unresolved.setdefault(opp,[]).append(fm["slug"]+":"+str(b.get("id")))
for opp,locs in sorted(unresolved.items()):
    print("  %-40s  @ %s" % (opp, ", ".join(locs[:6])))
print("(none above = every opponent resolves)")
print("\nbattles with empty vs[] (story/no-combat):")
for s,i,nm in empty_vs:
    print("  ", s, i, "-", nm)

# resolution-method breakdown for opponents (how many rely on normalized only)
method={}
for n,fm in eps:
    for b in fm.get("battles",[]):
        for opp in (b.get("vs",[]) or []):
            m=name_resolves(opp)
            method[m]=method.get(m,0)+1
print("\nopponent resolution methods:", method)

# normalized-only opponents (potential exact-name drift)
print("\nopponents resolving ONLY via normalization (name drift):")
seen=set()
for n,fm in eps:
    for b in fm.get("battles",[]):
        for opp in (b.get("vs",[]) or []):
            if opp in seen: continue
            seen.add(opp)
            if opp not in char_names and opp not in dm_names and norm(opp) in norm_names:
                tgt=norm_names[norm(opp)]
                print("  %-38s ~ %s" % (opp, tgt[:3]))

# ---------- GAME MODES ----------
print("\n" + "="*70 + "\nGAME MODES\n" + "="*70)
gms=[]
for p in md_files("game-modes"):
    fm,_=load_fm(p)
    gms.append((p.name,fm))
GC={"offline","online","pve","pvp","hub","training"}
print("game-mode count:", len(gms))
for n,fm in gms:
    if fm.get("category") not in GC: print("  BAD category:",n,fm.get("category"))
print("\n[slug | category | confidence]")
for n,fm in gms:
    print("  %-20s %-10s %s" % (fm["slug"], fm.get("category"), fm.get("confidence")))

# slug collisions across curated collections + shop
print("\nSLUG COLLISIONS (game-modes vs other collections):")
def slugs_of(sub):
    out={}
    for p in md_files(sub):
        fm,_=load_fm(p)
        if fm: out[fm.get("slug")]=p.name
    return out
gm_slugs=slugs_of("game-modes")
for other in ["mechanics","episode-battles","patches","dlc","guides","shop"]:
    os_=slugs_of(other)
    common=set(gm_slugs)&set(os_)
    for c in sorted(common):
        print("  '%s' in game-modes AND %s" % (c, other))
print("(none = no cross-collection slug collisions for game-modes)")

# cross-check episode-battle mode count vs collection
em=[fm for n,fm in gms if fm["slug"]=="episode-battle"][0]
for v in em.get("values",[]):
    if "What-If" in v["label"] or "Sparking" in v["label"]:
        print("\nepisode-battle MODE says routes =", v["value"], "(tag %s)"%v.get("tag"),
              "| collection sparkingEpisodes total =", total_se)

print("\nDONE")
