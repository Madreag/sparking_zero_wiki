import json
from collections import Counter

d = json.load(open(r"audit/a2_findings.json", encoding="utf-8"))
F = d["findings"]

print("=== DEDUP DROPS (detail) ===")
for s, nm, cl in d["stats"]["dropped"]:
    print(f"  slug={s}  name={nm!r}  class={cl}")

print("\n=== HIGH + MEDIUM findings ===")
for f in F:
    if f["sev"] in ("BLOCKER", "HIGH", "MEDIUM"):
        print(f"[{f['sev']}] {f['check']:10} {f['slug']:40} {f['msg']}")

print("\n=== kicost outliers grouped ===")
ki = [f for f in F if f["check"] == "kicost"]
c = Counter()
for f in ki:
    # extract the kiCost=NNN part
    msg = f["msg"]
    c[msg.split("kiCost=")[-1] if "kiCost=" in msg else "no-ki"] += 1
for k, n in c.most_common():
    print(f"  {n:3}  {k}")
print("  sample kicost findings:")
for f in ki[:12]:
    print(f"     {f['slug']:40} {f['msg']}")

print("\n=== body LOW ===")
for f in F:
    if f["check"] == "body" and f["sev"] == "LOW":
        print(f"  {f['slug']:40} {f['msg']}")

print("\n=== chip MEDIUM ===")
for f in F:
    if f["check"] == "chip":
        print(f"  {f['slug']:40} {f['msg']}")

print("\n=== wording (melee-labeled) sample 15 ===")
w = [f for f in F if f["check"] == "wording"]
for f in w[:15]:
    print(f"  {f['slug']:42} {f['msg']}")
print(f"  ... total wording findings: {len(w)}")
