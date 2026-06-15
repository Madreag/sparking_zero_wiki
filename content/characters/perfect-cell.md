---
slug: "perfect-cell"
name: "Perfect Cell"
charId: "0162_01"
baseCharacter: "Cell"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Perfect Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Perfect Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Solar Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "B"
playable: true
playstyle: "All-rounder zoner"
strengths:
  - "B-tier all-rounder with Instant Transmission teleport mix-ups and Wild Sense evasion"
  - "Cheap Perfect Beam (20,000 ki) for constant chip + Perfect Rush speed-impact (15,000 on trigger)"
  - "Solar Kamehameha 50,000-ki ultimate"
  - "40,000 HP baseline"
weaknesses:
  - "Slow 6.0 ki charge (2,000/s recovery) — sluggish to reach supers"
  - "DP7 with only Wild Sense (gutted Dec 2025) for active defense"
  - "No heal/regen in this form"
howToFight: "Exploit his slow 6.0 ki charge — force blocks so he can't fund supers. Bait Wild Sense and Super Counter (free) his Perfect Rush. Watch Instant Transmission for teleport pressure and react to the Solar Kamehameha on knockdown."
summary: "DP7 Perfect Cell: B-tier; 40,000 HP; Perfect Beam (20,000 ki) + Perfect Rush speed-impact (15,000 on trigger) + Solar Kamehameha 50,000-ki ult; slow 6.0 ki charge."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

