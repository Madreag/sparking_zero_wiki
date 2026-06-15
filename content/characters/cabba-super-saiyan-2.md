---
slug: "cabba-super-saiyan-2"
name: "Cabba, Super Saiyan 2"
charId: "0890_02"
baseCharacter: "Cabba"
era: "Super"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 9
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Growth"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Galick Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Galick Rain"
    type: "blast2"
    kiCost: 30000
  - name: "Final Stream"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Buffing Saiyan ceiling"
strengths:
  - "Growth S2 (4 stock) is a no-auto-guard damage buff at the top of the ladder"
  - "Super Galick Cannon and Galick Rain both at 30,000 ki; Final Stream ult (50,000 ki)"
  - "High Power Rush variant adds a speed-impact catch"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "Average 1,750 recovery, no teleport"
  - "Growth punishable on activation"
howToFight: "Punish Growth (4-stock, no-auto-guard). His 40,000 HP is low for DP7, so once in, convert hard. No escape tool means he can't break sustained pressure — starve ki to deny Final Stream."
summary: "DP7 Cabba SS2; 40k HP, Growth (4 stock) buff, High Power Rush speed-impact + Final Stream ult — ceiling form."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

