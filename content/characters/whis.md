---
slug: "whis"
name: "Whis"
charId: "0790_00"
baseCharacter: "Whis"
era: "Super"
dp: 10
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 5.5
kiAutoRecovery: 2250
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 18
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Snack Time"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Prelude to Destruction"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Symphonic Destruction"
    type: "blast2"
    kiCost: 20000
    damage: 750
    properties:
      - "Short-range energy attack"
    notes: "chip 300"
  - name: "Epilogue to Destruction"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "Z"
dpTier: "C"
singlesScore: 135.4
dpScore: 13.5
playable: true
playstyle: "Auto-dodge deity"
strengths:
  - "Elite 2,250 ki recovery (highest bracket) plus 45,000 HP — never starved, hard to kill"
  - "Best-in-class mobility and auto-dodge defense; #6 Singles (135.4)"
  - "Barrier S1 (3 stock) absorbing shield + Snack Time S2 (4 stock) utility"
  - "Prelude to Destruction (30,000 ki), Symphonic Destruction (20,000 ki), Epilogue to Destruction ult (50,000 ki)"
weaknesses:
  - "May-2026: Rush Chain now executes even through his auto-dodge — the dodge is no longer un-pressurable"
  - "Symphonic Destruction is now high-speed-evadable"
  - "DP10, awful DP efficiency (13.5); no super-armor — purely evasive"
howToFight: "Use Rush Chain — post-May-2026 it lands even while he's auto-dodging, the key counter to Whis. High-speed-evade his Symphonic Destruction. Force out the 3-stock Barrier, then pressure on cooldown. He has 45,000 HP and elite ki, so you won't out-resource him — you out-read him with Rush Chain and Super Counters (~2f)."
summary: "DP10 Angel; 45k HP, top 2,250 ki recovery, auto-dodge + Barrier (3 stock), Symphonic Destruction; #6 Singles (135.4), now Rush-Chain-counterable."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

