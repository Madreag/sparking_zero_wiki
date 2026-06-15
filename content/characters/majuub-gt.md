---
slug: "majuub-gt"
name: "Majuub (GT)"
charId: "0240_01"
baseCharacter: "Uub (GT)"
era: "GT"
dp: 6
source: "Base"
classes:
  - "Fusion"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Mystic Breath"
    type: "blast1"
    skillCost: 1
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Paralyze Beam"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Super Consecutive Energy Blast"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Majin Beam"
    type: "blast2"
    kiCost: 40000
  - name: "Lightning Arrow"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "Super Consecutive Energy Blast (20,000-ki super)"
  - "Majin Beam (40,000-ki super)"
  - "Lightning Arrow 50,000-ki ultimate finisher"
  - "Paralyze Beam — unblockable stun"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Lightning Arrow on knockdown — bait it out and punish the recovery."
summary: "DP6 GT-era fusion; 40,000 HP; Majin Beam 40,000-ki super, Lightning Arrow 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

