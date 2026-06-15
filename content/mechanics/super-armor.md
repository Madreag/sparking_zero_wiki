---
slug: "super-armor"
name: "Super Armor"
category: "status"
input: "Property of armored moves / the 'Power Body' item — absorb hits without flinching"
values:
  - label: "Hits to flinch through armor"
    value: "4–5 Smash / Rush-Chain hits ('Power Body' item)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Rush 5-hit into armor"
    value: "~2,289 (≈7% less than the ~2,460 baseline)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "'Power Body' item tradeoff"
    value: "grants back-armor, −12% defense"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Giant stagger threshold"
    value: "4–5 (giants flinch only past the threshold)"
    patch: "current (datamine)"
    tag: "datamined"
counters:
  - "Absorbs hits without flinching (push through pressure)"
  - "Reduces melee damage taken (~7% on rush-5)"
counteredBy:
  - "Throws (bypass armor)"
  - "Enough hits to break the threshold (4–5)"
  - "−12% defense tradeoff (Power Body item)"
  - "Unblockable / armor-break moves"
summary: "Super armor lets a move or body absorb hits without flinching. The datamined 'Power Body' item grants back-armor that takes 4–5 Smash/Rush-Chain hits to break, but at −12% defense. Armor also cuts melee damage (a rush-5 doing ~2,460 drops to ~2,289 into armor, ≈7% less). The same 4–5 stagger threshold governs giants, which are inherently armored. Throws bypass armor entirely."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§7 Super Armor moves — 'Power Body' item 4–5 hits, −12% def; §1.3 rush-5 vs armor ~2,289)"
  - "data-mined/sparkingzerometa.com datamine ('Power Body' item, giant stagger threshold)"
---
Super armor lets a move — or an item-buffed body — **absorb incoming hits without flinching**, so you can push a Smash or charge through an opponent's pressure instead of getting interrupted.

## The numbers

- **4–5 hits to break.** The datamined **"Power Body"** item grants **back-armor** that withstands **4–5 Smash / Rush-Chain hits** before it breaks and you flinch. The tradeoff is **−12% defense** while equipped — you take more damage per hit in exchange for not flinching.
- **Armor reduces melee damage:** a [[smash-and-rush|rush 5-hit]] that does ~**2,460** on a bare body does ~**2,289** into armor — roughly **7% less**. See [[health-and-damage|health & damage]].
- **Same threshold as giants:** the **4–5** stagger threshold that breaks Power-Body armor is the same value that governs [[giant-class|giants]], which are inherently armored (and throw-immune).

## Interactions

- **[[throws|Throws]] bypass armor.** Armor stops *strikes*, not grabs — the standard answer to an armored push is to throw, exactly as with [[guard-and-chip|guard]].
- **Enough hits break it:** a full [[smash-and-rush|rush chain]] (□ ×1–4 + △) can exceed the **4–5** threshold, so a long string will break armor — but armor often gives the user enough frames to land their own Smash first.
- The **−12% defense** cost means armored play is **high-risk**: you trade flinch-immunity for taking more damage, so it favors aggressive, committal offense over neutral.
- Distinct from the [[giant-class|giant]] (innate armor + throw immunity + 2-bar dashes) and [[android-class|android]] (resource) classes — super armor here is a **move/item property** any character can carry, not a body class.
