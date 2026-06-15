---
slug: "planet-namek"
name: "Planet Namek"
source: "Base"
destructible: "Yes"
variants:
  - "Planet Namek"
notes: "Default Episode-Battle and Versus arena (Namek arc). A stage-locked 'Power of Namek' item grants +2% all damage here (excludes Destroyed Planet Namek)."
summary: "Open destructible arena; the canonical Namek battlefield (map ID 0000)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/04-mechanics-frame-data.md §9 (Map Destruction flag; Power of Namek item)"
---
**Planet Namek** — stage entry from the game's map table.

| Map ID | Variant |
|---|---|
| `0000` | Planet Namek |

Planet Namek is an open arena with destructible terrain — blasts flagged `Map Destruction` carve up the environment. It is one of the maps tied to a stage-locked item buff: 'Power of Namek' grants +2% all damage when fighting here (notably it does **not** apply on the separate Destroyed Planet Namek stage), which implies the game tracks these as discrete map IDs.
