"""Parse raw CUE4Parse exports into consolidated reference JSON tables.

Inputs:  data-mined/raw/  (masterdata/*.json, stringtables.json, locres_en.json)
Outputs: data-mined/*.json (characters, stages, ranks, dlc, wishes, shop,
         blast_index, skills_catalog, system_constants, transformations)

FRESH-USMAP FIELD SEMANTICS (verified by value-matching 2026-06-10):
  Numeric.Life                              -> max HP
  Numeric.SPChargeSpeed                     -> MANUAL ki-charge speed (0 = cannot charge; androids)
  Numeric.SPAutoRecoverySpeed               -> passive ki recovery /s
  Numeric.SPAutoRecoveryLimit               -> passive-recovery cap (energy)
  Numeric.InitialSP                         -> starting ki (energy)
  Numeric.BlastStock / InitialBlastStock    -> max / starting skill stocks
  Numeric.SparkingModeGaugeDecreaseSpeed    -> Sparking!-mode gauge drain /s
  (The launch-era usmap mislabeled these; the old "ZCounterSPCost 2800" was
   actually SparkingModeGaugeDecreaseSpeed. Vanish cost is NOT in the files.)

DAMAGE: per-move datamined values exist where assets override defaults:
  BulletSetting/BulletParam_<cid>_act*  -> Power / Shave(chip) / BeamPower / BeamShave / ExpendEnergy
  BulletSetting/Common                  -> generic ki-blast defaults (e.g. 200 dmg / 40 chip / 2,000 ki)
  Combatives/<cid> Power/ArmorBreakLevel/EnergyGain/HitStop per action
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

RAW = Path(r"C:\vaults\sparking_zero\data-mined\raw")
OUT = Path(r"C:\vaults\sparking_zero\data-mined")


def load(p: Path) -> Any:
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def props(entry) -> dict:
    if not entry:
        return {}
    return entry[0].get("Properties") or {}


def text_of(ftext: dict | None, loc_tables: dict) -> str | None:
    if not isinstance(ftext, dict):
        return None
    key = ftext.get("Key")
    table_id = ftext.get("TableId") or ""
    if not key:
        return ftext.get("CultureInvariantString")
    ns = table_id.split(".")[-1] if table_id else None
    if ns and ns in loc_tables and key in loc_tables[ns]:
        return loc_tables[ns][key]
    for table in loc_tables.values():
        if key in table:
            return table[key]
    return ftext.get("SourceString")


def main() -> None:
    md = RAW / "masterdata"
    locres = load(RAW / "locres_en.json")
    data_loc = locres["SparkingZERO/Content/Localization/Data/en/Data.locres"]
    loc_all: dict[str, dict] = {}
    for f in locres.values():
        for ns, table in f.items():
            loc_all.setdefault(ns, {}).update(table)

    notes: list[str] = []

    chr_names = data_loc["ST_CHR_NAME"]
    chr_full = data_loc["ST_CHR_NAME_FULL"]
    numeric = load(md / "Numeric.json")
    blastskill = load(md / "BlastSkill.json")
    blastult = load(md / "BlastUltimate.json")
    blastforte = load(md / "BlastForte.json")
    chardata = load(md / "CharacterData.json")
    opguide = load(md / "OperationGuide.json")
    bullets = load(md / "BulletSetting" / "BulletParam.json")
    bullets_common = load(md / "BulletSetting" / "Common.json")

    def cid_of(key: str, prefix: str) -> str | None:
        m = re.match(rf"{prefix}_(\d{{4}}_\d{{2}})$", key)
        return m.group(1) if m else None

    ids: set[str] = set()
    for k in chr_names:
        c = cid_of(k, "ST_CHR_NAME")
        if c:
            ids.add(c)
    for src, prefix in ((numeric, "Numeric"), (chardata, "CharacterData")):
        for k in src:
            c = cid_of(k, prefix)
            if c:
                ids.add(c)

    # ---------- operation-guide: blast categories/tags + forte skill descriptions ----------
    LABEL_KEYS = {  # layout headers, not real tags
        "ST_BLAST_CONDITIONS_0002",
        "ST_BLAST_CONDITIONS_0003",
        "ST_BLAST_CONDITIONS_0004",
        "ST_BLAST_CONDITIONS_0005",
        "ST_BLAST_CONDITIONS_0006",
        "ST_BLAST_EXPLANATION_0000",
        "ST_BLAST_EXPLANATION_0001",
        "ST_BLAST_EXPLANATION_0002",
        "ST_BLAST_EXPLANATION_0003",
        "ST_BLAST_EXPLANATION_0004",
        "ST_BLAST_EXPLANATION_0005",
        "ST_BLAST_EXPLANATION_0006",
    }

    def guide_decode(p: dict) -> tuple[str | None, list[str]]:
        """-> (category, tags[]) from a BattleOperationGuide record."""
        data = p.get("BlastOperationGuideData") or {}
        category = None
        tags: list[str] = []
        for cell, ftext in data.items():
            if not isinstance(ftext, dict):
                continue
            key = ftext.get("Key") or ""
            txt = text_of(ftext, loc_all)
            if not txt or txt == "None" or key in LABEL_KEYS:
                continue
            if "BLAST_CATEGORY" in key:
                category = txt
            else:
                tags.append(txt.replace("\n", " ").strip())
        return category, tags

    # GR<cid><slot> -> guide
    blast_guides: dict[tuple[str, str], tuple[str | None, list[str]]] = {}
    slot_map = {"B1": "SPM1", "B2": "SPM2", "B3": "SPM3", "UB": "ULT", "UB2": "ULT2"}
    for k, v in opguide.items():
        m = re.match(r"BattleOperationGuide_GR(\d{4}_\d{2})(B1|B2|B3|UB2|UB)$", k)
        if m:
            blast_guides[(m.group(1), slot_map[m.group(2)])] = guide_decode(props(v))

    # Forte### -> in-game skill description
    forte_desc: dict[str, str] = {}
    for k, v in opguide.items():
        m = re.match(r"BattleOperationGuide_Forte(\d+)$", k)
        if not m:
            continue
        data = (props(v).get("BlastOperationGuideData")) or {}
        for ftext in data.values():
            txt = text_of(ftext, loc_all)
            if txt and txt != "None":
                forte_desc[m.group(1).lstrip("0") or "0"] = txt.replace(
                    "【１】", "(N)"
                ).strip()
                break

    # ---------- per-move datamined combat values ----------
    # bullets: BulletParam_<cid>_act<ACTION...> ; slot inferred from action substring
    def slot_of_action(action: str) -> str | None:
        if "SPM1" in action:
            return "SPM1"
        if "SPM2" in action:
            return "SPM2"
        if "ULT" in action or "UB" in action:
            return "ULT"
        return None

    char_bullets: dict[str, dict[str, list[dict]]] = defaultdict(
        lambda: defaultdict(list)
    )
    for k, v in bullets.items():
        m = re.match(r"BulletParam_(\d{4}_\d{2})_(act.+)$", k)
        if not m:
            continue
        cid, action = m.group(1), m.group(2)
        slot = slot_of_action(action)
        if not slot:
            continue
        p = props(v)
        if not any(p.get(x) for x in ("Power", "BeamPower", "Shave", "BeamShave")):
            continue
        char_bullets[cid][slot].append(
            {
                "action": action,
                "power": p.get("Power"),
                "chip": p.get("Shave"),
                "beamPower": p.get("BeamPower"),
                "beamChip": p.get("BeamShave"),
                "multiHit": p.get("CollisionRevibeNum"),
                "fireLimit": p.get("FireLimit"),
            }
        )

    # combatives per-char action params (Power overrides etc.)
    comb_params: dict[str, dict[str, dict]] = defaultdict(dict)
    comb_dir = md / "Combatives"
    for f in comb_dir.glob("*.json"):
        if f.stem == "Common":
            continue
        cid = f.stem
        try:
            d = load(f)
        except Exception:
            continue
        for k, v in d.items():
            m = re.match(r"Combatives(?:SubParam)?_\d{4}_\d{2}_(act.+)$", k)
            if not m:
                continue
            action = m.group(1)
            p = props(v)
            keep = {
                kk: p[kk]
                for kk in (
                    "Power",
                    "ArmorBreakLevel",
                    "EnergyGain",
                    "HitStop",
                    "GuardDown",
                    "bSuperCounterAvoidable",
                    "SuperZCounterTakeType",
                    "bZCounterAvoidable",
                    "SmashLevelGaugeIncrement",
                    "bIsSlashAttack",
                )
                if kk in p
            }
            if keep:
                cur = comb_params[cid].setdefault(action, {})
                cur.update(keep)

    # generic ki-blast defaults (Common bullets) — system reference table
    generic_bullets = []
    for k, v in bullets_common.items():
        p = props(v)
        if p.get("Power") or p.get("BeamPower"):
            generic_bullets.append(
                {
                    "action": (p.get("ActionComment") or {}).get("Key")
                    or k.replace("BulletParam_Common_", ""),
                    "power": p.get("Power"),
                    "chip": p.get("Shave"),
                    "beamPower": p.get("BeamPower"),
                    "beamChip": p.get("BeamShave"),
                    "kiCost": p.get("ExpendEnergy"),
                }
            )

    # ---------- characters ----------
    bs_names = data_loc["ST_BLASTSKILL"]
    bu_names = data_loc["ST_BLASTULTIMATE"]
    forte_names_tbl = data_loc.get("ST_BLASTFORTE", {})

    def name_of(c: str) -> str | None:
        return chr_full.get(f"ST_CHR_NAME_FULL_{c}") or chr_names.get(
            f"ST_CHR_NAME_{c}"
        )

    def comb_for(cid: str, slot: str) -> dict:
        """merged combatives overrides for actions belonging to a blast slot"""
        out: dict = {}
        for action, vals in comb_params.get(cid, {}).items():
            if slot_of_action(action) == slot:
                for kk, vv in vals.items():
                    if kk == "Power":
                        out.setdefault("meleePowers", []).append(vv)
                    else:
                        out.setdefault(kk, vv)
        return out

    characters = {}
    for cid in sorted(ids):
        name = chr_names.get(f"ST_CHR_NAME_{cid}")
        full = chr_full.get(f"ST_CHR_NAME_FULL_{cid}")
        num = props(numeric.get(f"Numeric_{cid}"))
        supers = []
        for slot_i in (1, 2):
            slot = f"SPM{slot_i}"
            nm = bs_names.get(f"ST_BLASTSKILL_{cid}_act{slot}")
            asset = props(blastskill.get(f"BlastSkill{slot_i}_{cid}"))
            if not (nm or asset):
                continue
            cat, tags = blast_guides.get((cid, slot), (None, []))
            entry = {
                "slot": slot,
                "name": nm,
                "kiCost": asset.get("ExpendEnergy"),
                "triggerKiCost": asset.get("TriggerExpendEnergy"),
                "speedImpact": asset.get("bCanSpeedImpact"),
                "blastImpact": asset.get("bCanBlastImpact"),
                "blastImpactPower": asset.get("BlastImpactPower"),
                "weakSpecialShield": asset.get("bWeakSpecialShield"),
                "zCounterType": (asset.get("BlastSkillParamData") or {})
                .get("SuperZCounterType", "")
                .split("::")[-1]
                or None
                if asset.get("BlastSkillParamData")
                else None,
                "category": cat,
                "tags": tags,
                "bullets": char_bullets.get(cid, {}).get(slot, []),
                "combatives": comb_for(cid, slot),
            }
            supers.append(entry)
        ult_name = bu_names.get(f"ST_BLASTULTIMATE_{cid}")
        ult_asset = props(blastult.get(f"BlastUltimate_{cid}")) or props(
            blastult.get(f"BlastUltimate2_{cid}")
        )
        ultimate = None
        if ult_name or ult_asset:
            cat, tags = blast_guides.get((cid, "ULT"), (None, []))
            ultimate = {
                "name": ult_name,
                "kiCost": ult_asset.get("ExpendEnergy"),
                "category": cat,
                "tags": tags,
                "bullets": char_bullets.get(cid, {}).get("ULT", []),
                "combatives": comb_for(cid, "ULT"),
            }

        characters[cid] = {
            "id": cid,
            "baseId": cid.split("_")[0],
            "formCode": cid.split("_")[1],
            "name": name,
            "fullName": full,
            "hp": num.get("Life"),
            "kiChargeSpeed": num.get("SPChargeSpeed"),
            "kiAutoRecovery": num.get("SPAutoRecoverySpeed"),
            "kiAutoRecoveryLimit": num.get("SPAutoRecoveryLimit"),
            "initialKi": num.get("InitialSP"),
            "maxSkillStock": num.get("BlastStock"),
            "initialSkillStock": num.get("InitialBlastStock"),
            "sparkingDrainPerSec": num.get("SparkingModeGaugeDecreaseSpeed"),
            "kiBlastShots": num.get("BulletNum"),
            "rushKiBlastLimit": num.get("RushBulletLimit"),
            "smashChargeSpeeds": num.get("AttackChargeSpeedsBySmashLevel"),
            "pursuitBaseLimit": num.get("PursuitBaseLimit"),
            "pursuitAddAtSparking": num.get("PursuitBaseLimitAddAtSparking"),
            "skillGaugeGains": {
                "vanishExchangeRate": num.get("RepelSkillGaugeGainRate"),
                "attackBreak": num.get("AttackBreakSkillGaugeGain"),
                "fastAvoid": num.get("FastAvoidSkillGaugeGain"),
                "throwBreak": num.get("ThrowBreakSkillGaugeGain"),
                "hitFromBehind": num.get("BackAttackedSkillGaugeGain"),
                "lastHPGauge": num.get("LastOneHPSkillGaugeGain"),
                "impactStart": num.get("ImpactStartSkillGaugeGain"),
            }
            if num
            else None,
            "supers": supers,
            "ultimate": ultimate,
            "hasNumeric": bool(num),
            "hasCharacterData": f"CharacterData_{cid}" in chardata,
        }

    # ---------- transformations / fusions + S1 skills + story tags ----------
    transformations = []
    for cid in sorted(ids):
        rec = (
            props(chardata.get(f"CharacterData_{cid}")).get("CharacterDataAssetRecord")
            or {}
        )
        battle = rec.get("BattleAssets") or {}
        c = characters.get(cid)
        if not c:
            continue
        story = rec.get("StorySettingParameter") or {}
        c["gender"] = (
            story.get("Gender")
            or rec.get("StorySettingParameter", {}).get("Gender")
            or ""
        ).split("::")[-1] or None
        c["seriesKey"] = (story.get("SeriesTitle") or {}).get("Key")
        c["unlockType"] = (rec.get("UnLockType") or "").split("::")[-1] or None

        def edge(entry: dict, kind: str):
            tgt = (entry.get("ChangeCharacter") or {}).get("Key")
            if not tgt:
                return None
            partners = []
            for pk in ("FusionCharacters", "PotaraCharacters"):
                for p in entry.get(pk, []) or []:
                    if isinstance(p, dict) and p.get("Key"):
                        partners.append(p["Key"])
            stock = entry.get("ConsumeBlastStock")
            same_base = tgt.split("_")[0] == cid.split("_")[0]
            resolved_kind = (
                "revert" if (kind == "transform" and stock == 0 and same_base) else kind
            )
            e = {
                "from": cid,
                "fromName": name_of(cid),
                "to": tgt,
                "toName": name_of(tgt),
                "kind": resolved_kind,
                "consumeBlastStock": stock,
                "hpRecovery": entry.get("HpRecovery"),
                "addMaxHp": entry.get("AddMaxHP"),
                "coolTimeSec": entry.get("CoolTime"),
                "noHealAfterSecondUse": entry.get("bDisableRecoveryAfterTheSecondTime"),
                "partners": partners,
                "partnerNames": [name_of(p) for p in partners],
            }
            transformations.append(e)
            return e

        fc = battle.get("FormChange")
        fcs = fc if isinstance(fc, list) else ([fc] if fc else [])
        c["formChanges"] = [e for x in fcs if x for e in [edge(x, "transform")] if e]
        fus = battle.get("Fusion")
        fus = fus if isinstance(fus, list) else ([fus] if fus else [])
        pot = battle.get("Potara")
        pot = pot if isinstance(pot, list) else ([pot] if pot else [])
        c["fusions"] = [e for x in fus if x for e in [edge(x, "fusion")] if e] + [
            e for x in pot if x for e in [edge(x, "potara")] if e
        ]

        s1 = []
        for slot in (1, 2):
            fp = props(blastforte.get(f"BlastForte{slot}_{cid}"))
            if not fp:
                continue
            pd = fp.get("BlastForteParamData") or {}
            key = (pd.get("BlastForteName") or {}).get("Key") or ""
            nm = forte_names_tbl.get(key) or forte_names_tbl.get(
                key.replace("ST_BlASTFORTE", "ST_BLASTFORTE")
            )
            idx_m = re.search(r"(\d+)$", key)
            fidx = (idx_m.group(1).lstrip("0") or "0") if idx_m else None
            guide_ref = (fp.get("BlastOperationData") or {}).get("ObjectName") or ""
            gm = re.search(r"Forte(\d+)", guide_ref)
            gidx = (gm.group(1).lstrip("0") or "0") if gm else None
            flags = []
            if pd.get("bIsImpossileGuard"):
                flags.append("unblockable")
            if pd.get("bNoAutoGuard"):
                flags.append("no-auto-guard")
            if pd.get("bNonLockUsable"):
                flags.append("usable-unlocked")
            s1.append(
                {
                    "slot": f"S{slot}",
                    "name": nm,
                    "nameKey": key,
                    "skillCost": fp.get("ExpendBlastStock"),
                    "triggerSkillCost": fp.get("TriggerExpendBlastStock"),
                    "type": (pd.get("Type") or {}).get("Key"),
                    "flags": flags,
                    "descIdx": gidx or fidx,
                    "desc": forte_desc.get(gidx or "") or None,
                }
            )
        c["s1Skills"] = s1

    # ---------- DLC ----------
    dlc_raw = load(md / "DownLoadContents.json")
    dlc = {}
    for k, v in sorted(dlc_raw.items()):
        p = props(v)
        name_text = text_of(p.get("Name"), loc_all) or ""
        char_ids = [
            c.get("Key") for c in p.get("CharacterIds", []) if isinstance(c, dict)
        ]
        dlc[k] = {
            "id": k,
            "title": name_text.splitlines()[0].strip() if name_text else None,
            "fullText": name_text,
            "characterIds": char_ids,
            "characters": [characters.get(c, {}).get("name") for c in char_ids],
            "summonTickets": p.get("SummonTickets"),
        }

    char_source: dict[str, str] = {}
    for k, d in dlc.items():
        if (
            k == "DLC_900"
        ):  # internal ops bundle ("DLC for operation") = base-game shop unlocks
            continue
        for cid2 in d["characterIds"]:
            char_source.setdefault(cid2, d["title"] or k)
    for cid2, c in characters.items():
        c["dlcPack"] = char_source.get(cid2)

    # ---------- shop (+ per-character unlock price) ----------
    shop_base = load(md / "ShopBaseItem.json")
    shop_sales = load(md / "ShopSalesItem.json")
    shop = []
    char_price: dict[str, int] = {}
    for k, v in sorted(shop_base.items()):
        p = props(v)
        sale = props(shop_sales.get(k.replace("ShopBase", "ShopSales")))
        unlock_chars = [
            c.get("Key") for c in p.get("UnlockCharacters", []) if isinstance(c, dict)
        ]
        price = sale.get("Price")
        if price is not None and (p.get("ContentsType") or "").endswith("Character"):
            for uc in unlock_chars:
                char_price.setdefault(uc, price)
        shop.append(
            {
                "id": k,
                "contentsType": (p.get("ContentsType") or "").split("::")[-1] or None,
                "unlockCharacters": unlock_chars,
                "unlockCharacterNames": [
                    characters.get(c, {}).get("name") for c in unlock_chars
                ],
                "sales": sale or None,
            }
        )
    for cid2, c in characters.items():
        c["shopPrice"] = char_price.get(cid2)

    # ---------- ranks / stages / wishes ----------
    ranks_raw = load(md / "RankMatchRank.json")
    ranks = [
        {"id": k, "name": text_of(props(ranks_raw[k]).get("RankName"), loc_all)}
        for k in sorted(ranks_raw)
    ]
    stages = [
        {"key": k, "id": k.replace("ST_MAP_", ""), "name": v}
        for k, v in sorted(data_loc["ST_MAP_NAME"].items())
    ]
    wish_contents = props(
        load(md / "WishComeTrue.json").get("WishComeTrueContentsDataAsset")
    )
    wishes = []
    for rec in wish_contents.get("Records", []):
        val = rec.get("Value") or {}
        cats = []
        for cat in val.get("Categories", []):
            rewards = [
                {
                    "rewardId": (r.get("RewardId") or {}).get("Key"),
                    "caption": text_of(r.get("caption"), loc_all),
                }
                for r in (cat.get("Value") or {}).get("RewardList", [])
            ]
            cats.append(
                {"category": (cat.get("Key") or "").split("::")[-1], "rewards": rewards}
            )
        wishes.append(
            {
                "dragon": rec.get("Key"),
                "dragonType": (val.get("DragonType") or "").split("::")[-1],
                "categories": cats,
            }
        )

    # ---------- skills catalog (with datamined descriptions where mapped) ----------
    skills_catalog = []
    name_desc: dict[str, Counter] = defaultdict(Counter)
    for c in characters.values():
        for sk in c.get("s1Skills") or []:
            if sk.get("name") and sk.get("desc"):
                name_desc[sk["name"]][sk["desc"]] += 1
    for k, v in sorted(data_loc.get("ST_BLASTFORTE", {}).items()):
        desc_counter = name_desc.get(v)
        skills_catalog.append(
            {
                "key": k,
                "index": k.split("_")[-1],
                "name": v,
                "descDatamined": desc_counter.most_common(1)[0][0]
                if desc_counter
                else None,
            }
        )

    # ---------- blast index ----------
    blast_index: dict[tuple[str, str], dict] = {}
    for cid2, c in characters.items():
        if not c["name"]:
            continue
        for s in c["supers"]:
            if not s["name"]:
                continue
            e = blast_index.setdefault(
                (s["name"], "super"), {"name": s["name"], "class": "super", "users": []}
            )
            e["users"].append(
                {
                    "charId": cid2,
                    "character": c["name"],
                    "kiCost": s["kiCost"],
                    "triggerKiCost": s.get("triggerKiCost"),
                    "slot": s["slot"],
                    "category": s.get("category"),
                    "tags": s.get("tags") or [],
                    "bullets": s.get("bullets") or [],
                    "combatives": s.get("combatives") or {},
                    "speedImpact": s.get("speedImpact"),
                    "blastImpact": s.get("blastImpact"),
                }
            )
        u = c.get("ultimate")
        if u and u.get("name"):
            e = blast_index.setdefault(
                (u["name"], "ultimate"),
                {"name": u["name"], "class": "ultimate", "users": []},
            )
            e["users"].append(
                {
                    "charId": cid2,
                    "character": c["name"],
                    "kiCost": u.get("kiCost"),
                    "slot": "ULT",
                    "category": u.get("category"),
                    "tags": u.get("tags") or [],
                    "bullets": u.get("bullets") or [],
                    "combatives": u.get("combatives") or {},
                }
            )
    blasts = sorted(blast_index.values(), key=lambda b: (b["name"], b["class"]))

    # ---------- system constants ----------
    def dist(field: str):
        d = defaultdict(list)
        for c in characters.values():
            v = c.get(field)
            if v is not None and c["name"]:
                d[v].append(c["name"])
        return [
            {"value": k, "count": len(vs), "examples": sorted(set(vs))[:10]}
            for k, vs in sorted(d.items())
        ]

    system_constants = {
        "hpDistribution": [
            {"hp": r["value"], "count": r["count"], "examples": r["examples"]}
            for r in dist("hp")
        ],
        "kiChargeSpeedDistribution": dist("kiChargeSpeed"),
        "kiAutoRecoveryDistribution": dist("kiAutoRecovery"),
        "sparkingDrainDistribution": dist("sparkingDrainPerSec"),
        "maxSkillStockDistribution": dist("maxSkillStock"),
        "initialSkillStockDistribution": dist("initialSkillStock"),
        "initialKiDistribution": dist("initialKi"),
        "kiBlastShotsDistribution": dist("kiBlastShots"),
        "genericKiBlasts": sorted(generic_bullets, key=lambda b: b["action"])[:40],
    }

    notes.append(
        "FRESH-USMAP semantics verified by value-matching: SPChargeSpeed = manual charge "
        "(0 for androids), SparkingModeGaugeDecreaseSpeed = the old mislabeled '2800'. "
        "Vanish/Z-Counter ki cost is NOT present in any parameter table (checked Numeric, "
        "Action_actSZC*, Combatives) — community-measured ≈0.5 bar."
    )
    notes.append(
        "Per-move damage IS partially datamined: BulletParam overrides (606 incl. 47 ultimates) "
        "carry Power/Shave/BeamPower/BeamShave; Combatives carries per-action Power/ArmorBreak/"
        "EnergyGain where overridden; BulletSetting/Common has generic ki-blast defaults. "
        "Moves without overrides inherit blueprint class defaults (not in these tables)."
    )
    notes.append(
        "DP cost is not in the game files; community-sourced via enrichment (research/02)."
    )

    OUT.mkdir(exist_ok=True)
    dumps = {
        "characters.json": characters,
        "dlc.json": dlc,
        "shop.json": shop,
        "ranks.json": ranks,
        "stages.json": stages,
        "wishes.json": wishes,
        "skills_catalog.json": skills_catalog,
        "blast_index.json": blasts,
        "system_constants.json": system_constants,
        "transformations.json": transformations,
    }
    for fname, data in dumps.items():
        with open(OUT / fname, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=1, ensure_ascii=False)
        count = len(data) if hasattr(data, "__len__") else "-"
        print(f"{fname}: {count} entries, {(OUT / fname).stat().st_size:,} bytes")

    with open(OUT / "PARSE_NOTES.md", "w", encoding="utf-8") as f:
        f.write("# Parse notes\n\n")
        for n in notes:
            f.write(f"- {n}\n")

    named = sum(1 for c in characters.values() if c["name"])
    with_hp = sum(1 for c in characters.values() if c["hp"] is not None)
    with_dmg = sum(
        1
        for c in characters.values()
        if any(
            (s.get("bullets") or s.get("combatives", {}).get("meleePowers"))
            for s in c["supers"]
        )
        or (
            c.get("ultimate")
            and (
                c["ultimate"].get("bullets")
                or c["ultimate"].get("combatives", {}).get("meleePowers")
            )
        )
    )
    cats = sum(
        1 for c in characters.values() for s in c["supers"] if s.get("category")
    ) + sum(
        1
        for c in characters.values()
        if c.get("ultimate") and c["ultimate"].get("category")
    )
    descs = sum(1 for s in skills_catalog if s.get("descDatamined"))
    print(
        f"\ncharacters: {len(characters)} ids, {named} named, {with_hp} with HP, "
        f"{with_dmg} with datamined move damage; blast slots with category: {cats}; "
        f"skills with datamined description: {descs}/{len(skills_catalog)}"
    )


if __name__ == "__main__":
    main()
