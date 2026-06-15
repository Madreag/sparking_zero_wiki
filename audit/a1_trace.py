"""Audit Agent 1 — hand-trace cids raw Numeric.json -> characters.json -> page."""
from __future__ import annotations
import json, re, glob, os
import yaml

ROOT = r"C:\vaults\sparking_zero"
DM = os.path.join(ROOT, "data-mined")
RAW = os.path.join(DM, "raw", "masterdata")
CHARDIR = os.path.join(ROOT, "content", "characters")

def load(p):
    with open(p, encoding="utf-8") as f: return json.load(f)

chars = load(os.path.join(DM, "characters.json"))
numeric = load(os.path.join(RAW, "Numeric.json"))
chardata = load(os.path.join(RAW, "CharacterData.json"))

FM_RE = re.compile(r"^---\n(.*?)\n---\n?(.*)$", re.S)
cid2fm = {}
for path in glob.glob(os.path.join(CHARDIR, "*.md")):
    raw = open(path, encoding="utf-8").read()
    m = FM_RE.match(raw)
    if not m: continue
    fm = yaml.safe_load(m.group(1))
    if fm and fm.get("charId"):
        cid2fm[fm["charId"]] = (os.path.splitext(os.path.basename(path))[0], fm)

def props(entry):
    return entry[0].get("Properties") if entry else {}

# raw field -> (json key, page key)
MAP = [
    ("Life","hp","hp"),
    ("SPChargeSpeed","kiChargeSpeed","kiChargeSpeed"),
    ("SPAutoRecoverySpeed","kiAutoRecovery","kiAutoRecovery"),
    ("SPAutoRecoveryLimit","kiAutoRecoveryLimit","kiAutoRecoveryLimit"),
    ("InitialSP","initialKi","initialKi"),
    ("BlastStock","maxSkillStock","maxSkillStock"),
    ("InitialBlastStock","initialSkillStock","initialSkillStock"),
    ("SparkingModeGaugeDecreaseSpeed","sparkingDrainPerSec","sparkingDrainPerSec"),
    ("BulletNum","kiBlastShots","kiBlastShots"),
]

def norm(v):
    if isinstance(v, bool): return v
    if isinstance(v, float) and v.is_integer(): return int(v)
    return v

def eq(a,b):
    a,b=norm(a),norm(b)
    if isinstance(a,(int,float)) and isinstance(b,(int,float)): return abs(a-b)<1e-9
    return a==b

TRACE = ["0000_00","0620_00","0790_00","3050_00","3100_03","3140_00","0700_01",
         "0680_00","0920_00","3040_00","0670_00","3020_00","0050_00","0881_00",
         "0110_00","0100_00"]

for cid in TRACE:
    slug, fm = cid2fm.get(cid,(None,None))
    c = chars.get(cid, {})
    nraw = numeric.get(f"Numeric_{cid}")
    p = props(nraw) if nraw else None
    print("="*78)
    print(f"{cid}  {slug}  name={c.get('name')!r}  source={fm.get('source') if fm else '?'} era={fm.get('era') if fm else '?'}")
    print(f"  Numeric_{cid} present in raw: {nraw is not None}   hasNumeric(json)={c.get('hasNumeric')}  hasCharacterData={c.get('hasCharacterData')}")
    if p is None:
        print("  !! NO Numeric asset in raw -> all ki/hp fields null")
    print(f"  {'rawField':<32}{'raw':>10}{'json':>10}{'page':>10}  verdict")
    for rawk, jk, pk in MAP:
        rv = p.get(rawk) if p else None
        jv = c.get(jk)
        pv = fm.get(pk) if fm else None
        ok_rj = eq(rv, jv)
        # page omits None; so page should equal json when json not None, else absent
        if jv is None:
            ok_jp = (pv is None)
        else:
            ok_jp = eq(jv, pv)
        verdict = "OK" if (ok_rj and ok_jp) else ("RAW!=JSON" if not ok_rj else "JSON!=PAGE")
        print(f"  {rawk:<32}{str(norm(rv)):>10}{str(norm(jv)):>10}{str(norm(pv)):>10}  {verdict}")

# ---- transform/fusion raw spot checks ----
print("\n" + "#"*78)
print("# TRANSFORM/FUSION RAW SPOT-CHECK (CharacterData -> characters.json edges)")
print("#"*78)
def battle_assets(cid):
    rec = (props(chardata.get(f"CharacterData_{cid}")) or {}).get("CharacterDataAssetRecord") or {}
    return rec.get("BattleAssets") or {}, rec

for cid in ["0620_00","0920_00","0100_00","3040_00"]:
    slug, fm = cid2fm.get(cid,(None,None))
    c = chars.get(cid, {})
    ba, rec = battle_assets(cid)
    print(f"\n{cid} {slug} ({c.get('name')!r})")
    fc = ba.get("FormChange"); fus = ba.get("Fusion"); pot = ba.get("Potara")
    def keys(x):
        if not x: return []
        xs = x if isinstance(x,list) else [x]
        out=[]
        for e in xs:
            if not e: continue
            tgt=(e.get("ChangeCharacter") or {}).get("Key")
            partners=[]
            for pk in ("FusionCharacters","PotaraCharacters"):
                for pp in e.get(pk,[]) or []:
                    if isinstance(pp,dict) and pp.get("Key"): partners.append(pp["Key"])
            out.append((tgt, e.get("ConsumeBlastStock"), e.get("HpRecovery"), partners))
        return out
    print(f"  raw FormChange: {keys(fc)}")
    print(f"  raw Fusion:     {keys(fus)}")
    print(f"  raw Potara:     {keys(pot)}")
    print(f"  json formChanges: {[(e['to'],e.get('consumeBlastStock'),e.get('kind')) for e in c.get('formChanges',[])]}")
    print(f"  json fusions:     {[(e['to'],e.get('consumeBlastStock'),e.get('kind'),e.get('partners')) for e in c.get('fusions',[])]}")
    print(f"  page transformsTo: {[(t.get('target'),t.get('targetSlug'),t.get('cost'),t.get('kind')) for t in (fm.get('transformsTo') or [])]}")

# ---- krillin / frost: confirm BLASTSKILL name locres gap ----
print("\n" + "#"*78)
print("# KRILLIN/FROST dropped-super root cause (raw BlastSkill assets present, names null)")
print("#"*78)
blastskill = load(os.path.join(RAW, "BlastSkill.json"))
locres = load(os.path.join(DM, "raw", "locres_en.json"))
data_loc = locres["SparkingZERO/Content/Localization/Data/en/Data.locres"]
bs_names = data_loc["ST_BLASTSKILL"]
for cid in ["0050_00","0881_00"]:
    print(f"\n{cid} {cid2fm.get(cid,(None,None))[0]}")
    for i in (1,2):
        asset = blastskill.get(f"BlastSkill{i}_{cid}")
        nm = bs_names.get(f"ST_BLASTSKILL_{cid}_actSPM{i}")
        print(f"  SPM{i}: asset_present={asset is not None}  locres_name={nm!r}")
