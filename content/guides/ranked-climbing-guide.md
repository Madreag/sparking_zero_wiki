---
slug: "ranked-climbing-guide"
title: "Ranked Climbing Guide (Season 0 → Season 1)"
category: "pvp"
summary: "The 26-rank ladder (D5 → Rank Z), Season 0 ending June 30 2026 and Season 1 starting July 1 (~3 months), the win-streak point multiplier (up to 2x), the seasonal soft-reset table (Z→B1, S→B3, A→B5, B→C5, C→D5), and the Single vs DP queue configs."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "confirmed"
sources:
  - "Bandai Namco EU — Notice Regarding Ranked Matches (season system + reset table), 25 May 2026: https://en.bandainamcoent.eu/dragon-ball/news/dragon-ball-sparking-zero-notice-regarding-ranked-matches"
  - "Bandai Namco — June 23 2025 patch notes (win-streak multiplier + reset table, official exact)"
  - "research/05-meta-pvp-tiers.md §4 (ranked system numbers)"
  - "research/01-overview-modes-economy.md §4 (26-rank ladder, queue configs)"
---

Ranked is a **26-rank ladder** running from **D5 (lowest)** up to **Rank Z (top)**. The system is **official** (Bandai ranked-match notices); only the per-rank player **distribution %** is unpublished. Below are the ladder, the season schedule, the point mechanics, and the two queues.

## The 26-rank ladder

Six tiers, each with sub-divisions, low → high:

> **D → C → B → A → S → Z**

- Sub-divisions count **down within a tier as you climb** (you start at the high number and work toward 1): e.g. **D5 → D1**, then **C5 → C1**, up through **B5/B3/B1**, etc. The reset table below uses these exact labels (B1, B3, B5, C5, D5).
- **D5 is the floor** (lowest possible rank); **Rank Z is the ceiling** (no sub-divisions above it in the published mapping).
- That is **26 distinct ranks** total across the six tiers.

## Season schedule (official)

| Season | Starts | Ends | Length | Reward |
|---|---|---|---|---|
| **Season 0** (launch-era open period) | (launch) | **June 30, 2026 — 08:00 UTC** | — | Cosmetic **title** based on final rank |
| **Season 1** | **July 1, 2026 — 08:00 UTC** | ~Oct 2026 | **~3 months** | (per-season title) |

- Season 0 is the long open period the game has run since launch. Your **final Season 0 rank** converts to a cosmetic **title** reward, then your rank **soft-resets** for Season 1.
- Season 1 is the first **fixed ~3-month** competitive season under the new cadence.

## Seasonal soft-reset table (official, exact)

You do **not** start Season 1 from scratch — your new starting rank is derived from where you finished Season 0:

| End-of-season rank | Resets to |
|---|---|
| **Z** | **B1** |
| **S** | **B3** |
| **A** | **B5** |
| **B** | **C5** |
| **C** | **D5** |
| **D** | **D5** |

Practical read: even the **#1 Z-rank player resets to B1**, three sub-divisions into the B tier — so everyone re-climbs the top end each season, but a strong finish still front-loads you well above the D5 floor. Anyone at **C or below resets to the D5 floor**.

## Point mechanics

- **Win-streak bonus — up to 2x rank-point gains.** Consecutive wins escalate your per-win points on the official curve (max streak length 5):

  | Win streak | Point multiplier |
  |---|---|
  | 2 wins | **x1.2** |
  | 3 wins | **x1.4** |
  | 4 wins | **x1.8** |
  | 5 wins | **x2.0** (cap) |

  So a clean 5-win streak doubles your climb rate versus trading wins and losses. Breaking the streak resets the multiplier.
- **Floor on point gain:** since the Sept 22, 2025 patch, you earn a **minimum of 50 points per match regardless of the rank-point gap** — beating a much lower-ranked opponent still pays something.
- **Player Card tracking (since Jan 2026):** Longest Ranked **Single Battle** Win Streak and Longest Ranked **DP Battle** Win Streak, both season-scoped and lifetime — the win-streak multiplier makes these directly valuable, not just cosmetic.

## Queue configs

There are **two independent ranked queues**, each with its own ladder and win-streak tracker:

| Queue | Team size | DP cap | Notes (post-May 26, 2026) |
|---|---|---|---|
| **Single Battle** | 1 character | n/a | **DP damage scaling removed; all characters have standardized HP.** Pick freely for kit quality — see the Singles half of [[current-meta-tier-list]]. |
| **DP Battle** | up to 3-5 characters | **15 DP** (standard ranked) | **DP gap widened** in all modes; **auto-reflect locked to DP7+** in Sparking! Mode. Build around value — see [[dp-team-value-math]]. |

- The **15-DP ranked standard** is the long-running default. Offline / Player Match / World Tournament / Training now expose a **10 / 15 / 20** DP toggle (persists between matches), but whether the **ranked** queue changes its 15-DP standard for Season 1 is **not yet confirmed** (treat 15 as current).
- Matchmaking is by **cost restriction + leaderboards**; a ranked **disconnect penalty wait-time** applies to rage-quitters.

## Climbing checklist

