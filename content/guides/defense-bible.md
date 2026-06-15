---
slug: "defense-bible"
title: "The Defense Bible — Every Defensive Option, Cost & Counter (v2.2)"
category: "pvp"
summary: "The complete defensive decision tree for Sparking! ZERO, current to the May 26 2026 patch: for every attack situation (front rush, rush from behind, Vanishing Assault, ki-blast volley, super beam, super rush, ultimate, throw attempt, Sparking pressure) it lists EVERY option with its cost, window, and what it loses to — Guard (chip), Perception (2 stocks + ki), Super Counter (free ~2f, up+rush), Sonic Sway, Revenge Counter (2 stocks), Vanish (≈½ ki bar), Z-Burst escape, sidestep, super armor. Includes a master decision table and anti-pressure ki management (stop charging once you hold ~half a bar for a vanish)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md §3 (defensive input windows), §2.2 (action ki costs), §4 (skill stock costs)"
  - "research/03-patches-balance.md (Dec 2024; Jan 20 2025; Apr 21 2025; Jun 23 2025; Sep 22 2025; May 26 2026 defensive changes)"
  - "research/05-meta-pvp-tiers.md §6 (notorious tech status: Afterimage, auto-reflect, Perception rework)"
  - "Bandai Namco official patch notes (Dec 11 2024 → May 26 2026)"
---

This is the **defensive half** of high-rank Sparking! ZERO: for any attack thrown at you, what are your options, what do they cost, and what beats them. Every figure is tagged `[official]` (Bandai patch notes), `[datamined]` (game files), or `[community]` (player labbing — no official frame data exists). The game runs at **60 fps**, so **1 frame ≈ 16.7 ms** `[community]`.

> **Currency note.** No official frame data has ever been published. Defensive *windows* (Super Counter ~2f, etc.) are **community-measured**; resource *costs* in skill stocks are mostly **official** (patch notes) or **datamined**; ki costs in bars are **community-tested** and may drift patch-to-patch. The structural facts (which patch nerfed what) are official. See [[super-counter|Super Counter]], [[perception|Perception]], [[vanish-z-counter|Vanish]], [[revenge-counter|Revenge Counter]], [[sonic-sway|Sonic Sway]], [[guard-and-chip|Guard]] for the per-mechanic deep dives.

## The defensive toolbox (costs at a glance)

| Option | Input | Cost | Window | Beats | Loses to |
|---|---|---|---|---|---|
| **Guard** | Hold guard | **1 ki bar of chip on guard-break**; per-hit chip otherwise `[datamined]` | Hold (no timing) | Everything frontal (no whiff risk) | **Throws**; **guard-break** (1 bar ki dmg, 1.5 w/ "Mind Breaker" item); chip ticking your ki |
| **Super Counter** | **↑ + Rush** on the hit | **Free** `[official]` | **~2 frames (~33 ms)** `[community]` | Front rush strings, Vanishing Assault follow-ups | Throws; **delayed/staggered strings**; ranged ki; whiff = **lockout + 0 ki gain during attempt** `[official, May 26 2026]` |
| **Perception (melee)** | Hold ○/B, release | **Ki only** (rising, unpublished figure) `[official]` | Read window (charge-holdable follow-up since Sep 2025) | Rush strings; cancels [[afterimage-strike\|Afterimage Strike]] | Throws; **cannot use in guard stun** `[official, Apr 2025]`; mixups/delays |
| **Perception (blast)** | Hold ○/B vs beam | **2 skill stocks** + ki `[official]` | Read window | Beams / Blast-2 supers | Throws; bad read; guard stun |
| **Super Perception → Sonic Sway** | **Frame-perfect** ○/B vs Rush | **Ki only** (no stock vs a rush) `[community]` | **Frame-perfect** (tighter than normal Perception) | Rush — dodge + counter + **drains attacker ki** | Throws; blasts; mistime = eat the rush |
| **Revenge Counter** | R3 / right-stick press | **2 skill stocks** `[official]` (1 in old guides) | Any time, even while being hit | **Combo from ANY direction** (back included) | Costs 2 stocks; **Super Z-Counter** can counter it back |
| **Vanish (Z-Counter)** | R1 just before their Vanishing Assault | **~0.5 ki bar/vanish**, escalating `[community]` | Tight pre-impact window | Vanishing Assault; wins the chain **if you have more ki** | **Less ki than them** (you lose the chain); QTE after **4** vanishes `[official]` |
| **Z-Burst escape** | Z-Burst Dash out of range | **Low initial + scales with distance** (post-May 26) `[official]` | On reaction to a gap | Repositions out of pressure / beams | Costs ki; trackable; beaten by their own Z-Burst / Instant Transmission |
| **Sidestep / Step** | Step (dash sideways) | **0 ki** (short dash) `[community]` | On a gap in pressure | Whiffs linear pokes/beams, repositions | Homing ki blasts; throws if read |
| **Super Armor** | Passive (armor moves / "Power Body" item) | Built-in / **−12% defense** (item) `[datamined]` | While the armor move is active | Tanks **4–5 Smash/Rush-Chain hits** before flinch `[datamined]` | Throws (ignore armor); guard-break; chip-through; big single hits |
| **Afterimage Strike** | Blast-1 skill | **3 skill stocks / 10 s** `[datamined]/[official]` | Auto-dodges all **melee** for the duration | All melee while active | **Perception cancels it**; **Super Counter ends it** `[official, May 2026]`; ki blasts; **Rush Chain pierces auto-dodge** `[official, May 2026]` |

