---
slug: "revenge-counter"
name: "Revenge Counter"
category: "defense"
input: "Right-stick press (R3) while being hit — breaks a combo from any direction"
values:
  - label: "Cost"
    value: "2 skill stocks (some launch guides said 1)"
    patch: "current"
    tag: "community"
  - label: "Direction"
    value: "any (front, back, mid-combo)"
    patch: "current"
    tag: "official"
  - label: "Counter-the-counter (Super Z-Counter)"
    value: "Perception-vs-Revenge-Counter cost reducible by 1 (min 1) via 'The Secret to Counters' item"
    patch: "current"
    tag: "datamined"
  - label: "Perception-vs-Revenge-Counter window"
    value: "fixed (was shorter than intended)"
    patch: "Sep 22, 2025"
    tag: "official"
counters:
  - "Combos from any direction"
  - "Pressure you cannot Super Counter (back hits, staggers)"
counteredBy:
  - "Having fewer than 2 skill stocks (cannot activate)"
  - "Super Z-Counter (Perception on the Revenge Counter)"
  - "Baiting it then whiff-punishing"
summary: "The skill-stock 'get-off-me': press R3 while being comboed to break out from any direction for 2 skill stocks. Unlike Super Counter (free, front-only, frame-tight) it works from behind and mid-string, but the stock cost makes it a finite resource. Launch guides cited 1 stock; current community consensus puts it at 2, but no official numeric note has resolved it."
changeHistory:
  - version: "Free Update (Dec 11, 2024)"
    date: "2024-12-11"
    change: "Skill Count consumed when using Perception AGAINST a Revenge Counter reduced 2 → 1 (cheaper to counter-the-counter)."
  - version: "Ver.2014.013.003.009.008 (Sep 22, 2025)"
    date: "2025-09-22"
    change: "Fixed the Perception-vs-Revenge-Counter window being shorter than intended."
  - version: "Ver.2014.013.003.009.008 (Sep 22, 2025)"
    date: "2025-09-22"
    change: "Paralyzing Smash Ki Blast: Revenge Counter now usable when hit from the front by it."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§3.4 Revenge Counter; Gaps #5 cost 1-vs-2)"
  - "research/03-patches-balance.md (Dec 11 2024; Sep 22 2025)"
  - "Bandai Namco official patch notes (Dec 11, 2024; Sep 22, 2025)"
---
Revenge Counter is the **skill-stock panic button**: press the **right stick (R3)** while you are being comboed and your character bursts out of the string — from **any** direction, even mid-combo — and counter-attacks. It is the last-ditch "get off me" when you can't [[super-counter|Super Counter]] your way out.

## The numbers

- **Cost: 2 skill stocks.** A handful of launch-era guides listed it at **1**, and Bandai's own text says "consumes a Skill Count" (singular), but current community labbing and consensus put it at **2 stocks** in the live build. This is flagged as a known 1-vs-2 ambiguity that has never been resolved by an official numeric note — treat **2** as the working figure pending a current-patch confirmation.
- **Any direction:** unlike Super Counter (front-only) and [[vanish-z-counter|Vanish]] (timing on the connecting hit), Revenge Counter breaks a combo regardless of where the hits are landing, which is what you pay the 2 stocks for.
- **Counter-the-counter:** an opponent can **Perception your Revenge Counter** (a "Super Z-Counter"). The datamined item **"The Secret to Counters"** reduces the skill cost of that Perception-vs-Revenge-Counter by **1 (minimum 1)**, making the counter-the-counter cheaper.

## Interactions

- **Sep 22, 2025** fixed the Perception-vs-Revenge-Counter window being shorter than intended, and made Revenge Counter usable from the **front** against a Paralyzing Smash Ki Blast.
- In **DP battles** Revenge Counter competes with [[super-counter|Super Counter]] as the comeback tool — Super Counter is free but front-only and frame-tight, Revenge Counter is omnidirectional but burns **2** of your finite [[skill-count|skill stocks]].
- Because it spends stocks, a Revenge Counter is only available when you have **at least 2** in the bank — pressure that drains your stocks (forcing transforms, [[perception|Perception]] blasts, or [[instant-sparking|Instant Sparking]]) also locks you out of this escape.
