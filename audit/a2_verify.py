import json, re
from pathlib import Path
RAW = Path(r"C:\vaults\sparking_zero\data-mined\raw\masterdata")
chars = json.load(open(r"C:\vaults\sparking_zero\data-mined\characters.json", encoding="utf-8"))

def props(e):
    return e[0].get("Properties") or {} if e else {}

def slug_to_cid(target):
    # reuse gen slug algorithm
    def slugify(s):
        s=s.lower(); s=re.sub(r"['’!.]","",s); s=re.sub(r"[^a-z0-9]+","-",s); return s.strip("-")
    slugs={}; used={}
    for cid,c in sorted(chars.items()):
        if not c["name"]: continue
        label=c["fullName"] or c["name"]; s=slugify(label)
        if s in used and used[s]!=cid: s=f"{s}-{cid.replace('_','-')}"
        used[s]=cid; slugs[cid]=s
    for cid,s in slugs.items():
        if s==target: return cid
    return None

def melee_powers(cid, want_slot):
    f=RAW/"Combatives"/f"{cid}.json"; out=[]
    if f.exists():
        d=json.load(open(f,encoding="utf-8"))
        for k,v in d.items():
            m=re.match(r"Combatives(?:SubParam)?_\d{4}_\d{2}_(act.+)$",k)
            if not m: continue
            a=m.group(1)
            slot = "SPM1" if "SPM1" in a else "SPM2" if "SPM2" in a else ("ULT" if ("ULT" in a or "UB" in a) else None)
            if slot==want_slot and props(v).get("Power"):
                out.append((k, props(v)["Power"]))
    return out

for label, slot in [("goten","SPM2"), ("goku-super-ultra-instinct-sign","ULT")]:
    cid = slug_to_cid(label)
    print(f"{label} -> cid {cid}")
    print("   melee:", melee_powers(cid, slot))
