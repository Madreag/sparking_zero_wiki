---
slug: "gamma-1"
name: "Gamma 1"
charId: "3020_00"
baseCharacter: "Gamma 1"
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
  - name: "Gamma Superhero Pose 1"
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
  - name: "Gamma Shift Shot"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Android zoner"
strengths:
  - "Android 2,000 ki auto-recovery keeps blasts funded despite 0.0 charge"
  - "Android Barrier S2 (free) gives an absorbing shield with no stock cost"
  - "Gamma Superhero Pose 1 S1 (free) buff/setup"
  - "Gamma Blaster (30,000 ki) and speed-impact Gamma Impact (30,000 ki / 15,000 trigger); Gamma Shift Shot ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — not durable"
  - "No transform; fixed ceiling"
  - "No super-armor; loses straight trades"
howToFight: "He'll Android Barrier to absorb — bait it out, then pressure. His 40,000 HP is low for DP7, so convert openings hard. Block the speed-impact Gamma Impact and starve ki to keep his ult offline."
summary: "DP7 Gamma 1; 40k HP, 2,000 ki recovery (android), Android Barrier + hero-pose buff, Gamma Impact speed-impact."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

