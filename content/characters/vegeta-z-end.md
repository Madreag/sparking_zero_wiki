---
slug: "vegeta-z-end"
name: "Vegeta (Z - End)"
charId: "0020_30"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Z - End), Super Saiyan"
    targetSlug: "vegeta-z-end-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Vegeta (Z - End), Super Saiyan 2"
    targetSlug: "vegeta-z-end-super-saiyan-2"
    cost: 2
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
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Double Galick Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Energy Wave Combo"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
  - name: "Big Bang Attack"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Double Galick Cannon (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Energy Wave Combo (20,000-ki super)"
  - "Big Bang Attack 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Double Galick Cannon rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; Double Galick Cannon 30,000-ki speed-impact super, Big Bang Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

