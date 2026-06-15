---
slug: "gamma-2"
name: "Gamma 2"
charId: "3030_00"
baseCharacter: "Gamma 2"
era: "Movie"
dp: 7
source: "\"Heroes of Justice\" Pack"
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
kiBlastShots: 999
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Android Barrier"
    type: "blast1"
    notes: "slot S2"
  - name: "Gamma Superhero Pose 2"
    type: "blast1"
    notes: "slot S1"
  - name: "Gamma Blaster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gamma Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Core Breaker"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "You also take damage"
tier: "A"
playable: true
playstyle: "Android zoner"
strengths:
  - "Android 2,000 ki auto-recovery sustains his blast game"
  - "Android Barrier S2 (free) absorbing shield at no stock cost"
  - "Gamma Superhero Pose 2 S1 (free) buff/setup"
  - "Gamma Blaster (30,000 ki) and speed-impact Gamma Impact (30,000 ki / 15,000 trigger); Core Breaker ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "No transform; B-tier ceiling"
  - "No super-armor"
howToFight: "Bait out Android Barrier, then attack while it's down. His 40,000 HP is low for DP7 — press your advantage once in. Block the speed-impact Gamma Impact; deny ki to keep Core Breaker offline."
summary: "DP7 Gamma 2; 40k HP, 2,000 ki recovery (android), Android Barrier + hero-pose, Core Breaker ult; B-tier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

