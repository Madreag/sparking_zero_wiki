---
slug: "tapion"
name: "Tapion"
charId: "0660_00"
baseCharacter: "Tapion"
era: "Movie"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Hero's Flute"
    type: "blast1"
    notes: "slot S1"
  - name: "Brave Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Brave Slash"
    type: "blast2"
    kiCost: 30000
    damage: 1000
    properties:
      - "Continuous Fire"
      - "Unguardable"
    notes: "chip 200"
  - name: "Brave Sword Attack"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Sword utility skirmisher"
strengths:
  - "Hero's Flute S1 (free) is a unique utility/control tool"
  - "Afterimage S2 (free) gives a 1-hit auto-dodge read"
  - "Brave Cannon and Brave Slash both at 30,000 ki for steady finishers"
  - "Brave Sword Attack ult (50,000 ki) for a closer"
weaknesses:
  - "DP4 with no transform — low ceiling"
  - "Average 1,750 recovery, no teleport"
  - "Underwhelming damage versus transforming peers"
howToFight: "No real threats — apply pressure. Afterimage is a single-hit read; stagger to bait it then punish. Deny ki so the ult never lands; a DP4 with no escape folds to sustained offense."
summary: "DP4 Tapion; 40k HP, Hero's Flute utility + Afterimage, twin 30k-ki Brave supers + Brave Sword Attack ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

