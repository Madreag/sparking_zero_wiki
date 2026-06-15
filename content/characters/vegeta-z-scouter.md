---
slug: "vegeta-z-scouter"
name: "Vegeta (Z - Scouter)"
charId: "0020_00"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
  - target: "Great Ape Vegeta"
    targetSlug: "great-ape-vegeta"
    cost: 3
    kind: "transform"
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Final Galick Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Dirty Fireworks"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Galick Gun (30,000-ki super)"
  - "Final Galick Cannon (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Dirty Fireworks 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Final Galick Cannon rush rather than mashing into it."
summary: "DP4 Z-era fighter; 40,000 HP; Galick Gun 30,000-ki super, Dirty Fireworks 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

