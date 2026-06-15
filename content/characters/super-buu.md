---
slug: "super-buu"
name: "Super Buu"
charId: "0172_00"
baseCharacter: "Super Buu"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
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
  - target: "Super Buu (Gotenks Absorbed)"
    targetSlug: "super-buu-gotenks-absorbed"
    cost: 2
    kind: "transform"
  - target: "Super Buu (Gohan Absorbed)"
    targetSlug: "super-buu-gohan-absorbed"
    cost: 3
    kind: "transform"
moveset:
  - name: "Regeneration"
    type: "blast1"
    skillCost: 4
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Vice Shout"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Assault Rain"
    type: "blast2"
    kiCost: 30000
    damage: 500
    hits: 11
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
    notes: "chip 100"
  - name: "Majin Beam"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Beam"
      - "Unguardable"
      - "Played after a hit"
  - name: "Revenge Death Bomber"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "You also take damage"
playable: true
playstyle: "Regen zoner"
strengths:
  - "Regeneration (4 stock) HP sustain and Vice Shout — an unblockable shockwave opener"
  - "Majin Beam 40,000-ki super + Revenge Death Bomber 50,000-ki ult for burst"
  - "Transforms to the absorbed (Gotenks) form for a power spike"
  - "40,000 HP baseline"
weaknesses:
  - "DP6; Regeneration costs 4 stock and was no-auto-guard (interruptible)"
  - "Slower 7.0 ki charge; no auto-dodge"
  - "Wants to transform to reach A-tier absorbed form"
howToFight: "Interrupt the Regeneration cast (4 stock) to deny the heal. Block the Vice Shout reads and punish the recovery. Keep him from stalling to transform."
summary: "DP6 Super Buu (base): 40,000 HP; Assault Rain (30,000 ki) + Majin Beam 40,000-ki super + Revenge Death Bomber 50,000-ki ult; Regeneration (4 stock) + Vice Shout unblockable."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

