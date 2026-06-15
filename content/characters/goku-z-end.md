---
slug: "goku-z-end"
name: "Goku (Z - End)"
charId: "0000_20"
baseCharacter: "Goku (Z - Early)"
era: "Z"
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
  - target: "Goku (Z - End), Super Saiyan"
    targetSlug: "goku-z-end-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Goku (Z - End), Super Saiyan 2"
    targetSlug: "goku-z-end-super-saiyan-2"
    cost: 2
    kind: "transform"
  - target: "Goku (Z - End), Super Saiyan 3"
    targetSlug: "goku-z-end-super-saiyan-3"
    cost: 3
    kind: "transform"
  - target: "Super Gogeta (Z) "
    targetSlug: "super-gogeta-z"
    cost: 4
    kind: "fusion"
  - target: "Vegito"
    targetSlug: "vegito"
    cost: 3
    kind: "fusion"
  - target: "Super Vegito"
    targetSlug: "super-vegito"
    cost: 4
    kind: "fusion"
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Meteor Smash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Spirit Bomb"
    type: "ultimate"
    kiCost: 50000
    damage: 13500
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Meteor Smash (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Spirit Bomb 50,000-ki ultimate finisher"
  - "Instant Transmission teleport repositioning"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the Meteor Smash rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; Kamehameha 30,000-ki super, Super Spirit Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

