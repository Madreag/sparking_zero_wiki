# Agent 09 — TypeScript / Next.js Code Review

**Scope:** `lib/`, `app/` (every page), `components/`, build config. Reviewed against the live
build in `.next/` (1144 pages, green) on **2026‑06‑15**. No code/content/data was modified.
Read‑only probe scripts were used (see Methodology) and are deleted.

Stack: **Next 16.2.7 · React 19.2.7 · Zod 4.4.3 · marked 18.0.5 · gray‑matter 4.0.3 · Tailwind 4**.
Node 22.22, Turbopack build.

## Severity counts

| Severity | Count |
|---|---|
| BLOCKER | 1 |
| HIGH | 3 |
| MEDIUM | 7 |
| LOW / NIT | 9 |

## Top bugs (one‑liners, file:line)

1. **BLOCKER** — `lib/markdown.ts` `autolink()` protect/restore uses ` ${i} ` (space‑index‑space) + `/ (\d+) /g`; collides with ordinary prose/table numbers → **346/908 rendered bodies corrupt** (numbers become `undefined` or inject headings/links). Currently *dormant* behind a stale `.next` prerender cache.
2. **HIGH** — `app/stats/page.tsx:32‑34,77‑78` `readJson(rel)` = `fs.readFileSync(path.join(process.cwd(), rel))` defeats NFT static analysis → stats traces the **whole project incl. `data-mined/raw/`** (`stats/page.js.nft.json` = 281 KB vs 73 KB baseline).
3. **HIGH** — `lib/schemas.ts:42,143` enum drift: `transformEntry.kind` lacks `awaken` (but `transformationSchema.kind:129` has it); `numericValue.tag` lacks `confirmed`/`unverified` (which `confidence` allows) → silent **build‑crash** if a future regen emits those values.
4. **HIGH** — `lib/schemas.ts:69,90,116` tier enums diverge (`unranked` for characters vs `situational` for skills/blasts) → cross‑collection enrichment value crashes the build.
5. **MEDIUM** — `lib/content.ts:156‑158` `normalizeSlug` only converts spaces; Python `gen_content.py:37‑40 slugify` strips `'’!.`/punctuation → `[[Goku (GT)]]`, `[[Gohan, Future]]` wikilinks silently don't resolve.
6. **MEDIUM** — `components/sortable-tables.tsx` + `components/roster-table.tsx:110‑125` click‑to‑sort headers are `<th onClick>` with no keyboard/ARIA; `sortable-tables` also mutates DOM of React‑owned tables (e.g. `meta-board` counters) → lost sort / reconciliation risk.
7. **MEDIUM** — `lib/formulas.ts:16‑38` `pctChange`/`dmgPerKi`/`dmgPerDp`/`hpPerDp` (+ both `fmtPct`) are **dead code** (never imported) → the advertised "value‑per‑DP" metrics are not surfaced anywhere.
8. **MEDIUM** — 12 `dangerouslySetInnerHTML` sinks render **unsanitized** `renderMarkdown` output (`app/**/[slug]/page.tsx`); first‑party so XSS risk is low, but the bug in #1 injects arbitrary stored markup into them.

---

# A. BLOCKER — `markdown.ts` autolink protect/restore numeric collision

### A.1 The defect

`lib/markdown.ts` `autolink()` (the file trips ripgrep/Read binary detection; line numbers below
are from the source‑map dump in `.next`, and the exact text is reproduced verbatim):

