"""Build data-mined/enrichment/characters.json by matching research/02 DP-table names
to datamined charIds.

The DP table in research/02-roster-dp-dlc.md (sections 3a base + 3b SP1 DLC) uses
Game8/Fandom-style display names with SPACE-separated form suffixes
("Goku (Z - End) Super Saiyan 2"), while data-mined/characters.json stores forms with
COMMA-separated suffixes in `fullName` ("Goku (Z - End), Super Saiyan 2") keyed by
charId ("0000_22").

Strategy:
  1. Parse the two markdown roster tables (3a, 3b) into rows with
     {name, dp, source, era, notes}.
  2. Build a normalized lookup of every named datamined character keyed on a
     punctuation/case-stripped form of both `name` and `fullName` (with the
     comma->space and "Nth Form" quirks folded in).
  3. Match each research row -> charId by normalized name. Fall back to an explicit
     OVERRIDES dict for the handful that cannot be fuzzy-matched.
  4. Layer derived fields (classes, unlock cost, tier, one-line summary, sources)
     and emit the enrichment overlay JSON consumed by gen_content.py.

Only matched slots get a `dp`. Unmatched research rows are reported, never invented.
"""

from __future__ import annotations

import json
import re
import unicodedata
from pathlib import Path

ROOT = Path(r"C:\vaults\sparking_zero")
DM = ROOT / "data-mined"
RESEARCH = ROOT / "research"
OUT = DM / "enrichment" / "characters.json"

ROSTER_MD = RESEARCH / "02-roster-dp-dlc.md"

RESEARCH_SRC = "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
TIER_SRC = (
    "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
)
UNLOCK_SRC = "research/06-pve-dlc-unlocks.md (shop Zeni costs)"


