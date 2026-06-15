---
slug: "super-buu-gotenks-absorbed"
name: "Super Buu (Gotenks Absorbed)"
charId: "0172_10"
baseCharacter: "Super Buu"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Super Buu (Gohan Absorbed)"
    targetSlug: "super-buu-gohan-absorbed"
    cost: 1
    kind: "transform"
moveset:
  - name: "Regeneration"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galactic Donut Volley"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    properties:
      - "Fire"
      - "Unguardable"
  - name: "Special Beam Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "A"
playable: true
playstyle: "Tanky regen zoner"
strengths:
  - "Regeneration (4 stock) restores HP — sustain that effectively raises his durability"
  - "A-tier; Galactic Donut Volley + Special Beam Cannon (both 30,000 ki) and Super Kamehameha 50,000-ki ult"
  - "Absorbed-form power spike (reached via 2-stock transform from base Super Buu)"
  - "Explosive Wave reset"
weaknesses:
  - "Regeneration costs a full 4 stock and was no-auto-guard — vulnerable during the cast"
  - "DP7; needs to transform up from base Super Buu to reach this form"
  - "No true auto-dodge; slower 7.0 ki charge"
howToFight: "Punish the Regeneration cast (4 stock, no auto-guard) — interrupt it to deny the heal. Don't let him stall to full; apply constant pressure. Vanish the Special Beam Cannon and Super Counter (free) his rushes."
summary: "DP7 Super Buu (Gotenks absorbed): A-tier; 40,000 HP; Galactic Donut Volley (30,000 ki) + Super Kamehameha 50,000-ki ult; Regeneration (4 stock) sustain."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

