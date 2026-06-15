---
slug: "super-baby-2-gt"
name: "Super Baby 2 (GT)"
charId: "0680_02"
baseCharacter: "Baby Vegeta (GT)"
era: "GT"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Great Ape Baby (GT)"
    targetSlug: "great-ape-baby-gt"
    cost: 3
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Final Flash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Revenge Cutter"
    type: "blast2"
    kiCost: 30000
    damage: 1667
    hits: 2
    properties:
      - "Fire"
      - "Unguardable"
    notes: "chip 333"
  - name: "Revenge Death Ball"
    type: "ultimate"
    kiCost: 50000
    damage: 11000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Pre-giant bruiser"
strengths:
  - "Three-stock transform to Great Ape Baby banking a huge +10,000 HP heal"
  - "Full Power S2 (4 stock) no-auto-guard buff raises damage"
  - "Final Flash (30,000 ki) and Revenge Cutter (30,000 ki); Revenge Death Ball ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP7 with only 40,000 HP — fragile until it apes out"
  - "Slow 1,500 ki recovery"
  - "Transform gated behind 3 stocks; punishable Full Power"
howToFight: "Deny the 3-stock Great Ape transform — that's the payoff and the +10,000 HP swing. Punish Full Power (no-auto-guard). Keep him stock-starved; the 40,000-HP human form has no escape and dies to pressure before it can ape out."
summary: "DP7 Super Baby 2; 40k HP, Full Power (4 stock) buff, Revenge Cutter; 3-stock transform to Great Ape Baby (+10,000 HP)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

