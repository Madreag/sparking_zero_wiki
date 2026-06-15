---
slug: "frieza-z-4th-form"
name: "Frieza (Z), 4th Form"
charId: "0153_00"
baseCharacter: "Frieza (Z)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 9
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Frieza (Z), Full Power"
    targetSlug: "frieza-z-full-power"
    cost: 1
    kind: "transform"
moveset:
  - name: "Your Arrogance Disgusts Me!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Barrage Death Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "You Might Die This Time"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "I'll Destroy This Planet!"
    type: "ultimate"
    kiCost: 50000
    damage: 2875
    hits: 3
    properties:
      - "Fire"
      - "In Sparking! Mode"
    notes: "chip 460"
tier: "B"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Psychokinesis — unblockable hold to crack defenders"
  - "C-tier; cheap Barrage Death Beam (20,000 ki) chip + speed-impact rush (15,000 on trigger)"
  - "Your Arrogance Disgusts Me! (4 stock) attack buff; 50,000-ki ult; transforms to 100%"
  - "40,000 HP baseline"
weaknesses:
  - "Slower 7.0 ki charge; no auto-dodge"
  - "Wants to transform up to 100% (DP7) to hit harder"
  - "No heal"
howToFight: "Don't block predictably — Psychokinesis is unblockable. Super Counter (free) the rush super and vanish the beams. Pressure before he transforms to 100%."
summary: "DP6 Frieza (Z) Final Form: C-tier; 40,000 HP; Barrage Death Beam (20,000 ki) + You Might Die This Time speed-impact (15,000 on trigger) + 50,000-ki ult; Psychokinesis unblockable."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

