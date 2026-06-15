---
slug: "chiaotzu"
name: "Chiaotzu"
charId: "0190_00"
baseCharacter: "Chiaotzu"
era: "Z"
dp: 2
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Telekinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Dodon Ray"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Psychic Rock Throw"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Fire"
      - "vanish: erase"
  - name: "Farewell, Mr. Tien"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
      - "You also take damage"
tier: "D"
playable: true
playstyle: "All-rounder fighter"
strengths:
  - "Dodon Ray (20,000-ki super)"
  - "Psychic Rock Throw (20,000-ki super)"
  - "Farewell, Mr. Tien 50,000-ki ultimate finisher"
  - "Telekinesis — unblockable hold"
  - "Afterimage evasive step"
weaknesses:
  - "30,000 HP — melts in roughly two combos"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Farewell, Mr. Tien on knockdown — bait it out and punish the recovery."
summary: "DP2 Z-era fighter, D-tier; 30,000 HP; Dodon Ray 20,000-ki super, Farewell, Mr. Tien 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

