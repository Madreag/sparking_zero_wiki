---
slug: "vegito"
name: "Vegito"
charId: "0100_00"
baseCharacter: "Vegito"
era: "Z"
dp: 7
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Super Vegito"
    targetSlug: "super-vegito"
    cost: 1
    kind: "transform"
  - target: "Vegito, Super Saiyan God Super Saiyan"
    targetSlug: "vegito-super-saiyan-god-super-saiyan"
    cost: 2
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Big Bang Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Rampaging Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "A"
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "A-tier fusion neutral at a reasonable DP7 — good entry into the Vegito ladder"
  - "Rampaging Rush speed-impact super (15,000 ki on combo trigger) for cheap extensions"
  - "Transforms up to Super Vegito (1 stock) then SSGSS (2 stock) for a mid-match power spike"
  - "High-Tension self ki-charge to fuel supers"
weaknesses:
  - "Base form ult is only Super Kamehameha (50,000 ki) — weaker than the God Final Kamehameha it gains later"
  - "DP7 with no defensive auto-dodge in base form"
  - "Wants to transform to be at full strength, costing stock"
howToFight: "Pressure base Vegito before it climbs to SSGSS. No auto-dodge here, so Super Counter (free) and vanish punish his strings. Watch for the 1-stock transform into Super Vegito which adds Afterimage Strike."
summary: "DP7 Vegito (base Z): A-tier fusion; Big Bang Cannon (30,000 ki) + Rampaging Rush speed-impact (15,000 on trigger); transforms to Super Vegito / SSGSS."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

