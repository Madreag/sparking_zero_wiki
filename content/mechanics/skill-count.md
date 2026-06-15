---
slug: "skill-count"
name: "Skill Count (Skill Stocks)"
category: "resource"
input: "Auto-regenerates over time and from combat events; spent to activate Blast Skills, counters, transforms, and Instant Sparking"
values:
  - label: "Auto-regen rate"
    value: "~1 stock / ~14 s (≈4.2 stocks/min) standard; Roshi 5.46/min"
    patch: "pre-May 2026 (community)"
    tag: "community"
  - label: "Max skill stocks"
    value: "character-specific, typically 4–5 (Cell/Piccolo 5; many 4; Yajirobe raised 5→6)"
    patch: "current"
    tag: "datamined"
  - label: "Starting stocks"
    value: "usually 0; androids +1, ki-drain androids +2; 'Secret Measures' item +1"
    patch: "current"
    tag: "datamined"
  - label: "Revenge Counter cost"
    value: "2 stocks"
    patch: "current"
    tag: "official"
  - label: "Perception (vs blast) cost"
    value: "2 stocks"
    patch: "current"
    tag: "official"
  - label: "Instant Sparking cost"
    value: "4 stocks (was 3 at launch)"
    patch: "Jan 20, 2025 →"
    tag: "official"
  - label: "Afterimage Strike cost"
    value: "3 stocks"
    patch: "current"
    tag: "datamined"
  - label: "Senzu Bean cost"
    value: "5 stocks (6 for buffed Yajirobe)"
    patch: "current"
    tag: "datamined"
  - label: "Low-HP bonus regen"
    value: "faster regen, but only below the LAST health bar"
    patch: "Jun 23, 2025 →"
    tag: "official"
counters:
  - "Funds every skill, counter, and transform"
  - "Builds passively even while neutral"
counteredBy:
  - "Expensive skills drain it fast (Instant Sparking 4, Senzu 5)"
  - "Slowed auto-regen (May 2026)"
  - "No longer regenerates on a successful tech (Jun 2025)"
summary: "The skill-stock economy: a character-specific bank (usually 4–5) that auto-regenerates at roughly 1 stock per 14 seconds (community estimate) plus combat events. It funds Blast Skills, defensive counters, transforms, and Instant Sparking. Costs of common actions: Revenge Counter 2, blast Perception 2, Afterimage Strike 3, Instant Sparking 4, Senzu Bean 5. The Jun 2025 and May 2026 patches slowed regen and removed tech/low-HP sources."
changeHistory:
  - version: "Ver.2013.012.003.008.007 (Jun 23, 2025)"
    date: "2025-06-23"
    change: "Auto-recovery rate slightly reduced; no longer recovers on a successful tech; low-HP bonus regen only triggers below the LAST health bar; Attack-Break gain increased."
  - version: "Ver.2014.013.003.009.008 (Sep 22, 2025)"
    date: "2025-09-22"
    change: "Dr. Wheelo max Skill Count reduced; Yajirobe-line Senzu loop tuned across DLC patches (max 5→6, Senzu cost →6)."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "Skill Stock auto-recovery speed slightly reduced again (cross-platform); increased recovery on a successful Attack Break."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§4 Skill (Skill-Stock) System; §4.2 skill costs)"
  - "data-mined/sparkingzerometa.com datamine (max stock, regen rate, starting stock)"
  - "research/03-patches-balance.md (Jun 23 2025; Sep 22 2025; May 26 2026)"
  - "Bandai Namco official patch notes (Jun 23, 2025; Sep 22, 2025; May 26, 2026)"
---
Skill Count (the **skill-stock** bank) is the second resource alongside [[ki-and-charging|ki]]. It funds Blast Skills, defensive counters, transformations, and [[instant-sparking|Instant Sparking]]. Stocks **regenerate over time** and from certain combat events, then are **spent** to activate skills.

## The numbers

- **Auto-regen: ~1 stock every ~14 seconds** (≈**4.2 stocks/min**) on a standard character — a **community** estimate, not an official figure. A few fighters regen faster (Master Roshi ~**5.46/min**). The Jun 2025 and May 2026 patches each **slightly reduced** this rate, so the 14-second figure is a **pre-May-2026** community number and has **not been re-measured** since the latest slowdown.
- **Max stocks: character-specific, usually 4–5** (Cell and Piccolo cap at **5**, many at **4**; Yajirobe was raised **5→6**).
- **Starting stocks:** usually **0**, but [[android-class|androids]] start **+1** (infinite-ki) or **+2** (ki-drain), and the **"Secret Measures"** item adds **+1**.

## Costs of common skills

| Action | Stock cost |
|---|---|
| [[revenge-counter|Revenge Counter]] | **2** |
| [[perception|Perception]] vs a blast | **2** |
| Wild Sense | **2** |
| [[afterimage-strike]] | **3** |
| [[instant-sparking|Instant Sparking]] | **4** (launch 3) |
| Senzu Bean (Yajirobe) | **5** (→**6** buffed) |
| Transformation (one tier) | **~1** |

## Regen sources & nerfs

- **Low-HP bonus regen** still exists but, since **Jun 23, 2025**, only triggers **below the last health bar** (it used to start earlier).
- Since **Jun 23, 2025** stocks **no longer recover on a successful tech**; the same patch **increased** the gain on a successful **Attack Break**, and **May 26, 2026** increased Attack-Break gain again while shaving the base auto-recovery rate.
- Stocks also build from [[vanish-z-counter|vanish wars]] (~15% of a gauge per vanish, though reduced Jan 2025). Because the bank is shared across **all** skill spending, expensive pops like Senzu (5) or Instant Sparking (4) lock you out of [[revenge-counter|Revenge Counter]] defense until you rebuild.
