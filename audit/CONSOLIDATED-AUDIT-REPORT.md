# Sparking! ZERO Wiki — Consolidated Audit Report

**Date:** 2026-06-15 · **Patch under audit:** v2.2 (2026-05-26 update) · **Build:** green, 1,144 static pages, exit 0
**Method:** 10 parallel Opus 4.8 sub-agents (one per domain) verifying **against the datamine** (`data-mined/raw/` → parsed JSON → enrichment), explicitly **not** trusting online sources. The orchestrator then **independently re-verified the 6 highest-severity / conflicting findings** against the freshly-built HTML and raw data before publishing. Per-agent detail lives in `audit/agent-01..10-*.md`.

---

## 0. Headline

The corpus is **numerically very accurate and builds green.** Across the generated collections, agents recomputed thousands of values from the raw layer and found **near-zero wrong numbers**: 3,675 character numeric-field comparisons (0 wrong), 611 blast-user rows (0 wrong), 417 BlastForte skill-cost pairs (0 wrong), 164 transformation stat-deltas recomputed (0 wrong), 83/83 datamined-damage claims traced to a real raw override (0 honesty violations in blasts).

The real problems cluster in **four buckets**, none of which are "the numbers are wrong":
1. **One systemic provenance-honesty defect** — `confidence: "datamined"` is hardcoded on ~376 generated pages that carry **community** DP (and class-default damage). This is the single most repeated finding (Agents 1, 4, 6, 10).
2. **Two real rendering/link bugs in `lib/markdown.ts`** — the escaped-pipe wikilink failure (broad) and a NUL-sentinel leak in nested headings (2 pages).
3. **A small cluster of genuinely-wrong datamined *claims* on curated mechanics pages** (skill-stock counts, lightning-attack pursuit) that trusted a third-party datamine site over the actual files.
4. **Consistency/logic drift** in a few guides (DP math busting the 15 cap), docs (HP-tier counts), and dates.

### Orchestrator verification verdicts (the conflicts)
| Claim | Source agent(s) | Verdict | Evidence |
|---|---|---|---|
| Escaped-pipe `[[slug\|Label]]` silently renders as plain text | A7, A8 | **CONFIRMED** | `bojack…html`: `From Bojack to Full-Power Bojack.` renders unlinked (generator emitted `[[bojack\|Bojack]]`) |
| autolink `/ (\d+) /` corrupts 346 prose/table numbers (BLOCKER) | A9 | **REFUTED — false positive** | `lib/markdown.ts` sentinel is **`\x00`** (NUL), not a space (L44/L63). Fresh build's `\| 7 \|` cells render `7`, not `undefined`. A9's `Get-Content` read showed NUL as a space and its replica reproduced a bug the real code can't trigger. |
| NUL leaks into headings that contain a wikilink/inline-code | A7 | **CONFIRMED — scoped to 2 pages** | NUL-scan of all built HTML: only `matchups-and-counterpicks.html` (32 NUL, ~15 headings) + `offense-and-pressure.html` (4 NUL, 2 headings) |
| skill-count page "max 4–5 / ki-drain androids +2" tagged datamined is wrong | A4 | **CONFIRMED** | `system_constants.json`: maxSkillStock ∈ {4,6,7} (**no 5**); Android 19 & Dr. Gero initialSkillStock = **1**, not 2 |
| Saibaman is DP2; guide team math busts 15-DP cap using DP1 | A6 | **CONFIRMED** | `saibaman.md:7` `dp: 2` (canonical); guide example therefore = 16 DP |
| Frost/Krillin advertise supers that render nowhere | A1 | **CONFIRMED** | `frost.md:47,54` claim "two 30,000-ki supers"; moveset `:25-41` lists 0 Blast 2 (names `null` in data → dropped by `gen_content.py:203-205`) |

---

## 1. BLOCKER / HIGH (fix first)

