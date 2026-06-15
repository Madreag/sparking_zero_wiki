---
slug: "cell-max"
name: "Cell Max"
charId: "3040_00"
baseCharacter: "Cell Max"
era: "Movie"
dp: 9
source: "\"Heroes of Justice\" Pack"
classes:
  - "Giant"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 40000
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Howl"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Max Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Mighty Fist"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
  - name: "Max Bomb"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
tier: "B"
playable: true
playstyle: "Boss giant anchor"
strengths:
  - "Giant-class boss: massive hitbox, super-armor, grab-immune, huge HP"
  - "Max Bomb ult (50,000 ki) was made UNBLOCKABLE in Jan-2026 — a guaranteed-damage threat if it lands"
  - "Max Cannon (30,000 ki) and Mighty Fist (40,000 ki); Howl S2 (4 stock) no-auto-guard buff"
  - "Explosive Wave S1 (free) AoE reversal"
weaknesses:
  - "B-tier after broad May-2026 giant nerfs: less damage, longer recovery, takes more melee, slower back-dash"
  - "Slow 1,500 ki recovery / 8.0 charge"
  - "Charge Blasts now damage and knock him back"
howToFight: "His Max Bomb ult is unblockable, but it's still Vanish-evadable and auto-evasion-evadable (May-2026) — so dodge it, don't guard. Otherwise pure anti-giant: charge Blasts knock him back, stay mobile, punish his long whiff recovery, never grab. Deny the 50,000 ki so Max Bomb stays offline as long as possible."
summary: "DP9 Cell Max Giant boss; null-HP giant, Howl (4 stock) + Mighty Fist 40k-ki, unblockable Max Bomb ult (Jan 2026); B-tier after giant nerfs."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

