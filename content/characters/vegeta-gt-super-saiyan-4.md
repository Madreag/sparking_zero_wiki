---
slug: "vegeta-gt-super-saiyan-4"
name: "Vegeta (GT), Super Saiyan 4"
charId: "0020_50"
baseCharacter: "Vegeta (Z - Scouter)"
era: "GT"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gogeta (GT), Super Saiyan 4"
    targetSlug: "gogeta-gt-super-saiyan-4"
    cost: 4
    kind: "fusion"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Final Flash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Spirit Breaking Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Final Shine Attack"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Final Flash (30,000-ki super)"
  - "Spirit Breaking Cannon (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Final Shine Attack 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Spirit Breaking Cannon rush rather than mashing into it."
summary: "DP8 GT-era fighter; 40,000 HP; Final Flash 30,000-ki super, Final Shine Attack 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

