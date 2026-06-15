---
slug: "gohan-future"
name: "Gohan (Future)"
charId: "0032_30"
baseCharacter: "Gohan (Adult)"
era: "Z"
dp: 5
source: "Martial Arts Pack"
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
  - target: "Gohan (Future), Super Saiyan"
    targetSlug: "gohan-future-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Destructive Wave"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Explosive Wave"
  - name: "Super Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Masenko (30,000-ki super)"
  - "Super Destructive Wave (40,000-ki super)"
  - "Super Kamehameha 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "Transforms (1 stock to Gohan (Future)) for a mid-match power spike"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Super Kamehameha on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Super Destructive Wave 40,000-ki super, Super Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

