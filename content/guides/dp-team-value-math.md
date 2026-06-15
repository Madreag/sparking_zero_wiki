---
slug: "dp-team-value-math"
title: "DP Team Value Math — HP-per-DP and the 15-DP Budget"
category: "pvp"
summary: "The analysis piece: an HP-per-DP table built from datamined HP and research DP costs (45,000-HP heavies, Roshi's 30k at DP2, the standard 40k), the best cheap-value 15-DP archetypes (Gohan Beast, Master Roshi Max Power, Yajirobe, Recoome, the Brolys), and how the post-May-2026 DP-gap mechanics (DP7+ auto-reflect gate, widened gap effect) reshape team building."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "data-mined/characters.json (datamined HP per fighter — hp field)"
  - "research/02-roster-dp-dlc.md (DP costs per fighter, 1-10 scale)"
  - "research/05-meta-pvp-tiers.md §5 (15-DP comps, cheap-value picks, DP-gap mechanics)"
  - "research/04-mechanics-frame-data.md §1.1 (datamined HP baseline, defense factors)"
  - "Bandai Namco — May 26 2026 Free Update Notice (auto-reflect DP7+, DP-gap widening)"
---

DP Battle is a **value-optimization** problem, not a strength contest. You have a **15 Destruction Point budget** for a team of up to 3-5 characters, and since the **May 26, 2026** patch the system **rewards points-per-DP** while **widening the gap** between high- and low-DP characters. This guide does the actual math: how much **HP you buy per DP** for the notable picks, which cheap bodies overperform, and how the new DP-gap rules change the build.

## Reading the numbers

