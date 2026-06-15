---
slug: "dp-system"
name: "DP System"
category: "system"
input: "Team-building — spend a DP budget to assemble your roster for DP Battle"
values:
  - label: "DP budget (standard)"
    value: "15 DP"
    patch: "current"
    tag: "official"
  - label: "Selectable DP totals"
    value: "10 / 15 / 20 (settings retained)"
    patch: "May 26, 2026"
    tag: "official"
  - label: "Singles vs DP balance"
    value: "split — single battle dropped DP scaling & equalized HP; DP battle keeps DP-cost differences"
    patch: "Jun 23, 2025"
    tag: "official"
  - label: "DP-difference damage (DP battle only)"
    value: "'Big Impact' item: +500 at 1 DP diff, +250 per extra DP"
    patch: "current"
    tag: "community"
  - label: "Auto-reflect DP gate"
    value: "only DP 7+ characters can auto-reflect in Sparking! Mode"
    patch: "Apr 21, 2025; re-locked May 26, 2026"
    tag: "official"
counters:
  - "Lets you field multiple cheaper characters or one expensive one"
  - "DP-difference damage bonus (in DP battle, with item)"
counteredBy:
  - "Budget cap forces tradeoffs"
  - "Single battle ignores DP entirely (since Jun 2025)"
summary: "The team-cost system: spend a DP budget (standard 15, selectable 10/15/20 since May 2026) to build your DP-Battle roster, where pricier characters cost more of the pool. Jun 23, 2025 split the balance — single battle dropped DP-based damage scaling and equalized HP, while DP battle keeps and widens DP-cost differences. May 26, 2026 widened the DP spread further and gates Sparking-mode auto-reflect to DP 7+ characters."
changeHistory:
  - version: "Ver.2013.012.003.008.007 (Jun 23, 2025)"
    date: "2025-06-23"
    change: "Single Battle: removed DP-based damage scaling in all modes and equalized HP; DP Battle rebalanced so DP-cost differences between characters are more pronounced (team rules unchanged). This is the singles/DP balance split."
  - version: "Ver.2011.010.003.007.006 (Apr 21, 2025)"
    date: "2025-04-21"
    change: "Auto-reflect can only be activated by DP 7+ characters during Sparking! Mode."
  - version: "Free Update (May 26, 2026)"
    date: "2026-05-26"
    change: "DP differences between characters made more pronounced in all modes (DP-gap widening); total DP selectable 10/15/20 with settings retained; auto-reflect DP 7+ gate re-locked cross-platform."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§8 DP-based damage scaling removed; 'Big Impact' item)"
  - "research/03-patches-balance.md (Apr 21 2025; Jun 23 2025; May 26 2026; DP total 10/15/20)"
  - "Bandai Namco official patch notes (Apr 21, 2025; Jun 23, 2025; May 26, 2026)"
---
DP (Destruction Points) is the **team-cost** system inherited from Budokai Tenkaichi 3. In **DP Battle** you assemble a team against a shared budget: pricier characters cost more, so you trade one expensive fighter against several cheap ones.

## The numbers

- **DP budget: 15** is the standard. Since the **May 26, 2026** update the total is **selectable at 10 / 15 / 20**, and the setting is retained between matches.
- **DP-difference damage (DP battle only):** the **"Big Impact"** item adds DP-gap damage — **+500** at a 1-DP difference, **+250** per additional DP — but **only in DP Battles**. The DP-gap math rides on per-character DP, which is **community-sourced** (not in the game files), so treat these figures as **community**. There is no longer any *innate* DP damage bonus.
- **Auto-reflect is gated to DP 7+** characters in [[sparking-mode|Sparking! Mode]] (Apr 21, 2025; re-locked May 26, 2026) — a soft cap that keeps cheap fighters from getting the reflect.

## The singles / DP balance split (Jun 23, 2025)

This is the **system-defining** change. The **Jun 23, 2025** patch (Ver.2013.012.003.008.007) split the two modes:

- **Single Battle** — **removed DP-based damage scaling** in all modes and set **all characters to the same health**. A high-DP single character no longer hits harder *or* survives longer than a low-DP one in singles. See [[health-and-damage|health & damage]].
- **DP Battle** — kept and **made DP-cost differences more pronounced**, so the budget tradeoff matters more when team-building.

## DP-gap widening (May 26, 2026)

The **May 26, 2026** free update **widened the DP spread further** ("DP differences between characters made more pronounced in all modes") and confirmed the **DP 7+ auto-reflect gate** cross-platform. The intent is to make the budget meaningfully constrain teams: a top-cost fighter should cost a real chunk of your 15 (or 10/20).

> The **exact DP value of each individual character** is tracked on the [[health-and-damage|character]] pages (the `dp` field), not here — this page documents the **system** (budget, split, gates), while per-character DP costs live in the roster data.
