# Audit Agent 5 — Patches · DLC · Episode-Battles · Game-Modes

**Date:** 2026-06-15 · **Scope:** `content/patches` (18) · `content/dlc` (9) · `content/episode-battles` (8) · `content/game-modes` (12) = **47 files, all read**.
**Source of truth:** `data-mined/dlc.json`, `data-mined/ranks.json`, `data-mined/characters.json`, `data-mined/enrichment/characters.json`, `content/characters/*` (245 pages), `research/01,03,06`. Online sources NOT trusted for numbers.
**Probes (read-only, under `audit/`):** `a5_probe.py` (all countable checks), `a5_dp_check.py` (DLC DP↔enrichment via charId), `a5_slug_check.py` (cross-collection slug collisions). Cross-validated against `scripts/audit_v3.py` (reports CLEAN; its checks are narrower — see §"Verifying audit_v3").

## Severity summary

| Severity | Count |
|---|---|
| BLOCKER | 0 |
| HIGH | 0 |
| MEDIUM | 3 |
| LOW | 8 |
| NIT | 6 |

**Headline:** The four collections are in very good shape. Every countable invariant the task asked for **passes**: patch `order` is unique *and* chronological (sort-by-order == sort-by-date), all `type`/`category` enums valid, all 8 episode `battleCount` == `len(battles[])`, all 196 episode opponents resolve to real characters, all 34 shipped-DLC character DP values exactly match `enrichment/characters.json`, and Season-2 NEO is correctly flagged `upcoming` and kept out of the 208 roster. The findings are confidence-labeling and cross-page-consistency issues, not wrong data.

---

## MEDIUM

### M1 — DLC pages tag community DP under a "datamined" banner (violates the explicit DP-provenance rule)
**Files:** `content/dlc/preorder-pack.md:37,46,53` · `hero-of-justice-pack.md:50,61` · `daima-character-pack-1.md:43,53` · `daima-character-pack-2.md:35,44` · `shallot.md:19,35`

**Evidence:** Five DLC pages carry page-level `confidence: "datamined"` and place per-character **DP** columns directly under captions such as `## Characters (x11, datamined — DLC_009)` (`hero-of-justice-pack.md:61`) and `### Characters unlocked early (x6, datamined)` (`preorder-pack.md:53`). But `CLAUDE.md` and `audit/README.md` are explicit: *"DP cost is not in the game files — community-sourced via research/02 → enrichment. Tag it `community`, never `datamined`."* `dlc.json` contains only `characterIds`/`characters`/`summonTickets` — **no DP**. So the roster *list* is genuinely datamined, but the DP (and USD price) are community.

**Verification:** the DP **values are correct** — `a5_dp_check.py` confirms all 34 shipped-DLC DP values equal `enrichment/characters.json` dp via charId (0 mismatches). This is purely a provenance-label problem, but it is exactly the class the codex flags as having "caused real bugs."

**Fix:** Either set these pages' `confidence` to `community` (their headline DP + price are community; only the roster list is datamined), or keep `datamined` for the pack contents and explicitly annotate the DP column as community (e.g. caption "DP = community / research-02"). The `sources:` arrays already cite `research/02` for DP — make the inline framing match.

### M2 — Episode-Battle mode says "12 major routes" but the collection enumerates 13 Sparking Episodes
**Files:** `content/game-modes/episode-battle.md:18-19,64-65` vs the 8 campaign pages' `sparkingEpisodes`.

**Evidence:** `episode-battle.md` lists `Major What-If / Sparking Episode routes = 12` (tag community) and body "12 major What-If / 'Sparking Episode' routes." But the campaign pages sum to **13**: Goku 3 (`episode-goku.md:7`), Vegeta 2, Gohan 1, Piccolo 1, Frieza 1, Goku Black 1, Future Trunks 3 (`episode-future-trunks.md:7`), Jiren 1 → **3+2+1+1+1+1+3+1 = 13**. `research/06` §1.2 is the origin of the error: its prose says "12 major routes" while its own table lists 13 rows (Goku ×3, Vegeta ×2, Gohan, Piccolo, Future Trunks ×3, Frieza, Goku Black, Jiren). The wiki inherited the "12" on the mode page but correctly enumerated 13 across campaigns.

