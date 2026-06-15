---
slug: "anilaza"
name: "Anilaza"
charId: "1500_00"
baseCharacter: "Anilaza"
era: "Super"
dp: 8
source: "Base"
classes:
  - "Giant"
  - "Fusion"
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
moveset:
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Ultrasonic Sensor"
    type: "blast1"
    notes: "slot S1"
  - name: "Warp Punch"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Played after a hit"
    notes: "Trigger cost 20,000 ki"
  - name: "Spread Energy Blast"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
  - name: "Destruction Burst"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Armored giant fusion"
strengths:
  - "Giant-class fusion: oversized hitbox, super-armor, grab-immune, big HP"
  - "Warp Punch super at 40,000 ki (20,000 trigger) is a long-range armored catch"
  - "Spread Energy Blast (30,000 ki) AoE; Destruction Burst ult (50,000 ki)"
  - "Ultrasonic Sensor S1 (free) tracking/control tool"
weaknesses:
  - "Hit by all May-2026 giant nerfs: less damage, longer whiff recovery, takes more melee, slower back-dash"
  - "Average 1,750 recovery for a DP8 giant; charge Blasts now knock him back"
  - "Howl (4 stock) buff is punishable; no teleport"
howToFight: "Anti-giant fundamentals: charge Blasts now damage and knock him back, so zone and stay mobile. Bait a Warp Punch or armored swing and punish the long whiff recovery. Don't grab; out-space his slow back-dash and chip him down from range."
summary: "DP8 Anilaza Giant fusion; null-HP, super-armor body, Warp Punch 40k-ki + Spread Energy Blast, but broadly giant-nerfed."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

