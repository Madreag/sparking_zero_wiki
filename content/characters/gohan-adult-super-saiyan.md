---
slug: "gohan-adult-super-saiyan"
name: "Gohan (Adult), Super Saiyan"
charId: "0032_01"
baseCharacter: "Gohan (Adult)"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Gohan (Adult), Super Saiyan 2"
    targetSlug: "gohan-adult-super-saiyan-2"
    cost: 1
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Explosive Cannon"
    type: "blast2"
    kiCost: 20000
    properties:
      - "vanish: erase"
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Bros. Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Explosive Cannon (20,000-ki super)"
  - "Full-Power Energy Blast Volley (30,000-ki super)"
  - "Bros. Kamehameha 50,000-ki ultimate finisher"
  - "Explosive Wave knockback/ki-shield reset"
  - "Transforms (1 stock to Gohan (Adult)) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Bros. Kamehameha on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Full-Power Energy Blast Volley 30,000-ki super, Bros. Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

