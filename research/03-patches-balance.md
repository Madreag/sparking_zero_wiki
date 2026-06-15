---
title: "DRAGON BALL: Sparking! ZERO — Complete Patch & Balance History (Launch → June 2026)"
date: 2026-06-10
confidence: medium-high
notes: >
  Official Bandai Namco patch notes describe nearly all balance changes QUALITATIVELY
  ("damage reduced", "Ki consumption increased"). Bandai almost never publishes raw
  damage/frame numbers. Where exact numbers exist they come either from the official note
  itself (skill-count / health / multiplier / duration values — tagged [official]) or from
  community datamining/testing (frame data, gauge costs — tagged [community-measured]).
  A widely-circulated AI-generated "version history" inventing precise frame data and fake
  version strings (e.g. "Ver.2014.013.003.009.008 = Feb 2026") was cross-checked against
  primary sources and DISCARDED where it conflicted. Version strings below are only those
  printed on official Bandai pages.
sources:
  - https://store.steampowered.com/news/app/1790600 (Steam news hub / ISteamNews API — authoritative date list)
  - https://en.bandainamcoent.eu/dragon-ball/dragon-ball-sparking-zero/news (EU official patch-notes hub)
  - https://www.bandainamcoent.com/news/ (US official patch notes)
  - https://www.eventhubs.com/news/2024/dec/11/dragon-ball-sparking-zero-patch/ (Dec 2024 full notes mirror)
  - https://games.gg/dragon-ball-sparking-zero/guides/.../complete-dlc-and-update-guide/ (DLC timeline)
  - dbzsparkingzero.fandom.com, game8.co, reddit.com/r/SparkingZero (community-measured numbers + meta consensus)
  - Local Steam manifest D:\SteamLibrary\steamapps\appmanifest_1790600.acf (installed build)
---

# DRAGON BALL: Sparking! ZERO — Complete Patch & Balance History

**Installed build (this machine):** Steam buildid `22517964`, depot manifest `4296220909017956466`, `lastupdated` = **2026-06-05 21:52 UTC**. This corresponds to the **May 26, 2026 free update** as the last gameplay/content patch (no newer balance patch shipped before June 10, 2026). Bandai did not publish a PS5/Xbox/PC long-form version string for May 26; the Switch strings are `2A013.012.003.009.011` (NS2) / `2013.012.003.009.011` (NS1).

> Numbering note: Console/PC launch was internally `Ver.1.xx`. From the Jan 2025 update onward Bandai prints a long version string of the form `20NN.0NN.003.0NN.0NN` on PS5/Xbox/PC, and `2A0xx…` / `20xx…` for Switch 2 / Switch. The second segment increments by one each major patch, which makes the sequence verifiable.

## Master table

