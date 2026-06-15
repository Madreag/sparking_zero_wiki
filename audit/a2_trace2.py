"""Authoritative damage trace with PRECISE cid (via page characterSlug).
Also detects: embedded-cid mismatches in Combatives keys, and groups by category/source."""
import json, re
from collections import defaultdict, Counter
from pathlib import Path
import yaml

ROOT = Path(r"C:\vaults\sparking_zero")
RAW = ROOT / "data-mined" / "raw" / "masterdata"
chars = json.load(open(ROOT / "data-mined" / "characters.json", encoding="utf-8"))


def props(e):
    return (e[0].get("Properties") or {}) if e else {}


def slugify(s):
    s = s.lower(); s = re.sub(r"['’!.]", "", s); s = re.sub(r"[^a-z0-9]+", "-", s); return s.strip("-")


# cid<->slug
slugs = {}; used = {}
for cid, c in sorted(chars.items()):
    if not c["name"]: continue
    label = c["fullName"] or c["name"]; s = slugify(label)
    if s in used and used[s] != cid: s = f"{s}-{cid.replace('_','-')}"
    used[s] = cid; slugs[cid] = s
slug2cid = {v: k for k, v in slugs.items()}


def slot_of(a):
    return "SPM1" if "SPM1" in a else "SPM2" if "SPM2" in a else ("ULT" if ("ULT" in a or "UB" in a) else None)


# raw bullets per cid+slot
raw_b = json.load(open(RAW / "BulletSetting" / "BulletParam.json", encoding="utf-8"))
bull = defaultdict(lambda: defaultdict(list))
for k, v in raw_b.items():
    m = re.match(r"BulletParam_(\d{4}_\d{2})_(act.+)$", k)
    if not m: continue
    cid, a = m.group(1), m.group(2); slot = slot_of(a)
    if not slot: continue
    p = props(v)
    if not any(p.get(x) for x in ("Power", "BeamPower", "Shave", "BeamShave")): continue
    bull[cid][slot].append((k, p.get("Power"), p.get("BeamPower"), p.get("Shave"), p.get("BeamShave"), p.get("CollisionRevibeNum")))

_mc = {}
def melee(cid, slot):
    key = (cid, slot)
    if key in _mc: return _mc[key]
    f = RAW / "Combatives" / f"{cid}.json"; out = []
    if f.exists():
        d = json.load(open(f, encoding="utf-8"))
        for k, v in d.items():
            m = re.match(r"Combatives(?:SubParam)?_(\d{4}_\d{2})_(act.+)$", k)
            if not m: continue
            if slot_of(m.group(2)) != slot: continue
            p = props(v)
            if "Power" in p and p["Power"]:
                out.append((k, m.group(1), p["Power"]))
    _mc[key] = out; return out


CONTENT = ROOT / "content" / "blasts"
rows = []
for f in sorted(CONTENT.glob("*.md")):
    raw = f.read_text(encoding="utf-8")
    fm = yaml.safe_load(re.match(r"^---\n(.*?)\n---", raw, re.S).group(1))
    for u in fm.get("users") or []:
        if u.get("damage"):
            rows.append((f.stem, fm.get("category"), fm.get("class"), u))

embed_mismatch = []
src_counter = Counter()
detail_rows = []
for slug, cat, cls, u in rows:
    cid = slug2cid.get(u.get("characterSlug"))
    slot = u.get("notes")
    bl = bull.get(cid, {}).get(slot, [])
    me = melee(cid, slot)
    bull_max = 0; bestb = None
    for t in bl:
        cand = max(x for x in (t[2], t[1], 0) if x is not None)
        if cand > bull_max: bull_max = cand; bestb = t
    melee_max = max([p for (_, _, p) in me], default=0)
    if melee_max and (bull_max == 0 or melee_max > bull_max):
        src = "Combatives"
        mk = [(k, ec, p) for (k, ec, p) in me if p == melee_max][0]
        detail = f"{mk[0]} Power={mk[2]}"
        if mk[1] != cid:
            embed_mismatch.append((slug, u.get("character"), cid, mk[0]))
    else:
        src = "BulletParam"
        k, pw, bpw, sh, bsh, mh = bestb
        detail = f"{k} Power={pw} BeamPower={bpw} Shave={sh} BeamShave={bsh} Revibe={mh}"
    src_counter[src] += 1
    detail_rows.append((slug, u.get("character"), cid, slot, cat, cls, u.get("damage"), u.get("chip"), u.get("hits"), src, detail))

print(f"damage rows: {len(rows)}  by source: {dict(src_counter)}")
print(f"\nEMBEDDED-CID MISMATCHES (Combatives key cid != char file cid): {len(embed_mismatch)}")
for slug, ch, cid, k in embed_mismatch:
    print(f"   {slug:40} {ch:22} file-cid={cid}  key={k}")

# print a curated 24-blast spread for the report
print("\n=== CURATED TRACE SAMPLE (beam/rush/fire/unblockable/multi-hit/high-dmg) ===")
pick = [
 "kamehameha-super","final-flash-super","final-kamehameha-super","special-beam-cannon-ultimate",
 "maximum-flasher-super","planet-geyser-ultimate","stardust-blaster-super","tri-beam-super",
 "wolf-fang-fist-super","charge-super","dynamite-kick-super","drain-life-cell-ultimate",
 "spirit-bomb-ultimate","big-bang-attack-ultimate","final-explosion-ultimate","revenge-death-ball-ultimate",
 "super-ghost-kamikaze-attack-ultimate","chain-destructo-disc-ultimate","assault-rain-super","chou-makouhou-barrage-super",
 "evil-containment-wave-ultimate","mr-buu-arrives-ultimate","photon-strike-super","death-saucer-super",
]
seen=set()
for slug, ch, cid, slot, cat, cls, d, chip, hits, src, detail in detail_rows:
    if slug in pick and slug not in seen:
        seen.add(slug)
        print(f"  {slug:40} {ch:18} {cid}/{slot} {cls:8} cat={str(cat):22} d={d} chip={chip} hits={hits}\n      RAW {src}: {detail}")
