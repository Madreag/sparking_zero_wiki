---
slug: "pan-gt"
name: "Pan (GT)"
charId: "0230_00"
baseCharacter: "Pan (GT)"
era: "GT"
dp: 3
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 4
initialSkillStock: 2
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
  - name: "Saiyan Spirit"
    type: "blast1"
    notes: "slot S2"
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Giru Missile"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Maiden's Rage"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Giru Missile (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Maiden's Rage 50,000-ki ultimate finisher"
  - "Afterimage Strike auto-dodge (3 stock; ends on a Super Counter post-May-2026)"
  - "Saiyan Spirit ki/attack buff"
weaknesses:
  - "35,000 HP — below the 40k baseline, dies a combo earlier"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish; don't feed raw strings into it. Perception (2 stock) or vanish the Giru Missile rush rather than mashing into it."
summary: "DP3 GT-era fighter; 35,000 HP; Kamehameha 30,000-ki super, Maiden's Rage 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

