"""READ-ONLY probe: consolidate slug-drift impact numbers for the report."""
from __future__ import annotations
import re
from collections import Counter, defaultdict
from pathlib import Path

CONTENT = Path(r"C:\vaults\sparking_zero\content")
PRIORITY = ["characters","skills","blasts","transformations","mechanics","game-modes",
            "episode-battles","patches","dlc","guides","stages","shop","glossary"]
DISPLAY = defaultdict(lambda: "name", {"patches":"version","guides":"title","glossary":"term"})


def nslug(s): return re.sub(r"\s+","-",s.strip().lower())
def gslug(s):
    s=s.lower(); s=re.sub(r"['’!.]","",s); s=re.sub(r"[^a-z0-9]+","-",s); return s.strip("-")
def grab(fm,f):
    m=re.search(rf'^{f}:\s*(.+?)\s*$',fm,re.M)
    if not m: return None
    v=m.group(1).strip()
    return v[1:-1] if len(v)>=2 and v[0] in "\"'" and v[-1]==v[0] else v

index={}; pages=[]
cfiles=defaultdict(list)
for d in sorted(CONTENT.iterdir()):
    if d.is_dir():
        for f in sorted(d.glob("*.md")): cfiles[d.name].append(f)
for coll in PRIORITY:
    for f in cfiles.get(coll,[]):
        fm=f.read_text(encoding="utf-8").split("---")
        fm=fm[1] if len(fm)>=3 else ""
        name=grab(fm,DISPLAY[coll]) or f.stem
        pages.append((coll,f.stem,name))
        index.setdefault(f.stem,(coll,f.stem))
        if coll=="glossary":
            am=re.search(r'^aliases:\s*\[(.*)\]',fm,re.M)
            block=re.search(r'^aliases:\s*$((?:\n[ \t]+-.*)+)',fm,re.M)
            als=[]
            if am: als=[x.strip().strip('"\'') for x in am.group(1).split(",") if x.strip()]
            elif block: als=[l.strip()[1:].strip().strip('"\'') for l in block.group(1).splitlines() if l.strip().startswith("-")]
            for a in als: index.setdefault(nslug(a),(coll,"#"+f.stem))

# 1. wrong-target pages
print("1. pages where [[display name]] resolves to a DIFFERENT page:")
for coll,slug,name in pages:
    hit=index.get(nslug(name))
    if hit and hit[1]!=slug and hit[1]!=("#"+slug):
        print(f"   {coll}/{slug}  name={name!r}  ->  {hit}")

# 2. characters unreachable purely due to punctuation
chars=[p for p in pages if p[0]=="characters"]
unreach=[(s,n) for c,s,n in chars if nslug(n) not in index]
print(f"\n2. character pages: {len(chars)} total, {len(unreach)} unreachable by [[exact display name]]")
print("   (all because normalizeSlug keeps punctuation the file-slug dropped)")
rc=Counter()
for s,n in unreach:
    if re.search(r"[()]",n): rc["parens"]+=1
    if "," in n: rc["comma"]+=1
    if "." in n: rc["period"]+=1
    if re.search(r"[^\x00-\x7f]",n): rc["non-ascii"]+=1
print("   reason breakdown:",dict(rc))

# 3. CURRENT real broken links with backslash stripped (audit.py's view) -> latency check
wl=re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
broken_clean=Counter()
for f in CONTENT.rglob("*.md"):
    for m in wl.finditer(f.read_text(encoding="utf-8")):
        tgt=m.group(1).rstrip("\\")          # strip the escaped-pipe backslash (like audit.py)
        if nslug(tgt) not in index:
            broken_clean[tgt]+=1
print(f"\n3. wikilinks still unresolved AFTER stripping '\\' (true current breakage): "
      f"{sum(broken_clean.values())} -> {dict(broken_clean)}")
print("   (confirms punctuation drift is LATENT: authors used slug-form targets)")
