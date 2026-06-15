---
slug: "z-burst-dash"
name: "Z-Burst Dash"
category: "movement"
input: "Burst-dash that arcs around the locked-on opponent to close distance / reposition"
values:
  - label: "Ki cost (non-giant)"
    value: "0.75 ki bar"
    patch: "Jan 20, 2025 (community)"
    tag: "community"
  - label: "Ki cost (giant)"
    value: "2.0 bars"
    patch: "Jan 20, 2025 (community)"
    tag: "community"
  - label: "Launch ki cost (historical)"
    value: "~2 bars (community estimate, pre-Jan 2025)"
    patch: "launch → Jan 19, 2025"
    tag: "community"
  - label: "Post-May 2026 cost model"
    value: "lower initial cost, then scales with travel distance"
    patch: "May 26, 2026"
    tag: "official"
  - label: "Speed vs Dragon Dash"
    value: "~50% slower than High-Speed Dragon Dash"
    patch: "current"
    tag: "community"
counters:
  - "Arcs around the opponent to reposition / close in"
  - "Cheap (0.75 bar) for non-giants post-Jan 2025"
counteredBy:
  - "Vanish / Perception on arrival"
  - "Giants pay 2 full bars (heavy tax)"
  - "Long-distance dashes cost more (May 2026 scaling)"
summary: "The burst-dash that arcs around a locked-on opponent. Costs ~0.75 ki bar for non-giants but 2 full bars for giants (a deliberate giant tax). The Jan 20, 2025 patch cut the non-giant cost to 0.75; the May 26, 2026 update lowered the initial cost but made it scale with travel distance (short hops cheap, full-screen expensive). Roughly 50% slower than the straight-line Dragon Dash."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Z-Burst Dash ki cost on activation increased; giant characters' Z-Burst tackle made guardable."
  - version: "Ver.2008.007.003.005.004 (Jan 20, 2025)"
    date: "2025-01-20"
    change: "Non-giant Z-Burst cost cut to ~0.75 bar (community-measured); short dashes made free."
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Activation ki cost reduced; now scales ki by distance travelled."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Initial ki cost reduced further, then scales with distance travelled (short hop cheap, full-screen expensive) — distance-scaling model locked in cross-platform."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§2.2 Z-Burst Dash; §7 giant 2-bar cost)"
  - "research/03-patches-balance.md (Dec 2024; Jan 20 2025; Apr 21 2025; May 26 2026)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Jan 20, 2025; Apr 21, 2025; May 26, 2026)"
---
Z-Burst Dash is the **arcing** burst movement — it sweeps **around** the locked-on opponent to reposition or close in, as opposed to the straight-line [[dragon-dash|Dragon Dash]].

## The numbers

- **Ki cost: 0.75 ki bar (non-giant) / 2.0 bars (giant).** The split is a deliberate **[[giant-class|giant]] tax** — a giant pays nearly **three times** what a normal character does to Z-Burst. Both figures are **community-measured** (no official number) on the **Jan 2025** build.
- **Distance-scaling (May 26, 2026):** the latest update **lowered the initial cost** but made the total **scale with travel distance** — a short hop is cheap, a full-screen dash is expensive. This means the **0.75-bar figure is now an approximation for a mid-range dash**; the true cost varies with distance and has **not been re-measured into a clean number since May 26, 2026**.
- **Historical:** a launch-era community estimate put the original Z-Burst at **~2 bars**; the Jan 2025 patch cut it to 0.75. Treat the 2-bar figure as **pre-Jan-2025 / stale**.
- **Speed: ~50% slower than [[dragon-dash|High-Speed Dragon Dash]]** — you trade straight-line speed for the ability to come at the opponent from an angle.

## Interactions

- On arrival the opponent can [[vanish-z-counter|Vanish]] or [[perception|Perception]] the follow-up; Z-Burst closes the gap but the hit still has to beat their defense.
- **[[giant-class|Giants]] pay 2 full bars** and (since Dec 2024) their Z-Burst **tackle is guardable**, so the dash is a much weaker tool on a giant body.
- Since **Jan 26, 2026**, **Solar Flare** no longer ends when approached via Z-Burst or [[dragon-dash|Dragon Dash]].
- The **free** alternative is the short (burst) dash — **0 ki**, chainable — which the Jan 2025 patch added as the cheap repositioning option below Z-Burst.
