---
slug: "cell-perfect-form"
name: "Cell, Perfect Form"
charId: "0162_00"
baseCharacter: "Cell"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
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
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Barrage Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Perfect Barrier"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Barrage Death Beam (20,000-ki super)"
  - "Perfect Barrier 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Afterimage evasive step"
weaknesses:
  - "Slow 6 ki charge — sluggish to fund supers"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Pressure his slow 6 ki charge by forcing blocks so he can't reach his supers. Respect Perfect Barrier on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Perfect Barrier 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

