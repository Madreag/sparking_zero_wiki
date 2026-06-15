---
slug: "turles"
name: "Turles"
charId: "0580_00"
baseCharacter: "Turles"
era: "Movie"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Fruit of the Tree of Might"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Kill Driver"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Full-Power Energy Wave Combo"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Meteor Burst"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Self-buff brawler"
strengths:
  - "Fruit of the Tree of Might S2 is a free self-buff/heal-style tool"
  - "Explosive Wave S1 is a free reversal/space-maker"
  - "Kill Driver and Full-Power Energy Wave Combo both at 30,000 ki give reliable finishers"
  - "Meteor Burst ult (50,000 ki) for a closer"
weaknesses:
  - "DP4 with no transform — fixed low ceiling"
  - "Plain 1,750 ki recovery, no mobility/teleport"
  - "Outclassed by transforming Saiyans at similar cost"
howToFight: "Nothing exotic to fear — pressure him steadily. He'll Explosive Wave to reset; bait it with a stagger then punish. Deny ki so Meteor Burst never charges; a DP4 with no escape tool folds to sustained offense."
summary: "DP4 Turles; 40k HP, Fruit of the Tree of Might self-buff S2, twin 30k-ki energy-wave supers + Meteor Burst ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

