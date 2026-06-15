---
slug: "golden-frieza"
name: "Golden Frieza"
charId: "0155_00"
baseCharacter: "Golden Frieza"
era: "Super"
dp: 8
source: "Base"
hp: 40000
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
transformsTo:
  - target: "Frieza (Super)"
    targetSlug: "frieza-super"
    cost: 0
    kind: "transform"
moveset:
  - name: "True Golden Frieza"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Great Death Beam"
    type: "blast2"
    kiCost: 30000
    damage: 570
    properties:
      - "weak-vs-shield"
    notes: "chip 114"
  - name: "\"No Hard Feelings\" Hit"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Earth Breaker"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Great Death Beam (30,000-ki super)"
  - "\"No Hard Feelings\" Hit (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Earth Breaker 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the \"No Hard Feelings\" Hit rush rather than mashing into it."
summary: "DP8 Super-era fighter; 40,000 HP; Great Death Beam 30,000-ki super, Earth Breaker 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

