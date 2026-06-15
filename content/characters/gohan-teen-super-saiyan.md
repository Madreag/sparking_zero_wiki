---
slug: "gohan-teen-super-saiyan"
name: "Gohan (Teen), Super Saiyan"
charId: "0031_01"
baseCharacter: "Gohan (Teen)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gohan (Teen), Super Saiyan 2"
    targetSlug: "gohan-teen-super-saiyan-2"
    cost: 1
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
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Assault Combo"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Raging Masenko"
    type: "ultimate"
    kiCost: 50000
    damage: 10500
    properties:
      - "Continuous Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Super Assault Combo (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Raging Masenko 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Full Power attack buff (4 stock)"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Super Assault Combo rush rather than mashing into it."
summary: "DP6 Z-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Raging Masenko 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

