---
slug: "broly-super"
name: "Broly (Super)"
charId: "0553_00"
baseCharacter: "Broly (Super)"
era: "Movie"
dp: 5
source: "Pre-order Pack"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Broly (Super), Super Saiyan"
    targetSlug: "broly-super-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Broly (Super), Super Saiyan (Full Power)"
    targetSlug: "broly-super-super-saiyan-full-power"
    cost: 3
    kind: "transform"
moveset:
  - name: "Going Berserk"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Full-Power Charge"
    type: "blast1"
    notes: "slot S1"
  - name: "Full-Power Energy Wave"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Gigantic Crash"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Gigantic Impact"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
dpTier: "A"
playable: true
playstyle: "Berserker base form"
strengths:
  - "Going Berserk S2 (4 stock) is the no-auto-guard ramp that sets up his power curve"
  - "Direct 3-stock transform to SS Full Power (the 45k-HP S-tier ceiling) with +5,000 HP heal"
  - "Gigantic Crash super at 40,000 ki (20,000 trigger) is a big speed-impact hit even in base"
  - "Full-Power Charge S1 builds meter for free"
weaknesses:
  - "DP5 base is the weakest point of the line — you race to Full Power"
  - "Transform gated behind stock; vulnerable while charging"
  - "Average 1,750 ki recovery, no mobility tool"
howToFight: "Same plan as Z-Broly: deny the climb to SS Full Power by pressuring through his stock-building. Going Berserk is no-auto-guard, so punish the activation. Bait the lack of a defensive escape and keep your turn; he is far less dangerous before the 3-stock transform lands."
summary: "DP5 Broly (Super) base; 40k HP, Going Berserk (4 stock) ramp, branches to SS or SS Full Power transforms."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

