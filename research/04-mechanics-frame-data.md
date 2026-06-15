---
title: "Combat Mechanics — Formulas, Frame Data & System Values"
game: "DRAGON BALL: Sparking! ZERO"
date: 2026-06-10
latest_build_referenced: "2026-05-25/26 patch (Season 0); next update June 27 2026"
confidence: medium
confidence_notes: >
  Datamined stat values (HP, ATK, defense, ki, blast energy costs) are HIGH confidence
  (sourced from the sparkingzerometa.com datamine wiki + sparking0data team builder).
  Frame windows for defensive options are COMMUNITY-TESTED (no official frame data is
  published); the most-cited Super Counter figure is 2f but a 4f camp exists. Official
  patch notes describe changes qualitatively ("increased", "reduced") and almost never
  give exact numbers, so most ki/skill costs come from community labbing and may drift
  patch-to-patch. Several widely-circulated "precise" figures (e.g. an AI-generated
  research pass claiming HP standardized to 6,000, Afterimage = single dodge, Sparking =
  exactly 15s/+25%) are UNVERIFIED or contradicted by primary sources — see Gaps.
tags: [sparking-zero, frame-data, mechanics, damage-formula, ki-system, datamine]
sources:
  - "sparkingzerometa.com (datamine: character stats, items, blast energy costs)"
  - "sparking0data.github.io/calculator (team builder: HP/ATK/KI/SSK/MSK)"
  - "w.atwiki.jp/sparkingzero (JP wiki: durability/attack tables, flightless chars)"
  - "dbzsparkingzero.fandom.com (skill pages: Afterimage Strike, Wild Sense, Senzu, Sparking Mode)"
  - "Bandai Namco official patch notes (Dec 2024, Jan 20 2025, Jun 23 2025, Sep 22 2025, Dec 15 2025, Jan 2026, Feb 19 2026, Apr 21 2026, May 25-26 2026)"
  - "Steam Community discussions (super counter 2f testing, Jan 2025 patch breakdown, vanish war costs)"
  - "GameFAQs boards 439864/439865; r/SparkingZero; IGN/Game8/TheGamer guides"
---

# Combat Mechanics — Sparking! ZERO

> **How to read the tags**
> `[datamined]` = pulled from game files (high trust).
> `[official]` = stated in Bandai Namco patch notes / official guides.
> `[community-tested]` = measured by players (training mode, frame-stepping, labbing). Trust varies.
> `[community-claim]` = asserted in community/AI write-ups but NOT independently verified here.
> The **Patch** column = the build the number was measured/last-confirmed on. "Launch" = 1.00 (Oct 11 2024). Treat anything pre-2025 as possibly stale.

> **CRITICAL CAVEAT ON UNITS.** The game exposes two number spaces:
> 1. **Internal datamine units** (HP ~40,000; melee 1st-hit ~390; blast "energy" cost 30,000/50,000). These are what the files store.
> 2. **Player-facing bars** (5 ki bars; 4-ish health bars; skill stock count). Conversions between the two are partly inferred — see notes.

---

## 0. Quick reference — the "must-know" numbers

| System | Value | Tag | Patch |
|---|---|---|---|
| Standard character total HP | **40,000** (datamine "durability" = HP × defense factor) | [datamined] | current |
| Health bars (standard) | ~4 bars → **~10,000 HP / bar** | [datamined]/[community-tested] | current |
| Ki gauge | **5 ki bars** | [official] | current |
| Ki blast cost | **16–22% of one bar per shot** (char-dependent; 20% typical) | [datamined] | current |
| Super attack energy cost | **30,000–40,000** | [datamined] | current |
| Ultimate attack energy cost | **50,000** | [datamined] | current |
| Super Counter window | **~2 frames** (≈33–40 ms); 4f minority claim | [community-tested] | current |
| Revenge Counter cost | **2 skill stock** (1 in some early sources) | [official]/[community] | current |
| Wild Sense cost | **2 skill stock** | [official] | current |
| Afterimage Strike | **3 skill stock**, **10 s** duration | [datamined]/[official] | current |
| Senzu Bean | **5 skill stock** (full heal); 6 for buffed Yajirobe | [datamined]/[official] | current |
| Instant Sparking cost | **4 skill stock** (was 3 at launch) | [official] | Jan 20 2025 → |
| Z-Burst Dash | **0.75 ki** (non-giant) / **2 bars** (giant) | [community/official] | Jan 20 2025 |
| Vanish (Z-Counter) cost | **~0.5 ki/vanish**, QTE after **4** consecutive | [community-tested] | Jan 20 2025 → |
| Skill stock auto-regen | **~14 s/stock** base (≈4.2 stock/min) | [datamined]/[community] | pre-May-2026 |

