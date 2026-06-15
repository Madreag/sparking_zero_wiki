---
slug: "vegeta-mini"
name: "Vegeta (Mini)"
charId: "3060_00"
baseCharacter: "Vegeta (Mini)"
era: "DAIMA"
dp: 4
source: "Dragon Ball DAIMA Character Pack 1"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Vegeta (Mini), Super Saiyan"
    targetSlug: "vegeta-mini-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Vegeta (Mini), Super Saiyan 2"
    targetSlug: "vegeta-mini-super-saiyan-2"
    cost: 2
    kind: "transform"
  - target: "Vegeta (Mini), Super Saiyan 3"
    targetSlug: "vegeta-mini-super-saiyan-3"
    cost: 3
    kind: "transform"
moveset:
  - name: "Afterimage"
    type: "blast1"
    notes: "slot S2"
  - name: "Revive Bug"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Full-Power Energy Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Rising Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Atomic Rush"
    type: "ultimate"
    kiCost: 50000
tier: "B"
playable: true
playstyle: "Revival transform base"
strengths:
  - "Revive Bug S1 (4 stock) is a no-auto-guard self-revival/comeback tool — unusual on a DP4"
  - "Flexible 1/2/3-stock transforms up the Mini-Vegeta ladder (SS/SS2/SS3)"
  - "Afterimage S2 (free) 1-hit auto-dodge; Rising Rush speed-impact super (30,000 ki / 15,000 trigger)"
  - "Full-Power Energy Cannon (30,000 ki); Atomic Rush ult (50,000 ki)"
weaknesses:
  - "C-tier DP4 base — weak until laddered"
  - "Average 1,750 recovery, no teleport"
  - "Revive Bug is punishable on activation"
howToFight: "Account for Revive Bug when you think you've closed the round — burst through the revival. Deny the cheap transforms up the ladder. Afterimage is one-hit; stagger to bait it. Punish Revive Bug activations and keep him stock-starved."
summary: "DP4 Vegeta (Mini) base; 40k HP, Revive Bug (4 stock) self-revival + Afterimage, Rising Rush speed-impact; 1-3 stock transforms; C-tier."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