**Fix:** Change `episode-battle.md` to **13** major routes (matches the campaign collection + the research *table*). Optionally note research/06's prose off-by-one.

### M3 — "Instant Sparking 3→4" is double-attributed to two different patches as a *new* change
**Files:** `content/patches/v2025-01-20.md:18,41-44` and `content/patches/v2025-12-15.md:18,20-24,69`

**Evidence:** `v2025-01-20.md` records *"[official] Instant Sparking: skill-count cost raised 3 → 4"* with a `measured` old `3` → new `4` (citing research/04 §5.1). `v2025-12-15.md` *also* records instant-Sparking `3 stocks → 4 stocks` and its body states *"The instant-Sparking 3→4 ... are the **genuinely new** community-attributed items here."* These conflict: the same balance change cannot be both an official Jan-2025 change and a "genuinely new" Dec-2025 change. The root cause is an unreconciled research conflict — `research/04` (lines 58/249/264/282) dates it **Jan 20 2025 [official]**, while `research/05` (lines 80/149/206) dates it **Dec 15 2025 [community]** and admits it "come[s] from a community patch-breakdown video, not the official notes." The Dec-2025 page transparently downgrades the *AIS* and *False Courage* restatements as "community memory" of the Dec-2024 patch, but it fails to do the same for instant-Sparking vs the Jan-2025 page.

**Fix:** Pick the better-attested date (research/04 = Jan 20 2025, the only [official]-tagged source) as the real change; reframe the Dec-2025 entry as a community restatement and cross-link `v2025-01-20`. Also reconsider the `[official]` prefix on `v2025-01-20.md:18` — research/03 (the official enumeration) does not list this change and the value is admittedly community-attested.

---

## LOW

### L1 — `dp-system` slug exists in BOTH `mechanics` and `game-modes` (game-modes page is wikilink-shadowed)
`content/mechanics/dp-system.md:2` and `content/game-modes/dp-system.md:2` both declare `slug: "dp-system"`. Per `lib/content.ts` first-wins order (mechanics > game-modes), **every `[[dp-system]]` wikilink resolves to the mechanics page** — including the links from `ranked-match.md`, the DLC pages, and `dp-system.md` (game-mode) itself — so the game-modes DP page is unreachable by wikilink and shares a search-index slug. This is **whitelisted as by-design** in `audit_v3.py` `OK_PAIRS {("game-modes","mechanics")}`, and the two pages *are* mutually consistent (both: budget 15, community-tagged; the game-mode page honestly presents the 5-vs-3 team-size source conflict). Flagging only the consequence. **Fix (optional):** give the mode page a distinct slug (e.g. `dp-battle`) so both are linkable, or keep one canonical page.

### L2 — `shallot` DLC slug collides with the `shallot` character (DLC page wikilink-shadowed)
`content/dlc/shallot.md:2` `slug: "shallot"` collides with `content/characters/shallot.md`. Characters outrank dlc, so `[[shallot]]` always resolves to the character (probably intended), leaving the DLC page wikilink-unreachable. Whitelisted in `audit_v3.py` `OK_PAIRS {("characters","dlc")}`. Note: the other character-bearing packs avoid this by using pack-name slugs (`hero-of-justice-pack`, `daima-character-pack-1`…). **Fix (optional):** rename to `shallot-dlc`/`shallot-pack`.

### L3 — DLC release dates disagree with the patches collection (same events, different days)
- DAIMA Pack 2: `content/dlc/daima-character-pack-2.md:4` `releaseDate: "2025-09-24"` and `season-pass-1.md:39` "Sep 24, 2025" vs `content/patches/dlc3-2025-09-25.md:4` `"2025-09-25"` (full release; EA Sep 21).
- Shallot: `content/dlc/shallot.md:5` `"2025-06-26"` vs `content/patches/shallot-2025-06-27.md:5` `"2025-06-27"`.

