---
slug: "king-cold"
name: "King Cold"
charId: "0430_00"
baseCharacter: "King Cold"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 4
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
  - name: "King's Dignity"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Super Explosive Wave"
    type: "blast2"
    kiCost: 40000
  - name: "Power of the Cold Clan"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "D"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Full-Power Death Beam (20,000-ki super)"
  - "Super Explosive Wave (40,000-ki super)"
  - "Power of the Cold Clan 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Power of the Cold Clan on knockdown — bait it out and punish the recovery."
summary: "DP4 Z-era fighter, D-tier; 40,000 HP; Super Explosive Wave 40,000-ki super, Power of the Cold Clan 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

