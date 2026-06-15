---
slug: "goku-super-super-saiyan-god-super-saiyan"
name: "Goku (Super), Super Saiyan God Super Saiyan"
charId: "0000_43"
baseCharacter: "Goku (Z - Early)"
era: "Super"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - name: "Kaioken"
    type: "blast1"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "God Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "\"No Hard Feelings\" Hit"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Limit Breaker God Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "God Kamehameha (30,000-ki super)"
  - "\"No Hard Feelings\" Hit (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Limit Breaker God Kamehameha 50,000-ki ultimate finisher"
  - "Instant Transmission teleport repositioning"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the \"No Hard Feelings\" Hit rush rather than mashing into it."
summary: "DP8 Super-era fighter; 40,000 HP; God Kamehameha 30,000-ki super, Limit Breaker God Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