- **HP values are `[datamined]`** from `data-mined/characters.json` (the `hp` field). Confidence: high.
- **DP values are from `research/02`** (the 1-10 in-game point cost). Confidence: high for base roster, medium for some DLC forms.
- **HP/DP** below is a **value index** (datamined HP divided by DP cost), *not* an in-game stat. It captures the core DP-Battle truth: a **45,000-HP heavy at DP2** is buying more than twice the bulk-per-point of a **40,000-HP god at DP10**.
- **Caveat — some top fusions have null HP in the datamine.** Vegito SSGSS, Gogeta GT SS4, Gohan Beast, Jiren Full Power, Toppo GoD, and Cell Max read `hp: null` in the files (their HP isn't exposed). For those, the table uses the **standardized 40,000** baseline as an estimate and flags it. Confidence on those rows: estimated.

## HP-per-DP table (notable picks)

| Character | HP (datamined) | DP | HP / DP | Role read |
|---|---:|---:|---:|---|
| **Master Roshi** (base) | **30,000** | **2** | **15,000** | Low-HP skirmisher, but cheapest body in tier — pure DP filler. |
| Mr. Satan | 30,000 | 1 | 30,000 | **Highest raw HP/DP in the game** by index (lowest DP). Joke kit, but a 1-DP body. |
| Saibaman | 35,000 | 1 | 35,000 | 1-DP throwaway; self-destruct chip value. |
| **Yajirobe** | **35,000** | **2** | **17,500** | The classic cheap tank; Senzu heal (now 6-stock / 0-start). Ki-recovery nerfed May 26. |
| Spopovich | 35,000 | 2 | 17,500 | Tanky DP2 bruiser (Defense 1100). HP reduced May 26 — drifting down. |
| Nappa | 40,000 | 3 | 13,333 | Standard-HP DP3 heavy. HP reduced May 26. |
| **Recoome** | **40,000** | **3** | **13,333** | DP3 super-armor bruiser; strong value carry. HP reduced May 26. |
| Master Roshi (Max Power) | 40,000 | 2 | **20,000** | Max Power form keeps DP2 but jumps to 40k HP — a top value pick. |
| **Broly (Z) Legendary SS** | **45,000** | **9** | 5,000 | **45k-HP heavy** — best-in-class bulk, but premium DP. Top of both lists. |
| **Broly (Super) SS Full Power** | **45,000** | **9** | 5,000 | Same 45k heavy archetype; armor + damage. |
| Kale (Berserk) | 45,000 | 7 | 6,429 | 45k berserker at DP7 — better value than the DP9 Brolys, still DP7+ for auto-reflect. |
| Beerus | 45,000 | 10 | 4,500 | 45k-HP god, but DP10 — inefficient on points-per-DP despite the bulk. |
| Whis | 45,000 | 10 | 4,500 | Same: elite kit + 45k HP, but DP10 craters the value index. |
| Orange Piccolo | 45,000 | 8 | 5,625 | 45k bulk at DP8; giant form available (nerfed May 26). |
| Fusion Android 13 | 45,000 | 7 | 6,429 | 45k giant-class at DP7 — sneaky value anchor. |
| Android 16 | 40,000 | 5 | 8,000 | DP5 standard HP; self-destruct value, high melee Defense (1252). |
| Android 19 | 40,000 | 4 | 10,000 | DP4 standard HP; ki-drain throws, +2 starting skill stock. |
| Mini Vegeta SS3 | 40,000 | 7 | 5,714 | DP7 standard HP; cheap transform-ladder top form, DP7+ eligible. |
| Mini Vegeta SS2 | 40,000 | 6 | 6,667 | DP6 standard HP; efficient but **sub-DP7 → loses auto-reflect**. |
| **Gohan Beast** | **40,000** (est., null in datamine) | **9** | ~4,444 | #1 DP **score** despite a low HP-index — proves value isn't just HP; kit/damage carry it. |
| Vegito SSGSS | 40,000 (est., null) | 10 | ~4,000 | Premium carry; the standard "1 god" slot. |
| Gogeta (GT) SS4 | 40,000 (est., null) | 10 | ~4,000 | Premium carry; fastest normals in the game. |
| Jiren Full Power | 40,000 (est., null) | 9 | ~4,444 | Armor anchor; expensive, low efficiency index. |
| Cell Max | 40,000 (est., null) | 9 | ~4,444 | Giant-class boss; Max Bomb unblockable, but giant-nerfed. |

> **Datamined facts behind the table:** standard DBZ-roster HP is **40,000** (Piccolo baseline). Heavies — Broly (Z) LSSJ, Broly (Super) SSFP, Beerus, Whis, Kale Berserk, Orange Piccolo, Fusion Android 13 — read **45,000**. The low-HP skirmishers Master Roshi (base), Mr. Satan, and Yajirobe/Spopovich read **30,000-35,000**. GT-era and kid bodies dip to 31k-36k. (`data-mined/characters.json`; HP basics also in `research/04` §1.1.)

## What the table tells you

1. **Raw HP/DP overstates the cheap tanks and understates the gods.** A 30k Roshi at DP2 (index 15,000) is *not* three times better than a 45k Whis at DP10 (index 4,500) — Whis's auto-dodge kit wins neutral outright. The value index is a **starting filter**, not the verdict; that's exactly why **Gohan Beast is #1 on the DP score list** despite a mediocre HP-index — its damage kit overperforms its DP. See the DP table in [[current-meta-tier-list]].
2. **45,000-HP heavies are bulk monsters but premium-priced.** The Brolys (DP9) and Beerus/Whis (DP10) all carry 45k, but you can only fit one or two in a 15-DP budget.
3. **The sweet spot is cheap 40k bodies + one carry.** Master Roshi Max Power (40k @ DP2), Recoome (40k @ DP3), and Android 16/19 (40k @ DP4-5) give standard bulk for very few points.

## Best 15-DP team archetypes (cheap-value)

From `research/05` §5, the dominant post-patch shells. The principle is **1 premium carry + cheap value/utility**, because efficiency matters more now and auto-reflect needs DP7+.

- **"Premium + value" (most common ladder shell):** one **10-DP fusion carry** (Vegito SSGSS or Gogeta GT SS4) + ~5 DP of cheap DP7+ bodies for auto-reflect access and chip. Example: **10 (SS4 Gogeta) + 5** split across two cheap bruisers.
- **Gohan Beast value core:** **Gohan Beast** (DP9, #1 DP score) + **Master Roshi Max Power** (DP2) + a **DP4** body (e.g. Android 19) = 15 DP, with the best DP-efficient carry in the game anchoring it.
- **Cheap-bruiser triple (value spam):** **Recoome** (DP3) + **Yajirobe** (DP2) + a mid like **Mini Vegeta SS3** (DP7) — three overperformers under budget. Strong on the efficiency model, but the sub-DP7 bodies **lose auto-reflect** under the new rule, so it's weaker than its pre-May-2026 form.
- **Heavy-anchor build:** one **Broly** (DP9, 45k HP) + two ~DP3 value bodies (Recoome / Spopovich) — maximum bulk anchor + cheap chip. The Broly satisfies the DP7+ auto-reflect gate.
- **Kale-centric efficient core:** **Kale (Berserk)** (DP7, 45k HP, DP7+ eligible) + **Recoome** (DP3) + **Android 19** (DP4) + **Saibaman** (DP1) = 15 DP across four bodies, all bulk-positive.

## DP-gap mechanics (post-May 26, 2026)

The May 26 patch changed *how DP itself works*, which is why the value math shifted:

| Change | Mechanical effect | Team-building consequence |
|---|---|---|
| **Auto-reflect → DP7+ gate** | Only **DP7+** characters get auto-reflect during [[sparking-mode\|Sparking! Mode]]. | Cheap sub-DP7 turtle shells lost a key defensive tool. Keep at least your **anchor at DP7+** (Kale DP7, Brolys DP9, fusion carries DP10). |
| **DP gap "made more pronounced in all modes"** | The practical strength gap between e.g. a DP7 and a DP3 character **widened** — high-DP picks hit harder relative to cheap ones. | Stacking only cheap bodies is now riskier; the math still favors **1 premium carry** to win damage races. |
| **"Big Impact" item (DP-diff damage, DP Battle only)** | **+500 damage at 1 DP difference, +250 per extra DP** when your attacker out-DPs the defender. | Rewards bringing a high-DP carry into matchups against cheap teams — another nudge toward premium + value. |
| **Roshi / Yajirobe / Mr. Satan Ki-recovery reduced** | Direct nerf to the cheapest tank bodies' resource engine. | The classic cheese value picks still rate S on stale lists but are **drifting down**; weight that when copying a tier list. |
| **Recoome / Spopovich / Nappa HP reduced** | The DP3-and-under bruisers lost some bulk. | Their HP/DP index above is the *pre-or-at-patch* read; treat as a ceiling. |

## Bottom line

- Compute **HP/DP** as a first filter, then **override with kit quality** — Gohan Beast (low HP-index, #1 DP score) is the proof.
- Spend on **one DP7+ carry** for auto-reflect and the widened DP-gap damage, then fill with **cheap 40k bodies** (Roshi Max Power, Recoome, Android 16/19).
- The **45k heavies (Brolys, Kale)** are your best bulk-per-pick if you can afford the DP.
- Cross-reference the DP tier table in [[current-meta-tier-list]] and the ladder in [[ranked-climbing-guide]]; for the resource numbers (ki, skill stocks) every pick spends, see [[beginner-numbers-guide]].

## The ladder-arbitrage table (computed June 10, 2026)

DP prices the **slot you draft, not the form you finish in**. Every transform path worth ≥2 DP of
arbitrage, ranked (endpoint stats datamined):

| Draft (DP) | → Endpoint (DP) | Arb | Stocks | End tier | End HP |
|---|---|---|---|---|---|
| Gohan (Super Hero) (4) | → Gohan Beast (9) | **+5** | 6 | S | ~40k |
| Broly (Z) (5) | → Legendary Super Saiyan (9) | **+4** | 3 | S | 45,000 |
| Broly (Super) (5) | → SS Full Power (9) | **+4** | 3 | S | 45,000 |
| Gohan (Super Hero) (4) | → Ultimate Gohan SH (8) | +4 | 3 | — | 40,000 |
| Piccolo (Super Hero) (5) | → Orange Piccolo (8) | +3 | 3 | A | 45,000 |
| Goku Black (5) | → SS Rosé (8) | +3 | 2 | A | 40,000 |
| Gohan (Adult) (4) | → SS2 (7) | +3 | 2 | A | 40,000 |
| Goku (GT) (5) | → SS4 (8) | +3 | 3 | A | 40,000 |
| Android 13 (5) | → Fusion Android 13 (7) | +2 | 2 | S | 45,000 |
| Kale (5) | → SS (Berserk) (7) | +2 | 3 | S | 45,000 |

### The optimized triple-ladder team (15/15)

**Broly (Z) 5 + Broly (Super) 5 + Android 13 5** → after 8 total stocks: **LSSJ (9S) + SSFP (9S) +
Fusion 13 (7S)** — 25 endpoint-DP of S-tier on a 15 budget, **135,000 team HP**, the lowest
total stock requirement of any top team, and the DP-gap modifier still prices all three as DP-5s.

- **Open with Android 13**: cheapest ladder (2 stocks ≈ 28s), and Wild Sense covers the window.
- **Ceiling variant** (+2 endpoint DP, much riskier): swap A13 → **Gohan (Super Hero) (4)** and
  climb the +5 ladder to Beast — but that path costs **6 stocks** on a DP-4 body; rushdown
  teams will deny it.
- **Anti-deny variant**: swap a Broly → **Piccolo SH → Orange Piccolo (8A, 45k)** — sturdier
  early kit, same 3-stock timing.
- Honorable mention (fusion hybrid): Goku (Z - End) 5 + Vegeta (Z - End) 5 + Recoome 3 — two
  standard bodies with a mid-match **Super Vegito (4-stock Potara)** comeback button.

Trade-offs that keep this honest: transforms **don't heal** (May 26 rule) — climb early and
healthy; laddered fighters skip their form's starting-ki bonus; Fusion 13 is Giant-class, so the
May-2026 giant melee-vulnerability applies; and every ladder team's universal counter is
early-game rushdown on your base forms — bank stocks behind zoning, not in their face.
