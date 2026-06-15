---
slug: "android-17-super"
name: "Android 17 (Super)"
charId: "0450_10"
baseCharacter: "Android 17 (Z)"
era: "Super"
dp: 6
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 2000
kiAutoRecoveryLimit: 50000
initialKi: 30000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Time to Get Serious"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Android Barrier"
    type: "blast1"
    notes: "slot S1"
  - name: "High Power Blitz"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Electric Strike"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "weak-vs-shield"
      - "vanish: erase"
  - name: "Barrier Explosion"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
      - "You also take damage"
tier: "A"
playable: true
playstyle: "Barrier zoner"
strengths:
  - "B-tier; Android Barrier damage-block + Barrier Explosion 50,000-ki ultimate"
  - "High Power Blitz + Super Electric Strike (both 30,000 ki); Time to Get Serious (4 stock) buff"
  - "Highest android passive recovery in this set (2,000/s) eases the no-charge limit"
  - "40,000 HP baseline"
weaknesses:
  - "Android: cannot manually charge ki — slower super access than chargers"
  - "DP6; Android Barrier is a block, not an evasion (no auto-dodge)"
  - "No heal"
howToFight: "Apply early pressure before passive recovery funds his supers. Bait Android Barrier then strike after it drops. Super Counter (free) his rushes and watch Barrier Explosion on wake-up."
summary: "DP6 Android 17 (Super): B-tier; 40,000 HP; CANNOT charge ki (0 charge, 2,000/s recovery); High Power Blitz (30,000 ki) + Barrier Explosion 50,000-ki ult; Android Barrier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

