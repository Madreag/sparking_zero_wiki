---
slug: "dabura"
name: "Dabura"
charId: "0500_00"
baseCharacter: "Dabura"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Evil Breath"
    type: "blast1"
    skillCost: 1
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Evil Impulse"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Evil Flame"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Short-range energy attack"
      - "Unguardable"
      - "vanish: erase"
  - name: "Dark Sword Strike"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Unblockable-poke zoner"
strengths:
  - "Evil Breath S1 costs just 1 skill stock and is unblockable + no-auto-guard — a cheap chip/mix-up opener"
  - "Afterimage Strike (3 stock) gives a launch-era auto-dodge window for stalling pressure"
  - "Twin 30,000-ki supers (Evil Impulse, Evil Flame) plus 50,000-ki Dark Sword Strike ult give consistent finishers"
  - "Standard 40,000 HP and 1,750 ki recovery — no glaring durability hole"
weaknesses:
  - "DP6 with no transform — fixed ceiling, no scaling payoff"
  - "Afterimage Strike now ends the moment you land a Super Counter (post-May-2026)"
  - "No mobility/teleport tool; outpaced by fusions and divine picks"
howToFight: "Bait Evil Breath on block — it is unblockable but slow, so sidestep with a vanish (≈half a ki bar) or dash. If Dabura pops Afterimage Strike, land one ~2f Super Counter to delete it instantly, then punish the 3-stock investment. He has no escape button, so corner him and keep your turn."
summary: "DP6 Z-villain bruiser; 40k HP, unblockable Evil Breath (1 stock) + Afterimage Strike (3 stock) defensive kit."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

