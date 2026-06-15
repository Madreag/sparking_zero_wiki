---
slug: "ultimate-gohan-super-hero"
name: "Ultimate Gohan (Super Hero)"
charId: "3000_02"
baseCharacter: "Gohan (Super Hero)"
era: "Movie"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Gohan Beast"
    targetSlug: "gohan-beast"
    cost: 3
    kind: "transform"
moveset:
  - name: "The Power to Rise Again"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Bullet"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Super Explosive Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Explosive Onslaught"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Revival pre-Beast form"
strengths:
  - "The Power to Rise Again S2 (free) is a revival/comeback tool"
  - "Three-stock transform to S-tier Gohan Beast (+10,000 HP heal)"
  - "Wild Sense S1 (free) 1-hit auto-dodge"
  - "Explosive Bullet (30,000 ki) and speed-impact Super Explosive Rush (30,000 ki / 15,000 trigger); Explosive Onslaught ult (50,000 ki)"
weaknesses:
  - "DP8 with only 40,000 HP — fragile for the cost"
  - "Average 1,750 recovery, no teleport"
  - "Transform gated behind 3 stocks"
howToFight: "Deny the 3-stock transform to S-tier Gohan Beast — that's a +10,000 HP swing. Wild Sense is one-hit; stagger to bait it. Account for The Power to Rise Again revival when you think you've closed the round; burst through it and starve his stocks."
summary: "DP8 Ultimate Gohan (SH); 40k HP, Wild Sense + The Power to Rise Again (revival), Super Explosive Rush speed-impact; 3-stock to Gohan Beast."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

