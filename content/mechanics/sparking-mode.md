---
slug: "sparking-mode"
name: "Sparking! Mode"
category: "resource"
input: "Fill ki gauge + ≥1 skill count, keep charging to fill the Sparking gauge, then spend 1 skill count to activate (or use Instant Sparking)"
values:
  - label: "Sparking gauge charge speed"
    value: "7.0 / sec"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Pre-Sparking gauge decay"
    value: "10.5 / sec (drains if you stop charging)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Activation cost"
    value: "1 skill count (full ki gauge required first)"
    patch: "current"
    tag: "official"
  - label: "Damage in Sparking"
    value: "uses 'Boosted' blast values (~×1.2 to ×1.5)"
    patch: "current"
    tag: "datamined"
  - label: "Base duration (seconds)"
    value: "finite but UNPUBLISHED — items add +3 s, base not confirmed"
    patch: "not re-measured since May 26, 2026"
    tag: "community"
  - label: "Auto-reflect gate"
    value: "only DP 7+ characters can auto-reflect in Sparking! Mode"
    patch: "Apr 21, 2025; re-locked May 26, 2026"
    tag: "official"
counters:
  - "Unlocks your Ultimate Blast"
  - "Makes dashes/blasts ki-free"
  - "Grants immunity to ki-blast stun"
counteredBy:
  - "Defense-down window right after activation (May 2026)"
  - "Harsher combo scaling on rush attacks inside Sparking (Dec 2024)"
  - "Running out the timer"
summary: "The burst/comeback state (formerly 'Max Power'): fill ki + the separate Sparking gauge, spend 1 skill count, and gain your Ultimate, ki-free actions, ki-blast-stun immunity, and Boosted (~×1.2-1.5) damage. The datamine exposes the gauge charge speed (7.0/s) and the pre-Sparking decay (10.5/s) but the base DURATION in seconds and the exact stat-buff percentages are NOT published. Activation now carries a defense-down window since the panic-Sparking nerfs."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Rush attacks in Sparking! Mode: gradual consecutive-hit damage scaling increased (long combos punished harder inside Sparking)."
  - version: "Ver.2013.012.003.008.007 (Jun 23, 2025)"
    date: "2025-06-23"
    change: "Skills that instantly trigger Sparking! Mode and full-ki-recovery skills now reduce defense for a period after activation."
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Auto-reflect can only be activated by DP 7+ characters during Sparking! Mode."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Instant-Sparking and full-ki-recovery skills reduce defense for a period after activation (anti-panic-Sparking); auto-reflect DP 7+ gate re-locked cross-platform; standard charge-type Blasts now damage + knock back giants even in Sparking."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "data-mined/system_constants.json + sparkingzerometa.com datamine (Sparking gauge charge 7.0/s, pre-Sparking decay 10.5/s)"
  - "research/04-mechanics-frame-data.md (§5 Sparking! Mode; Gaps #1 base duration unverified)"
  - "research/03-patches-balance.md (Dec 2024; Apr 21 2025; Jun 23 2025; May 26 2026)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Apr 21, 2025; Jun 23, 2025; May 26, 2026)"
---
Sparking! Mode (the renamed **Max Power** burst from the Budokai Tenkaichi lineage) is the comeback/burst state. Fill your **ki gauge**, hold **≥1 skill count**, then keep charging to top off the **separate Sparking gauge**; spend **1 skill count** to pop it (or skip the gauge entirely with [[instant-sparking|Instant Sparking]]).

## The numbers

- **Sparking gauge charge speed: 7.0 / sec** (datamined). That is how fast holding charge fills the dedicated Sparking gauge once your ki is full.
- **Pre-Sparking decay: 10.5 / sec** (datamined). If you **stop** charging before activating, the partially-filled gauge drains at **10.5/s** — faster than it fills (7.0/s) — so you have to commit to the charge rather than feathering it.
- **Activation:** **1 skill count**, with a full ki gauge as the entry requirement.
- **Damage:** blasts in Sparking use their **"Boosted"** values, roughly **×1.2 to ×1.5** depending on the move (e.g. Super Kamehameha 9,080 → 13,660 ≈ ×1.50; most ultimates ≈ ×1.30). See [[health-and-damage|health & damage]].

> **Two gaps flagged explicitly.** The **base duration in seconds** is **not published** in any official note or on the datamine wiki — items add **"+3 s"**, which only proves the base is finite. Likewise the **stat-buff percentages** (attack/speed/special multipliers) are **not confirmed**; a circulating "exactly 15 s, +25% attack, +15% speed" figure set is **unverified and likely fabricated** — do not cite it as fact. Neither the base duration nor the buff magnitudes have been **re-measured since the May 26, 2026 update**.

## Buffs (official, qualitative)

On entering Sparking! Mode you gain: access to your **Ultimate Blast**, **ki-free actions** (dashes and blasts cost no ki), **immunity to ki-blast stun**, the **Boosted** damage values, and on a few characters extra stat boosts (e.g. Kid Gohan, Uub GT).

## Nerfs / changes

- **Dec 11, 2024** — consecutive-hit damage scaling on **rush attacks inside Sparking** was *increased*, so long combos are punished harder than out of Sparking.
- **Jun 23, 2025 & May 26, 2026** — skills that **instantly** trigger Sparking (see [[instant-sparking|Instant Sparking]]) and full-ki-recovery skills now **reduce your defense for a period after activation**. Popping Sparking to panic out of pressure leaves you **exposed**.
- **Auto-reflect is gated to DP 7+** characters in Sparking! Mode (Apr 21, 2025; re-locked May 26, 2026) — see [[dp-system|DP system]].
- **May 26, 2026** — standard charge-type Blasts now **damage and knock back** [[giant-class|giants]] even while the giant is in Sparking.