### H1 — Escaped-pipe wikilinks silently fail (renderer regex bug) — *systemic*
`lib/markdown.ts` `renderMarkdown` wikilink regex `\[\[([^\]|]+)(?:\|([^\]]+))?\]\]` lets the **backslash** in the generator's `[[slug\|Label]]` be captured into the target (`bojack\`), so `normalizeSlug` can't resolve it and the link degrades to plain text.
- The generator emits **every** labeled wikilink with the escaped pipe (`gen_content.py:416,511-513,702-704`), so **~1,020 of 2,591 wikilinks (39%)** fail to resolve as links. `autolink` masks most (re-links the label where it's a known page name), but **~105 cross-references are fully lost** across 68 pages, plus **58 blast super↔ultimate sibling links** and the in-table skill/transform links lose their link affordance.
- **Why every audit said CLEAN:** `audit.py`/`fix_links.py` strip the `\` before checking (so they validate a target the renderer never sees); `audit_v3/v4` only scan built `href=`s (these never become hrefs). **False-clean** — see A7 #4, A8 #2.
- **Fix:** one line — make the wikilink regex consume an optional escaping backslash before the pipe, e.g. `\[\[([^\]|\\]+)\\?(?:\|([^\]]+))?\]\]`. Re-run audits afterward.
- Sources: Agent 7 (H1), Agent 8 (#1). Verified by orchestrator on `bojack-to-full-power-bojack.html`.

### H2 — `confidence: "datamined"` over-claimed on ~376 community-DP pages — *systemic provenance*
`gen_content.py:310,391,590` hardcode `confidence: "datamined"` on all characters/blasts/transformations, but those pages carry **DP** (208 characters) and **dpFrom/dpTo** (163/164 transformations) and DLC DP (34 values) — and CLAUDE.md's prime rule is "**DP is community, never datamined**."
- Sharpest subset: **163 transformation bodies literally state "all numbers datamined from CharacterData"** while showing community DP (e.g. `transformations/jiren-to-jiren-full-power.md:10,16,21`).
- Character pages are gentler (their `sources` *do* cite `research/02 (Game8/Fandom)` for DP, e.g. `goku-z-early.md:81`) — but the page-level `confidence` enum is still coarse.
- **Fix:** either add a per-field provenance model, or set generated page `confidence` to `community` (since they mix datamined + community), or split DP out under its own community tag. At minimum, stop emitting the "all numbers datamined" sentence on transformation bodies that print DP.
- Sources: Agents 1 (H), 4, 6 (H2), 10 (H1+H2). Directly confirmed by orchestrator.

### H3 — NUL sentinel leaks into nested-protected headings (visible garbage) — 2 flagship pages
`lib/markdown.ts` `autolink` protects spans with a `\x00N\x00` placeholder and restores in a **single** `.replace` pass (L63). When a protected span (heading) **contains** another protected span (a converted wikilink or inline code), the inner placeholder is not restored, leaving literal NUL bytes.
- `guides/matchups-and-counterpicks.html`: the entire **"Top-15 meta picks"** list renders `<h3>1. ␀70␀ — #1 Singles</h3>` … (character names replaced by NUL+index) — ~15 headings.
- `guides/offense-and-pressure.html`: `<h3>Which S1s are flagged unblockable ␀26␀</h3>` and `<h3>The lab evidence ␀38␀</h3>` (inline-code in heading).
- **Fix:** restore in a loop until no `\x00\d+\x00` remains (or restore in reverse insertion order). 
- Source: Agent 7 (H3). Confirmed by orchestrator NUL-scan of all 1,144 pages (only these 2).

### H4 — Curated mechanics pages present **wrong** numbers as `datamined` (trusted a 3rd-party datamine site)
Verified against `system_constants.json`:
- `mechanics/skill-count.md:11-14` "max skill stocks typically **4–5** (Cell/Piccolo 5)" `datamined` → real distribution is **4 / 6 / 7, there is no 5** (Perfect Cell & Piccolo = 6, Babidi = 7). Also `:77` body repeats it.
- `mechanics/skill-count.md:15-18` "ki-drain androids **+2**" `datamined` → Android 19 & Dr. Gero start at **1**; the chars at initialSkillStock 2 are unrelated (Android 13, Roshi, Saibaman…). Repeated on `mechanics/ki-and-charging.md:27-30` and `mechanics/android-class.md:19-22` (5 pages total).
- `mechanics/lightning-attack-pursuit.md:8` "PursuitLimitLightningAttack = 6" `datamined` → that field is **0** in `Numeric.json`; the real cap is `pursuitBaseLimit` 1–4. `glossary/lightning-attack.md:14` cites a non-existent field and **contradicts** it.
- Root cause: these pages' `sources` cite `sparkingzerometa.com datamine` over the actual extract — the exact "don't trust online sources" failure.
- **Fix:** correct the values to the extract and re-tag (the real per-character stock values are datamined; the invented "5" and "+2" are not). Source: Agent 4 (BLOCKER×2 + HIGH×several).

