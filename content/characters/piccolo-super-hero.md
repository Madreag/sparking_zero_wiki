---
slug: "piccolo-super-hero"
name: "Piccolo (Super Hero)"
charId: "3010_00"
baseCharacter: "Piccolo (Super Hero)"
era: "Movie"
dp: 5
source: "\"Heroes of Justice\" Pack"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Piccolo (Super Hero), Power Awakening"
    targetSlug: "piccolo-super-hero-power-awakening"
    cost: 1
    kind: "transform"
moveset:
  - name: "False Courage"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Full Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Full Power Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "Trigger cost 15,000 ki"
  - name: "Light Grenade"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Orange-access base"
strengths:
  - "Cheap 1-stock transform to Power Awakening, climbing toward A-tier Orange Piccolo"
  - "Wild Sense S1 (free) 1-hit auto-dodge + False Courage S2 (free) buff"
  - "Full Power Energy Blast Volley (30,000 ki) and speed-impact Full Power Rush (30,000 ki / 15,000 trigger); Light Grenade ult (50,000 ki)"
weaknesses:
  - "DP5 base is weak; value is in the Orange line"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "Deny the cheap transform path toward Orange Piccolo. Wild Sense is a single-hit read; stagger to bait it. Keep him stock-starved and pressure the base — no escape tool means your turn sticks."
summary: "DP5 Piccolo (SH) base; 40k HP, Wild Sense + False Courage, Full Power Rush speed-impact; 1-stock to Power Awakening toward Orange."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

