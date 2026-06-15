---
slug: "great-ape-vegeta"
name: "Great Ape Vegeta"
charId: "0023_00"
baseCharacter: "Great Ape Vegeta"
era: "Z"
dp: 5
source: "Base"
classes:
  - "Giant"
hp: 45000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
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
moveset:
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Chou Makouhou"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Chou Makouhou Barrage"
    type: "blast2"
    kiCost: 30000
    damage: 2234
    hits: 4
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
    notes: "chip 447"
  - name: "Super Galick Gun"
    type: "ultimate"
    kiCost: 50000
    damage: 14000
tier: "C"
playable: true
playstyle: "Giant AoE wall"
strengths:
  - "Giant-class: 45,000 HP and hyper-armor on big-body attacks — AoE wall pressure"
  - "Two 30,000-ki Chou Makouhou mouth-beams plus Super Galick Gun 50,000-ki ult"
  - "Howl (4 stock) buff; reached as a transform from base Z-Scouter Vegeta (heals 10,000 HP on the change)"
  - "C-tier but threatening vs unprepared opponents"
weaknesses:
  - "Giants nerfed May 2026: less rush/smash damage, more whiff recovery, take more melee damage, slower back-dash; normal charge Blasts now knock giants back"
  - "Huge hurtbox — easy to combo and zone"
  - "DP5 with no evasion; immobile relative to normal-size fighters"
howToFight: "Use the post-May-2026 anti-giant tools: charge Blasts now damage and knock him back, and he takes extra melee damage with slow recovery on whiffs. Stay mobile, punish his laggy big-body swings, and avoid standing in the Chou Makouhou AoE."
summary: "DP5 Great Ape Vegeta (Giant): C-tier; 45,000 HP; Chou Makouhou + Chou Makouhou Barrage (both 30,000 ki) + Super Galick Gun 50,000-ki ult; Giants broadly nerfed May 2026."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

