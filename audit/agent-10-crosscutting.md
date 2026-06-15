# Agent 10 — Cross-Cutting Integrity Audit

**Scope:** frontmatter / schema conformance at scale, confidence-honesty counting, numeric sanity,
date/version consistency, duplicates, and rendered-output QA across the built HTML.
**Date:** 2026-06-15 · **Corpus:** 1,153 `content/**/*.md` + 1,144 built `*.html`
**Method:** read-only Python probes (`audit/a10_*.py`) for **full coverage** (not spot checks).
No content/data/code modified.

| Probe | What it covers |
|---|---|
| `audit/a10_frontmatter.py` (+ `a10_frontmatter.json`) | parses every page's YAML; checks 1,2,3,4,5,7,8 |
| `audit/a10_numeric_detail.py` | super/ult ki distributions, HP-count split, name-dupe verification |
| `audit/a10_html.py` (+ `a10_html.json`) | scans all 1,144 HTML for leaked artifacts |
| `audit/a10_html_context.py` | classifies the `>null<` + empty-`<td>` cells |
| `audit/a10_addendum.py` | DLC DP-under-datamined, null-HP prose, grand tally |

## Severity summary

| Severity | Count | Headline |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 1 | **376 pages stamped `confidence: datamined` carry community-only DP** (208 chars + 163 transforms + 5 DLC); 163 transform bodies literally claim "all numbers datamined" |
| MEDIUM | 1 | 6 glossary pages stamped `datamined` cite **only research briefs** (no game-file source) |
| LOW | 4 | HP-count drift vs datamine snapshot; 20 playable chars with null HP; duplicate stage `variants` entry; one skill missing `userCount` |
| NIT | 1 | "null-HP" prose in 11 character summaries reads like a leaked value |
| **VERIFIED CLEAN** | — | **0 enum violations · 0 invalid HP/DP/ki · 0 stale/future/malformed dates · 0 duplicate slugs · 0 leaked `[[`/`\|`/`[object Object]`/`>undefined<`/unformatted numbers** |

The big picture: the corpus is **mechanically very healthy** — it builds green, every closed enum is in
range, every date is sane, every number is in a plausible band, and the rendered HTML is essentially
artifact-free. The one systemic problem is **provenance honesty**: the single-value `confidence` enum
over-claims `datamined` on ~⅓ of pages because those pages also surface a community DP value.

---

# 1. CONFIDENCE HONESTY AT SCALE (flagship)

Every one of the 1,153 pages carries an **explicit** `confidence` value (0 rely on the schema default).
Distribution per collection:

| Collection | datamined | community | confirmed | unverified | total |
|---|--:|--:|--:|--:|--:|
| blasts | **453** | 0 | 0 | 0 | 453 |
| characters | **245** | 0 | 0 | 0 | 245 |
| transformations | **164** | 0 | 0 | 0 | 164 |
| skills | 13 | 133 | 0 | 0 | 146 |
| glossary | 7 | 7 | 16 | 0 | 30 |
| stages | **27** | 0 | 0 | 0 | 27 |
| mechanics | 1 | 21 | 0 | 0 | 22 |
| patches | 0 | 2 | 16 | 0 | 18 |
| game-modes | 0 | 10 | 2 | 0 | 12 |
| guides | 2 | 9 | 1 | 0 | 12 |
| dlc | 7 | 1 | 1 | 0 | 9 |
| episode-battles | 0 | 8 | 0 | 0 | 8 |
| shop | 7 | 0 | 0 | 0 | 7 |
| **TOTAL** | **925** | 191 | 36 | 0 | 1,153 |

**925 pages (80% of corpus) are stamped `datamined`.** Per `CLAUDE.md` §"Datamine rules" and
§"Cite confidence honestly", `datamined` is reserved for values pulled straight from game files; **DP,
vanish/Z-Counter cost, and non-override move damage are explicitly community.** The pages below claim
`datamined` at the page level while prominently displaying a community DP value.

### Grand tally — datamined-stamped pages carrying a community DP value

| Source of the community DP | datamined pages w/ DP | DP data points |
|---|--:|--:|
| `characters` — top-level `dp:` | **208** | 208 |
| `transformations` — `dpFrom:`/`dpTo:` | **163 / 164** | 326 |
| `dlc` — per-character `dp:` in `characters[]` | **5 / 7** | 34 |
| **TOTAL** | **376 pages** | **568 values** |

