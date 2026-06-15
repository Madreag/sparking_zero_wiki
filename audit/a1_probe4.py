"""Audit Agent 1 — enumerate hpInherited cases where sibling forms disagree on HP."""
import json, glob, os, re, yaml
from collections import defaultdict

FM = re.compile(r"^---\n(.*?)\n---", re.S)
pages = {}
for p in glob.glob(r"content/characters/*.md"):
    fm = yaml.safe_load(FM.match(open(p, encoding="utf-8").read()).group(1))
    pages[os.path.splitext(os.path.basename(p))[0]] = fm
c = json.load(open(r"data-mined/characters.json", encoding="utf-8"))
groups = defaultdict(list)
for k, v in c.items():
    if v["name"]:
        groups[v["baseId"]].append(v)

inh = [(s, fm) for s, fm in pages.items() if fm.get("hpInherited")]
print("total hpInherited=true pages:", len(inh))
amb = 0
for slug, fm in sorted(inh):
    cid = fm["charId"]; bid = c[cid]["baseId"]
    sibhps = sorted({int(v["hp"]) for v in groups[bid] if v.get("hp") is not None})
    flag = "  <-- siblings DISAGREE" if len(sibhps) > 1 else ""
    if len(sibhps) > 1:
        amb += 1
    print(f"  {slug:46} hp={fm.get('hp')} hpInheritedFrom_sibHPs={sibhps}{flag}")
print("ambiguous (siblings disagree on HP):", amb)
