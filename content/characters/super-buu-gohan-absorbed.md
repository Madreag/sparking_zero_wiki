---
slug: "super-buu-gohan-absorbed"
name: "Super Buu (Gohan Absorbed)"
charId: "0172_11"
baseCharacter: "Super Buu"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Majin Beam"
    type: "blast2"
    kiCost: 40000
  - name: "Super Ghost Buu Attack"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Majin Beam (40,000-ki super)"
  - "Super Ghost Buu Attack 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "High-Tension self ki-charge buff"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Super Ghost Buu Attack on knockdown — bait it out and punish the recovery."
summary: "DP7 Z-era fighter; 40,000 HP; Majin Beam 40,000-ki super, Super Ghost Buu Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

