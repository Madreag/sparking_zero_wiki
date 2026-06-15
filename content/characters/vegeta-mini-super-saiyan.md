---
slug: "vegeta-mini-super-saiyan"
name: "Vegeta (Mini), Super Saiyan"
charId: "3060_01"
baseCharacter: "Vegeta (Mini)"
era: "DAIMA"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Mini), Super Saiyan 2"
    targetSlug: "vegeta-mini-super-saiyan-2"
    cost: 1
    kind: "transform"
  - target: "Vegeta (Mini), Super Saiyan 3"
    targetSlug: "vegeta-mini-super-saiyan-3"
    cost: 2
    kind: "transform"
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Overpowering Crush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Galick Gun"
    type: "ultimate"
    kiCost: 50000
dpTier: "S"
playable: true
playstyle: "Mini mid-ladder"
strengths:
  - "Cheap 1-stock transforms onward to SS2/SS3"
  - "Saiyan Spirit S1 (free) charge + Afterimage S2 (free) 1-hit auto-dodge"
  - "Full-Power Energy Blast Volley (30,000 ki) and speed-impact Overpowering Crush (30,000 ki / 15,000 trigger); Galick Gun ult (50,000 ki)"
weaknesses:
  - "DP5 mid-ladder; weaker than SS3"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Afterimage is one-hit only"
howToFight: "Keep him off the cheap 1-stock transforms up the ladder. Afterimage is one-hit; stagger to bait it. Starve ki and pressure the 40,000-HP body."
summary: "DP5 Vegeta (Mini) SS; 40k HP, Saiyan Spirit + Afterimage, Overpowering Crush speed-impact; 1-stock steps up the ladder."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

