---
slug: "kale-super-saiyan-berserk"
name: "Kale, Super Saiyan (Berserk)"
charId: "0911_00"
baseCharacter: "Kale"
era: "Super"
dp: 7
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
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
moveset:
  - name: "Berserk Rage"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Cry of Rage"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Gigantic Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gigantic Throw"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Berserk Blaster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "Z"
dpTier: "Z"
singlesScore: 129.1
dpScore: 25.5
playable: true
playstyle: "S-tier berserker"
strengths:
  - "Top-bracket 45,000 HP berserker — strong in BOTH modes (#9 Singles 129.1, 25.5 DP)"
  - "Cry of Rage S1 is unblockable + no-auto-guard for a guaranteed-style opener (activation time raised May-2026)"
  - "Berserk Rage S2 (4 stock) no-auto-guard buff stacks huge damage"
  - "Gigantic Impact (30,000 ki) and speed-impact Gigantic Throw (30,000 ki / 15,000 trigger); Berserk Blaster ult (50,000 ki)"
weaknesses:
  - "Cry of Rage activation time was increased in May-2026 — slower to deploy"
  - "Average 1,750 ki recovery for a DP7"
  - "Berserk Rage punishable on activation"
howToFight: "Cry of Rage is unblockable but its activation is now slower (May-2026 nerf) — react and vanish (≈half a ki bar) it, then punish. Don't trade into her 45,000 HP and damage buffs; use Super Counters (~2f) to interrupt. Punish Berserk Rage activations and starve ki to keep her ult offline."
summary: "DP7 Kale Berserk; 45k HP, unblockable Cry of Rage + Berserk Rage (4 stock), Gigantic Throw speed-impact; #9 Singles (129.1)/25.5 DP."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

