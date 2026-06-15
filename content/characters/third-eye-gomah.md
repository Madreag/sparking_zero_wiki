---
slug: "third-eye-gomah"
name: "Third Eye Gomah"
charId: "3080_00"
baseCharacter: "Third Eye Gomah"
era: "DAIMA"
dp: 7
source: "Dragon Ball DAIMA Character Pack 2"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.1
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
transformsTo:
  - target: "Giant Gomah"
    targetSlug: "giant-gomah"
    cost: 3
    kind: "transform"
moveset:
  - name: "Third Eye Barrier"
    type: "blast1"
    notes: "slot S2"
  - name: "Magic Bind"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Magic Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Magic Stream"
    type: "blast2"
    kiCost: 20000
  - name: "Magic Burst"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Magic-trap base"
strengths:
  - "Magic Bind S1 is unblockable + no-auto-guard for a free binding opener"
  - "Third Eye Barrier S2 (free) absorbing shield at no stock cost"
  - "Three-stock transform to Giant Gomah banking +10,000 HP"
  - "Magic Cannon (30,000 ki) and Magic Stream (20,000 ki); Magic Burst ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP until it apes out"
  - "Average 1,750 recovery, no teleport"
  - "Unblockable bind is vanish-evadable"
howToFight: "Vanish (≈half a ki bar) the unblockable Magic Bind. Bait out Third Eye Barrier, then pressure. Deny the 3-stock transform to Giant Gomah (+10,000 HP swing) by keeping him stock-starved."
summary: "DP7 Third Eye Gomah; 40k HP, unblockable Magic Bind + Third Eye Barrier, Magic Cannon; 3-stock transform to Giant Gomah (+10,000 HP)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

