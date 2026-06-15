---
slug: "health-and-damage"
name: "Health & Damage"
category: "system"
input: "Passive — HP pool, per-hit damage, and combo scaling that govern every exchange"
values:
  - label: "Standard HP (147 fighters)"
    value: "40,000 HP"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "High-HP tier (16 fighters)"
    value: "45,000 HP (e.g. Beerus, Cooler, Great Ape Vegeta)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Mid-low tier (14 fighters)"
    value: "35,000 HP (e.g. Goten, Krillin, Yajirobe, Spopovich)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Low-HP tier (9 fighters)"
    value: "30,000 HP (e.g. Master Roshi, Mr. Satan, Videl, Gohan Kid)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "HP per health bar"
    value: "~10,000 HP / bar (≈4 bars on a 40k body)"
    patch: "current"
    tag: "datamined"
  - label: "Rush 1st hit"
    value: "~390 (standard)"
    patch: "current (community lab)"
    tag: "community"
  - label: "Rush 5-hit string"
    value: "~2,460 (≈2,289 into armor)"
    patch: "current (community lab)"
    tag: "community"
  - label: "Super blast damage"
    value: "~9,080 base / ~13,660 Boosted (Super Kamehameha, Cell)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Ultimate blast damage / cost"
    value: "~15,000 base, up to ~19,638 Boosted (Special Beam Cannon); 50,000 energy cost (universal)"
    patch: "current (datamine)"
    tag: "datamined"
counters:
  - "Higher HP tiers survive more"
  - "High-ATK bodies kill in shorter combos"
counteredBy:
  - "Combo scaling (long combos lose damage)"
  - "Defense / Energy Defense modifiers"
  - "Single-battle HP equalization (Jun 2025)"
summary: "The datamine stores HP directly in four tiers — 30k (9 fighters) / 35k (14) / 40k (147 standard) / 45k (16) — at ~10,000 HP per bar. Per-hit melee (~390 first hit, ~2,460 rush-5) are community labs; named-move blast damage (super ~9k base, ultimate ~15k+) is datamined. Combo scaling is real and aggressive: a raw Ultimate often out-damages a long combo→Ultimate. Single battle has equalized HP and removed DP damage-scaling since Jun 23, 2025."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Sparking! Mode rush attacks: consecutive-hit damage scaling increased (long combos punished harder)."
  - version: "Ver.2013.012.003.008.007 (Jun 23, 2025)"
    date: "2025-06-23"
    change: "Single Battle: removed DP-based damage scaling in all modes; all characters set to the same health in single battle (online & offline)."
  - version: "Patch (Jan 26, 2026)"
    date: "2026-01-26"
    change: "Cell Max: Max Bomb made unblockable. (Note: the circulating 'all characters standardized to 6,000 HP' claim is FALSE — datamined HP stays in the tens of thousands.)"
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Blasts/Ultimates do less when hit during a combo; consecutive-Blast damage reduced; rapid-fire ki-blast damage increased; Ultimate-Blast combo damage-reduction eased (partial walk-back)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "data-mined/system_constants.json (hpDistribution: 30k×9 / 35k×14 / 40k×147 / 45k×16)"
  - "research/04-mechanics-frame-data.md (§1 Health & Damage; §1.5 combo scaling; Gaps #7 '6,000 HP' is false)"
  - "research/03-patches-balance.md (Dec 2024; Jun 23 2025; Jan 26 2026; May 26 2026)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Jun 23, 2025; Jan 26, 2026; May 26, 2026)"
---
Health and damage are stored **directly** in the game files (no abstraction): each character has a raw HP pool, each move a raw damage value, and combo scaling prorates everything down as a string gets longer.

## HP tiers (datamined)

The datamine (`system_constants.json`) resolves the roster into **four clean HP tiers**:

| HP | Fighters | Examples |
|---|---|---|
| **30,000** | **9** | Master Roshi, Mr. Satan, Videl, Gohan (Kid), Chiaotzu, Guldo, Babidi, Panzy |
| **35,000** | **14** | Goten, Krillin, Yajirobe, Yamcha, Spopovich, Trunks (Kid), Goku (Teen), Saibaman |
| **40,000** | **147** | the standard body — Bardock, Broly, Android 16/17/18/19, Baby Vegeta… |
| **45,000** | **16** | Beerus, Cooler, Great Ape Vegeta, Fused Zamasu, Gotenks, Kale, Orange Piccolo, Omega Shenron |

- **~10,000 HP per bar.** A 40,000-HP body shows ~**4** segments on the HUD. Cross-checked by a lab where an SSJ4 Gogeta combo dealing **19,832 damage** was described as "two full bars" (≈9,900/bar).

> The widely-circulated claim that the **Jan 2026 patch "standardized all characters to 6,000 HP" is FALSE.** Datamined HP remains in the **tens of thousands** and character-specific. What Jun 23, 2025 actually did: **removed DP-based damage scaling** in single battles and set all characters to the **same** health *in single battle* — the per-tier datamine values above are the underlying pools.

## Damage

| Quantity | Value |
|---|---|
| Rush 1st hit | ~**390** |
| Full basic string (melee aggregate) | ~**2,275** |
| Rush 5-hit | ~**2,460** (≈**2,289** into [[super-armor|armor]], ~7% less) |
| [[throws|Throw]] damage | ~**1,250–1,312** |
| Super blast (Super Kamehameha, Cell) | **9,080** base / **13,660** Boosted (≈×1.50) |
| Ultimate (Special Beam Cannon, Piccolo) | **15,000** base / **19,638** Boosted |
| Ultimate energy cost | **50,000** (universal; supers 20,000–40,000) |

The **melee aggregates** above (rush 1st hit, basic string, rush-5, throw) are **community labs** (`research/04`), not datamined; the **named-move blast** values (Super Kamehameha, Special Beam Cannon) and the 50,000 energy cost are **datamined**. Higher-tier bodies scale up (Hit: 1st-hit 508, rush-5 3,283). Blasts in [[sparking-mode|Sparking! Mode]] use the **Boosted** column (~×1.2–1.5).

## Combo scaling (community-tested)

- **Diminishing returns is real and aggressive.** Each added hit returns less, so a **raw Ultimate frequently out-damages a long combo→Ultimate**: Kid Gohan raw ult **17,388** vs a 60+ hit combo→ult dropping the whole sequence to **~13–15k**; SSJ4 Gogeta raw **19,950** vs 70-hit→ult **19,250**. Optimal damage = **short combos on high-ATK bodies**.
- **Sparking! Mode rush scaling is harsher** (Dec 2024). The **May 26, 2026** patch reduced blast/consecutive-blast damage when hit during a combo but **eased** Ultimate-Blast combo scaling (a partial walk-back). The exact per-hit proration coefficients are **not published** — only the behavior is known.
- See [[dp-system|DP system]] for the removed DP damage-scaling and the DP-only "Big Impact" item.
