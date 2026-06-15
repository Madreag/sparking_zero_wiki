---
slug: "piccolo-super-hero-power-awakening"
name: "Piccolo (Super Hero), Power Awakening"
charId: "3010_01"
baseCharacter: "Piccolo (Super Hero)"
era: "Movie"
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
  - target: "Orange Piccolo"
    targetSlug: "orange-piccolo"
    cost: 2
    kind: "transform"
moveset:
  - name: "This Won't End the Same Way"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Ruin"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "vanish: erase"
  - name: "Chou Magougeki"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
      - "weak-vs-shield"
      - "vanish: repel"
    notes: "Trigger cost 15,000 ki"
  - name: "Special Beam Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
playable: true
playstyle: "Mid-form Namekian"
strengths:
  - "Two-stock transform to the A-tier Orange Piccolo (+5,000 HP heal)"
  - "Wild Sense S1 (free) 1-hit auto-dodge + This Won't End the Same Way S2 (free) buff"
  - "Explosive Ruin (30,000 ki) and speed-impact Chou Magougeki (30,000 ki / 15,000 trigger); Special Beam Cannon ult (50,000 ki)"
weaknesses:
  - "DP6 intermediate; weaker than Orange"
  - "Average 1,750 recovery, no teleport"
  - "Wild Sense is one-hit only"
howToFight: "Keep him off the 2-stock transform to Orange Piccolo. Wild Sense is one-hit; bait it with a stagger. Starve ki and pressure the 40,000-HP body before he ascends."
summary: "DP6 Piccolo (SH) Power Awakening; 40k HP, Wild Sense + This Won't End the Same Way, Chou Magougeki speed-impact; 2-stock to A-tier Orange."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