```ts
// lib/markdown.ts  (autolink, ~L43–66)
const protectedParts: string[] = [];
const protect = (s: string) => {
  protectedParts.push(s);
  return ` ${protectedParts.length - 1} `;        // <-- placeholder = SPACE index SPACE
};
let work = md
  .replace(/```[\s\S]*?```/g, protect)            // code fences  -> " 0 "
  .replace(/`[^`\n]*`/g, protect)                 // inline code  -> " 1 "
  .replace(/!?\[[^\]]*\]\([^)]*\)/g, protect)     // links/images -> " 2 " ...
  .replace(/^#{1,6} .*$/gm, protect)              // headings
  .replace(/^\|[ :|-]+\|\s*$/gm, protect);        // table separator rows
// ... name‑autolink pass ...
return work.replace(/ (\d+) /g, (_, i) => protectedParts[Number(i)]);   // <-- restore
```

The placeholder is a **bare integer wrapped in single spaces**, and the restore regex is the
unanchored, global `/ (\d+) /g`. That pattern matches **any** space‑delimited integer in ordinary
prose or in GFM table cells — not just the placeholders. Every such number is destructively
replaced by `protectedParts[thatNumber]`:

- If the index is **out of range** → the replacement value is `undefined`, which `String.replace`
  coerces to the literal string `"undefined"` (and eats the surrounding spaces, mashing words
  together): `deal 0 damage and gain 1 bar` → `dealundefineddamage and gainundefinedbar`.
- If the index is **in range** → the prose number is replaced by an unrelated shielded span
  (a heading, link, or code span) pulled from elsewhere in the same document.

This is `marked`‑independent: corruption happens in `autolink()` **before** `marked.parse`, so the
broken string is what gets parsed and emitted.

Notes on edge behaviour (all verified):
- The placeholders themselves are double‑spaced when adjacent (`" 0 " + " 1 " = " 0  1 "`), so the
  *intended* restore still works; the collision is purely with content numbers.
- The regex is **non‑overlapping**, so in a run like `1 2 3 4` only alternating numbers are caught
  (`areundefined2undefined4`) — corruption is partial and irregular, which makes it easy to miss.
- Multi‑digit numbers collide too: a transformation stat cell `| 40000 |` → `protectedParts[40000]`
  → `undefined`.

### A.2 Worked example — `content/skills/afterimage-strike.md`

Body prose contains `The Dec 11 2024 update cut the duration…` and a user table row
`| Super Baby 1 (GT) | 1 | — |`. Running the **real** pipeline (faithful reimplementation using the
project's own `gray-matter`, `marked`, and the real cross‑collection slug index) produces:

```text
buggy : … "Wild West" meta. The Decundefined2024 update cut the duration …
fixed : … "Wild West" meta. The Dec 11 2024 update cut the duration …

buggy : …/super-baby-1-gt">Super Baby## Datamined users & stock costs …   (heading injected)
fixed : …/super-baby-1-gt">Super Baby 1 (GT)</a></td> …

buggy : <td>undefined</td>   (every single‑digit stock cost cell)
fixed : <td>4</td>
```

`Dec 11 2024` → `Decundefined2024` because ` 11 ` indexes past the end of `protectedParts`.
The stock‑cost cells (` 4 `, ` 1 `, ` 3 `) and the name `Super Baby 1 (GT)` (` 1 `) all collide.

Lightning example (`content/mechanics/lightning-attack-pursuit.md`): `Pursuit limit: 6 per combo`
→ `Pursuit limit:## The numbersper combo` (the ` 6 ` resolves to the protected `## The numbers`
heading).

### A.3 Blast radius — 346 / 908 bodies

Rendering every collection body buggy‑vs‑fixed (a diff is, by construction, a corruption):

| Collection | corrupt / total | Collection | corrupt / total |
|---|---|---|---|
| transformations | **164 / 164** | mechanics | 19 / 22 |
| skills | 91 / 146 | patches | 16 / 18 |
| guides | **12 / 12** | dlc | **9 / 9** |
| episode‑battles | **8 / 8** | glossary | 15 / 30¹ |
| game‑modes | 11 / 12 | stages | 1 / 27 |
| characters | 0 / 0² | blasts / shop | 0 |

Total **346 / 908**; **318** emit a literal `undefined`. ¹ Glossary bodies are *never rendered*
(`app/glossary/page.tsx:27` shows only the frontmatter `definition` as plain text), so glossary
escapes this live. ² Character pages have empty markdown bodies (all data is frontmatter).
Net pages that would ship corrupted on a clean build: **~331**, including **every transformation,
guide, DLC, and episode‑battle page**, plus most skills/mechanics/patches.

### A.4 Why the live build looks clean (and why that is a trap)

The current `.next/server/app/*.html` is **clean** — I confirmed by reading the built HTML for
`lightning-attack-pursuit` (`Pursuit limit: 6 per combo`) and `afterimage-strike` (`Dec 11 2024`,
`<td>3</td>`), and by grepping all 1144 pages for the corruption signatures `[a-z]undefined[a-z]`
and `[a-z]## ` (zero matches; the earlier "undefined" hits are React RSC noise like
`"crossOrigin":"$undefined"`).

This is **not** because the code is correct. Evidence chain:
- `lib/markdown.ts` mtime = 2026‑06‑10 15:47 (buggy); the build is fresh (`BUILD_ID` 2026‑06‑15 10:16).
- The build's **own source map** (`.next/server/chunks/ssr/node_modules_next_dist_1d_onnt._.js.map`
  → `sourcesContent` for `../../../../lib/markdown.ts`) contains the **exact buggy** `/ (\d+) /g`
  restore — so the build compiled the buggy code.
