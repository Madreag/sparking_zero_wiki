---
slug: "trunks-sword"
name: "Trunks (Sword)"
charId: "0080_00"
baseCharacter: "Trunks (Sword)"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Trunks (Sword), Super Saiyan"
    targetSlug: "trunks-sword-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Power Up to the Very Limit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Finish Buster"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Burning Storm"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Lightning Sword Slash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Finish Buster (30,000-ki super)"
  - "Burning Storm (30,000-ki super)"
  - "Lightning Sword Slash 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Lightning Sword Slash on knockdown — bait it out and punish the recovery."
summary: "DP4 Z-era fighter; 40,000 HP; Finish Buster 30,000-ki super, Lightning Sword Slash 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