## Situation-by-situation decision tree

### 1. Rush string, from the FRONT
The bread-and-butter pressure. You are being comboed face-to-face.

1. **Super Counter (↑+Rush)** — **free**, ~2f. The default. Aim for the **second hit or the launcher**, not the first `[community]`. Since **May 26 2026** ki does **not** recover during the attempt and a whiff incurs a **lockout** — so *read*, don't mash.
2. **Perception (melee)** — **ki only**; deflect and release into a Smash/Rush-Chain follow-up (**2 stocks** for the follow-up since Apr 2025). Pays damage but is a harder read than Super Counter.
3. **Super Perception → [[sonic-sway\|Sonic Sway]]** — frame-perfect; dodge + counter + **drain their ki**. Best payoff, tightest window.
4. **Revenge Counter (R3)** — **2 stocks**; guaranteed get-off-me when you have no read left.
5. **Guard** — safe but bleeds ki via chip and risks a **guard-break** (1 bar ki dmg). Buys time to find a Super Counter window.

> **Loses to:** all of the above lose to a **delayed/staggered string** (beats Super Counter timing) and to a **throw** (ignores guard, counters, and parries). See situation 8.

### 2. Rush string, from BEHIND
You got turned around. Your options shrink hard.

1. **Revenge Counter (R3)** — **2 stocks**. The *only* reliable answer; it breaks a combo **from any direction including the back** `[official]`. This is what Revenge Counter exists for.
2. **Super Counter** — **does NOT work from behind** (it is a front-facing reversal) `[community]`. Don't waste the input.
3. **Vanish** — if the back-rush includes a Vanishing Assault you can R1 it, but if you're being meleed from behind there's usually no vanish prompt.
4. **Hold guard and wait** — back-guard exists; eat chip until they reset to the front, then Super Counter. Note longer rush chains **grant YOU more skill stock when hit from behind** `[official]`, so a back-combo at least feeds your Revenge Counter.

### 3. Vanishing Assault pressure (vanish war)
They teleport-strike; you can clash repeatedly.

1. **Vanish (R1)** — **~0.5 ki bar each**, escalating; each subsequent vanish is **faster and costs more** `[official]`. After **4 consecutive** a **QTE/Impact clash** decides it `[official]`.
2. **The rule that decides it: whoever has more ki wins the chain** `[community]`. If you have less ki, **bail early** (guard or sidestep out) rather than feed a losing vanish war.
3. **Super Counter** — works on the *melee* portion of a Vanishing Assault follow-up.
4. **Note:** you gain only **~15% of a skill gauge per vanish** and the Jan 2025 patch **reduced** skill gain from vanish wars — you can no longer fish stocks for free `[official]`.

### 4. Ki-blast volley (rush ki blasts / spread)
Chip from range.

