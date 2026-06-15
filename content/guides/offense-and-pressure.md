---
slug: "offense-and-pressure"
title: "Offense & Pressure — Opening Neutral, Mixups & Conversions (v2.2)"
category: "pvp"
summary: "The offensive playbook for Sparking! ZERO, current to the May 26 2026 patch: opening neutral (Z-Burst dash approach costs, ki-blast checks), rush mixups (delays beat Super Counter mashing; throw beats guard; how the May 2026 Rush Chain buff pierces auto-dodge), snap-vanish pressure, unblockable setups (which S1s carry the bIsImpossileGuard flag), Sparking conversion routes, and the combo-into-ultimate damage reality (scaling makes a raw ultimate often out-damage a long combo-into-ult — cited from datamined lab numbers)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md §1.5-1.6 (combo scaling, Rush Chain), §2.2 (Z-Burst/dash ki), §5 (Sparking), §8 (unblockable/Impossible Guard flag)"
  - "research/03-patches-balance.md (Dec 2024 → May 26 2026 offense/blast/Rush-Chain changes)"
  - "research/05-meta-pvp-tiers.md §6 (Rush Chain beats auto-dodge; unblockable status)"
  - "content/skills/* (datamined 'unblockable, no-auto-guard' flags: god-bind, magic-bind, cry-of-rage, solar-flare, etc.)"
  - "Bandai Namco official patch notes (Dec 11 2024 → May 26 2026)"
---

This is the **offensive half** of high-rank Sparking! ZERO: how to open the opponent, how to keep your turn, and how to convert a hit into maximum damage. Tags are `[official]` (Bandai patch notes), `[datamined]` (game files), `[community]` (player labbing). 60 fps → **1 frame ≈ 16.7 ms**. Read alongside [[defense-bible|The Defense Bible]] (the mirror), [[matchups-and-counterpicks|Matchups & Counterpicks]], and [[current-meta-tier-list|the current tier list]].

> **Currency note.** Ki/frame numbers are **community-tested** (no official frame data); skill-stock and damage values are **datamined**; the "what changed when" is **official**. Combo damage figures are from community lab teardowns and are the headline reason this guide exists.

## 1. Opening neutral

Neutral is a **ki-economy duel** before it's a damage duel. You win the opening by approaching efficiently and forcing a reaction you can punish.

### Approach costs
- **Z-Burst Dash** (the around-the-opponent fast approach): **low initial cost, then scales with travel distance** since the **May 26 2026** patch `[official]` — a **short hop is cheap, a full-screen dash is expensive**. So **close the gap in stages**: walk/short-dash to mid, then Z-Burst the last stretch. Don't burn a full-screen Z-Burst from the back wall.
- **Short (Burst) Dash:** **0 ki**, chainable `[community]` — your free neutral movement. Use it to bait, micro-space, and bridge into a cheap Z-Burst.
- **High-Speed Dragon Dash:** ~**50% faster than Z-Burst** `[official]`, "significantly reduced" ki cost; **guarantees you reach the opponent's front** despite trajectory manipulation `[official, Apr 2025]`. The premium gap-closer when you've banked ki.
- **Rapid Ascend/Descend:** ki cost **increased** May 26 2026 `[official]` — no longer a free vertical reset; use sparingly.

> **Ki discipline:** you still want to hold a **~half-bar vanish reserve** (see [[defense-bible|Defense Bible]] §ki management) even on offense, because a whiffed approach can flip into a vanish war you'll lose if depleted.

### Ki-blast checks
- **Throw a ki-blast check** to force a defensive commitment: the opponent must **guard, deflect, Perception, or sidestep** — each tells you what they'll do under pressure, and each costs *them* something. **Rush Ki Wave reduces their ki when guarded** `[official, Jan 2026]` — chip their economy for free.
- **Cost:** **16–22% of a ki bar per shot** (Normal class ~20%, Ki-Blast class ~16%) `[datamined]`. Cheap, but don't volley your whole bar away — May 26 2026 **reduced Rush Ki Blast damage with harsher consecutive scaling** `[official]`, so blasts are a *poke*, not a kill.
- **Best use:** a single check to read the opponent, then convert the reaction (they guard → approach for a throw; they Perception → bait the recovery; they sidestep → Dragon Dash the predicted position).

## 2. Rush mixups (keeping your turn)

Once you're in, your pressure is a guessing game with three layers. The opponent's best defense is the **free** Super Counter (~2f), so your job is to **beat the Super Counter**.

### Layer 1 — Delays beat Super Counter mashing
- Super Counter is a **~2-frame** read on the **exact hit-connect frame** `[community]`. A defender who **mashes ↑+Rush** is timing the *expected* rhythm of your string.
- **Stagger your string** — delay the next hit by a beat — and the masher's input falls in the **whiff lockout** the Jan 2025 patch added `[official]`. Since **May 26 2026** a whiffed Super Counter also **gains no ki** `[official]`, so baiting whiffs **drains their reserve** while you stay plus.
- Practical: mix **fast strings** (catch them not mashing) with **delayed strings** (catch the mashers). This is the core of opening a turtle.

