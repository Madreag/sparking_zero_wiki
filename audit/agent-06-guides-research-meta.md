# Audit Agent 6 — Guides, Research Briefs & Meta/Tier Layer

**Scope:** 12 `content/guides/*.md`, 6 `research/01..06*.md` provenance briefs, `data-mined/meta.json`, the `/meta` tier board (`components/meta-board.tsx` + `app/meta/page.tsx`), and the in-scope `content/game-modes/dp-system.md`. Focus: tier consistency, patch-tagging, DP arithmetic, confidence honesty, research-vs-datamine, internal links, cross-guide contradictions.

**Source of truth:** `data-mined/*.json` + `system_constants.json` + `lib/version.ts`. Tiers / matchups / win-rates / DP are COMMUNITY synthesis (must be patch-tagged + community, never datamined).

**Method:** read all 12 guides + 6 briefs + dp-system page in full; wrote two read-only probes (`audit/a6_probe.py` = tier/counter/DP-math; `audit/a6_links.py` = wikilink resolution) and recomputed example teams by hand against `lib/formulas.ts`. No content/data/code modified.

---

## Severity counts

| Severity | Count |
|---|---|
| BLOCKER | 0 |
| HIGH | 2 |
| MEDIUM | 7 |
| LOW | 6 |
| NIT | 2 |

**Headline:** The three tier layers (meta.json ↔ tier-list guide ↔ character-page `tier`) are **remarkably consistent** — the probe found **0 placement mismatches** across 67 Singles entries and **0 unresolved counter slugs**. The real damage is in **(a)** two guides tagged `confidence: datamined` while built on community DP/tiers (one of them re-citing the CLAUDE-forbidden `vanish = 2800` mislabel), **(b)** a Saibaman-DP1 error that propagates from `research/05` into two guides and **busts a worked 15-DP team to 16**, **(c)** a wrong Gohan-Beast HP in the value-math guide, and **(d)** a pervasive misleading `k` suffix on model scores.

---

## Coverage

| Layer | Coverage |
|---|---|
| `content/guides/*.md` | **12 / 12** read in full |
| `research/01..06*.md` | **6 / 6** read in full (sources + gaps sections confirmed present in all 6) |
| `data-mined/meta.json` | full: Singles (67 entries / 5 bands), DP (47 / 5 bands), 15 counter rows, `unmatched` |
| `/meta` board render | `meta-board.tsx` + `app/meta/page.tsx` reviewed |
| character pages cross-checked | 245 parsed; **67 Singles + 47 DP** meta entries tier-checked; **all 15 counter picks + ~120 beats/losesTo refs** resolved |
| `game-modes/dp-system.md` | read |
| DP math recomputed | 24 HP/DP rows + **5 example teams** end-to-end vs `formulas.ts` |
| wikilinks checked | **143** across the 12 guides |
| Probes | `audit/a6_probe.py`, `audit/a6_links.py` (both read-only) |

---

## 1. LEAD — Tier-consistency table (meta.json ↔ tier-list guide ↔ page `tier`)

**Convention discovered (load-bearing):** `meta.json` uses bands **Z / S / A / B / D** (Singles) and **Z / S / A / C / D** (DP). The character schema `tier` enum is **S / A / B / C / D / unranked — there is no `Z`**. The page `tier` encodes the **Singles** placement under a *systematic relabel*:

`board Z → page S` · `board S → page A` · `board A → page B` · `board B → page C` · `board D → page D`

The `current-meta-tier-list.md` guide makes the same relabel explicit in its headers (`S (Z-rank)`, `A (S-rank)`, …). Applying that map, the probe result is:

- **meta.json Singles ↔ page `tier`: 0 mismatches** (all 67 ranked Singles slugs agree).
- **meta.json (Singles & DP) ↔ tier-list guide: identical** band membership (the guide is generated from `research/05` = `meta.json`), with **one** editorial divergence (Super Buu variants — see L2).
- **counters[]: 0 unresolved** slugs.

So there is **no per-character tier contradiction** — a genuinely clean result. The findings below are the *exceptions, label hazards, and cross-mode divergences*, plus the small data gaps.

