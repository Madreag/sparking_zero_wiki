---
slug: "goku-z-end-super-saiyan-3"
name: "Goku (Z - End), Super Saiyan 3"
charId: "0000_23"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
sparkingDrainPerSec: 2800
kiBlastShots: 9
skillGaugeGains:
  vanishExchangeRate: 1.1
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
  - name: "Super Dragon Twin Fists"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Dragon Fist"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "S"
playable: true
playstyle: "Rushdown finisher"
strengths:
  - "A-tier finisher form with Dragon Fist 50,000-ki homing ultimate"
  - "Super Dragon Twin Fists speed-impact rush (15,000 ki on trigger) for cheap combo extensions"
  - "Power Up to the Very Limit (4 stock) for a late attack spike; Instant Transmission for mix-ups"
  - "8.0 ki charge / 1,500/s recovery"
weaknesses:
  - "DP7 and sits at the top of a 3-stock transform ladder from base Z-End — slow and stock-hungry to reach"
  - "No auto-dodge or heal; relies on raw offense"
  - "SS3 historically drains gauge fast — limited Sparking uptime"
howToFight: "Pressure him during the transform climb; each stage costs a stock. Once in SS3, bait Dragon Fist and Super Counter (free) his rush approaches. Keep him blocking to starve the gauge."
summary: "DP7 Goku (Z-End) SS3: A-tier; 40,000 HP, 8.0 ki charge; Super Kamehameha (30,000 ki) + Dragon Fist 50,000-ki ult; top of the Z-End transform chain."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