### 1a. Characters — `dp` under a `datamined` stamp (208/208 playable)

All 208 playable character pages set `confidence: "datamined"` yet carry `dp:` (community). Examples:

```7:7:content/characters/goku-super.md
dp: 5
```
```99:105:content/characters/goku-super.md
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
  - "research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"
```

More: `content/characters/android-13.md:7` (dp=5, confidence@L77) · `android-17-super.md:7` (dp=6,
@L78) · `anilaza.md:7` (dp=8, @L72) · `babidi.md:7` (dp=3, @L75) … (full list in `a10_frontmatter.json`).

> **Fairness note:** on *character* pages the `sources` array **does** disclose the DP origin
> (`research/02-roster-dp-dlc.md (Game8/Fandom DP tables)`), so the page is honest at the source level —
> the single coarse `confidence: datamined` enum is the weak link, not the sourcing. The rendered page
> even labels the chip "Datamined" next to a "DP cost: 5" tile sourced to Game8/Fandom.

### 1b. Transformations — `dpFrom`/`dpTo` under a `datamined` stamp (163/164) — *sharpest offender*

163 of 164 transformation pages carry `dpFrom`/`dpTo` (community) under `confidence: "datamined"`,
and — unlike characters — they do **not** cite a DP source **and the body prose literally asserts every
number is datamined**:

```7:18:content/transformations/jiren-to-jiren-full-power.md
cost: 2
kind: "transform"
hpRule: "HP recovery on change: 10,000 · cooldown 5s"
dpFrom: 8
dpTo: 9
summary: "Transformation: costs 2 skill stock(s)"
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "datamined"
sources:
  - "game files (CUE4Parse extract, Steam build 22517964, 2026-06-05)"
```
```21:21:content/transformations/jiren-to-jiren-full-power.md
**Jiren → Jiren, Full Power** (in-battle transformation) — all numbers datamined from CharacterData.
```

`dpFrom: 8`/`dpTo: 9` are **community** values, but the only `source` is the CUE4Parse extract and the
body states "all numbers datamined from CharacterData." This is a direct provenance falsehood replicated
across **163 pages** (`dpFrom`/`dpTo` at L10–L11; body claim around L21; sample slugs:
`android-13-to-fusion-android-13`, `broly-super-to-broly-super-super-saiyan`,
`broly-z-to-broly-z-legendary-super-saiyan`, … — full list in `a10_frontmatter.json`).
The lone exception with no DP: `third-eye-gomah-to-giant-gomah` (giants have no DP).

### 1c. DLC — per-character `dp` under a `datamined` stamp (5/7 packs, 34 DP values)

| Page | datamined? | chars w/ DP | confidence line |
|---|---|--:|--:|
| `content/dlc/hero-of-justice-pack.md` | yes | 11 | L50 |
| `content/dlc/daima-character-pack-1.md` | yes | 9 | L43 |
| `content/dlc/preorder-pack.md` | yes | 7 | — |
| `content/dlc/daima-character-pack-2.md` | yes | 6 | — |
| `content/dlc/shallot.md` | yes | 1 | — |

```8:11:content/dlc/daima-character-pack-1.md
characters:
  - name: "Goku (Mini)"
    dp: 4
    slug: "goku-mini"
```
The DLC pack/character/costume lists *are* datamined (DLC_009/DLC_010), but the DP column is community —
the pages do cite `research/02-roster-dp-dlc.md` so sourcing is honest; the page-level `datamined` enum
over-claims the DP sub-field.

### 1d. Datamined pages with class-default ("—") move/blast damage

Secondary honesty surface (non-override move damage = community per `CLAUDE.md`). These pages disclose the
caveat in body prose, so they are *less* misleading than the DP case, but the page-level field still says
datamined:

