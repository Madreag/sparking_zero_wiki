---
slug: "vegeta-daima-super-saiyan-3"
name: "Vegeta (DAIMA), Super Saiyan 3"
charId: "3100_03"
baseCharacter: "Vegeta (DAIMA)"
era: "DAIMA"
dp: 7
source: "Dragon Ball DAIMA Character Pack 2"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
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
moveset:
  - name: "Limit Breaker Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Saiyan Burst"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Infinite Blaster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Spirit Breaker"
    type: "blast2"
    kiCost: 40000
    properties:
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Maximum Final Flash"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Double-buff Saiyan"
strengths:
  - "Two stacking buffs: Saiyan Burst S1 (3 stock) and Limit Breaker Power S2 (4 stock, no-auto-guard) for large damage"
  - "Infinite Blaster (30,000 ki) and speed-impact Spirit Breaker (40,000 ki / 20,000 trigger); Maximum Final Flash ult (50,000 ki)"
  - "Standard 40,000 HP"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Both buffs are punishable on activation"
howToFight: "Punish his buff activations — Saiyan Burst (3 stock) and especially Limit Breaker Power (4-stock, no-auto-guard) leave windows. His 40,000 HP is low for DP7; convert hard once in. Vanish the speed-impact Spirit Breaker and starve ki to keep Maximum Final Flash offline."
summary: "DP7 Vegeta (DAIMA) SS3; 40k HP, Saiyan Burst (3 stock) + Limit Breaker Power (4 stock), Spirit Breaker speed-impact + Maximum Final Flash ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

