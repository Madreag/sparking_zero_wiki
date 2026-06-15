---
slug: "master-roshi"
name: "Master Roshi"
charId: "0140_00"
baseCharacter: "Master Roshi"
era: "DB"
dp: 2
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Master Roshi, Max Power"
    targetSlug: "master-roshi-max-power"
    cost: 2
    kind: "transform"
moveset:
  - name: "False Courage"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Original Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Thunder Shock Surprise"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Beam"
      - "Unguardable"
      - "Played after a hit"
  - name: "Evil Containment Wave"
    type: "ultimate"
    kiCost: 50000
    damage: 12500
    properties:
      - "Short-range energy attack"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "You also take damage"
      - "Damage dealt and taken changes based on your opponent's DP."
playable: true
playstyle: "Tricky DP filler"
strengths:
  - "Afterimage Strike (3 stock) auto-dodge on a DP2 body — disproportionate value in the DP queue"
  - "DP2 — extremely cheap; transforms to Max Power (DP-efficiency S-tier) for 2 stock"
  - "Evil Containment Wave 50,000-ki ultimate is an unusual seal/punish; Thunder Shock Surprise 40,000-ki super"
  - "False Courage for instant ki despite low charge access"
weaknesses:
  - "30,000 HP — extremely fragile, dies in roughly two combos"
  - "Base form is flightless and slow; wants to transform to Max Power immediately"
  - "Ki recovery nerfed May 2026; useless tankiness in standardized-HP Singles"
howToFight: "His 30,000 HP melts — open him up once and commit. Land a Super Counter (free) to pop Afterimage Strike, then burst. In Singles his value collapses (no DP tank edge). Deny the Max Power transform with early pressure."
summary: "DP2 Master Roshi (base): 30,000 HP, flightless skirmisher; Afterimage Strike (3 stock) + Evil Containment Wave 50,000-ki ult; transforms to Max Power (2 stock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

