---
slug: "piccolo-fused-with-kami"
name: "Piccolo (Fused with Kami)"
charId: "0040_10"
baseCharacter: "Piccolo"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 30000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "False Courage"
    type: "blast1"
    notes: "slot S2"
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S1"
  - name: "Special Beam Cannon"
    type: "blast2"
    kiCost: 30000
    properties:
      - "weak-vs-shield"
  - name: "Light Grenade"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Hellzone Grenade"
    type: "ultimate"
    kiCost: 50000
    damage: 500
    properties:
      - "Simultaneous Fire"
      - "In Sparking! Mode"
      - "Played after a hit"
    notes: "chip 100"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Special Beam Cannon (30,000-ki super)"
  - "Light Grenade (30,000-ki super)"
  - "Hellzone Grenade 50,000-ki ultimate finisher"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
  - "False Courage instant ki gain"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No transform path — fixed kit with no mid-match power spike"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Respect Hellzone Grenade on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Special Beam Cannon 30,000-ki super, Hellzone Grenade 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