| Version (PS5/Xbox/PC) | Date | Type | Headline |
|---|---|---|---|
| Ver.1.00 (launch) | 2024-10-11 | Launch | Game ships, 182-character base roster, BT3-style mechanics |
| Ver.1.0x hotfix(es) | 2024-10 (Oct 11–18) | Hotfix | Stability / Switch-style visual + matchmaking fixes; no balance |
| (Free Update) | 2024-12-11 | **Balance** | First real balance pass: Afterimage Strike 15s→10s, Android 19/Dr. Gero ascend-stall nerf, giant Z-Burst tackle guardable |
| Ver.2008.007.003.005.004 | 2025-01-20 | Balance + content prep | DLC1 system patch: Perception costs Ki, Super Counter input gap up, Wild Sense damage down; Legendary Warrior Face-Off mode |
| (DLC 1) | 2025-01-23/24 | Content | "Hero of Justice Pack" — 11 Super Hero fighters |
| Ver.2009.008.003.006.005 | 2025-03-04 | Minor balance | Legendary Warrior Face-Off rebalance; Orange Piccolo transform heal fix |
| Ver.2011.010.003.007.006 | 2025-04-21 | **Major balance** | Perception skill-count 1→2, giant nerfs, Ki/Blast economy overhaul |
| (DLC 2) | 2025-04-24 | Content | "DAIMA Character Pack 1" — 8 mini-DAIMA fighters |
| Ver.2013.012.003.008.007 | 2025-06-23 | **Major balance** | Removed DP-based damage scaling, equalized all HP, ranked seasons + win-streak multipliers, Gohan Beast nerf |
| (Shallot DLC) | 2025-06-27 | Content | Shallot (DRAGON BALL LEGENDS) standalone fighter |
| Ver.2014.013.003.009.008 | 2025-09-22 | **Major balance** | Transform-heal removed, transform = permanent ATK buff, Super Counter no Ki regen, First Demon World stage |
| (DLC 3) | 2025-09-25 (EA 09-21) | Content | "DAIMA Character Pack 2" — 6 fighters |
| (NS/NS2 launch) | 2025-11-14 | Platform | Switch & Switch 2 release; visual-enhancement data patch |
| Ver. (Dec patch) | 2025-12-15 | Minor / bugfix | Motion-control tuning, giant Burst Smash close-range fix, skill-description fixes |
| Ver. (Jan patch) | 2026-01-26 | Balance + content | Mission 100 + "Ultra" CPU; Ki-economy tuning, Cell Max Max Bomb unblockable |
| NS2 2A013.012.003.009.011 | 2026-02-19 | Content (Switch) | Extreme Warrior Time Attack mode; all-stages in Battle Together (Switch/NS2 only) |
| Ver.2019.018.003.011.012 | 2026-04-21 | Minor / content | Survival Mode added; Ultra-difficulty CPU tuning |
| NS2 2A013.012.003.009.011 | 2026-05-26 | **Major balance** | Giant nerf + Perception 1→2 + instant-Sparking defense-down + DP-spread overhaul (cross-platform); First Demon World added on Switch |
| (announced) Super Limit-Breaking NEO | Summer 2026 | Content (future) | Season Pass 2: 30+ fighters, 4 stages, Limit Breaker Journey mode |

---

## Launch — Ver.1.00 (October 11, 2024) — type: launch

- **Roster:** 182 characters at launch (base game). Modes: Episode Battle, Custom Battle, Battle, World Tournament, online Ranked/Player Match. [official/Steam]
- **Core mechanics established** (baseline for everything below): Sparking! Mode (burst), Vanish/Z-Counter (Ki-cost defensive teleport), Super Counter (frame-perfect melee reversal), Revenge Counter (skill-stock reversal), Perception/Super Perception (parry), Afterimage Strike & Wild Sense (auto-dodge Blast 1 skills), Skill Count/Stock economy.
- **Community-measured baseline numbers** (NOT in official notes):
  - **Afterimage Strike duration: 15 seconds** at launch (Blast 1 skill; dodges all melee, not Ki blasts). [community-measured — Game8] → later cut to 10s (see Dec 2024).
  - **Super Counter: ~12-frame input cooldown** between attempts; window itself frame-tight (community guides cite frame-1 timing). [community-measured — RikudouFox/Reddit] Note: a circulating "15-frame official window" figure is **unverified** — not in any Bandai note.
  - Vanish/Z-Counter consumes a fixed chunk of the Ki gauge per use (commonly cited ~1 bar). Exact "25 Ki" figures online are **unverified/community estimates** — treat with caution.
- **Launch meta problems** (drove later patches): Android 19 / Dr. Gero infinite ascend/descend stall; giant characters (Great Ape Vegeta, etc.) over-tanky and over-damaging; Afterimage Strike / Wild Sense auto-dodge degeneracy; DP-based damage scaling making high-DP single characters dominant. [community consensus]

## October 2024 hotfix(es) — type: hotfix

- Launch-week updates addressed **online matchmaking/stability and visual issues**; Bandai's only explicit public wording is a Switch "first update" to improve visuals (later, for the 2025 Switch release). **No gameplay/balance changes.** A discrete "v1.0.1.0" changelog is **not published** by Bandai (community label only). [official — sparse; confidence low on exact versioning]

---

## December 11, 2024 — Free Update — type: BALANCE (first real balance patch)
Source: official Bandai EU note; full text mirrored at EventHubs (Dec 11 2024).

