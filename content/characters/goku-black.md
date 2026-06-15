---
slug: "goku-black"
name: "Goku Black"
charId: "0800_00"
baseCharacter: "Goku Black"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "75,000 Zeni (shop)"
transformsTo:
  - target: "Goku Black, Super Saiyan Rosé"
    targetSlug: "goku-black-super-saiyan-ros"
    cost: 2
    kind: "transform"
moveset:
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Black Power Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Black Bind"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Black Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
playable: true
playstyle: "Rosé-access base"
strengths:
  - "Two-stock transform to the A-tier Super Saiyan Rosé form"
  - "Wild Sense S1 (free) 1-hit auto-dodge counter; Finish Sign S2 (free) is a buff/taunt setup"
  - "Black Bind super at 40,000 ki (20,000 trigger, speed-impact) is a strong catch even in base"
  - "Black Kamehameha ult (50,000 ki)"
weaknesses:
  - "DP5 base — you want Rosé fast"
  - "Average 1,750 recovery, no teleport in base"
  - "Wild Sense is one-hit only post-nerf"
howToFight: "Deny the 2-stock transform to Rosé. Wild Sense is a single-hit read — stagger to bait it. He has no teleport in base, so keep pressure and starve his stocks before he ascends."
summary: "DP5 Goku Black base; 40k HP, Wild Sense + Finish Sign, Black Bind speed-impact; 2-stock transform to A-tier Rosé."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

