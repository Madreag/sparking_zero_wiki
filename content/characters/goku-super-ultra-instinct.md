---
slug: "goku-super-ultra-instinct"
name: "Goku (Super), Ultra Instinct"
charId: "0000_51"
baseCharacter: "Goku (Z - Early)"
era: "Super"
dp: 9
source: "Base"
hp: 40000
hpInherited: true
kiChargeSpeed: 6
kiAutoRecovery: 2000
initialKi: 10000
maxSkillStock: 6
sparkingDrainPerSec: 2800
kiBlastShots: 18
skillGaugeGains:
  vanishExchangeRate: 1.2
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "No Backing Down"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Ultra Movement"
    type: "blast1"
    notes: "slot S1"
  - name: "Ultra Kamehameha"
    type: "blast2"
    kiCost: 30000
    properties:
      - "blast-impact 5"
      - "weak-vs-shield"
      - "vanish: repel"
  - name: "Ultra Barrage"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Supreme Kamehameha"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "S"
playable: true
playstyle: "Auto-dodge counter god"
strengths:
  - "Ultra Movement passive auto-dodge — evades melee/blast without spending stock (best defensive engine in the game)"
  - "S-tier Singles, sparkingzerometa 134.4k — top-8 standardized-HP pick"
  - "Supreme Kamehameha 50,000-ki ultimate plus Ultra Barrage (40,000-ki speed-impact rush, 20,000 on trigger)"
  - "Slow 6.0 ki charge offset by 2,000/s recovery and constant evasion pressure"
weaknesses:
  - "Nerfed May 2026: Rush Chain now connects through the auto-dodge; Smash Ki Blast cooldown increased"
  - "DP9 — expensive, weak points-per-DP in the 15-DP queue"
  - "No transform/heal; once the dodge is solved he has only 40k-equivalent durability"
howToFight: "Do not throw raw strings into the auto-dodge — bait it, then use Rush Chain (post-May-2026 it beats the dodge) or grab. Pressure his slow 6.0 ki charge by forcing blocks so he can't reach Ultra Kamehameha. Spend Perception (2 stock) on his Ultra Barrage rush rather than mashing into the evade."
summary: "DP9 Ultra Instinct: S-tier Singles (sparkingzerometa 134.4k) on passive auto-dodge; Ultra Kamehameha 30,000-ki + Supreme Kamehameha 50,000-ki ult; nerfed May 2026 but still elite."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

