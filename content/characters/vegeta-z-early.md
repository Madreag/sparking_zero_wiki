---
slug: "vegeta-z-early"
name: "Vegeta (Z - Early)"
charId: "0020_10"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Z - Early), Super Saiyan"
    targetSlug: "vegeta-z-early-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Super Vegeta"
    targetSlug: "super-vegeta"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Energy Wave Combo"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Super Explosive Wave"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Galick Gun (30,000-ki super)"
  - "Super Energy Wave Combo (30,000-ki super)"
  - "Super Explosive Wave 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Full Power attack buff (4 stock)"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Super Explosive Wave on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Galick Gun 30,000-ki super, Super Explosive Wave 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