# ---------------------------------------------------------------------------
# Normalization
# ---------------------------------------------------------------------------
def norm(s: str) -> str:
    """Aggressively normalize a character/form name for matching.

    - unicode NFKD + strip accents (Rosé -> Rose)
    - lowercase
    - en/em dash -> hyphen
    - drop a comma that separates a form suffix ("Goku (Z - End), Super Saiyan")
    - collapse "(... Form)" parenthetical that only appears in datamine
      ("Frieza (Z), 1st Form" -> handled via suffix map below)
    - strip all non-alphanumerics, collapse spacing
    """
    s = unicodedata.normalize("NFKD", s)
    s = "".join(c for c in s if not unicodedata.combining(c))
    s = s.lower()
    s = s.replace("–", "-").replace("—", "-").replace("−", "-")
    s = s.replace(",", " ")
    # canonicalize ordinal form words so "2nd"/"second" etc. don't matter
    s = re.sub(r"[^a-z0-9]+", " ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def norm_key(s: str) -> str:
    """Final match key: normalized + spaces removed."""
    return norm(s).replace(" ", "")


# Datamine fullName suffix quirks that don't appear (or appear differently) in the
# research display names. For a single datamine string, return every research-style
# spelling that should match it.
def name_variants(base: str) -> set[str]:
    out: set[str] = {norm_key(base)}
    # "X, 1st Form" / "X, Perfect Form" -> research drops the comma:
    #   "Cell, 2nd Form" -> "Cell 2nd Form"; "Cell, 1st Form" -> "Cell"
    if "," in base:
        head, _, tail = base.partition(",")
        tail = tail.strip()
        out.add(norm_key(f"{head} {tail}"))
        # research drops the "1st Form" entirely for base forms
        if tail.lower() in ("1st form",):
            out.add(norm_key(head))
    # "(Gotenks Absorbed)" parenthetical -> research writes it without parens
    if "(" in base and ")" in base:
        out.add(norm_key(re.sub(r"[()]", " ", base)))
    return out


# ---------------------------------------------------------------------------
# Parse the research markdown roster tables (3a base + 3b SP1 DLC)
# ---------------------------------------------------------------------------
def parse_roster() -> list[dict]:
    text = ROSTER_MD.read_text(encoding="utf-8")
    rows: list[dict] = []

    # --- 3a base table: | Name | DP | Source | Era | Transforms / Class / Notes |
    sec_a = text.split("### 3a. BASE ROSTER", 1)[1].split("### 3b.", 1)[0]
    for line in sec_a.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 5:
            continue
        name, dp, source, era, notes = cells[0], cells[1], cells[2], cells[3], cells[4]
        if name in ("Name", "") or set(name) <= {"-", ":"}:
            continue
        if not re.fullmatch(r"\d+", dp):
            continue
        rows.append(
            {
                "name": name,
                "dp": int(dp),
                "source": source,
                "era": era,
                "notes": notes,
                "table": "base",
            }
        )

    # --- 3b SP1 DLC table: | # | Name | DP | Source | Era | Transforms / Notes |
    sec_b = text.split("### 3b. SEASON PASS 1 DLC", 1)[1].split("### 3c.", 1)[0]
    for line in sec_b.splitlines():
        line = line.strip()
        if not line.startswith("|"):
            continue
        cells = [c.strip() for c in line.strip("|").split("|")]
        if len(cells) < 6:
            continue
        slot, name, dp, source, era, notes = cells[:6]
        if name in ("Name", "") or set(slot) <= {"-", ":"} or slot == "#":
            continue
        if not re.fullmatch(r"\d+", dp):
            continue
        rows.append(
            {
                "name": name,
                "dp": int(dp),
                "source": source,
                "era": era,
                "notes": notes,
                "table": "dlc",
                "slot": int(slot),
            }
        )
    return rows


# ---------------------------------------------------------------------------
# Explicit overrides: research display name -> charId.
# Only for rows that normalized matching cannot resolve (genuine spelling gaps,
# datamine forms that share a `name`, or rows the table writes differently).
# ---------------------------------------------------------------------------
OVERRIDES: dict[str, str] = {
    # Frieza (Z) base form is "Frieza (Z), 1st Form" in datamine.
    "Frieza (Z)": "0150_00",
    "Frieza (Z) 2nd Form": "0151_00",
    "Frieza (Z) 3rd Form": "0152_00",
    "Frieza (Z) 4th Form": "0153_00",
    "Frieza (Z) Full Power": "0154_00",
    # Cell base/forms: datamine uses ", Nth Form".
    "Cell": "0160_00",
    "Cell 2nd Form": "0161_00",
    "Cell Perfect Form": "0162_00",
    # Piccolo (Fused With Kami) — datamine lowercases "with".
    "Piccolo (Fused With Kami)": "0040_10",
    # Super Buu absorbed forms — datamine parenthesizes.
    "Super Buu Gohan Absorbed": "0172_11",
    "Super Buu Gotenks Absorbed": "0172_10",
    # Broly (Super) full-power form — datamine adds parens.
    "Broly (Super) Super Saiyan Full Power": "0555_00",
    # Kale berserk — datamine parenthesizes "(Berserk)".
    "Kale Super Saiyan (Berserk)": "0911_00",
    # Super Gogeta (Z) — datamine fullName carries trailing spaces.
    "Super Gogeta (Z)": "0110_04",
    # Trunks (Melee) line: research "Super Trunks" is its own datamine slot.
    "Super Trunks": "0081_20",
    # Super Vegeta / Great Ape Vegeta are standalone datamine slots (share Vegeta name).
    "Super Vegeta": "0021_20",
    "Great Ape Vegeta": "0023_00",
    # GT fusion / SS4 slots store the form in fullName, not name.
    "Gogeta (GT) Super Saiyan 4": "0110_02",
    "Goku (GT) Super Saiyan 4": "0000_33",
    "Vegeta (GT) Super Saiyan 4": "0020_50",
    # Omega/Syn Shenron.
    "Omega Shenron (GT)": "0700_01",
    # --- DLC (3b) rows ---
    # Ultimate Gohan (Super Hero) — distinct datamine entry name.
    "Ultimate Gohan (Super Hero)": "3000_02",
    # Goku (Mini) SS4 / Goku (DAIMA) SS4 / Vegeta (DAIMA) SS3 store form in fullName.
    "Goku (Mini) Super Saiyan 4": "3050_14",
    "Goku (DAIMA) Super Saiyan 4": "3120_04",
    "Vegeta (DAIMA) Super Saiyan 3": "3100_03",
    # Orange Piccolo Giant Form — datamine ", Giant Form".
    "Orange Piccolo Giant Form": "3012_00",
    # Piccolo (Super Hero) Power Awakening — datamine ", Power Awakening".
    "Piccolo (Super Hero) Power Awakening": "3010_01",
}


# ---------------------------------------------------------------------------
# Derived metadata
# ---------------------------------------------------------------------------
# Class tags inferred from research/02 §6 + roster notes (Giant / Android / Fusion).
GIANT = {
    "0023_00",  # Great Ape Vegeta
    "0681_00",  # Great Ape Baby (GT)
    "0670_00",  # Hirudegarn
    "0591_00",  # Lord Slug Giant Form
    "3012_00",  # Orange Piccolo Giant Form
    "3150_00",  # Giant Gomah
    "3040_00",  # Cell Max
    "0621_00",  # Fusion Android 13
    "1500_00",  # Anilaza
}
ANDROID = {
    "0440_00",  # Android 16
    "0450_00",  # Android 17 (Z)
    "0450_10",  # Android 17 (Super)
    "0460_00",  # Android 18
    "0470_00",  # Android 19
    "0480_00",  # Dr. Gero
    "0153_10",  # Mecha Frieza
    "0600_10",  # Metal Cooler
    "0620_00",  # Android 13
    "0621_00",  # Fusion Android 13
    "3020_00",  # Gamma 1
    "3030_00",  # Gamma 2
}
FUSION = {
    "0100_00",  # Vegito
    "0100_01",  # Super Vegito
    "0100_02",  # Vegito SSGSS
    "0110_00",  # Gogeta (Super)
    "0110_01",  # Gogeta (Super) SS
    "0110_02",  # Gogeta (GT) SS4
    "0110_03",  # Gogeta (Super) SSGSS
    "0110_04",  # Super Gogeta (Z)
    "0120_00",  # Gotenks
    "0120_01",  # Gotenks SS
    "0120_02",  # Gotenks SS3
    "0920_00",  # Kefla
    "0920_01",  # Kefla SS
    "0920_02",  # Kefla SS2
    "0810_01",  # Fused Zamasu
    "0811_00",  # Fused Zamasu Half-Corrupted
    "0621_00",  # Fusion Android 13
    "1500_00",  # Anilaza
    "0240_01",  # Majuub (GT)
}

# Shop unlock Zeni costs (research/06 §3.1). Keyed by datamine charId; a purchase
# unlocks all forms, so the cost attaches to the base/buyable slot.
UNLOCK_ZENI: dict[str, int] = {
    "0130_00": 30000,  # Videl
    "0002_50": 45000,  # Goku (Teen)
    "0910_00": 60000,  # Kale
    "0002_30": 75000,  # Goku (GT) (base) -> all GT Goku forms
    "0800_00": 75000,  # Goku Black
    "0881_00": 90000,  # Frost
    "0950_00": 90000,  # Dyspo
    "0020_40": 105000,  # Majin Vegeta
    "0000_50": 120000,  # Goku (Super) Ultra Instinct -Sign-
    "0110_02": 120000,  # Gogeta (GT) SS4
}

# Tier placements — ONLY where research/05 clearly slots the fighter (Singles list,
# §2a / §8). S/A/B/C/D. Keyed by datamine charId for the exact form named.
TIER: dict[str, str] = {
    # S (Singles)
    "0100_02": "S",  # Vegito SSGSS
    "0110_02": "S",  # Gogeta (GT) SS4
    "0552_00": "S",  # Broly (Z) Legendary SS
    "0555_00": "S",  # Broly (Super) SS Full Power
    "0931_00": "S",  # Jiren Full Power
    "0790_00": "S",  # Whis
    "0000_51": "S",  # UI Goku
    "0110_03": "S",  # Gogeta (Super) SSGSS
    "0911_00": "S",  # Kale (Berserk)
    "3000_03": "S",  # Gohan Beast
    "0941_00": "S",  # Toppo God of Destruction
    "0100_01": "S",  # Super Vegito
    "0621_00": "S",  # Fusion Android 13
    # A
    "0110_01": "A",  # Gogeta (Super) SS
    "0811_00": "A",  # Fused Zamasu Half-Corrupted
    "0780_00": "A",  # Beerus
    "0100_00": "A",  # Vegito (base)
    "0172_10": "A",  # Super Buu (Gotenks Absorbed)
    "0000_33": "A",  # Goku (GT) SS4
    "0600_10": "A",  # Metal Cooler
    "0000_50": "A",  # UI -Sign-
    "0920_02": "A",  # Kefla SS2
    "0800_01": "A",  # Goku Black Super Saiyan Rosé
    "0700_01": "A",  # Omega Shenron
    "0601_00": "A",  # Cooler Final Form
    "3011_00": "A",  # Orange Piccolo
    "0032_02": "A",  # Gohan (Adult) SS2
    "0000_23": "A",  # Goku (Z-End) SS3
    "0110_00": "A",  # Gogeta (Super) SS (base fusion) — listed "Gogeta Super SS"
    # B
    "0080_31": "B",  # Future Trunks SS
    "3030_00": "B",  # Gamma 2
    "3040_00": "B",  # Cell Max
    "0031_02": "B",  # Gohan (Teen) SS2
    "0020_40": "B",  # Majin Vegeta
    "0162_01": "B",  # Perfect Cell
    "0032_20": "B",  # Ultimate Gohan
    "0021_20": "B",  # Super Vegeta
    "0681_00": "B",  # Great Ape Baby
    "0020_63": "B",  # Vegeta (Super) SSGSS
    "0440_00": "B",  # Android 16
    "0154_00": "B",  # Frieza (Z) Full Power
    "0450_10": "B",  # Android 17 (Super)
    # C
    "0390_00": "C",  # Recoome
    "0591_00": "C",  # Lord Slug (Giant)
    "0650_00": "C",  # Janemba
    "0570_00": "C",  # Dr. Wheelo
    "0090_01": "C",  # Goten SS
    "0153_00": "C",  # Frieza (Z) 4th Form
    "0023_00": "C",  # Great Ape Vegeta
    "0450_00": "C",  # Android 17 (Z)
    "0070_00": "C",  # Tien
    "0032_00": "C",  # Gohan (Adult) base
    "0600_00": "C",  # Cooler base
    "3060_00": "C",  # Vegeta (Mini) base
    # D
    "3110_00": "D",  # Majin Kuu
    "1321_00": "D",  # Ribrianne
    "0430_00": "D",  # King Cold
    "0210_00": "D",  # Yajirobe (Singles)
    "0141_00": "D",  # Master Roshi Max Power (Singles — standardized HP removes tank edge)
    "3050_00": "D",  # Goku (Mini)
    "0310_00": "D",  # Bardock
    "0130_00": "D",  # Videl
    "0032_10": "D",  # Great Saiyaman
    "0330_00": "D",  # Saibaman
    "3130_00": "D",  # Panzy
    "0190_00": "D",  # Chiaotzu
    "0420_00": "D",  # Guldo
    "0180_00": "D",  # Mr. Satan
}

# One-line, data-dense summaries for the most meta-relevant fighters (research §8/§2).
# Only attach where research gives concrete role + numbers. charId -> summary.
SUMMARY: dict[str, str] = {
    "0100_02": "DP10 Potara fusion; #1 Singles (sparkingzerometa 152.8k); elite fusion speed + Final Kamehameha ultimate burst.",
    "0110_02": "DP10 Fusion-Dance carry; #2 Singles (151.5k); normals faster than many chars' Sparking-mode speed — premier rushdown.",
    "0552_00": "DP9 berserker; top-3 both modes (Singles 150.6k / DP 29.1k); tanky, huge damage, scales with permanent attack-buff transform.",
    "0555_00": "DP9 armor bruiser; #4 Singles (149.6k) and top DP value (29.0k); Broly (Super) ceiling form.",
    "0931_00": "DP9 Singles S-tier (140.3k); armor + counters + raw power, but low DP efficiency (12.0k) — an expensive anchor.",
    "0790_00": "DP10 deity; #6 Singles (135.4k); best-in-class mobility + auto-dodge (Rush-Chain-counterable post-May-2026).",
    "0000_51": "DP9 auto-dodge S-tier (134.4k); nerfed May 2026 (Smash Ki Blast cooldown up, Rush Chain beats dodge) but still top.",
    "0110_03": "DP10 Singles S-tier (132.7k); nerfed May 2026 (Smash Ki Blast damage + homing cut) — needs deliberate spacing.",
    "0911_00": "DP7 berserker; #9 Singles (129.1k), strong DP value (25.5k); Cry of Rage activation time raised May 2026.",
    "3000_03": "DP9 DLC carry; #10 Singles (128.7k) AND #1 DP (33.9k) — best all-around pick across both modes.",
    "0941_00": "DP8 God of Destruction; #11 Singles (128.0k); armor + raw power anchor.",
    "0100_01": "DP8 Potara fusion; #12 Singles (126.9k); fusion burst just below SSGSS Vegito.",
    "0621_00": "DP7 Giant/Android fusion; #13 Singles (125.2k) and strong DP value (24.7k); surprise high-tier.",
    "0780_00": "DP10 God of Destruction; A-tier Singles (120.9k) but perennial competitive pick for cheap-DP mobility/zoning.",
    "0800_01": "DP8 pressure/okizeme specialist (Singles 113.0k); strong ladder + tournament pick, solid DP body (20.7k).",
    "0600_10": "DP7 Android; A-tier Singles (116.4k); revival + regeneration kit.",
    "0210_00": "DP2 Senzu healer; once meta-defining stall, gutted to niche DP tank (Senzu 6 stock / 0 start; Ki recovery nerfed May 2026).",
    "0140_00": "DP2 low-HP (30,000) flightless skirmisher; transforms to Max Power.",
    "0141_00": "DP2 Max Power form; DP-efficiency S-tier (sparkingzerometa 31.2k points-per-DP) but Ki recovery nerfed May 2026; weak in standardized-HP Singles.",
    "0180_00": "DP1 — lowest DP in the game; weakest Singles score (8.7k); joke/utility pick only.",
    "3040_00": "DP9 Giant boss; Max Bomb made unblockable Jan 2026; B-tier Singles after broad May 2026 giant nerfs.",
    "0390_00": "DP3 heavy bruiser; DP-value S-tier (30.3k) for points-per-DP, but HP reduced in May 2026 patch.",
    "0760_00": "DP2 tank; DP-efficiency S-tier (28.2k) overperformer, but HP reduced May 2026.",
}


def main() -> None:
    chars: dict = json.load(open(DM / "characters.json", encoding="utf-8"))

    # Two-tier index:
    #   full_index: key derived from `fullName` (form-specific, e.g.
    #     "Goku (Z - End), Super Saiyan 2") -> charId. These are unique per form,
    #     so a research row like "Goku (Z - End) Super Saiyan 2" resolves cleanly.
    #   name_index: key derived from bare `name` (shared across a form family,
    #     e.g. "Goku (Z - End)") -> list of charIds. Used as a fallback for base
    #     rows; ambiguity is broken by preferring the form whose own fullName key
    #     equals its name key (i.e. the genuine base form).
    full_index: dict[str, list[str]] = {}
    name_index: dict[str, list[str]] = {}
    base_form: dict[str, str] = {}  # name-key -> charId of the family's base form
    for cid, c in chars.items():
        if not c.get("name"):
            continue
        if cid.startswith("8") or cid.startswith("7"):  # NPC / narrator range
            continue
        full = c.get("fullName") or c["name"]
        for k in name_variants(full):
            full_index.setdefault(k, [])
            if cid not in full_index[k]:
                full_index[k].append(cid)
        for k in name_variants(c["name"]):
            name_index.setdefault(k, [])
            if cid not in name_index[k]:
                name_index[k].append(cid)
        # the base form is the one whose fullName == name (no ", Super Saiyan" suffix)
        if norm_key(full) == norm_key(c["name"]):
            base_form.setdefault(norm_key(c["name"]), cid)

    override_keys = {norm_key(n): cid for n, cid in OVERRIDES.items()}

    rows = parse_roster()
    enrich: dict[str, dict] = {}
    matched: list[tuple[str, str]] = []
    unmatched: list[str] = []
    used_ids: set[str] = set()

    for row in rows:
        name = row["name"]
        k = norm_key(name)
        cid = None
        if k in override_keys:
            cid = override_keys[k]
        else:
            # 1) exact fullName match (unique per form) wins
            fcands = [c for c in full_index.get(k, []) if c not in used_ids]
            if len(fcands) == 1:
                cid = fcands[0]
            elif full_index.get(k) and len(full_index[k]) == 1:
                cid = full_index[k][0]
            # 2) genuine base form for this name family
            elif k in base_form and base_form[k] not in used_ids:
                cid = base_form[k]
            else:
                # 3) name-only fallback, preferring an unused candidate
                cands = name_index.get(k, [])
                fresh = [c for c in cands if c not in used_ids]
                if len(fresh) == 1:
                    cid = fresh[0]
                elif len(cands) == 1:
                    cid = cands[0]

        if cid is None:
            unmatched.append(f"{name} (DP{row['dp']}, {row['source']})")
            continue

        used_ids.add(cid)
        matched.append((name, cid))

        # classes
        classes: list[str] = []
        if cid in GIANT:
            classes.append("Giant")
        if cid in ANDROID:
            classes.append("Android")
        if cid in FUSION:
            classes.append("Fusion")

        # sources used for this row's enrichment-derived fields
        sources = [RESEARCH_SRC]
        if cid in TIER:
            sources.append(TIER_SRC)
        if cid in UNLOCK_ZENI:
            sources.append(UNLOCK_SRC)

        entry: dict = {"dp": row["dp"], "era": row["era"]}
        if classes:
            entry["classes"] = classes
        if cid in UNLOCK_ZENI:
            entry["unlock"] = f"{UNLOCK_ZENI[cid]:,} Zeni (shop)"
        if cid in TIER:
            entry["tier"] = TIER[cid]
        if cid in SUMMARY:
            entry["summary"] = SUMMARY[cid]
        entry["sources"] = sources
        enrich[cid] = entry

    # deterministic key order
    enrich = {k: enrich[k] for k in sorted(enrich)}
    OUT.parent.mkdir(parents=True, exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump(enrich, f, ensure_ascii=False, indent=2)
        f.write("\n")

    total = len(rows)
    print(
        f"roster rows parsed: {total}  (base {sum(1 for r in rows if r['table'] == 'base')}"
        f" + dlc {sum(1 for r in rows if r['table'] == 'dlc')})"
    )
    print(f"matched: {len(matched)} / {total}")
    print(f"unmatched: {len(unmatched)}")
    for u in unmatched:
        print(f"  UNMATCHED: {u}")
    print(f"wrote {OUT} ({len(enrich)} charIds enriched)")


if __name__ == "__main__":
    main()
