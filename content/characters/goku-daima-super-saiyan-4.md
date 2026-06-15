---
slug: "goku-daima-super-saiyan-4"
name: "Goku (DAIMA), Super Saiyan 4"
charId: "3120_04"
baseCharacter: "Goku (DAIMA)"
era: "DAIMA"
dp: 8
source: "Dragon Ball DAIMA Character Pack 2"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - name: "Saiyan Burst"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "True Divine Dragon Strike"
    type: "blast2"
    kiCost: 30000
    damage: 6000
    properties:
      - "Fire"
      - "Played after a hit"
      - "weak-vs-shield"
  - name: "True Flash Dragon Kick"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Transcendent Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Double-buff SS4"
strengths:
  - "Stacking buffs: Saiyan Burst S1 (3 stock) and Limit Breaker Power S2 (4 stock, no-auto-guard) for huge damage"
  - "True Divine Dragon Strike (30,000 ki) and speed-impact True Flash Dragon Kick (30,000 ki / 15,000 trigger); Transcendent Kamehameha ult (50,000 ki)"
  - "Standard 40,000 HP"
weaknesses:
  - "DP8 with only 40,000 HP — fragile for the cost"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Both buffs punishable on activation; no super-armor"
howToFight: "Punish his buff activations — Saiyan Burst (3 stock) and Limit Breaker Power (4-stock, no-auto-guard). His 40,000 HP is low for a DP8 with no armor; use ~2f Super Counters to break strings and convert hard. Starve ki to keep Transcendent Kamehameha offline."
summary: "DP8 Goku (DAIMA) SS4; 40k HP, Saiyan Burst (3 stock) + Limit Breaker Power (4 stock), True Flash Dragon Kick speed-impact + Transcendent Kamehameha ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

