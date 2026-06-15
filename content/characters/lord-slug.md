---
slug: "lord-slug"
name: "Lord Slug"
charId: "0590_00"
baseCharacter: "Lord Slug"
era: "Movie"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Lord Slug, Giant Form"
    targetSlug: "lord-slug-giant-form"
    cost: 3
    kind: "transform"
moveset:
  - name: "High-Tension"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Finger Beam"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Beam"
      - "weak-vs-shield"
  - name: "Darkness Eye Beam"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Mow down and explode"
  - name: "Power of Darkness"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Giant-access base"
strengths:
  - "Transforms to Giant Form for 3 stocks banking a big +10,000 HP heal"
  - "High-Tension S2 is a free charge/buff"
  - "Finger Beam (20,000 ki) is a cheap ranged poke; Darkness Eye Beam (30,000 ki) the heavier option"
  - "Power of Darkness ult at 50,000 ki"
weaknesses:
  - "DP4 base is frail; the Giant payoff is itself C-tier and giant-nerfed"
  - "Average 1,750 recovery, no escape tool"
  - "Slow, telegraphed approach"
howToFight: "Deny the 3-stock Giant transform by keeping him stock-starved — the giant form is his only real threat and it's been broadly nerfed (takes more melee, slower back-dash). Charge Blasts now knock back giants, so if he does transform, zone him. In base, just bully him."
summary: "DP4 Namekian; 40k HP, High-Tension buff, branches to Giant Form (3 stock, +10,000 HP heal); 20k-ki Finger Beam."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