1. **Guard** — ki blasts chip-guard cleanly; the cheapest answer. Note **Rush Ki Wave reduces your ki when guarded** `[official, Jan 2026]`, so don't hold guard into a ki-wave forever.
2. **Deflect** — tap guard on the blast to deflect; deflect→Smash is **fast** since Sep 2025 `[official]`.
3. **Perception (blast)** — **2 skill stocks**; only worth it vs a committed big blast, not a pea-shooter volley.
4. **Sidestep / Z-Burst** — step out of linear volleys; homing variants force a guard.
5. **Good news (May 26 2026):** Rush Ki Blast **damage was reduced with harsher consecutive scaling** `[official]` — volleys chip for less than they used to. **Immunity to ki-blast stun** exists inside [[sparking-mode\|Sparking! Mode]] `[official]`.

### 5. Super beam (Kamehameha-class Blast 2)
A committed beam super.

1. **Perception (blast)** — **2 skill stocks** + ki; deflects it outright. The clean answer if you have the stocks.
2. **Vanish / Z-Burst out of the line** — beams are linear; reposition off-axis. Z-Burst out costs **low+distance-scaled** ki (post-May 26).
3. **Guard** — you'll take **chip**; acceptable if you can't afford 2 stocks.
4. **Beam clash** — fire your own beam into it; **Blast Impact Power** (clash priority 0–5) decides who wins `[datamined]`.
5. **Sidestep** — short dash perpendicular; **0 ki** `[community]`, but only beats non-homing beams.

### 6. Super RUSH (Blast-2 melee rush super)
A super that starts as a melee rush (e.g. a Final-Kamehameha-style rush ender, "Speed Impact" moves).

1. **Super Counter** — **free**, can reverse the melee portion if you catch the connect frame.
2. **Perception (melee)** — **ki only**; reads the rush.
3. **Sonic Sway** — frame-perfect Super Perception vs the rush; dodge + counter + ki drain.
4. **Revenge Counter** — **2 stocks**; if it catches you mid-string, breaks it from any direction.
5. **Vanish** — if it has a Speed-Impact / vanish-clash component, R1 it (ki-economy rule applies).

### 7. Ultimate Blast
The 50,000-energy finisher `[datamined]`.

1. **Get out of range** — most ultimates are committed and slow to start; **Z-Burst / Dragon Dash** out is often cleanest. Long-range Blasts/Ultimates had **speed reduced** (Dec 2024) `[official]`, widening your escape window.
2. **Perception (blast)** — **2 skill stocks** deflects a beam/blast ultimate if you read it.
3. **Vanish** — some ultimates can be vanished on the clash frame.
4. **Guard** — last resort; ultimate chip is severe but a guard beats eating the full hit.
5. **Bait it** — if they're charging an ultimate, the **defense-down window** from a fresh Sparking activation (situation 9) or their commitment is your cue to punish, not defend.

### 8. Throw attempt
The universal mixup that **beats guard, Super Counter, Perception, and Sonic Sway** — all of which throws ignore.