Each page sources a different brief (research/01 says Sep 24 / research/02 says Jun 26; research/03 says Sep 25 / Jun 27) and footnotes the conflict, but the two collections pick different canonical dates for the same drop. **Fix:** choose one date per event across both collections (recommend the research/03 patch dates Sep 25 / Jun 27, which match the official EA→release pattern), or add a shared "date conflict" note pointing both ways.

### L4 — `super-limit-breaking-neo`: body claims "27 catalogued" / slots "#209-235" (27) but lists only 25
`content/dlc/super-limit-breaking-neo.md:36` adds `"30+ new playable characters (27 revealed / catalogued so far)"` and body `:62` "27 catalogued so far (roster slots #209–235)" (235−209+1 = 27), but the `characters:` array (`:8-34`) has **25** entries. **Fix:** add the 2 missing teases, or change the prose to "25 catalogued (#209-233)". (This page is otherwise correctly `upcoming: true`, see PASS notes.)

### L5 — `episode-gohan` "The Strongest Warrior" stages say "Gohan Black" (looks like a "Goku Black" typo)
`content/episode-gohan.md:96` id `s4` name `"Gohan Black's True Identity (The Strongest Warrior route)"` (vs `Zamasu`) and `:101` id `s5` name `"Gohan Black and Gohan (...)"` (vs `Goku Black`). The villain is **Goku Black**; there is no "Gohan Black." These mirror Goku's stages `Goku Black's True Identity` (`episode-goku.md:136`) and appear to be a Goku→Gohan substitution error in the stage titles. The `vs[]` opponent data is correct. **Fix:** correct the two stage names to "Goku Black…" (verify against Game8's Gohan What-If table).

### L6 — `ranked-match` asserts "Season 1 starts July 1 2026" as `official`, which research/01 still flags as unconfirmed
`content/game-modes/ranked-match.md:24-25` lists `Season 1 start = July 1 2026, 08:00 UTC (runs ~3 months)` tagged **official**. `research/05` supports this (lines 6/98), and the page cites the 25-May-2026 EU ranked notice; but `research/01` §Gaps #9 explicitly says *"whether ranked formally rebrands to Season 1 after June 30, 2026 is not yet announced."* This is consistent with `version.ts` (which only documents the current "Season 0 — ends 2026-06-30") but represents an **unreconciled cross-brief tension** presented at `official` confidence. **Fix:** confirm the 25-May notice actually names "Season 1 / July 1," or downgrade the Season-1 line to `community`/upcoming and reconcile research/01 §Gaps #9.

### L7 — DLC coverage gap vs `dlc.json`: Victory Pack & Martial Arts Pack have no page
`dlc.json` defines `DLC_005` "Victory Pack" and `DLC_006` "Martial Arts Pack" (the latter grants **early-unlock Bardock, Gohan (Future), Gohan (Future) SS + the Super Sparking! item**, dated Oct 9 2024 $0.99 per research/06 §4). Neither has a `content/dlc/*.md` page. The collection covers 7 of the consumer packs well; these two character-relevant pre-order-tier DLCs are omitted. (`DLC_002`/`DLC_007` summon tickets are reasonably folded into season-pass/encyclopedia; `DLC_900` is internal.) **Fix:** add stub pages for Victory Pack and Martial Arts Pack (or note in a DLC index why they're excluded), for parity with the datamined source of truth.

### L8 — `shallot` DLC is `type: "free"` yet `priceUSD: 1.99`
`content/dlc/shallot.md:6-7` sets `type: "free"` and `priceUSD: 1.99`. The body explains it (free with Season Pass / Deluxe / Ultimate; ~$1.99 standalone), but `type: free` + a non-null price is internally contradictory at the data level. **Fix:** pick the dominant distribution (it is bundled-free for Season-Pass owners → `free` with `priceUSD: null`, or `paid`/`preorder` with 1.99), and keep the nuance in the body.

---

## NIT

- **N1** `content/game-modes/dp-system.md:9-11` tags `DP scale (per character) "1–10"` as `official`. The per-character DP scale is community (DP isn't in game files); the *budget/auto-reflect/selectable-totals* official tags on the same page are fine (patch-note facts). Minor: retag the 1–10 scale `community`. (Also a benign tag mismatch: `mechanics/dp-system.md:8` tags "DP budget 15" `official` while `game-modes/dp-system.md` tags the Versus 15-budget `community` — both agree on the value 15.)
- **N2** DLC `order` is not chronological (`season-pass-1.md` order 7 = 2024-10-10; `anime-music-packs.md` order 9 = 2024-10-07, the earliest date). This is an intentional curated display order (character packs 1-6 in release order, then bundle/upcoming/music) and the schema/task do **not** require DLC `order` to track date (only patches do). Informational only.
- **N3** `content/episode-goku-black.md` `battleCount: 13` (`:6`) includes 4 cross-saga "reference" stages (`alt-into-third-future`, `alt-third-future-2`, `alt-rose-mirror`, `alt-zen-oh`, `:75-104`) that are Goku-saga mirrors "documented for cross-reference," padding Goku Black's own short campaign. `battleCount` correctly equals `len(battles[])`, and the page is transparent, but the count mixes own-campaign stages with cross-references.
- **N4** Episode opponents name the same Cell-Games boss two ways: `"Cell Perfect Form"` (`episode-goku.md:79`, → `cell-perfect-form` / charId 0162_00, DP6) vs `"Perfect Cell"` (`:86,94`, → `perfect-cell` / charId 0162_01, DP7). Both resolve to real (distinct) datamined entries, so nothing is broken, but the narrative boss is referenced inconsistently across stages.
- **N5** `ultimate-upgrade-pack.md` is `type: "paid"` with `priceUSD: null` (edition-exclusive — defensible); `anime-music-packs.md` carries one `priceUSD: 14.99` for two packs ($14.99 *each*, clarified in body). Minor data-shape quirks.
- **N6** Six episode battles have empty `vs: []` story/no-combat segments counted in `battleCount` (`episode-frieza` f1 & alt-king-cold-stage; `episode-future-trunks` 5 & alt-shining-hope-scene; `episode-goku-black` alt-zen-oh; `episode-piccolo` m4). By design (route stages), noted for completeness.

---

## What PASSES (verified clean)

**PATCHES (checks 1-4)**
- **Order unique & chronological:** 18 patches, 0 duplicate `order`s; `order` == YYYYMMDD for every page; sort-by-order **==** sort-by-date (no out-of-chronology). This *verifies and extends* `audit_v3.py`'s dup-order check (which only tests uniqueness) — clean.
- **Type enum:** all ∈ {launch, major, balance, content, hotfix}. Distribution: launch 1, hotfix 1, balance 5, content 5, major 4 (Apr/Jun/Sep 2025 + May 2026).
- **Measured deltas:** 66 `measured` entries, all have `target`+`metric`; all directionally sane (nerfs raise cost / lower duration/damage; buffs the reverse) and consistent with note text (e.g. AIS 15s→10s, Perception 1→2, win-streak ×1.2/×1.4/×1.8/×2.0, reset Z→B1/S→B3/A→B5/B→C5/C→D5/D→D5 — all match research/03 verbatim).
- **Dates:** none after today (2026-06-15); latest = `v2026-05-26` (order 20260526). **It documents the heal-removal** ("transform characters NO LONGER heal on transform; instead gain a permanent ATK buff," `:9,112`), aligning with `CLAUDE.md`'s `HpRecovery→0` / `CURRENT_VERSION v2.2 (2026-05-26)`.
- **Confidence tags:** balance patches `confirmed`; the two community-contested passes (`hotfix-2024-10`, `v2025-12-15`) correctly `community` and honest about contested attributions. **No patch uses a `datamined` tag** (so check #4 — no fake datamined claims — passes).

**DLC (checks 5-6)**
- 9 pages; `order` unique (1-9); `type` ∈ {paid, free, preorder, season-pass}; `upcoming` boolean.
- **All 34 shipped-DLC character slugs resolve** to real character pages, and **all 34 DP values exactly match `enrichment/characters.json`** via charId (`a5_dp_check.py`: 0 mismatches). Names cross-check vs `dlc.json` (forms expanded from the base `characterIds`; counts 11/8(+1 listed)/6/1 → roster math 182+26 = 208).
- **Season 2 "Super Limit-Breaking NEO" is correctly handled:** `upcoming: true`, `confidence: community`, placeholder `releaseDate: 2026-07-01` explicitly labelled "ANNOUNCED but NOT YET RELEASED," fighters assigned hypothetical slots #209-235 with DP unpublished. Its fighters are **not** in the live 208 (Champa/Supreme Kai resolve only to `playable: false` story-NPC pages; the rest have no page). No place treats S2 content as current.

**EPISODE-BATTLES (check 7)**
- 8 campaigns; `order` unique (1-8). **`battleCount` == `len(battles[])` for all 8** (28/25/22/17/17/13/17/11 = 150 battle entries) — verifies & extends `audit_v3.py`'s check.
- **All 196 `vs[]` opponent references resolve to real characters** (130 exact name match + 66 via punctuation/spacing normalization, e.g. "Goku (Z - Mid) Super Saiyan" → `goku-z-mid-super-saiyan`); 0 unresolved.
- `sparkingEpisodes` counts sane (3/2/1/1/1/1/3/1 = 13, matching research/06's route *table*). `altRoute`/`altResult` are perfectly paired (0 asymmetric battles) and present on every branch/finale.

**GAME-MODES (check 8)**
- 12 modes; all `category` ∈ {offline, online, pve, pvp, hub, training}.
- `game-modes/dp-system.md` is **consistent** with `mechanics/dp-system.md` (both budget 15, community-tagged; mode page honestly documents the 5-vs-3 team-size source conflict).
- `ranked-match.md`: **26 ranks D5→Z** matches `ranks.json` (26 tiers) and `version.ts` (`rankCount: 26`); **Season 0 ends 2026-06-30** matches `version.ts`; reset table matches research/03/05.
- `world-tournament.md` (toggles, unlocks) and `shop.md` are consistent with research/01,06; **`shop` mode slug does NOT collide** with the generated `shop` collection (which uses `equippowerup`, `character`, etc.). `episode-battle` mode slug does not collide with the `episode-battles` collection. `values[]` tags are largely honest (one quibble in N1).

## Coverage stats
| Collection | Files | Read | Probed |
|---|---|---|---|
| patches | 18 | 18 | order/type/date/measured/confidence/datamined-scan |
| dlc | 9 | 9 | order/type/price/upcoming + 34 char slug+DP↔enrichment |
| episode-battles | 8 | 8 | battleCount(150)/order/196 opponents/sparkingEpisodes/altRoute-altResult |
| game-modes | 12 | 12 | category/slug-collisions/DP+ranked cross-consistency |
| **Total** | **47** | **47** | + `audit_v3.py` cross-validated (CLEAN) |

## Verifying audit_v3
`audit_v3.py` runs and reports **CLEAN**; its relevant checks (patch `order` uniqueness §G, episode `battleCount` §F) confirm what `a5_probe.py` found independently. Its slug-collision check (§A) reports "18 total, 0 unexpected" because `dp-system` and `shallot` are in its `OK_PAIRS` whitelist (hence L1/L2 are LOW/by-design, not breakages). audit_v3 does **not** check: patch chronological monotonicity, type enums, measured directional sanity, DLC DP↔enrichment, episode opponent resolution, game-mode categories, or DP-confidence honesty — all added here.
