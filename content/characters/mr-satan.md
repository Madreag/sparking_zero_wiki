---
slug: "mr-satan"
name: "Mr. Satan"
charId: "0180_00"
baseCharacter: "Mr. Satan"
era: "Z"
dp: 1
source: "Base"
hp: 30000
hpInherited: false
kiChargeSpeed: 7
kiAutoRecovery: 1750
initialKi: 50000
maxSkillStock: 4
initialSkillStock: 3
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
  - name: "Royal Raiment?!"
    type: "blast1"
    notes: "slot S2"
  - name: "False Courage"
    type: "blast1"
    notes: "slot S1"
  - name: "Dynamite Kick"
    type: "blast2"
    kiCost: 30000
    damage: 8500
    properties:
      - "Rush"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 15,000 ki"
  - name: "Present Bomb"
    type: "blast2"
    kiCost: 40000
    damage: 6350
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Mr. Buu Arrives!"
    type: "ultimate"
    kiCost: 50000
    damage: 16750
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
tier: "D"
playable: true
playstyle: "Joke / utility"
strengths:
  - "DP1 — the single cheapest body in the game; pure budget filler"
  - "Present Bomb 40,000-ki speed-impact super (20,000 on trigger) is a surprising burst gimmick"
  - "Mr. Buu Arrives! 50,000-ki ultimate; Royal Raiment?! utility"
  - "False Courage for instant ki"
weaknesses:
  - "Lowest Singles score in the game (8.7k); 30,000 HP — melts in two combos"
  - "DP1 but brings no real combat value; Ki-recovery nerfed May 2026"
  - "No transform, no auto-dodge, no heal"
howToFight: "Just attack — 30,000 HP and no evasion means he dies almost immediately. The only thing to respect is a desperation Present Bomb gimmick at point-blank. Otherwise overwhelm him."
summary: "DP1 Mr. Satan — lowest DP in the game; 30,000 HP; weakest Singles score (8.7k); Dynamite Kick + Present Bomb speed-impact supers + Mr. Buu Arrives! 50,000-ki ult; joke pick."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