---

## 1. Health & Damage Basics

### 1.1 Health pool (datamined)
Source: sparkingzerometa.com character profiles + JP atwiki "耐久" (durability) column. The datamine stores HP directly.

| Character | HP (datamined) | Notes | Tag |
|---|---|---|---|
| Piccolo (standard reference) | **40,000** | Defense 1000, the "baseline" body | [datamined] |
| Goku (Z – Early) | 40,000 | | [datamined] |
| Goku (Super) Ultra Instinct -Sign- | 41,238 | forms carry slightly higher HP | [datamined] |
| Goku (GT) base | 36,364 | | [datamined] |
| Goku (Kid /少年期) | 31,819 | **flightless character** (飛べないキャラ) | [datamined] |
| Master Roshi | **30,000** | low-HP skirmisher | [datamined] |
| Cell (Perfect) | 40,000 | | [datamined] |
| Gamma 1 | 40,000 | | [datamined] |

- **Most DBZ-roster fighters = 40,000 HP.** GT-era and kid/mini bodies are lower (31k–36k). A handful of forms read slightly above 40k.
- **Health bars:** the HUD shows ~4 segments for a 40,000-HP character → **≈10,000 HP per bar**. Cross-checked by a GameFAQs lab: an SSJ4 Gogeta combo dealing **19,832 damage** was described as "**two full bars of damage**" → ≈9,900/bar. `[community-tested, ~Dec 2024]`
- **`耐久` (durability) = HP × defense correction.** JP wiki notes giants are listed at the 1.0× factor; the displayed durability index already folds defense in.

> ⚠️ A circulating AI research write-up claimed the **Jan 2026 patch "standardized all characters to 6,000 HP."** This is **false** — datamined HP is in the tens of thousands and remains character-specific. What the Jan 2026 notes actually did: removed DP-based damage scaling in single battles and tuned individual characters. See Gaps.

### 1.2 Defense (datamined)
Stored as a **Defense** value (baseline **1000**) plus an **Energy Defense** multiplier (~1.0).

| Character | Defense | Energy Def | Class note | Tag |
|---|---|---|---|---|
| Piccolo / Goku (standard) | 1000 | 1.0 | Normal | [datamined] |
| Vegeta (Z) | 900 | 1.05 | Ki-Blast class (squishier melee, better vs ki) | [datamined] |
| Spopovich | 1100 | — | tankier | [datamined] |
| Android 16 | 1252 | 0.874 | Giant/Power — high melee def, weak vs ki | [datamined] |
| Android 19 | 1138 | 0.931 | Ki-drain Power | [datamined] |

Higher Defense = less melee damage taken; Energy Defense <1 means **extra** ki-blast damage taken (e.g. Android 16 eats more from blasts).

### 1.3 Attack / combo damage (datamined + tested)
sparkingzerometa.com exposes per-character melee numbers:

| Quantity | Standard value | Tag |
|---|---|---|
| **Rush 1st hit** (char-select ATK sort key) | ~**390** | [datamined] |
| **Melee** (full basic string aggregate) | ~**2,275** | [datamined] |
| **Rush 5-hit** | ~**2,460** | [datamined] |
| **Rush 5-hit vs Armor** | ~**2,289** (≈7% less into armor) | [datamined] |
| **Throw damage** | ~**1,250–1,312** | [datamined] |
| Giant stagger threshold | 4–5 | [datamined] |

