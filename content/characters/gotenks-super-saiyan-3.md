---
slug: "gotenks-super-saiyan-3"
name: "Gotenks, Super Saiyan 3"
charId: "0120_02"
baseCharacter: "Gotenks"
era: "Z"
dp: 8
source: "Base"
classes:
  - "Fusion"
hp: 45000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 15
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
  - name: "Vice Shout"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Victory Bazooka"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "DIE DIE Missile Barrage"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Charging Ultra Buu Buu Volleyball"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "45,000 HP — above-baseline bulk"
  - "Victory Bazooka (30,000-ki super)"
  - "DIE DIE Missile Barrage (30,000-ki super)"
  - "Charging Ultra Buu Buu Volleyball 50,000-ki ultimate finisher"
  - "Vice Shout — unblockable shockwave"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Charging Ultra Buu Buu Volleyball on knockdown — bait it out and punish the recovery."
summary: "DP8 Z-era fusion; 45,000 HP; Victory Bazooka 30,000-ki super, Charging Ultra Buu Buu Volleyball 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

