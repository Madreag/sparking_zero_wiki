---
slug: "guldo"
name: "Guldo"
charId: "0420_00"
baseCharacter: "Guldo"
era: "Z"
dp: 2
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 1
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
  - name: "SP Fighting Pose 4"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Paralysis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Psychic Rock Throw"
    type: "blast2"
    kiCost: 30000
    properties:
      - "vanish: erase"
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Guldo Special"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
tier: "D"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Psychic Rock Throw (30,000-ki super)"
  - "Full-Power Energy Blast Volley (30,000-ki super)"
  - "Guldo Special 50,000-ki ultimate finisher"
  - "Paralysis — unblockable stun"
  - "DP2 — dirt-cheap DP-queue body; frees budget for a premium carry"
weaknesses:
  - "30,000 HP — melts in roughly two combos"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Guldo Special on knockdown — bait it out and punish the recovery."
summary: "DP2 Z-era fighter, D-tier; 30,000 HP; Psychic Rock Throw 30,000-ki super, Guldo Special 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

