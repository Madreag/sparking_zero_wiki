---
slug: "gohan-beast"
name: "Gohan Beast"
charId: "3000_03"
baseCharacter: "Gohan (Super Hero)"
era: "Movie"
dp: 9
source: "Base"
hp: 35000
hpInherited: true
kiChargeSpeed: 6
kiAutoRecovery: 2000
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
moveset:
  - name: "Guess It's My Turn"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Beast Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Explosive Ray"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Explosive Flash"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Special Beam Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "S"
playable: true
playstyle: "Best all-around carry"
strengths:
  - "The premier dual-meta DLC carry: #10 Singles (128.7k) AND #1 DP value (33.9k) — elite in both modes"
  - "2,000 ki auto-recovery keeps his kit fully funded"
  - "Beast Sense S1 (free) is a strong evasive/counter read; Guess It's My Turn S2 (4 stock) no-auto-guard damage buff"
  - "Super Explosive Ray (30,000 ki) and speed-impact Explosive Flash (40,000 ki / 20,000 trigger); Special Beam Cannon ult (50,000 ki)"
weaknesses:
  - "DP9 premium — expensive even if efficient"
  - "No super-armor; relies on Beast Sense reads to defend"
  - "Guess It's My Turn punishable on activation"
howToFight: "Beast Sense is his defensive crutch — bait it with staggered pressure, then punish the whiff. Don't feed Guess It's My Turn (4-stock, no-auto-guard) reads. He has no armor, so ~2f Super Counters and Perception (2 stock) break his turns; starve ki to keep Explosive Flash and the ult offline. Respect his damage — one clean confirm hurts."
summary: "DP9 Gohan Beast; giant-ish (null HP), 2,000 ki recovery, Beast Sense + Guess It's My Turn (4 stock), Explosive Flash 40k-ki; best dual-meta pick (#10 Singles 128.7k, #1 DP 33.9k)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

