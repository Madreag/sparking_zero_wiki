---
slug: "future-trunks"
name: "Future Trunks"
charId: "0080_30"
baseCharacter: "Trunks (Sword)"
era: "Z"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 7
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
transformsTo:
  - target: "Future Trunks, Super Saiyan"
    targetSlug: "future-trunks-super-saiyan"
    cost: 1
    kind: "transform"
moveset:
  - name: "Wild Sense"
    type: "blast1"
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Masenko"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Lightning Sword Slash"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "Unguardable"
      - "Played after a hit"
  - name: "Shining Slash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
playable: true
playstyle: "Beam zoner"
strengths:
  - "Masenko (30,000-ki super)"
  - "Lightning Sword Slash (30,000-ki super)"
  - "Shining Slash 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Wild Sense counter-dodge (gutted Dec 2025 — situational now)"
weaknesses:
  - "Leans on Wild Sense, which was gutted Dec 2025 — situational defense"
  - "No heal/regen — fixed effective durability once committed"
howToFight: "Bait his Wild Sense (gutted Dec 2025) then punish the recovery — it's his main evasion. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Respect Shining Slash on knockdown — bait it out and punish the recovery."
summary: "DP5 Z-era fighter; 40,000 HP; Masenko 30,000-ki super, Shining Slash 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
---

