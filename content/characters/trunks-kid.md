---
slug: "trunks-kid"
name: "Trunks (Kid)"
charId: "0082_00"
baseCharacter: "Trunks (Kid)"
era: "Z"
dp: 4
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Trunks (Kid), Super Saiyan"
    targetSlug: "trunks-kid-super-saiyan"
    cost: 1
    kind: "transform"
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
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Finish Buster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Full-Power Energy Wave (30,000-ki super)"
  - "High Speed Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Finish Buster 50,000-ki ultimate finisher"
  - "Afterimage evasive step"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the High Speed Rush rather than mashing into it."
summary: "DP4 Z-era fighter; 35,000 HP; Full-Power Energy Wave 30,000-ki super, Finish Buster 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

