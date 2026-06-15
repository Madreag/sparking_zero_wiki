---
slug: "super-zarbon"
name: "Super Zarbon"
charId: "0351_00"
baseCharacter: "Super Zarbon"
era: "Z"
dp: 3
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Zarbon"
    targetSlug: "zarbon"
    cost: 0
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Elegant Blaster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Wild Pressure"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Monster Crush"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
dpTier: "Z"
dpScore: 24.5
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Elegant Blaster (30,000-ki super)"
  - "Wild Pressure (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Monster Crush 50,000-ki ultimate finisher"
  - "False Courage instant ki gain"
  - "High-Tension self ki-charge buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Wild Pressure rush rather than mashing into it."
summary: "DP3 Z-era fighter; 40,000 HP; Elegant Blaster 30,000-ki super, Monster Crush 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

