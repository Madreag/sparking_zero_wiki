---
slug: "goku-mini-super-saiyan"
name: "Goku (Mini), Super Saiyan"
charId: "3050_01"
baseCharacter: "Goku (Mini)"
era: "DAIMA"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - target: "Goku (Mini), Super Saiyan 4"
    targetSlug: "goku-mini-super-saiyan-4"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Energy Strike"
    type: "blast2"
    kiCost: 30000
    damage: 6200
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "High-Speed Strike"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mini mid-form"
strengths:
  - "Two-stock transform to the SS4 ceiling form"
  - "Afterimage S1 (free) gives a 1-hit auto-dodge read; Full Power S2 (4 stock) no-auto-guard buff"
  - "Energy Strike and High-Speed Strike both speed-impact (30,000 ki / 15,000 trigger); Super Kamehameha ult (50,000 ki)"
weaknesses:
  - "DP5 mid-form; weaker than SS4"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Afterimage is one-hit only"
howToFight: "Keep him off the 2-stock SS4 transform. Afterimage is one-hit; stagger to bait it. Punish Full Power (no-auto-guard) and pressure the 40,000-HP body."
summary: "DP5 Goku (Mini) SS; 40k HP, Afterimage + Full Power (4 stock), double speed-impact strikes; 2-stock to SS4."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

