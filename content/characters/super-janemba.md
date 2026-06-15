---
slug: "super-janemba"
name: "Super Janemba"
charId: "0651_00"
baseCharacter: "Super Janemba"
era: "Movie"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 5.5
kiAutoRecovery: 2250
initialKi: 30000
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Dimension Shift"
    type: "blast1"
    notes: "slot S2"
  - name: "Mystic Breath"
    type: "blast1"
    skillCost: 1
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Evil Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Lightning Shower Rain"
    type: "blast2"
    kiCost: 30000
    damage: 1040
    hits: 11
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
      - "vanish: erase"
    notes: "chip 208"
  - name: "Dimension Sword Attack"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Teleport unblockable zoner"
strengths:
  - "Elite 2,250 ki auto-recovery (highest bracket) keeps blasts and ult funded"
  - "Dimension Shift S2 (free) gives teleport mobility/escape"
  - "Mystic Breath S1 stays unblockable + no-auto-guard at 1 stock for stun mix-ups"
  - "Evil Cannon and Lightning Shower Rain both at 30,000 ki; Dimension Sword Attack ult (50,000 ki)"
weaknesses:
  - "Only 40,000 HP — not durable for a DP7"
  - "No super-armor; loses straight trades"
  - "Relies on teleport spacing rather than raw power"
howToFight: "He teleports with Dimension Shift, so bait the escape with a delayed string then catch the landing. Vanish (≈half a ki bar) the unblockable Mystic Breath. His 2,250 recovery means you can't out-zone him — close the gap and punish his 40,000 HP with melee."
summary: "DP7 Super Janemba; 40k HP, top 2,250 ki recovery, Dimension Shift teleport + unblockable Mystic Breath; strong neutral."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

