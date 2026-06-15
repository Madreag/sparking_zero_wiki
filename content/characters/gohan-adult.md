---
slug: "gohan-adult"
name: "Gohan (Adult)"
charId: "0032_00"
baseCharacter: "Gohan (Adult)"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gohan (Adult), Super Saiyan"
    targetSlug: "gohan-adult-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Gohan (Adult), Super Saiyan 2"
    targetSlug: "gohan-adult-super-saiyan-2"
    cost: 2
    kind: "transform"
  - target: "Great Saiyaman"
    targetSlug: "great-saiyaman"
    cost: 1
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Cannon"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Short-range energy attack"
      - "vanish: erase"
  - name: "Explosive Flash Strike"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "C"
playable: true
playstyle: "All-rounder"
strengths:
  - "C-tier efficient DP4 entry — transforms up to SS/SS2 (A-tier) for 1-2 stock"
  - "Cheap Explosive Cannon (20,000 ki) chip + Explosive Flash Strike speed-impact (15,000 on trigger)"
  - "Wild Sense evasion; can also switch to Great Saiyaman form"
  - "40,000 HP baseline"
weaknesses:
  - "Base form is weak — wants to transform to be effective"
  - "DP4 with only Wild Sense (gutted Dec 2025) for defense; no heal"
  - "Slower 7.0 ki charge in base"
howToFight: "Deny the transform window with early pressure to keep him in the weak base form. Bait Wild Sense and Super Counter (free) the Explosive Flash Strike. Out-damage him before he reaches SS2."
summary: "DP4 Gohan (Adult) base: C-tier; 40,000 HP; Explosive Cannon (20,000 ki) + Explosive Flash Strike speed-impact (15,000 on trigger) + Super Kamehameha 50,000-ki ult; Wild Sense."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

