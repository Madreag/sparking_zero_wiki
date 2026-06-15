---
slug: "android-class"
name: "Android Class"
category: "status"
input: "Passive class trait of android characters (16, 17, 18, Super 17, 19, Dr. Gero)"
values:
  - label: "Manual ki charge speed"
    value: "0 (androids CANNOT manually charge ki)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Ki blasts"
    value: "effectively unlimited (cost still 16–22%/bar; bar refills via android mechanic)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Starting skill stocks (infinite-ki)"
    value: "+1 (Android 16, 17, 18, Super 17)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Starting skill stocks (ki-drain)"
    value: "+2 (Android 19, Dr. Gero)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Ki-drain throw damage"
    value: "~3,594 / 3,875 (Android 19 / Dr. Gero — absorb-on-grab)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Super Absorption vs beam"
    value: "now triggers Sparking! Mode; stat-boost effect removed"
    patch: "Jun 23, 2025; re-locked May 26, 2026"
    tag: "official"
counters:
  - "No charge needed — ki blasts effectively unlimited"
  - "Start with extra skill stocks (+1 / +2)"
  - "Ki-drain throws absorb opponent resources"
counteredBy:
  - "Cannot manually charge (can't burst-refill on demand)"
  - "Auto ki-recovery stops during a Z-Counter (Apr 2025)"
  - "Super Absorb buff removed (Jun 2025 / May 2026)"
summary: "The android class trades manual ki charging for sustained ki output. Androids CANNOT hold charge (charge speed 0) but get effectively unlimited ki blasts and start the match with extra skill stocks: +1 for infinite-ki androids (16/17/18/Super 17), +2 for ki-drain androids (19, Dr. Gero). The ki-drain pair also absorb on grab (throw damage ~3,594/3,875). The Apr 2025 patch stopped their auto ki-recovery during Z-Counters, and Jun 2025/May 2026 removed the Super-Absorption stat-boost."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Android 19 / Dr. Gero: Dragon Dash, Quick Ascend, Quick Descend now consume ki (killed the infinite ascend/descend stall); throw HP/ki absorption adjusted."
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Androids (general): auto ki recovery now stops during a Z-Counter; silhouette hidden with Z-Search off."
  - version: "Ver.2013.012.003.008.007 (Jun 23, 2025)"
    date: "2025-06-23"
    change: "Dr. Gero: Super-Absorption vs beam/ki blast now triggers Sparking! Mode and the stat-boost effect is removed."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Dr. Gero / Android 19: Super Perception vs beam/projectile now triggers Sparking! Mode, stat-boost removed (cross-platform lock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§2.3 class ki quirks; §7 character-class modifiers)"
  - "research/03-patches-balance.md (Dec 2024; Apr 21 2025; Jun 23 2025; May 26 2026)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Apr 21, 2025; Jun 23, 2025; May 26, 2026)"
---
The **Android** class — [[android-16|16]], [[android-17-z|17]], [[android-18|18]], Super 17, [[android-19|19]], and [[dr-gero|Dr. Gero]] — trades **manual ki charging** for **sustained ki output**. They are the only bodies that cannot hold charge.

## The numbers

- **Manual charge speed: 0.** Androids **cannot** hold R2/RT to refill ki — the [[ki-and-charging|charge]] action does nothing for them. Instead their ki blasts are **effectively unlimited** (each shot still costs **16–22%/bar**, but the bar refills via the android mechanic rather than manual charge).
- **Extra starting [[skill-count|skill stocks]]:** to compensate for no manual charge, androids **begin the match with bonus stocks** — **+1** for the infinite-ki group ([[android-16|16]], 17, [[android-18|18]], Super 17) and **+2** for the ki-drain group ([[android-19|19]], [[dr-gero|Dr. Gero]]).
- **Ki-drain absorb-on-grab:** [[android-19|Android 19]] and [[dr-gero|Dr. Gero]] deal **~3,594 / 3,875** on a [[throws|throw]] — about **3×** a normal grab — because the throw **absorbs** the opponent's resources. This absorb identity is the whole point of the ki-drain subclass.

## Nerf history

- **Dec 11, 2024** — the infamous fix: [[android-19|Android 19]] / [[dr-gero|Dr. Gero]] Dragon Dash, Quick Ascend, and Quick Descend now **consume ki**, killing the **infinite ascend/descend stall** that got two finalists DQ'd in a Nov 2024 tournament.
- **Apr 21, 2025** — androids' **auto ki-recovery stops during a [[vanish-z-counter|Z-Counter]]**, closing the infinite-ki advantage in vanish wars; silhouette hidden with Z-Search off.
- **Jun 23, 2025 → May 26, 2026** — [[dr-gero|Dr. Gero]]'s (and Android 19's) **Super Absorption / Super Perception vs a beam now triggers [[sparking-mode|Sparking! Mode]]** instead of granting a stat boost (the buff was **removed**), cross-platform.

## Interactions

- Because they **can't burst-charge**, androids can't instantly top off ki before a [[sparking-mode|Sparking]] pop the way other characters can — their ki is steady but not on-demand.
- The +1/+2 stock head start makes early [[revenge-counter|Revenge Counter]], [[perception|Perception]], or transform plays available sooner than for a 0-stock character.
- Distinct from the [[giant-class|giant]] class (bulk/armor, throw-immune, 2-bar dashes) and from [[super-armor|super-armor]] moves — androids are a **resource** archetype, not a defensive-stat one.