- **373 of 453** `datamined` blast pages have **no** per-user datamined damage at all (every user row is
  `—` / class-default); only ki costs are datamined. Body prose discloses this ("'—' means the move
  inherits its class default"). e.g. `content/blasts/super-kamehameha-super.md:114`.
- **68** `datamined` character pages carry at least one moveset `damage:` value (mix of genuine
  `BulletSetting` overrides and community-labbed numbers; not separable from frontmatter alone).

### Recommended fix (one place, since these are generated collections)

The numbers themselves are not wrong — only the **label**. Fix in `scripts/gen_content.py` (do **not**
hand-edit generated files), choose one:
1. **Downgrade page-level `confidence` to `community`** for any generated page that surfaces a DP value
   (most faithful to the rule, but loses the "stats are datamined" signal); **or**
2. **Per-field provenance** — keep `datamined` for the battle params but tag DP/dpFrom/dpTo as community
   inline (the character template already does this in `sources`; extend it to transformations + DLC and
   render a "DP: community" chip); **or**
3. **Minimum viable:** (a) add `research/02-roster-dp-dlc.md` to every transformation/DLC `sources` array,
   and (b) change the transformation body template from "all numbers datamined from CharacterData" to
   "battle stats datamined; **DP is community** (research/02)."

---

# 2. ENUM CONFORMANCE — CLEAN (0 violations)

Validated every closed enum against `lib/schemas.ts` across all 13 collections (full coverage, not the
build's pass/fail bit). **Zero violations** — no latent build/regen crash hazard from hand-edit drift.

| Enum field | Collections | Allowed set | Violations |
|---|---|---|--:|
| `confidence` | all | confirmed/datamined/community/unverified | 0 |
| `moveset[].type` | characters | rush/smash/throw/blast1/blast2/ultimate/evasive/special | 0 |
| `transformsTo[].kind` | characters | transform/fusion/revert | 0 |
| `tier` | characters | S/A/B/C/D/unranked | 0 |
| `tier` | skills, blasts | S/A/B/C/D/situational | 0 |
| `class` | blasts | super/ultimate | 0 |
| `kind` | transformations | transform/fusion/awaken/revert | 0 |
| `category` + `values[].tag` | mechanics | offense/…/status + official/datamined/community | 0 |
| `category` + `values[].tag` | game-modes | offline/…/training + official/datamined/community | 0 |
| `type` | patches | launch/major/balance/content/hotfix | 0 |
| `type` | dlc | paid/free/preorder/season-pass | 0 |
| `category` | guides | meta/pvp/pve/beginner/tech/economy/tier-list | 0 |

(`glossary.category` is a free string in the schema — not enum-checked.)

---

# 3. NUMERIC SANITY SWEEP

| Check | Result | Detail |
|---|---|---|
| HP ∈ {30k,35k,40k,45k} | **0 bad** | every non-null HP is a valid tier |
| `dp` plausible (1–10) | **0 bad** | all DP in range |
| moveset `kiCost` ∈ [1000,60000] | **0 bad** | none out of band |
| ultimates ≈ 50k | **0 outliers** | all 207 ultimate entries = exactly 50,000 |
| supers cluster 10k–30k | **49 above 30k** (see note) | all are **40,000** = legit 2-bar supers; **0 truly anomalous** |
| `maxSkillStock` ≤ ~10 | **0 bad** | max observed = 7 (Babidi) |
| `initialSkillStock` ≤ `maxSkillStock` | **0 violations** | — |
| `skillGaugeGains` ∈ [0,2] | **0 bad** | max observed = 1.2 (vanishExchangeRate) |

**Super ki distribution** (char moveset / blast per-user): `{20000: 46, 30000: 317/309, 40000: 49}`.
The 40k entries flagged by the strict 10k–30k heuristic are **real 2-bar supers** (e.g. Jiren's
"Overheating Blast (40,000 ki)"), confirmed by the datamine — **not errors**. Ultimates: `{50000: 207}`.

### HP tier-count cross-check vs `data-mined/system_constants.json` — LOW drift

| HP | content (all) | content (playable) | datamine `hpDistribution` | Δ |
|---|--:|--:|--:|--:|
| 30,000 | 9 | 9 | 9 | 0 |
| 35,000 | 15 | 15 | 14 | **+1** |
| 40,000 | 150 | 148 | 147 | **+3** |
| 45,000 | 16 | 16 | 16 | 0 |
| **total** | **190** | 188 | **186** | **+4** |

All values are valid tiers (0 invalid). The +4 breaks down as: **+2** from two intentional *story-only*
duplicate character pages (`goku-super-0000-44`, `vegeta-super-0020-64`, both `playable:false`,
`hpInherited:true`, HP 40k), and **+2** benign drift between the live content (188 playable-with-HP) and
the `system_constants.json` snapshot (186). Treat as a **stale snapshot** note, not a content error.

---

# 4. DATE / VERSION CONSISTENCY — essentially CLEAN

| Check | Result |
|---|---|
| `asOfVersion` == `"v2.2 (2026-05-26 update)"` (non-patch pages) | **0 deviations** |
| `asOfDate` == `"2026-05-26"` (non-patch pages) | **0 deviations** |
| `lastVerified` stale (> 240 days before 2026-06-15) | **0** |
| `lastVerified` in the future (> 2026-06-15) | **0** |
| `lastVerified` malformed / unparseable | **0** |
| `lastVerified` missing | **0** (all 1,153 pages dated, almost all `2026-06-10`) |
| `sources` present & non-empty | **0 missing** (every page has ≥1 source) |

### 4a. `datamined` pages whose `sources` cite no game build — MEDIUM (6 glossary pages)

Datamined claim without a datamine source — sources are research briefs / other content pages only:

| Page | confidence | sources |
|---|---|---|
| `content/glossary/android-class.md:13` | datamined | research/04 only |
| `content/glossary/giant-class.md:13` | datamined | research/04, /02, /05 |
| `content/glossary/ki-blast.md:13` | datamined | research/04, /05 |
| `content/glossary/skill-count.md:14` | datamined | research/04, content/mechanics/skill-count.md |
| `content/glossary/smash-attack.md:13` | datamined | research/04 |
| `content/glossary/super-armor.md:13` | datamined | research/02, /04 |

**Fix:** retag these 6 glossary terms `community` (or `confirmed`) — their content is community frame-data
synthesis, not a game-file dump. (Curated collection — safe to hand-edit one file at a time.)

---

# 5. DUPLICATES

| Check | Result |
|---|---|
| Duplicate `slug:` within a collection | **0** |
| Duplicate display names | 31 — **all intentional** (29 blast super/ultimate pairs verified cross-class; 2 story-only character variants `goku-super` vs `goku-super-0000-44`, `vegeta-super` vs `vegeta-super-0020-64`) |
| Duplicate entries inside arrays | **1** (below) |

**LOW — duplicate `variants` entry:**
```5:7:content/stages/kame-house-tv-dimension.md
variants:
  - "Kame House TV Dimension"
  - "Kame House TV Dimension"
```
The body table shows this reflects two distinct stage IDs (`0720`, `0740`) that share one display name, so
the `variants` array lists the same label twice. Cosmetic; dedupe in the generator or list the IDs.

---

# 6. RENDERED-OUTPUT QA (scan of all 1,144 built HTML) — CLEAN

Scanned visible HTML (after stripping `<script>` React-flight payloads, `<style>`, and comments — those
legitimately contain `null`/`$undefined`/`[…]`).

| Artifact | Genuine occurrences | Verdict |
|---|--:|---|
| `>undefined<` | 0 | clean |
| `>NaN<` | 0 | clean |
| `>None<` | 0 | clean (4 text hits are prose: "None at the gameplay level", "None (unranked)") |
| `[object Object]` | 0 | clean |
| leaked `[[` wikilink | 0 | clean — all wikilinks resolved or degraded to text |
| leaked `\|` table-pipe | 0 | clean — GFM pipes escaped correctly |
| unformatted 5–7 digit numbers in `<td>` | **0** | clean — `fmtNum` applied everywhere (`40,000`, `1,750 /s`, `14,000`) |
| `>null<` | **1** — *false positive* | `mechanics/vanish-z-counter.html`: intentional `<code>null</code>` in prose explaining `vanishKiCost` is `null` in `characters.json` (honest!) |
| empty `<td></td>` | 1,175 — *benign* | the **optional trailing "note" column** of stat tables; the value column always renders `—` for unknowns, never blank (verified on `android-13`, `all-members`) |

The 22 text-node "null" hits are authored summary prose ("DP8 Anilaza Giant fusion; null-HP, super-armor
body…") — see NIT below. **No leaked rendering artifacts found.**

---

# 7. EMPTY / THIN BODIES — confirmed by design

| Collection | empty bodies | note |
|---|--:|---|
| characters | **245 / 245** | **frontmatter-only by design** — verified the rendered HTML shows rich content (DP/HP tiles, datamined battle-params table, skill-gauge table, strengths/weaknesses, how-to-fight, sortable moveset, transformation & "other forms" link grids). Not blank. |
| all other 12 collections | 0 | every page has a non-empty body |
| placeholder bodies (`TODO`/`TBD`/`lorem`/`pending fresh`/`schema dump`) | **0** | none |

`content/characters/goku-super.md` (empty body, 0 chars after frontmatter) renders to a full detail page
(`/characters/goku-super`) with no blank/near-blank sections. **No flag.**

---

# 8. MISC

| Check | Result |
|---|---|
| `playable` boolean present on all characters | ✓ 245/245 |
| `order` numeric where required (episode-battles, patches, dlc) | ✓ 0 bad |
| blasts with zero `users` | ✓ 0 |
| skills with `userCount` but empty `users` | ✓ 0 |
| `userCount` vs actual `users` length mismatch | ✓ 0 |
| skills with `users` but **no** `userCount` | **1** — `content/skills/fury.md` (2 users, no `userCount`) — LOW/NIT, schema-optional, renders fine |

---

# Findings ledger (severity-ranked)

### HIGH
**H1 — `confidence: datamined` over-claimed on 376 pages that surface community DP.**
208 characters (`dp:`), 163/164 transformations (`dpFrom`/`dpTo`), 5/7 DLC packs (34 char `dp`).
Worst subset: the **163 transformation pages** cite *only* the CUE4Parse extract and whose body states
*"all numbers datamined from CharacterData"* (e.g. `content/transformations/jiren-to-jiren-full-power.md:10`
dpFrom/dpTo, `:16` confidence, `:21` false body claim). Violates `CLAUDE.md` "DP is community, never
datamined." Numbers aren't wrong — the provenance label is. **Fix:** in `scripts/gen_content.py`, either
downgrade page `confidence`→`community` when a DP value is present, or add per-field DP-community tagging +
`research/02` to transformation/DLC `sources` + fix the transformation body template.

### MEDIUM
**M1 — 6 glossary terms stamped `datamined` with research-only sources** (no game-file citation):
`android-class:13`, `giant-class:13`, `ki-blast:13`, `skill-count:14`, `smash-attack:13`, `super-armor:13`.
**Fix:** retag `community`/`confirmed` (curated — edit directly).

### LOW
**L1 — HP tier counts drift from the datamine snapshot.** Content 9/15/150/16 (190) vs
`system_constants.json` 9/14/147/16 (186); +2 from intentional story-only dupes, +2 benign. All HP valid.
**Fix:** regenerate `system_constants.json` or note the snapshot date.
**L2 — 20 playable characters have null HP** (giants/fusion forms: `anilaza`, `cell-max`, `gogeta-super`,
`jiren-full-power`, `great-ape-baby-gt`, `hirudegarn`, `janemba`, …). Numbers-first completeness gap;
renders as `—`. **Fix:** datamine/lab the giant HP or document why null.
**L3 — duplicate `variants` entry**, `content/stages/kame-house-tv-dimension.md:6-7` (two stage IDs share
a name). **Fix:** dedupe in generator.
**L4 — `content/skills/fury.md`** has 2 `users` but no `userCount`. **Fix:** emit `userCount` in generator.

### NIT
**N1 — "null-HP" prose in 11 character summaries** (`anilaza`, `cell-max`, `giant-gomah`, `gohan-beast`,
`janemba`, `jiren-full-power`, `kefla`, `kefla-super-saiyan`, `kefla-super-saiyan-2`,
`orange-piccolo-giant-form`, `toppo-god-of-destruction`) reads like a leaked value in the rendered page
(`<p>…DP8 Anilaza Giant fusion; null-HP…`). **Fix:** reword to "HP not datamined".

---

*Probes are read-only and re-runnable: `python audit/a10_frontmatter.py | a10_numeric_detail.py |
a10_html.py | a10_html_context.py | a10_addendum.py`. JSON dumps: `audit/a10_frontmatter.json`,
`audit/a10_html.json`.*
