---
slug: "kale"
name: "Kale"
charId: "0910_00"
baseCharacter: "Kale"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "60,000 Zeni (shop)"
transformsTo:
  - target: "Kale, Super Saiyan (Berserk)"
    targetSlug: "kale-super-saiyan-berserk"
    cost: 3
    kind: "transform"
  - target: "Kale, Super Saiyan"
    targetSlug: "kale-super-saiyan"
    cost: 2
    kind: "transform"
  - target: "Kefla"
    targetSlug: "kefla"
    cost: 2
    kind: "fusion"
  - target: "Kefla, Super Saiyan"
    targetSlug: "kefla-super-saiyan"
    cost: 3
    kind: "fusion"
  - target: "Kefla, Super Saiyan 2"
    targetSlug: "kefla-super-saiyan-2"
    cost: 4
    kind: "fusion"
moveset:
  - name: "Going Berserk"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S1"
  - name: "Resistance Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Resistance Blast"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Berserk-access Saiyan"
strengths:
  - "Three-stock transform to the S-tier Berserk form (+5,000 HP heal); also a no-heal 2-stock SS branch"
  - "Going Berserk S2 (4 stock) no-auto-guard ramp sets up the payoff"
  - "Potara-fuses with Caulifla into Kefla (2-4 stock variants)"
  - "Resistance Cannon (30,000 ki) and Full-Power Energy Blast Volley (30,000 ki); Resistance Blast ult (50,000 ki)"
weaknesses:
  - "DP5 base is fragile; you race to Berserk"
  - "Average 1,750 recovery, no escape tool"
  - "Transform gated behind stock"
howToFight: "Deny the 3-stock transform to S-tier Berserk and watch for the Kefla Potara. Punish Going Berserk (no-auto-guard). Keep her stock-starved — the base has no defensive escape and folds to a sustained turn."
summary: "DP5 Kale base; 40k HP, Going Berserk (4 stock), 3-stock transform to S-tier Berserk; Potara into Kefla."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

