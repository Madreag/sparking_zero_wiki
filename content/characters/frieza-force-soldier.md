---
slug: "frieza-force-soldier"
name: "Frieza Force Soldier"
charId: "0540_00"
baseCharacter: "Frieza Force Soldier"
era: "Z"
dp: 2
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 2
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S1"
  - name: "Energy Wave"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Life-Risking Blow!"
    type: "ultimate"
    kiCost: 50000
    damage: 12000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
playable: true
playstyle: "Cheap throwaway body"
strengths:
  - "DP2 cost makes him near-free filler in a 15-DP team"
  - "Fast 8.0 ki-charge speed feeds his cheap 20,000-ki Energy Wave spam"
  - "Sleep S2 (4 stock) is a no-auto-guard status tool that can steal a turn"
  - "Life-Risking Blow! ult at 50,000 ki is a surprise burst from a 2-DP body"
weaknesses:
  - "Rock-bottom 30,000 HP — dies to a single confirmed combo in DP scaling"
  - "Only 1,500 ki recovery; can't sustain pressure"
  - "No transform, no mobility tool, weak normals — a body, not a threat"
howToFight: "Treat him as free damage: he has 30,000 HP and folds to any Smash combo. Don't respect Sleep — block low or step it. There's nothing to fear defensively; just open him up and convert one full combo to remove the slot."
summary: "DP2 fodder soldier; only 30,000 HP (lowest tier) and fast 8.0 ki-charge but no transform — pure DP-filler body."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

