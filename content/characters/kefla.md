---
slug: "kefla"
name: "Kefla"
charId: "0920_00"
baseCharacter: "Kefla"
era: "Super"
dp: 6
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Kefla, Super Saiyan"
    targetSlug: "kefla-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Kefla, Super Saiyan 2"
    targetSlug: "kefla-super-saiyan-2"
    cost: 2
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Blaster Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gigantic Swing"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Gigantic Burn"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Fusion-ladder rushdown"
strengths:
  - "Cheap 1-stock transform to SS, 2-stock to SS2 — fast fusion ladder"
  - "Wild Sense S1 (free) 1-hit auto-dodge + High-Tension S2 (free) charge"
  - "Blaster Ball (30,000 ki) and speed-impact Gigantic Swing (30,000 ki / 15,000 trigger); Gigantic Burn ult (50,000 ki)"
weaknesses:
  - "Base fusion form is the weakest of the three — climb to SS2 fast"
  - "Average 1,750 recovery, no super-armor"
  - "Wild Sense is one-hit only"
howToFight: "Deny the cheap 1/2-stock transforms to keep her at the weak base. Wild Sense is a single-hit read; stagger to bait it. Pressure continuously — she has no escape tool and wants the meter to climb."
summary: "DP6 Kefla base; giant-ish (null HP) fusion, Wild Sense + High-Tension, Gigantic Swing speed-impact; 1/2-stock to SS/SS2."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

