---
slug: "beginner-numbers-guide"
title: "Beginner Numbers Guide — The 10 Numbers Every New Player Needs"
category: "beginner"
summary: "The ten core numbers a new player must internalize: a vanish costs ≈half a ki bar (community-measured), 10,000 HP = 1 health bar, supers cost ~30,000 / ultimates ~50,000, the Super Counter window is ~2 frames, skill stocks regen every ~14s, Perception vs blasts costs 2 stocks, HP tiers (30k/40k/45k), and the 15-DP team budget — each linked to its full mechanics page."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "data-mined/characters.json (vanishKiCost 2800, ultimate kiCost 50000, super kiCost 20k/30k/40k, hp tiers)"
  - "research/04-mechanics-frame-data.md §0 quick reference (must-know numbers)"
  - "research/02-roster-dp-dlc.md (15-DP budget)"
  - "content/mechanics/* (linked mechanic pages)"
---

Sparking! ZERO hides almost all of its numbers — the game shows you bars, not values — but the **datamine** exposes them. Internalize these ten and you will stop guessing at ki, health, and skill economy. Each links to its full mechanics page.

## 1. A vanish costs about half a ki bar

Every vanish (the [[vanish-z-counter|Z-Counter]] teleport that reverses an incoming attack) costs **≈5,000 ki — about half a bar** `[community]` (the cost is not stored in the parameter tables; community-measured, and it escalates over consecutive exchanges). After **4 consecutive vanishes** a QTE/Impact clash triggers, and **whoever has more ki wins** the chain. Bail early if you're behind on ki. See [[vanish-z-counter]].

## 2. 10,000 HP = one health bar

A standard fighter has **40,000 HP** shown as roughly **4 bars**, so **~10,000 HP per bar** `[datamined / community-tested]`. A combo dealing ~20,000 damage takes "two full bars." This is your damage yardstick: a raw ultimate hitting for ~17,000-19,000 is nearly two bars. See [[ki-and-charging]] for the ki side.

## 3. Supers cost ~30,000 ki; ultimates cost 50,000

[[sparking-mode|Super (Blast 2)]] attacks cost **20,000-40,000 ki** (most are **30,000**), and **every Ultimate Blast costs exactly 50,000** `[datamined]` — universal across the roster. Since your full gauge is **5 ki bars**, an ultimate is roughly a full gauge. You can only use ultimates in [[sparking-mode|Sparking! Mode]].

## 4. The Super Counter window is ~2 frames

[[super-counter|Super Counter]] (↑ + Rush at the exact frame a hit lands) reverses a rush combo for **free**, but the input window is only **~2 frames (~33 ms)** `[community-tested]` — a minority argue up to 4f. It's the only zero-cost escape, which is why it defines high-rank play. Failed attempts now incur a lockout, and (since May 26 2026) **ki no longer recovers during the attempt**. See [[super-counter]].

## 5. Skill stocks regen about every 14 seconds

[[skill-count|Skill stocks]] (the resource for skills, transformations, and counters) auto-regenerate at **~1 stock per ~14 seconds** (~4.2/min) `[datamined]`. Max is character-specific, typically **4-5**. Most characters **start at 0 stocks**; Androids start +1, ki-drain Androids (19/Gero) +2. The May 26 patch **slightly reduced** the regen rate. See [[skill-count]].

## 6. Perception vs blasts costs 2 skill stocks

[[perception|Perception]] (hold guard to parry) is **ki-only against melee**, but parrying a **blast** (like an incoming Kamehameha) costs **2 Skill Count** `[official]`. The May 26 2026 rework also raised the **Smash/Rush-Chain follow-up** cost to **2 stocks** and banned Perception **during guard stun** — it now rewards precision over spam. See [[perception]].

## 7. The Super Counter / vanish stack is your defensive economy

Your defensive options aren't free reads — they're a **resource budget**:

| Option | Cost |
|---|---|
| [[super-counter|Super Counter]] | **0** (free, ~2f window) |
| [[vanish-z-counter|Vanish / Z-Counter]] | **≈½ ki bar** per vanish `[community]` |
| [[perception|Perception]] vs blast | **2 skill stocks** |
| [[revenge-counter|Revenge Counter]] | **2 skill stocks** |

Spend skill stocks on defense and you can't transform or use a skill — that tradeoff is the core of high-level play.

## 8. HP tiers: 30k / 40k / 45k

Three datamined HP bands define how tanky a pick is `[datamined]`:

| HP | Who | Read |
|---|---|---|
| **30,000-35,000** | Master Roshi (base), Mr. Satan, Yajirobe, Spopovich | Low-HP skirmishers (cheap DP value). |
| **40,000** | Standard DBZ roster (Goku, Piccolo, Cell, Vegeta…) | The baseline body. |
| **45,000** | Broly (Z) LSSJ, Broly (Super) SSFP, Beerus, Whis, Kale Berserk, Orange Piccolo | Heavies — best bulk, usually premium DP. |

These matter most in **DP Battle** (see [[dp-team-value-math]]); in **Single Battle**, HP is **standardized** so this tier list doesn't apply there.

## 9. Sparking! Mode powers up — but exposes you now

[[sparking-mode|Sparking! Mode]] unlocks your **ultimate**, makes dashes/blasts **ki-free**, grants ki-blast stun immunity, and applies the **"Boosted" damage values (~x1.2-1.5)**. Entry needs a **full ki gauge + 1 skill stock**. [[instant-sparking|Instant Sparking]] skips the gauge for **4 skill stocks** (was 3 at launch). Catch since May 26 2026: **activating Sparking! lowers your defense for a window** — no more panic-popping it safely. See [[sparking-mode]] and [[instant-sparking]].

## 10. Your DP team budget is 15

In **DP Battle** (and ranked DP queue), you build a team under a **15 Destruction Point** cap, each character costing **1-10 DP**. Cheap value picks (Roshi DP2, Recoome DP3) overperform their cost; gods (Beerus, Whis, fusions) cost **10 DP** each. Since May 26 2026, **auto-reflect needs DP7+**, so keep at least your anchor expensive. Full breakdown in [[dp-team-value-math]]; current rankings in [[current-meta-tier-list]].

---

**Next steps:** drill the [[super-counter]] window in training, learn your character's [[skill-count]] max and starting stock, and read [[ranked-climbing-guide]] before queuing ranked.
