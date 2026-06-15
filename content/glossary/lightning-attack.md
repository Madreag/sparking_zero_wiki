---
slug: "lightning-attack"
term: "Lightning Attack"
definition: "A high-speed dashing melee pursuit that chases a knocked-away opponent; the datamined pursuit cap is 'pursuitBaseLimit' — 1–4 per combo (most fighters 2), rising +2 while Sparking. It's how you extend pressure after a launch."
aliases:
  - "Lightning Pursuit"
  - "Pursuit Attack"
category: "offense"
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "data-mined/characters.json (pursuitBaseLimit: 1/2/3/4, mode 2; pursuitAddAtSparking +2)"
  - "research/04-mechanics-frame-data.md §1 (combo pursuit behavior)"
---
**Lightning Attack** is the high-speed dashing pursuit that lets you chase a knocked-away opponent and continue a combo. The datamine caps how many pursuits you can chain in one combo via the **`pursuitBaseLimit`** field (characters.json), which runs **1 to 4** — **most fighters sit at 2** — and **rises by +2 while [[sparking-mode|Sparking]]** (`pursuitAddAtSparking` = 2). There is **no `pursuitLimitLightning` field**: the old "**4 / 6 / 7**" reading was actually [[skill-count|max skill stock]], and `Numeric.json`'s `PursuitLimitLightningAttack` reads **0**. Hitting that per-combo limit is one reason long combos eventually drop — see [[smash-attack]] and combo scaling in [[beginner-numbers-guide]].
