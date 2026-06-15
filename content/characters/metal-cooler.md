---
slug: "metal-cooler"
name: "Metal Cooler"
charId: "0600_10"
baseCharacter: "Cooler"
era: "Movie"
dp: 7
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 6
kiAutoRecovery: 2000
kiAutoRecoveryLimit: 50000
initialKi: 30000
maxSkillStock: 4
sparkingDrainPerSec: 2800
kiBlastShots: 6
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Regeneration"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Instant Transmission"
    type: "blast1"
    notes: "slot S1"
  - name: "Lock-On Buster"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Fire"
      - "Unguardable"
  - name: "Finger Blitz Barrage"
    type: "blast2"
    kiCost: 20000
    properties:
      - "Continuous Fire"
      - "weak-vs-shield"
  - name: "Supernova"
    type: "ultimate"
    kiCost: 50000
tier: "S"
dpTier: "A"
singlesScore: 116.4
playable: true
playstyle: "Regen/teleport android"
strengths:
  - "Regeneration S2 (4 stock) restores HP — a rare sustain tool on a DP7 body"
  - "Instant Transmission S1 (free) gives true teleport mobility and escape"
  - "Top-bracket 2,000 ki auto-recovery (android trait) keeps supers funded"
  - "Lock-On Buster super at 40,000 ki is a homing heavy hit; Supernova ult at 50,000 ki"
  - "A-tier Singles (116.4) on the strength of the revival/regen kit"
weaknesses:
  - "Still only 40,000 HP — not a tank, leans on regen to survive"
  - "Regeneration costs 4 stock and is no-auto-guard — punishable on use"
  - "No raw armor; loses straight trades to berserkers"
howToFight: "Punish Regeneration: it's a 4-stock no-auto-guard animation — catch it and you negate the heal plus the investment. He'll Instant Transmission out of pressure, so bait the teleport with a delayed string then re-engage. Burn his ki to keep Lock-On Buster and Supernova offline; a 40,000-HP body without sustain dies fast."
summary: "DP7 Metal Cooler; 40k HP but best-in-range 2,000 ki recovery, Regeneration (4 stock) heal + Instant Transmission; A-tier (116.4)."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

