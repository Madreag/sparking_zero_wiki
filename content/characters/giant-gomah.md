---
slug: "giant-gomah"
name: "Giant Gomah"
charId: "3150_00"
baseCharacter: "Giant Gomah"
era: "DAIMA"
dp: 8
source: "Dragon Ball DAIMA Character Pack 2"
classes:
  - "Giant"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
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
moveset:
  - name: "Third Eye Enhance"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Third Eye Heal"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Magic Missile"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    properties:
      - "weak-vs-shield"
  - name: "Magic Tempest"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Explosive Wave"
      - "Played after a hit"
  - name: "Giga Magic Burst"
    type: "ultimate"
    kiCost: 50000
    damage: 12000
playable: true
playstyle: "Self-healing giant"
strengths:
  - "Giant-class: oversized hitbox, super-armor, grab-immune, big HP"
  - "Two no-auto-guard support skills: Third Eye Heal and Third Eye Enhance (4 stock each) — rare giant sustain/buff"
  - "Magic Missile (30,000 ki) and Magic Tempest (40,000 ki); Giga Magic Burst ult (50,000 ki)"
weaknesses:
  - "Subject to all giant nerfs — less damage, longer whiff recovery, takes more melee, slower back-dash"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Both 4-stock support skills are punishable; charge Blasts knock him back"
howToFight: "Anti-giant zoning: charge Blasts now damage and knock him back, so chip from range and stay mobile. Punish his 4-stock Third Eye Heal/Enhance animations to deny sustain and buffs. Don't grab; bait an armored swing and punish the long whiff recovery."
summary: "DP8 Giant Gomah; null-HP giant, dual Third Eye Heal/Enhance (4 stock each), Magic Tempest 40k-ki; giant-nerfed."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

