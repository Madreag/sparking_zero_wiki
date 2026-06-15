---
slug: "settings-and-controls"
title: "Settings & Controls — Ranked Setup and Training Recipes (v2.2)"
category: "beginner"
summary: "Control-scheme and settings guide for Sparking! ZERO, current to May 26 2026: Standard vs Classic control comparison (what actually changes), the settings that matter for ranked (camera, HUD/input display, Z-Search, lock-on), the Dec 2025 motion-control 3-level sliders, training-mode setup recipes for labbing defense (CPU recording, Guarding-After-Attacks option, the 10/15/20 DP toggle), and accessibility notes — quantified wherever the game exposes a number."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/03-patches-balance.md (Jan 20 2025 training 'Guarding After Attacks'; Dec 15 2025 motion-control 3-level sliders; Apr 2025 Z-Search-off silhouette)"
  - "research/04-mechanics-frame-data.md §3 (input windows the settings affect: Super Counter ~2f, Perception); §2 (ki); 60fps frame timing"
  - "research/05-meta-pvp-tiers.md §4 (Training/offline 10/15/20 DP toggle, persists)"
  - "content/game-modes/training.md (Battle Training + Free Practice; DP toggle)"
  - "Bandai Namco official patch notes (Jan 20 2025; Dec 15 2025; May 26 2026)"
---

How to configure Sparking! ZERO for ranked, and how to set up [[training|Training]] to lab the mechanics from [[defense-bible|The Defense Bible]] and [[offense-and-pressure|Offense & Pressure]]. Tags: `[official]` (patch notes / in-game options), `[community]` (player consensus — the control *defaults* and most menu layouts are not in patch notes). The game runs at **60 fps** on console (**1 frame ≈ 16.7 ms**); PC builds **below 60 fps materially change** your effective defensive windows `[community]`.

> **Currency note.** Bandai patch notes document *option additions* (motion-control sliders, the DP toggle, training options) but not the full settings menu or the button maps. Scheme details below are **community-documented** from the in-game controller config; where a real number exists (60 fps, the 10/15/20 toggle, the 3-level sliders, CPU level → 21) it is tagged and cited.

## Control scheme comparison: Standard vs Classic

The game ships two button layouts. **What changes is the mapping of the four core combat verbs**, not the moves themselves — every action exists on both schemes.

| Action | Standard scheme | Classic (BT-style) scheme | Notes |
|---|---|---|---|
| **Rush Attack** (basic chain) | □ / X | □ / X | Same core button both schemes `[community]` |
| **Smash Attack** (heavy) | △ / Y | mapped differently (BT3-style heavy) | Classic mirrors old Budokai Tenkaichi muscle memory `[community]` |
| **Ki Blast** | ○ / B (context) | dedicated ki-blast button | Classic separates ki-blast more explicitly `[community]` |
| **Guard / Perception** | hold guard; ○/B read | hold guard | [[perception\|Perception]] = hold guard-read on both `[community]` |
| **Vanish / Z-Counter** | R1 | R1 | [[vanish-z-counter\|Vanish]] timing identical `[community]` |
| **Super Counter** | **↑ + Rush** | **↑ + Rush** | The free ~2f reversal is the **same input on both** `[community]` |
| **Skills / Blast menu** | hold a trigger + face button | hold a trigger + face button | Skill-stock spends are scheme-agnostic |

**Which to pick:**
- **Standard** — the game's intended modern layout; most current guides, combo notations, and the wiki's mechanic pages assume Standard. **Recommended for new players** so notations match `[community]`.
- **Classic** — for **returning Budokai Tenkaichi 3 players** whose muscle memory expects the old heavy/ki mapping. No competitive advantage either way — the **frame data and costs are identical**; only the button *positions* differ `[community]`.

> **The competitively load-bearing inputs are identical across schemes:** Super Counter (**↑ + Rush**, free, ~2f), Vanish (**R1**, ~0.5 ki/vanish), Revenge Counter (**R3**, 2 stocks). Pick the scheme whose *rest position* lets you hit those cleanly — that's the only real decision.

### Motion controls (Switch / Switch 2) — quantified
- The **Dec 15 2025** patch added **3-level sliders** for the Motion-Control play style: **"ease of performing/stopping Rush Attacks"** and **"ease of Smash Attacks"** — **3 settings each** `[official]`.
- Motion control is a casual/accessibility option; for ranked, a **standard controller layout is strongly preferred** for input precision on the ~2f Super Counter `[community]`.

## Ranked settings that actually matter

These are the options worth changing before you queue [[ranked-match|ranked]]. Numbers where the game exposes them.

### Camera & lock-on
- **Lock-on / Z-Search:** keep lock-on **on**; it governs homing and target tracking. **With Z-Search OFF, character silhouettes are hidden** (since Apr 21 2025) `[official]` — useful info to know your opponent can hide approaches if *they* turn it off, but for your own play, **on** gives you the most information.
- **Camera distance/speed:** set to whatever keeps **both fighters and the stage edge visible** — the Sep 22 2025 patch added an option to **display the battle-area edge** `[official]`; enable it so you don't get wall-locked blind.

