# DRAGON BALL: Sparking! ZERO — Codex

**Numbers-first knowledge platform** for DB Sparking! ZERO (UE5.1.1 arena fighter): a human-readable wiki AND a datamined corpus. Content-as-data: **1,153 markdown files in `content/`** render to ~1,150 static pages via Next.js 16. Prime directive (the inverse of the sister XV2 codex): **every page leads with numbers** — datamined HP/ki costs, DP values, quantified patch deltas (old→new), frame data, shop price tables. Prose exists only to explain the numbers. Sibling project to `C:\vaults\xenoverse_2` (same stack); `PLAN.md` is the architecture bible, richer than `README.md`.

**Not a git repo** (no `.git/`, no `backups/`) — there is no revert safety net, so be deliberate about bulk regen/edits. Build output proves the corpus compiles green.

## Commands

- `npm run dev` — dev server at localhost:3000 (user usually has it running)
- `npm run build` — static build; **Zod-validates every page** (`lib/schemas.ts`), expect ~1,150 pages green
- **Patch refresh pipeline** (run in order after a game update):
  1. `dotnet run -c Release` in `tools/extractor` — re-dump game data to `data-mined/raw/`
  2. `python scripts/parse_data.py` — raw → `data-mined/*.json` reference tables
  3. `python scripts/gen_content.py` — JSON + enrichment → generated `content/` + `public/search-index.json`
  4. bump `lib/version.ts` `CURRENT_VERSION`, add the new `content/patches/` page, re-verify `content/guides/` meta pages, `npm run build`
- `python scripts/audit.py` / `audit_v3.py` / `audit_v4.py` — wiki QA (wikilink integrity, stale text, coverage; v4 checks the built HTML link graph + raw→render numeric consistency)
- `python scripts/fix_links.py` — repairs common broken `[[wikilinks]]` (blast super/ultimate suffix guessing)

## Answering game questions — lookup order

1. `**content/<collection>/<slug>.md`** — the authoritative layer. Frontmatter holds structured values (HP, ki/skill costs, damage, DP); body holds analysis. Grep here first; the answer usually exists already.
2. `**data-mined/*.json**` — parsed reference tables when you need to verify or go deeper:


| Question about…                                                                    | Look in                                                         |
| ---------------------------------------------------------------------------------- | --------------------------------------------------------------- |
| Per-fighter HP, ki economy, supers/ultimates, move damage, S1 skills, form changes | `characters.json`                                               |
| Named supers/ultimates + per-user costs/damage                                     | `blast_index.json`                                              |
| Blast Forte (S1) catalog + datamined descriptions                                  | `skills_catalog.json`                                           |
| Transformations/fusions/Potara: stock cost, HP recovery, cooldowns, partners       | `transformations.json` (208 edges)                              |
| Stage IDs/names, shop prices/unlocks, DLC packs                                    | `stages.json`, `shop.json`, `dlc.json`                          |
| Ranked tiers, Shenron wishes, global HP/ki/stock defaults                          | `ranks.json` (26 tiers), `wishes.json`, `system_constants.json` |
| Tier boards + counter-pick table (community synthesis)                             | `meta.json` (drives `/meta`)                                    |


1. `**data-mined/enrichment/*.json**` — manual/agent overlays merged at generation time (these survive regen): `characters.json` (DP, era, tier, classes, unlock), `sw_a.json`+`sw_b.json` (strengths/weaknesses/playstyle/how-to-fight for all 208 slots), `skills.json`+`skill_effects.json`, `stages.json`.
2. `**data-mined/raw/**` — CUE4Parse extract: `masterdata/` (CharacterData, BlastForte, BulletSetting, Combatives, Numeric, …), `locres_en.json`, `stringtables.json`. Only when reference tables don't cover it. Parser: `scripts/parse_data.py`.
3. **Game install**: `D:\SteamLibrary\steamapps\common\DRAGON BALL Sparking! ZERO` (UE5.1.1 IoStore paks; extractor at `tools/extractor`, vendored `tools/CUE4Parse`, `tools/Mappings_fresh.usmap`). Last resort.

### Datamine rules (violating these caused real bugs)

