---
slug: "goku-super-super-saiyan-god"
name: "Goku (Super), Super Saiyan God"
charId: "0001_42"
baseCharacter: "Goku (Super)"
era: "Super"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
  - target: "Goku (Super), Super Saiyan God Super Saiyan"
    targetSlug: "goku-super-super-saiyan-god-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Goku (Super)"
    targetSlug: "goku-super"
    cost: 0
    kind: "transform"
moveset:
  - name: "Shenron Aura"
    type: "blast1"
    notes: "slot S2"
  - name: "God Bind"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "God Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "God Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "God Burst Kamehameha"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "God Kamehameha (30,000-ki super)"
  - "God Impact (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "God Burst Kamehameha 50,000-ki ultimate finisher"
  - "Transforms (1 stock to Goku (Super)) for a mid-match power spike"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the God Impact rush rather than mashing into it."
summary: "DP7 Super-era fighter; 40,000 HP; God Kamehameha 30,000-ki super, God Burst Kamehameha 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

