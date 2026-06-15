---
slug: "panzy"
name: "Panzy"
charId: "3130_00"
baseCharacter: "Panzy"
era: "DAIMA"
dp: 2
source: "Dragon Ball DAIMA Character Pack 1"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
initialSkillStock: 2
sparkingDrainPerSec: 2800
kiBlastShots: 5
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Last Chance Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wasabi Bomb"
    type: "blast1"
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Last Chance Shot"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Last Chance Shock"
    type: "blast2"
    kiCost: 40000
    damage: 4500
    properties:
      - "Fire"
      - "Unguardable"
      - "Played after a hit"
    notes: "Trigger cost 20,000 ki"
  - name: "Kadan Combination"
    type: "ultimate"
    kiCost: 50000
tier: "D"
playable: true
playstyle: "Cheap gimmick body"
strengths:
  - "DP2 cost makes her near-free filler"
  - "Wasabi Bomb S1 (free) is a no-auto-guard status/trap tool"
  - "Last Chance Full Power S2 (4 stock) no-auto-guard comeback buff"
  - "Last Chance Shot (20,000 ki) and Last Chance Shock (40,000 ki); Kadan Combination ult (50,000 ki)"
weaknesses:
  - "Rock-bottom 30,000 HP — dies to one combo in DP scaling"
  - "D-tier joke character; no transform, no mobility"
  - "Both skills are punishable on activation"
howToFight: "She has only 30,000 HP — open her up and delete the slot. Don't respect Wasabi Bomb; block or step it. Punish Last Chance Full Power (no-auto-guard). Nothing to fear defensively; convert one combo to remove her."
summary: "DP2 Panzy; only 30k HP, Wasabi Bomb (no-auto-guard) + Last Chance Full Power (4 stock), Last Chance supers; D-tier joke."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

