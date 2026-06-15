---
slug: "fusion-android-13"
name: "Fusion Android 13"
charId: "0621_00"
baseCharacter: "Fusion Android 13"
era: "Movie"
dp: 7
source: "Base"
classes:
  - "Giant"
  - "Android"
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 2000
kiAutoRecoveryLimit: 50000
initialKi: 30000
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
moveset:
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "Android Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "S.S. Deadly Bomber"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Super Explosive Wave"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Explosive Wave"
  - name: "S.S. Deadly Hammer"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
tier: "S"
playable: true
playstyle: "Armored fusion anchor"
strengths:
  - "Triple-class Giant/Android/Fusion: 45,000 HP, giant armor, plus android 2,000 ki recovery"
  - "Surprise high-tier — #13 Singles (125.2k) AND strong 24.7k DP value"
  - "Android Barrier S1 (3 stock) gives an on-demand absorbing shield"
  - "S.S. Deadly Bomber (30,000 ki) and Super Explosive Wave (40,000 ki) plus S.S. Deadly Hammer ult (50,000 ki)"
  - "Pump Up S2 (free) stacks more armored damage"
weaknesses:
  - "DP7 for a giant-class body means it ate the May-2026 giant nerfs (more melee taken, slower back-dash)"
  - "8.0/0.0 charge profile leans entirely on auto-recovery"
  - "Barrier is its main escape and costs 3 stock"
howToFight: "Treat it like a giant: standard charge Blasts now damage and knock it back, so zone it out. Force the 3-stock Android Barrier, then pressure on its cooldown. Avoid grabs (giant immunity) and don't trade into the 45,000-HP armor — punish whiffed swings during its long recovery."
summary: "DP7 Giant/Android fusion; 45k HP, surprise S-tier (#13, 125.2k / 24.7k DP), Android Barrier (3 stock) + 2,000 ki recovery."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

