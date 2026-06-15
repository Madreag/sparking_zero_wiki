---
slug: "zarbon"
name: "Zarbon"
charId: "0350_00"
baseCharacter: "Zarbon"
era: "Z"
dp: 3
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Super Zarbon"
    targetSlug: "super-zarbon"
    cost: 1
    kind: "transform"
moveset:
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Shooting Star Arrow"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Bloody Dance"
    type: "blast2"
    kiCost: 30000
    damage: 6000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Elegant Blaster"
    type: "ultimate"
    kiCost: 50000
    damage: 12000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Shooting Star Arrow (20,000-ki super)"
  - "Bloody Dance (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Elegant Blaster 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "Full Power attack buff (4 stock)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the Bloody Dance rush rather than mashing into it."
summary: "DP3 Z-era fighter; 40,000 HP; Bloody Dance 30,000-ki speed-impact super, Elegant Blaster 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

