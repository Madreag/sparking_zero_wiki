---
slug: "uub-gt"
name: "Uub (GT)"
charId: "0240_00"
baseCharacter: "Uub (GT)"
era: "GT"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
transformsTo:
  - target: "Majuub (GT)"
    targetSlug: "majuub-gt"
    cost: 2
    kind: "transform"
moveset:
  - name: "Power Up to the Very Limit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
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
  - name: "Blazing Barrage Palm"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Explosive Wave"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Blazing Barrage Palm (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Super Explosive Wave 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "DP4 — efficient DP-queue filler; frees budget for a premium carry"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Perception (2 stock) or vanish the Blazing Barrage Palm rush rather than mashing into it."
summary: "DP4 GT-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Super Explosive Wave 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

