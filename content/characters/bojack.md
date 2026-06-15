---
slug: "bojack"
name: "Bojack"
charId: "0630_00"
baseCharacter: "Bojack"
era: "Movie"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
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
transformsTo:
  - target: "Full-Power Bojack"
    targetSlug: "full-power-bojack"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Psycho Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Full-Power Energy Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Trap Shooter"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Grand Smasher"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Barrier brawler base"
strengths:
  - "Psycho Barrier S1 (3 stock) absorbs damage for stalling"
  - "Full Power S2 (4 stock) no-auto-guard buff raises output"
  - "Two-stock transform to Full-Power Bojack (+5,000 HP heal)"
  - "Full-Power Energy Ball (30,000 ki) and Grand Smasher ult (50,000 ki)"
weaknesses:
  - "DP5 base; weak until transformed"
  - "Average 1,750 recovery, no teleport"
  - "Barrier is the only escape and costs 3 stock"
howToFight: "Deny the 2-stock transform and force out Psycho Barrier early. Punish Full Power activations (no-auto-guard). With no mobility tool, he can't escape sustained corner pressure."
summary: "DP5 Bojack base; 40k HP, Psycho Barrier (3 stock) + Full Power (4 stock); 2-stock transform to Full-Power Bojack."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

