---
slug: "vegeta-z-end-super-saiyan-2"
name: "Vegeta (Z - End), Super Saiyan 2"
charId: "0020_32"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Big Bang Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Infinite Blaster"
    type: "blast2"
    kiCost: 20000
  - name: "Infinity Flasher"
    type: "ultimate"
    kiCost: 50000
    damage: 12500
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Big Bang Attack (30,000-ki super)"
  - "Infinite Blaster (20,000-ki super)"
  - "Infinity Flasher 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Infinity Flasher on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Big Bang Attack 30,000-ki super, Infinity Flasher 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

