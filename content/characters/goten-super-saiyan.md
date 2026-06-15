---
slug: "goten-super-saiyan"
name: "Goten, Super Saiyan"
charId: "0090_01"
baseCharacter: "Goten"
era: "Z"
dp: 5
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
transformsTo:
  - target: "Gotenks"
    targetSlug: "gotenks"
    cost: 2
    kind: "fusion"
  - target: "Gotenks, Super Saiyan"
    targetSlug: "gotenks-super-saiyan"
    cost: 3
    kind: "fusion"
  - target: "Gotenks, Super Saiyan 3"
    targetSlug: "gotenks-super-saiyan-3"
    cost: 4
    kind: "fusion"
moveset:
  - name: "False Courage"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Kamekameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Charge!"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Double Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "B"
playable: true
playstyle: "Fragile rushdown"
strengths:
  - "C-tier; Double Kamehameha 50,000-ki ult and Charge! speed-impact rush (15,000 ki on trigger)"
  - "Wild Sense evasion + False Courage instant ki"
  - "DP5 and 8.0 ki charge keeps supers funded"
  - "Transforms back to base for utility"
weaknesses:
  - "35,000 HP — below baseline, dies a combo earlier"
  - "DP5 with only Wild Sense (gutted Dec 2025) for defense; no heal"
  - "Child kit — limited reach and damage ceiling"
howToFight: "His 35,000 HP folds fast — open him once and commit. Bait Wild Sense, Super Counter (free) the Charge! rush, and overwhelm before he funds Double Kamehameha."
summary: "DP5 Goten SS: C-tier; 35,000 HP; Kamekameha (30,000 ki) + Charge! speed-impact (15,000 on trigger) + Double Kamehameha 50,000-ki ult; Wild Sense evasion."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

