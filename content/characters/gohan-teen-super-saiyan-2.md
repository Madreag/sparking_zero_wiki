---
slug: "gohan-teen-super-saiyan-2"
name: "Gohan (Teen), Super Saiyan 2"
charId: "0031_02"
baseCharacter: "Gohan (Teen)"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Unforgivable"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 20000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Explosive Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Father-Son Kamehameha"
    type: "ultimate"
    kiCost: 50000
tier: "B"
playable: true
playstyle: "Rushdown finisher"
strengths:
  - "B-tier; Father-Son Kamehameha 50,000-ki signature ultimate (iconic beam)"
  - "Super Kamehameha here is a cheap 20,000-ki super + Explosive Rush speed-impact (15,000 on trigger)"
  - "Unforgivable (4 stock) rage attack buff; 8.0 ki charge / 1,500/s recovery"
  - "Top of the Teen Gohan transform chain (2 stock from base)"
weaknesses:
  - "No auto-dodge (Explosive Wave + Unforgivable) — defense is Super Counter only"
  - "DP7; must climb the transform ladder to reach SS2"
  - "40,000-equivalent durability, no heal"
howToFight: "Punish before he reaches SS2. With no evasive skill he trades poorly into Super Counter (free) and vanish. Respect Father-Son Kamehameha on knockdown and Perception (2 stock) the Explosive Rush."
summary: "DP7 Gohan (Teen) SS2: B-tier; 40,000 HP, 8.0 ki charge; cheap Super Kamehameha (20,000 ki) + Father-Son Kamehameha 50,000-ki ult; Unforgivable (4 stock)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

