# DRAGON BALL: Sparking! ZERO — Codex
**Numbers-first knowledge base** · started 2026-06-10 · sibling project to `C:\vaults\xenoverse_2`

## 1. Vision

One data-heavy wiki for Sparking! ZERO where **every page leads with numbers**: datamined HP and
ki costs per fighter, DP costs, quantified patch history (old→new), mechanics frame data, full
shop price tables, and a current-meta layer that is explicitly patch-tagged. The XV2 codex
initially shipped with too few numbers — this project's prime directive is the opposite:
**quantitative data only; prose exists to explain the numbers.**

## 2. Architecture (same stack as xenoverse_2)

```
game files (UE5.1.1 IoStore paks)                 web research (6 briefs in /research)
        │ tools/extractor (C# CUE4Parse)                   │
        ▼                                                  │
data-mined/raw/*.json  ──  scripts/parse_data.py  ──►  data-mined/*.json (reference tables)
                                                           │
                       data-mined/enrichment/*.json  ◄── agent/manual curation (DP, eras, tiers)
                                                           │
                                  scripts/gen_content.py ──►  content/{characters,blasts,skills,stages,shop}
                                  hand/agent-written      ──►  content/{mechanics,patches,dlc,game-modes,
                                                                episode-battles,guides,glossary}
                                                           │
                            Next.js App Router (app/) + Zod content layer (lib/) ──► static site
```

- **Source of truth = typed markdown** (`content/`), validated by `lib/schemas.ts` (Zod) at build.
- **Generated collections** (characters/blasts/skills/stages/shop) are owned by
  `scripts/gen_content.py` — never hand-edit those files; edit the enrichment overlays and regen.
- **Curated collections** (mechanics/patches/dlc/game-modes/episode-battles/guides/glossary) are
  hand/agent-written markdown.
- Every fact-bearing page carries `asOfVersion`, `lastVerified`, `confidence`
  (confirmed | datamined | community | unverified) and `sources`.

## 3. Game-data pipeline (reproducible)

| Step | Tool | Notes |
|---|---|---|
| Mount paks | `tools/extractor` (dotnet 9 + CUE4Parse 1.2.2) | UE **5.1.1**, IoStore; AES key in Program.cs (community-published); Oodle DLL auto-downloaded to `tools/` |
| Mappings | `tools/Mappings_fresh.usmap` | Current-patch UE4SS dump (2026-06-10); usmap v4 needs the vendored `tools/CUE4Parse` build |
| Extract | `dotnet run -c Release` in `tools/extractor` | Dumps ~60 MasterDataAsset folders + StringTables + en locres to `data-mined/raw/` |
| Parse | `python scripts/parse_data.py` | → `data-mined/{characters,dlc,shop,ranks,stages,wishes,skills_catalog,blast_index,system_constants}.json` |
| Generate | `python scripts/gen_content.py` | → 850+ content pages; merges `data-mined/enrichment/*.json` overlays |
| Build | `npm run build` | Zod-validates every page |

### Data-gap status (RESOLVED 2026-06-10 via fresh UE4SS usmap dump)
A current-patch `tools/Mappings_fresh.usmap` (usmap v4 — requires CUE4Parse built from source,
vendored at `tools/CUE4Parse`, net10.0) was dumped from the running game with UE4SS
(experimental-latest; boot-crash fixed by disabling all [Hooks] except ProcessInternal/ConsoleExec).
It unlocked:
- `CharacterData_*` → **form changes/fusions/Potara with skill-stock costs, HP recovery,
  cooldowns, partner requirements** (→ `data-mined/transformations.json`, 208 edges → 130 pages),
  costumes, series/gender/unlock tags.
- `BlastForte1/2_*` → **per-character S1 skill mapping + ExpendBlastStock costs + unblockable flags**
  (→ skills pages now list datamined users).
- Confirmed in-data: `HpRecovery: 0` on transforms (May 26, 2026 heal-removal is in the shipped data).

### Damage status (CORRECTED 2026-06-10 after full-corpus sweep)
Per-move damage IS partially datamined — the earlier "blueprint-only" conclusion was a sampling
error (one character folder):
- `BulletSetting/BulletParam_<cid>_act*` (606 overrides incl. 47 ultimates): Power / Shave(chip) /
  BeamPower / BeamShave / multi-hit / ExpendEnergy per projectile move.
