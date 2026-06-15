---
slug: "baby-vegeta-gt"
name: "Baby Vegeta (GT)"
charId: "0680_00"
baseCharacter: "Baby Vegeta (GT)"
era: "GT"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Super Baby 1 (GT)"
    targetSlug: "super-baby-1-gt"
    cost: 1
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Finger Blitz Barrage"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Final Flash"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Transform-ladder base"
strengths:
  - "Cheap 1-stock transform to Super Baby 1, starting a long evolution ladder"
  - "High-Tension S2 (free) charge/buff feeds the climb"
  - "Galick Gun (30,000 ki) and Finger Blitz Barrage (20,000 ki); Final Flash ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP5 base is weak; value is entirely in the ladder"
  - "Average 1,750 recovery, no escape tool"
  - "Each form-up costs stock and time"
howToFight: "Deny the cheap 1-stock transforms — every step up the Baby ladder makes him stronger and eventually a giant. Keep him stock-starved and pressure the base form, which has no defensive escape. Whoever controls the meter controls the climb."
summary: "DP5 Baby Vegeta base; 40k HP, High-Tension buff, 1-stock transforms up the Super Baby ladder to Great Ape Baby."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