### H5 — Two characters advertise Blast 2 supers that exist in data but render nowhere
`characters.json` has `name: null` on Frost's and Krillin's two 30,000-ki supers, so `gen_content.py:203-205` drops them from the moveset and no blast page is created — yet `frost.md:47,54` and `krillin.md` prose still claim them ("two 30,000-ki supers"). The supers are real (kiCost present) but **invisible across the wiki**.
- **Fix:** recover the super names in `parse_data.py` (check the `ST_BLASTSKILL_<cid>_actSPM*` keys / fallback to asset), or suppress the prose claim. Source: Agent 1 (H), Frost confirmed by orchestrator.

### H6 — `stats/page.tsx` traces the whole project into the serverless bundle (build warning)
`app/stats/page.tsx` reads JSON via `fs.readFileSync(path.join(process.cwd(), rel))` with a dynamic `rel`, so Next's NFT traces the entire repo (incl. `data-mined/raw/`) — the Turbopack "whole project was traced unintentionally" warning. (Agent 9 correctly retracted the "next.config import" premise; the cause is `process.cwd()` + dynamic path.)
- **Fix:** statically scope the reads (import the JSON, or `path.join(process.cwd(), 'data-mined', staticName)`), or add the documented `turbopackIgnore`. Source: Agent 9 (H2).

---

## 2. MEDIUM

