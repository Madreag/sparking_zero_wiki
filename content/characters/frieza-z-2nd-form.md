---
slug: "frieza-z-2nd-form"
name: "Frieza (Z), 2nd Form"
charId: "0151_00"
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
kiBlastShots: 5
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Frieza (Z), 3rd Form"
    targetSlug: "frieza-z-3rd-form"
    cost: 1
    kind: "transform"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Punishing Blaster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
  - name: "Death Storm"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Attack opponent's location"
  - name: "HAIL Frieza"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Punishing Blaster (30,000-ki super)"
  - "Death Storm (40,000-ki super)"
  - "HAIL Frieza 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Transforms (1 stock to Frieza (Z), heals 5,000 HP on the change) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect HAIL Frieza on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Death Storm 40,000-ki super, HAIL Frieza 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

