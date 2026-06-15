---
slug: "frost"
name: "Frost"
charId: "0881_00"
baseCharacter: "Frost"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
unlock: "90,000 Zeni (shop)"
moveset:
  - name: "Welcome to My World"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Chaos Beam"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Secret Poison"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Chaos Ball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Buffing trickster"
strengths:
  - "Welcome to My World S2 (4 stock) is a no-auto-guard damage buff"
  - "Explosive Wave S1 (free) reversal/space-maker"
  - "Two 30,000-ki supers (one speed-impact at 15,000 trigger) plus Chaos Ball ult (50,000 ki)"
  - "Standard 40,000 HP and 1,750 recovery — no glaring weakness"
weaknesses:
  - "DP6 with no transform — fixed ceiling"
  - "Average recovery, no teleport/mobility tool"
  - "Welcome to My World punishable on activation"
howToFight: "Punish Welcome to My World (4-stock, no-auto-guard) to deny his buff. Bait Explosive Wave with a stagger. No escape tool means sustained pressure works; starve ki to keep Chaos Ball offline."
summary: "DP6 Frost; 40k HP, Welcome to My World (4 stock) buff, twin 30k-ki supers + Chaos Ball ult — Frieza-race trickster."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

