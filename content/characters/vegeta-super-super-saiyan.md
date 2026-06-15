---
slug: "vegeta-super-super-saiyan"
name: "Vegeta (Super), Super Saiyan"
charId: "0020_61"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Super"
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
  - target: "Vegeta (Super), Super Saiyan God"
    targetSlug: "vegeta-super-super-saiyan-god"
    cost: 1
    kind: "transform"
  - target: "Vegeta (Super), Super Saiyan God Super Saiyan"
    targetSlug: "vegeta-super-super-saiyan-god-super-saiyan"
    cost: 2
    kind: "transform"
moveset:
  - name: "I'll Get You For This..."
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Rush"
    type: "blast2"
    kiCost: 30000
    damage: 3900
    properties:
      - "Fire"
      - "Played after a hit"
      - "weak-vs-shield"
  - name: "Galick Uppercut"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Final Galick Blast"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Galick Rush (30,000-ki super)"
  - "Galick Uppercut (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Final Galick Blast 50,000-ki ultimate finisher"
  - "Saiyan Spirit ki/attack buff"
  - "Transforms (1 stock to Vegeta (Super)) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Galick Uppercut rush rather than mashing into it."
summary: "DP6 Super-era fighter; 40,000 HP; Galick Rush 30,000-ki super, Final Galick Blast 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