Higher-tier bodies scale up (e.g. Hit: 1st-hit 508, Rush-5 3,283; Android 16: 468 / 2,952).

### 1.4 Super / Ultimate blast damage (datamined)
Stored as **Base Damage** and **Boosted Damage** (boosted = the Sparking-Mode / in-Sparking value). Examples:

| Move (char) | Slot | Base | Boosted | Energy cost | Tag |
|---|---|---|---|---|---|
| Super Kamehameha (Cell) | Super 1 | 9,080 | 13,660 | 30,000 | [datamined] |
| Barrage Death Beam (Cell) | Super 2 | 7,960 | 9,557 | 20,000 | [datamined] |
| Special Beam Cannon (Piccolo) | Ultimate | 15,000 | 19,638 | 50,000 | [datamined] |
| Perfect Barrier (Cell) | Ultimate | 19,620 | 25,584 | 50,000 | [datamined] |
| Gamma Shift Shot (Gamma 1) | Ultimate | 17,250 | 22,425 | 50,000 | [datamined] |

- **Boost multiplier ≈ ×1.2 to ×1.5** depending on move (e.g. Super Kamehameha 9,080→13,660 ≈ ×1.50; most ultimates ≈ ×1.30). The "Boosted" value applies in Sparking! Mode / "In Sparking! Mode"-flagged ultimates.
- **Ultimates universally cost 50,000 energy** (= roughly a full max-ish gauge, see §2). Supers cost 20,000–40,000.

### 1.5 Combo damage scaling (community-tested)
- **Diminishing returns is real and aggressive.** Each additional hit in a rush chain returns less; a raw Ultimate frequently out-damages a long-combo→Ultimate because the combo's scaling carries into the finisher. `[community-tested, Dec 2024]`
  - Lab example: Kid Gohan **raw ultimate = 17,388**; a 60+ hit combo into the same ultimate dropped the **whole sequence** to ~13–15k. SSJ4 Gogeta: raw ult 19,950 vs 70-hit combo→ult 19,250. Long combos can net *less* total. `[community-tested]`
- **Optimal damage = short combos with high-ATK chars.** GameFAQs reference combo: SSJ4 Gogeta `□×5 → Step-in+Down+△ → Up+△ → □ → Rush Super = 19,832` (≈2 health bars) unboosted. `[community-tested]`
- **Sparking! Mode rush attacks** had their "gradual damage reduction of consecutive hits **increased**" (i.e. scaling got *harsher* inside Sparking) — `[official, Dec 2024 patch]`.
- **May 25-26 2026:** reduced damage of Blasts/Ultimate Blasts *when hit during a combo*, reduced consecutive-Blast damage, **but eased** the scaling on Ultimate Blasts hitting mid-combo (partial walk-back). `[official]`

### 1.6 Rush Chain (official)
- Rush Chain = `□ (×1–4 max) + △`. Longer chain = more damage but more escape windows for the opponent and **more skill-stock recovery granted to the victim when hit from behind**. `[official]/[community-tested]`

---

## 2. Ki System

### 2.1 Gauge structure
| Quantity | Value | Tag | Patch |
|---|---|---|---|
| Ki bars | **5** | [official] | current |
| Ki blast cost | **16–22% of a bar per shot** (Normal class 20%; Ki-Blast class 16%; some 22%) | [datamined] | current |
| Ki blast cap (queued shots) | char-specific (e.g. 3–8; Ki-blast androids/Gamma effectively 999) | [datamined] | current |
| Ki charge speed (manual, R2) | ~**1.4 / sec** (Roshi 1.47, Vegeta 1.54, Cell 1.32) | [datamined] | current |
| Passive ki gain (on hit) | small, "slightly charges when you land hand-to-hand combos" | [official] | current |
| **Ki-exhaustion (red bar)** | when bar goes red you **cannot move** until it recovers | [official] | current |

