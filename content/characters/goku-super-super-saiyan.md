---
slug: "goku-super-super-saiyan"
name: "Goku (Super), Super Saiyan"
charId: "0000_41"
baseCharacter: "Goku (Z - Early)"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
transformsTo:
  - target: "Goku (Super), Super Saiyan God"
    targetSlug: "goku-super-super-saiyan-god"
    cost: 1
    kind: "transform"
  - target: "Goku (Super), Super Saiyan God Super Saiyan"
    targetSlug: "goku-super-super-saiyan-god-super-saiyan"
    cost: 2
    kind: "transform"
moveset:
  - name: "All-Encompassing Power"
    type: "blast1"
    skillCost: 3
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
  - name: "Dragon Blast"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Sonic Blast"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Dragon Blast (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Sonic Blast 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "Transforms (1 stock to Goku (Super)) for a mid-match power spike"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the Dragon Blast rush rather than mashing into it."
summary: "DP6 Super-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Sonic Blast 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

