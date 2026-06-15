---
slug: "master-roshi-max-power"
name: "Master Roshi, Max Power"
charId: "0141_00"
baseCharacter: "Master Roshi"
era: "DB"
dp: 2
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
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
transformsTo:
  - target: "Master Roshi"
    targetSlug: "master-roshi"
    cost: 0
    kind: "transform"
moveset:
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Original Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Turtle School Ultimate Fist"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Max Power Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "D"
playable: true
playstyle: "DP-value bruiser"
strengths:
  - "DP-efficiency S-tier (31.2k points-per-DP) — overperforms its DP2 cost massively in the DP queue"
  - "40,000 HP in this form (up from 30k base) plus Turtle School Ultimate Fist speed-impact rush (15,000 on trigger)"
  - "Max Power Kamehameha 50,000-ki ultimate; Pump Up defensive buff"
  - "DP2 — frees budget for a premium carry"
weaknesses:
  - "Ki-recovery nerfed May 2026 — expect a downward drift on the next DP list"
  - "D-tier in Singles: standardized HP erases the tank value that makes him good in DP"
  - "No auto-dodge in this form; transform-locked off the fragile 30k base"
howToFight: "In Singles ignore his DP reputation — out-damage the 40k body normally. In DP, end the round fast before the cheap value snowballs. He has no evasion here, so Super Counter (free) and vanish punish his rushes."
summary: "DP2 Roshi (Max Power): D-tier Singles but DP-efficiency S-tier (sparkingzerometa 31.2k points-per-DP); 40,000 HP; Max Power Kamehameha 50,000-ki ult; Ki recovery nerfed May 2026."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

