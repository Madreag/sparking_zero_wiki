---
slug: "tien"
name: "Tien"
charId: "0070_00"
baseCharacter: "Tien"
era: "Z"
dp: 4
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
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Dodon Ray"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Tri-Beam"
    type: "blast2"
    kiCost: 30000
    damage: 5700
    hits: 2
    properties:
      - "Fire"
      - "weak-vs-shield"
      - "vanish: erase"
    notes: "chip 1,140"
  - name: "Neo Tri-Beam"
    type: "ultimate"
    kiCost: 50000
    damage: 3000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "You also take damage"
      - "Repeated usage possible"
    notes: "chip 800"
tier: "B"
playable: true
playstyle: "Glass-cannon zoner"
strengths:
  - "Solar Flare — unblockable screen-blind opener that persists through dashes (Jan 2026 buff)"
  - "C-tier; cheap Dodon Ray (20,000 ki) chip + Neo Tri-Beam 50,000-ki ultimate (multi-hit)"
  - "Wild Sense evasion; DP4 efficient filler"
  - "40,000 HP baseline"
weaknesses:
  - "DP4 with no heal; Wild Sense gutted Dec 2025"
  - "Neo Tri-Beam is high-commitment for the payoff"
  - "Outclassed in raw stats by transforming Saiyans"
howToFight: "Expect Solar Flare on his approach — don't get blinded into a combo. Super Counter (free) his rushes and punish the long Neo Tri-Beam recovery. He has no real defense beyond Wild Sense."
summary: "DP4 Tien: C-tier; 40,000 HP; Dodon Ray (20,000 ki) + Tri-Beam (30,000 ki) + Neo Tri-Beam 50,000-ki ult; Solar Flare unblockable + Wild Sense."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

