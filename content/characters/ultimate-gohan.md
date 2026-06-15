---
slug: "ultimate-gohan"
name: "Ultimate Gohan"
charId: "0032_20"
baseCharacter: "Gohan (Adult)"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 9
skillGaugeGains:
  vanishExchangeRate: 1.1
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
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Fierce Combination"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Burst Rush"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "A"
playable: true
playstyle: "Rushdown all-rounder"
strengths:
  - "B-tier rushdown with Burst Rush 50,000-ki ultimate and Fierce Combination speed-impact rush (15,000 on trigger)"
  - "Wild Sense evasion plus Power Up to the Very Limit (4 stock) damage spike"
  - "Mystic power — no transform needed, full kit from the start"
  - "40,000 HP baseline"
weaknesses:
  - "DP7 and 7.0 ki charge — slower super access than the 8.0-charge sluggers"
  - "Wild Sense was gutted Dec 2025; no heal"
  - "Outclassed at the top by fusion speed"
howToFight: "Bait Wild Sense then punish — it's his only evasion. Super Counter (free) the Fierce Combination rush and vanish the Super Kamehameha. Pressure his 7.0 ki charge by forcing blocks."
summary: "DP7 Ultimate Gohan: B-tier; 40,000 HP; Super Kamehameha (30,000 ki) + Burst Rush 50,000-ki ult; Wild Sense + Power Up to the Very Limit (4 stock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