### 1a. Exceptions / gaps (the only tier-table defects)

| # | Slug | meta Singles | meta DP | page `tier` | Issue |
|---|---|:--:|:--:|:--:|---|
| T1 | `gotenks-super-saiyan` | **S** | – | *(none)* | **In Singles S-band but page has NO `tier`** (page: DP7, 45 000 HP). Expected page `A`. |
| T2 | `super-buu` "variants" (generic) | listed **A-band** by guide/research | – | n/a | `meta.json` `unmatched` (line 280) labels it **"B-tier Singles"**; guide+research place "Super Buu variants" one band higher (A). 1-band divergence. |
| T3 | 21 DP-ranked slugs incl. `spopovich`, `super-zarbon`, `vegeta-mini-super-saiyan-2/3`, `gohan-super-hero-super-saiyan`, `goku-super-super-saiyan`, `full-power-bojack`, `android-19` | – | **Z/S/A** | page `tier` is empty for **every DP-only pick** (page tier = Singles only). Several are **DP Z/S** (top DP) yet show untiered on their page. |

### 1b. Cross-mode divergence (NOT errors — shown for the "full table" requirement)

These are the picks whose Singles vs DP standing diverges hardest; all are internally consistent (page tier follows Singles), but they are where a reader is most likely to misread "tier":

| Slug | Singles (board→page) | DP band | Page `tier` |
|---|:--:|:--:|:--:|
| `whis` | Z → S | C | S |
| `beerus` | S → A | C | A |
| `jiren-full-power` | Z → S | C | S |
| `goku-super-ultra-instinct` | Z → S | C | S |
| `gogeta-gt-super-saiyan-4` | Z → S | C | S |
| `master-roshi-max-power` | *(unranked Singles)* | **Z** | D |
| `yajirobe` | D → D | **Z** | D |
| `recoome` | B → C | **Z** | C |
| `saibaman` | D → D | **S** | D |
| `videl` | D → D | **S** | D |
| `gohan-beast` | Z → S | **Z** | S |

> Full 90-row machine dump (every Singles + DP slug, board vs page) is reproducible via `python audit/a6_probe.py` (CHECK 1). It prints `mismatches: 0; unresolved slugs: 0`.

### 1c. Label hazard (MEDIUM-worthy design note)

The board calls the top tier **`Z`** while every character page calls it **`S`** (schema has no `Z`). The guides bridge this with "S (Z-rank)" headers, but the **`/meta` board and a character page show the same fighter as `Z` and `S` respectively** with no on-board explanation. This is the single most likely source of reader confusion in the tier layer. *Fix:* add a one-line "board Z = page S" note to `app/meta/page.tsx` header, or add `Z` to the character `tier` enum and regenerate. (Schema/UX change — flag to Agents 9/10.)

### 1d. counters[] resolution — PASS

All 15 `meta.json` `counters[].slug`, plus every `beats[]` and `losesTo[]` reference, resolve to a real `content/characters/*.md` slug (`a6_probe.py` CHECK 2 = `0 unresolved`). The `nameOf[s] ?? s` fallback in `meta-board.tsx:103/111` would silently print a raw slug on any miss, but there are no misses. *Note (NIT):* `meta.json:280` `"unmatched": [...]` is **not consumed** by `app/meta/page.tsx` (its `Meta` type omits the field), so the "Super Buu variants" note is dead data, never rendered.

---

## 2. Patch-tagging — PASS (strong)

Every guide carries `asOfVersion: "v2.2 (2026-05-26 update)"`, `asOfDate: "2026-05-26"`, `lastVerified: "2026-06-10"`. `meta.json` carries `"asOf": "v2.2 (2026-05-26 update)"` + `"updated": "2026-06-10"`, and `app/meta/page.tsx:33` renders both in the board header. No undated "current/best" tier claim was found. `current-meta-tier-list.md:24` explicitly **excludes the stale Game8 "Nov 2024" list** and flags it as history — exactly the CLAUDE rule ("a tier list older than CURRENT_VERSION is history"). `cheese-tech-status-board.md`, `defense-bible.md`, `matchups-and-counterpicks.md` all consistently date claims to May 26 2026 and tag older patches as history. **No patch-tagging findings.**

