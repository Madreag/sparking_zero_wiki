---
slug: "majin-buu"
name: "Majin Buu"
charId: "0170_00"
baseCharacter: "Majin Buu"
era: "Z"
dp: 6
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
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
  - name: "Sleep"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Paralyze Beam"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Buu Buu Gum"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "Played after a hit"
  - name: "Super Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Angry Explosion"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Buu Buu Gum (30,000-ki super)"
  - "Super Kamehameha (30,000-ki super)"
  - "Angry Explosion 50,000-ki ultimate finisher"
  - "Paralyze Beam — unblockable stun"
weaknesses:
  - "No auto-dodge/evasion skill — active defense is Super Counter only"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Angry Explosion on knockdown — bait it out and punish the recovery."
summary: "DP6 Z-era fighter; 40,000 HP; Buu Buu Gum 30,000-ki super, Angry Explosion 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

