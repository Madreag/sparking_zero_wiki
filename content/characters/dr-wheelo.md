---
slug: "dr-wheelo"
name: "Dr. Wheelo"
charId: "0570_00"
baseCharacter: "Dr. Wheelo"
era: "Movie"
dp: 4
source: "Base"
hp: 40000
hpInherited: false
kiChargeSpeed: 0
kiAutoRecovery: 1700
kiAutoRecoveryLimit: 50000
initialKi: 30000
maxSkillStock: 4
initialSkillStock: 1
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
  - name: "Full Power"
    type: "blast1"
    skillCost: 4
    properties:
      - "no-auto-guard"
    notes: "slot S2"
  - name: "Barrier"
    type: "blast1"
    skillCost: 3
    notes: "slot S1"
  - name: "Photon Strike"
    type: "blast2"
    kiCost: 30000
    damage: 1900
    hits: 4
    properties:
      - "Fire"
      - "weak-vs-shield"
    notes: "chip 380"
  - name: "Gigantic Bomber"
    type: "blast2"
    kiCost: 40000
    damage: 6000
    properties:
      - "Rush"
      - "Unguardable"
  - name: "Planet Geyser"
    type: "ultimate"
    kiCost: 50000
    damage: 750
    properties:
      - "Beam"
      - "In Sparking! Mode"
    notes: "chip 250"
tier: "B"
playable: true
playstyle: "Barrier turtle zoner"
strengths:
  - "Barrier S1 (3 stock) grants a damage-absorbing shield for stalling"
  - "Full Power S2 (4 stock) no-auto-guard buff raises damage output"
  - "Gigantic Bomber super at 40,000 ki is a heavy two-hand blast finisher"
  - "Planet Geyser ult at 50,000 ki for chip closeouts"
weaknesses:
  - "DP4, no transform, HP reduced in past giant-meta tuning era"
  - "0.0 listed ki-charge speed — relies on 1,700 auto-recovery, slow offense"
  - "Barrier is the only defensive tool and costs 3 stock; once spent he's exposed"
howToFight: "Force out his Barrier early, then attack while it's on cooldown — he has no second escape. His ki economy is poor (near-zero charge), so out-vanish him in exchanges (≈half a bar each) and he runs dry first. Punish Full Power activations (no-auto-guard)."
summary: "DP4 mad-scientist; 40k HP, Barrier (3 stock) defense + Full Power (4 stock); near-zero ki-charge but Gigantic Bomber 40k-ki."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
  - "research/05-meta-pvp-tiers.md (sparkingzerometa + propelrc, May 26 2026 patch)"
---

