---
slug: "android-16"
name: "Android 16"
charId: "0440_00"
baseCharacter: "Android 16"
era: "Z"
dp: 5
source: "Base"
classes:
  - "Android"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 1700
kiAutoRecoveryLimit: 50000
initialKi: 30000
maxSkillStock: 4
initialSkillStock: 1
sparkingDrainPerSec: 2800
kiBlastShots: 4
skillGaugeGains:
  attackBreak: 0.15
  fastAvoid: 0.05
  throwBreak: 0.1
  hitFromBehind: 0.03
  lastHPGauge: 1
  impactStart: 1
moveset:
  - name: "Pump Up"
    type: "blast1"
    notes: "slot S2"
  - name: "Explosive Wave"
    type: "blast1"
    notes: "slot S1"
  - name: "Hell's Impact"
    type: "blast2"
    kiCost: 30000
    properties:
      - "Fire"
  - name: "Hell Flash"
    type: "blast2"
    kiCost: 40000
    properties:
      - "Rush"
      - "Unguardable"
      - "Played after a hit"
      - "speed-impact"
    notes: "Trigger cost 20,000 ki"
  - name: "Self Destruct Device"
    type: "ultimate"
    kiCost: 50000
    properties:
      - "Rush"
      - "In Sparking! Mode"
      - "Played after a hit"
      - "Unguardable"
      - "You also take damage"
tier: "A"
dpTier: "S"
dpScore: 21.5
playable: true
playstyle: "Self-destruct tank"
strengths:
  - "Self Destruct Device 50,000-ki ultimate — massive guaranteed burst, the signature A16 finisher"
  - "B-tier; Hell Flash 40,000-ki speed-impact super (20,000 on trigger) + Hell's Impact (30,000 ki)"
  - "40,000 HP tank; Explosive Wave + Pump Up defense buff"
  - "DP5 — decent DP-queue value (sparkingzerometa 21.5)"
weaknesses:
  - "Android: cannot manually charge ki (charge 0) — only 1,700/s passive recovery, slow to fund supers"
  - "No auto-dodge; large, deliberate body"
  - "Self Destruct is high-commitment and telegraphed"
howToFight: "Watch for Self Destruct Device at point-blank — keep spacing when he has ki. Exploit that he can't charge ki: rush him before passive recovery funds Hell Flash. Super Counter (free) his approaches."
summary: "DP5 Android 16: B-tier; 40,000 HP; CANNOT charge ki (0 charge, 1,700/s recovery); Hell Flash 40,000-ki speed-impact + Self Destruct Device 50,000-ki ult."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

