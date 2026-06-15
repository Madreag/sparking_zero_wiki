---
slug: "goku-z-early"
name: "Goku (Z - Early)"
charId: "0000_00"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Kaioken"
    type: "blast1"
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    damage: 4560
    hits: 4
    properties:
      - "Beam"
      - "Chargeable"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "chip 1,140"
  - name: "Kaioken Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Spirit Bomb"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Kaioken Attack (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Spirit Bomb 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Kaioken Attack rush rather than mashing into it."
summary: "DP4 Z-era fighter; 40,000 HP; Kamehameha 30,000-ki super, Spirit Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

