# Agent 07 — Link Integrity & Built-HTML Graph

**Scope:** wikilinks, the built-HTML href graph, cross-references, autolink, and the search
index. Read-only audit; no content/data/code modified. Probes live in `audit/a7_*.py|*.cjs`.

**Method:** Faithfully reconstructed `lib/content.ts` `getSlugIndex()` (first-wins priority +
glossary aliases) and `normalizeSlug()`, the `lib/markdown.ts` wikilink regex + autolink, and
`lib/linkify.tsx`, then resolved every link against that index and **cross-checked against the
already-green build** (`.next/server/app/**/*.html`, 1144 pages). The built HTML is treated as
ground truth — every theoretical finding below was confirmed (or refuted) against it.

---

## 0. Baseline — the three audit scripts all report CLEAN

| Script | Headline output | Verdict |
|---|---|---|
| `scripts/audit.py` | 1153 content files; **wikilinks 2591 total, 1 "broken"** (only `super-17`, whitelisted) | `AUDIT CLEAN` |
| `scripts/audit_v3.py` | **18 slug collisions, 0 unexpected**; 0 dead moveset links; 0 transformsTo-without-targetSlug; 0 rendered artifacts | `AUDIT v3 CLEAN` |
| `scripts/audit_v4.py` | scanned **1144 built pages**; **link graph 0 dead**; 1 dominant `asOfVersion` (1135 files); e2e samples ok; dup names `Goku (Super)`×2, `Vegeta (Super)`×2; 0 search-index dup hrefs | `AUDIT v4 CLEAN` |

**The scripts are clean but blind to the two biggest defects** (below). `audit.py`'s wikilink
regex is `\[\[([^\]|\\]+)` — it **excludes the backslash** from the target, so it silently
"repairs" the escaped-pipe links the real renderer chokes on, and never sees Finding **H1**.
No script renders/inspects heading-level placeholder leakage (**H2**).

---

## Severity summary

