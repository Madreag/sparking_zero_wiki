---
slug: "android-17-z"
name: "Android 17 (Z)"
charId: "0450_00"
baseCharacter: "Android 17 (Z)"
era: "Z"
dp: 5
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 1800
kiAutoRecoveryLimit: 50000
initialKi: 30000
maxSkillStock: 4
initialSkillStock: 1
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
  - name: "Finish Sign"
    type: "blast1"
    notes: "slot S2"
  - name: "Android Barrier"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Ball"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Photon Flash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Sadistic Dance"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "C"
playable: true
playstyle: "Barrier zoner"
strengths:
  - "C-tier; Android Barrier block and Sadistic Dance 50,000-ki ultimate"
  - "Two 30,000-ki supers (Full-Power Energy Ball, Photon Flash) for zoning"
  - "DP5 efficient filler"
  - "40,000 HP baseline"
weaknesses:
  - "Android: cannot manually charge ki (1,800/s passive only) — slow to reach supers"
  - "C-tier; Android Barrier is a block, not evasion; no heal"
  - "Below DP7 so no auto-reflect in Sparking mode"
howToFight: "Rush him before passive recovery funds supers. Bait Android Barrier and punish. Super Counter (free) his approaches; he can't auto-reflect (DP5 < 7)."
summary: "DP5 Android 17 (Z): C-tier; 40,000 HP; CANNOT charge ki (0 charge, 1,800/s recovery); Photon Flash + Full-Power Energy Ball (both 30,000 ki) + Sadistic Dance 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

