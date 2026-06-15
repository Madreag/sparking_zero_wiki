---
slug: "trunks-melee"
name: "Trunks (Melee)"
charId: "0080_10"
baseCharacter: "Trunks (Sword)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Trunks (Melee), Super Saiyan"
    targetSlug: "trunks-melee-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Super Trunks"
    targetSlug: "super-trunks"
    cost: 2
    kind: "transform"
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Burning Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Finish Buster"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Burning Attack (30,000-ki super)"
  - "High Speed Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Finish Buster 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the High Speed Rush rather than mashing into it."
summary: "DP5 Z-era fighter; 40,000 HP; Burning Attack 30,000-ki super, Finish Buster 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

