---
slug: "spopovich"
name: "Spopovich"
charId: "0760_00"
baseCharacter: "Spopovich"
era: "Z"
dp: 2
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 1
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Berserker"
    type: "blast1"
    notes: "slot S2"
  - name: "A Servant's Latent Power"
    type: "blast1"
    skillCost: 1
    notes: "slot S1"
  - name: "Berserker Crash"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
      - "speed-impact"
  - name: "Mad Banquet"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Majin Buu Resurrection"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
dpTier: "Z"
dpScore: 28.2
playable: true
playstyle: "Cheap berserker body"
strengths:
  - "Outrageous DP efficiency for a 2-DP slot (28.2 value) — overperforms its cost in DP Battle"
  - "Berserker S2 (free) is a damage-amp activation"
  - "Both supers speed-impact: Berserker Crash (40,000 ki) and Mad Banquet (30,000 ki / 15,000 trigger)"
  - "Majin Buu Resurrection ult (50,000 ki) is a surprise 50k-ki payload from a DP2 body"
weaknesses:
  - "HP reduced in the May-2026 patch — now just 35,000"
  - "Worthless in Singles (standardized HP erases his tank value)"
  - "Slow, no mobility, no escape tool — pure DP filler"
howToFight: "In Singles he has no tank edge and only 35,000 HP — open him up and delete the slot. In DP he's a cheap value body, so focus him first to remove disproportionate points. Don't respect Berserker; just block the speed-impact supers and punish."
summary: "DP2 Majin servant; only 35k HP but DP-value S-tier (28.2), Berserker S2 + double speed-impact supers; HP cut May 2026."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

