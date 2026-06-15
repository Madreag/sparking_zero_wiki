---
slug: "dodoria"
name: "Dodoria"
charId: "0360_00"
baseCharacter: "Dodoria"
era: "Z"
dp: 3
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Chou Makouhou"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Dodoria Head Ram"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
      - "speed-impact"
  - name: "Maximum Buster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
dpTier: "S"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Chou Makouhou (30,000-ki super)"
  - "Dodoria Head Ram (40,000-ki super, speed-impact rush)"
  - "Maximum Buster 50,000-ki ultimate finisher"
  - "False Courage instant ki gain"
  - "Pump Up defense buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Dodoria Head Ram rush rather than mashing into it."
summary: "DP3 Z-era fighter; 40,000 HP; Dodoria Head Ram 40,000-ki speed-impact super, Maximum Buster 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