- Yet the rendered HTML is the *correct* output. The only consistent explanation is Next's
  **prerender cache** (`.next/cache` exists): pages were rendered into the route cache by a build
  *before* the bug landed (pre‑06‑10 15:47) and the 06‑15 build re‑emitted those cached renders for
  unchanged `.md` files.

**Consequence:** the bug is **dormant, not fixed.** It activates on the next cache‑busting event —
`rm -rf .next`, a fresh clone, a CI build, or (most likely, per the Season 2 roadmap) the next
`python scripts/gen_content.py` run, which rewrites every generated `.md`, invalidates the route
cache, and forces a re‑render through the buggy code. For a "numbers‑first" wiki, shipping pages
where datamined numbers read `undefined` is a product‑breaking regression that the green build does
not catch.

### A.5 Fix

Use a placeholder that cannot occur in content and a restore regex that matches only it. Minimal,
behaviour‑preserving change (validated: produces byte‑identical output to the "fixed" column above
on all 908 bodies):

```ts
const protect = (s: string) => {
  protectedParts.push(s);
  return `\u0000${protectedParts.length - 1}\u0000`;   // NUL sentinels — never in markdown
};
// ...
return work.replace(/\u0000(\d+)\u0000/g, (_, i) => protectedParts[Number(i)]);
```

(Any private‑use sentinel works, e.g. `\uF8FF…\uF8FF`.) Better long‑term: stop string‑splicing and
autolink against `marked`'s token stream / text nodes, or use a `marked` extension, so code/links/
headings never need shielding. Add a regression test that renders a body containing
`deal 3 hits in 2 bars` and asserts the digits survive.

---

# B. HIGH findings

### B1. `app/stats/page.tsx` — whole‑project NFT over‑tracing (the real cause is `process.cwd()` + a dynamic path, not a `next.config` import)

`app/stats/page.tsx:32‑34,77‑78`:

```ts
function readJson<T>(rel: string): T {
  return JSON.parse(fs.readFileSync(path.join(process.cwd(), rel), "utf8")) as T;
}
// ...
const c = readJson<Constants>("data-mined/system_constants.json");
const ranks = readJson<Rank[]>("data-mined/ranks.json");
```

There is **no `import next.config.mjs`** anywhere in `app/`/`lib/`/`components/` (grep‑confirmed) —
the assumption in the brief doesn't match this code. The actual trigger of the
"whole project traced unintentionally" warning is the `process.cwd()` + **dynamic argument** read:
Turbopack's Node‑File‑Trace can't statically resolve `path.join(process.cwd(), rel)` when `rel` is a
function parameter, so it conservatively traces the entire working directory.

**Evidence (build artifacts):** `stats/page.js.nft.json` = **281,865 bytes** vs ~73,000 for every
other page and ~76,800 for `[slug]` pages. It includes `CLAUDE.md`, `PLAN.md`, `README.md`, every
`app/**/page.tsx`, and — uniquely — `data-mined/raw/…` (`masterdata`/`locres`/`stringtable`); the
`meta` page (which builds its path from **literal** segments, `app/meta/page.tsx:20`) does **not**
pull `raw/`. So `stats` alone drags the multi‑hundred‑MB CUE4Parse dump into its trace.

*Failure scenario:* a `standalone`/server deploy (or `next start`) copies the whole repo + raw
datamine into the function bundle for one stats page; build‑time tracing is also markedly slower.

