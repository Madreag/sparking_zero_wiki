---
slug: "yajirobe"
name: "Yajirobe"
charId: "0210_00"
baseCharacter: "Yajirobe"
era: "Z"
dp: 2
source: "Base"
hp: 35000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 1
skillGaugeGains:
  vanishExchangeRate: 1.1
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Senzu Beans"
    type: "blast1"
    skillCost: 6
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Super Unyielding Spirit"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S1"
  - name: "Ka-Blam Attack"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
      - "speed-impact"
  - name: "Flash and Kill"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Miracle Ka-Blam Slash"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "D"
dpTier: "Z"
dpScore: 30.7
playable: true
playstyle: "Senzu staller"
strengths:
  - "Senzu Beans (6 stock) full-heal — the famous stall tool, still a niche DP2 tank"
  - "DP2 — dirt-cheap DP-queue body; pairs with a premium carry"
  - "Ka-Blam Attack 40,000-ki speed-impact super + Miracle Ka-Blam Slash 50,000-ki ult give it a punish"
  - "Super Unyielding Spirit (4 stock) for a defensive buff"
weaknesses:
  - "Senzu starts at 0 stock and costs 6 — you must build a long time before the first heal (Oct-2024 nerf)"
  - "Ki-recovery speed reduced May 2026; standardized Singles HP removes his tank value entirely"
  - "35,000 HP, no offense to speak of — pure utility; D-tier"
howToFight: "Race the stock clock: he can't heal until 6 skill stock, so burst him before the first Senzu lands. In Singles his HP is standardized so the stall does nothing — just out-damage him. Bait Super Unyielding Spirit and keep the pressure relentless."
summary: "DP2 Yajirobe: D-tier; 35,000 HP; Senzu Beans heal (6 stock, start with 0) — once a meta-defining stall, gutted; Ki recovery nerfed May 2026."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

