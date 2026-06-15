---
slug: "ki-and-charging"
name: "Ki & Charging"
category: "resource"
input: "Hold Charge (R2/RT) to manually refill the ki gauge; landing hits grants a small passive gain"
values:
  - label: "Energy per ki bar"
    value: "10,000 energy = 1 bar"
    patch: "current"
    tag: "datamined"
  - label: "Ki gauge size"
    value: "5 bars (50,000 energy full)"
    patch: "current"
    tag: "official"
  - label: "Manual charge speed"
    value: "~1.3 bars/sec (community lab); datamined kiChargeSpeed index = 6/7/8 (Cell 6, most 7, some 8)"
    patch: "current"
    tag: "community"
  - label: "Ki blast cost"
    value: "16–22% of one bar per shot (Normal class ~20%, Ki-Blast class ~16%)"
    patch: "current"
    tag: "datamined"
  - label: "Androids manual charge"
    value: "0 (cannot manually charge ki)"
    patch: "current"
    tag: "datamined"
  - label: "Android starting skill stocks"
    value: "+1 (all androids; Android 19 & Dr. Gero = 1, not +2)"
    patch: "current"
    tag: "datamined"
  - label: "Ki-exhaustion (red bar)"
    value: "cannot move until it recovers"
    patch: "current"
    tag: "official"
counters:
  - "Refills the resource that powers blasts, dashes, vanishes, Sparking"
  - "Passive gain on landing hand-to-hand hits"
counteredBy:
  - "Pressure (no time to charge)"
  - "Ki-exhaustion lock (red bar = frozen)"
  - "Charging is interruptible"
summary: "Ki is the universal action currency — 5 bars, 10,000 energy each (50,000 full). You refill it by holding Charge (R2) at ~1.3/sec standard, or passively by landing melee. Ki blasts cost 16–22% of a bar; a full gauge maps to the ~50,000-energy scale an Ultimate consumes. Androids CANNOT manually charge (charge speed 0) but get unlimited blasts and start with +1 skill stock to compensate. A fully depleted (red) bar freezes you until it recovers."
changeHistory:
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "General melee ki recovery on hit increased; first ki gauge auto-recovery speed increased."
  - version: "Ver.2014.013.003.009.008 (Sep 22, 2025)"
    date: "2025-09-22"
    change: "Quick Ascent/Descent ki cost increased; Ki Blast Deflect → Smash made fast."
  - version: "Patch (Jan 26, 2026)"
    date: "2026-01-26"
    change: "Action lock during ki depletion — certain counter actions disabled while out of ki; mash-UI now shows correctly. Rush Ki Wave reduces opponent's ki when guarded."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Rapid Ascend/Descend ki cost increased; Z-Burst Dash initial ki cost reduced then scaled by distance; rapid-fire Ki Blast damage increased."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "data-mined/system_constants.json (kiChargeSpeedDistribution 6/7/8, ki-blast %, android charge 0; 10,000/bar datamine-inferred)"
  - "community (sparkingzerometa.com): ~1.3 bars/sec charge conversion"
  - "research/04-mechanics-frame-data.md (§2 Ki System; §2.3 class ki quirks)"
  - "research/03-patches-balance.md (Apr 21 2025; Sep 22 2025; Jan 26 2026; May 26 2026)"
  - "Bandai Namco official patch notes (Apr 21, 2025; Sep 22, 2025; Jan 26, 2026; May 26, 2026)"
---
Ki is the universal action currency. It powers ki blasts, [[vanish-z-counter|Vanish]], dashes ([[z-burst-dash|Z-Burst]], [[dragon-dash|Dragon Dash]]), and entry into [[sparking-mode|Sparking! Mode]]. You refill it by **holding Charge (R2/RT)** or passively by landing hand-to-hand hits.

## The numbers

- **Energy per bar: 10,000.** The gauge holds **5 bars**, so a full gauge is **50,000 energy** — which is exactly the scale a 50,000-energy **Ultimate** consumes, i.e. an Ultimate costs roughly a **full gauge**. (Supers cost 20,000–40,000, i.e. 2–4 bars.) See [[health-and-damage|health & damage]] for blast costs.
- **Manual charge speed: ~1.3 bars/sec** standard — a **community** conversion, not in our files. The datamined per-character figure is an index (`kiChargeSpeed` = **6 / 7 / 8**: Cell **6**, most fighters **7**, some **8**; androids **0**); higher = faster refill.
- **Ki blast cost: 16–22% of one bar** per shot — Normal class ~**20%**, Ki-Blast class ~**16%**, some at **22%**.
- **Ki-exhaustion:** when a bar goes **red** you **cannot move** until it recovers. The Jan 26, 2026 patch added an explicit **action lock** during ki depletion (certain counters disabled while out of ki).

## Androids can't charge

- **[[android-class|Androids]] have a manual charge speed of 0** — they **cannot** hold R2 to refill ki. Instead they get effectively **unlimited ki blasts** (the bar refills via the android mechanic) and **start the match with +1 skill stock** — including the ki-drain pair [[android-19|Android 19]] and [[dr-gero|Dr. Gero]], whose datamined `initialSkillStock` is **1** (**not +2**). The ki-drain pair also have huge throw damage from their absorb-on-grab identity.

## Charging-related patch drift

- **Apr 21, 2025** increased melee ki recovery on hit and sped up first-bar auto-recovery.
- **Sep 22, 2025** raised Quick Ascent/Descent ki cost.
- **May 26, 2026** raised Rapid Ascend/Descend cost again, made [[z-burst-dash|Z-Burst Dash]] cheaper to start but distance-scaled, and **increased rapid-fire ki-blast damage**.

> The **bar ↔ energy** bridge (5 bars = 50,000 energy) is **datamine-inferred**, not officially published — ki-blast cost is stated as "% of a bar" while blast cost is stored as raw energy. The 10,000/bar figure is the consistent reconciliation but is **not a confirmed official conversion**.