**Energy-vs-bar relationship (inferred):** datamined blast costs are in "energy" (Super 30,000; Ultimate 50,000) while ki-blast cost is given as "% of a bar." A full 5-bar gauge appears to map to roughly the 50,000-energy scale that an Ultimate consumes (i.e. an Ultimate ≈ a full/near-full gauge). **This bar↔energy conversion is not officially published — treat as inferred.** `[community-inferred]`

### 2.2 Movement & action ki costs
| Action | Ki cost | Tag | Patch |
|---|---|---|---|
| **Z-Burst Dash** (around-opponent fast dash) | **0.75 ki** (non-giant); **2.0 bars** (giant) | [community-tested]/[official: "reduced"] | Jan 20 2025 |
| **High-Speed Dragon Dash** | "significantly reduced"; ~**50% faster than Z-Burst** | [official] | Jan 20 2025 |
| **Short (Burst) Dash** | **0 ki**; can chain consecutively | [community/official] | Jan 20 2025 |
| **Z-Burst Dash (post-May 2026)** | **lower initial cost; now scales with travel distance** (short hop cheap, full-screen expensive) | [official] | May 25 2026 |
| **Rapid Ascend / Descend** | **increased** ki cost (no longer a free escape) | [official] | May 25 2026 |
| **Vanishing Assault** | small; reduced 16.5% by the "Dragon Assault" item (implies modest base) | [datamined item] | current |
| **Blast Attacks / Ki Blasts** | drain the ki gauge per §2.1 | [official] | current |

> Pre-Jan-2025 baseline (for the historians): a widely-repeated community figure put **Dragon Dash at ~2.5 ki bars** and the original **Z-Burst at ~2 bars**; the Jan 20 2025 patch cut non-giant Z-Burst to 0.75 and made short dashes free. `[community-claim, launch–Jan 2025]`

### 2.3 Class ki quirks (datamined)
- **Infinite-Ki Androids (16, 17, 18, Super 17):** **Ki Charge Speed = 0** — they *cannot manually charge ki* but have effectively unlimited ki blasts (cost still 16–22%/bar, but the bar refills via the android mechanic). They start with **+1 skill stock**. `[datamined]`
- **Ki-Drain Androids (19, Dr. Gero):** Ki Charge Speed 0, **start with +2 skill stock**, and have **huge throw damage** (3,594 / 3,875) reflecting their absorb-on-grab identity. Super Absorption vs a beam now triggers Sparking! Mode (buff removed). `[datamined]/[official Jun 2025]`

---

## 3. Defensive Systems (input windows)

> No official frame data exists. All windows below are **community-tested** and the game runs at **60 fps (1 frame ≈ 16.7 ms)**. PC builds <60 fps and online latency materially change effective windows.

### 3.1 Super Counter (↑ + □ to reverse a melee combo)
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Input window | **~2 frames** (≈33 ms); some top players argue ~4f offline | [community-tested] | current |
| Re-attempt lockout | **"time between inputs increased after a failed attempt"** (~ up to ~1 s felt; ~12f cooldown claimed) | [official: increased]/[community] | Jan 20 2025 |
| Ki recovery during SC | **removed** (ki no longer auto-recovers during Super Counter) | [official] | ~May 2026 |
| Consecutive use | "becomes more difficult if performed consecutively (like Z-Counter)" | [official] | Jan 20 2025 |
| Loses to | mistimed = whiff/reset; slower/"tanky" chars are *harder* to SC (timing shifts late) | [community-tested] | current |

- Best-practice (community): **counter the *second* hit / the launcher**, not the first; hold ↑ then tap □ a frame later, or press both simultaneously. `[community-tested]`
- A datamine/cheat-engine teardown located the SC success check at `SparkingZERO-Win64-Shipping.exe+235EC4D` (input id `0x16`), confirming it's a single discrete success/fail gate (consistent with a tiny window). `[datamined]`

