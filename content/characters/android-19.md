---
slug: "android-19"
name: "Android 19"
charId: "0470_00"
baseCharacter: "Android 19"
era: "Z"
dp: 4
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 4500
initialKi: 40000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
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
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Power Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Drain Life 19"
    type: "ultimate"
    kiCost: 50000
    damage: 9270
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Android drain zoner"
strengths:
  - "Full-Power Energy Wave (30,000-ki super)"
  - "High Power Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Drain Life 19 50,000-ki ultimate finisher"
  - "False Courage instant ki gain"
  - "Pump Up defense buff"
weaknesses:
  - "Android: cannot manually charge ki (charge speed 0, 4,500/s passive only) — slow to reach supers"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Exploit that he can't charge ki — rush him before passive recovery funds his supers. Perception (2 stock) or vanish the High Power Rush rather than mashing into it. He can't auto-reflect (DP<7 under the May 2026 rule), so contest his blasts freely."
summary: "DP4 Z-era android; 40,000 HP; Full-Power Energy Wave 30,000-ki super, Drain Life 19 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