**System / mechanic changes**
- **Z-Counter (Vanish counter):** input window **shortened**; becomes **harder to perform when used consecutively**; **Ki consumed on success increased**; **Skill Count gain on success reduced**. [official, qualitative] — net: defensive vanish-spam nerf.
- **Revenge Counter:** Skill Count consumed when using **Perception against** a Revenge Counter **reduced 2 → 1**. [official, exact]
- **Z-Burst Dash:** Ki cost on activation **increased**. **Giant characters' Z-Burst tackle is now guardable.** [official]
- **Burst Smash:** no longer costs Ki on activation; instead consumes Ki **by distance travelled**. [official]
- **Rush Attacks in Sparking! Mode:** gradual consecutive-hit **damage scaling increased** (combos do less). [official]
- **Character Switch:** standby-character **health-recovery rate reduced**. [official]
- New action added: **High-Speed Dragon Dash** (hold R2+✕ / RT+A). [official]

**Skill changes (with numbers)**
- **Afterimage Strike:** duration **reduced 15s → 10 seconds**; now **ends if opponent lands a Perception** on you. [official exact — headline nerf; fandom confirms current 10s]
- **False Courage:** Skill Count cost **increased 1 → 2**. [official exact]
- **"All I Need Is Five Seconds!":** Skill Count cost **3 → 2** and activation stat boost increased. [official exact]

**Character changes**
- **Android 19 / Dr. Gero:** Dragon Dash, Quick Ascend, Quick Descend **now consume Ki** (kills the infinite ascend/descend stall); throw HP/Ki absorption adjusted. [official — directly aimed at the tournament-DQ stall exploit]
- **Great Ape Vegeta / Dr. Wheelo:** **maximum health reduced.** [official]
- **Giant characters (general):** Smash Attack **charge time increased and power reduced.** [official]
- **Cooler:** transform HP restore **increased** (buff). **Cell 2nd Form:** throw now escapable.

**Blast changes:** long-range Blasts/Ultimates **speed reduced**; Super Vegito Final Kamehameha Ki cost & damage up; Mr. Satan Present Bomb ending lag up.

