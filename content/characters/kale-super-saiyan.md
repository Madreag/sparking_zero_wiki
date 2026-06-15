---
slug: "kale-super-saiyan"
name: "Kale, Super Saiyan"
charId: "0912_00"
baseCharacter: "Kale"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Kale"
    targetSlug: "kale"
    cost: 0
    kind: "transform"
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Resistance Blast"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Explosive Wave"
    type: "blast2"
    kiCost: 40000
  - name: "Limit Break Blaster"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mid-form Saiyan"
strengths:
  - "Wild Sense S1 (free) 1-hit auto-dodge + Saiyan Spirit S2 (free) charge"
  - "Reverts to base (0 stock) to re-access the 3-stock Berserk transform"
  - "Resistance Blast (30,000 ki) and Super Explosive Wave (40,000 ki); Limit Break Blaster ult (50,000 ki)"
weaknesses:
  - "DP6 controlled SS form — weaker than the Berserk payoff"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "This is the calmer SS form — she'll likely revert and re-transform toward Berserk, so deny her the meter. Wild Sense is one-hit; stagger to bait it. Pressure the 40,000-HP body and keep stocks low."
summary: "DP6 Kale SS; 40k HP, Wild Sense + Saiyan Spirit, Super Explosive Wave 40k-ki; control form en route to Berserk."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

