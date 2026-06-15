---
slug: "dp-system"
name: "DP Battle (Destruction Points System)"
category: "pvp"
players: "1–2 (offline & online)"
access: "Versus → DP Battle · Ranked → DP Battle queue · Player Match · World Tournament · Training"
rewards: []
values:
  - label: "DP scale (per character)"
    value: "1–10"
    tag: "community"
  - label: "Offline / Versus — team size"
    value: "up to 5 characters"
    patch: "overview source"
    tag: "community"
  - label: "Offline / Versus — DP budget"
    value: "15 (default); selectable 10 / 15 / 20 (persists since May 26 2026)"
    patch: "May 26 2026"
    tag: "official"
  - label: "Ranked DP queue — team size"
    value: "3 characters (ranked standard)"
    patch: "meta research"
    tag: "community"
  - label: "Ranked DP queue — DP budget"
    value: "15 (ranked standard)"
    patch: "meta research"
    tag: "community"
  - label: "DP1 characters (whole game)"
    value: "1 (Mr. Satan)"
    tag: "community"
  - label: "DP10 base characters"
    value: "5 (Beerus, Whis, Vegito SSGSS, Gogeta (Super) SSGSS, Gogeta (GT) SS4)"
    tag: "community"
  - label: "Auto-reflect eligibility"
    value: "DP7+ only during Sparking! Mode (since May 26 2026)"
    patch: "May 26 2026"
    tag: "official"
  - label: "DP scaling"
    value: "Widened — DP gap reflects strength more strongly (since May 26 2026)"
    patch: "May 26 2026"
    tag: "official"
summary: "The Destruction Points team-building system. Each character has a fixed DP cost (1–10); you build a team under a DP budget. SOURCES CONFLICT on the standard team format: the overview research says VERSUS is up to 5 characters under 15 DP, while the meta/ranked research says the RANKED DP queue is a 3-character team under 15 DP, with offline totals selectable 10/15/20 (persistent since May 26 2026). Both numbers are presented below, tagged by source. May 26 2026 also restricted auto-reflect to DP7+ and widened DP scaling."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/01-overview-modes-economy.md (§2 DP examples — 15 DP / 5 characters Versus & ranked; Goku Z-Mid 5 DP, UI Goku 9 DP)"
  - "research/05-meta-pvp-tiers.md (§4/§5 — ranked DP queue standard 15 DP / 3-character team; offline 10/15/20 selectable, persists; auto-reflect DP7+; DP scaling widened)"
  - "research/02-roster-dp-dlc.md (§0/§1 — DP scale 1–10; DP1 = Mr. Satan only; DP10 base = 5 fusions/deities; team up to 5 under cap)"
  - "research/06-pve-dlc-unlocks.md (§6 — DP total 10/15/20 settable offline/player match/tournament/training, persists since May 26 2026)"
---
**DP Battle** is the team format built on **Destruction Points (DP)**. Every character carries a **fixed DP cost from 1 to 10** (higher = stronger), and you assemble a team that fits inside a **DP budget**. It is used by [[versus\|Versus]] (offline), the [[ranked-match\|Ranked]] DP queue, [[player-match\|Player Match]], [[world-tournament\|World Tournament]], and [[training\|Training]].

## The team-format conflict (present both, tagged)

Sources **disagree** on the "standard" team shape. This page does not pick a winner — it records both:

| Context | DP budget | Team size | Source (tag) |
|---|---|---|---|
| **Offline / Versus** | **15** (default) | **up to 5** characters | research/01 overview (**community**) |
| **Offline / Versus / WT / Training** | **10 / 15 / 20** selectable, persists | (per chosen budget) | research/06 + research/05 (**official** — May 26 2026) |
| **Ranked DP queue** | **15** (ranked standard) | **3** characters | research/05 meta (**community**) |
| **Ranked DP queue** (overview claim) | **15** | **5** characters | research/01 overview (**community**) |

> **Honest reconciliation:** all sources agree the **DP budget is 15** in the default/ranked case. They **conflict on team size** — the overview research says **5 fighters**, the meta/ranked research says the **ranked DP queue uses 3-character teams**. The **10/15/20 budget toggle** is confirmed for **offline / Player Match / World Tournament / Training** (persistent since the **May 26 2026** update); whether the **ranked** budget also changes for Season 1 (given the new toggle) is **not explicitly confirmed** (research/05 §Gaps). Each character is usable once per match.

## DP cost facts

- **Scale:** 1–10 per character.
- **DP1:** exactly **1** character in the whole game — **Mr. Satan**.
- **DP10 (base):** **5** characters — **Beerus**, **Whis**, **Vegito SSGSS**, **Gogeta (Super) SSGSS**, and **Gogeta (GT) SS4**.
- Example costs: Goku (Z-Mid) = **5 DP**, Ultra Instinct Goku = **9 DP**, Gohan Beast = **9 DP**, Saibaman = **1–2 DP**.

## Mechanics tied to DP tier (May 26 2026 update)

- **Auto-reflect** during Sparking! Mode is **restricted to DP7+** characters — a direct nerf to cheap-character turtling.
- **DP scaling widened** — "differences in DP between characters made more pronounced in all modes," so a DP7 vs DP3 gap is now larger. This is why the **DP-efficiency meta** (cheap overperformers) shifted; see [[ranked-match]].

## Competitive note

A typical 15-DP shell is **1 premium carry (DP ~9–10) + cheap value bodies**; under the new rule those cheap bodies ideally stay **DP7+** to keep auto-reflect access.