One ambiguity (see L4): the **ranked "Season 1"** (July 1 2026) referenced by `ranked-climbing-guide.md` is a *ranked-season* label, distinct from the *content* "Season 2 (Super Limit-Breaking NEO)" in `version.ts.nextContent`. The guides never disambiguate "ranked season" vs "content season," and `version.ts.era` even says "Season 1 complete" (content). Not a patch-tag error, but a numbering hazard.

---

## 3. DP team math (recomputed end-to-end vs `lib/formulas.ts`)

`formulas.ts`: `hpPerDp = Math.round(hp/dp)`; `dmgPerDp = Math.round(damage/dp)`. Budget 15, team ≤5. The HP/DP table in `dp-team-value-math.md` rounds correctly **wherever its inputs are right** (Kale 45000/7=6429 ✓, Mini Vegeta SS2 40000/6=6667 ✓, Nappa 40000/3=13333 ✓, etc. — 22/24 rows clean). The two bad inputs (Saibaman DP, Gohan Beast HP) are below. I recomputed **5 worked teams**:

| Team (guide) | Guide claim | Recomputed | Verdict |
|---|---|---|---|
| Triple-ladder: Broly Z 5 + Broly S 5 + Android 13 5 | 15 DP; endpoints 9+9+7=**25**; **135 000 HP**; **8** stocks (3+3+2) | 5+5+5=15 ✓; 25 ✓; 45 000×3=135 000 ✓; 8 ✓ | **all correct** |
| Gohan Beast core: Gohan Beast 9 + Roshi MP 2 + Android 19 4 | "= 15 DP" | 9+2+4=15 ✓ | DP correct (HP aside, see M2) |
| Heavy-anchor: Broly 9 + Recoome 3 + Spopovich ~3 | "= 15 DP" | 9+3+2=**14** (Spopovich is DP2) | under budget; "~DP3" hedged — OK |
| **Kale-centric: Kale 7 + Recoome 3 + Android 19 4 + Saibaman 1** | "**= 15 DP** across four bodies" | 7+3+4+**2**=**16** (Saibaman is **DP2**) | **❌ OVER the 15 cap** (M1) |
| **Premium+value: SS4 Gogeta 10 + "~5 DP of cheap DP7+ bodies"** | "10 + 5 split across two cheap bruisers" | 10+5=15 sum ✓, but **5 DP cannot field any DP7+ body** | **❌ logically impossible** (M3) |

### [MEDIUM] M1 — Saibaman is DP2, not DP1 → wrong HP/DP and a busted team
- **Where:** `dp-team-value-math.md:33` (`Saibaman | 35,000 | 1 | 35,000`), `dp-team-value-math.md:72` (Kale-centric team uses "Saibaman (DP1)"), `current-meta-tier-list.md:52` ("Saibaman (DP1)"). Origin: `research/05-meta-pvp-tiers.md:122` ("Saibaman (1)") + §2b "Saibaman (DP1)".
- **Evidence:** `content/characters/saibaman.md` → `dp: 2`, `hp: 35000`; `research/02-roster-dp-dlc.md:246` lists Saibaman **DP 2**, and `research/02`'s own DP distribution states **"DP1 = exactly 1 character: Mr. Satan"** (line 49) — so Saibaman *cannot* be DP1. Probe CHECK 3: `saibaman … DP DIFF page=2 guide=1; HP/DP DIFF true=17500 guide=35000`.
- **Consequences:** (a) HP/DP index 35,000 is wrong → **17,500** (35000/2). (b) The "Kale-centric efficient core" team (`:72`) sums to **16 DP, illegal** under the 15 cap. (c) Saibaman's HP/DP no longer "ties Mr. Satan for highest in game."
- **Fix:** set Saibaman DP=2 everywhere; HP/DP=17,500; recompute/repair the Kale-centric team (e.g. drop Android 19 to a DP3 or remove a body); fix `research/05` Saibaman(1)→(2).

