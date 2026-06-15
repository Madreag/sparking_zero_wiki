---
slug: "glorio"
name: "Glorio"
charId: "3070_00"
baseCharacter: "Glorio"
era: "DAIMA"
dp: 4
source: "Dragon Ball DAIMA Character Pack 1"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Thunder Charge"
    type: "blast1"
    notes: "slot S2"
  - name: "Spark Bind"
    type: "blast1"
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Bolt Buster"
    type: "blast2"
    kiCost: 20000
    properties:
      - "weak-vs-shield"
  - name: "Electric Whip"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Lightning Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Short-range energy attack"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Lightning trap skirmisher"
strengths:
  - "Spark Bind S1 (free) is a no-auto-guard binding/stun tool"
  - "Thunder Charge S2 (free) builds meter for free"
  - "Bolt Buster (20,000 ki) and speed-impact Electric Whip (30,000 ki / 15,000 trigger); Lightning Cannon ult (50,000 ki)"
weaknesses:
  - "DP4 with no transform — low ceiling"
  - "Average 1,750 recovery, no mobility tool"
  - "Plain neutral outside the bind gimmick"
howToFight: "Bait Spark Bind and punish its recovery — it's his main opener. He has no transform or escape, so apply pressure and convert. Deny ki to keep Lightning Cannon offline."
summary: "DP4 Glorio; 40k HP, Spark Bind (no-auto-guard) + Thunder Charge, Electric Whip speed-impact + Lightning Cannon ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

