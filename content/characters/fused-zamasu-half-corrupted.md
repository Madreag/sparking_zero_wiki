---
slug: "fused-zamasu-half-corrupted"
name: "Fused Zamasu, Half-Corrupted"
charId: "0811_00"
baseCharacter: "Fused Zamasu"
era: "Super"
dp: 9
source: "Base"
classes:
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 16
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Light of Justice"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Mark of Condemnation"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Violent Fierce God Slicer"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Divine Hammer"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "S"
dpTier: "A"
singlesScore: 122.3
playable: true
playstyle: "Corrupted fusion anchor"
strengths:
  - "Premium 45,000 HP ceiling form — A-tier Singles (122.3) with strong burst"
  - "Light of Justice S2 (free) is a damage/control tool"
  - "Mark of Condemnation (30,000 ki) and speed-impact Violent Fierce God Slicer (30,000 ki / 15,000 trigger)"
  - "Divine Hammer ult (50,000 ki); Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP9 premium — inefficient on a 15-DP budget"
  - "Slow 1,500 ki recovery / 8.0 charge for the cost"
  - "No teleport; no super-armor — relies on burst"
howToFight: "No teleport and no armor — pressure him directly and use ~2f Super Counters to break his strings. Vanish (≈half a ki bar) the speed-impact Violent Fierce God Slicer. Starve his slower-recovering ki to keep Divine Hammer offline; the 45,000 HP is the only thing keeping him alive, so grind it."
summary: "DP9 Fused Zamasu Half-Corrupted; 45k HP, Light of Justice + Violent Fierce God Slicer speed-impact; A-tier (122.3)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

