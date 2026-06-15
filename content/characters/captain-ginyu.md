---
slug: "captain-ginyu"
name: "Captain Ginyu"
charId: "0380_00"
baseCharacter: "Captain Ginyu"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Dangerous Shock"
    type: "blast1"
    skillCost: 1
    notes: "slot S2"
  - name: "SP Fighting Pose 5"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Galaxy Dynamite"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Body Change"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "Switch body"
      - "When you and your opponent switch bodies, you cannot use\r Transformation, Switch, skills, Blasts, or Ultimate Blasts."
playable: true
playstyle: "Beam zoner"
strengths:
  - "Full-Power Energy Wave (30,000-ki super)"
  - "Galaxy Dynamite (30,000-ki super)"
  - "Body Change 50,000-ki ultimate finisher"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Body Change on knockdown — bait it out and punish the recovery."
summary: "DP4 Z-era fighter; 40,000 HP; Full-Power Energy Wave 30,000-ki super, Body Change 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

