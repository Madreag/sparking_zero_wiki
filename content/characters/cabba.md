---
slug: "cabba"
name: "Cabba"
charId: "0890_00"
baseCharacter: "Cabba"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Cabba, Super Saiyan"
    targetSlug: "cabba-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Cabba, Super Saiyan 2"
    targetSlug: "cabba-super-saiyan-2"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Cannon"
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
  - name: "Galick Rage"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Transform-ladder Saiyan"
strengths:
  - "Cheap 1-stock transform to SS, 2-stock to SS2 — flexible ladder"
  - "Full Power S2 (4 stock) no-auto-guard buff feeds the climb"
  - "High Speed Rush super at 30,000 ki (15,000 trigger, speed-impact); Galick Rage ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP5 base is weak; value is in the ladder"
  - "Average 1,750 recovery, no escape tool"
  - "Each form-up costs stock"
howToFight: "Deny the cheap transforms — keep him stock-starved at the weak base. Punish Full Power (no-auto-guard). He has no defensive escape, so press your turn before he ascends to SS2."
summary: "DP5 Cabba base; 40k HP, Full Power (4 stock), High Speed Rush speed-impact; 1-stock/2-stock transforms to SS and SS2."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

