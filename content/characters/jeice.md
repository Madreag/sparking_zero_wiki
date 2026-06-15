---
slug: "jeice"
name: "Jeice"
charId: "0410_00"
baseCharacter: "Jeice"
era: "Z"
dp: 3
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
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
  - name: "SP Fighting Pose 3"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Crusher Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Purple Comet Attack"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Full-Power Energy Wave (30,000-ki super)"
  - "Crusher Ball (30,000-ki super)"
  - "Purple Comet Attack 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "DP3 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Purple Comet Attack on knockdown — bait it out and punish the recovery."
summary: "DP3 Z-era fighter; 40,000 HP; Full-Power Energy Wave 30,000-ki super, Purple Comet Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

