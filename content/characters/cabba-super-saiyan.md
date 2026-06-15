---
slug: "cabba-super-saiyan"
name: "Cabba, Super Saiyan"
charId: "0890_01"
baseCharacter: "Cabba"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Cabba, Super Saiyan 2"
    targetSlug: "cabba-super-saiyan-2"
    cost: 1
    kind: "transform"
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Rain"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Galick Rage"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Galick Cannon"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mid-ladder Saiyan"
strengths:
  - "Cheap 1-stock transform onward to SS2"
  - "Wild Sense S2 (free) gives a 1-hit auto-dodge counter"
  - "Galick Rage super at 30,000 ki (15,000 trigger, speed-impact); Super Galick Cannon ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP6 intermediate; weaker than SS2 payoff"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "Keep him off the 1-stock SS2 transform. Wild Sense is a single-hit read — stagger to bait it. Starve ki and pressure the 40,000-HP body."
summary: "DP6 Cabba SS; 40k HP, Wild Sense escape, Galick Rage speed-impact; cheap 1-stock step to SS2."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

