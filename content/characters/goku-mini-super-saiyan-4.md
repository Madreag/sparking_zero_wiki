---
slug: "goku-mini-super-saiyan-4"
name: "Goku (Mini), Super Saiyan 4"
charId: "3050_14"
baseCharacter: "Goku (Mini)"
era: "DAIMA"
dp: 7
source: "Dragon Ball DAIMA Character Pack 2"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1750
initialKi: 10000
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.1
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
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Dragon Strike"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Kamehameha Reversal"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mini SS4 ceiling"
strengths:
  - "Limit Breaker Power S2 (4 stock) no-auto-guard buff for big damage"
  - "Wild Sense S1 (free) gives a 1-hit auto-dodge counter"
  - "Super Kamehameha (30,000 ki) and speed-impact Dragon Strike (30,000 ki / 15,000 trigger); Kamehameha Reversal ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "Average recovery, no teleport"
  - "Limit Breaker Power punishable on activation"
howToFight: "Punish Limit Breaker Power (4-stock, no-auto-guard). Wild Sense is one-hit; bait it with a stagger. His 40,000 HP is low for DP7 — convert hard once in and starve ki to deny Kamehameha Reversal."
summary: "DP7 Goku (Mini) SS4; 40k HP, Wild Sense + Limit Breaker Power (4 stock), Dragon Strike speed-impact + Kamehameha Reversal ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

