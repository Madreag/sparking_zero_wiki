---
slug: "recoome"
name: "Recoome"
charId: "0390_00"
baseCharacter: "Recoome"
era: "Z"
dp: 3
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 8
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "SP Fighting Pose 1"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Recoome Eraser Gun"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Beam"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Recoome Grenade Bomber"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Recoome Fighting Bomber"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "B"
dpTier: "Z"
dpScore: 30.3
playable: true
playstyle: "DP-value tank"
strengths:
  - "DP-value S-tier (30.3 points-per-DP) — a cheap DP3 wall that overperforms its cost"
  - "40,000 HP bruiser with Recoome Eraser Gun + Recoome Grenade Bomber (both 30,000 ki)"
  - "Recoome Fighting Bomber 50,000-ki ultimate; SP Fighting Pose 1 (4 stock) buff"
  - "DP3 — cheap body for value-spam DP teams"
weaknesses:
  - "HP reduced in the May 2026 patch — less tanky than its peak"
  - "C-tier in Singles; no auto-dodge, slow approach"
  - "Below DP7, so it loses auto-reflect in Sparking mode under the new rule"
howToFight: "Out-space him — he has no evasion and only False Courage/Fighting Pose for utility. In DP, kill the round quickly so the cheap value doesn't accrue. Super Counter (free) his rushes; he can't auto-reflect (DP3 < 7)."
summary: "DP3 Recoome: C-tier Singles, DP-value S-tier (sparkingzerometa 30.3 points-per-DP); 40,000 HP; two 30,000-ki supers + Recoome Fighting Bomber 50,000-ki ult; HP reduced May 2026."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

