---
slug: "roasie"
name: "Roasie"
charId: "1341_00"
baseCharacter: "Roasie"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 15
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Maiden's Fury"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S1"
  - name: "Yatchaina Fist"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Love Symphony"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Maiden brawler"
strengths:
  - "Full-Power Charge S1 (free) builds meter"
  - "Maiden's Fury S2 (4 stock) no-auto-guard buff raises output"
  - "Yatchaina Fist and Full-Power Energy Blast Volley both at 30,000 ki; Love Symphony ult (50,000 ki)"
  - "Standard 40,000 HP and 1,750 recovery"
weaknesses:
  - "DP5 with no transform — low ceiling"
  - "Average recovery, no mobility tool"
  - "Plain neutral; outclassed by transformers"
howToFight: "Nothing exotic — pressure her. Punish Maiden's Fury (no-auto-guard). Deny ki to keep the ult offline; with no escape tool she can't break a sustained turn."
summary: "DP5 Roasie; 40k HP, Full-Power Charge + Maiden's Fury (4 stock), twin 30k-ki supers + Love Symphony ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

