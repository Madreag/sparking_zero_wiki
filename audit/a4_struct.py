import json, os, collections
ROOT = r"c:\vaults\sparking_zero"
chars = json.load(open(os.path.join(ROOT, "data-mined", "characters.json"), encoding="utf-8"))
print("top type:", type(chars).__name__)
if isinstance(chars, dict):
    print("top keys (first 20):", list(chars.keys())[:20])
    # peek one value
    k0 = list(chars.keys())[0]
    v0 = chars[k0]
    print("first value type:", type(v0).__name__)
    if isinstance(v0, dict):
        print("first record keys:", list(v0.keys()))

def walk(o, depth=0):
    # find any dict that has a key containing 'pursuit'
    found = []
    if isinstance(o, dict):
        for k, v in o.items():
            if "pursuit" in str(k).lower():
                found.append((k, v))
            found += walk(v, depth+1)
    elif isinstance(o, list):
        for it in o[:5]:
            found += walk(it, depth+1)
    return found

hits = walk(chars)
print("\nsample pursuit field hits (first 12):")
for k, v in hits[:12]:
    print(f"  {k} = {v}")

# Now collect per-character pursuitLimitLightning style across records.
# Determine record container:
records = []
if isinstance(chars, dict):
    for k, v in chars.items():
        if isinstance(v, dict):
            records.append(v)
print("\nrecord count (dict values):", len(records))
for field in ["pursuitLimitLightning", "pursuitLimitLightningAttack", "pursuitBaseLimit",
              "pursuitLimitDragonHoming", "pursuitLimitVanishingAttack",
              "PursuitLimitLightningAttack", "PursuitBaseLimit"]:
    dist = collections.Counter(r.get(field) for r in records if isinstance(r, dict) and field in r)
    if dist:
        print(f"{field}: {dict(dist)}")
