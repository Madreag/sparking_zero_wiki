---
slug: "super-vegeta"
name: "Super Vegeta"
charId: "0021_20"
baseCharacter: "Super Vegeta"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
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
  - target: "Vegeta (Z - Early)"
    targetSlug: "vegeta-z-early"
    cost: 0
    kind: "transform"
moveset:
  - name: "I am Super Vegeta!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Big Bang Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Spirit Breaking Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Final Flash"
    type: "ultimate"
    kiCost: 50000
    damage: 13000
tier: "A"
playable: true
playstyle: "Rushdown bruiser"
strengths:
  - "B-tier bruiser; Spirit Breaking Cannon speed-impact rush (15,000 ki on trigger) for cheap extensions"
  - "Final Flash 50,000-ki ultimate charge beam; Big Bang Attack 30,000-ki super"
  - "I am Super Vegeta! (4 stock) attack buff; Explosive Wave reset"
  - "40,000 HP / 8.0 ki charge"
weaknesses:
  - "DP6 with no auto-dodge — defense is Super Counter only"
  - "Reached as a transform from Z-Early Vegeta"
  - "Outclassed by higher forms; no heal"
howToFight: "Super Counter (free) his rushes and vanish the Spirit Breaking Cannon. Bait I am Super Vegeta! then pressure. Respect the Final Flash on knockdown."
summary: "DP6 Super Vegeta (Z): B-tier; 40,000 HP, 8.0 ki charge; Big Bang Attack (30,000 ki) + Spirit Breaking Cannon speed-impact (15,000 on trigger) + Final Flash 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