- **M1 — slugify drift (latent link footgun).** `gen_content.slugify` strips `'’!.`+punctuation while `lib/content.ts normalizeSlug` strips **nothing** but spaces. ~127/245 character names (and 419 names overall) produce a file slug unreachable by a naive `[[Exact Display Name]]` link; `"Goku Black, Super Saiyan Rosé"` → `…-ros` (é dropped); `[[Energy Blast]]` mis-routes to `/glossary#ki-blast`. **0 live breaks today** (authors used slug-form links) but a guaranteed future bug. Fix: share one slugify (port it to TS, or normalize at lookup). Agents 8 (#3), 9 (M5).
- **M2 — blast slug collisions drop users.** `gen_content.py:338-342` `continue`s on a slug clash because `slugify` folds space==hyphen: **"Full-Power Energy Blast Volley"** collides with another and shows 1 user (true 8); **"High-Speed Rush"** orphans Gohan (Super Hero). Downstream, 8 characters list a Blast 2 with no blast-page user entry. Fix: **merge** colliding entries' `users[]` instead of dropping. Agent 2 (H1/H2 + M).
- **M3 — DP team math errors in flagship guides.** `dp-team-value-math.md` uses **Saibaman as DP1** (canonical = DP2 per `saibaman.md:7`), busting the worked "Kale-centric" team to **16 DP > 15 cap**; `:50` lists **Gohan Beast HP 40,000 "(null)"** though it's datamined **35,000** (→ wrong HP/DP). Also "~5 DP of cheap DP7+ bodies" is impossible (`:68`). Agent 6 (M3/M4).
- **M4 — dead transform stat rows.** `gen_content.py:637-647` reads `sparkingGaugeChargeSpeed`/`preSparkingGaugeDecreaseSpeed`, which the parser never emits → those two delta rows render on **0/164** pages (silent dead code). Agent 8 (#4).
- **M5 — `best_damage` melee override distorts damage.** `gen_content.py:160-176` lets a melee `Power` override beam damage and nulls chip/hits: *Raging Masenko* 500→shown 10,500; multi-bullet moves collapse to one bullet; 54/83 "projectile/beam" damage rows are actually melee `Power` (mislabeled in body). Agents 2 (M/L), 8 (#5).
- **M6 — `numericValue.tag` enum can crash regen.** `lib/schemas.ts:143` allows only `official|datamined|community`; the natural value `confirmed`/`unverified` (valid for the *other* confidence enum) would crash the build if ever used in a mechanic value. Latent. Agent 9 (H3, severity adjusted to MED-latent).
- **M7 — `glossary/page.tsx` renders only `definition`, never `body`.** 74 wikilinks + all glossary body prose are dormant (absent from `glossary.html`). Either intended (definitions-only) or a feature gap — confirm. Agent 7 (M3).
- **M8 — `[[dp-system]]` (×22) always resolves to `/mechanics/dp-system`;** the `/game-modes/dp-system` page is unreachable by wikilink (first-wins priority). Several links intend the mode page. Agents 5 (L), 7 (M1).
- **M9 — research/doc claims contradict the datamine.** `research/02:398-412` says "no datamined HP / HP is community estimate" (false — HP is datamined 30/35/40/45k); `research/04` mislabels a durability index as "HP (datamined)"; `beginner-numbers-guide` §8 says "three HP bands" (there are four). Agent 6 (M2/M6/M7).
- **M10 — Episode-Battle mode count mismatch.** `game-modes/episode-battle.md:19` "12 major routes" vs 13 campaigns summing `sparkingEpisodes`. Agent 5 (M2).
- **M11 — duplicated "Instant Sparking 3→4" change** attributed as *new* to two patches (`patches/v2025-01-20.md:18` and `v2025-12-15.md:18,69`) — unreconciled research/04-vs-05 date conflict. Agent 5 (M3).

---

## 3. LOW / NIT (selected; full lists in per-agent reports)

- **Confidence labeling (community values under datamined banner)** also affects **5 DLC packs** (`dlc/preorder-pack.md:37,53`, etc.) and **6 glossary terms** with research-only sources (`android-class.md:13`, `giant-class.md:13`, `ki-blast.md:13`, `skill-count.md:14`, `smash-attack.md:13`, `super-armor.md:13`). Agents 5 (M1), 10 (M).
- **Date conflicts:** DAIMA Pack 2 `2025-09-24` vs `2025-09-25`; Shallot `2025-06-26` vs `2025-06-27` (page vs patch). `episode-gohan.md:96,101` "Gohan Black" typos (should be "Goku Black"). Agent 5 (L).
- **Doc drift:** `CLAUDE.md:45` / `PLAN.md:90` HP-tier counts "9/14/147/16" match `system_constants.json` but the live content has a few more (story dupes → 9/15/148–150/16); **20 playable fighters have null HP** (giants/fusions, raw `Numeric.Life` absent). Agents 1 (M), 10 (L).
- **`best_damage`/parser edge cases:** `body-change-ultimate` has a stray `\r` in a tag (`parse_data.py:131` strips `\n` not `\r`); `point-blank-kamehameha-ultimate` attributes a Combatives key by file stem (`0000_50.json` vs embedded cid `0050_00`). Agent 2.
- **`Fury` skill has bad enrichment data** (`enrichment/skills.json:527-534`) — claims Gohan (Teen/Adult) users but no character has "Fury" in the datamine; also missing `userCount`. Agent 3 (M1).
- **Dead code / API gaps:** `lib/formulas.ts` `pctChange/dmgPerKi/dmgPerDp/hpPerDp` are never surfaced in the UI (the advertised value-per-DP metrics). Agent 9 (M7).
- **Accessibility:** `<th onClick>` sortable headers (`components/sortable-tables.tsx`, `roster-table.tsx:110-125`) aren't keyboard/ARIA-accessible; meta-board sort mutates a React-owned array. Agent 9 (M6).
- **Self-links:** 85 auto-links point to the current page (10 collections omit the `excludeHref` that characters/blasts pass). Agent 7 (L1).
- **Autolink first-wins mis-targets:** 29 blast names always link `-super` (never `-ultimate`); `Goku (Super)`/`Vegeta (Super)` link to the charId-suffixed slug. Agent 7 (M2).
- **`super-limit-breaking-neo.md:36,62`** says "27 fighters / slots #209-235" but lists 25. `stages/kame-house-tv-dimension.md:6-7` duplicate `variants`. Agents 5, 10.

---

## 4. Verified CLEAN (do not re-litigate)

- **Datamined numbers are faithful:** characters (3,675 field comparisons, 16 cids hand-traced to raw `Numeric.json`), blasts (611 user rows, 83/83 damage claims traced to overrides), skills (417 BlastForte pairs), transformations (164 stat-deltas + 164 moveset diffs recomputed) — **0 wrong values** in each.
- **autolink does NOT corrupt prose numbers** (NUL sentinel; fresh build verified). Agent 9's BLOCKER is a false positive.
- **Structured links are intact:** 163 transformsTo targetSlugs, 611 blast characterSlugs, 1,035 moveset move-links → **0 dead**, 0 missing. Built-HTML href graph: **0 dead routes**, 0 bad `/glossary#` anchors. Search index: 1,153 entries, 0 dups, 0 dead hrefs.
- **No rendered artifacts:** 0 `>undefined<`/`>NaN<`/`[object Object]`, 0 leaked `\|`, 0 leaked `[[`, 0 unformatted big numbers (the lone `>null<` is intentional `<code>` prose; empty `<td>` are the by-design optional note column).
- **Enum conformance:** 0 violations across all 13 collections (no current build/regen crash). Dates: 0 stale, 0 future, 0 malformed; `asOfVersion` canonical on all non-patch pages.
- **Roster/economy invariants:** 208 playable / 37 non-playable correctly split; patch `order` unique + chronological; all 8 episode `battleCount == len(battles)` (150 entries); 196 episode opponents resolve; 34 DLC DP values match enrichment; Season-2 NEO correctly `upcoming` and excluded from 208; ranked = 26 tiers + Season 0 ends 2026-06-30; `v2026-05-26` documents the HpRecovery→0 heal-removal.
- **Confidence done right (models to copy):** `mechanics/vanish-z-counter.md`, `super-counter.md`, `perception.md`, `fusion-and-potara.md`, all movement ki costs (community), the defensive-RPS reciprocity graph, and the meta tier layer (0 placement mismatches across 67 Singles entries; 0 unresolved counters).
- **Note on docs:** the blanket "HpRecovery: 0 on all transforms" in `CLAUDE.md:46`/`PLAN.md:58` is an over-simplification — 27/164 transforms legitimately heal 5k–10k in the shipped data (the **pages are correct**; the doc rule is the inaccuracy). Agent 3.

---

## 5. Prioritized fix queue

1. **Fix the wikilink regex** (`lib/markdown.ts`) — one line; restores ~1,020 links incl. 58 blast siblings + 105 lost cross-refs (H1).
2. **Fix the NUL single-pass restore** (`lib/markdown.ts`) — loop until stable; clears garbage headings on 2 guides (H3).
3. **Resolve the confidence model** — generated pages stamped `datamined` while carrying community DP (H2 + LOW DLC/glossary).
4. **Correct the wrong "datamined" mechanics values** — skill-stock 4/6/7 (no 5), ki-drain androids = 1, lightning-attack pursuit (H4).
5. **Recover Frost/Krillin null super names** in the parser (H5).
6. **Unify slugify** Python↔TS to kill the latent link footgun (M1), and **merge colliding blast users** instead of dropping (M2).
7. **Fix `stats/page.tsx` tracing** (H6); fix DP team-math/Gohan-Beast-HP in guides (M3); dead transform stat rows (M4); `best_damage` melee mislabel (M5).
8. **Add `confirmed`/`unverified` to `numericValue.tag`** or guard it (M6); decide on glossary `body` rendering (M7).

> Reminder for fixes: characters/blasts/skills/transformations/stages/shop are **generated** — fix `scripts/*.py` + `enrichment/*.json` and regenerate, never hand-edit those files. Mechanics/glossary/guides/patches/dlc/game-modes/episode-battles are curated (edit directly, one file at a time). There is **no git safety net** — be deliberate.

---

## 6. Per-agent reports
`agent-01-characters.md` · `agent-02-blasts.md` · `agent-03-skills-transformations.md` · `agent-04-mechanics-glossary.md` · `agent-05-patches-dlc-episodes-modes.md` · `agent-06-guides-research-meta.md` · `agent-07-links.md` · `agent-08-python-code.md` · `agent-09-typescript-code.md` · `agent-10-crosscutting.md` (+ each agent's read-only `aN_*.py` probes). Orchestrator verification probes: `verify_sentinel.py`, `verify_nul.py`.
