---
slug: "caulifla-super-saiyan-2"
name: "Caulifla, Super Saiyan 2"
charId: "0900_02"
baseCharacter: "Caulifla"
era: "Super"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Energy Blast"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Power Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Limit Break Blaster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Buffing Saiyan ceiling"
strengths:
  - "Full Power S2 (4 stock) no-auto-guard buff for damage swings"
  - "Wild Sense S1 (free) gives a 1-hit auto-dodge counter"
  - "Energy Blast (30,000 ki) and speed-impact High Power Rush (30,000 ki / 15,000 trigger); Limit Break Blaster ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — fragile"
  - "Average 1,750 recovery, no teleport"
  - "Full Power punishable on activation"
howToFight: "Punish Full Power (4-stock, no-auto-guard). Wild Sense is one-hit — bait it with a stagger. Her 40,000 HP is low for the cost; convert hard once you get a turn and starve ki to deny the ult."
summary: "DP7 Caulifla SS2; 40k HP, Wild Sense + Full Power (4 stock), High Power Rush speed-impact + Limit Break Blaster ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

