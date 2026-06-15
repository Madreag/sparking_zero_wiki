---
slug: "android-18"
name: "Android 18"
charId: "0460_00"
baseCharacter: "Android 18"
era: "Z"
dp: 5
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
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Super Unyielding Spirit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Android Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Infinity Bullet"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Chain Destructo Disc"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Sadistic 18"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Android barrier zoner"
strengths:
  - "Infinity Bullet (20,000-ki super)"
  - "Chain Destructo Disc (30,000-ki super)"
  - "Sadistic 18 50,000-ki ultimate finisher"
  - "Android Barrier damage-block"
weaknesses:
  - "Android: cannot manually charge ki (charge speed 0, 2,000/s passive only) — slow to reach supers"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait the Android Barrier block, then strike after it drops. Exploit that he can't charge ki — rush him before passive recovery funds his supers. Respect Sadistic 18 on knockdown — bait it out and punish the recovery. He can't auto-reflect (DP<7 under the May 2026 rule), so contest his blasts freely."
summary: "DP5 Z-era android; 40,000 HP; Chain Destructo Disc 30,000-ki super, Sadistic 18 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

