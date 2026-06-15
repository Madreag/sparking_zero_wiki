---
slug: "gohan-kid"
name: "Gohan (Kid)"
charId: "0030_00"
baseCharacter: "Gohan (Kid)"
era: "Z"
dp: 3
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Super Unyielding Spirit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "Chargeable"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Energy Blast Barrage"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Wild Rush Blaster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Masenko (30,000-ki super)"
  - "Energy Blast Barrage (20,000-ki super)"
  - "Wild Rush Blaster 50,000-ki ultimate finisher"
  - "Afterimage Strike auto-dodge (3 stock; ends on a Super Counter post-May-2026)"
  - "DP3 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "30,000 HP — melts in roughly two combos"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish; don't feed raw strings into it. Respect Wild Rush Blaster on knockdown — bait it out and punish the recovery."
summary: "DP3 Z-era fighter; 30,000 HP; Masenko 30,000-ki super, Wild Rush Blaster 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

