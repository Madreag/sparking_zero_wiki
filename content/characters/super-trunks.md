---
slug: "super-trunks"
name: "Super Trunks"
charId: "0081_20"
baseCharacter: "Super Trunks"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Trunks (Melee)"
    targetSlug: "trunks-melee"
    cost: 0
    kind: "transform"
moveset:
  - name: "Inexperienced Power Up"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Finish Buster"
    type: "blast2"
    kiCost: 30000
    damage: 7125
    hits: 11
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "chip 1,140"
  - name: "Burning Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Explosive Wave"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Finish Buster (30,000-ki super)"
  - "Burning Attack (30,000-ki super)"
  - "Super Explosive Wave 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Super Explosive Wave on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Finish Buster 30,000-ki super, Super Explosive Wave 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

