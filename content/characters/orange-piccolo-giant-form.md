---
slug: "orange-piccolo-giant-form"
name: "Orange Piccolo, Giant Form"
charId: "3012_00"
baseCharacter: "Orange Piccolo"
era: "Movie"
dp: 8
source: "Base"
classes:
  - "Giant"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Orange Piccolo"
    targetSlug: "orange-piccolo"
    cost: 0
    kind: "transform"
moveset:
  - name: "Behave Yourself!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Chou Makouhou"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Mighty Fist"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
  - name: "Apocalyptic Burst"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Armored giant form"
strengths:
  - "Giant-class: oversized hitbox, super-armor, grab-immune, big HP"
  - "Mighty Fist super at 40,000 ki is a heavy armored hit; Chou Makouhou (30,000 ki) AoE"
  - "Behave Yourself! S2 (4 stock) no-auto-guard buff; Apocalyptic Burst ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "Subject to all giant nerfs — less damage, longer whiff recovery, takes more melee, slower back-dash"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Charge Blasts now knock him back; reverts to standard Orange (0 stock)"
howToFight: "Zone it: charge Blasts now damage and knock back giants, so chip from range and stay mobile. Bait Mighty Fist or an armored swing and punish the long whiff recovery. Don't grab. He'll often revert to the 45,000-HP standard Orange — be ready to switch back to melee pressure."
summary: "DP8 Orange Piccolo Giant Form; null-HP giant, Behave Yourself! (4 stock) + Mighty Fist 40k-ki, but giant-nerfed."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