### Layer 2 — Throw beats guard
- A patient defender who just **holds guard** eats your strings safely (chip aside) and waits for a Super Counter window. **Throw them.** A throw **ignores guard, Super Counter, Perception, and Sonic Sway** — it is the universal answer to a blocker `[community]`.
- **Throw damage ~1,250–1,312** `[datamined]` — modest, but it **resets pressure** and breaks the guard habit so your next strike-string lands clean. The real value is the **strike/throw 50/50**: once they fear the throw, they stop holding guard and your rush opens up.
- Don't throw a **giant** (throw-immune) — see [[matchups-and-counterpicks|Matchups]] for the giant answer.

### Layer 3 — Rush Chain pierces auto-dodge
- **Rush Chain = `□ (×1–4) + △`** `[official]`. Against the auto-dodge top tier ([[goku-super-ultra-instinct|UI Goku]], [[whis|Whis]], [[afterimage-strike|Afterimage Strike]] users), the **May 26 2026** patch is the game-changer: **Rush Chain can be executed even while attacks are being auto-dodged** `[official]` — it **explicitly names UI Goku & Whis**.
- **Translation:** auto-dodge no longer makes a character un-pressurable. Lead your offense vs those characters with **Rush Chain** rather than plain rush strings — the chain connects through the evasion.
- **Tradeoff:** a **longer chain = more damage but more escape windows** and **more skill stock granted to the victim when hit from behind** `[official]`. Don't always go max length — `□×1–2 + △` keeps your turn tighter and feeds the opponent fewer stocks.

