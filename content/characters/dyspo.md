---
slug: "dyspo"
name: "Dyspo"
charId: "0950_00"
baseCharacter: "Dyspo"
era: "Super"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
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
unlock: "90,000 Zeni (shop)"
moveset:
  - name: "Pride Trooper Pose 2"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Super Maximum Light Speed Mode"
    type: "blast1"
    notes: "slot S1"
  - name: "Justice Crusher"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Justice Kick"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "United Justice Stream"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Hyper-speed rushdown"
strengths:
  - "Super Maximum Light Speed Mode S1 (free) is a signature speed buff for relentless rushdown"
  - "Justice Crusher (30,000 ki) and speed-impact Justice Kick (30,000 ki / 15,000 trigger); United Justice Stream ult (50,000 ki)"
  - "Pride Trooper Pose 2 S2 (4 stock) no-auto-guard buff"
  - "Standard 40,000 HP and 1,750 recovery"
weaknesses:
  - "Lowest DP score in the game (8.3k) — heavily outclassed in DP Battle"
  - "No transform; fixed ceiling"
  - "Light-speed mode is his only real gimmick; punishable buffs"
howToFight: "His speed buff makes him fast but he has no armor and only 40,000 HP — use Perception (2 stock) and ~2f Super Counters to interrupt the rushdown. Punish Pride Trooper Pose 2 (no-auto-guard). Once you catch him, he folds; don't get flustered by the speed."
summary: "DP6 Dyspo; 40k HP, Super Maximum Light Speed Mode (free) speed buff, Justice Kick speed-impact; DP-floor (8.3k lowest)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

