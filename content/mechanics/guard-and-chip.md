---
slug: "guard-and-chip"
name: "Guard & Chip Damage"
category: "defense"
input: "Hold Guard (L1/LB) to block; sustained pressure chips your health and a guard-break costs ki"
values:
  - label: "Chip damage while guarding"
    value: "guards take chip damage by default (inferred from the 'Perfect Guard' item)"
    patch: "current"
    tag: "community"
  - label: "Guard-break ki damage (base)"
    value: "1 ki bar of damage (inferred from the 'Mind Breaker' item)"
    patch: "current"
    tag: "community"
  - label: "Guard-break ki damage (Mind Breaker item)"
    value: "1.5 bars (+50%)"
    patch: "current"
    tag: "datamined"
  - label: "Perfect Guard item"
    value: "no chip damage while blocking"
    patch: "current"
    tag: "datamined"
  - label: "Guard Master item"
    value: "guard becomes unbreakable"
    patch: "current"
    tag: "datamined"
  - label: "Perception during guard stun"
    value: "disabled (cannot Perception out of blockstun)"
    patch: "Apr 21, 2025 →"
    tag: "official"
counters:
  - "Rush strings (blocks the hits)"
  - "Most blasts head-on"
counteredBy:
  - "Throws (beat guard)"
  - "Guard-break pressure (depletes ki)"
  - "Chip damage over time"
  - "Unblockable / Impossible-Guard blasts"
summary: "Holding Guard blocks attacks but is not free: guards take chip damage by default, and a guard-break deals a base 1 ki bar of damage (1.5 with the Mind Breaker item). The existence of the 'Perfect Guard' (no chip) and 'Guard Master' (unbreakable) items confirms guards chip and break by default. Since Apr 2025 you cannot Perception during guard stun, and the May 2026 patch fixed guard-break inconsistencies."
changeHistory:
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Perception can no longer be used during guard stun; fixed guard being possible between a Rush-In and the following Rush Attacks."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Guard-break inconsistencies fixed; Perception remains unusable during guard stun (cross-platform lock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§3.5 Guard — item-implied defaults)"
  - "research/03-patches-balance.md (Apr 21 2025; May 26 2026)"
  - "Bandai Namco official patch notes (Apr 21, 2025; May 26, 2026)"
---
Guarding (**hold L1/LB**) blocks incoming melee and most blasts, but it is a **leaky** defense — sustained pressure chips your health, and if the opponent overwhelms your guard it **breaks**, costing you ki and leaving you open.

## The numbers

Most guard values are **inferred from datamined item effects** rather than published directly — the items only make sense if the defaults are what they imply:

- **Chip damage:** guards take chip damage by default. The **"Perfect Guard"** item exists specifically to grant **no chip while blocking**, which confirms ordinary guards *do* chip.
- **Guard-break ki damage:** a guard-break deals a **base 1 ki bar** of damage. The **"Mind Breaker"** item raises this to **1.5 bars (+50%)** — again implying the **1-bar** baseline.
- **Breakability:** the **"Guard Master"** item makes a guard **unbreakable**, which only matters because normal guards *are* breakable.

The exact chip-damage value per hit is **not datamined or community-measured into a number** — only the *existence* of chip and the *1-bar* guard-break cost are established.

## Interactions

- **Cannot Perception out of guard stun** since Apr 21, 2025: once you're in blockstun you can't mash [[perception|Perception]] to escape, so the opponent's pressure window is real. The same patch removed an exploit where you could guard *between* a Rush-In and its Rush Attacks.
- **Throws beat guard** — the standard answer to a turtling opponent is to grab. See [[throws|throws]].
- **Unblockable / "Impossible Guard" blasts** ignore guard entirely (e.g. Cell Max's Max Bomb was made unblockable in Jan 2026; see [[health-and-damage|damage]]).
- **May 26, 2026** fixed guard-break inconsistencies, so the **1-bar** guard-break cost should now apply reliably; the underlying per-hit chip number has **not been re-measured** since.
- When guard isn't an option, the active alternatives are [[super-counter|Super Counter]], [[vanish-z-counter|Vanish]], [[revenge-counter|Revenge Counter]], and [[perception|Perception]].
