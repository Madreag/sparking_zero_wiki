---
slug: "vanish-z-counter"
name: "Vanish (Z-Counter)"
category: "defense"
input: "Vanish (R1/RB) the instant the opponent's melee/Vanishing Assault connects; repeat to escalate a vanish war"
values:
  - label: "Ki cost per vanish"
    value: "~≈5,000 energy (community-measured) (community estimate; not a datamined field — no vanishKiCost field exists)"
    patch: "current (community)"
    tag: "community"
  - label: "Ki cost per vanish (bar estimate)"
    value: "~0.5 ki bar; ~0.25 bar at launch"
    patch: "Jan 20, 2025 → (community)"
    tag: "community"
  - label: "Skill stock gained per vanish"
    value: "~15% of a skill gauge (reduced from vanish wars Jan 2025)"
    patch: "current"
    tag: "community"
  - label: "QTE / Impact clash trigger"
    value: "after 4 consecutive vanishes"
    patch: "Jan 20, 2025 →"
    tag: "official"
  - label: "Escalation per exchange"
    value: "each vanish is faster and costs more ki"
    patch: "Jan 20, 2025 →"
    tag: "official"
  - label: "Return-counter damage"
    value: "scales up the longer the exchange runs"
    patch: "current"
    tag: "official"
counters:
  - "Incoming melee strings"
  - "Vanishing Assault pressure"
  - "Smash attacks (with timing)"
counteredBy:
  - "Running out of ki first (you lose the chain)"
  - "Throws (cannot be vanished)"
  - "Delayed/staggered timing that beats the window"
summary: "The ki-cost defensive teleport: vanish the exact frame a hit connects to reverse positions, then trade vanishes in a 'vanish war' until someone runs low on ki or a QTE fires after the 4th consecutive vanish. The per-vanish ki cost is community-estimated (~0.5 ki bar, sometimes quoted as ~≈5,000 energy (community-measured)) — it is NOT exposed as a datamined field, so treat every figure as a community estimate. Whoever has more ki wins the chain."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Input window shortened; becomes harder to perform when used consecutively; ki consumed on success increased; Skill Count gained on success reduced."
  - version: "Ver.2008.007.003.005.004 (Jan 20, 2025)"
    date: "2025-01-20"
    change: "Vanish-war escalation locked in — each subsequent vanish is faster and costs more ki; QTE/Impact clash after 4 consecutive vanishes; skill-stock gain from vanish wars reduced."
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Androids' auto ki recovery now stops during a Z-Counter (cuts the infinite-ki vanish advantage)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§3.3 Z-Counter / Vanishing Wars, community ki-bar tests)"
  - "research/03-patches-balance.md (Dec 11 2024; Jan 20 2025; Apr 21 2025)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Jan 20, 2025; Apr 21, 2025)"
---
Vanish — also called the **Z-Counter** — is the ki-cost defensive teleport. The instant an opponent's melee attack or [[vanishing-assault|Vanishing Assault]] connects, tap Vanish (R1/RB) to blink behind them and reverse the exchange. The opponent can vanish your follow-up in turn, and the two of you trade blinks in a **vanish war** until someone runs low on ki or the chain forces a clash.

## The numbers

- **Cost per vanish:** the community estimates the vanish action at **~0.5 of a ki bar** (up from ~0.25 at launch), sometimes quoted as **~≈5,000 energy (community-measured)**. This is **not** a datamined value — **no `vanishKiCost` field exists** in `characters.json`, and `system_constants.json` carries no vanish-cost distribution, so there is no per-character datamine number to confirm uniformity. Treat all per-vanish ki figures as community estimates; the bar conversion also predates the May 26, 2026 distance/ki re-tuning.
- **Skill-stock gain:** each successful vanish returns roughly **15% of a skill gauge**, though the Jan 20, 2025 patch explicitly **reduced** skill-stock gain from vanish wars to stop players farming stocks off the exchange.
- **Escalation:** since Jan 20, 2025 each vanish in a chain is **faster and costs more ki** than the last, so a long war drains both players and the **return-counter damage grows** the longer it runs.
- **QTE after 4:** after **4 consecutive vanishes** an Impact/QTE clash triggers, resolving the war into a button-mash or directional minigame rather than letting it loop forever.

> The exact per-vanish ki cost has **not been cleanly re-measured since the May 26, 2026 update**, which made dashes distance-scaled and re-tuned the ki economy. The ~0.5-bar (≈5,000-energy) figure is the best community estimate from the Jan 2025 era — there is no datamined vanish-cost field to fall back on.

## Interactions

- **Whoever has more ki wins the chain.** Community consensus: if you entered the war with less ki, bail early rather than getting blown up when your gauge empties mid-exchange.
- Cannot be used against [[throws|throws]] — grabs ignore the vanish window entirely, which is why throws are the standard answer to a vanish-happy opponent.
- [[android-class|Androids]] historically dominated vanish wars on effectively infinite ki; the Apr 21, 2025 patch stopped their auto ki-recovery **during** a Z-Counter to close that gap.
- Distinct from [[super-counter|Super Counter]] (free, up + rush, melee-only) and [[revenge-counter|Revenge Counter]] (2 skill stocks, any direction) — Vanish is the **ki**-priced reversal and the only one that snowballs into a war.
