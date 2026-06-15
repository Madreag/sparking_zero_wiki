---
slug: "yamcha"
name: "Yamcha"
charId: "0060_00"
baseCharacter: "Yamcha"
era: "Z"
dp: 3
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
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
  - name: "Power Up to the Very Limit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Wolf Fang Fist"
    type: "blast2"
    kiCost: 30000
    damage: 6700
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Spirit Ball"
    type: "ultimate"
    kiCost: 50000
    damage: 12000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Wolf Fang Fist (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Spirit Ball 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "DP3 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Wolf Fang Fist rush rather than mashing into it."
summary: "DP3 Z-era fighter; 35,000 HP; Kamehameha 30,000-ki super, Spirit Ball 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

