---
slug: "toppo"
name: "Toppo"
charId: "0940_00"
baseCharacter: "Toppo"
era: "Super"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Toppo, God of Destruction"
    targetSlug: "toppo-god-of-destruction"
    cost: 2
    kind: "transform"
moveset:
  - name: "Pride Trooper Pose 1"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Justice!"
    type: "blast1"
    notes: "slot S1"
  - name: "Justice Flash"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Justice Tornado"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "United Justice Stream"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Justice bruiser base"
strengths:
  - "Two-stock transform to S-tier God of Destruction banking +10,000 HP"
  - "Pride Trooper Pose 1 S2 (4 stock) no-auto-guard buff"
  - "Justice! S1 (free) buff/setup"
  - "Justice Flash (20,000 ki) and speed-impact Justice Tornado (30,000 ki / 15,000 trigger); United Justice Stream ult (50,000 ki)"
weaknesses:
  - "DP7 base with only 40,000 HP until it transforms"
  - "Average 1,750 recovery, no teleport"
  - "Pose 1 punishable on activation"
howToFight: "Deny the 2-stock transform to GoD Toppo — that's a +10,000 HP swing into S-tier. Punish Pride Trooper Pose 1 (no-auto-guard). Pressure the base form before he ascends."
summary: "DP7 Toppo base; 40k HP, Justice! + Pride Trooper Pose 1 (4 stock), Justice Tornado speed-impact; 2-stock transform to S-tier GoD (+10,000 HP)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

