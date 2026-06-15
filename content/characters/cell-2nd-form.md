---
slug: "cell-2nd-form"
name: "Cell, 2nd Form"
charId: "0161_00"
baseCharacter: "Cell"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Cell, Perfect Form"
    targetSlug: "cell-perfect-form"
    cost: 2
    kind: "transform"
moveset:
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Big Bang Crash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Drain Life Cell"
    type: "blast2"
    kiCost: 30000
    damage: 3970
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Unforgivable!"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "You also take damage"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Big Bang Crash (30,000-ki super)"
  - "Drain Life Cell (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Unforgivable! 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Pump Up defense buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Drain Life Cell rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; Big Bang Crash 30,000-ki super, Unforgivable! 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

