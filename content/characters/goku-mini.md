---
slug: "goku-mini"
name: "Goku (Mini)"
charId: "3050_00"
baseCharacter: "Goku (Mini)"
era: "DAIMA"
dp: 4
source: "Pre-order Pack"
hp: 40000
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
  - target: "Goku (Mini), Super Saiyan"
    targetSlug: "goku-mini-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Warm-up Exercise"
    type: "blast1"
    notes: "slot S2"
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Quick Rush"
    type: "blast2"
    kiCost: 30000
    damage: 6200
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Take This!"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Power Pole Rush"
    type: "ultimate"
    kiCost: 50000
tier: "D"
playable: true
playstyle: "Mini transform base"
strengths:
  - "Cheap 1-stock transform to SS (then SS4 later)"
  - "Sleep S1 (4 stock) no-auto-guard status tool to steal a turn"
  - "Both supers speed-impact: Quick Rush and Take This! (30,000 ki / 15,000 trigger each)"
  - "Power Pole Rush ult (50,000 ki); Warm-up Exercise S2 (free) buff"
weaknesses:
  - "D-tier; weak DP4 base"
  - "Average 1,750 recovery, no escape tool"
  - "Long climb to the SS4 payoff"
howToFight: "Don't respect Sleep — block or step it, then punish the 4-stock investment. Deny the transform path toward SS4. He's D-tier with no escape; pressure freely and convert openings on the 40,000-HP base."
summary: "DP4 Goku (Mini) base; 40k HP, Sleep (4 stock) + Warm-up Exercise, double speed-impact supers; 1-stock to SS; D-tier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

