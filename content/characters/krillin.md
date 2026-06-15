---
slug: "krillin"
name: "Krillin"
charId: "0050_00"
baseCharacter: "Krillin"
era: "Z"
dp: 3
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
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
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Spread Energy Wave"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
    notes: "chip 1,140"
  - name: "Chain Destructo Disc"
    type: "ultimate"
    kiCost: 50000
    damage: 1000
    properties:
      - "Continuous Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
    notes: "chip 1,500"
playable: true
playstyle: "All-rounder fighter"
strengths:
  - "Chain Destructo Disc 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Afterimage Strike auto-dodge (3 stock; ends on a Super Counter post-May-2026)"
  - "DP3 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish; don't feed raw strings into it. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Chain Destructo Disc on knockdown — bait it out and punish the recovery."
summary: "DP3 Z-era fighter; 35,000 HP; Chain Destructo Disc 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

