---
slug: "goku-z-end-super-saiyan"
name: "Goku (Z - End), Super Saiyan"
charId: "0000_21"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (Z - End), Super Saiyan 2"
    targetSlug: "goku-z-end-super-saiyan-2"
    cost: 1
    kind: "transform"
  - target: "Goku (Z - End), Super Saiyan 3"
    targetSlug: "goku-z-end-super-saiyan-3"
    cost: 2
    kind: "transform"
moveset:
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Energy Wave Combo"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Instant Transmission Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Super Energy Wave Combo (30,000-ki super)"
  - "Instant Transmission Kamehameha 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Instant Transmission Kamehameha on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Instant Transmission Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

