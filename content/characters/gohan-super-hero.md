---
slug: "gohan-super-hero"
name: "Gohan (Super Hero)"
charId: "3000_00"
baseCharacter: "Gohan (Super Hero)"
era: "Movie"
dp: 4
source: "\"Heroes of Justice\" Pack"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gohan (Super Hero), Super Saiyan"
    targetSlug: "gohan-super-hero-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Ultimate Gohan (Super Hero)"
    targetSlug: "ultimate-gohan-super-hero"
    cost: 3
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High-Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
playable: true
playstyle: "Beast-access base"
strengths:
  - "Branches up to Ultimate Gohan (3 stock, +5,000 HP) on the path to S-tier Gohan Beast"
  - "Afterimage S1 (free) gives a 1-hit auto-dodge read; Full-Power Charge S2 (free) builds meter"
  - "Masenko (30,000 ki) and speed-impact High-Speed Rush (30,000 ki / 15,000 trigger); Super Kamehameha ult (50,000 ki)"
weaknesses:
  - "Fragile 35,000 HP base — dies fast before transforming"
  - "Average 1,750 recovery, no escape tool"
  - "Long climb to the payoff form"
howToFight: "Punish hard while he's the fragile 35,000-HP base — deny the stock-building toward Gohan Beast. Afterimage is one-hit; stagger to bait it. Keep him stock-starved and pressure; this is his most vulnerable state."
summary: "DP4 Gohan (SH) base; fragile 35k HP, Afterimage + Full-Power Charge, branches to Ultimate (3 stock) toward Gohan Beast."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

