"""Generate data-driven content pages (markdown + frontmatter) from data-mined JSON.

Collections generated here: characters, blasts, skills (catalog stubs), stages, shop.
Curated collections (mechanics, patches, dlc, guides, game-modes, episode-battles,
glossary) are hand-written separately.

Re-runnable: pages are fully regenerated each run (gen owns these directories).
Enrichment overlays (DP costs, eras, classes, tiers) are read from
data-mined/enrichment/*.json when present so manual/agent-curated facts survive regen.
"""

from __future__ import annotations

import json
import re
from collections import Counter, defaultdict
from pathlib import Path
from typing import Any

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
CONTENT = ROOT / "content"

AS_OF = "v2.2 (2026-05-26 update)"
AS_OF_DATE = "2026-05-26"
TODAY = "2026-06-10"
GAME_SOURCE = "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"


def load(p: Path, default=None) -> Any:
    if not p.exists():
        return default
    with open(p, encoding="utf-8") as f:
        return json.load(f)


def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")


def yml(v, indent=0) -> str:
    """Tiny YAML emitter for our frontmatter shapes (scalars, lists, dicts)."""
    pad = "  " * indent
    if isinstance(v, dict):
        lines = []
        for k, val in v.items():
            if val is None or (isinstance(val, (list, dict)) and not val):
                continue
            if isinstance(val, (dict, list)):
                lines.append(f"{pad}{k}:")
                lines.append(yml(val, indent + 1))
            else:
                lines.append(f"{pad}{k}: {scalar(val)}")
        return "\n".join(lines)
    if isinstance(v, list):
        lines = []
        for item in v:
            if isinstance(item, (dict, list)):
                body = yml(item, indent + 1)
                first, *rest = body.split("\n")
                lines.append(f"{pad}- {first.strip()}")
                lines.extend(rest)
            else:
                lines.append(f"{pad}- {scalar(item)}")
        return "\n".join(lines)
    return f"{pad}{scalar(v)}"


def scalar(v) -> str:
    if isinstance(v, bool):
        return "true" if v else "false"
    if isinstance(v, (int, float)):
        if isinstance(v, float) and v.is_integer():
            return str(int(v))
        return str(v)
    s = str(v)
    return json.dumps(s, ensure_ascii=False)


def write_page(dirname: str, slug: str, front: dict, body: str):
    d = CONTENT / dirname
    d.mkdir(parents=True, exist_ok=True)
    fm = yml(front)
    with open(d / f"{slug}.md", "w", encoding="utf-8") as f:
        f.write(f"---\n{fm}\n---\n{body.strip()}\n")


def fmt(n) -> str:
    if n is None:
        return "—"
    if isinstance(n, float) and n.is_integer():
        n = int(n)
    if isinstance(n, int):
        return f"{n:,}"
    return str(n)