### HUD & input display
- **Input display:** turn it **on while labbing** (see Training below) to verify your Super Counter / Vanish timing frame-by-eye; many players turn it **off in ranked** to reduce clutter `[community]`.
- **Damage/ki readouts:** keep the **ki gauge (5 bars)** and **skill-stock count** prominent — your entire resource game (the **~half-bar vanish reserve**, the 2-stock Perception/Revenge thresholds) is read off those two meters `[community]`. See [[ki-and-charging|ki & charging]] and [[skill-count|skill count]].

### DP total (where applicable)
- **Offline / Player Match / World Tournament / Training** expose a **10 / 15 / 20 DP** toggle that **persists between matches** since **May 26 2026** `[official]`.
- **Ranked DP queue standard remains 15 DP** `[community]` — practice at **15** to mirror ranked (set Training to 15; see recipes below). See [[dp-system|DP system]] and [[dp-team-value-math|DP team value math]].

## Training-mode setup recipes (for labbing)

[[training|Training]] splits into **Battle Training** (guided tutorials) and **Free Practice** `[official]`. Free Practice is where you lab. Recipes below target the mechanics that decide matches.

### Recipe 1 — Lab Super Counter timing (the ~2f reversal)
1. **Free Practice**, set the **CPU to attack** (rush strings).
2. **Input display ON** to see your ↑+Rush frames.
3. Practice countering the **second hit / launcher**, not the first `[community]` — that's the reliable Super Counter timing.
4. Note: since **May 26 2026**, ki does **not** recover during the attempt and a whiff triggers a **lockout** `[official]` — so practice **reading**, not mashing. See [[super-counter|Super Counter]].

### Recipe 2 — Record a counter / punish (CPU recording)
1. Use the CPU **action-recording / playback** (set the dummy to record a specific string or blast, then loop it).
2. Lab your answer to the recorded sequence: e.g. record a **Vanishing Assault** and drill the **R1 vanish** timing; record a **beam super** and drill **blast Perception (2 stocks)**.
3. This is how you build the per-situation muscle memory from the [[defense-bible|Defense Bible]] decision tree.

### Recipe 3 — Guard-stun / "Guarding After Attacks"
1. The **Jan 20 2025** patch added a training option for **"Guarding After Attacks"** `[official]` — use it to drill **what you can and can't do out of guard stun**.
2. Critical lesson: **Perception is DISABLED during guard stun** (since Apr 21 2025) `[official]` — confirm in the lab that you **cannot** Perception out of blockstun, so you learn to **Super Counter or Revenge Counter** instead.

### Recipe 4 — Combo-vs-raw-ultimate damage check
1. Set the dummy to **no guard / standing**.
2. Compare **a short combo → rush super** against a **raw Ultimate** on the **damage readout** — confirm for *your* character whether the raw ult out-damages the long combo (it often does — see [[offense-and-pressure|Offense & Pressure]] §5; SS4 Gogeta raw ult **19,950** vs 70-hit combo→ult **~19,250**) `[community]`.
3. Find your **highest-value SHORT route** rather than the flashiest long one.

### Recipe 5 — DP & ki-reserve discipline
1. Set Training DP to **15** (matches ranked) `[community]`.
2. Watch the **ki gauge**: practice **stopping your charge at ~half a bar** (vanish reserve) when the CPU approaches, then defending — internalizing the anti-pressure rule from the [[defense-bible|Defense Bible]].

> **Frame-stepping:** the game has **no documented frame-by-frame step / hitbox-viewer** in Training as of the May 26 2026 patch — frame data here is **community-measured via input display + recording**, not an official frame-step tool `[community]`. If you need exact frames, the community method is **record → playback → input-display capture**, accepting ~60fps eyeball precision.

### CPU difficulty ladder (for harder dummies)
- Standard difficulty ladder tops out at **"Ultra"** CPU (added Jan 26 2026, above "Super") `[official]`.
- **Custom Battle** CPU level caps at **21** (raised Jan 26 2026) `[official]` — use a high-level CPU when you want a dummy that actually fights back with counters.

## Accessibility notes

- **Motion controls** with **3-level ease sliders** (Rush/Smash) for players who can't manage full controller inputs (Switch/Switch 2) `[official]`.
- **Classic scheme** eases the transition for Budokai Tenkaichi veterans (muscle-memory accessibility) `[community]`.
- **Input display + CPU recording** let you self-pace mechanic practice at any speed by looping a single situation `[community]`.
- **HUD options** (battle-area edge display since Sep 2025; toggleable input display) reduce visual overload `[official]`/`[community]`.
- **No official remappable-per-button editor is documented** beyond Standard/Classic + motion sliders as of May 26 2026 `[community]` — scheme choice + slider tuning is the available customization surface.

## The one-line setup

> **Standard scheme, lock-on ON, battle-area-edge ON, input-display ON for labbing (off for ranked), Training at 15 DP** — then drill the [[defense-bible|Defense Bible]] situations via CPU recording. The competitively decisive inputs (**↑+Rush** Super Counter, **R1** Vanish, **R3** Revenge Counter) are identical on every scheme, so your settings job is **information clarity**, not finding a hidden advantage.

For what to do once you're in ranked, see [[ranked-climbing-guide|the Ranked Climbing Guide]]; for the mechanics themselves, the [[super-counter|Super Counter]], [[perception|Perception]], and [[vanish-z-counter|Vanish]] pages.
