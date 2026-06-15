---
slug: "kefla-super-saiyan"
name: "Kefla, Super Saiyan"
charId: "0920_01"
baseCharacter: "Kefla"
era: "Super"
dp: 7
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
  - target: "Kefla, Super Saiyan 2"
    targetSlug: "kefla-super-saiyan-2"
    cost: 1
    kind: "transform"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Blaster Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gigantic Claw"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Hexa-Cannonball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Mid-form fusion"
strengths:
  - "Cheap 1-stock transform onward to the A-tier SS2"
  - "False Courage S1 (free) buff + Finish Sign S2 (free) setup"
  - "Blaster Ball (30,000 ki) and speed-impact Gigantic Claw (30,000 ki / 15,000 trigger); Hexa-Cannonball ult (50,000 ki)"
weaknesses:
  - "DP7 intermediate; weaker than SS2"
  - "Average 1,750 recovery, no super-armor"
  - "Relies on speed rather than durability"
howToFight: "Keep her off the 1-stock SS2 transform. Vanish (≈half a ki bar) the speed-impact Gigantic Claw. Starve ki and pressure; the fusion has no defensive escape."
summary: "DP7 Kefla SS; null-HP fusion, False Courage + Finish Sign, Gigantic Claw speed-impact; 1-stock step to SS2."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

