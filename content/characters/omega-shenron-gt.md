---
slug: "omega-shenron-gt"
name: "Omega Shenron (GT)"
charId: "0700_01"
baseCharacter: "Syn Shenron (GT)"
era: "GT"
dp: 8
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 40000
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
moveset:
  - name: "Power Up to the Very Limit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Gigantic Blaze"
    type: "blast2"
    kiCost: 40000
    damage: 5700
    properties:
      - "Attack opponent's location"
      - "Played after a hit"
  - name: "Dragon Thunder"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Minus Energy Power Ball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "S"
playable: true
playstyle: "Buffing armor anchor"
strengths:
  - "Upgraded 45,000 HP makes him a real A-tier anchor"
  - "Power Up to the Very Limit S2 (4 stock) no-auto-guard buff for big damage swings"
  - "Wild Sense S1 (free) gives a 1-hit auto-dodge counter"
  - "Gigantic Blaze super at 40,000 ki and speed-impact Dragon Thunder (30,000 ki / 15,000 trigger); Minus Energy Power Ball ult (50,000 ki)"
weaknesses:
  - "DP8 anchor — expensive on a 15-DP budget"
  - "Average 1,750 ki recovery for the cost"
  - "Wild Sense is one-hit; Power Up is punishable on activation"
howToFight: "Punish Power Up to the Very Limit (4-stock, no-auto-guard) to deny his damage spike. Wild Sense is a single-hit read — stagger to bait it. Avoid trading into 45,000 HP; use Super Counters (~2f) and starve ki to keep Gigantic Blaze offline."
summary: "DP8 Omega Shenron; 45k HP, Wild Sense + Power Up to the Very Limit (4 stock), Gigantic Blaze 40k-ki; A-tier GT boss."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

