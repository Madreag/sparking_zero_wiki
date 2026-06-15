---
slug: "goten"
name: "Goten"
charId: "0090_00"
baseCharacter: "Goten"
era: "Z"
dp: 4
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goten, Super Saiyan"
    targetSlug: "goten-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Gotenks"
    targetSlug: "gotenks"
    cost: 2
    kind: "fusion"
  - target: "Gotenks, Super Saiyan"
    targetSlug: "gotenks-super-saiyan"
    cost: 3
    kind: "fusion"
  - target: "Gotenks, Super Saiyan 3"
    targetSlug: "gotenks-super-saiyan-3"
    cost: 4
    kind: "fusion"
moveset:
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Boulder Toss Barrage"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
  - name: "Charge!"
    type: "blast2"
    kiCost: 20000
    damage: 5700
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
  - name: "Super Kamekameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Boulder Toss Barrage (20,000-ki super)"
  - "Charge! (20,000-ki super, speed-impact rush)"
  - "Super Kamekameha 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Charge! rush rather than mashing into it."
summary: "DP4 Z-era fighter; 35,000 HP; Boulder Toss Barrage 20,000-ki super, Super Kamekameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

