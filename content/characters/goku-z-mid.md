---
slug: "goku-z-mid"
name: "Goku (Z - Mid)"
charId: "0000_10"
baseCharacter: "Goku (Z - Early)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (Z - Mid), Super Saiyan"
    targetSlug: "goku-z-mid-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "I Can't Wait!"
    type: "blast1"
    notes: "slot S2"
  - name: "Give Me Your Energy!"
    type: "blast1"
    notes: "slot S1"
  - name: "x20 Kaioken Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Kaioken Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Spirit Bomb"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "x20 Kaioken Kamehameha (30,000-ki super)"
  - "Kaioken Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Spirit Bomb 50,000-ki ultimate finisher"
  - "Transforms (1 stock to Goku (Z - Mid)) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Kaioken Rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; x20 Kaioken Kamehameha 30,000-ki super, Spirit Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

