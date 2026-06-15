---
slug: "gotenks"
name: "Gotenks"
charId: "0120_00"
baseCharacter: "Gotenks"
era: "Z"
dp: 6
source: "Base"
classes:
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gotenks, Super Saiyan"
    targetSlug: "gotenks-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Gotenks, Super Saiyan 3"
    targetSlug: "gotenks-super-saiyan-3"
    cost: 2
    kind: "transform"
moveset:
  - name: "Ta-dah!"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Victory Cannon"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "45,000 HP — above-baseline bulk"
  - "Full-Power Energy Wave (30,000-ki super)"
  - "High Speed Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Victory Cannon 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the High Speed Rush rather than mashing into it."
summary: "DP6 Z-era fusion; 45,000 HP; Full-Power Energy Wave 30,000-ki super, Victory Cannon 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

