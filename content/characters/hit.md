---
slug: "hit"
name: "Hit"
charId: "0870_00"
baseCharacter: "Hit"
era: "Super"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
  - name: "Time Skip"
    type: "blast1"
    notes: "slot S2"
  - name: "Ki Clone"
    type: "blast1"
    notes: "slot S1"
  - name: "Assassin's Art"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "weak-vs-shield"
  - name: "Time Skip/Jump Spike"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Time Prison"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Time-skip counter assassin"
strengths:
  - "Time Skip S2 (free) freezes the opponent for guaranteed punishes — signature control tool"
  - "Ki Clone S1 (free) creates a decoy for mix-ups and zoning"
  - "Time Skip/Jump Spike super at 40,000 ki (20,000 trigger, speed-impact) is a heavy time-stop catch"
  - "Time Prison ult (50,000 ki) is a powerful lockdown finisher"
weaknesses:
  - "Only 40,000 HP for a DP8 — not durable"
  - "Average 1,750 ki recovery; no super-armor"
  - "Counter-reliant — struggles when forced to open you up"
howToFight: "Respect Time Skip — don't commit to a long string he can freeze and punish; use short, staggered pokes. Bait Ki Clone and hit the real Hit. His 40,000 HP is low for the cost, so once you get in, convert hard before he resets with another Time Skip."
summary: "DP8 Hit; 40k HP, Time Skip + Ki Clone, Time Skip/Jump Spike speed-impact super + Time Prison ult — counter-assassin."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

