---
slug: "beerus"
name: "Beerus"
charId: "0780_00"
baseCharacter: "Beerus"
era: "Super"
dp: 10
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 17
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Verdict of Destruction"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Sphere of Destruction"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Hakai Headshot"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Sphere of Destruction"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
tier: "A"
playable: true
playstyle: "Mobility/zoning deity"
strengths:
  - "Premium 45,000 HP plus 2,000 ki auto-recovery — durable and resource-rich deity"
  - "Best-in-class god mobility makes him a perennial tournament pick (cited among top comp characters)"
  - "Verdict of Destruction S2 (4 stock) is a heavy no-auto-guard Hakai threat; Sleep S1 (4 stock) steals turns"
  - "Sphere of Destruction (30,000 ki) and speed-impact Hakai Headshot (30,000 ki / 15,000 trigger); Super Sphere ult (50,000 ki)"
weaknesses:
  - "DP10 — most expensive bracket, terrible DP efficiency (12.0k), eats the whole budget"
  - "Auto-reflect access only because he's DP7+; but no super-armor on normals"
  - "Both signature skills cost 4 stock — punishable on whiff"
howToFight: "Don't get read by Verdict of Destruction or Sleep — both are 4-stock no-auto-guard reads; bait and punish the recovery. His strength is mobility/spacing, so close the gap and force melee where his 45,000 HP can still be ground down with Super Counters (~2f). Win the ki war (vanish ≈half a bar each) to keep his ult and Hakai offline."
summary: "DP10 God of Destruction; 45k HP, 2,000 ki recovery, Sleep + Verdict of Destruction (4 stock each), Hakai Headshot; A-tier (120.9k), tournament staple."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

