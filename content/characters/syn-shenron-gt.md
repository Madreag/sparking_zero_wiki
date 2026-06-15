---
slug: "syn-shenron-gt"
name: "Syn Shenron (GT)"
charId: "0700_00"
baseCharacter: "Syn Shenron (GT)"
era: "GT"
dp: 7
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
transformsTo:
  - target: "Omega Shenron (GT)"
    targetSlug: "omega-shenron-gt"
    cost: 2
    kind: "transform"
moveset:
  - name: "Mystic Breath"
    type: "blast1"
    skillCost: 1
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Trap Shooter"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Blazing Storm"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Mow down and explode"
  - name: "Gigantic Blaze"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Attack opponent's location"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Unblockable-poke base"
strengths:
  - "Mystic Breath S2 is unblockable + no-auto-guard for 1 stock — cheap stun opener"
  - "Two-stock transform to the A-tier Omega Shenron (+5,000 HP heal)"
  - "Cheap supers Trap Shooter and Blazing Storm at 20,000 ki each"
  - "Gigantic Blaze ult (50,000 ki); Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP7 base is the weaker half of the line — you want Omega"
  - "Average 1,750 recovery, no teleport"
  - "Unblockable is vanish-evadable"
howToFight: "Deny the 2-stock transform to Omega Shenron. Vanish (≈half a ki bar) the unblockable Mystic Breath. He has no escape tool in base — keep continuous pressure and starve his stocks."
summary: "DP7 Syn Shenron; 40k HP, unblockable Mystic Breath (1 stock), twin 20k-ki supers; 2-stock transform to A-tier Omega."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

