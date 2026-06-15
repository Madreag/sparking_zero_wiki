---
slug: "goku-z-end-super-saiyan-2"
name: "Goku (Z - End), Super Saiyan 2"
charId: "0000_22"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (Z - End), Super Saiyan 3"
    targetSlug: "goku-z-end-super-saiyan-3"
    cost: 1
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Instant Transmission Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Meteor Crash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
    damage: 12500
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Instant Transmission Kamehameha (30,000-ki super)"
  - "Meteor Crash (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Kamehameha 50,000-ki ultimate finisher"
  - "Instant Transmission teleport repositioning"
  - "Full Power attack buff (4 stock)"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Meteor Crash rush rather than mashing into it."
summary: "DP6 Z-era fighter; 40,000 HP; Instant Transmission Kamehameha 30,000-ki super, Super Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

