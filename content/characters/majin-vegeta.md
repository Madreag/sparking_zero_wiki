---
slug: "majin-vegeta"
name: "Majin Vegeta"
charId: "0020_40"
baseCharacter: "Vegeta (Z - Scouter)"
era: "Z"
dp: 7
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 8
kiAutoRecovery: 1500
initialKi: 50000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 999
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
unlock: "105,000 Zeni (shop)"
moveset:
  - name: "Majin's Awakening"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Prince's Pride"
    type: "blast1"
    notes: "slot S1"
  - name: "Final Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Big Bang Attack"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Final Explosion"
    type: "ultimate"
    kiCost: 50000
    damage: 16000
    properties:
      - "Explosive Wave"
      - "In Sparking! Mode"
      - "Unguardable"
      - "Played after a hit"
      - "You also take damage"
tier: "A"
playable: true
playstyle: "Berserker bruiser"
strengths:
  - "Final Explosion 50,000-ki ultimate — huge burst (self-KO finisher) that can swing a match"
  - "B-tier bruiser; two 30,000-ki supers (Final Impact, Big Bang Attack) and Prince's Pride buff"
  - "Majin's Awakening (4 stock) attack spike for the kill window"
  - "40,000 HP baseline"
weaknesses:
  - "DP7 with no auto-dodge — eats pressure if the ki isn't up"
  - "Final Explosion is suicidal: misusing it loses you the body"
  - "Unlocked behind 105,000 Zeni (shop)"
howToFight: "Stay aware of Final Explosion at point-blank on his knockdown/wake — don't crowd him at low HP. Bait Majin's Awakening, then pressure his lack of evasion with Super Counter (free) and vanish reads."
summary: "DP7 Majin Vegeta: B-tier; 40,000 HP, 8.0 ki charge; Final Impact + Big Bang Attack (both 30,000 ki) + Final Explosion 50,000-ki suicide ult; Majin's Awakening (4 stock)."
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

