---
slug: "cooler"
name: "Cooler"
charId: "0600_00"
baseCharacter: "Cooler"
era: "Movie"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Cooler, Final Form"
    targetSlug: "cooler-final-form"
    cost: 2
    kind: "transform"
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Psychokinesis"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Darkness Eye Beam"
    type: "blast2"
    kiCost: 20000
  - name: "Death Ball"
    type: "ultimate"
    kiCost: 50000
tier: "C"
playable: true
playstyle: "Unblockable-poke base"
strengths:
  - "Psychokinesis S1 is unblockable + no-auto-guard and free — a cheap stun opener"
  - "Afterimage S2 (free) gives a 1-hit auto-dodge read"
  - "Transforms to Final Form for 2 stocks with a +6,000 HP heal"
  - "Death Ball ult at 50,000 ki"
weaknesses:
  - "DP6 base is C-tier; you want Final Form or the Metal Cooler variant"
  - "Average 1,750 recovery, no teleport in base"
  - "Unblockable is slow and vanish-evadable"
howToFight: "Vanish (≈half a ki bar) the telegraphed Psychokinesis rather than guarding. Deny the 2-stock transform to Final Form by keeping him stock-starved. Afterimage is a single-hit read — stagger and bait it, then punish."
summary: "DP6 Cooler base; 40k HP, unblockable Psychokinesis S1 + Afterimage; 2-stock transform to Final Form (+6,000 HP)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

