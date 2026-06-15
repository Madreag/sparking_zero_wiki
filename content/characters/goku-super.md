---
slug: "goku-super"
name: "Goku (Super)"
charId: "0000_40"
baseCharacter: "Goku (Z - Early)"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (Super), Super Saiyan"
    targetSlug: "goku-super-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Goku (Super), Super Saiyan God"
    targetSlug: "goku-super-super-saiyan-god"
    cost: 2
    kind: "transform"
  - target: "Goku (Super), Super Saiyan God Super Saiyan"
    targetSlug: "goku-super-super-saiyan-god-super-saiyan"
    cost: 3
    kind: "transform"
  - target: "Gogeta (Super)"
    targetSlug: "gogeta-super"
    cost: 3
    kind: "fusion"
  - target: "Gogeta (Super), Super Saiyan"
    targetSlug: "gogeta-super-super-saiyan"
    cost: 4
    kind: "fusion"
  - target: "Gogeta (Super), Super Saiyan God Super Saiyan"
    targetSlug: "gogeta-super-super-saiyan-god-super-saiyan"
    cost: 5
    kind: "fusion"
  - target: "Vegito"
    targetSlug: "vegito"
    cost: 3
    kind: "fusion"
  - target: "Vegito, Super Saiyan God Super Saiyan"
    targetSlug: "vegito-super-saiyan-god-super-saiyan"
    cost: 5
    kind: "fusion"
moveset:
  - name: "All Fired Up"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Dragon Burst"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Spirit Bomb"
    type: "ultimate"
    kiCost: 50000
    damage: 14000
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Dragon Burst (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Spirit Bomb 50,000-ki ultimate finisher"
  - "Instant Transmission teleport repositioning"
  - "Transforms (1 stock to Goku (Super)) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Dragon Burst rush rather than mashing into it."
summary: "DP5 Super-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Super Spirit Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