### Snap-vanish pressure
- After a blocked/connected string, a **snap vanish** (vanish to the opponent's back) keeps the pressure rotating, but each vanish costs **~0.5 ki bar** and **escalates** `[official]` — and the **vanish war is won by whoever has more ki** `[community]`. Only snap-vanish when you're **ki-ahead**; otherwise you hand them the clash.
- Vanish pressure now grants only **~15% skill gauge** with **reduced** gain from vanish wars `[official]` — it's a positioning tool, not a stock farm.

## 3. Unblockable setups

Some Blast-1 (S1) skills and Smash Ki Blasts carry the datamined **`bIsImpossileGuard`** flag (in the wiki's skill pages this shows as the **`unblockable, no-auto-guard`** flag) — they **cannot be guarded**, making them guaranteed mixup enders *if* they connect.

### Which S1s are flagged unblockable `[datamined]`
From the datamined skill pages (CUE4Parse extract, Steam build 22517964):

| Skill | User(s) | Flag |
|---|---|---|
| [[god-bind\|God Bind]] | Goku (Super) Super Saiyan God | unblockable, no-auto-guard |
| [[magic-bind\|Magic Bind]] | Third Eye Gomah | unblockable, no-auto-guard |
| [[cry-of-rage\|Cry of Rage]] | Kale (Berserk) | unblockable, no-auto-guard |
| [[solar-flare\|Solar Flare]] | (multiple) | unblockable, no-auto-guard |
| [[paralyze-beam\|Paralyze Beam]] / [[sealing-paralyze-beam\|Sealing Paralyze Beam]] | (multiple) | unblockable, no-auto-guard |
| [[psychokinesis\|Psychokinesis]] / [[telekinesis\|Telekinesis]] | (psychic users) | unblockable, no-auto-guard |
| [[demon-eye\|Demon Eye]] / [[evil-breath\|Evil Breath]] / [[vice-shout\|Vice Shout]] / [[powerful-shout\|Powerful Shout]] | (various) | unblockable, no-auto-guard |

*(18 skill pages carry the `unblockable` flag total in the datamine — the table above lists the combat-relevant ones.)*

### How to use — and the catch
- **They beat guard**, so the setup is: condition the opponent to **hold guard** (via strike/throw pressure), then land the unblockable while they're committed to blocking.
- **But unblockable ≠ unbeatable as of 2026.** The counters stack up across patches:
  - **Jun 23 2025:** unblockable **Smash Ki Blasts → Vanish-evadable**, tracking reduced `[official]`.
  - **Sep 22 2025:** general unblockable **Rush Blasts → evadable with auto-evasion skills** (Afterimage etc.) `[official]`.
  - **May 26 2026:** auto-evasion skills can now evade **unblockable charge Blasts** too `[official]`.
- **So the guaranteed-damage version is largely gone.** An unblockable still beats *guard*, but it can be **vanished, sidestepped, or auto-dodged**. Use it as a **mixup option** (vs a blocker), not a guaranteed kill. **Cell Max Max Bomb** is unblockable since Jan 2026 `[official]`, but Cell Max is giant-nerfed (see [[matchups-and-counterpicks|Matchups]]).

## 4. Sparking conversion routes

[[sparking-mode|Sparking! Mode]] is your damage spike. Convert *into* it on offense, not as a panic button.

- **Entry:** **full ki + ≥1 skill stock**, then charge to fill the separate Sparking gauge, spend **1 stock** to activate `[official]`. **Instant Sparking** skips the gauge for **4 skill stocks** (was 3 at launch) `[official]`.
- **The activation is now risky.** Since **May 26 2026**, activating Sparking (or any Full-Ki-Recovery skill) **lowers your defense for a window** `[official]`. So **don't pop it raw in neutral** where you can be punished — pop it:
  1. **After a knockdown / hard read** when the opponent can't immediately punish, or
  2. **Mid-combo** to access boosted damage and your Ultimate, or
  3. **Out of the opponent's range** so the defense-down window is safe.
- **What you gain:** access to your **Ultimate Blast**, **ki-free actions** (dashes/blasts cost no ki), **immunity to ki-blast stun**, and **boosted blast damage (≈×1.2–1.5)** `[official]/[datamined]`.
- **Sparking combo scaling is HARSHER.** The Dec 2024 patch **increased** the consecutive-hit damage reduction *inside* Sparking `[official]` — so a long Sparking combo proration eats your damage. Prefer **short, high-value routes** in Sparking, capped by an Ultimate or boosted super.
- **Auto-reflect note:** in Sparking, only **DP7+** characters auto-reflect blasts `[official, May 2026]` — a cheap body in Sparking does not get that defensive perk.

## 5. The combo-into-ultimate damage reality

**The single most important offensive number in the game:** because combo scaling is **aggressive**, a **raw Ultimate frequently out-damages a long combo → Ultimate**. The combo's proration carries *into* the finisher, so padding hits before an ult can **lower** your total.

### The lab evidence `[community/datamined]`
| Route | Total damage | Source |
|---|---|---|
| **Kid Gohan — raw Ultimate** | **17,388** | community lab, Dec 2024 |
| Kid Gohan — 60+ hit combo → same Ultimate | **~13,000–15,000** (whole sequence) | community lab |
| **SS4 Gogeta — raw Ultimate** | **19,950** | community lab |
| SS4 Gogeta — 70-hit combo → Ultimate | **~19,250** (whole sequence) | community lab |
| **SS4 Gogeta — optimized SHORT combo** (`□×5 → Step-in+↓+△ → ↑+△ → □ → Rush Super`) | **19,832 (≈2 health bars), unboosted** | GameFAQs reference combo |

### Takeaways
1. **A raw Ultimate can beat a 60–70-hit combo into the same Ultimate.** If you have the meter, **just throw the ult** in many cases — the long combo is *flashier and worse*.
2. **Optimal real damage = short combos on high-ATK characters.** The SS4 Gogeta reference does **~2 health bars (19,832)** off a **single short string into a rush super** — that's the model: a handful of hits, high per-hit ATK, capped by a super/ultimate.
3. **Datamined ult/super baselines** for calibration: Ultimates universally cost **50,000 energy**; Super Kamehameha (Cell) base **9,080 → boosted 13,660**; Special Beam Cannon (Piccolo) ult base **15,000 → boosted 19,638**; Perfect Barrier (Cell) ult base **19,620 → boosted 25,584** `[datamined]`. **Boost ≈ ×1.2–1.5** in Sparking.
4. **May 26 2026 nuance:** the patch **reduced Blast/Ultimate damage when hit during a combo** and **reduced consecutive-Blast damage**, *but* **eased** the scaling on **Ultimate Blasts hitting mid-combo** (a partial walk-back) `[official]`. Net: combo→ult is slightly less bad than it was, but a **clean raw ult is still often the higher-damage, lower-risk choice** — and it skips the dropped-combo risk entirely.

### The rule
> **Don't chase the 100-hit combo.** Land a **short, high-ATK string** (≈5 hits), cap it with a **rush super or raw Ultimate**, and you'll out-damage the flashy long combo while spending less time exposed. Use the freed time to maintain your **ki reserve** and your **turn**.

## What the May 26 2026 patch changed for offense

- **Z-Burst Dash:** low initial cost **+ distance scaling** — approach in stages `[official]`.
- **Rush Chain:** **pierces auto-dodge** (UI Goku / Whis named) — your answer to the evasion tier `[official]`.
- **Rush Ki Blast:** **damage down, harsher consecutive scaling** — blasts are pokes `[official]`.
- **Unblockables:** now **auto-evasion-evadable** (on top of Vanish-evadable since 2025) — mixup tool, not a guarantee `[official]`.
- **Sparking activation:** **defense-down window** — convert into it safely, never raw in neutral `[official]`.
- **Ultimate-in-combo scaling:** **eased** slightly — but raw ults still win on damage/risk `[official]`.

The throughline: **opening neutral is a ki/stock economy, your mixup must beat the free Super Counter (delay + throw + Rush Chain), and your damage comes from SHORT routes capped by a super/ultimate — not long combos.** For how this plays out against each meta pick, see [[matchups-and-counterpicks|Matchups & Counterpicks]].