1. **Don't be passive** — the only true counters to a throw are **moving (it whiffs)** or **hitting them first**. Throws have startup; a pre-emptive Super Counter/poke or a sidestep beats a read throw.
2. **Throw damage is ~1,250–1,312** `[datamined]` — low compared to a combo, so eating one occasionally is fine; the danger is the *mixup* (throw vs strike) breaking your guard habit.
3. **Giants and Ki-Drain Androids are throw threats:** giants are **throw-IMMUNE** (you can't throw them; situation handled in matchups), and **Ki-Drain Androids (19, Gero)** have **huge throw damage (3,594 / 3,875)** `[datamined]` — respect their grab.
4. **Tech awareness:** the Sep 2025 patch removed skill-stock gain on a successful **tech** but **increased** gain on a successful **Attack Break** `[official]` — break out, don't just tech.

### 9. Sparking! Mode pressure
They popped [[sparking-mode\|Sparking! Mode]] and are bearing down with ki-free actions and boosted damage.

1. **Punish the activation window** — since **Jun 23 2025** (instant-Sparking) and **May 26 2026** (all Sparking + Full-Ki-Recovery), **activating Sparking lowers defense for a window** `[official]`. The moment they pop it, they're **more vulnerable** — strike, don't cower.
2. **Auto-reflect is gone for cheap characters** — since **May 26 2026**, **auto-reflect only works on DP7+ characters** in Sparking `[official]`. A sub-DP7 body in Sparking does **not** auto-reflect your blasts — keep shooting.
3. **Out-space it** — Sparking is a **timed** buff (base duration unpublished; items add **+3 s**) `[datamined]`. Run the clock: Z-Burst/Dragon Dash to safety and let it expire.
4. **Don't panic-Sparking back** — popping your own Sparking defensively now exposes *you* (same defense-down). Save it for offense.
5. **Standard defense still applies** to their actual hits — Super Counter their rushes, Perception their blasts.

## Master defensive decision table

| Incoming | #1 (cheapest/safest) | #2 | #3 | Hard counter that beats your defense |
|---|---|---|---|---|
| **Front rush** | Super Counter (free, ~2f) | Perception (ki) | Revenge Counter (2 stk) | Delayed string; **throw** |
| **Rush from behind** | **Revenge Counter (2 stk)** | Guard + wait | — | Continued back-pressure (no SC from behind) |
| **Vanishing Assault** | Vanish if ki-ahead (~0.5/vanish) | Super Counter the melee | Bail if ki-behind | More ki than you (loses chain) |
| **Ki-blast volley** | Guard / Deflect | Sidestep | Perception-blast (2 stk) | Homing variants force guard |
| **Super beam** | Perception-blast (2 stk) | Vanish/Z-Burst off-line | Guard (chip) | Tracking; low stocks |
| **Super rush** | Super Counter (free) | Sonic Sway | Revenge Counter (2 stk) | Throw component; delay |
| **Ultimate** | Escape range (Z-Burst) | Perception-blast (2 stk) | Guard (last resort) | Cornered with no ki/stocks |
| **Throw** | Move (whiff) / hit first | — | — | (Throw IS the counter to passive defense) |
| **Sparking pressure** | Punish activation defense-down | Out-space / run clock | Standard per-hit defense | Their boosted damage if you stand still |

## Anti-pressure ki management (the half-bar rule)

Your ki is your defensive budget. Charging refills it but **leaves you open**; the question is when to *stop* charging and start holding.

- **Hold a vanish in reserve.** A single vanish costs **~0.5 ki bar** `[community]`; a practical reserve floor is **~5,000 ki (half a bar)** — enough to answer the first exchange. **Once you hold about half a bar, stop free-charging** and keep that reserve — you always want enough to **answer a Vanishing Assault**, because the vanish war is won by **whoever has more ki**.
- **Charging is a commitment.** Manual charge is **~1.4 ki/sec** `[datamined]`. Charging to full takes real time during which you can't act — only charge when you have a safe gap (they're far, recovering, or you're out of their Z-Burst range).
- **Stop charging at ~half a bar when pressure is imminent.** If the opponent is within Z-Burst range, do **not** be caught mid-charge with a depleted bar — that's how vanish wars are lost and how you get opened up. Bank the reserve, play your defense, recharge on the next real gap.
- **Ki-exhaustion is a death sentence.** If your bar goes **red you cannot move** until it recovers `[official]` — never let charging or a lost vanish war drain you to red under pressure.
- **Skill stocks are your second budget.** Revenge Counter (**2**), blast Perception (**2**), and Afterimage (**3**) all draw from the same **~1 stock / 14 s** regen `[datamined]`. Spend stocks on the situations that *only* stocks solve (back-rush → Revenge Counter; beams → Perception), and use the **free** Super Counter everywhere you can to preserve them. The May 26 2026 patch **slightly reduced** stock regen `[official]`, so stock discipline matters more now.

## What the May 26 2026 patch changed for defense

- **Super Counter:** still free/~2f, but **no ki recovery during the attempt** — mashing now bleeds your reserve `[official]`.
- **Perception:** **2 skill stocks** for Smash/Rush-Chain follow-up, **higher ki cost**, **unusable in guard stun** `[official]`.
- **Auto-reflect:** **DP7+ only** in Sparking `[official]`.
- **Afterimage Strike:** ends on **Super Counter**; **Rush Chain pierces** the auto-dodge `[official]`.
- **Sparking activation:** **defense-down window** — no more safe panic-Sparking `[official]`.

The throughline: **reactive defense got more expensive, and the free option (Super Counter) got punished for spam.** Precision beats panic. For the offensive mirror of this guide see [[offense-and-pressure|Offense & Pressure]]; for how each tool fares vs the meta cast see [[matchups-and-counterpicks|Matchups & Counterpicks]]; for the live tier context see [[current-meta-tier-list|the current tier list]].
