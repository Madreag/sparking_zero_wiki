---
slug: "goku-z-mid-super-saiyan"
name: "Goku (Z - Mid), Super Saiyan"
charId: "0000_11"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Now I'm Angry!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
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
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Angry Kamehameha"
    type: "ultimate"
    kiCost: 50000
    damage: 12500
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Meteor Smash (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Angry Kamehameha 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the Meteor Smash rush rather than mashing into it."
summary: "DP6 Z-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Angry Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

