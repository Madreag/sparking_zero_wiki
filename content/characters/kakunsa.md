---
slug: "kakunsa"
name: "Kakunsa"
charId: "1331_00"
baseCharacter: "Kakunsa"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Maiden's Fury"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Primal Charge"
    type: "blast2"
    kiCost: 40000
    damage: 5000
    properties:
      - "Rush"
      - "Unguardable"
      - "speed-impact"
  - name: "Primal Instinct"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Love Symphony"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Beast-mode skirmisher"
strengths:
  - "Wild Sense S1 (free) gives a 1-hit auto-dodge counter"
  - "Both supers speed-impact: Primal Charge (40,000 ki) and Primal Instinct (30,000 ki / 15,000 trigger)"
  - "Maiden's Fury S2 (4 stock) no-auto-guard buff; Love Symphony ult (50,000 ki)"
weaknesses:
  - "DP5 with no transform — low ceiling"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "Wild Sense is a single-hit read — stagger to bait it, then punish. Punish Maiden's Fury (no-auto-guard). Block the speed-impact supers and apply steady pressure; she has no escape tool."
summary: "DP5 Kakunsa; 40k HP, Wild Sense + Maiden's Fury (4 stock), double speed-impact supers + Love Symphony ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

