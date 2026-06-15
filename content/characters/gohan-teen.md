---
slug: "gohan-teen"
name: "Gohan (Teen)"
charId: "0031_00"
baseCharacter: "Gohan (Teen)"
era: "Z"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gohan (Teen), Super Saiyan"
    targetSlug: "gohan-teen-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Gohan (Teen), Super Saiyan 2"
    targetSlug: "gohan-teen-super-saiyan-2"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Energy Blast Barrage"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Beam"
      - "In Sparking! Mode"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Masenko (30,000-ki super)"
  - "Energy Blast Barrage (20,000-ki super)"
  - "Super Kamehameha 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Super Kamehameha on knockdown — bait it out and punish the recovery."
summary: "DP4 Z-era fighter; 40,000 HP; Super Masenko 30,000-ki super, Super Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