- `Combatives/<cid>` per-action overrides (1,761 Power entries + ArmorBreakLevel / EnergyGain /
  HitStop / Super-Counter-avoidable flags).
- `BulletSetting/Common`: generic ki-blast defaults (e.g. 200 dmg / 40 chip / 2,000 ki).
- Moves WITHOUT overrides inherit blueprint class defaults — only those still need community labs.
- `OperationGuide` GR records: per-slot blast **category** (Beam/Rush/…) + ability tags
  (Chargeable/Unguardable/…); Forte records: per-skill **in-game descriptions** (168/170 mapped).

### Remaining genuine gaps
- **DP cost is not in the game files** — community-sourced (research/02 → enrichment).
- **Vanish/Z-Counter ki cost is not in the parameter tables** (the old "2,800 [datamined]" was a
  launch-usmap mislabel of SparkingModeGaugeDecreaseSpeed) — community ≈½ bar.
- Non-overridden moves' damage (class defaults) — community labs.
- After each game patch, re-dump the usmap if new DLC assets fail to parse.

## 4. Currency rules (first-class, like XV2 §11a)

- `lib/version.ts` `CURRENT_VERSION` = the documented patch (now: **May 26, 2026 update**,
  Steam build 22517964). Bump it every patch.
- Patch-update workflow: Steam updates game → re-run extract/parse/gen (datamined numbers refresh
  automatically) → add the new `content/patches/` page → re-verify `content/guides/` meta pages →
  bump `CURRENT_VERSION` + `lastVerified`.
- Meta/tier claims must name their patch; tier lists older than the current patch are history.

## 5. Key datamined facts (sanity anchors)

- HP tiers: **30,000 / 35,000 / 40,000 / 45,000** (9 / 14 / 147 / 16 fighters); 10,000 HP per bar.
- Sparking!-mode gauge drain: **2,800/s** uniform (the launch-usmap mislabeled this as a vanish cost — vanish cost is NOT in the files; community ≈½ bar).
- Energy units: 10,000 = 1 ki bar; supers typically 30,000; ultimates 50,000.
- Ranked: 26 tiers (D5→Z); Season 0 ends 2026-06-30.
- Roster: 208 slots live (182 launch + DLC); Season 2 "Super Limit-Breaking NEO" lands Summer 2026
  with 30+ more and two new mechanics (Chain Blast, Sparking! Boost) — expect a full re-verify pass.

## 6. Research corpus

`research/01..06` — agent-written, numbers-first briefs (overview/economy, roster+DP, patches,
mechanics frame data, meta/tiers, PvE/DLC/unlocks), each with sources + gaps sections. These are
the provenance layer for everything not datamined.

## 7. Strategy & UX layer (added 2026-06-10, post-audit)

- **Strategy content:** Defense Bible / Offense & Pressure / Matchups & Counterpicks /
  Settings & Controls guides; per-campaign Episode Battle walkthroughs with boss tactics;
  strengths/weaknesses/playstyle/how-to-fight on **all 208 roster slots**
  (via `data-mined/enrichment/sw_a.json` + `sw_b.json`, merged by the generator).
- **UX:** global ⌘K search (`public/search-index.json`, emitted by gen_content.py);
  filterable/sortable roster table (era/source/tier/class/DP, story-only toggle);
  `/meta` visual tier board driven by `data-mined/meta.json` (singles/DP tabs + counter-pick
  table); filtered blasts/skills tables; grouped two-row nav; guide-first home page.
- **Transformation pages** carry exact datamined deltas: stat-change table (HP/ki/sparking
  before→after with Δ), full moveset diff with costs, and the honest note that attack/defense are
  per-move values, not flat form multipliers.

## 8. Roadmap

1. Season 2 (Summer 2026): new mechanics pages (Chain Blast, Sparking! Boost), 30+ roster adds,
   Limit Breaker Journey mode page; re-dump usmap; refresh meta.json + tier guides.
2. Per-move damage datamine (blueprint/anim-notify level) — the one remaining numeric layer.
3. Optional: per-page JSON API, AI-layer skill — mirroring XV2 plan.
