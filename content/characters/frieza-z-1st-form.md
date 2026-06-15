---
slug: "frieza-z-1st-form"
name: "Frieza (Z), 1st Form"
charId: "0150_00"
baseCharacter: "Frieza (Z)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Frieza (Z), 2nd Form"
    targetSlug: "frieza-z-2nd-form"
    cost: 1
    kind: "transform"
moveset:
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Punishing Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Death Ball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Death Beam (20,000-ki super)"
  - "Punishing Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Death Ball 50,000-ki ultimate finisher"
  - "Psychokinesis — unblockable hold"
  - "Pump Up defense buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Punishing Rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; Punishing Rush 30,000-ki speed-impact super, Death Ball 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