def main() -> None:
    chars: dict = load(DM / "characters.json", {})
    blasts: list = load(DM / "blast_index.json", [])
    skills_catalog: list = load(DM / "skills_catalog.json", [])
    stages: list = load(DM / "stages.json", [])
    shop: list = load(DM / "shop.json", [])
    transforms: list = load(DM / "transformations.json", [])

    enrich = load(DM / "enrichment" / "characters.json", {}) or {}
    # strengths/weaknesses overlays (sw_a = ids < 0500, sw_b = ids >= 0500)
    for sw_file in ("sw_a.json", "sw_b.json"):
        for cid, sw in (load(DM / "enrichment" / sw_file, {}) or {}).items():
            if cid in enrich and isinstance(sw, dict):
                for k in (
                    "summary",
                    "playstyle",
                    "strengths",
                    "weaknesses",
                    "howToFight",
                ):
                    if sw.get(k) and not enrich[cid].get(k):
                        enrich[cid][k] = sw[k]
                # sw summaries are richer than the original one-liners; prefer them
                if sw.get("summary"):
                    enrich[cid]["summary"] = sw["summary"]

    # ---------- characters ----------
    # group forms by baseId; choose group label = name of lowest formCode entry
    groups: dict[str, list] = defaultdict(list)
    for c in chars.values():
        if c["name"]:
            groups[c["baseId"]].append(c)
    base_label: dict[str, str] = {}
    for bid, members in groups.items():
        members.sort(key=lambda c: c["formCode"])
        base_label[bid] = members[0]["name"]

    # HP fallback: inherit from sibling form when missing
    def resolved_hp(c) -> tuple[float | None, bool]:
        if c["hp"] is not None:
            return c["hp"], False
        for sib in groups.get(c["baseId"], []):
            if sib["hp"] is not None:
                return sib["hp"], True
        return None, False

    # slug assignment with collision handling
    slugs: dict[str, str] = {}
    used: dict[str, str] = {}
    for cid, c in sorted(chars.items()):
        if not c["name"]:
            continue
        label = c["fullName"] or c["name"]
        s = slugify(label)
        if s in used and used[s] != cid:
            s = f"{s}-{cid.replace('_', '-')}"
        used[s] = cid
        slugs[cid] = s

    def best_damage(move: dict) -> tuple[int | None, int | None, int | None]:
        """-> (damage, chip, hits) from datamined bullet/melee overrides."""
        dmg = chip = hits = None
        for b in move.get("bullets") or []:
            cand = max(
                x for x in (b.get("beamPower"), b.get("power"), 0) if x is not None
            )
            if cand and (dmg is None or cand > dmg):
                dmg = cand
                chip = b.get("beamChip") or b.get("chip")
                hits = b.get("multiHit")
        melee = [p for p in (move.get("combatives") or {}).get("meleePowers", []) if p]
        if melee and (dmg is None or max(melee) > dmg):
            dmg = max(melee)
            chip = None
            hits = None
        return dmg, chip, hits

    def blast_props(move: dict) -> list[str]:
        out: list[str] = []
        if move.get("category"):
            out.append(move["category"])
        for t in move.get("tags") or []:
            if t not in ("Ki Required",):  # implicit for every super/ult
                out.append(t)
        if move.get("speedImpact"):
            out.append("speed-impact")
        if move.get("blastImpact"):
            p = move.get("blastImpactPower")
            out.append(f"blast-impact{f' {p}' if p is not None else ''}")
        if move.get("weakSpecialShield"):
            out.append("weak-vs-shield")
        if move.get("zCounterType") and move["zCounterType"] != "None":
            out.append(f"vanish: {move['zCounterType'].lower()}")
        return out

    n_pages = 0
    for cid, c in sorted(chars.items()):
        if not c["name"]:
            continue
        e = enrich.get(cid, {})
        hp, inherited = resolved_hp(c)
        moveset = []
        for s in c["supers"]:
            if not s["name"]:
                continue
            dmg, chip, hits = best_damage(s)
            moveset.append(
                {
                    "name": s["name"],
                    "type": "blast2",
                    "kiCost": s["kiCost"],
                    "damage": dmg,
                    "hits": hits,
                    "properties": blast_props(s),
                    "notes": " · ".join(
                        x
                        for x in (
                            f"Trigger cost {fmt(s['triggerKiCost'])} ki"
                            if s.get("triggerKiCost") not in (None, s["kiCost"])
                            else None,
                            f"chip {fmt(chip)}" if chip else None,
                        )
                        if x
                    )
                    or None,
                }
            )
        if c.get("ultimate") and c["ultimate"].get("name"):
            u = c["ultimate"]
            dmg, chip, hits = best_damage(u)
            moveset.append(
                {
                    "name": u["name"],
                    "type": "ultimate",
                    "kiCost": u.get("kiCost"),
                    "damage": dmg,
                    "hits": hits,
                    "properties": blast_props(u),
                    "notes": f"chip {fmt(chip)}" if chip else None,
                }
            )
        for sk in c.get("s1Skills") or []:
            if not sk.get("name"):
                continue
            moveset.insert(
                0,
                {
                    "name": sk["name"],
                    "type": "blast1",
                    "skillCost": sk.get("skillCost"),
                    "properties": sk.get("flags", []),
                    "notes": f"slot {sk['slot']}",
                },
            )

        transforms_to = []
        for t in (c.get("formChanges") or []) + (c.get("fusions") or []):
            if not t or not t.get("toName") or t["kind"] == "revert":
                continue
            transforms_to.append(
                {
                    "target": t["toName"],
                    "targetSlug": slugs.get(t["to"]),
                    "cost": t.get("consumeBlastStock"),
                    "kind": "fusion"
                    if t["kind"] in ("fusion", "potara")
                    else "transform",
                }
            )

        front = {
            "slug": slugs[cid],
            "name": c["fullName"] or c["name"],
            "charId": cid,
            "baseCharacter": base_label[c["baseId"]],
            "era": e.get("era", "Story-only"),
            "dp": e.get("dp"),
            "source": e.get("source", c.get("dlcPack") or "Base"),
            "classes": e.get("classes", []),
            "hp": hp,
            "hpInherited": inherited,
            "kiChargeSpeed": c.get("kiChargeSpeed"),
            "kiAutoRecovery": c.get("kiAutoRecovery"),
            "kiAutoRecoveryLimit": c.get("kiAutoRecoveryLimit"),
            "initialKi": c.get("initialKi"),
            "maxSkillStock": c.get("maxSkillStock"),
            "initialSkillStock": c.get("initialSkillStock"),
            "sparkingDrainPerSec": c.get("sparkingDrainPerSec"),
            "kiBlastShots": c.get("kiBlastShots"),
            "skillGaugeGains": {
                k2: v2
                for k2, v2 in (c.get("skillGaugeGains") or {}).items()
                if v2 is not None
            }
            or None,
            "unlock": e.get("unlock")
            or (f"Shop — {fmt(c['shopPrice'])} Zeni" if c.get("shopPrice") else None),
            "transformsTo": transforms_to or e.get("transformsTo", []),
            "moveset": moveset,
            "tier": e.get("tier"),
            "playable": bool(e),
            "playstyle": e.get("playstyle"),
            "strengths": e.get("strengths", []),
            "weaknesses": e.get("weaknesses", []),
            "howToFight": e.get("howToFight"),
            "summary": e.get("summary"),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": "datamined",
            "sources": [GAME_SOURCE] + e.get("sources", []),
        }

        # Battle parameters and the moveset render as structured UI from frontmatter;
        # the body carries only curated prose.
        lines = []
        if e.get("body"):
            lines += [e["body"]]
        write_page("characters", slugs[cid], front, "\n".join(lines))
        n_pages += 1
    print(f"characters: {n_pages} pages")

    # ---------- blasts ----------
    n = 0
    bslugs = set()
    name_class_pairs = {(b["name"], b["class"]) for b in blasts}
    TAG_GLOSS = {
        "Chargeable": "hold the input to charge for more damage",
        "Unguardable": "cannot be blocked",
        "In Sparking! Mode": "only usable during Sparking! Mode",
        "Played after a hit": "connects as a follow-up after the initial hit lands",
        "You also take damage": "the user takes recoil damage",
        "Absorbs opponent's HP": "drains HP from the opponent to the user",
        "Invulnerable to Super Perception": "cannot be Super-Perceptioned",
        "Uses Skill Count": "costs skill stocks instead of ki",
        "Continuous Ki Consumption": "drains ki while active",
    }
    for b in blasts:
        s = f"{slugify(b['name'])}-{b['class']}"
        if s in bslugs:
            continue
        bslugs.add(s)
        users = []
        for u in sorted(b["users"], key=lambda x: x["character"]):
            dmg, chip, hits = best_damage(u)
            users.append(
                {
                    "character": u["character"],
                    "characterSlug": slugs.get(u["charId"]),
                    "kiCost": u.get("kiCost"),
                    "triggerKiCost": u.get("triggerKiCost"),
                    "damage": dmg,
                    "chip": chip,
                    "hits": hits,
                    "category": u.get("category"),
                    "tags": [t for t in (u.get("tags") or []) if t != "Ki Required"],
                    "notes": u.get("slot"),
                }
            )
        costs = sorted({u["kiCost"] for u in b["users"] if u.get("kiCost") is not None})
        cats = Counter(u["category"] for u in users if u["category"])
        page_cat = cats.most_common(1)[0][0] if cats else None
        all_tags = sorted({t for u in users for t in u["tags"]})
        dmgs = sorted({u["damage"] for u in users if u["damage"]})
        other_class = "ultimate" if b["class"] == "super" else "super"
        sibling = (
            f"{slugify(b['name'])}-{other_class}"
            if (b["name"], other_class) in name_class_pairs
            else None
        )

        front = {
            "slug": s,
            "name": b["name"],
            "class": b["class"],
            "category": page_cat,
            "users": users,
            "summary": " · ".join(
                x
                for x in (
                    f"{page_cat}-class {b['class']}" if page_cat else b["class"],
                    f"{len(users)} user(s)",
                    f"ki cost {', '.join(fmt(c) for c in costs)}" if costs else None,
                    f"datamined damage up to {fmt(dmgs[-1])}" if dmgs else None,
                )
                if x
            ),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": "datamined",
            "sources": [GAME_SOURCE],
        }

        body_lines = ["## What it does", ""]
        desc = []
        desc.append(
            f"**{b['name']}** is a **{page_cat or 'signature'}**-class "
            f"{'Ultimate Blast' if b['class'] == 'ultimate' else 'Super (Blast 2)'}"
        )
        if costs:
            desc.append(f"costing **{' / '.join(fmt(c) for c in costs)} ki energy**")
        body_lines.append(" ".join(desc) + ".")
        for t in all_tags:
            gloss = TAG_GLOSS.get(t)
            body_lines.append(
                f"- **{t}**{f' — {gloss}' if gloss else ''} *[datamined]*"
            )
        if dmgs:
            body_lines.append(
                f"- **Datamined power: {', '.join(fmt(d) for d in dmgs)}** "
                f"(projectile/beam values vs 40,000-HP standard cast; chip values in the table) *[datamined]*"
            )
        if sibling:
            body_lines.append(
                f"- Also exists as a separate **{other_class}** for other fighters: [[{sibling}\\|{b['name']} ({other_class})]]"
            )
        body_lines += [
            "",
            "Power/chip in the table above are the move's datamined projectile values where the "
            "asset overrides defaults; '—' means the move inherits its class default (typical Beam "
            "supers land ~4,000–6,000 total on a 40,000-HP fighter). Trigger ki is the discounted "
            "cost when fired as a combo follow-up. See [[health-and-damage]] and [[ki-and-charging]].",
        ]
        write_page("blasts", s, front, "\n".join(body_lines))
        n += 1
    print(f"blasts: {n} pages")

    # ---------- skills (datamined per-char mapping + costs; enrichment adds context) ----------
    skill_enrich = load(DM / "enrichment" / "skills.json", {}) or {}
    skill_fx = load(DM / "enrichment" / "skill_effects.json", {}) or {}
    byname: dict[str, list] = defaultdict(list)
    skill_game_desc: dict[str, str] = {}
    for sk in skills_catalog:
        if sk["name"] and sk["name"] != "None":
            byname[sk["name"]].append(sk["index"])
            if sk.get("descDatamined") and sk["name"] not in skill_game_desc:
                skill_game_desc[sk["name"]] = sk["descDatamined"]

    # datamined skill -> users/costs from each character's BlastForte slots
    skill_users: dict[str, list] = defaultdict(list)
    for cid, c in sorted(chars.items()):
        if not c["name"]:
            continue
        for sk in c.get("s1Skills") or []:
            if sk.get("name"):
                skill_users[sk["name"]].append(
                    {
                        "character": c["fullName"] or c["name"],
                        "slug": slugs.get(cid),
                        "cost": sk.get("skillCost"),
                        "flags": sk.get("flags", []),
                    }
                )

    n = 0
    for name, idxs in sorted(byname.items()):
        s = slugify(name)
        e = dict(skill_fx.get(name, {}))
        e.update({k: v for k, v in (skill_enrich.get(name) or {}).items() if v})
        users = skill_users.get(name, [])
        mined_costs = sorted({u["cost"] for u in users if u["cost"] is not None})
        cost = (
            mined_costs[0]
            if len(mined_costs) == 1
            else e.get("skillCost")
            if not mined_costs
            else None
        )
        game_desc = skill_game_desc.get(name)
        front = {
            "slug": s,
            "name": name,
            "skillCost": cost if cost is not None else e.get("skillCost"),
            "effect": e.get("effect") or game_desc,
            "durationSec": e.get("durationSec"),
            "users": [u["character"] for u in users] or e.get("users", []),
            "userCount": len(users) or None,
            "tier": e.get("tier"),
            "summary": e.get(
                "summary",
                f"Skill (Blast Forte) — {len(users)} user(s)"
                + (
                    f" · {', '.join(str(int(c2)) for c2 in mined_costs)} stock(s) [datamined]"
                    if mined_costs
                    else ""
                ),
            ),
            "changeHistory": e.get("changeHistory", []),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": e.get("confidence", "datamined"),
            "sources": [GAME_SOURCE] + e.get("sources", []),
        }
        body_parts = []
        if game_desc:
            body_parts.append(
                f"## In-game description *[datamined]*\n\n> {game_desc.replace(chr(10), ' ')}"
            )
        if e.get("body"):
            body_parts.append(e["body"])
        if users:
            tbl = [
                "## Datamined users & stock costs",
                "",
                "| Character | Cost (stocks) | Flags |",
                "|---|---|---|",
            ]
            for u in users:
                link = (
                    f"[[{u['slug']}\\|{u['character']}]]"
                    if u.get("slug")
                    else u["character"]
                )
                tbl.append(
                    f"| {link} | {fmt(u['cost'])} | {', '.join(u['flags']) or '—'} |"
                )
            tbl.append("")
            tbl.append(
                "Costs marked — inherit the class default (not serialized per-asset); "
                "community-verified values appear in the frontmatter where known."
            )
            body_parts.append("\n".join(tbl))
        if not body_parts:
            body_parts.append(
                f"**{name}** — datamined skill name (catalog index {', '.join(idxs)}); "
                "no current roster user (story/legacy entry)."
            )
        write_page("skills", s, front, "\n\n".join(body_parts))
        n += 1
    print(f"skills: {n} pages")

    # ---------- transformations (datamined form-change/fusion economy) ----------
    tr_enrich = load(DM / "enrichment" / "transformations.json", {}) or {}
    n = 0
    tr_used: set[str] = set()
    for t in transforms:
        if t["kind"] == "revert" or not t.get("toName") or not t.get("fromName"):
            continue
        kind = "fusion" if t["kind"] in ("fusion", "potara") else "transform"
        nm = f"{t['fromName']} → {t['toName']}"
        s = slugify(f"{t['fromName']}-to-{t['toName']}")
        if s in tr_used:
            s = f"{s}-{t['kind']}"
            if s in tr_used:
                continue
        tr_used.add(s)
        e = tr_enrich.get(s, {})
        de = enrich.get(t["from"], {})
        de_to = enrich.get(t["to"], {})
        method = {"fusion": "Fusion (dance)", "potara": "Potara"}.get(t["kind"])
        partner_names = list(dict.fromkeys(p for p in t.get("partnerNames") or [] if p))
        front = {
            "slug": s,
            "name": nm,
            "baseCharacter": (chars.get(t["from"]) or {}).get("name") or t["fromName"],
            "from": t["fromName"],
            "to": t["toName"],
            "cost": t.get("consumeBlastStock"),
            "kind": kind,
            "hpRule": (
                f"HP recovery on change: {fmt(t.get('hpRecovery'))}"
                + (
                    f" · adds max HP: {fmt(t.get('addMaxHp'))}"
                    if t.get("addMaxHp")
                    else ""
                )
                + (
                    f" · cooldown {fmt(t.get('coolTimeSec'))}s"
                    if t.get("coolTimeSec") is not None
                    else ""
                )
                + (
                    " · no HP recovery after 2nd use"
                    if t.get("noHealAfterSecondUse")
                    else ""
                )
            ),
            "dpFrom": de.get("dp"),
            "dpTo": de_to.get("dp"),
            "summary": e.get(
                "summary",
                f"{method or 'Transformation'}: costs {fmt(t.get('consumeBlastStock'))} skill stock(s)"
                + (f" · partners: {', '.join(partner_names)}" if partner_names else ""),
            ),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": "datamined",
            "sources": [GAME_SOURCE],
        }
        from_slug, to_slug = slugs.get(t["from"]), slugs.get(t["to"])
        body = [
            f"**{nm}** ({method or 'in-battle transformation'}) — all numbers datamined from CharacterData.",
            "",
            "| Parameter | Value |",
            "|---|---|",
            f"| Skill-stock cost | **{fmt(t.get('consumeBlastStock'))}** |",
            f"| HP recovery on change | {fmt(t.get('hpRecovery'))} |",
        ]
        if t.get("addMaxHp") is not None:
            body.append(f"| Max-HP added | {fmt(t.get('addMaxHp'))} |")
        body.append(f"| Cooldown | {fmt(t.get('coolTimeSec'))}s |")
        if partner_names:
            body.append(f"| Required partner(s) | {', '.join(partner_names)} |")

        # --- exact stat deltas + moveset diff between the two forms (datamined) ---
        cf, ct = chars.get(t["from"]) or {}, chars.get(t["to"]) or {}
        hp_f, _ = resolved_hp(cf) if cf else (None, False)
        hp_t, _ = resolved_hp(ct) if ct else (None, False)
        stat_rows = []

        def delta_row(label, a, b, unit=""):
            if a is None or b is None:
                return
            if a == b:
                stat_rows.append(
                    (label, f"{fmt(a)}{unit}", f"{fmt(b)}{unit}", "no change")
                )
            else:
                sign = "+" if (b - a) > 0 else ""
                stat_rows.append(
                    (
                        label,
                        f"{fmt(a)}{unit}",
                        f"{fmt(b)}{unit}",
                        f"{sign}{fmt(b - a)}{unit}",
                    )
                )

        delta_row("Health (max)", hp_f, hp_t)
        delta_row("Ki charge speed", cf.get("kiChargeSpeed"), ct.get("kiChargeSpeed"))
        delta_row(
            "Ki auto-recovery", cf.get("kiAutoRecovery"), ct.get("kiAutoRecovery"), "/s"
        )
        delta_row(
            "Sparking gauge charge",
            cf.get("sparkingGaugeChargeSpeed"),
            ct.get("sparkingGaugeChargeSpeed"),
        )
        delta_row(
            "Pre-Sparking gauge decay",
            cf.get("preSparkingGaugeDecreaseSpeed"),
            ct.get("preSparkingGaugeDecreaseSpeed"),
            "/s",
        )
        if stat_rows:
            body += [
                "",
                "## Exact stat changes (datamined)",
                "",
                "| Stat | Before | After | Δ |",
                "|---|---|---|---|",
            ]
            body += [
                f"| {lbl} | {before} | {after} | {dlt} |"
                for lbl, before, after, dlt in stat_rows
            ]
        front["statChanges"] = (
            "; ".join(
                f"{a}: {b} → {c2} ({d})"
                for a, b, c2, d in stat_rows
                if d != "no change"
            )
            or "No flat stat changes — this change is moveset/property-based"
        )

        def kit(c):
            out = []
            for sk in c.get("s1Skills") or []:
                if sk.get("name"):
                    cost = (
                        f" ({fmt(sk['skillCost'])} stocks)"
                        if sk.get("skillCost") is not None
                        else ""
                    )
                    out.append(f"S{1 if sk['slot'] == 'S1' else 2}: {sk['name']}{cost}")
            for sp in c.get("supers") or []:
                if sp.get("name"):
                    out.append(f"{sp['slot']}: {sp['name']} ({fmt(sp['kiCost'])} ki)")
            u = c.get("ultimate") or {}
            if u.get("name"):
                out.append(f"ULT: {u['name']} ({fmt(u.get('kiCost'))} ki)")
            return out

        kit_f, kit_t = kit(cf), kit(ct)
        if kit_f or kit_t:
            body += ["", "## Moveset change", "", "| Before | After |", "|---|---|"]
            for i in range(max(len(kit_f), len(kit_t))):
                a = kit_f[i] if i < len(kit_f) else "—"
                b2 = kit_t[i] if i < len(kit_t) else "—"
                body.append(f"| {a} | {b2} |")
            body += [
                "",
                "Attack/defense in Sparking! ZERO are **per-move damage values, not flat form "
                "multipliers** — the new form's offense comes from its replaced kit above (and its "
                "own rush/smash damage tables). Flat datamined stats that do change are listed in "
                "'Exact stat changes'.",
            ]

        from_link = f"[[{from_slug}\\|{t['fromName']}]]" if from_slug else t["fromName"]
        to_link = f"[[{to_slug}\\|{t['toName']}]]" if to_slug else t["toName"]
        body += ["", f"From {from_link} to {to_link}."]
        if e.get("body"):
            body += ["", e["body"]]
        write_page("transformations", s, front, "\n".join(body))
        n += 1
    print(f"transformations: {n} pages")

    # ---------- stages ----------
    variant_re = re.compile(r"^(.*?) \((Evening|Night|Daytime - Cloudy|No Crowd)\)$")
    stage_groups: dict[str, dict] = {}
    for st in stages:
        if st["name"] in (None, "None"):
            continue
        m = variant_re.match(st["name"])
        base = m.group(1) if m else st["name"]
        g = stage_groups.setdefault(base, {"variants": []})
        g["variants"].append({"id": st["id"], "name": st["name"]})
    stage_enrich = load(DM / "enrichment" / "stages.json", {}) or {}
    n = 0
    for base, g in sorted(stage_groups.items()):
        ids = [v["id"] for v in g["variants"]]
        story_only = all(i >= "0500" for i in ids)
        e = stage_enrich.get(base, {})
        s = slugify(base)
        front = {
            "slug": s,
            "name": base,
            "source": e.get("source", "Base"),
            "destructible": e.get("destructible"),
            "variants": [v["name"] for v in g["variants"]],
            "notes": e.get("notes", "Story/menu-only backdrop" if story_only else None),
            "summary": e.get(
                "summary", f"{len(g['variants'])} variant(s) · map IDs {', '.join(ids)}"
            ),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": "datamined",
            "sources": [GAME_SOURCE] + e.get("sources", []),
        }
        body_lines = [
            f"**{base}** — stage entry from the game's map table.",
            "",
            "| Map ID | Variant |",
            "|---|---|",
        ] + [f"| `{v['id']}` | {v['name']} |" for v in g["variants"]]
        if e.get("body"):
            body_lines += ["", e["body"]]
        write_page("stages", s, front, "\n".join(body_lines))
        n += 1
    print(f"stages: {n} pages")

    # ---------- shop ----------
    cats: dict[str, list] = defaultdict(list)
    for it in shop:
        cats[it.get("contentsType") or "Other"].append(it)
    n = 0
    for cat, items in sorted(cats.items()):
        rows = []
        for it in items:
            sale = it.get("sales") or {}
            price = sale.get("Price")
            currency = (sale.get("Currency") or "").split("::")[-1] or "Zeni"
            unlock_bits = []
            ult = (sale.get("UnLockType") or "").split("::")[-1]
            if ult and ult not in ("None",):
                unlock_bits.append(ult)
            if sale.get("ConditionPlayerRank") is not None:
                unlock_bits.append(f"Player rank {sale['ConditionPlayerRank']}+")
            name = None
            if it.get("unlockCharacterNames"):
                name = " / ".join(x for x in it["unlockCharacterNames"] if x)
            rows.append(
                {
                    "name": name or it["id"].replace("ShopBase_", ""),
                    "price": price,
                    "currency": currency,
                    "type": cat,
                    "unlock": "; ".join(unlock_bits) or None,
                }
            )
        rows.sort(key=lambda r: (r["price"] is None, r["price"] or 0, r["name"]))
        s = slugify(cat)
        priced = [r["price"] for r in rows if r["price"] is not None]
        front = {
            "slug": s,
            "name": f"Shop — {cat}",
            "items": rows,
            "summary": (
                f"{len(rows)} item(s)"
                + (
                    f" · prices {fmt(min(priced))}–{fmt(max(priced))} Zeni"
                    if priced
                    else ""
                )
            ),
            "asOfVersion": AS_OF,
            "asOfDate": AS_OF_DATE,
            "lastVerified": TODAY,
            "confidence": "datamined",
            "sources": [GAME_SOURCE],
        }
        body = (
            f"Full datamined price table for the **{cat}** shop category "
            f"({len(rows)} entries). Prices in Zeni unless noted."
        )
        write_page("shop", s, front, body)
        n += 1
    print(f"shop: {n} category pages ({len(shop)} items)")

    # ---------- global search index (all collections, incl. curated dirs) ----------
    href_map = {
        "characters": "/characters/",
        "blasts": "/blasts/",
        "skills": "/skills/",
        "transformations": "/transformations/",
        "mechanics": "/mechanics/",
        "game-modes": "/game-modes/",
        "episode-battles": "/episode-battles/",
        "patches": "/patches/",
        "dlc": "/dlc/",
        "guides": "/guides/",
        "stages": "/stages/",
        "shop": "/shop/",
        "glossary": "/glossary#",
    }
    group_label = {
        "characters": "Fighter",
        "blasts": "Blast",
        "skills": "Skill",
        "transformations": "Transformation",
        "mechanics": "Mechanic",
        "game-modes": "Mode",
        "episode-battles": "Episode Battle",
        "patches": "Patch",
        "dlc": "DLC",
        "guides": "Guide",
        "stages": "Stage",
        "shop": "Shop",
        "glossary": "Glossary",
    }
    fm_field = re.compile(
        r'^(name|title|version|term|dp|hp|category|releaseDate|tier):\s*"?([^"\n]+)"?\s*$',
        re.M,
    )
    index = []
    for coll, prefix in href_map.items():
        d = CONTENT / coll
        if not d.exists():
            continue
        for f in sorted(d.glob("*.md")):
            raw = f.read_text(encoding="utf-8")
            parts = raw.split("---")
            if len(parts) < 3:
                continue
            fields = dict(fm_field.findall(parts[1]))
            title = (
                fields.get("name")
                or fields.get("title")
                or fields.get("version")
                or fields.get("term")
                or f.stem
            )
            hints = []
            if coll == "characters":
                if fields.get("dp"):
                    hints.append(f"DP {fields['dp']}")
                if fields.get("hp"):
                    hints.append(f"HP {int(float(fields['hp'])):,}")
                if fields.get("tier"):
                    hints.append(f"{fields['tier']}-tier")
            elif fields.get("category"):
                hints.append(fields["category"])
            elif fields.get("releaseDate"):
                hints.append(fields["releaseDate"])
            index.append(
                {
                    "t": title,
                    "h": prefix + f.stem,
                    "g": group_label[coll],
                    "x": " · ".join(hints),
                }
            )
    pub = ROOT / "public"
    pub.mkdir(exist_ok=True)
    with open(pub / "search-index.json", "w", encoding="utf-8") as f:
        json.dump(index, f, ensure_ascii=False)
    print(f"search index: {len(index)} entries -> public/search-index.json")


if __name__ == "__main__":
    main()
