---
slug: "jiren"
name: "Jiren"
charId: "0930_00"
baseCharacter: "Jiren"
era: "Super"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Jiren, Full Power"
    targetSlug: "jiren-full-power"
    cost: 2
    kind: "transform"
moveset:
  - name: "Meditation"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Ki Pressure"
    type: "blast1"
    notes: "slot S1"
  - name: "Power Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Infinity Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Heat Break"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Armored counter base"
strengths:
  - "Two-stock transform to S-tier Full Power banking a huge +10,000 HP heal"
  - "Meditation S2 (4 stock) no-auto-guard buff/recovery tool"
  - "Ki Pressure S1 (free) zoning/control"
  - "Power Impact (30,000 ki) and speed-impact Infinity Rush (30,000 ki / 15,000 trigger); Heat Break ult (50,000 ki)"
weaknesses:
  - "DP8 base with only 40,000 HP until it transforms"
  - "Average 1,750 recovery; Meditation is punishable"
  - "Slower without the Full Power armor"
howToFight: "Deny the 2-stock transform to Full Power — that's a +10,000 HP swing into S-tier. Punish Meditation (4-stock, no-auto-guard). Pressure the 40,000-HP base before he ascends; he has no teleport escape."
summary: "DP8 Jiren base; 40k HP, Ki Pressure + Meditation (4 stock), Infinity Rush speed-impact; 2-stock transform to S-tier Full Power (+10,000 HP)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

