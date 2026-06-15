---
slug: "broly-z"
name: "Broly (Z)"
charId: "0550_00"
baseCharacter: "Broly (Z)"
era: "Movie"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Broly (Z), Super Saiyan"
    targetSlug: "broly-z-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Broly (Z), Legendary Super Saiyan"
    targetSlug: "broly-z-legendary-super-saiyan"
    cost: 3
    kind: "transform"
moveset:
  - name: "Kakarottt!"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "High Speed Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Super Explosive Wave"
    type: "ultimate"
    kiCost: 50000
playable: true
playstyle: "Berserker base form"
strengths:
  - "Wild Sense S1 gives a free 1-hit auto-dodge counter (no stock cost)"
  - "Transforms straight to Legendary SS for 3 stocks, banking a +5,000 HP heal and a permanent attack buff in Singles"
  - "Kakarottt! (4 stock) is a no-auto-guard power-up that fuels the berserker ramp"
  - "High Speed Rush super at 30,000 ki (15,000 trigger) is a cheap speed-impact finisher"
weaknesses:
  - "DP5 base is fragile relative to its payoff form — you want to evolve fast"
  - "Slow 1,500 ki recovery in base; transform is gated behind 3 stocks"
  - "Wild Sense was gutted Dec 2025 — no longer a mid-combo escape, just a 1-hit read"
howToFight: "Pressure him before he banks 3 stocks for Legendary SS — deny the transform window. Wild Sense is a 1-hit counter only now, so stagger your strings and bait it with a single hit, then punish. If he transforms, respect the new attack buff and play for vanish (≈half a ki bar) spacing rather than trading."
summary: "DP5 Movie-Broly base; 40k HP, Wild Sense + Kakarottt! (4 stock) launcher, gateway to LSSJ via 3-stock transform."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

