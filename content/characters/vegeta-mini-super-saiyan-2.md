---
slug: "vegeta-mini-super-saiyan-2"
name: "Vegeta (Mini), Super Saiyan 2"
charId: "3060_02"
baseCharacter: "Vegeta (Mini)"
era: "DAIMA"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Mini), Super Saiyan 3"
    targetSlug: "vegeta-mini-super-saiyan-3"
    cost: 1
    kind: "transform"
moveset:
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Galick Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Head-On Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Big Bang Attack"
    type: "ultimate"
    kiCost: 50000
dpTier: "Z"
dpScore: 24.8
playable: true
playstyle: "Mini SS2 (AIS)"
strengths:
  - "Afterimage Strike S2 (3 stock) gives a launch-era auto-dodge window"
  - "Cheap 1-stock transform onward to SS3"
  - "Galick Gun and Head-On Impact both at 30,000 ki; Big Bang Attack ult (50,000 ki)"
  - "Explosive Wave S1 (free) reversal"
weaknesses:
  - "DP6 mid-form; weaker than SS3"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Afterimage Strike ends on a Super Counter"
howToFight: "If he pops Afterimage Strike, land a ~2f Super Counter to delete it. Keep him off the 1-stock SS3 transform. Starve ki and pressure the 40,000-HP body."
summary: "DP6 Vegeta (Mini) SS2; 40k HP, Afterimage Strike (3 stock) + Explosive Wave, Big Bang Attack ult; 1-stock to SS3."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

