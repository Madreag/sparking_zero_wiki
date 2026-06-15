---
slug: "gohan-future-super-saiyan"
name: "Gohan (Future), Super Saiyan"
charId: "0032_31"
baseCharacter: "Gohan (Adult)"
era: "Z"
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
moveset:
  - name: "Power Up to the Very Limit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Evil Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Hyper Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Special Beam Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "Chargeable"
  - name: "Fierce Combination"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Hyper Masenko (30,000-ki super)"
  - "Special Beam Cannon (30,000-ki super)"
  - "Fierce Combination 50,000-ki ultimate finisher"
  - "Evil Barrier guard (3 stock)"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Fierce Combination on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Hyper Masenko 30,000-ki super, Fierce Combination 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

