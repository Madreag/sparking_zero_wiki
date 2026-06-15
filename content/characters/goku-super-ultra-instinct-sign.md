---
slug: "goku-super-ultra-instinct-sign"
name: "Goku (Super), Ultra Instinct -Sign-"
charId: "0000_50"
baseCharacter: "Goku (Z - Early)"
era: "Super"
dp: 8
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 15
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "120,000 Zeni (shop)"
transformsTo:
  - target: "Goku (Super), Ultra Instinct"
    targetSlug: "goku-super-ultra-instinct"
    cost: 2
    kind: "transform"
moveset:
  - name: "You'll Never Beat Me"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Even Greater Potential"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Kamehameha -Sign-"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Flash -Sign-"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Point-Blank Kamehameha"
    type: "ultimate"
    kiCost: 50000
    damage: 8000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "A"
playable: true
playstyle: "All-rounder rushdown"
strengths:
  - "Transforms into Ultra Instinct -Sign- (s1 'You'll Never Beat Me', heals 10,000 HP on the change) — strong mid-match power spike"
  - "A-tier; balanced rushdown with Kamehameha -Sign- (30,000 ki) and Flash -Sign- speed-impact rush (15,000 on trigger)"
  - "Even Greater Potential (3 stock) attack buff sets up the transform window"
  - "40,000 HP baseline bulk"
weaknesses:
  - "DP8 — premium cost for a non-fusion all-rounder"
  - "Unlocked behind 120,000 Zeni (shop)"
  - "Base form lacks the auto-dodge; must survive to transform to access the UI engine"
howToFight: "Punish the transform animation — the 2-stock change has a 5s window where he's committed. Keep him in base form by applying constant pressure so he can't safely spend stock. Once he is UI -Sign-, switch to Rush Chain reads rather than raw strings."
summary: "DP8 Goku (Super) -Sign-, A-tier; 40,000 HP; transforms to UI Goku (-Sign- → DP9) consuming 2 stock + 10,000 HP heal; Even Greater Potential (3 stock) buff."
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

