---
slug: "vegeta-z-end-super-saiyan"
name: "Vegeta (Z - End), Super Saiyan"
charId: "0020_31"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Z - End), Super Saiyan 2"
    targetSlug: "vegeta-z-end-super-saiyan-2"
    cost: 1
    kind: "transform"
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Final Flash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Infinite Blaster"
    type: "blast2"
    kiCost: 20000
  - name: "Cosmic Circle"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Final Flash (30,000-ki super)"
  - "Infinite Blaster (20,000-ki super)"
  - "Cosmic Circle 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Cosmic Circle on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Final Flash 30,000-ki super, Cosmic Circle 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