**Meta impact:** Killed the Android 19/Dr. Gero stall (the exploit that got two finalists DQ'd in Nov 2024). Afterimage Strike 15s→10s + Perception-cancel was the first dent in AIS dominance, but AIS/Wild Sense remained top-tier. Giant nerf was mild. [community consensus]

---

## January 20, 2025 — Ver.2008.007.003.005.004 — type: balance + DLC1 system prep
Source: official Bandai EU ("Changes and Adjustments to Features and Battle Systems").

**Battle system**
- **Perception / Super Perception:** now **consume a set amount of Ki on activation**; **recovery time after the move increased**. [official] — first Perception nerf.
- **Super Counter:** **time before you can input again after a FAILED attempt increased** (whiff punish window widened). [official]
- **Speed Impact:** re-input timing after the move pushed **later**.
- **Chase Change:** damage from **Giant characters reduced** when chase-changing into them. [official]
- **Rush Ki Blast:** can no longer High-Speed Evade while being hit. **Smash Ki Blast:** easier to get hit if fired while moving. **Charge Attacks:** no recoil while charging when hit by Rush Attack/Ki Blast in Sparking! Mode.

**Skills**
- **Wild Sense:** **attack damage reduced.** [official, qualitative]
- **All auto-avoidance skills (Wild Sense etc.):** opponent can **no longer use them when continuing a combo with a Rush-In.** [official] — big anti-AIS/Wild Sense change.
- **Kaioken:** Skill Count cost reduced (Goku Z-Early only). **Ta-dah!:** Skill Count cost reduced. **All I Need Is Five Seconds!:** Ki now fully recovered.

**Modes/content:** **Legendary Warrior Face-Off** (limited-time boss mode) added; Quick Match reworked to instant-match; ranked disconnect penalty wait-time added; training "Guarding After Attacks" option.

**Meta impact:** Began the multi-patch campaign to tame auto-dodge skills and Perception. Paved the way for DLC1. [community consensus]

## January 23–24, 2025 — DLC 1 "Hero of Justice Pack" — type: content
- **11 playable fighters** from *Dragon Ball Super: SUPER HERO* + early DAIMA: Gohan (Super Hero), Gohan (Super Hero) SSJ, Ultimate Gohan (Super Hero), **Gohan Beast**, Piccolo (Super Hero), Piccolo (Super Hero) Power Awakening, **Orange Piccolo**, Orange Piccolo Giant Form, **Gamma 1**, **Gamma 2**, **Cell Max**. Plus a costume + 3 bonus battles. [official Steam DLC page]
- **Meta:** Gohan Beast arrived strong but community consensus: "right amount of broken to fight top tiers, not enough to shift the meta." UI Goku / SSJ4 Gogeta / Yajirobe / AIS users stayed dominant. [Reddit r/SparkingZero]

---

## March 4, 2025 — Ver.2009.008.003.006.005 — type: minor balance
Source: official (Steam community / Bandai).
- **Legendary Warrior Face-Off:** fixed Broly (Super) status-reduction bug; "adjusted battle balance." [official]
- **Character:** Piccolo (Super Hero)/Power Awakening → Orange Piccolo, and Orange Piccolo → Giant Form, **first transform of the match now restores HP and Ki.** [official] (buff/fix)
- Performance/UX only otherwise. No roster-wide balance.

---

## April 21, 2025 — Ver.2011.010.003.007.006 — type: MAJOR balance
Source: official patch notes (Steam Community discussion thread, verbatim).

**Battle system — movement & neutral**
- **Short Dash:** **backward Short Dash speed reduced**; recovery after starting Dragon Dash from Short Dash reduced. [official]
- **High-Speed Dragon Dash:** easier Rush-Attack connect; Smash charge time reduced; guarantees you reach opponent's front despite trajectory manipulation. [official]
- **Z-Burst Dash:** **activation Ki cost reduced**, now scales **Ki by distance travelled.** [official]
- **General Melee:** Ki recovery on hit **increased**; less targeting deviation vs Step.
- **Rush-In:** fixed guard being possible between Rush-In and Rush Attacks (defensive nerf).
- **First Ki gauge:** auto-recovery speed **increased**.

**Battle system — defense**
- **Perception:** cannot perform during guard stun; follow-up window increased; **activation Ki cost increased**; **Skill Count requirement raised 1 → 2** to use against Smash Attacks and Rush Chains. [official exact — headline Perception nerf]
- **Super Perception:** deflect buff stronger + longer; slight Ki restore on deflect.
- **Auto-reflect:** only **DP 7+ characters** can activate it during Sparking! Mode. [official]
- **Skills with auto-evasion:** **cancelled if Perception used during activation.** [official] — continued AIS/Wild Sense crackdown.

**Blast / Ki**
- **Rush Ki Blast:** damage reduced + stronger consecutive-hit scaling. **Smash Ki Blast (spread):** damage reduced; UI Goku variants' Smash Ki Blasts now deflectable; unblockable variants cost more Ki + recovery.
- **Blast/Ultimate in combos:** damage reduced; consecutive-Blast damage reduced.
- **Future Trunks (Super) Final Flash:** Ki cost + damage **increased**. **Super Trunks Finish Buster:** damage **increased**. **Whis Symphonic Destruction:** now High-Speed-Evadable.

**Character**
- **Giant characters (general):** Rush & Smash damage **reduced**; whiff recovery **increased**; **damage taken from melee increased**; backward Short Dash slower. [official — biggest giant nerf yet]
- **Master Roshi / Mr. Satan / Yajirobe:** Ki recovery speed **reduced.** [official — Yajirobe was a meta menace]
- **Androids (general):** auto Ki recovery stops during Z-Counter; silhouette hidden with Z-Search off.
- **UI Goku -Sign-/UI Goku:** Smash Ki Blast cooldown **increased.** [official — direct top-tier nerf]
- **Dr. Wheelo:** max Skill Count reduced. **Nappa / Recoome / Spopovich:** **health reduced.**
- **Gogeta (Super) SSGSS:** Smash Ki Blast damage & homing **reduced.** [official — SSGSS Gogeta nerf]

**Meta impact:** Remembered as a **mobility + defense-tool nerf** that slowed neutral and hit the dominant cast (Yajirobe Ki regen, UI Goku zoning, SSGSS Gogeta, giants). Perception 1→2 made reactive parrying much costlier. [community consensus]

## April 24, 2025 — DLC 2 "DAIMA Character Pack 1" — type: content
- **8 fighters:** Goku (Mini) SSJ, Vegeta (Mini), Vegeta (Mini) SSJ, Vegeta (Mini) SSJ2, Vegeta (Mini) SSJ3, Glorio, Panzy, Majin Kuu. + Goku (Mini) technique-changing costume. [official/Nintendo Life]

---

## June 23, 2025 — Ver.2013.012.003.008.007 — type: MAJOR balance (system-defining)
Source: official Bandai US patch note (June 23, 2025), verbatim.

**Fundamental DP / health overhaul**
- **Single Battle: REMOVED damage scaling based on DP** in all modes. [official — huge: ends "high-DP hits harder" era]
- **All characters set to the SAME health** in single battle (online & offline). [official exact-in-spirit]
- **DP Battle:** rebalanced so DP-cost differences between characters are **more pronounced** (Team rules unchanged). [official]

**Ranked system (concrete numbers)**
- Seasonal system with resets. End-of-season demotion: **Z→B1, S→B3, A→B5, B→C5, C→D5, D→D5.** [official exact]
- **Win-streak bonus** (max 5): **2 wins ×1.2, 3 ×1.4, 4 ×1.8, 5 ×2.0.** [official exact]

**Battle system**
- **Skill Counts:** auto-recovery rate slightly reduced; no longer recovers on a successful tech; low-HP bonus only triggers below the **last** health bar; Attack-Break gain increased. [official]
- **Unblockable Smash Ki Blasts:** now **Vanish-evadable**; tracking slightly reduced.
- **Skills that instantly trigger Sparking! Mode** and **full-Ki-recovery skills:** **defense reduced for a period after activation.** [official — recurring theme]
- **Afterimage Strike:** now **ends if opponent lands a Super Counter.** [official — yet another AIS counter added]
- **Buff skills (Saiyan Spirit, Pump Up):** duration increased. **Turles Fruit of the Tree of Might:** bigger boost + Ki recovery.

**Character**
- **Gohan (Super Hero) & SSJ:** health **reduced.** **Gohan→Ultimate Gohan:** Skill Count to transform increased, HP restored on transform. **Ultimate Gohan→Gohan Beast:** Skill Stock to transform **increased.** [official — Gohan Beast access nerf]
- **Dr. Gero:** Super-Absorption vs beam/Ki blast now triggers Sparking! Mode and the stat-boost effect removed. [official]
- BGM: +2 tracks (from DRAGON BALL LEGENDS).

**Meta impact:** The **equalized-HP + no-DP-scaling** change is the single biggest competitive shift — it reset character-vs-character damage math and made many mid-DP picks viable. Gohan Beast got harder to access. [community consensus]

## June 27, 2025 — Shallot (DRAGON BALL LEGENDS) — type: content
- Standalone crossover fighter added (free or separate DLC). [official Steam]

---

## September 22, 2025 — Ver.2014.013.003.009.008 — type: MAJOR balance
Source: official Bandai US patch note (Sept 22, 2025), verbatim. (Shipped alongside DAIMA Pack 2 early access; PS5/Xbox/PC.)

**Transformation overhaul (system-defining)**
- **Characters that healed on transformation NO LONGER heal.** [official]
- **Characters who can transform gain a PERMANENT attack-power buff when transforming via Skill Stock** (removed on revert). [official] — reshapes transform-character value entirely.

**Battle system**
- **Super Counter: Ki no longer auto-recovers during Super Counter.** [official]
- **Short Dash:** second short dash immediately after starting one (once). **Ascent/Descent:** faster at close range. **Quick Ascent/Descent:** Ki cost **increased.**
- **Ultimate Blasts (general):** combo damage-reduction correction eased (Ultimates do a bit more in combos). [official]
- **Ki Blast Deflect → Smash:** now fast. **Perception:** follow-up can be charged by holding.
- **Revenge Counter:** fixed the Perception-vs-Revenge-Counter window being shorter than intended.
- **Paralyzing Smash Ki Blast:** Ki cost up; Revenge Counter usable when hit from front; 2 combo hits now knock away instead of paralyze.
- **General unblockable Rush Blasts:** now evadable with auto-evasion skills (Afterimage etc.).

**Character**
- **Gogeta (Super) SSGSS:** on-the-spot **Smash Ki Blast attack power INCREASED** (partial buff after April nerf). [official]
- **Whis:** "Overture to Destruction" less likely to hit directly above/below.

**Ranked:** minimum **50 points per match regardless of rank-point gap**; top 1–100 player & character ranks get text titles. **Content:** **First Demon World** stage added; option to display battle-area edge.

**Meta impact:** Removing transform-healing + the permanent-ATK-buff model rebalanced the entire "transforming character" archetype (Gohan Beast, SSGSS, UI lines). Super Counter losing Ki regen reduced its defensive value. [community consensus]

## September 25, 2025 (EA Sept 21) — DLC 3 "DAIMA Character Pack 2" — type: content
- **6 fighters:** Goku (Mini) SSJ4, Goku (DAIMA) SSJ4, Vegeta (DAIMA) SSJ3, Majin Duu, Third Eye Gomah, Giant Gomah. [official Bandai US]

---

## November 14, 2025 — Nintendo Switch / Switch 2 launch — type: platform
- Game releases on **Switch & Switch 2** (Standard/Deluxe/Ultimate). A **"Software Update Data Patch"** (announced Nov 7, live Nov 14) upgrades the Switch cartridge for enhanced visuals on Switch 2. No balance changes. [official EU]

## December 15, 2025 — Patch Note — type: minor / bugfix
Source: official Bandai EU (Dec 15, 2025).
- **Options:** Motion-Control play style gets 3-level sliders for "ease of performing/stopping Rush Attacks" and "ease of Smash Attacks." [official]
- **Burst Smash:** fixed failing to hit at close range for **giant characters.** [official bugfix]
- **Great Ape Baby (GT) Rush Attack (Motion Control):** fixed follow-up hits not landing. **Great Ape Vegeta Super Galick Gun:** fixed distance-dependent whiff.
- **Skill descriptions:** fixed mismatches for "Afterimage Strike" and "Wild Sense" (description vs effect). [official — note: text fix, not a balance change]
- No roster damage changes. QoL/stability pass.

---

## January 26, 2026 — Patch Notes (January 2026) — type: balance + content
Source: official Bandai EU (Jan 2026). PS5/Xbox/PC.

**Modes:** "Ultimate Battle" added to main menu (Custom Battle moved inside it); **Mission 100** solo mode; **"Ultra" CPU difficulty** (above Super); Custom Battle max CPU level **→ 21**.

**Battle system**
- **Super Perception:** Ki recovery on deflect **increased.** [official]
- **Rush Ki Wave:** now **reduces opponent's Ki when guarded.** [official]
- **Jump Rush Blast:** Ki consumption **reduced.** **Dash Rush Ki Blast:** Ki consumption reduced for characters firing **7+ shots.** [official]
- **Vanishing Attack:** easier for tall characters to land follow-ups on grounded foes.
- **Action Lock during Ki Depletion:** certain counter actions disabled while out of Ki; mash-UI now shows correctly. [official]

**Skills/Blasts**
- **Solar Flare:** no longer ends when approached via Dragon Dash / Z-Burst Dash. [official]
- **Cell Max: Max Bomb → made UNBLOCKABLE.** [official — notable buff]
- Forward projectile/beam hitbox rear-adjusted; charge/rush Blasts hit-consistency at point-blank fixed; some Z-Search-off Blasts disabled/enabled.

**Other:** shop bulk-purchase; player card win-streak stats.

**Meta impact:** Mostly Ki-economy and consistency tuning; Cell Max Max Bomb unblockable is the standout combat change. [community consensus, light]

## February 19, 2026 — Free Update — type: content (Switch / Switch 2 only)
Source: official Bandai EU. Versions: NS2 `2A013.012.003.009.011`, NS `2013.012.003.009.011`.
- **Extreme Warrior Time Attack** limited-time mode (fight super-buffed enemies). [official]
- **Battle Together:** all stages selectable (only when played on a Switch 2 with the update). [official]
- Custom Battle scenario/cut-in/text additions. Usability/stability. **No PS5/Xbox/PC balance** in this entry (it is the Switch-platform companion patch; aligns with the Feb 20 Switch DLC drop). 

## April 21, 2026 — Patch Note — type: minor / content
Source: official Bandai EU. Version **Ver.2019.018.003.011.012** (PS5/Xbox/PC).
- **Ultimate Battle: Survival Mode** (new single-player) added. [official]
- **Versus:** "Ultra" CPU behavior tuned. [official]
- No roster balance changes listed.

---

## May 26, 2026 — Free Update — type: MAJOR balance (current build)
Source: official Bandai EU "Free Update Notice (25 May 2026)" / US "Free Update Notice (May 26)". Switch strings shown (NS2 `2A013.012.003.009.011`); applies cross-platform. This is the **largest single balance patch in the game's history** and the last one before the June 10, 2026 cutoff. Shipped ahead of the June 27 2026 Switch re-bundle of DAIMA Packs 1&2 + Shallot.

**System-defining**
- **Single Battle: transform characters NO LONGER heal on transform; instead gain a permanent ATK buff via Skill Stock** (removed on revert) — brings all platforms in line / extends the Sept 2025 model. [official]
- **DP Battle:** DP differences between characters made **more pronounced** in all modes; total DP selectable **10/15/20**; settings retained. [official]
- **First Demon World** stage added (to Switch parity). [official]

**Battle system (selected, with direction)**
- **Skill Stock:** auto-recovery speed **slightly reduced.** [official]
- **Z-Burst Dash:** initial Ki cost **reduced**, then Ki by distance. **Rapid Ascend/Descend:** Ki cost **increased.** **High-Speed Dragon Dash:** smoother rush connect, reduced Smash charge time.
- **Perception:** cannot use during guard stun; follow-up window up; **Ki cost up**; **Skill Stock requirement 1 → 2 for Smash Attacks & Rush Chain**; follow-ups chargeable. [official exact — mirrors/locks in the April 2025 Perception nerf cross-platform]
- **Super Counter:** **auto Ki recovery disabled** during it. [official]
- **Super Perception:** buffs stronger + longer; slight Ki on deflect.
- **Rush Ki Blast:** damage **reduced** + stronger consecutive scaling. **Smash Ki Blast (spread):** damage reduced; UI Goku variants deflectable.
- **Blast Attacks:** combo & consecutive-hit damage **reduced**; rapid-fire Ki Blast damage **increased**; standard-vs-giant charge Blasts now deal damage + knockback. **Ultimate Blast:** combo damage-reduction eased.
- **Auto-reflect:** only **DP 7+** in Sparking! Mode. [official]
- **Stun-type Smash Ki Blast:** Ki cost up; Revenge Counter usable from front; double-hit knocks away instead of paralyzing.

**Skills**
- **Buff skills (Saiyan Spirit, Pump Up):** duration **increased.** **Turles Fruit of Tree of Might:** bigger boost + Ki recovery.
- **Skills that instantly trigger Sparking! Mode:** **defense reduced for a period after.** [official — anti-panic-Sparking]
- **Full-Ki-recovery skills:** defense reduced for a period after. **Afterimage Strike:** ends if hit by a **Super Counter.** [official]
- **Dyspo Super Maximum Light Speed Mode:** Ki cost for Short Dash reduced + icon. **Kale Cry of Rage:** activation time up.

**Character (with direction)**
- **Giant characters (general):** rush & smash melee **damage reduced**; whiff recovery **increased**; **damage taken from melee increased**; backward Short Dash slower. [official — the definitive giant nerf, cross-platform]
- **Master Roshi / Mr. Satan / Yajirobe:** Ki recovery **reduced.** [official]
- **Dr. Gero / Android 19:** Super Perception vs beam/projectile now triggers Sparking! Mode, stat-boost removed.
- **UI Goku -Sign- / UI Goku:** Smash Ki Blast cooldown **increased.**
- **Dr. Wheelo:** max Skill Stock reduced. **Nappa / Recoome / Spopovich:** health **reduced.**
- **Gogeta (Super) SSGSS:** Smash Ki Blast damage & homing **reduced**, stationary Smash Ki Blast power **increased.**
- **Future Trunks (Super) Final Flash:** Ki cost + damage up. **Super Trunks Finish Buster:** damage up. **Whis Symphonic Destruction:** High-Speed-Evadable.

**Meta impact:** A sweeping rebalance: locks in giant nerfs, Perception 1→2, instant-Sparking defense-down, and the DP-spread system across all platforms. Targets the long-standing menaces (giants, Yajirobe Ki regen, UI Goku zoning, SSGSS Gogeta, panic-Sparking). [community consensus]

---

## Announced / future content (post-cutoff, for completeness)
- **"Super Limit-Breaking NEO" DLC (Season Pass 2)** — announced Dec 30 2025, dated **Summer 2026**: **30+ new fighters** (Super 17, Bardock SSJ, Champa, Vegeta GT, Grandpa Gohan, Demon King Piccolo, Pikkon, Zangya, King Vegeta, Cheelai, Jaco, Trunks GT, Nuova Shenron, etc.), **4 new stages** (Kami's Palace, Stratosphere/Planet Vegeta…), 20+ customization options, and a new solo mode **"Limit Breaker Journey."** Not yet released as of June 10 2026. [official EU NEO DLC page]
- DAIMA Packs 1&2 + Shallot **Switch/Switch 2 re-release: June 27, 2026.** [official]

---

## The 5 most meta-defining balance changes (quantified where possible)
1. **DP damage-scaling REMOVED + all single-battle HP equalized** (June 23 2025) — reset the entire damage economy; the biggest competitive change. [official]
2. **Afterimage Strike 15s → 10s** + can be cancelled by Perception (Dec 2024), then also by Super Counter (June/Sept 2025/May 2026) — dismantled the #1 launch degeneracy over four patches. [official exact]
3. **Perception Skill-Count cost 1 → 2** for Smash/Rush-Chain + Ki cost on activation (Apr 21 2025, re-locked May 26 2026) — made reactive parrying expensive. [official exact]
4. **Android 19 / Dr. Gero ascend-descend now costs Ki** (Dec 2024) — killed the infinite-stall exploit that caused a tournament double-DQ. [official]
5. **Giant characters: damage down + whiff-recovery up + take more melee damage** (Apr 21 2025 → cross-platform May 26 2026), plus **transform-heal removed → permanent ATK buff** model (Sept 22 2025) — reshaped giants and the entire transform archetype. [official]

---

## Gaps / Unverified
- **Exact frame/Ki/gauge values** (vanish Ki cost, Super Counter window in frames, revenge-counter stock count, sparking-gauge point thresholds, instant-Sparking cost) are **NOT in official notes**. Widely-cited figures ("25 Ki vanish", "15-frame super counter", "400-point sparking gauge", "Revenge Counter 8 stock") are community estimates of varying reliability — treat as community-measured, not official. A 12-frame Super Counter input cooldown is the best-attested community number.
- **PS5/Xbox/PC long version strings** are not published for the Dec 2025, Jan 2026, and May 2026 patches (only Switch strings for some). Console/PC launch "Ver.1.00/1.0x" exact sub-numbers are community labels.
- **An AI-generated "version history"** circulating online invents precise per-move frame data, fake quotes ("analysis of 12,000 ranked matches"), and fabricated version strings, and mis-dates 2024 patches into 2025/2026. It was cross-checked and **rejected** wherever it conflicted with primary sources; none of its invented numbers are used here.
- **DLC exact dates** vary slightly by region/early-access vs full release; dates here use the Steam feed + official Bandai pages. DAIMA Pack 1 = Apr 24 2025; Pack 2 = Sept 25 2025 (EA Sept 21).
- **Sept 22 2025 community meta consensus** is thinner than April 2025's in available sources; the transform-heal/ATK-buff impact is inferred from the official change + general community reaction, not a single definitive tier-shift writeup.
- Per-character exact old→new **damage percentages** are essentially unavailable from any reliable source; Bandai describes them as "increased/reduced." The numeric per-character values in the rejected AI document are fabricated.
