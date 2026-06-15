---
slug: "hirudegarn"
name: "Hirudegarn"
charId: "0670_00"
baseCharacter: "Hirudegarn"
era: "Movie"
dp: 6
source: "Base"
classes:
  - "Giant"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 40000
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Dark Eyes"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Chou Makousen"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Short-range energy attack"
      - "weak-vs-shield"
      - "vanish: erase"
  - name: "Super Explosive Wave"
    type: "blast2"
    kiCost: 40000
  - name: "Gigantic Flame"
    type: "ultimate"
    kiCost: 50000
    damage: 13000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Armored giant bruiser"
strengths:
  - "Giant-class body: oversized hitbox, super-armor moves, grab-immune"
  - "Super Explosive Wave at 40,000 ki is a large AoE clear"
  - "Dark Eyes S2 (free) for ranged control; Gigantic Flame ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal/space-maker"
weaknesses:
  - "Subject to all giant nerfs — less damage, longer whiff recovery, takes more melee, slower back-dash"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Charge Blasts now knock him back; no defensive escape skill"
howToFight: "Anti-giant fundamentals: zone with charge Blasts (they now damage and knock back giants), stay mobile, and punish his long whiff recovery. Don't grab. Keep chipping from range — his slow back-dash can't disengage from sustained zoning."
summary: "DP6 dragon-kaiju Giant; giant-class HP + armor, Super Explosive Wave 40k-ki AoE, but slow 1,500 recovery and giant-nerfed."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

