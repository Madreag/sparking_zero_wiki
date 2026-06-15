---
slug: "goku-gt-super-saiyan-4"
name: "Goku (GT), Super Saiyan 4"
charId: "0000_33"
baseCharacter: "Goku (Z - Early)"
era: "GT"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
sparkingDrainPerSec: 2800
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Goku (GT)"
    targetSlug: "goku-gt"
    cost: 0
    kind: "transform"
  - target: "Gogeta (GT), Super Saiyan 4"
    targetSlug: "gogeta-gt-super-saiyan-4"
    cost: 4
    kind: "fusion"
moveset:
  - name: "All I Need Is Five Seconds!"
    type: "blast1"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "x10 Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Meteor Crash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Dragon Fist"
    type: "ultimate"
    kiCost: 50000
tier: "S"
singlesScore: 117.8
playable: true
playstyle: "Mobile rushdown"
strengths:
  - "A-tier GT rushdown — strong neutral and Dragon Fist 50,000-ki ultimate (homing pierce)"
  - "Meteor Crash speed-impact super (15,000 ki on combo trigger) extends pressure cheaply"
  - "Instant Transmission teleport for mix-ups and gap-closing"
  - "8.0 ki charge + 1,500/s recovery keeps supers online"
weaknesses:
  - "DP8 — expensive; in the DP queue the cheaper SS3/SS2 stages give better value"
  - "Reached only at the top of the GT transform ladder (3 stock from base GT) — slow to access"
  - "40,000-equivalent durability; no heal once committed"
howToFight: "Catch him mid-transform-ladder before he reaches SS4 — the climb costs stock and time. Respect Dragon Fist on knockdown; vanish or Perception (2 stock) the Meteor Crash rush. He has no defensive auto-dodge, so trade into his approaches with Super Counter (free)."
summary: "DP8 Goku (GT) SS4: A-tier; 40,000 HP, 8.0 ki charge; x10 Kamehameha (30,000 ki) + Dragon Fist 50,000-ki ult; 'All I Need Is Five Seconds!' burst buff."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

