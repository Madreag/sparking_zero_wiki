---
slug: "caulifla"
name: "Caulifla"
charId: "0900_00"
baseCharacter: "Caulifla"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Caulifla, Super Saiyan 2"
    targetSlug: "caulifla-super-saiyan-2"
    cost: 2
    kind: "transform"
  - target: "Kefla"
    targetSlug: "kefla"
    cost: 2
    kind: "fusion"
  - target: "Kefla, Super Saiyan"
    targetSlug: "kefla-super-saiyan"
    cost: 3
    kind: "fusion"
  - target: "Kefla, Super Saiyan 2"
    targetSlug: "kefla-super-saiyan-2"
    cost: 4
    kind: "fusion"
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Explosive Wave"
    type: "blast2"
    kiCost: 40000
  - name: "Crush Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Kefla-access Saiyan"
strengths:
  - "Two-stock transform to SS2, plus Potara-fusion into Kefla (2-4 stock for SS/SS2 variants)"
  - "False Courage S1 (free) and Wild Sense S2 (free) give a buff and a 1-hit auto-dodge"
  - "Full-Power Energy Wave (30,000 ki) and Super Explosive Wave (40,000 ki); Crush Cannon ult (50,000 ki)"
weaknesses:
  - "DP5 base is weak; value is in the transform and Kefla fusion"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "Deny the transform and watch the meter — she can Potara into Kefla (2-4 stock) if Kale is on the team. Wild Sense is a single-hit read; stagger to bait it. Keep her stock-starved and pressure the base."
summary: "DP5 Caulifla base; 40k HP, False Courage + Wild Sense, 2-stock transform to SS2; Potara into Kefla."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

