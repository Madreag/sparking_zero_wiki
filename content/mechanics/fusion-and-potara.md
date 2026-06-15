---
slug: "fusion-and-potara"
name: "Fusion & Potara"
category: "system"
input: "L2 + transform input with the required partner alive on your team (DP/team battles)"
values:
  - label: "Fusion Dance cost (typical)"
    value: "3–5 skill stocks (e.g. Gogeta (Super) 3; Super Gogeta (Z) / Gogeta (GT) 4; SSGSS tier 5)"
    tag: "datamined"
    patch: "v2.2 (2026-05-26)"
  - label: "Potara cost (typical)"
    value: "3–5 skill stocks (Vegito 3; Super Vegito 4; Vegito SSGSS 5)"
    tag: "datamined"
    patch: "v2.2 (2026-05-26)"
  - label: "HP recovery on fusing"
    value: "0 (no heal — across all 38 datamined fusion/Potara records)"
    tag: "datamined"
    patch: "v2.2 (2026-05-26)"
  - label: "Max-HP added on fusing"
    value: "0 (the fused form uses its own HP pool/state rules, no bonus max HP)"
    tag: "datamined"
  - label: "Cooldown"
    value: "5.0s (uniform; one Goku (Super) → Vegito record at 0s)"
    tag: "datamined"
  - label: "Datamined records"
    value: "38 fusion/Potara edges (22 Fusion records + 16 Potara records)"
    tag: "datamined"
counters: []
counteredBy:
  - "Killing the required partner before the fusion is performed"
  - "Pressure that denies the skill-stock bank (stocks regen ~1 per 14s)"
summary: "Team-battle fusions are datamined as form-changes with partner requirements: 3–5 skill stocks depending on the result's power, zero HP recovery, zero bonus max HP, 5s cooldown. The cost ladder (Vegito 3 → Super Vegito 4 → SSGSS 5) prices the strongest forms in the game."
changeHistory:
  - version: "Jun 23, 2025 (v2013)"
    date: "2025-06-23"
    change: "Singles/DP balance split — fusion-form HP standardization in Singles changed the value math of fusing vs. picking the fusion outright."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964) — CharacterData BattleAssets.Fusion/Potara records"
  - "data-mined/transformations.json (38 fusion/potara edges)"
---
In team modes, characters with a canon partner can fuse mid-battle — mechanically a
[form change](/transformations) with extra requirements, all datamined from `CharacterData`:

## The numbers

| Parameter | Value | Notes |
|---|---|---|
| Skill-stock cost | **3–5** | scales with the result: Vegito **3**, Super Vegito **4**, Vegito SSGSS **5**; Gogeta (Super) **3**, Super Gogeta (Z)/Gogeta (GT) **4** |
| Partner requirement | specific character alive on team | e.g. Goku (Z - End) needs Vegeta (Z - End) for [[goku-z-end-to-vegito\|Potara → Vegito]] |
| HP recovery | **0** | fusing is not a heal (uniform across all 38 records) |
| Bonus max HP | **0** | `AddMaxHP` is 0 on every record |
| Cooldown | **5.0s** | before another change can occur |

## Strategy math

- A 3-stock Potara into Vegito converts ~42 seconds of passive [[skill-count|stock regen]]
  (~1 stock / 14s) into one of the game's strongest forms — but the same 3 stocks fund
  [[perception]] reads or a [[revenge-counter]]. Fusing is a *win-more* spend unless you're
  stabilizing behind its fresh kit.
- In DP battle, fusing effectively trades two roster slots' DP for one top-tier body — check the
  [[dp-team-value-math|DP value guide]] for when the math favors just drafting the fusion outright.
- Every fusion edge with exact costs is on its own page: see the
  [transformations index](/transformations) (kind = fusion).
