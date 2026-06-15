---
slug: "kid-buu"
name: "Kid Buu"
charId: "0173_00"
baseCharacter: "Kid Buu"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
initialKi: 30000
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Mystic Combination"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Planet Burst"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
dpTier: "D"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Mystic Combination (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Planet Burst 50,000-ki ultimate finisher"
  - "Instant Transmission teleport repositioning"
weaknesses:
  - "Slow 6 ki charge — sluggish to fund supers"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Pressure his slow 6 ki charge by forcing blocks so he can't reach his supers. Perception (2 stock) or vanish the Mystic Combination rush rather than mashing into it."
summary: "DP7 Z-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Planet Burst 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

