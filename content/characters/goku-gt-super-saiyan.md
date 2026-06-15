---
slug: "goku-gt-super-saiyan"
name: "Goku (GT), Super Saiyan"
charId: "0002_31"
baseCharacter: "Goku (GT)"
era: "GT"
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
  - target: "Goku (GT), Super Saiyan 3"
    targetSlug: "goku-gt-super-saiyan-3"
    cost: 1
    kind: "transform"
  - target: "Goku (GT), Super Saiyan 4"
    targetSlug: "goku-gt-super-saiyan-4"
    cost: 2
    kind: "transform"
moveset:
  - name: "Full Power"
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
  - name: "Full-Power Energy Blast Volley"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Super Explosive Wave"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Full-Power Energy Blast Volley (30,000-ki super)"
  - "Super Explosive Wave 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "Full Power attack buff (4 stock)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Super Explosive Wave on knockdown — bait it out and punish the recovery."
summary: "DP6 GT-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Super Explosive Wave 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

