---
slug: "videl"
name: "Videl"
charId: "0130_00"
baseCharacter: "Videl"
era: "Z"
dp: 2
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
initialKi: 40000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 3
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "30,000 Zeni (shop)"
moveset:
  - name: "Super Unyielding Spirit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Videl Kick"
    type: "blast2"
    kiCost: 20000
    damage: 5700
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
  - name: "Desperado Rush"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Videl Rush"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "D"
dpTier: "S"
dpScore: 20.1
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Videl Kick (20,000-ki super, speed-impact rush)"
  - "Desperado Rush (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Videl Rush 50,000-ki ultimate finisher"
  - "Afterimage Strike auto-dodge (3 stock; ends on a Super Counter post-May-2026)"
  - "DP2 — dirt-cheap DP-queue body; frees budget for a premium carry"
weaknesses:
  - "30,000 HP — melts in roughly two combos"
  - "Slow 6 ki charge — sluggish to fund supers"
  - "Bottom-tier kit — limited damage ceiling and few defensive tools"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish; don't feed raw strings into it. Pressure his slow 6 ki charge by forcing blocks so he can't reach his supers. Perception (2 stock) or vanish the Videl Kick rush rather than mashing into it."
summary: "DP2 Z-era fighter, D-tier; 30,000 HP; Desperado Rush 30,000-ki speed-impact super, Videl Rush 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

