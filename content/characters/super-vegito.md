---
slug: "super-vegito"
name: "Super Vegito"
charId: "0100_01"
baseCharacter: "Vegito"
era: "Z"
dp: 8
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 15
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegito, Super Saiyan God Super Saiyan"
    targetSlug: "vegito-super-saiyan-god-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Big Bang Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Final Kamehameha"
    type: "blast2"
    kiCost: 40000
    damage: 5360
    hits: 4
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "chip 1,340"
  - name: "Beam Sword Slash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "Z"
singlesScore: 126.9
playable: true
playstyle: "Fusion burst rushdown"
strengths:
  - "S-tier fusion burst — Final Kamehameha 40,000-ki super and Beam Sword Slash 50,000-ki ultimate"
  - "#12 Singles (126.9); fast fusion normals just below SSGSS Vegito"
  - "Afterimage Strike (3 stock) auto-dodge gives it a defensive option base Vegito lacks"
  - "8.0 ki charge / 1,500/s recovery"
weaknesses:
  - "DP8 — premium cost; the SSGSS form (DP10) outclasses it where budget allows"
  - "Afterimage Strike ends on a Super Counter and was duration-nerfed (Dec 2025)"
  - "No heal; standardized fusion durability"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish. Don't feed raw strings into the auto-dodge — bait it first. Respect Beam Sword Slash and Final Kamehameha on knockdown."
summary: "DP8 Super Vegito: S-tier, #12 Singles (126.9); Final Kamehameha 40,000-ki super + Beam Sword Slash 50,000-ki ult; Afterimage Strike (3 stock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

