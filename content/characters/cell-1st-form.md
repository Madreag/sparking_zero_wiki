---
slug: "cell-1st-form"
name: "Cell, 1st Form"
charId: "0160_00"
baseCharacter: "Cell"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
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
transformsTo:
  - target: "Cell, 2nd Form"
    targetSlug: "cell-2nd-form"
    cost: 2
    kind: "transform"
moveset:
  - name: "Afterimage"
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
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Special Beam Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Drain Life Cell"
    type: "ultimate"
    kiCost: 50000
    damage: 9270
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Special Beam Cannon (30,000-ki super)"
  - "Drain Life Cell 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Afterimage evasive step"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Drain Life Cell on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Kamehameha 30,000-ki super, Drain Life Cell 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

