---
slug: "saibaman"
name: "Saibaman"
charId: "0330_00"
baseCharacter: "Saibaman"
era: "Z"
dp: 2
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 3
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
  - name: "Acid"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Saibaman Bomb"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
      - "You also take damage"
tier: "D"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Full-Power Energy Wave (30,000-ki super)"
  - "High Speed Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Saibaman Bomb 50,000-ki ultimate finisher"
  - "Acid — unblockable debuff"
  - "Afterimage evasive step"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the High Speed Rush rather than mashing into it."
summary: "DP2 Z-era fighter, D-tier; 35,000 HP; Full-Power Energy Wave 30,000-ki super, Saibaman Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

