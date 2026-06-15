---
slug: "babidi"
name: "Babidi"
charId: "0490_00"
baseCharacter: "Babidi"
era: "Z"
dp: 3
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
initialKi: 30000
maxSkillStock: 7
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.3
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Wizard Barrier"
    type: "blast1"
    notes: "slot S2"
  - name: "Demon Eye"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Pui Pui Nice Shot"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Ultimate Explosive Power"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Attack opponent's location"
  - name: "Super Electroshock Sorcery"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Short-range energy attack"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Pui Pui Nice Shot (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Ultimate Explosive Power (40,000-ki super)"
  - "Super Electroshock Sorcery 50,000-ki ultimate finisher"
  - "Demon Eye — unblockable control"
  - "DP3 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "30,000 HP — melts in roughly two combos"
  - "Slow 6 ki charge — sluggish to fund supers"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Pressure his slow 6 ki charge by forcing blocks so he can't reach his supers. Perception (2 stock) or vanish the Pui Pui Nice Shot rush rather than mashing into it."
summary: "DP3 Z-era fighter; 30,000 HP; Ultimate Explosive Power 40,000-ki super, Super Electroshock Sorcery 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

