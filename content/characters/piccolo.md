---
slug: "piccolo"
name: "Piccolo"
charId: "0040_00"
baseCharacter: "Piccolo"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "All-Out"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Paralyze Beam"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Explosive Demon Wave"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Short-range energy attack"
      - "vanish: erase"
  - name: "Explosive Breath Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Special Beam Cannon"
    type: "ultimate"
    kiCost: 50000
    damage: 9600
    hits: 5
    properties:
      - "Beam"
      - "In Sparking! Mode"
    notes: "chip 3,840"
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Explosive Demon Wave (20,000-ki super)"
  - "Explosive Breath Cannon (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Special Beam Cannon 50,000-ki ultimate finisher"
  - "Paralyze Beam — unblockable stun"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Explosive Breath Cannon rush rather than mashing into it."
summary: "DP4 Z-era fighter; 40,000 HP; Explosive Breath Cannon 30,000-ki speed-impact super, Special Beam Cannon 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