| ID | Sev | Finding | Count |
|---|---|---|---|
| **H1** | HIGH | `[[slug\|Label]]` escaped-pipe wikilinks never resolve (regex captures the `\`) | **1020/2591 links (39%)**; **105 cross-refs fully lost** in render across **68 pages** |
| **H2** | HIGH | Headings containing a wikilink/inline-code render NUL+index garbage (`␀70␀`) | **15 broken headings** on **2 flagship guides** |
| **M1** | MED | `dp-system` collision: `/game-modes/dp-system` (DP-Battle mode) unreachable via `[[dp-system]]` | 22 links → all hit `/mechanics/dp-system` |
| **M2** | MED | Autolink first-wins mis-targets duplicate display names | **31** labels (29 blast super/ult; 2 char dup-names) |
| **M3** | MED | Glossary **bodies never render** (page shows `definition` only) | **74** dormant wikilinks + all body prose, 30 pages |
| **L1** | LOW | Self-links: 10 collections omit `excludeHref` → body links to its own page | **85** self-links |
| **L2** | LOW | `slugify()` vs `normalizeSlug()` divergence (punctuation) — latent | 165 page names at risk; **0** live breaks |
| **L3** | LOW | 18 slug collisions shadow glossary/stage/dlc pages (mostly by-design) | 16 benign + M1 + `shallot` |
| **L4** | LOW | 5 common-word autolink labels (`shop`,`training`,`perception`,`kale`,`whis`) over-link risk | 5 |
| **N1** | NIT | 2 move-name spelling variants collapse to one blast page | 2 |
| **N2** | NIT | `[[hit]]` & other <4-char names can't be autolink-rescued | ties to H1 |

**Clean passes (verified, not assumed):** Check 3 moveset move-links (0 dead / 1035), Check 4
structured slugs (0 missing / 0 dead), Check 5 href graph (0 dead / 0 bad anchors / 0 `#`),
Check 6 search index (1153 entries, 0 dup, 0 dead, full coverage), Check 7 table pipes
(0 leaked `\|`, 0 malformed tables), and the autolink **protect/restore prose-corruption**
theory is **refuted** — the sentinel is `\x00` (NUL), which cannot collide with prose.

---

## CHECK 1 — Wikilink resolution (every `[[…]]` across `content/`)

Probe: `a7_check1.py`, `a7_check1b_rendered.py`. Faithful `markdown.ts` regex
`\[\[([^\]|]+)(?:\|([^\]]+))?\]\]` resolved via `normalizeSlug` against the reconstructed index.

```
TOTAL wikilinks            : 2591
resolve cleanly            : 1570
escaped-pipe VICTIMS       : 1020  (322 distinct targets) -- would resolve if fixed
escaped-pipe + still broken:    1  ([[super-17]], intentional S2)
genuine unresolved (plain) :    0
```

### H1 (HIGH) — `[[slug\|Label]]` escaped-pipe links silently degrade to plain text

**Root cause.** `gen_content.py` and the curated authors follow the CLAUDE.md §"Content &
linking conventions" rule *"In table cells, escape the pipe as `\|`"*, emitting `[[goku\|Goku]]`.
But `lib/markdown.ts`'s wikilink regex target group `[^\]|]+` **does not exclude `\`**, so for
`[[jiren\|Jiren]]` it captures target = `jiren\` (trailing backslash) → `normalizeSlug("jiren\\")`
= `jiren\` → **not in index → renders as the plain label**. Verified with `node` (`a7_regex_test.js`)
and in the build:

```75:75:.next/server/app/transformations/jiren-to-jiren-full-power.html
<p>From Jiren to Jiren, Full Power.</p>   <!-- neither "Jiren" is a link -->
```

Source that produced it: `gen_content.py` line 702-704 emits `From [[{from_slug}\|…]] to [[{to_slug}\|…]].`

**Scale — 1020 occurrences / 322 targets**, by source collection (`a7_aggregate.py`):

| Source collection | victims | origin |
|---|---|---|
| skills | 416 | generated "Datamined users" tables (`gen_content.py` L514) |
| transformations | 326 | generated "From X to Y" + sibling line (L702-703) |
| **episode-battles** | **129** | **hand-written** boss/counter tables |
| blasts | 58 | generated super↔ultimate sibling line (L416) |
| dlc | 44 | hand-written pack tables |
| guides | 27 | hand-written |
| game-modes | 19 | hand-written |
| mechanics | 1 | hand-written |

Top targets (occurrences): `sparking-mode`×15, `goku-super`×12, `vegeta-super`×12,
`perfect-cell`×11, `kale`×10, `fused-zamasu`×10, `vegito`×9, `goku-z-end`×9,
`perception`×8, `vanish-z-counter`×8, `gotenks`×8 … (full list: `python audit/a7_check1.py`).

**Real rendered impact (`a7_check1b_rendered.py`).** Autolink partially papers over this by
re-linking the plain-text label's *first* mention per page:

```
pages with victim links            : 394
distinct intended targets          : 988
RESCUED by autolink (href present) : 883
LOST  (href absent from page)      : 105   across 68 pages
```

The **105 lost cross-references** are the real damage. Worst pages:

| Page | lost targets |
|---|---|
| `episode-battles/episode-frieza.md` | `/characters/goku-super`, `/characters/goku-z-mid-super-saiyan`, **`/characters/hit`**, `/characters/vegeta-super`, `/mechanics/sparking-mode`, `/mechanics/vanish-z-counter` |
| `episode-battles/episode-future-trunks.md` | `fused-zamasu-half-corrupted`, `gohan-adult`, `goku-black-super-saiyan-ros`, `vegeta-z-end`, `sparking-mode`, `vanish-z-counter` |
| `episode-battles/episode-vegeta.md` | `goku-z-end`, `android-class`, `skill-count`, `sparking-mode`, `super-armor`, `vanish-z-counter` |
| `episode-battles/episode-goku.md` | `perfect-cell`, `giant-class`, `smash-and-rush`, `sparking-mode`, `vanish-z-counter` |
| `episode-battles/episode-goku-black.md` | `future-trunks-super-saiyan`, `goku-super-…-ssgss`, `vegeta-super-…-ssgss`, `sparking-mode`, `vanish-z-counter` |
| `episode-battles/episode-jiren.md` | `android-17-z`, `goku-super-ultra-instinct`, `vegeta-super-…-ssgss`, `skill-count`, `sparking-mode` |
| `episode-battles/episode-gohan.md`, `episode-piccolo.md` | 4 each (mechanics + a character) |
| `guides/ranked-climbing-guide.md` | `defense-bible`, `matchups-and-counterpicks`, `offense-and-pressure`, `settings-and-controls` (4 sibling guides) |
| `dlc/season-pass-1.md` | `daima-character-pack-1`, `daima-character-pack-2` |
| **29 × `blasts/<x>-super`** | each loses its `/blasts/<x>-ultimate` sibling link (e.g. `galick-gun-super` → `galick-gun-ultimate`) |

`[[hit\|Hit]]` (episode-frieza) is doubly doomed: the wikilink fails **and** "Hit" is 3 chars,
below the autolink length≥4 gate, so it can never be rescued (see N2).

**Recommended fix (one line, fixes all 1020).** In `lib/markdown.ts`, make the wikilink regex
tolerate the escaped pipe — exclude `\` from the target and optionally consume it before `|`:

```js
// was: /\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g
md.replace(/\[\[([^\]|\\]+)\\?(?:\|([^\]]+))?\]\]/g, (_m, target, label) => { … })
```

This matches `audit.py`'s own regex behavior, keeps the `\|` table-escape working, and restores
all 322 targets at once. (No content edit needed; the escape stays valid GFM.)

---

## CHECK 2 — Slug-collision mis-resolution (first-wins)

Probe: `a7_check2_collisions.py`. **18 collisions** (matches `audit_v3`). Priority:
`characters > skills > blasts > transformations > mechanics > game-modes > episode-battles >
patches > dlc > guides > stages > shop > glossary`.

### M1 (MEDIUM) — `dp-system`: the DP-Battle *mode* page is wikilink-unreachable
- Owners: `mechanics/dp-system` (label **"DP System"**, WINNER) vs `game-modes/dp-system`
  (label **"DP Battle (Destruction Points System)"**, shadowed). **22** `[[dp-system]]` links.
- Intent is genuinely split. Most links want the cost mechanic and are fine on mechanics, but
  several explicitly mean the **mode**: `game-modes/versus.md:45,53` ("Team-format details:
  `[[dp-system]]`"), `game-modes/world-tournament.md:63` ("Team math: `[[dp-system]]`"),
  `game-modes/ranked-match.md:48` ("see the conflict on `[[dp-system]]`"). All resolve to
  `/mechanics/dp-system`; the mode page is reachable only by typing `/game-modes/dp-system`.
- **Fix:** rename the mode page slug (e.g. `game-modes/dp-battle`) or add a prominent
  cross-link between the two pages.

### Benign / by-design collisions (16)
- **`shallot`** (characters > dlc): every `[[shallot]]` (skills tables, `patches/shallot-2025-06-27.md:25`,
  `dlc/season-pass-1.md:40`) intends the **fighter** → intent satisfied. The DLC-pack page
  `/dlc/shallot` is just wikilink-unreachable. **No mis-resolution.**
- **mechanics shadow glossary (12):** `perception`(56), `super-counter`(40), `sparking-mode`(32),
  `revenge-counter`(22), `skill-count`(18), `giant-class`(14), `z-burst-dash`(14),
  `instant-sparking`(14), `sonic-sway`(8), `dragon-dash`(6), `super-armor`(5),
  `vanishing-assault`(4). The fuller mechanics page winning is **correct**; the glossary term is
  only reachable by scrolling `/glossary` (it has no `[[slug]]` route). Acceptable.
- **`afterimage-strike`** (skills > glossary): skill page wins; fine.
- **game-modes shadow stages (2):** `custom-battle`, `world-tournament` — the mode wins over the
  menu-backdrop stage; intent satisfied.
- **9 glossary aliases shadowed by a real slug** (`a7_check2` tail): all point to an equal-or-better
  page (`sparking-mode`, `super-counter`, `z-burst-dash`, `dragon-dash` → mechanics; the rest →
  their own glossary slug). Benign.

**No character-vs-glossary collision exists.** (Characters outrank everything, but none share a
slug with a glossary term.)

---

## CHECK 3 — Moveset move-links + slugify divergence

Probe: `a7_check3_movesets.py`, `a7_check3b_movecollide.py`.

- **0 dead** out of **1035** move-links (416 blast1, 412 blast2, 207 ultimate). The component
  `app/characters/[slug]/page.tsx` `slugifyName()` (L30-36) is **byte-identical** to
  `gen_content.py` `slugify()` (L37-41) — both strip `['’!.]` then `[^a-z0-9]+→-` — so every
  `blast2→<s>-super`, `ultimate→<s>-ultimate`, `blast1→<s>` target maps to a real page.
- **L2 (LOW) divergence (latent).** `normalizeSlug()` (used for `[[wikilinks]]`) only lowercases
  + collapses whitespace — it does **not** strip punctuation, unlike `slugify()` (used for file
  names). **165 page names** would therefore fail if wikilinked by display name, e.g.
  `Dr. Gero`→file `dr-gero` but `normalizeSlug("Dr. Gero")`=`dr.-gero`; `Cell, 1st Form`→
  `cell-1st-form` vs `cell,-1st-form`; `Android 17 (Super)`→`android-17-super` vs
  `android-17-(super)`. **Live breaks today: 0** (authors always write the pre-slugified target).
  Footgun only. **Fix:** align `normalizeSlug` to strip the same punctuation as `slugify`, or
  register display-name aliases.
- **N1 (NIT).** 2 distinct move spellings collapse to one page: `Full Power Energy Blast Volley`
  / `Full-Power Energy Blast Volley` → `/blasts/full-power-energy-blast-volley-super`;
  `High Speed Rush` / `High-Speed Rush` → `/blasts/high-speed-rush-super`. Both reach a valid page
  (not dead) — purely a source-data spelling inconsistency.

---

## CHECK 4 — Missing structured-link slugs

Probe: `a7_check4_slugs.py` (YAML-parsed, not regex). **All clean:**

| Layer | total | missing slug | slug→missing page |
|---|---|---|---|
| `characters.transformsTo[].targetSlug` (→ `#` if absent) | 163 | **0** | **0** |
| `blasts.users[].characterSlug` (→ plain text if absent) | 611 | **0** | **0** |
| skills body-table user rows (`[[slug\|name]]`) | all | **0** | n/a |

Note: the skill detail page renders frontmatter `users` (a name-string list) as **plain `<span>`
badges, never linked** (`app/skills/[slug]/page.tsx` L52-56) — by design; the only skill→character
links are the body table, which are H1 escaped-pipe victims. No `href="#"` exists anywhere in the
build (cross-checked in Check 5).

---

## CHECK 5 — Built-HTML internal href graph

Probe: `a7_check5_htmlgraph.py`. Scanned **1144** pages; valid-path set built from content dirs +
`/ /stats /meta /compare /dna /classes` + 13 listing routes (1142 paths + 30 glossary anchors).

```
DEAD internal href bases        : 0
DEAD /glossary#anchor (no id)    : 0   (all anchors hit a real <div id="slug"> on /glossary)
href="#" dead anchors            : 0   (confirms Check 4: 0 transformsTo missing targetSlug)
non-glossary #fragment hrefs     : 0
distinct internal targets seen   : 1137
```

**The href graph is completely clean.** This is the key structural insight: failed wikilinks emit
**no href at all** (they become plain text), so H1 produces *missing* links, never *dead* ones —
which is exactly why every link-graph audit passes while 105 cross-references are silently gone.

---

## CHECK 6 — Search index (`public/search-index.json`)

Probe: `a7_check6_searchindex.py`.

```
entries: 1153  == content files: 1153   (one entry per file; 30 glossary → /glossary#slug)
missing title t: 0 | missing group g: 0 | missing href h: 0
href does not resolve to a built page: 0
duplicate hrefs: 0
detail pages absent from index: 0   (full coverage)
empty hint x (optional field): 469
```

Group distribution matches collection counts exactly (Fighter 245, Blast 453, Skill 146,
Transformation 164, Mechanic 22, Mode 12, Episode Battle 8, Patch 18, DLC 9, Guide 12, Stage 27,
Shop 7, Glossary 30). **No gaps, no dups, no dead hrefs.** (Entry count 1153 = content files;
built *pages* 1144 because 30 glossary terms collapse to one `/glossary` page while listing/utility
routes add ~21 — both reconcile to the ~1144 expectation.)

---

## CHECK 7 — Table pipe escaping & malformed GFM tables

Probe: `a7_check7_tables.py` (scans all 1144 built pages).

```
leaked literal '\|' in output      : 0
'|' inside rendered <td>/<th>      : 0
malformed tables (col-count != hdr): 0
```

Clean. The `\|` in `[[slug\|label]]` is always consumed (the backslash goes into the wikilink
target, the pipe is the separator, the label is extracted) so the GFM table stays intact — the
**only** casualty is the link itself (H1). Outside wikilinks, `marked` handles `\|` correctly.

---

## CHECK 8 — Autolink integrity

Probes: `a7_check8a_corruption.py` (+ `a7_check8a_nodetest.cjs`, `a7_full_render.cjs`,
`a7_bytes.py`/`a7_bytes2.py`), `a7_check8_autolink.py`, `a7_nul_context.py`, `a7_nul_count.py`.

### H2 (HIGH) — Headings with a wikilink/inline-code render NUL+index garbage

`lib/markdown.ts` `autolink()` shields code/links/headings/table-separators by replacing each
with a **NUL-delimited** placeholder `` `\x00${i}\x00` `` (L44) and restores with
`work.replace(/\x00(\d+)\x00/g, …)` (L63) — a **single pass**. Protection runs **inline-code/links
first, then whole headings** (L48-52), so a heading that contains a link/code gets a placeholder
*nested inside* the heading placeholder. On restore, the heading placeholder is replaced by text
that still contains the inner `\x00N\x00`, and `String.replace` does **not** re-scan inserted text
→ the inner placeholder leaks as a literal NUL into the HTML.

Confirmed in the build (`a7_nul_context.py`):

```
<h3>1. ␀70␀ — #1 Singles (152.8k)</h3>          (matchups Top-15: character link → garbage)
<h3>Which S1s are flagged unblockable ␀26␀</h3> (offense: inline-code tag → garbage)
```

Source triggers (`a7_nul_count.py`, **17** headings; **15 visibly broken** in build):
- `guides/matchups-and-counterpicks.md:34-146` — **15** "Top-15 meta picks" headings, each
  `### N. [[<char>|Label]] — …` (e.g. L34 `[[vegito-super-saiyan-god-super-saiyan|Vegito (SSGSS)]]`).
  13 leak NUL; the character name is replaced by a stray index number on this **flagship** guide.
- `guides/offense-and-pressure.md:66,106` — 2 headings with inline-code (`` `[datamined]` ``).

Only these **2 pages** leak NUL (the only content headings that embed a link/code).

**Fix (`lib/markdown.ts`):** either (a) loop the restore until no `\x00\d+\x00` remains, or
(b) protect headings/table-separators **before** inline-code/links so nesting can't occur, or
(c) exclude headings from autolink entirely. Option (a) is the minimal change.

### Control: protect/restore prose corruption — **NOT a bug** (theory refuted)
A space-delimited placeholder would let a prose number like `" 15 "` collide with the restore
regex and be overwritten (→ `undefined`/injected fragment). My first port reproduced this and the
shell rendered the placeholder as a space — but the **raw bytes show the delimiter is `\x00`**
(`a7_bytes.py`), which cannot occur in prose. The build confirms intact prose: `"…base game's 182
roster slots…"`, `"…Season 1 bundle…"`, `"…chapters 2, 3, 5 and 7…"`, `"10 / 15 / 20"` all correct,
**0 `undefined`** in body text. So the mechanism is safe; only the *nesting* edge (H2) breaks.

### L1 (LOW) — 85 self-links (missing `excludeHref`)
Only `characters` and `blasts` pass `{ excludeHref: self }` to `renderMarkdown`; the other 10
collections call `renderMarkdown(body)` bare, so a body mention of the page's own name autolinks
to itself. **85 self-links** (`a7_aggregate.py`): skills 25, stages 25, mechanics 11, game-modes
10, dlc 8, patches 6. Examples: `mechanics/perception` → "Perception" links to itself;
`patches/v2025-01-20` → version "Ver.2008…" self-links. **Fix:** pass `{ excludeHref: '/<coll>/<slug>' }`
in the 10 detail pages (mirror characters/blasts).

### M2 (MEDIUM) — 31 duplicate-label autolink mis-targets (first-wins)
`a7_check8_autolink.py`. When a display name maps to ≥2 pages, autolink always picks the
priority-first one:
- **29 blast super/ultimate pairs** — e.g. `Final Flash`, `Galick Gun`, `Super Kamehameha`,
  `Special Beam Cannon`, `Big Bang Attack`, `Dragon Fist` … always link to `/blasts/<x>-super`,
  never `…-ultimate`. Any prose mention of these (and the lost sibling links from H1) can never
  reach the ultimate variant.
- **2 character dup-names** — `Goku (Super)` autolinks to `/characters/goku-super-0000-44`
  (the charId-suffixed collision slug), **not** `/characters/goku-super`; same for
  `Vegeta (Super)` → `/characters/vegeta-super-0020-64`. The mention may point at the wrong form.
  (Root data dup flagged by `audit_v4`; relevant to Agent 1.)

### L4 (LOW) — common-word autolink labels
5 labels are ordinary words matched case-insensitively: `shop`→`/game-modes/shop`,
`training`→`/game-modes/training`, `perception`→`/mechanics/perception`, `kale`→`/characters/kale`,
`whis`→`/characters/whis`. Mostly correct in context (these terms are domain jargon here), but
`shop`/`training` can grab an unrelated prose word's first occurrence. The classic *"Hit"* case is
**safe** — `Hit` is 3 chars, below the length≥4 autolink gate (the flip side of N2).

---

## CHECK (bonus) — Glossary bodies not rendered

### M3 (MEDIUM) — `app/glossary/page.tsx` renders `definition` only, never `body`
The glossary page (L18-29) outputs `t.term`, `t.aliases`, `t.category`, `t.definition` — but never
`t.body` and never calls `renderMarkdown`. So every glossary file's markdown body is invisible in
the build. Verified: body-only phrases ("auto-reflect is locked to DP7+", "cost system that
balances") are **absent** from `.next/server/app/glossary.html`; only the `definition` field shows.
Impact: **74 wikilinks** in glossary bodies (`a7_aggregate.py`) plus all body prose are dormant.
(Also: because `definition` is interpolated as a plain React string, any markdown/`[[link]]` an
author puts in `definition` would render literally — none do today.) **Fix:** render
`renderMarkdown(t.body)` under each definition (and pass `excludeHref` to avoid self-links).

---

## Probe inventory (throwaway, under `audit/`)
`a7_lib.py` (shared index/regex), `a7_check1.py`, `a7_check1b_rendered.py`,
`a7_check2_collisions.py`, `a7_check3_movesets.py`, `a7_check3b_movecollide.py`,
`a7_check4_slugs.py`, `a7_check5_htmlgraph.py`, `a7_check6_searchindex.py`,
`a7_check7_tables.py`, `a7_check8a_corruption.py`, `a7_check8_autolink.py`,
`a7_nul_context.py`, `a7_nul_count.py`, `a7_aggregate.py`, `a7_bytes.py`, `a7_bytes2.py`,
`a7_dump_maps.py`, plus node: `a7_regex_test.js`, `a7_check8a_nodetest.cjs`, `a7_full_render.cjs`.
All read-only.
