---
slug: "vegeta-mini-super-saiyan-3"
name: "Vegeta (Mini), Super Saiyan 3"
charId: "3060_03"
baseCharacter: "Vegeta (Mini)"
era: "DAIMA"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
moveset:
  - name: "Special Training Results"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Slash Flash"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    hits: 11
    properties:
      - "weak-vs-shield"
      - "vanish: erase"
    notes: "chip 1,140"
  - name: "Vanishing Strike"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Galick Doom"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Mini SS3 ceiling"
strengths:
  - "Sneaky DP-value pick at the top of the Mini-Vegeta ladder"
  - "Special Training Results S2 (4 stock) no-auto-guard buff for big damage"
  - "Wild Sense S1 (free) 1-hit auto-dodge"
  - "Slash Flash (30,000 ki) and speed-impact Vanishing Strike (30,000 ki / 15,000 trigger); Galick Doom ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Special Training Results punishable on activation"
howToFight: "Punish Special Training Results (4-stock, no-auto-guard). Wild Sense is one-hit; bait it with a stagger. His 40,000 HP is low for DP7 — convert hard once in and deny ki to keep Galick Doom offline."
summary: "DP7 Vegeta (Mini) SS3; 40k HP, Wild Sense + Special Training Results (4 stock), Vanishing Strike speed-impact; sneaky DP-value pick."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