*Fix:* import the JSON statically (tsconfig already has `resolveJsonModule: true`):
`import constants from "@/data-mined/system_constants.json";` — the dependency becomes exact. At
minimum, inline literal path segments and drop the generic `readJson(rel)` helper. (Note `lib/content.ts:21,29‑35` also uses `process.cwd()` + `readdirSync`, which is why the 73 KB baseline already traces all of `content/`; that's the unavoidable directory‑glob case, but `data-mined/raw/` should never be in any trace.)

### B2. `lib/schemas.ts` — enum drift between the embedded `transformEntry` and `numericValue` and their siblings (latent build‑crash)

- `transformEntry.kind` (`schemas.ts:42`) = `["transform","fusion","revert"]` — **missing `awaken`**,
  but the standalone `transformationSchema.kind` (`:129`) = `["transform","fusion","awaken","revert"]`.
  A character whose `transformsTo[].kind === "awaken"` hard‑crashes `characterSchema.parse` and the
  whole build. (`awaken` already appears in transformation slugs/names like
  `…-power-awakening`, so an "awaken" kind is plausible the moment the generator emits it for the
  character‑side edge. Currently safe — `gen_content.py` emits no `kind: "awaken"` — i.e. **latent**.)
- `numericValue.tag` (`:143`) = `["official","datamined","community"]`, but the shared `confidence`
  (`:11‑13`) = `["confirmed","datamined","community","unverified"]`. It is very easy to tag a
  mechanic/game‑mode value `confirmed` or `unverified` (the words used everywhere else) → crash.
  Grep confirms current content uses neither tag (latent).

*Failure scenario:* a Season‑2 enrichment overlay adds one value with the "wrong" closed‑set member;
`loadCollection` throws (it does name the file, `content.ts:42‑47`, which is good), and **all 1144
pages fail to build**. *Fix:* unify the enums (add `awaken` to `transformEntry.kind`; decide one tag
vocabulary), or relax to `z.string()` + a lint, since out‑of‑set values should degrade, not detonate.

### B3. `lib/schemas.ts` — tier enum is collection‑specific and mutually exclusive

`characterSchema.tier:69` = `S|A|B|C|D|unranked`; `skillSchema.tier:90` and `blastSchema.tier:116`
= `S|A|B|C|D|situational`. The two extra members are disjoint. Enrichment that sets a character to
`situational`, or a skill/blast to `unranked`, crashes the build. Combined with B2 this is the single
most likely way a future data pass turns the green build red. *Fix:* one shared `tierSchema`, or
allow both sentinels everywhere.

---

# C. MEDIUM findings

### C1. `lib/content.ts:156‑158` — `normalizeSlug` ≠ Python `slugify` → silent dead wikilinks
```ts
export function normalizeSlug(s: string){ return s.trim().toLowerCase().replace(/\s+/g, "-"); }
```
The generator (`scripts/gen_content.py:37‑40`) does `lower → strip /['’!.]/ → [^a-z0-9]+→"-"`.
`normalizeSlug` strips **nothing but spaces**, so any `[[target]]` whose target carries punctuation
diverges: `[[Goku (GT)]]` → `goku-(gt)` ≠ slug `goku-gt`; `[[Gohan, Future]]` → `gohan,-future`;
`[[Spirit Bomb!]]` → `spirit-bomb!`. Per `renderMarkdown` (`markdown.ts`, wikilink pass) an unknown
target **degrades to plain text** — no crash, no dead `<a>`, but the intended link silently vanishes.
Generated `[[slug|Label]]` links are safe (already clean slugs); hand‑authored curated links using
display names are the exposure. *Fix:* make `normalizeSlug` mirror the Python slugify
(`replace(/['’!.]/g,"").replace(/[^a-z0-9]+/g,"-").replace(/^-+|-+$/g,"")`).

### C2. `components/sortable-tables.tsx` & `components/roster-table.tsx:110‑125` — sort a11y + React/DOM ownership conflict
- Click‑to‑sort headers are `<th onClick … style.cursor=pointer>` with no `role="button"`,
  `tabindex`, or keydown handler → not keyboard‑operable, not announced by SR.
- `SortableTables` (`:14`) selects `main table:not([data-sortable-self])` and reorders rows via
  `tbody.appendChild`. The client tables opt out via `data-sortable-self`, **but the `meta-board`
  counter table does not** (`meta-board.tsx:82`). It's a React‑rendered table, so (a) the manual
  sort is wiped when `MetaBoard` re‑renders on Singles/DP tab toggle, and (b) the effect only re‑runs
  on `pathname` change (`:60`), so after a tab toggle the freshly mounted table has no listeners.
  Mutating React‑owned DOM nodes also risks reconciliation glitches. *Fix:* add
  `data-sortable-self` to the meta counters table (or make it a client‑sorted table), and make the
  static‑table headers real buttons with keyboard support.

### C3. `lib/formulas.ts:16‑38` + `components/ui.tsx:4‑7` — value metrics are dead code
`pctChange`, `dmgPerKi`, `dmgPerDp`, `hpPerDp` and **both** copies of `fmtPct` are never imported by
any page/component (grep: only the definitions in `formulas.ts`/`ui.tsx` + docs). Only `fmtNum` is
used. So the "core team‑builder value metrics" the docs advertise (damage‑per‑DP, HP‑per‑DP, quantified
patch %‑deltas) are **not rendered anywhere** — `compare.tsx`/patch pages show raw costs/old‑new
strings instead. This is the numbers‑first promise going unfulfilled in the UI, plus dead surface
area. Their latent bugs (below, D7) only matter once wired up. *Fix:* either surface them
(e.g. a damage/DP column in `compare`/blasts) or delete them; de‑duplicate `fmtPct`.

### C4. Unsanitized `dangerouslySetInnerHTML` (12 sinks)
All `[slug]` detail pages render `renderMarkdown(body)` via `dangerouslySetInnerHTML`:
`app/{characters,blasts}/[slug]/page.tsx` (with `excludeHref`) and
`app/{mechanics,skills,transformations,patches,dlc,episode-battles,game-modes,shop,stages,guides}/[slug]/page.tsx`
(no `excludeHref`). `markdown.ts` explicitly does **not** sanitize. Content is first‑party so direct
XSS risk is low, but: (a) the bug in §A injects *stray* markup (headings/links/code) into prose; and
(b) any enrichment‑derived string that reaches a body (e.g. datamined names with `<`/`>` or raw HTML)
is emitted verbatim. *Fix:* run output through a sanitizer (e.g. `marked` + DOMPurify on the server,
or `rehype-sanitize`), or at least escape `<`/`>` in interpolated data. Lower priority than §A but
they share the same sink.

### C5. `schemas.ts` `confidence` silently defaults to `community`; many numerics silently null
`versionMetaShape.confidence` (`:11‑14`) `.default("community")` and `sources` `.default([])`; `dp`
is `.nullable().default(null)` (`:52`); most stats are `.nullable().optional()`. A page that simply
omits `confidence` is rendered as **Community** (badge in `ui.tsx:34‑41`) with no signal that the
value was *missing* vs *deliberately community*. Likewise missing numbers render as `—`
(indistinguishable from "datamined as N/A"). For a provenance‑first wiki this masks data gaps. *Fix:*
make `confidence` required for fact pages (or add an `unknown` sentinel that the UI flags), and
distinguish "absent" from "null".

### C6. `components/search.tsx` — modal a11y / focus management
The ⌘K palette (`:92‑150`) is a `<div>` overlay with no `role="dialog"`/`aria-modal`, no focus trap,
and focus is not restored to the trigger on close. ⌘/Ctrl‑K toggling and Esc work, and results are
keyboard‑navigable, so it's usable, but not accessible. Error handling and `/search-index.json`
fetch are correct (`:26‑34` falls back to `[]`). *Fix:* add dialog semantics + focus trap/restore.

### C7. `app/characters/[slug]/page.tsx:38‑44` — derived move→page links can 404
`moveHref` builds `/blasts/<slugifyName(name)>-super|-ultimate` and `/skills/<…>` from the move name
via a *local* `slugifyName` (`:30‑36`). If a move's display name doesn't slug‑match the blast/skill
page slug (naming drift, the same C1 punctuation class, or a missing override page), the link 404s on
click. Not build‑validated. *Fix:* resolve against the real slug index (reuse `getSlugIndex`) and
render plain text when there's no match (as the moveset already does for `null`).

---

# D. LOW / NIT

- **D1.** `components/ui.tsx:9‑25` `TierBadge` has no style for `D` or `unranked` (falls back to `C`);
  `tier:"unranked"` renders the label `unranked-tier`. Add `D`/`unranked` handling.
- **D2.** `components/dna-explorer` data prep `app/dna/page.tsx:93` `Math.min(...tf.map(t => t.cost ?? 99))`
  leaks the `99` sentinel as "from 99 stocks" when *all* transform costs are null.
- **D3.** `components/compare.tsx:36‑39` hard‑codes default slugs `goku-z-early`/`vegeta-z-scouter`
  (they exist today). If a regen renames them, the controlled `<select value>` won't match any option
  (blank select) while the table shows fallback `chars[0]`/`chars[1]` → state/UI mismatch. Derive
  defaults from `chars[0]/[1]`.
- **D4.** `app/dna/page.tsx:140` hard‑codes "(all 207)" while `CURRENT_VERSION.rosterSlots = 208`;
  drift‑prone string. Compute it.
- **D5.** `app/globals.css:81‑92` `.prose table { display:block; width:fit-content }` can misalign
  columns of body markdown tables (the table loses its table formatting context); the wrapping
  `overflow-x-auto` div already provides scroll, so `display:block` on the `<table>` is unnecessary.
- **D6.** Duplicate logic: `fmtPct` defined in both `lib/formulas.ts:10` and `components/ui.tsx:4`;
  the name‑index/regex builder is duplicated in `lib/linkify.tsx:18‑35` and `lib/markdown.ts`
  `autoIndex` with **divergent STOP sets** (`linkify` adds `wish`, `shop — other`). Centralize.
- **D7.** `lib/formulas.ts` (if ever used, see C3): `dmgPerKi/dmgPerDp/hpPerDp` guard with `!damage`
  so a genuine **0** returns `null` (can't distinguish "0 dmg" from "no data"); `fmtPct(0)→"—"`
  conflates "no change" with "no value". `pctChange:17` correctly guards `!oldVal` (div‑by‑zero safe).
- **D8.** `components/roster-table.tsx:85` source filter assumes `source` is exactly `"Base"` vs
  anything‑else (works for current Base/DLC data); `:98‑99` null sort uses `"˜"` as a high‑sort
  sentinel (locale‑dependent); descending tiebreak `:105` is not direction‑aware (ties always A→Z).
  All cosmetic.
- **D9.** Glossary (`app/glossary/page.tsx:27`) renders `definition` as **plain text** (no markdown,
  no wikilinks, no autolink) and never renders the glossary markdown **body** at all → any formatting
  or `[[links]]` in a glossary definition show as raw text, and body content is dead. (Upside: this
  is *why* glossary dodges §A live.)

---

# E. Review‑focus coverage notes

- **getSlugIndex / memoization (`content.ts:164‑195`).** First‑wins priority is correct and
  deterministic for a static build: collections are loaded in fixed order (characters first) and each
  `getX()` is sorted (`localeCompare`/`order`) before `add()`, so intra‑collection slug collisions
  resolve deterministically. Module‑level memos `_slugIndex` / `_idx` / `_auto` are safe (content is
  immutable at runtime). No ordering bug found. The only slug issue is `normalizeSlug` (C1).
- **Giant autolink alternation / backtracking (`linkify.tsx`, `markdown.ts`).** The regex is a single
  alternation of ~900 **literal** display names with zero‑width look‑arounds — no nested quantifiers,
  so **no catastrophic backtracking**; build cost is paid once (memoized) and is negligible. Lookbehind
  `(?<!…)` **is** supported in the Node 22 / V8 runtime. Mitigations (`length<4` skip, STOP set,
  `(?<![\w/\[])…(?![\w\]])` boundaries, longest‑first, first‑mention `seen`) are mostly sufficient,
  but case‑insensitive matching still mislinks short common‑word names ≥4 chars — **`Cell`, `Frost`,
  `Beast`, `Time`, `Broly`** etc. will autolink inside ordinary prose (`a cell of …` → link to Cell).
  Consider expanding STOP or requiring a leading capital. (MEDIUM‑LOW.)
- **Client/server boundaries (Next 16 / React 19).** Correct: all interactive components are
  `"use client"`; server detail pages `await params` (Promise) per Next 16; `ui.tsx`/`linkify.tsx`
  are server‑safe and only used in server trees; `SortableTables`/`SearchButton` are client and
  mounted in the server `layout.tsx`. No misplaced directives found.
- **generateStaticParams completeness.** All 12 dynamic routes implement it as
  `getX().map(x => ({slug: x.slug}))` — complete vs their collections (characters returns all 245
  incl. story‑only). Glossary is intentionally a single anchor page (no `[slug]`).
- **Component sort/filter correctness.** `roster/blasts/skills` tables: numeric vs string sort and
  null handling are sound (nulls sort last; `?? 99`/`?? Infinity` sentinels are above real ranges);
  React `key`s are stable (`slug`, or index for static rows). `sortable-tables` `num()` strips
  `,%$` and lone dashes, then `parseFloat` — fine for the stat columns. Main issues are a11y/ownership
  (C2), not correctness.

---

# Methodology

Because `lib/markdown.ts` trips binary detection (Read/Grep refuse it), I (a) dumped its exact source
from the build's source map and (b) reproduced `renderMarkdown` faithfully with the project's own
`gray-matter`/`marked` + a re‑implemented cross‑collection slug index, then diffed buggy‑vs‑fixed
rendering across all 908 bodies. Corruption claims were cross‑checked against the real
`.next/server/app/*.html`. Probe scripts were written under `audit/`, used read‑only, and deleted.
No `npm run build` / `gen_content.py` / `parse_data.py` / `fix_links.py` was run.
