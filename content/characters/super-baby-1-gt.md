---
slug: "super-baby-1-gt"
name: "Super Baby 1 (GT)"
charId: "0680_01"
baseCharacter: "Baby Vegeta (GT)"
era: "GT"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - target: "Super Baby 2 (GT)"
    targetSlug: "super-baby-2-gt"
    cost: 1
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Tuffle Revenger"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Final Flash"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mid-ladder villain"
strengths:
  - "Cheap 1-stock transform onward to Super Baby 2 (then Great Ape Baby)"
  - "Afterimage S1 (free) gives a 1-hit auto-dodge read"
  - "Tuffle Revenger super at 30,000 ki (15,000 trigger, speed-impact)"
  - "Galick Gun (30,000 ki) and Final Flash ult (50,000 ki)"
weaknesses:
  - "DP6 intermediate; weaker than the Great Ape payoff"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "No teleport escape"
howToFight: "Keep him from the next 1-stock transform — he's two cheap steps from a giant. Afterimage is one-hit; stagger to bait it. Starve ki and pressure; his 40,000 HP and lack of escape can't survive a sustained turn."
summary: "DP6 Super Baby 1; 40k HP, Afterimage + High-Tension, Tuffle Revenger speed-impact; 1-stock step to Super Baby 2."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

