---
slug: "zamasu"
name: "Zamasu"
charId: "0810_00"
baseCharacter: "Zamasu"
era: "Super"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
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
  - target: "Fused Zamasu"
    targetSlug: "fused-zamasu"
    cost: 3
    kind: "fusion"
moveset:
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Immortal Body"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Divine Steel Blast"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "vanish: erase"
  - name: "God Slicer"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Holy Light Grenade"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Immortal stall body"
strengths:
  - "Immortal Body S1 (4 stock) is a no-auto-guard damage-reduction stall tool"
  - "Afterimage Strike S2 (3 stock) gives a launch-era auto-dodge window"
  - "Potara-fuses with Goku Black into the DP8 Fused Zamasu for 3 stocks"
  - "Divine Steel Blast (30,000 ki) and speed-impact God Slicer (30,000 ki / 15,000 trigger); Holy Light Grenade ult (50,000 ki)"
weaknesses:
  - "DP5 base; value is in the fusion and stall, not raw offense"
  - "Average 1,750 recovery, no teleport"
  - "Afterimage Strike ends on a Super Counter (post-May-2026)"
howToFight: "If he pops Afterimage Strike, land a ~2f Super Counter to delete it. Immortal Body just reduces damage — keep hitting through it and bait the fusion attempt (3-stock Potara). Deny stocks so he can't both stall and fuse."
summary: "DP5 Zamasu; 40k HP, Immortal Body (4 stock) damage-reduction + Afterimage Strike (3 stock); Potara into Fused Zamasu."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

