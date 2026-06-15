---
slug: "gohan-super-hero-super-saiyan"
name: "Gohan (Super Hero), Super Saiyan"
charId: "3000_01"
baseCharacter: "Gohan (Super Hero)"
era: "Movie"
dp: 6
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Ultimate Gohan (Super Hero)"
    targetSlug: "ultimate-gohan-super-hero"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Ray"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Explosive Kick"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
      - "weak-vs-shield"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
dpTier: "Z"
dpScore: 25.1
playable: true
playstyle: "Mid-form (fragile)"
strengths:
  - "Two-stock transform to Ultimate Gohan (+5,000 HP) continuing toward Gohan Beast"
  - "Explosive Wave S1 (free) reversal + Full-Power Charge S2 (free) meter"
  - "Explosive Ray (30,000 ki) and speed-impact Explosive Kick (30,000 ki / 15,000 trigger); Super Kamehameha ult (50,000 ki)"
weaknesses:
  - "Still fragile 35,000 HP — low durability for DP6"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Transitional; the payoff is two transforms away"
howToFight: "Still only 35,000 HP — keep punishing and deny the climb to Ultimate/Beast. Pressure through his stock-building; he has no escape tool. The longer you keep him in these forms, the safer you are."
summary: "DP6 Gohan (SH) SS; fragile 35k HP, Explosive Wave + Full-Power Charge, Explosive Kick speed-impact; 2-stock to Ultimate."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

