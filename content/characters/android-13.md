---
slug: "android-13"
name: "Android 13"
charId: "0620_00"
baseCharacter: "Android 13"
era: "Movie"
dp: 5
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 1800
kiAutoRecoveryLimit: 50000
initialKi: 30000
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Fusion Android 13"
    targetSlug: "fusion-android-13"
    cost: 2
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Silent Assassin 13"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "S.S. Deadly Bomber"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "Fusion-access android"
strengths:
  - "Two-stock transform straight into the S-tier Fusion Android 13 (+5,000 HP heal)"
  - "Wild Sense S1 (free) gives a 1-hit auto-dodge counter"
  - "Slightly elevated 1,800 ki auto-recovery (android) funds blasts"
  - "Silent Assassin 13 super at 30,000 ki (15,000 trigger), speed-impact; S.S. Deadly Bomber ult (50,000 ki)"
weaknesses:
  - "DP5 base is a stepping stone — weak until it fuses"
  - "Wild Sense is a single-hit read post-Dec-2025, not a real escape"
  - "No teleport; readable approach"
howToFight: "Deny the 2-stock fusion into the S-tier Fusion form — that's the whole threat. Wild Sense is one-hit only; stagger and bait it. Keep him stock-starved and he stays a weak DP5 body."
summary: "DP5 Android 13; 40k HP, Wild Sense + High-Tension, 1,800 ki recovery; 2-stock transform to S-tier Fusion A13."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

