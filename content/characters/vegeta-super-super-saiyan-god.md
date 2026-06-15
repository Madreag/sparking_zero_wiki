---
slug: "vegeta-super-super-saiyan-god"
name: "Vegeta (Super), Super Saiyan God"
charId: "0022_62"
baseCharacter: "Vegeta (Super)"
era: "Super"
dp: 7
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
  - target: "Vegeta (Super), Super Saiyan God Super Saiyan"
    targetSlug: "vegeta-super-super-saiyan-god-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Vegeta (Super)"
    targetSlug: "vegeta-super"
    cost: 0
    kind: "transform"
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "God Shine Attack"
    type: "blast2"
    kiCost: 30000
    damage: 3900
    properties:
      - "Continuous Fire"
      - "Played after a hit"
      - "weak-vs-shield"
  - name: "Gamma Fist"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Prominence Flash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "God Shine Attack (30,000-ki super)"
  - "Gamma Fist (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Prominence Flash 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Gamma Fist rush rather than mashing into it."
summary: "DP7 Super-era fighter; 40,000 HP; God Shine Attack 30,000-ki super, Prominence Flash 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