1. **Pick your queue and commit** — the two ladders are separate; splitting time splits your climb.
2. **Single Battle:** ignore DP entirely; play the strongest **kit** you execute well (fusions, Whis, Beerus, UI Goku, Gohan Beast). See [[current-meta-tier-list]] Singles table.
3. **DP Battle:** build a **15-DP** team of **1 premium carry + cheap value bodies**, keeping at least your anchor at **DP7+** for auto-reflect. See [[dp-team-value-math]].
4. **Protect win streaks** — the x1.2 → x2.0 curve means a 5-streak is worth more than double; play your safest character when a streak is live.
5. **Finish the season high** — even a Z finish resets to **B1**, but that is far above the D5 floor that C/D finishers reset to.

## Season 1 preparation (starts 2026-07-01, 08:00 UTC)

Season 0 ends **June 30, 2026 — 08:00 UTC**; Season 1 starts **July 1, 2026 — 08:00 UTC** and runs **~3 months** `[official]`. Here is the soft-reset math, the queue choice, and a concrete first-10-days plan.

### Soft-reset placement math (where you actually start)

Your Season 1 starting rank is **fully determined by your Season 0 finish** via the official reset table — there is **no placement-match variance**, so your June 30 rank *is* your July 1 head start:

| Finish Season 0 | Start Season 1 | Sub-divisions above the D5 floor | Re-climb burden |
|---|---|---|---|
| **Z** (top) | **B1** | high — deepest into B tier | Re-climb only **B1 → S → Z** |
| **S** | **B3** | two sub-divisions below a Z-finisher | B3 → B1 → S → Z |
| **A** | **B5** | bottom of B tier | B5 → … → Z |
| **B** | **C5** | one full tier below B-tier finishers | C5 → B5 → … |
| **C** | **D5** (floor) | none | full climb from the floor |
| **D** | **D5** (floor) | none | full climb from the floor |

**The actionable math:** the reset **compresses the whole top end into the B tier** — a #1 Z player and an A-tier player land just **B1 vs B5** apart (a handful of sub-divisions), while the cliff is **B → C5**: finishing **B drops you a full tier** to C5, but finishing **A keeps you in B (B5)**. So in the final days of Season 0:
- **If you are A or above:** you are guaranteed a **B-tier start** — protect the rank, don't risk-tilt it down.
- **If you are sitting at B:** **pushing from B to A is worth a full tier** at reset (C5 → B5). This is the single highest-leverage climb of the season's end.
- **If you are C or below:** you reset to **D5 regardless**, so play freely / experiment — there's no placement to protect.

### Optimal queue choice

The two ladders are **independent** (separate ranks, separate win-streak trackers), so **commit to one** for Season 1 — splitting time splits your climb `[community]`:

| Queue | Pick it if… | Season-1-relevant facts |
|---|---|---|
| **Single Battle** | You want **pure kit skill** to decide games | **DP damage scaling removed; standardized HP** `[official]`. Meta = raw-kit S-tiers (fusions, Whis, UI Goku, Gohan Beast) — see [[current-meta-tier-list\|tier list]] Singles. **One character to master**, so faster to lab. |
| **DP Battle** | You like **team-building / value optimization** | **15-DP standard** `[community]`; **DP gap widened** + **auto-reflect locked to DP7+** `[official]`. Build **1 premium carry + DP7+ value bodies** — see [[dp-team-value-math\|DP team value math]]. More variables, more comeback paths. |

- **Recommendation for a focused climb:** **Single Battle.** One character to lab, no team-DP math, and the win-streak multiplier (below) applies cleanly to a single mastered pick `[community]`.
- **Whichever you choose, the soft-reset and win-streak rules are identical** across both queues `[official]`.

### First-10-days plan

Season resets flood the **B/C/D** ranks with strong players who soft-reset down — so the **early season is the easiest time to climb** before the ladder re-stratifies. Use the **win-streak multiplier** while opponents are still mismatched to your true skill.

- **Days 1-2 — Lock your main + warm up.** Pick **one** character (Singles) or **one** 15-DP team (DP) and do **not** switch — consistency feeds win streaks. Re-run the [[settings-and-controls\|Training recipes]] (Super Counter timing, CPU recording) to shake off rust **before** you queue, since early losses cost you the easy-climb window.
- **Days 3-6 — Streak-farm the soft-reset chaos.** This is when the ladder is most exploitable. **Chain wins:** the multiplier escalates **x1.2 (2 wins) → x1.4 (3) → x1.8 (4) → x2.0 (5, cap)** `[official]`, so a clean **5-streak doubles your climb rate**. When a streak is live, **play your safest character and your safest gameplan** — a broken streak resets the multiplier to x1. Even a stomp pays a **minimum 50 points** `[official]`, so there's no "wasted" win.
- **Days 7-10 — Bank rank before re-stratification.** As the population settles into true skill bands, easy wins dry up. **Push hard now** to bank the rank gained during the chaos window, then shift to steady climbing. Track your **Longest Ranked Win Streak** on the Player Card (season-scoped since Jan 2026) `[official]` — it's directly valuable given the multiplier, not just cosmetic.
- **Throughout:** apply the live meta — lead vs auto-dodge with **Rush Chain** (pierces UI Goku/Whis since May 2026), punish every **Sparking activation** (defense-down window), and never let a giant wall-lock you (charge-blast knockback). See [[matchups-and-counterpicks\|Matchups & Counterpicks]] for the full counter list and [[offense-and-pressure\|Offense & Pressure]] / [[defense-bible\|Defense Bible]] for the mechanics.

> **The Season 1 thesis:** your June-30 finish is a **free head start** (A-or-above = guaranteed B-tier), and the **first ~week post-reset is the cheapest rank in the game** because everyone is soft-reset below their skill — **streak-farm it early, bank it, then grind.**
