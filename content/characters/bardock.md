---
slug: "bardock"
name: "Bardock"
charId: "0310_00"
baseCharacter: "Bardock"
era: "Z"
dp: 4
source: "Martial Arts Pack"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Shockwave of Rebellion"
    type: "blast1"
    skillCost: 5
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Riot Blaster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Final Revenger"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Final Spirit Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "D"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Riot Blaster (30,000-ki super)"
  - "Final Revenger (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Final Spirit Cannon 50,000-ki ultimate finisher"
  - "Saiyan Spirit ki/attack buff"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Final Revenger rush rather than mashing into it."
summary: "DP4 Z-era fighter, D-tier; 40,000 HP; Riot Blaster 30,000-ki super, Final Spirit Cannon 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

