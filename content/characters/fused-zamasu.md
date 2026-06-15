---
slug: "fused-zamasu"
name: "Fused Zamasu"
charId: "0810_01"
baseCharacter: "Zamasu"
era: "Super"
dp: 8
source: "Base"
classes:
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 15
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Fused Zamasu, Half-Corrupted"
    targetSlug: "fused-zamasu-half-corrupted"
    cost: 2
    kind: "transform"
moveset:
  - name: "This is True Justice!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Immortal Body"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Holy Wrath"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Blades of Judgment"
    type: "blast2"
    kiCost: 30000
    damage: 500
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
    notes: "chip 100"
  - name: "Lightning of Absolution"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Immortal fusion anchor"
strengths:
  - "Premium 45,000 HP fusion with double no-auto-guard buff skills (Immortal Body + This is True Justice!, 4 stock each)"
  - "Two-stock transform to the A-tier Half-Corrupted form (+5,000 HP heal)"
  - "Holy Wrath and Blades of Judgment both at 30,000 ki; Lightning of Absolution ult (50,000 ki)"
weaknesses:
  - "DP8 anchor — expensive on the budget"
  - "Average 1,750 ki recovery for the cost"
  - "Both 4-stock skills are punishable on activation"
howToFight: "Punish his 4-stock no-auto-guard buffs (Immortal Body / This is True Justice!) to deny the damage swing. Deny the 2-stock transform to Half-Corrupted. Avoid trading into 45,000 HP; use Super Counters (~2f) and starve ki to keep his ult offline."
summary: "DP8 Fused Zamasu; 45k HP, dual Immortal Body + This is True Justice! (4 stock each), 2-stock transform to A-tier Half-Corrupted."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

