---
slug: "broly-z-super-saiyan"
name: "Broly (Z), Super Saiyan"
charId: "0551_00"
baseCharacter: "Broly (Z)"
era: "Movie"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Broly (Z), Legendary Super Saiyan"
    targetSlug: "broly-z-legendary-super-saiyan"
    cost: 2
    kind: "transform"
moveset:
  - name: "Kakarottt!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S1"
  - name: "Bloody Smash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Trap Shooter"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Simultaneous Fire"
      - "weak-vs-shield"
  - name: "Eraser Cannon"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Mid-form berserker"
strengths:
  - "Cheaper 2-stock transform to Legendary SS (vs 3 from base) with +5,000 HP heal"
  - "Saiyan Spirit S1 is a free charge/power tool (no stock)"
  - "Bloody Smash super at 30,000 ki (15,000 trigger) is a speed-impact catch"
  - "Kakarottt! (4 stock) no-auto-guard buff sustains the ramp"
weaknesses:
  - "DP7 with still-40,000 HP — pricier than base but no tankier"
  - "An intermediate form; weaker than the LSSJ payoff you're aiming for"
  - "1,750 ki recovery is only average for the cost"
howToFight: "This is the in-between form — he is one 2-stock transform from S-tier LSSJ, so interrupt charging and keep him under 2 stocks. Trap Shooter (20,000 ki) is his ranged poke; vanish or guard it. Don't let him stockpile; whoever controls the meter controls the transform."
summary: "DP7 Broly (Z) SS; 40k HP, Saiyan Spirit charge + Bloody Smash speed-impact super; 2-stock bridge to LSSJ."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

