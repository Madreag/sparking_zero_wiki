---
slug: "goku-black-super-saiyan-ros"
name: "Goku Black, Super Saiyan Rosé"
charId: "0800_01"
baseCharacter: "Goku Black"
era: "Super"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 9
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Fused Zamasu"
    targetSlug: "fused-zamasu"
    cost: 3
    kind: "fusion"
moveset:
  - name: "Audacious Laugh"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Black Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Godly Display Slash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Godly Black Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "A"
playable: true
playstyle: "Teleport okizeme specialist"
strengths:
  - "Strong pressure/okizeme kit — A-tier Singles (113.0k) and solid DP body (20.7k)"
  - "Instant Transmission S1 (free) gives true teleport mix-ups and escape"
  - "Potara-fuses with Zamasu into the DP8 Fused Zamasu for 3 stocks — a comeback option"
  - "Godly Display Slash super at 30,000 ki (15,000 trigger, speed-impact); Godly Black Kamehameha ult (50,000 ki)"
  - "Audacious Laugh S2 (4 stock) no-auto-guard buff"
weaknesses:
  - "Only 40,000 HP and slow 1,500 ki recovery — fragile for a DP8"
  - "Leans on teleport mix-ups rather than raw durability"
  - "Audacious Laugh punishable on activation"
howToFight: "He lives on Instant Transmission okizeme — block patiently through the teleport mix-up, and bait the TP with a delayed button to catch the landing. Punish Audacious Laugh (4-stock, no-auto-guard). His 40,000 HP and weak recovery mean once you get a turn, press it — and watch for the 3-stock Potara into Fused Zamasu if Zamasu is on the team."
summary: "DP8 Goku Black Rosé; 40k HP, Instant Transmission + Audacious Laugh (4 stock), Godly Display Slash; A-tier pressure/okizeme (113.0k), Potara into Fused Zamasu."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

