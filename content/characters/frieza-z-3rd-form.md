---
slug: "frieza-z-3rd-form"
name: "Frieza (Z), 3rd Form"
charId: "0152_00"
baseCharacter: "Frieza (Z)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Frieza (Z), 4th Form"
    targetSlug: "frieza-z-4th-form"
    cost: 1
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Barrage Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Crazy Finger Beam"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Barrage Death Beam (20,000-ki super)"
  - "High Speed Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Crazy Finger Beam 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "High-Tension self ki-charge buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the High Speed Rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; High Speed Rush 30,000-ki speed-impact super, Crazy Finger Beam 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

