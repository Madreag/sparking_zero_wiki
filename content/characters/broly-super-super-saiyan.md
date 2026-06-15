---
slug: "broly-super-super-saiyan"
name: "Broly (Super), Super Saiyan"
charId: "0554_00"
baseCharacter: "Broly (Super)"
era: "Movie"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Broly (Super), Super Saiyan (Full Power)"
    targetSlug: "broly-super-super-saiyan-full-power"
    cost: 2
    kind: "transform"
moveset:
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S1"
  - name: "Gigantic Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gigantic Rage"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Gigantic Ball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Mid-form armor bruiser"
strengths:
  - "Cheaper 2-stock transform to SS Full Power (+5,000 HP heal) from this form"
  - "Gigantic Cannon (30,000 ki) and Gigantic Rage (30,000 ki / 15,000 trigger, speed-impact) cover range and rush"
  - "Howl S2 (4 stock) is a no-auto-guard intimidation buff"
  - "Saiyan Spirit S1 charges for free"
weaknesses:
  - "DP7, still 40,000 HP — no durability gain over base for the cost"
  - "Transitional form; the payoff is the next transform"
  - "No teleport; predictable approach"
howToFight: "He is one 2-stock transform from S-tier Full Power — interrupt and keep him stock-starved. Gigantic Ball ult costs 50,000 ki; deny the meter. Step his speed-impact Gigantic Rage and punish whiffed Howl activations."
summary: "DP7 Broly (Super) SS; 40k HP, Howl (4 stock) buff, Gigantic Rage speed-impact; 2-stock step to SS Full Power."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

