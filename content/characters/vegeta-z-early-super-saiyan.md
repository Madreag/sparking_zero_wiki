---
slug: "vegeta-z-early-super-saiyan"
name: "Vegeta (Z - Early), Super Saiyan"
charId: "0020_11"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - target: "Super Vegeta"
    targetSlug: "super-vegeta"
    cost: 1
    kind: "transform"
moveset:
  - name: "Awakened by Anger"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Maximum Flasher"
    type: "blast2"
    kiCost: 30000
    damage: 4560
    hits: 9
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "chip 1,140"
  - name: "Cosmic Impact"
    type: "blast2"
    kiCost: 30000
    damage: 6000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Big Bang Attack"
    type: "ultimate"
    kiCost: 50000
    damage: 12000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Maximum Flasher (30,000-ki super)"
  - "Cosmic Impact (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Big Bang Attack 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Transforms (1 stock to Super Vegeta) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Cosmic Impact rush rather than mashing into it."
summary: "DP6 Z-era fighter; 40,000 HP; Maximum Flasher 30,000-ki super, Big Bang Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

