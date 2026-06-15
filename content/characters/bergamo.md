---
slug: "bergamo"
name: "Bergamo"
charId: "1190_00"
baseCharacter: "Bergamo"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Come at Me!"
    type: "blast1"
    notes: "slot S2"
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Wolfgang Penetrator"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Danger Knuckle"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Triangle Danger Beam"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Taunt-grow brawler"
strengths:
  - "Come at Me! S2 (free) is a defensive taunt/absorb setup that grows his power"
  - "Howl S1 (4 stock) no-auto-guard intimidation buff"
  - "Wolfgang Penetrator (30,000 ki) and speed-impact Danger Knuckle (30,000 ki / 15,000 trigger); Triangle Danger Beam ult (50,000 ki)"
weaknesses:
  - "DP5 with no transform — low ceiling"
  - "Average 1,750 recovery, no teleport"
  - "His grow-gimmick rewards you attacking into it — discipline counters it"
howToFight: "Don't feed Come at Me! — his gimmick grows when you swing recklessly, so play patient and bait it out. Punish Howl (no-auto-guard). With no escape tool, controlled pressure and ki-denial shut him down."
summary: "DP5 Bergamo; 40k HP, Howl (4 stock) + Come at Me! taunt, Danger Knuckle speed-impact + Triangle Danger Beam ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

