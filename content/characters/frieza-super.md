---
slug: "frieza-super"
name: "Frieza (Super)"
charId: "0153_20"
baseCharacter: "Frieza (Z)"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Golden Frieza"
    targetSlug: "golden-frieza"
    cost: 3
    kind: "transform"
moveset:
  - name: "Power of Revenge"
    type: "blast1"
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Super Nova Strike"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Super Death Ball"
    type: "ultimate"
    kiCost: 50000
    damage: 12500
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Melee rushdown"
strengths:
  - "Death Beam (20,000-ki super)"
  - "Super Nova Strike (40,000-ki super, 20,000-ki on combo trigger, speed-impact rush)"
  - "Super Death Ball 50,000-ki ultimate finisher"
  - "Psychokinesis — unblockable hold"
  - "Transforms (3 stock to Golden Frieza) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Super Nova Strike rush rather than mashing into it."
summary: "DP6 Super-era fighter; 40,000 HP; Super Nova Strike 40,000-ki speed-impact super, Super Death Ball 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