### [MEDIUM] M2 — Gohan Beast HP is 35,000 (datamined), not "40,000 (null)"
- **Where:** `dp-team-value-math.md:50` (`Gohan Beast | 40,000 (est., null in datamine) | 9 | ~4,444`) and `:25` (null-HP caveat list includes Gohan Beast).
- **Evidence:** `content/characters/gohan-beast.md` → `hp: 35000`, `hpInherited: true`, `dp: 9`. `matchups-and-counterpicks.md:99,103` correctly says **"35,000 HP [datamined]"**. Probe CHECK 3: `gohan-beast … HP DIFF page=35000 guide=40000; HP/DP DIFF true=3889 guide=4444`.
- **Detail:** Of the 6 fighters the caveat calls "null HP," **5 are genuinely null** (Vegito SSGSS, Gogeta GT SS4, Jiren FP, Toppo GoD, Cell Max — all confirmed `hp:` absent), but **Gohan Beast resolves to 35,000** (inherited from Gohan Super Hero's 35k band). So the guide both (a) mis-lists Gohan Beast as null and (b) estimates 40,000 when the resolved value is 35,000.
- **Fix:** Gohan Beast row → HP 35,000, HP/DP **3,889**; remove it from the null-HP caveat list (keep the other 5).

### [MEDIUM] M3 — "Premium + value" archetype is internally contradictory
- **Where:** `dp-team-value-math.md:68` ("one 10-DP fusion carry + **~5 DP of cheap DP7+ bodies** for auto-reflect access … 10 (SS4 Gogeta) + 5 split across **two cheap bruisers**"). Origin: `research/05-meta-pvp-tiers.md:125` (same wording).
- **Evidence:** a DP7+ body costs **≥7 DP**; 5 remaining DP cannot contain any DP7+ body. Two bruisers totalling 5 DP are necessarily **sub-DP7**, which the *same guide* (`:80`, `:49`) says **lose auto-reflect**. So the bullet's stated rationale ("DP7+ bodies for auto-reflect") is impossible and self-contradicting.
- **Fix:** reword — the **DP10 carry** is the DP7+ body (it already satisfies the gate); the 5 DP of cheap bodies are sub-DP7 chip/utility that knowingly forgo auto-reflect. Drop "DP7+" from the cheap-body description.

---

## 4. Confidence honesty (the two HIGH findings)

### [HIGH] H1 — `beginner-numbers-guide.md` re-cites the forbidden `vanish = 2,800` datamined mislabel
- **Where:** `beginner-numbers-guide.md:9` (`confidence: "datamined"`) and **`:11`** sources: `"data-mined/characters.json (vanishKiCost 2800, ultimate kiCost 50000, super kiCost 20k/30k/40k, hp tiers)"`.
- **Evidence:** CLAUDE.md §Datamine-rules and PLAN.md §5 are explicit: **`2,800/s` is the uniform Sparking-mode gauge drain, NOT the vanish cost; vanish cost is not in the parameter tables at all** ("the launch-usmap mislabeled `SparkingModeGaugeDecreaseSpeed` as a vanish/Z-Counter cost … Never cite vanish cost as datamined"). `data-mined/characters.json` has **no `vanishKiCost` field** (grep: `sparkingDrainPerSec` and `skillGaugeGains.vanishExchangeRate` exist; `vanishKiCost` does not). The body of the very same guide (`:19-21`) **correctly** says a vanish costs "≈5,000 ki — about half a bar `[community]` … the cost is not stored in the parameter tables." So the `sources` line **invents a datamined field, attributes the Sparking-drain number to it, and contradicts the guide's own body** (2,800 vs 5,000).
- **Why HIGH:** this is the exact mislabel CLAUDE says "caused real bugs," reintroduced in machine-readable provenance, and it stamps the page `confidence: datamined` while its #1 and #4 headline numbers (vanish cost, ~2f Super Counter) are community-measured.
- **Fix:** drop `vanishKiCost 2800` from `sources`; set page `confidence: "community"` (or split — datamined for HP/ult-ki, community for vanish/SC). Keep the (correct) body wording.

### [HIGH] H2 — `dp-team-value-math.md` is tagged `confidence: "datamined"` but is built on community DP + community tiers
- **Where:** `dp-team-value-math.md:9` (`confidence: "datamined"`).
- **Evidence:** Every row's denominator is a **DP cost**, which CLAUDE.md §3 names as the canonical *never-datamined* value ("DP cost is not in the game files — community-sourced via research/02 → enrichment; tag it community, never datamined"). The team comps, tier reads, and the entire ladder-arbitrage section come from `research/05` (community synthesis). Only the HP numerator is datamined — and even that is partly wrong (M2). The sibling `current-meta-tier-list.md:9` correctly uses `confidence: "community"` for the same class of content.
- **Why HIGH:** asserts game-file certainty for the wiki's headline community-value document; directly violates the prime confidence rule on the most-warned-about value (DP).
- **Fix:** set `confidence: "community"` (the body already honestly tags HP `[datamined]` and DP "from research/02," so only the frontmatter field is wrong).

> Spot-checks that PASSED: `defense-bible.md` tags vanish `~0.5 ki bar [community]`, Super Counter window `[community]`, frame timing `[community]` — all correct. `matchups`/`offense` tag throw damage, armor stagger, blast energy costs `[datamined]` consistently with `research/04` and `blast_index.json` (ult kiCost 50,000 / super 30,000 confirmed in `data-mined/blast_index.json`). The forbidden values (vanish cost, frame data, DP, Sparking duration) are community-tagged in the body text throughout. The H1/H2 problems are confined to **frontmatter metadata**, not body prose.

---

## 5. Research-brief cross-check vs `version.ts` + `system_constants.json`

**Headline numbers reconcile:** 208 roster slots (`research/01,02` ↔ `version.ts.rosterSlots`), DP budget 15 (`01/02/05` ↔ `dpBudget`), 26 ranks (`01/05` ↔ `rankCount`), Season 0 ends 2026-06-30 (`01/05` ↔ `rankedSeason`), energy anchors supers ~30k / ults 50k (`04` ↔ `blast_index.json`). **All 6 briefs have explicit `sources:` and `## Gaps / Unverified` sections** — provenance layer intact. Internal DP-distribution arithmetic in `research/02` is exact (base 182, SP1 26, combined 208 all sum correctly; base+SP1 reconciles per DP value). Three substantive divergences:

### [MEDIUM] M6 — `research/02` claims HP is NOT datamined (contradicts the datamine)
- **Where:** `research/02-roster-dp-dlc.md:398` ("Sparking! ZERO does **not** expose numeric health/stat values") and `:404,412` ("**any HP figures circulating are community estimates, not official**" / "**No official HP / numeric stats** exist for any character — only DP").
- **Evidence:** HP **is** datamined and is a stated sanity anchor: `system_constants.json` `hpDistribution` = **30 000 / 35 000 / 40 000 / 45 000** at counts **9 / 14 / 147 / 16** (CLAUDE.md §5, PLAN.md §5). `dp-team-value-math.md:22` and `beginner-numbers-guide.md:58` both correctly present HP as `[datamined]` from `characters.json`. So `research/02`'s "HP isn't real data" framing is **stale** (it predates / ignores the usmap dump that PLAN.md §3 marks "RESOLVED 2026-06-10") and is contradicted by the rest of the corpus that cites `research/02` as a source.
- **Fix:** update `research/02` §6 + §Gaps to note that per-fighter HP is now datamined (30/35/40/45k bands); DP remains the only community balancing number.

### [MEDIUM] M7 — `research/04` §1.1 labels durability-index values as "HP (datamined)" and omits the 45k band
- **Where:** `research/04-mechanics-frame-data.md:70-85` — HP table lists `41,238` (UI -Sign-), `36,364` (Goku GT), `31,819` (Goku Kid), and tops out at 40,000 (no 45,000 row); the brief itself notes these are the JP-wiki "耐久 (durability) = HP × defense correction" column.
- **Evidence:** the parsed datamine (`system_constants.json`) has **only four discrete HP values** 30/35/40/45k. The granular figures (41,238/36,364/31,819) are a third-party durability index, not the game's raw HP, and the **45,000 band (16 fighters) is entirely absent** from §1.1 even though the guides rely on it. `dp-team-value-math.md:56` echoes the artifact ("GT-era and kid bodies dip to **31k-36k**"), values that don't exist in the parsed bands.
- **Fix:** relabel §1.1 as "durability index (HP × defense)" distinct from raw HP, add the 45k band, and reconcile `dp-team-value-math.md:56` to the 30/35/40/45k bands.

### [LOW] L4 — Ranked "Season 1" confirmed vs unconfirmed (briefs disagree)
- **Where:** `research/01-overview-modes-economy.md:256` §Gaps ("whether ranked formally rebrands to Season 1 after June 30 2026 is **not yet announced**") vs `research/05:98` + `ranked-climbing-guide.md:34,89` (state **"Season 1 starts July 1 2026"** as fact; the guide is `confidence: "confirmed"`).
- **Evidence:** `research/05` and the guide cite a specific Bandai Namco EU notice (25 May 2026) for the season schedule + reset table; `research/01` lists it as an open gap. Either `research/01`'s gap is stale or the guide's "confirmed" overshoots. Compounded by **content-Season-2 vs ranked-Season-1 numbering** (no guide disambiguates the two season tracks; `version.ts.era` says "Season 1 complete" referring to *content*).
- **Fix:** reconcile across briefs (cite the 25-May notice in `research/01` or downgrade the guide); add a one-line "ranked seasons ≠ content/DLC seasons" note in `ranked-climbing-guide.md`.

---

## 6. Internal links — PASS

`a6_links.py` replicated `normalizeSlug` (lowercase + whitespace→hyphen) against the full cross-collection slug index (1,212 keys incl. glossary aliases) and scanned **143** wikilinks across the 12 guides: **0 unresolved**. The unblockable-skill table in `offense-and-pressure.md:71-77` (`[[god-bind]]`, `[[magic-bind]]`, `[[cry-of-rage]]`, `[[solar-flare]]`, `[[paralyze-beam]]`, …), all mechanic/game-mode links, and all cross-guide links resolve. No silent plain-text dead links.

---

## 7. Cross-guide contradictions & stale framing

- **M2 (already listed)** is the principal cross-guide contradiction: `matchups` (Gohan Beast 35,000 [datamined], **correct**) vs `dp-team-value-math` (40,000/null, **wrong**).
- **M1 (already listed):** Saibaman DP1 (`dp-team-value-math`, `current-meta-tier-list`, `research/05`) vs DP2 (`research/02`, character page, datamine).
- **Defense ↔ mechanics consistency: PASS.** `defense-bible.md` defensive costs match `research/04` §3 and the glossary/mechanics: Revenge Counter 2 stocks (`:30` ↔ research/04 §3.4 "2, some launch guides said 1"), Perception-vs-blast 2 stocks, Super Counter free/~2f, Afterimage 3 stocks/10s, vanish ≈½ bar [community]. `cheese-tech-status-board.md` and `matchups` agree with `meta.json` on which picks are nerfed/drifting (Roshi/Yajirobe/Recoome/Spopovich, UI Goku, Gogeta SSGSS, Kale Cry-of-Rage, giants). No defensive-options contradiction found.
- **[MEDIUM] M5 — `beginner-numbers-guide.md` §8 understates the HP-band count.** `:56` heading "HP tiers: 30k / 40k / 45k" + `:58` "**Three** datamined HP bands" + summary `:5` "(30k/40k/45k)" omit the distinct **35,000** band. The datamine has **four** bands (30/35/40/45k; counts 9/14/147/16). The table row `:62` does write "30,000-35,000," but framing it as three bands in a numbers-first beginner reference is inaccurate. *Fix:* "Four datamined HP bands: 30k / 35k / 40k / 45k."
- **Stale framing:** the only material stale-framing item is **M6** (`research/02`'s "HP not datamined"). No guide presents a pre-v2.2 state as current — patch hygiene is otherwise excellent (Game8 Nov-2024 list explicitly excluded).

---

## 8. The misleading `k` suffix (pervasive presentation error)

### [MEDIUM] M4 — model scores rendered as `NNN.Nk` (implies thousands; they are ~150-point scores)
- **Where:** `current-meta-tier-list.md:35-39,51-54` ("Vegito SSGSS (**152.8k**)", "Mr. Satan (**8.7k** — lowest score in game)"), `matchups-and-counterpicks.md:34,42,50,…` ("#1 Singles (**152.8k**)"), `meta-analysis-june-2026.md:27-28,79` ("**152.8k**", "#1 DP value (**33.9k**)").
- **Evidence:** `meta.json` scores are `152.8`, `8.7`, `33.9` — **sparkingzerometa model points (~8–153)**, which the guides themselves describe as "model points (higher = better), **not raw in-game damage**" (`current-meta-tier-list.md:23`). Appending `k` asserts ×1000 (152,800 / 8,700 / 33,900), which is internally contradictory and easily misread as HP (the wiki's HP values live in the same 30k–45k range) or damage. The `/meta` board renders them **correctly** without `k` (`meta-board.tsx:68` → `e.score.toFixed(1)` → "152.8"), so the guides are out of step with the board.
- **Fix:** drop the `k` across the three guides (write "152.8", "8.7", "33.9"), or label the column "model score" once and keep bare numbers.

---

## 9. Remaining LOW / NIT findings

- **[LOW] L1 — `gotenks-super-saiyan` Singles-S on board, no page `tier`.** `meta.json` Singles S-band lists "Gotenks, Super Saiyan"; `content/characters/gotenks-super-saiyan.md` (DP7, 45 000 HP) has no `tier` frontmatter. Expected page `A`. *Fix:* add `tier: "A"` via the enrichment overlay + regen.
- **[LOW] L2 — Super Buu variants band divergence + dead `unmatched`.** Guide/`research/05` place generic "Super Buu variants" in the A-band; `meta.json:280` `unmatched` labels them "B-tier Singles." Also `unmatched` is never rendered (`app/meta/page.tsx` omits the field). *Fix:* align the label, and either render or remove `unmatched`.
- **[LOW] L3 — DP-board picks show no page `tier`.** ~21 DP-ranked slugs (incl. DP-Z `spopovich`, `super-zarbon`, `vegeta-mini-super-saiyan-2/3`, `gohan-super-hero-super-saiyan`) have empty page `tier` because the field encodes Singles only; a fighter that is elite in DP but unranked in Singles looks "untiered" on its page. Schema/coverage note for Agents 1/10 (the page has one `tier` slot but the meta has two axes).
- **[LOW] L5 — DP team size 3 vs 5.** `version.ts.teamSizeMax = 5` and `research/01:122` say "up to 5"; `research/05:93,117` say the **ranked** queue is 3-character. Guides hedge "3-5"; `game-modes/dp-system.md:55-66` handles it best (presents both, tagged by source). Acknowledged conflict, not an error — but `version.ts` commits to 5 while the ranked-standard research says 3.
- **[LOW] L6 — blast base/boosted damage `[datamined]` is third-party, not locally verifiable.** `offense-and-pressure.md:118` tags base/boosted blast damage (e.g. Perfect Barrier 19,620→25,584) `[datamined]`; those values come from `research/04` §1.4's external sparkingzerometa datamine. This wiki's `data-mined/blast_index.json` exposes the **kiCost** (50,000 ult / 30,000 super — confirmed) and combatives, but not those base/boosted damage numbers, so the tag is third-party-datamined rather than verifiable in the local extract. Consistent research↔guide, so low risk; flagged for Agent 2.
- **[NIT] N1 — Roshi entry conflation.** `matchups-and-counterpicks.md:130-132` headers "Master Roshi / Roshi Max Power" then attributes the `31.2k` DP score (Max Power's, `meta.json` dp Z) and "30,000 HP" (base Roshi's) in adjacent lines. Both are DP2 so harmless, but it mixes the two forms' stats.
- **[NIT] N2 — economy numbers are community estimates (appropriately tagged).** `zeni-economy-guide.md` / `episode-battle-completion.md` Zeni rates (300k/run, ~3-4.5M/hr, 52 BGM × 90k = 4.68M, shop ~3M) are community/online-sourced and out of the datamine-numeric scope; they are correctly `confidence: "community"` and arithmetically self-consistent (e.g. 1,000,000/300,000=3.3×, 120,000×3=360,000, 300,000/15,000=20×). Character shop prices are **not** in `data-mined/shop.json` in a directly cross-checkable form, so they remain community-sourced; acceptable per the audit's "online may corroborate community values" rule.

---

## 10. Consolidated severity-ranked index

| ID | Sev | File:line | One-line |
|---|---|---|---|
| H1 | HIGH | `beginner-numbers-guide.md:9,11` | `sources` invents `vanishKiCost 2800` (the forbidden Sparking-drain mislabel) + page `confidence: datamined` while #1 number is community vanish cost |
| H2 | HIGH | `dp-team-value-math.md:9` | `confidence: "datamined"` on a guide built from community DP + community tiers (DP is the canonical never-datamined value) |
| M1 | MED | `dp-team-value-math.md:33,72` · `current-meta-tier-list.md:52` · `research/05:122` | Saibaman DP1→**DP2**; HP/DP 35,000→**17,500**; "Kale-centric" team is **16 DP (over the 15 cap)** |
| M2 | MED | `dp-team-value-math.md:25,50` | Gohan Beast "40,000/null" → datamined **35,000** (page) → HP/DP **3,889**; contradicts `matchups:99` |
| M3 | MED | `dp-team-value-math.md:68` · `research/05:125` | "~5 DP of cheap **DP7+** bodies" impossible (DP7+ ≥7); contradicts the guide's own auto-reflect gate |
| M4 | MED | `current-meta-tier-list.md`, `matchups…md`, `meta-analysis…md` | model scores written as `152.8k`/`8.7k`/`33.9k` — implies ×1000; they are ~150-pt scores (board renders them bare) |
| M5 | MED | `beginner-numbers-guide.md:5,56,58` | "**Three** datamined HP bands (30k/40k/45k)" — datamine has **four** (30/35/40/45k; 9/14/147/16) |
| M6 | MED | `research/02:398,404,412` | "no datamined HP / HP figures are community estimates" — contradicted by the datamine (HP is datamined) |
| M7 | MED | `research/04:70-85` | durability-index values (41,238/36,364/31,819) labeled "HP (datamined)"; 45k band omitted; echoed in `dp-team-value-math:56` |
| L1 | LOW | `content/characters/gotenks-super-saiyan.md` | Singles-S on board, page has no `tier` |
| L2 | LOW | `meta.json:280` · `app/meta/page.tsx` | Super Buu variants A vs B band; `unmatched` array never rendered |
| L3 | LOW | character schema / meta.json | ~21 DP-ranked picks show no page `tier` (page tier = Singles only) |
| L4 | LOW | `research/01:256` vs `research/05:98` / `ranked-climbing-guide.md:9,34` | ranked "Season 1" gap-vs-confirmed; ranked-season vs content-season numbering unclarified |
| L5 | LOW | `version.ts` vs `research/05:93` | DP team size 5 (version.ts) vs 3 (ranked research); guides hedge "3-5" |
| L6 | LOW | `offense-and-pressure.md:118` | blast base/boosted damage `[datamined]` is third-party (not in local `blast_index.json`) |
| N1 | NIT | `matchups-and-counterpicks.md:130-132` | base Roshi (30k HP) / Roshi Max Power (31.2 score) conflated under one header |
| N2 | NIT | `zeni-economy-guide.md`, `episode-battle-completion.md` | economy figures are community estimates (correctly tagged; shop prices not in local data) |

**Net:** the tier/meta/link layer is structurally sound (0 tier mismatches, 0 unresolved counters/links, strong patch-tagging, all 6 briefs carry sources+gaps). Fix the two `confidence: datamined` overclaims (H1, H2 — both metadata-only), the Saibaman-DP and Gohan-Beast-HP numeric errors (M1, M2 — M1 busts a worked team), the `k`-suffix (M4), and the two research-vs-datamine HP framings (M5, M6, M7).

*Probes: `audit/a6_probe.py` (tier/counter/DP-math), `audit/a6_links.py` (wikilinks) — both read-only, re-runnable.*



