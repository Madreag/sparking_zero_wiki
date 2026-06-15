---
slug: "gogeta-super-super-saiyan"
name: "Gogeta (Super), Super Saiyan"
charId: "0110_01"
baseCharacter: "Gogeta (Super)"
era: "Movie"
dp: 8
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 15
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gogeta (Super), Super Saiyan God Super Saiyan"
    targetSlug: "gogeta-super-super-saiyan-god-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Rising Vortex"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
tier: "S"
dpTier: "A"
singlesScore: 123.4
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Rising Vortex (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Instant Transmission teleport repositioning"
  - "Transforms (1 stock to Gogeta (Super)) for a mid-match power spike"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Rising Vortex rush rather than mashing into it."
summary: "DP8 Movie-era fusion, A-tier; Super Kamehameha 30,000-ki super."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

