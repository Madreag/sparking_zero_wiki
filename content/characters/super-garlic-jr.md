---
slug: "super-garlic-jr"
name: "Super Garlic Jr."
charId: "0561_00"
baseCharacter: "Super Garlic Jr."
era: "Movie"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Makyo Star"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Sealing Paralyze Beam"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Death Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Darkness Illusion"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Dead Zone"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
dpTier: "A"
playable: true
playstyle: "Unblockable-trap zoner"
strengths:
  - "Sealing Paralyze Beam S1 is unblockable + no-auto-guard and free (no stock) — a cheap paralysis opener"
  - "Darkness Illusion super at 40,000 ki (20,000 trigger) is a speed-impact catch"
  - "Makyo Star S2 (3 stock) buffs his output"
  - "Dead Zone ult (50,000 ki) is a wide finisher"
weaknesses:
  - "DP4 with no transform — low ceiling"
  - "Average 1,750 ki recovery and pedestrian normals"
  - "Telegraphed unblockable; easily vanished"
howToFight: "His whole game is the unblockable Sealing Paralyze Beam — it's slow and unblockable, so vanish (≈half a ki bar) or dash around it rather than guarding. Once you read it, punish the recovery. He has no defensive escape, so apply continuous pressure."
summary: "DP4 Movie villain; 40k HP, unblockable Sealing Paralyze Beam S1, Darkness Illusion 40k-ki speed-impact super."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

