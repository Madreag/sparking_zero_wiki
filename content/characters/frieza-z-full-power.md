---
slug: "frieza-z-full-power"
name: "Frieza (Z), Full Power"
charId: "0154_00"
baseCharacter: "Frieza (Z)"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 30000
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
  - name: "Long Awaited-for 100%"
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
  - name: "Death Saucer"
    type: "blast2"
    kiCost: 30000
    damage: 1000
    hits: 2
    properties:
      - "Fire"
      - "Unguardable"
    notes: "chip 1,200"
  - name: "Nova Strike"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
      - "speed-impact"
  - name: "I'm the One Who'll Kill You!"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "B"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Psychokinesis — unblockable hold that opens defenders for a combo"
  - "B-tier; Nova Strike 40,000-ki speed-impact charge super and Death Saucer (30,000 ki) homing discs"
  - "Long Awaited-for 100% (4 stock) full-power attack buff; 50,000-ki ult"
  - "8.0 ki charge / 1,500/s recovery"
weaknesses:
  - "DP7 with no auto-dodge — Super Counter is the only active defense"
  - "Top of the Frieza Z transform chain — must climb to reach 100%"
  - "No heal"
howToFight: "Respect Psychokinesis — don't sit blocking predictably or you eat the unblockable. Vanish the Nova Strike and Super Counter (free) his approaches. Pressure before he reaches the 100% form."
summary: "DP7 Frieza 100% (Z): B-tier; 40,000 HP, 8.0 ki charge; Death Saucer (30,000 ki) + Nova Strike 40,000-ki speed-impact + 50,000-ki ult; Psychokinesis unblockable hold."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

