---
slug: "lightning-attack"
term: "Lightning Attack"
definition: "A high-speed dashing melee pursuit that chases a knocked-away opponent; the datamine caps the number of Lightning pursuits in a single combo (the 'pursuitLimitLightning' field is 6 for most characters, with some at 4). It's how you extend pressure after a launch."
aliases:
  - "Lightning Pursuit"
  - "Pursuit Attack"
category: "offense"
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "data-mined/characters.json (pursuitLimitLightning: 4 / 6 / outlier 7)"
  - "research/04-mechanics-frame-data.md §1 (combo pursuit behavior)"
---
**Lightning Attack** is the high-speed dashing pursuit that lets you chase a knocked-away opponent and continue a combo. The datamine caps how many Lightning pursuits you can chain in one combo via the **`pursuitLimitLightning`** field, which reads **6 for most characters** (e.g. Goku) and **4 for many others** (e.g. Krillin, Tien, Future Trunks); a single outlier (Babidi) reads 7. Hitting that per-combo limit is one reason long combos eventually drop — see [[smash-attack]] and combo scaling in [[beginner-numbers-guide]].
