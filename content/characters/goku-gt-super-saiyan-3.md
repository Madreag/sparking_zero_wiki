---
slug: "goku-gt-super-saiyan-3"
name: "Goku (GT), Super Saiyan 3"
charId: "0002_32"
baseCharacter: "Goku (GT)"
era: "GT"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (GT), Super Saiyan 4"
    targetSlug: "goku-gt-super-saiyan-4"
    cost: 1
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Saiyan Spirit"
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
      - "weak-vs-shield"
  - name: "Dragon Fist"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Beam zoner"
strengths:
  - "Super Kamehameha (30,000-ki super)"
  - "Full-Power Energy Blast Volley (30,000-ki super)"
  - "Dragon Fist 50,000-ki ultimate finisher"
  - "Saiyan Spirit ki/attack buff"
  - "High-Tension self ki-charge buff"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Respect Dragon Fist on knockdown — bait it out and punish the recovery."
summary: "DP7 GT-era fighter; 40,000 HP; Super Kamehameha 30,000-ki super, Dragon Fist 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

