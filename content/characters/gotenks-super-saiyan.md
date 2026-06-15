---
slug: "gotenks-super-saiyan"
name: "Gotenks, Super Saiyan"
charId: "0120_01"
baseCharacter: "Gotenks"
era: "Z"
dp: 7
source: "Base"
classes:
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 4
sparkingDrainPerSec: 2800
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gotenks, Super Saiyan 3"
    targetSlug: "gotenks-super-saiyan-3"
    cost: 1
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Victory Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Galactic Donuts"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "Unguardable"
      - "Played after a hit"
  - name: "Super Ghost Kamikaze Attack"
    type: "ultimate"
    kiCost: 50000
    damage: 2000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Unguardable"
    notes: "chip 212"
tier: "S"
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "45,000 HP — above-baseline bulk"
  - "Victory Cannon (30,000-ki super)"
  - "Galactic Donuts (30,000-ki super)"
  - "Super Ghost Kamikaze Attack 50,000-ki ultimate finisher"
  - "False Courage instant ki gain"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Super Ghost Kamikaze Attack on knockdown — bait it out and punish the recovery."
summary: "DP7 Z-era fusion; 45,000 HP; Victory Cannon 30,000-ki super, Super Ghost Kamikaze Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

