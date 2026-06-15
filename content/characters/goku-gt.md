---
slug: "goku-gt"
name: "Goku (GT)"
charId: "0002_30"
baseCharacter: "Goku (GT)"
era: "GT"
dp: 5
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "75,000 Zeni (shop)"
transformsTo:
  - target: "Goku (GT), Super Saiyan"
    targetSlug: "goku-gt-super-saiyan"
    cost: 1
    kind: "transform"
  - target: "Goku (GT), Super Saiyan 3"
    targetSlug: "goku-gt-super-saiyan-3"
    cost: 2
    kind: "transform"
  - target: "Goku (GT), Super Saiyan 4"
    targetSlug: "goku-gt-super-saiyan-4"
    cost: 3
    kind: "transform"
moveset:
  - name: "Afterimage Strike"
    type: "blast1"
    skillCost: 3
    notes: "slot S2"
  - name: "Solar Flare"
    type: "blast1"
    properties:
      - "unblockable"
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Dragon Fist"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Spirit Bomb"
    type: "ultimate"
    kiCost: 50000
    damage: 13000
playable: true
playstyle: "Evasive rushdown"
strengths:
  - "Kamehameha (30,000-ki super)"
  - "Dragon Fist (30,000-ki super, 15,000-ki on combo trigger, speed-impact rush)"
  - "Spirit Bomb 50,000-ki ultimate finisher"
  - "Solar Flare — unblockable screen-blind opener"
  - "Afterimage Strike auto-dodge (3 stock; ends on a Super Counter post-May-2026)"
weaknesses:
  - "No heal/regen — fixed effective durability once committed"
  - "Outclassed by transforming/fusion picks at equivalent DP — no standout edge"
howToFight: "Land a Super Counter (free) to instantly pop his Afterimage Strike, then punish; don't feed raw strings into it. Watch for his unblockable opener (Solar Flare/Psychokinesis/Paralyze type) — don't sit blocking predictably. Perception (2 stock) or vanish the Dragon Fist rush rather than mashing into it."
summary: "DP5 GT-era fighter; 40,000 HP; Kamehameha 30,000-ki super, Spirit Bomb 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/06-pve-dlc-unlocks.md (shop Zeni costs)"
---

