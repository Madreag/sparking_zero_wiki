---
slug: "mecha-frieza"
name: "Mecha Frieza"
charId: "0153_10"
baseCharacter: "Frieza (Z)"
era: "Z"
dp: 6
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Fissure Slash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "Unguardable"
  - name: "Supernova"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Android drain zoner"
strengths:
  - "Death Beam (20,000-ki super)"
  - "Fissure Slash (30,000-ki super)"
  - "Supernova 50,000-ki ultimate finisher"
  - "Psychokinesis — unblockable hold"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Supernova on knockdown — bait it out and punish the recovery. He can't auto-reflect (DP<7 under the May 2026 rule), so contest his blasts freely."
summary: "DP6 Z-era android; 40,000 HP; Fissure Slash 30,000-ki super, Supernova 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