### 3.2 Perception / Super Perception (hold ○/B)
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Cost vs melee | **ki only** (no skill cost) | [official] | current |
| Cost vs blasts (e.g. Kamehameha) | **2 Skill Count** | [official] | launch → |
| Ki on activation | now **consumes ki on activation** (didn't at launch) | [official] | Jan 20 2025 |
| Recovery after move | "time until next action **increased**" | [official] | Jan 20 2025 |
| **May 2026 rework** | cannot be used during **guard stun**; **ki cost up**; **Skill Stock for Smash/Rush-Chain follow-up raised 1 → 2**; follow-up window **wider**; follow-ups **chargeable** | [official] | May 25 2026 |
| **Super Perception** | buff **stronger + longer**; small **ki recovery on blast deflect** | [official] | May 25 2026 |
| Vs Afterimage Strike | Perception **cancels** an active Afterimage Strike | [official] | Dec 2024 |
| Sonic Sway | triggered by **frame-perfect Super Perception vs a Rush** → dodge + counter + drains opponent ki | [official] | current |

### 3.3 Z-Counter / Vanishing Wars (R1 before opponent's Vanishing Assault lands)
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Cost per vanish | **~0.5 ki bars** (post-patch); **~0.25/bar at launch** | [community-tested] | Jan 20 2025 |
| Skill stock gained per vanish | **~15% of a skill gauge** | [community-tested] | current |
| Escalation | each subsequent vanish is **faster and costs more ki** | [official] | Jan 20 2025 |
| QTE / impact trigger | after **4 consecutive vanishes** a QTE/Impact clash occurs | [official] | Jan 20 2025 |
| Skill gain from vanish wars | **reduced** ("you gain fewer skill stocks from vanish wars") | [official] | Jan 20 2025 |
| Damage | "the longer the exchange, the greater the return-counter damage" | [official] | current |
| Outcome rule | whoever has **more ki wins** the chain; advice = bail early if you have less ki | [community-tested] | current |
| Dec 2024 | Z-Counter **input window shortened**; harder when consecutive | [official] | Dec 2024 |

### 3.4 Revenge Counter (R3 / right-stick press)
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Cost | **2 Skill Count** (some launch guides said 1) | [official]/[community] | current |
| Use | breaks a combo from any direction, even while being hit; "last-ditch get-off-me" | [official] | current |
| Counter-the-counter | **Super Z-Counter** (countering a Revenge Counter) skill cost can be reduced by 1 via "The Secret to Counters" item (min 1) | [datamined item] | current |

### 3.5 Guard
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Chip damage | guards take chip; **"Perfect Guard" item = no chip** while blocking, **"Guard Master" item = unbreakable** (implies guards *are* breakable + *do* chip by default) | [datamined items] | current |
| Guard-break ki damage | base 1 ki bar of damage; **"Mind Breaker" item makes it 1.5 bars (+50%)** | [datamined item] | current |
| May 2026 | Guard-break inconsistencies fixed; Perception unusable during guard stun | [official] | May 25 2026 |

---

## 4. Skill (Skill-Stock) System

### 4.1 Stock economy
| Metric | Value | Tag | Patch |
|---|---|---|---|
| Max skill stock | **char-specific**, typically **4–5** (Cell/Piccolo 5; many 4; Yajirobe raised 5→6) | [datamined] | current |
| Skill regen | **~4.2 stock / minute** standard (≈**1 stock / ~14 s**); Roshi 5.46 | [datamined] | current |
| "Dragon Spirit" item | regen 14 s → **11.5 s** (−18%) | [datamined item] | current |
| Starting stock | usually **0**; Androids start +1, Ki-drain Androids +2; "Secret Measures" item +1 | [datamined] | current |
| Low-HP bonus regen | skill counts rise faster at low HP — **now only below the LAST health bar** (was earlier) | [official] | Sep 2025 / Jan 2026 |
| May 2026 | auto-recovery speed **slightly reduced**; no longer recovers on a successful tech; **increased** recovery on a successful Attack Break | [official] | May 25 2026 |

### 4.2 Skill costs (per use)
| Skill | Cost (stock) | Effect / numbers | Tag | Patch |
|---|---|---|---|---|
| **Afterimage Strike** | **3** | auto-dodge **every melee attack** for **10 s** | [datamined]/[official] | current |
| **Wild Sense** | **2** | permanent **1-hit** auto-dodge+counter (consumes on trigger); dmg **reduced** Jan 2025 | [official IGN] | current |
| **Revenge Counter** | **2** | see §3.4 | [official] | current |
| **Super Perception vs blast** | **2** | see §3.2 | [official] | current |
| **Senzu Bean** (Yajirobe) | **5** (→**6** for buffed Yajirobe) | **FULL** health restore | [datamined]/[official] | current |
| **Instant Sparking** | **4** (launch **3**) | instantly enter Sparking! Mode | [official] | Jan 20 2025 → |
| **Explosive Wave** | **2** *and* **3-cost** variants exist | AoE knockback / ki clear | [community: TheGamer] | current |
| **Kaioken** (Goku Z-Early) | **reduced** cost | — | [official] | Jan 20 2025 |
| **Transformation** (one tier, e.g. base→SSJ) | **~1** | "Super Transformation" item −1 | [community/official] | current |
| **Fusion / Potara (Vegito, Gogeta)** | higher (multi-stock) | no time limit, no damage de-fusion; voluntary revert | [official] | current |
| **Instant Transmission** | skill-stock teleport reposition (cost char-specific) | — | [community] | current |

> **Senzu history:** BT3 cost 5; SZ launch 5. A later DLC patch raised Yajirobe's **max** skill count 5→6 *and* raised **Senzu cost to 6** (and shaved ~½ a health bar), nerfing the infinite-heal loop. `[official/community]`

---

## 5. Sparking! Mode (formerly "Max Power")

### 5.1 Entry & gauge (official)
- Requirement: **ki gauge full** + **≥1 skill count**, then keep charging to fill the **separate Sparking gauge**; spend **1 skill count** to activate. `[official]`
- **Instant Sparking** skills skip the gauge for **4 skill stock** (launch 3). `[official]`

### 5.2 Buffs (official, qualitative)
On entering Sparking! Mode you gain:
- access to your **Ultimate Blast**,
- **ki-free actions** (dashes/blasts cost no ki),
- **immunity to ki-blast stun**,
- damage uses the **"Boosted"** blast values (≈×1.2–1.5, §1.4),
- some chars get extra stat boosts (Kid Gohan, Uub GT). `[official]`

### 5.3 Nerfs / changes
| Change | Tag | Patch |
|---|---|---|
| Sparking! **rush-attack consecutive-hit scaling increased** (long combos punished) | [official] | Dec 2024 |
| Skills that **instantly trigger Sparking! → defense reduced** for a period after activation | [official] | Jun 23 2025 |
| **May 2026:** Sparking! Mode **reduces defense** for a window on activation (you're exposed after popping); same penalty on Full-Ki-Recovery skills | [official] | May 25 2026 |
| **Auto-reflect** now only on **DP ≥ 7** characters during Sparking! Mode | [official] | May 25 2026 |
| Item **"Sparking! Plus" / "Style of the Strong"** = **+3 s** Sparking duration (Plus also −12% defense) | [datamined item] | current |
| Instant Sparking cost **3 → 4** stock | [official] | Jan 20 2025 |

> **Base Sparking! duration in seconds is NOT officially published.** Items add "+3 s," which only tells us the base is finite. An AI write-up's "exactly 15 s / +25% attack / +15% speed" figures are **unverified** — flagged in Gaps.

---

## 6. Transformation / Fusion

| Aspect | Value | Tag |
|---|---|---|
| Cost per transformation tier | **~1 skill stock** per tier (base→SSJ ≈ 1) | [community/official] |
| Fusion / Potara | multi-stock (higher than a single transform) | [community] |
| "Super Transformation" item | −1 stock to transform/fuse (min 1) | [datamined item] |
| HP carryover | persists across transforms; **some forms restore HP on transform** (e.g. Ultimate Gohan SH transform now heals) and some patches **reduced** specific forms' HP (Gohan SH line) | [official Jun 2025] |
| Form stat changes | datamined per-form HP & ATK rise with tier (e.g. Goku Z 40,000/390 → SSJ 40,000/476 → later forms 40,817+/496+) | [datamined] |
| DP cost budget | team cost capped at **15** (transformed forms folded into tiers, BT3-style) | [official] |
| De-fusion | no time limit, no damage-based forced de-fusion; voluntary at any time | [official] |

---

## 7. Character-Class Modifiers

| Class / trait | Modifier | Tag | Patch |
|---|---|---|---|
| **Giant** | Z-Burst costs **2 full bars** (not 0.75); **grab/throw immune** (giant stagger value instead); **May 2026: −rush/smash dmg, +recovery on whiff, +dmg taken from melee, slower back-dash** | [datamined]/[official] | May 25 2026 |
| Giant vs standard charge-blast | standard charge-type Blast now **damages + knocks back** giants (previously whiffed/nullified) | [official] | Jun 2025 / May 2026 |
| **Infinite-Ki Androids** (16,17,18,S17) | **Ki charge speed 0** (no manual charge), unlimited blasts, **+1 starting skill stock** | [datamined] | current |
| **Ki-Drain Androids** (19, Gero) | Ki charge 0, **+2 starting skill stock**, **massive throw dmg** (absorb), Super-Absorb→Sparking | [datamined]/[official] | Jun 2025 |
| **Flightless** (Kid Goku, Mr. Satan/Hercule, Videl, Yajirobe-type) | flagged 飛べないキャラ; lower HP (Kid Goku 31,819); **May 2026: Roshi/Satan/Yajirobe ki-recovery reduced** | [datamined]/[official] | May 25 2026 |
| **Ki-Blast class** | Defense ~900 + Energy Def ~1.05 (weaker melee def, tankier vs ki); 16% ki-blast cost | [datamined] | current |
| **Power class** | high melee Defense (1138–1252), Energy Def <1 (eats more ki-blast dmg) | [datamined] | current |
| Super Armor moves | "Power Body" item gives back-armor, **4–5 Smash/Rush-Chain hits to flinch**, −12% defense | [datamined item] | current |
| Rival class (Hit) | very high ATK (1st-hit 508, Rush-5 3,283), low ki-blast limit | [datamined] | current |

---

## 8. Damage Formula (datamine status)

The files store, per move:
- **Base Damage** and **Boosted Damage** (Boosted = Sparking/in-Sparking value, ≈×1.2–1.5),
- **Max Expend Energy** and **Trigger Expend Energy** (ki energy cost; supers 20–40k, ults 50k),
- **Blast Impact Power** (clash priority 0–5), **Hit Count**, and behavioral flags (`Can Blast Impact`, `Map Destruction`, `Lock-On Needed`, `Impossible Guard`, `Target Giant`, etc.).

Per-character: **HP**, **Melee/Rush** damage values, **Defense** + **Energy Defense** multiplier, **Throw Damage**, **Ki charge speed**, **Ki blast cost %**, **Skill regen**, **Max skill stock**.

**Inferred effective formula:** `damage_taken ≈ attacker_move_value × (Sparking? boosted) × scaling(combo) × defender_defense_factor (melee vs energy)` minus combo proration (§1.5). The exact defense divisor and the combo-scaling curve are **not published as a clean equation** — only the input tables are datamined. `[datamined tables; formula community-inferred]`

DP-based damage scaling (higher-DP attacker hitting lower-DP defender) **existed at launch in single-player** but was **removed from single battles in all modes** in the Jan 2026 patch. The "Big Impact" item still adds DP-difference damage **in DP Battles only** (+500 at 1 DP diff, +250 per extra DP). `[official]/[datamined item]`

---

## 9. Stage Interactions

| Aspect | Value | Tag |
|---|---|---|
| Smash-into-wall / ground | wall/ground slams add follow-up damage; "Chase" attacks continue the slam combo | [official] (qualitative) |
| Stage destruction | maps have destructible terrain (`Map Destruction` flag on some blasts); World-Tournament stages force **evacuation** (`World Tournament Evacuation` flag) for ring-out-style ultimates | [datamined flags] |
| Stage-locked item buffs | "Power of Namek/Earth/Universe" items = **+2% all damage** on their matching maps (Namek doesn't apply on Destroyed Namek; Earth excludes City Ruins & Hyperbolic Time Chamber) — implies discrete map IDs | [datamined items] |
| In-water recovery | "Water's Blessing" item = recover 1 HP bar per 1m40s **while in water** (water stages exist as a state) | [datamined item] |
| Stage size / dimensions | **not datamined publicly**; maps vary in size but no measured arena dimensions found | — (gap) |
| Persistent destruction 2.0 | leaked for the rumored "NEO Limit Break" summer-2026 expansion (craters persist) — **unverified leak** | [community-leak] |

---

## Gaps / Unverified

**Numbers nobody has cleanly measured / that conflict between sources:**

1. **Base Sparking! Mode duration (seconds).** Not in official notes or the datamine wiki page. Items add "+3 s" but the base is unconfirmed. The AI-sourced "15 s, +25% attack, +15% move speed, +30% special, 1.25× combo" set is **unverified/likely fabricated** — do not cite as fact.
2. **Exact Super Counter window in frames per patch.** Community consensus = **~2f**; a credible **4f** camp exists; no datamined frame value surfaced. There is **no evidence** of a documented "6f→4f→2f" progression — the only *official* change is "time between inputs after a failed attempt increased" (Jan 2025) + "no ki recovery during SC" (~May 2026). The "6f at launch" figure in the brief is **not supported**.
3. **Bar ↔ energy conversion.** Whether 5 ki bars == 50,000 energy (so an Ultimate = exactly one full gauge) is **inferred**, not confirmed. Ki-blast cost is given as "% of bar," blast cost as raw energy; the bridge is unverified.
4. **Precise ki cost of a single vanish / Dragon Dash in current build.** "~0.25→0.5 ki per vanish" and "Dragon Dash ~2.5 bars" are **community-tested on older patches** (≤ Jan 2025). The **May 25 2026** patch made Z-Burst **distance-scaled** and changed Rapid Ascend/Descend costs, so any fixed pre-2026 ki number for dashes is **likely stale**.
5. **Revenge Counter cost (1 vs 2).** Official text says "consumes a Skill Count" (singular); community widely reports **2**. Likely 2 in current build but the "1" wording persists in older guides — needs a current-patch lab confirm.
6. **Combo-scaling curve as an equation.** Only the *behavior* is known (long combos lose damage; Sparking scaling is harsher; raw ults can beat combo→ult). The per-hit proration coefficients are **not published**.
7. **Jan 2026 "all characters same HP" claim is FALSE.** Datamine shows HP stays 30k–41k and character-specific. The real Jan 2026 changes: removed DP damage-scaling in single battles + per-character tuning + UI fixes. Flagging because an AI research pass asserted a flat 6,000 HP — **do not propagate**.
8. **Afterimage Strike "single dodge" claim is FALSE.** Both the datamine wiki and official text say it dodges **every melee attack for 10 s** (then ends on Perception, or — since Jun 2025 — if hit by a Super Counter, or — May 2026 — it can be made to whiff vs Rush Chain / unblockable charge blasts). The "1 dodge per activation" figure circulating in AI summaries is wrong.
9. **Stage dimensions / sizes.** No measured arena sizes found; only map-ID-implied item behavior.
10. **Exact frame cooldowns** (Super Counter "~12f", Perception recovery, Afterimage internal cooldown) are **community estimates**, not datamined.
11. **sparkingzerometa.com staleness.** The site itself notes "Site reflects current patch" but also "we're still working on updates / life happened" — some item % and stat values may lag the May 2026 patch. The big structural facts (HP, class behavior, blast energy) are stable; fine-grained %s may be a patch or two behind.

**Reliability ranking of the source pool:** datamine wikis (sparkingzerometa, sparking0data, JP atwiki) > official Bandai patch notes (but qualitative) > top-player Steam/GameFAQs/Reddit testing > general guide sites (Game8/IGN/TheGamer, good for *which* mechanic but loose on numbers) >> AI-generated research summaries (several fabricated precise values — verify everything).
