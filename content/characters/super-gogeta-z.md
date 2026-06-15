---
slug: "super-gogeta-z"
name: "Super Gogeta (Z) "
charId: "0110_04"
baseCharacter: "Gogeta (Super)"
era: "Movie"
dp: 8
source: "Base"
classes:
  - "Fusion"
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 20
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "I'm the One Who Will Defeat You!"
    type: "blast1"
    notes: "slot S2"
  - name: "Immovable Stance"
    type: "blast1"
    notes: "slot S1"
  - name: "Big Bang Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Punisher Drive"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Stardust Breaker"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Fusion rushdown"
strengths:
  - "Big Bang Kamehameha (30,000-ki super)"
  - "Punisher Drive (40,000-ki super, 20,000-ki on combo trigger, speed-impact rush)"
  - "Stardust Breaker 50,000-ki ultimate finisher"
  - "Immovable Stance super-armor"
weaknesses:
  - "DP8 — premium cost, poor points-per-DP value"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "He has no auto-dodge, so trade into his approaches with Super Counter (free) and vanish reads. Perception (2 stock) or vanish the Punisher Drive rush rather than mashing into it."
summary: "DP8 Movie-era fusion; Punisher Drive 40,000-ki speed-impact super, Stardust Breaker 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

