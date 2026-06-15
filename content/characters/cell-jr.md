---
slug: "cell-jr"
name: "Cell Jr."
charId: "0163_00"
baseCharacter: "Cell Jr."
era: "Z"
dp: 3
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Special Beam Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Innocence Rush"
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
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Special Beam Cannon (30,000-ki super)"
  - "Innocence Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Kamehameha 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Explosive Wave knockback/ki-shield reset"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Innocence Rush rather than mashing into it."
summary: "DP3 Z-era fighter; 35,000 HP; Special Beam Cannon 30,000-ki super, Super Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

