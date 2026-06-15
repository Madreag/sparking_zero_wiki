---
slug: "majin-duu"
name: "Majin Duu"
charId: "3140_00"
baseCharacter: "Majin Duu"
era: "DAIMA"
dp: 7
source: "Dragon Ball DAIMA Character Pack 2"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Snack Time"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Powerful Shout"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Powerful Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Rolling Attack"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "speed-impact"
  - name: "Full-Power Special Attack"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Unblockable heal brawler"
strengths:
  - "Powerful Shout S1 is unblockable + no-auto-guard for a free stun opener"
  - "Snack Time S2 (4 stock) no-auto-guard heal/sustain tool"
  - "Powerful Cannon (30,000 ki) and speed-impact Rolling Attack (40,000 ki); Full-Power Special Attack ult (50,000 ki)"
weaknesses:
  - "DP7 with only 40,000 HP — fragile for the cost"
  - "Average 1,750 recovery, no teleport"
  - "Unblockable is vanish-evadable; Snack Time punishable"
howToFight: "Vanish (≈half a ki bar) the unblockable Powerful Shout. Punish Snack Time (4-stock, no-auto-guard) to deny the heal. His 40,000 HP is low for DP7 — convert hard once in and starve ki to keep his ult offline."
summary: "DP7 Majin Duu; 40k HP, unblockable Powerful Shout + Snack Time (4 stock) heal, Rolling Attack speed-impact + Full-Power Special Attack ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

