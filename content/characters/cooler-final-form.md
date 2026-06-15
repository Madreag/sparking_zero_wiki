---
slug: "cooler-final-form"
name: "Cooler, Final Form"
charId: "0601_00"
baseCharacter: "Cooler"
era: "Movie"
dp: 7
source: "Base"
hp: 45000
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
  - name: "Psycho Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Death Chaser"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Supernova"
    type: "ultimate"
    kiCost: 50000
tier: "A"
playable: true
playstyle: "Unblockable armor anchor"
strengths:
  - "Upgraded 45,000 HP makes Final Form a genuine anchor"
  - "Psychokinesis S1 stays unblockable + no-auto-guard for cheap stun mix-ups"
  - "Psycho Barrier S2 (3 stock) absorbs damage on demand"
  - "Death Beam (20,000 ki) and speed-impact Death Chaser (30,000 ki / 15,000 trigger) plus Supernova ult (50,000 ki)"
weaknesses:
  - "DP7 with no further transform — this is the ceiling"
  - "Average 1,750 ki recovery for the cost"
  - "Unblockable is vanish-evadable; Barrier is his only escape and costs 3 stock"
howToFight: "Vanish (≈half a ki bar) the unblockable Psychokinesis and punish recovery. Force out Psycho Barrier, then pressure while it's down — he has no teleport escape. His 45,000 HP means avoid raw trades; use Super Counters (~2f) to break his turn."
summary: "DP7 Cooler Final Form; 45k HP, unblockable Psychokinesis + Psycho Barrier (3 stock), Death Chaser speed-impact; A-tier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