- **Sparking!-mode gauge drain = 2,800/s uniform. This is NOT the vanish cost.** The launch-usmap mislabeled `SparkingModeGaugeDecreaseSpeed` as a vanish/Z-Counter cost — that cost is **not in the parameter tables at all** (community ≈ ½ bar). Never cite vanish cost as `datamined`.
- **DP cost is not in the game files** — community-sourced via `research/02` → `enrichment/characters.json`. Tag it `community`, never `datamined`.
- **Per-move damage is only partially datamined.** Overrides exist in `BulletSetting/BulletParam_<cid>_act*` (606 incl. 47 ultimates: Power / Shave=chip / BeamPower / BeamShave / multi-hit / ExpendEnergy) and `Combatives/<cid>` (1,761 Power entries + ArmorBreakLevel / EnergyGain / HitStop / Super-Counter-avoidable flags). `BulletSetting/Common` = generic ki-blast defaults (200 dmg / 40 chip / 2,000 ki). **Moves without an override inherit blueprint class defaults — those still need community labs**, so don't present them as datamined.
- Energy units: **10,000 = 1 ki bar**; supers ~30,000; ultimates ~50,000. HP tiers: 30,000 / 35,000 / 40,000 / 45,000 (9 / 14 / 147 / 16 fighters); **10,000 HP per bar**. (Sanity anchors — see `PLAN.md` §5.)
- `CharacterData_*` carries per-edge `HpRecovery` — the May 26 2026 heal-removal shipped, so **most transforms are now `0`, but ~27/164 still recover 5k–10k** (check the edge in `transformations.json`; don't assume `0`). `BlastForte1/2_*` = per-character S1 mapping + `ExpendBlastStock` + unblockable flags.

## Generated vs curated collections

**Generated** (owned by `scripts/gen_content.py` — **never hand-edit these files**; edit the `enrichment/` overlays and regen):


| Collection | files | Collection      | files |
| ---------- | ----- | --------------- | ----- |
| characters | 245¹  | transformations | 164   |
| blasts     | 453   | stages          | 27    |
| skills     | 146   | shop            | 7     |


**Curated** (hand/agent-written markdown — edit directly, one file at a time):


| Collection | files | Collection      | files |
| ---------- | ----- | --------------- | ----- |
| mechanics  | 22    | episode-battles | 8     |
| patches    | 18    | guides          | 12    |
| dlc        | 9     | glossary        | 30    |
| game-modes | 12    |                 |       |


¹ **245 character pages but only 208 *playable* roster slots** — the rest are system/NPC entries pulled straight from `CharacterData` (e.g. `status`, `enemy`, `ally`, `you`, `narration`, `shenron`, `porunga`, `not-used`). The `playable` boolean separates them. Guides (12) are the strategy layer (`defense-bible`, `offense-and-pressure`, `matchups-and-counterpicks`, `current-meta-tier-list`, `dp-team-value-math`, the flagships). `research/01..06` are the numbers-first provenance briefs cited in `sources` arrays for everything not datamined.

## Site architecture

- `lib/schemas.ts` — one Zod schema per collection. Shared meta spread into every fact page: `asOfVersion`, `asOfDate`, `lastVerified`, `sources`, and `**confidence` (`confirmed|datamined|community|unverified`, default `community`) — any other value crashes the build.** Many other closed enums are build-crash hazards too: move `type` (`rush|smash|throw|blast1|blast2|ultimate|evasive|special`), `tier`, `category` per collection, and `numericValue.tag` which is a *different* set (`official|datamined|community`).
- `lib/content.ts` — `loadCollection()` (gray-matter + `schema.parse`, throws an error **naming the offending file** on validation failure), `getX()`/`getX(slug)` per collection, and `**getSlugIndex()`**: a memoized cross-collection `slug → {href,label}` map for resolving `[[wikilinks]]`. **First-wins on slug collisions**, in this priority order: characters → skills → blasts → transformations → mechanics → game-modes → episode-battles → patches → dlc → guides → stages → glossary (glossary terms + their aliases resolve to `/glossary#slug`). Characters outrank everything.
- `lib/markdown.ts` — `renderMarkdown(md, {excludeHref})`: (1) converts `[[target]]`/`[[target|label]]` to links via `normalizeSlug` against the slug index — **unknown targets render as plain text (no dead links)**; (2) `autolink` wraps plain-text mentions of known page labels (length ≥ 4, not in STOP `{base, story, standard}`, no `→`), longest-match-first, first mention per name, while protecting code fences/spans, existing links/images, headings, and table-separator rows; then `marked.parse`. Content is first-party/trusted → **not sanitized**. ⚠️ This file is valid UTF-8 but trips "binary" detection in some file-readers — read it via the shell if the Read tool refuses.
- `lib/linkify.tsx` — `getNameIndex()` + `linkifyText()` auto-link known display names inside frontmatter-rendered strings (summaries, strengths, counter lists) at render time.
- `lib/formulas.ts` — `fmtNum`, `fmtPct`, `pctChange`, `dmgPerKi`, `dmgPerDp`, `hpPerDp` (the core team-builder value metrics). Use these rather than re-deriving.
- `lib/version.ts` — `CURRENT_VERSION` (patch, roster slots, DP budget, ranked season, rank count, nextContent), `STALE_AFTER_DAYS = 240`, `isStale()`. The UI flags any page whose `lastVerified` is older than the window.
- `app/` — 13 collections (listing + `[slug]` detail each) plus utility pages: `/` (guide-first home), `/meta` (visual tier board from `meta.json`), `/dna`, `/classes`, `/compare`, `/stats`. Layout has a grouped two-row nav (data vs play) and a ⌘K `SearchButton` over `public/search-index.json`.
- `components/` — `roster-table`, `blasts-table`, `skills-table` (filter/sort), `sortable-tables` (click-to-sort static tables), `meta-board`, `dna-explorer`, `compare`, `search`.

## Content & linking conventions

1. **Numbers-first.** Lead every page with the quantitative data; prose explains it. Don't write a paragraph where a stat table will do.
2. **Never hand-edit generated collections.** Characters/blasts/skills/transformations/stages/shop come from `gen_content.py` — your edit will be wiped on the next regen. Fix the datamine parse or the `enrichment/*.json` overlay instead.
3. **Cite confidence honestly.** `datamined` only for values straight from game files. DP, vanish/Z-Counter cost, and non-override move damage are `community`. Disputed values: present both camps. Generated fact pages carry one page-level `confidence` for their datamined stat block and flag the community DP overlay in `sources` (research/02) — never relabel DP itself as datamined (transformation bodies state this inline). A per-field provenance model is the deeper fix if the single enum ever feels dishonest.
4. **Wikilinks** in body text use `[[slug]]` or `[[slug|Label]]`. **In table cells, escape the pipe as `\|`** before the label (the generator emits this) so it doesn't break the GFM table. Unknown targets degrade to plain text; run `python scripts/fix_links.py` + `audit.py` after large content passes.
5. **One file at a time** for curated content; Read before Edit/Write. No bulk regex rewrites of prose (there's no git to revert).
6. **Meta/tier claims must name their patch.** A tier list older than `CURRENT_VERSION` is history, not current — label it.

## Environment notes

- Windows; **PowerShell** shell. `**$` variables get stripped/mangled** when one-liners are passed through (confirmed: `$_`, `$b` were corrupted into broken syntax — same class of hook/dumb-terminal bug the sister project warns about). Avoid `$`-heavy or backslash-regex PowerShell one-liners; for anything non-trivial, **write a script to `scripts/` and run it**. Prefer the dedicated Glob/Grep/Read tools over shell `dir`/`type` for file ops.
- Python scripts and the C# extractor have **hardcoded `C:\vaults\sparking_zero` and Steam paths** — they assume this exact layout.
- `tools/`: `extractor/` (.NET, CUE4Parse, AES key + Steam path in `Program.cs`), vendored `CUE4Parse/` (built from source for usmap v4), `ue4ss/`, `Mappings_fresh.usmap` (current-patch UE4SS dump), `oo2core_9_win64.dll` (Oodle). After a patch, re-dump the usmap if new DLC assets fail to parse.

## Status / roadmap

- Datamine, content generation (all 13 collections), enrichment overlays, strategy guides, and the meta/UX layer are **complete and building green** at patch `**v2.2 (2026-05-26 update)`** (208 roster slots, DP budget 15, Season 0 ranked ending 2026-06-30).
- **Next: Season 2 "Super Limit-Breaking NEO" (Summer 2026)** — 30+ fighters and two new mechanics (Chain Blast, Sparking! Boost) → full re-verify pass (re-dump usmap, refresh `meta.json` + tier guides, new mechanics pages).
- Remaining numeric gap: non-override (class-default) move damage — the one layer still needing community labs.

