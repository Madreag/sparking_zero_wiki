---
slug: "full-power-bojack"
name: "Full-Power Bojack"
charId: "0631_00"
baseCharacter: "Full-Power Bojack"
era: "Movie"
dp: 7
source: "Base"
hp: 45000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 7
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
  - name: "Psycho Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Grand Smasher"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Galactic Tyrant"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Galactic Buster"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
dpTier: "S"
playable: true
playstyle: "Armor-buff brawler"
strengths:
  - "Upgraded 45,000 HP makes him a respectable anchor"
  - "Psycho Barrier S1 (3 stock) for on-demand absorption"
  - "Pump Up S2 (free) stacks self-buff toward armor trades"
  - "Galactic Tyrant super at 30,000 ki (15,000 trigger, speed-impact); Galactic Buster ult (50,000 ki)"
weaknesses:
  - "DP7 ceiling form — no further scaling"
  - "Plain 1,750 ki recovery for the cost"
  - "Barrier is his sole escape; no teleport"
howToFight: "Avoid trading into his 45,000 HP — use ~2f Super Counters to break strings. Bait out Psycho Barrier, then attack on cooldown. Starve ki to keep Galactic Buster offline; he has no teleport to reset neutral."
summary: "DP7 Full-Power Bojack; 45k HP, Psycho Barrier (3 stock) + Pump Up, Galactic Tyrant speed-impact super + Galactic Buster ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

