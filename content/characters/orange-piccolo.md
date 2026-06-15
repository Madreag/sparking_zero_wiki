---
slug: "orange-piccolo"
name: "Orange Piccolo"
charId: "3011_00"
baseCharacter: "Orange Piccolo"
era: "Movie"
dp: 8
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Orange Piccolo, Giant Form"
    targetSlug: "orange-piccolo-giant-form"
    cost: 2
    kind: "transform"
  - target: "Piccolo (Super Hero)"
    targetSlug: "piccolo-super-hero"
    cost: 0
    kind: "transform"
moveset:
  - name: "That Shenron..."
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Demon Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Fierce Fist"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "Trigger cost 15,000 ki"
  - name: "Special Beam Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "A"
playable: true
playstyle: "Buffing armor anchor"
strengths:
  - "Premium 45,000 HP A-tier anchor with a strong buff/zone kit"
  - "That Shenron... S2 (4 stock) no-auto-guard buff for big damage; Pump Up S1 (free) self-amp"
  - "Two-stock transform to the Giant Form for armor/AoE swings"
  - "Explosive Demon Wave (30,000 ki) and speed-impact Fierce Fist (30,000 ki / 15,000 trigger); Special Beam Cannon ult (50,000 ki)"
weaknesses:
  - "DP8 anchor — expensive on the budget"
  - "Average 1,750 ki recovery for the cost"
  - "Giant Form inherits the May-2026 giant nerfs"
howToFight: "Punish That Shenron... (4-stock, no-auto-guard) to deny his spike. If he goes Giant Form, switch to anti-giant zoning (charge Blasts knock back giants). Avoid trading into 45,000 HP; use ~2f Super Counters and starve ki to keep his ult offline."
summary: "DP8 Orange Piccolo; 45k HP, Pump Up + That Shenron... (4 stock), Fierce Fist speed-impact; A-tier, can go Giant Form (2 stock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

