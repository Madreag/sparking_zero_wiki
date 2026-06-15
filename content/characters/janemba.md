---
slug: "janemba"
name: "Janemba"
charId: "0650_00"
baseCharacter: "Janemba"
era: "Movie"
dp: 5
source: "Base"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 2
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Super Janemba"
    targetSlug: "super-janemba"
    cost: 3
    kind: "transform"
moveset:
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Mystic Breath"
    type: "blast1"
    skillCost: 1
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Chou Makouhou"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Rapid Cannon"
    type: "blast2"
    kiCost: 30000
    damage: 838
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
    notes: "chip 210"
  - name: "Illusion Smash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
tier: "C"
playable: true
playstyle: "Unblockable-poke base"
strengths:
  - "Mystic Breath S1 is unblockable + no-auto-guard for only 1 stock — cheap stun opener"
  - "Transforms to Super Janemba for 3 stocks (powerful payoff form)"
  - "Chou Makouhou and Rapid Cannon both at 30,000 ki"
  - "Howl S2 (4 stock) no-auto-guard buff; Illusion Smash ult (50,000 ki)"
weaknesses:
  - "DP5 base is C-tier; you want Super Janemba"
  - "Slow 1,500 ki recovery and 8.0 charge"
  - "Transform gated behind 3 stocks"
howToFight: "Vanish (≈half a ki bar) the cheap unblockable Mystic Breath rather than guarding. Deny the 3-stock transform to Super Janemba by pressuring through his stock-building. He has no defensive escape in base — keep your turn."
summary: "DP5 Janemba base; giant-ish (null HP), unblockable Mystic Breath (1 stock), 3-stock transform to Super Janemba; C-tier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

