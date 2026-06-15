# Agent 08 — Python Pipeline Code Review (`scripts/`)

**Scope:** `parse_data.py`, `gen_content.py`, `fix_links.py`, `build_enrichment.py`,
`audit.py`, `audit_v3.py`, `audit_v4.py`; compared the Python `slugify` against
`lib/content.ts normalizeSlug` and `lib/markdown.ts` wikilink resolution.
**Method:** read-only. All numbers below come from probes under `audit/a8_*.py`
(see inventory at the end) that only read `data-mined/`, `content/`, `.next/` and the
raw masterdata — no mutating script was run. The three `audit*.py` were run read-only;
**all three report CLEAN**, which is itself a finding (§HIGH-2).

> Build is green (1,144 HTML pages). No crash/blocker exists in the *current* data —
> the parser is robust against most hypothesized failures (see "Verified-OK" §). The
> real defects are (a) a live render-time dead-link bug the QA suite cannot see, and
> (b) latent correctness traps that will bite on the next data/patch change.

## Severity summary

| Severity | Count | Findings |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 2 | H1 dead `\|` cross-links (58 blast pages), H2 audits false-CLEAN |
| MEDIUM | 3 | M1 slugify⇄normalizeSlug drift, M2 dead transform stat-delta rows, M3 best_damage chip/hit loss |
| LOW | 8 | L1 playable proxy + dropped S/W, L2 dup-name collision pages, L3 search-index quote regex, L4 silent Combatives `except`, L5 revert heuristic, L6 redundant gender op, L7 zCounterType null, L8 transform double-collision drop |
| NIT | 4 | N1 hardcoded paths, N2 audit_v4 weak checks, N3 fix_links suffix guess, N4 misc |

---

## HIGH

### H1 — `gen_content` emits `[[slug\|Label]]` with an escaped pipe that `markdown.ts` cannot resolve → 58 dead blast cross-links (and every body-table link survives only via a fragile fallback)

- **Files:** `scripts/gen_content.py:414-417` (emit) ; `lib/markdown.ts:67-75` (resolver) ; `lib/content.ts:156-158` (`normalizeSlug`)
- **Problem:** The blast "sibling" cross-link is emitted as

```414:417:scripts/gen_content.py
        if sibling:
            body_lines.append(
                f"- Also exists as a separate **{other_class}** for other fighters: [[{sibling}\\|{b['name']} ({other_class})]]"
            )
```

  i.e. literal markdown `[[...-ultimate\|Super Kamehameha (ultimate)]]`. The renderer's
  wikilink regex is `/\[\[([^\]|]+)(?:\|([^\]]+))?\]\]/g` (`lib/markdown.ts:67-75`). The
  character class `[^\]|]` excludes `]` and `|` **but not `\`**, so the capture group
  swallows the backslash: `target = "super-kamehameha-ultimate\"`. `normalizeSlug`
  (lib/content.ts:156-158) only does `trim+lower+\s+→-` and keeps the backslash, so the
  key `"super-kamehameha-ultimate\\"` is never in the slug index → the link degrades to
  plain text. The separate `autolink` pass cannot rescue it: the visible label
  `"Super Kamehameha (ultimate)"` is not a page name, and its bare-name substring
  `"Super Kamehameha"` maps to the *current* page, which `autolink` skips via
  `excludeHref` (`lib/markdown.ts:58`).
- **Repro (verified in built HTML):** `node` confirms the regex captures
  `target:"android-13\\"` for `[[android-13\|Android 13]]`. Built page
  `.next/server/app/blasts/super-kamehameha-super.html` line 4:
  `…for other fighters: Super Kamehameha (ultimate)</li>` — **plain text, no `<a>`**.
  Probe `a8_sibling_scan.py`: **58 of 58** blast sibling cross-links render dead
  (`0` linked), e.g. `big-bang-attack-super`, `dragon-fist-ultimate`,
  `black-kamehameha-super`, …
- **Why it isn't caught:** these render as plain text (no `href`), so the built-HTML
  dead-href scans in `audit_v3`/`audit_v4` see nothing, and `audit.py`/`fix_links.py`
  strip the backslash (see H2).
- **Secondary blast radius:** the same `\|` form is emitted in skill user tables
  (`gen_content.py:511-518`) and transformation From/To prose
  (`gen_content.py:702-704`). Those *happen* to survive because `autolink` re-links the
  label text (the label there **is** the target's page name) — but only the
  **first mention per name** and only when the label exactly equals a page name. Any
  custom label, repeated mention, or `excludeHref` collision silently dies.
- **Fix:** The sibling link is in a **bullet list, not a GFM table**, so the `\|` escape
  is unnecessary there — emit a plain pipe: `[[{sibling}|{b['name']} ({other_class})]]`.
  The robust fix is in the renderer: change `lib/markdown.ts` to `[[([^\]|\\]+)` (exclude
  backslash) so the documented table-escape `\|` resolves everywhere. (Coordinate with
  Agent 9.)

### H2 — The QA suite reports CLEAN while H1 (and the slug drift) is present — `audit*.py` model link resolution differently from the real renderer

- **Files:** `scripts/audit.py:29,32-37` ; `scripts/fix_links.py:32,38-43` ; `scripts/audit_v3.py:54-77` ; `scripts/audit_v4.py:62-74`
- **Problem:** None of the audits replicate `markdown.ts`'s actual resolution
  (`normalizeSlug` applied to a target that still contains the `\`):
  - `audit.py:29` uses `wl = re.compile(r"\[\[([^\]|\\]+)")` — this **excludes** `\`, so
    for `[[goku-super\|Goku (Super)]]` it extracts the clean target `goku-super`, finds
    it in `slug_set`, and reports healthy. The renderer keeps the `\` and fails.
  - `fix_links.py:32` uses the identical backslash-excluding regex.
  - `audit_v3.py:54-58` defines its **own** copy of gen's `slugify` and checks moveset
    links against the file set — it validates gen-internal slug consistency, never the
    renderer's `normalizeSlug`.
  - `audit_v3.py:135-156` / `audit_v4.py:62-74` scan **built HTML for dead `href=`** —
    but H1's links render as plain text (no `href`), so they are invisible.
- **Repro:** `python scripts/audit.py` → `=== wikilinks: 2591 total, 1 broken` →
  `AUDIT CLEAN`; `audit_v3` → `CLEAN`; `audit_v4` → `CLEAN`. Yet 58 cross-links are dead
  (H1) and 127 character pages are unreachable by display name (M1). The single "broken"
  link is `super-17`, which `audit.py:40` deliberately skips.
- **Impact:** the audit suite gives false confidence; a real wikilink regression in the
  renderer or a `\|`-form link can ship green.
- **Fix:** add a check that resolves wikilinks **exactly** as `markdown.ts` does
  (`normalizeSlug(rawTargetIncludingBackslash)` against the slug index, then the
  `autolink`/`excludeHref` fallback), and assert that body-emitted sibling links appear
  as `<a>` in the rendered HTML.

---

## MEDIUM

### M1 — `slugify` (gen) vs `normalizeSlug` (TS) drift: 127/245 character pages unreachable by a naive `[[Display Name]]` link; "Rosé" loses its `é`

- **Files:** `scripts/gen_content.py:37-41` vs `lib/content.ts:156-158`
- **Problem:**

```37:41:scripts/gen_content.py
def slugify(s: str) -> str:
    s = s.lower()
    s = re.sub(r"['’!.]", "", s)
    s = re.sub(r"[^a-z0-9]+", "-", s)
    return s.strip("-")
```

  strips `'’!.`, collapses every non-alphanumeric run (including parentheses, commas,
  colons, `&`, `/`, accented letters, `→`) to `-`. `normalizeSlug` strips **nothing** —
  only `trim+lower+\s+→-`. So the file slug and the slug a wikilink produces from the
  display name diverge for any punctuated/accented name. (`audit_v3.py:54-58` and
  `fix_links.py` each carry yet another copy of the gen logic — four slug functions,
  three different behaviors.)
- **Quantified (probe `a8_slug_drift.py` / `a8_final_probe.py`):**
  - **419** page display-names where `slugify(name) != normalizeSlug(name)`
    (parens 239, comma 203, non-ascii 192, `!` 32, `.` 26, apostrophe 25, `&` 14, `/` 5, `:` 3).
  - **127 of 245 character pages** are unreachable via `[[exact display name]]`
    (parens 100, comma 71, period 6, non-ascii 1). All 453 blasts and 164 transformations
    are likewise unreachable by their display name (compounded by the class/`→` suffixes).
  - **Silent data corruption in a slug:** `"Goku Black, Super Saiyan Rosé"` →
    `slugify` → **`goku-black-super-saiyan-ros`** (the `é` is dropped, not transliterated),
    so the page and `transformations/goku-black-to-goku-black-super-saiyan-ros.md` carry a
    truncated slug; `[[…Rosé]]` → `…-rosé` never matches.
  - Concrete examples: `Android 17 (Z)`→file `android-17-z` vs link `android-17-(z)`;
    `Cell, 1st Form`→`cell-1st-form` vs `cell,-1st-form`; `Dr. Gero`→`dr-gero` vs `dr.-gero`;
    skills `Behave Yourself!`→`behave-yourself` vs `behave-yourself!`; `Hero's Flute`→`heros-flute` vs `hero's-flute`.
- **Current status — LATENT (be honest):** content authors used **slug-form** targets, so
  after stripping the `\` the only genuinely-broken link today is `super-17`
  (probe `a8_final_probe.py` §3). `autolink` also re-links plain-text mentions. So this
  is not currently mass-breaking — but it is a real footgun: the "type the page's name in
  `[[ ]]`" affordance silently fails for 2/3 of the corpus, and one wrong-target already
  exists: `[[Energy Blast]]` → `normalizeSlug` `energy-blast` → resolves to the glossary
  alias `/glossary#ki-blast`, not the blast page.
- **Fix:** make `normalizeSlug` mirror `slugify` (strip the same `'’!.` and collapse
  punctuation), or have the generator register display-name → slug aliases in the slug
  index (and transliterate accents, e.g. `é→e`, instead of dropping them).

### M2 — Transformation "Exact stat changes" silently omits both sparking-gauge rows (delta_row reads keys that don't exist)

- **File:** `scripts/gen_content.py:637-647`
- **Problem:** the delta table calls:

```637:647:scripts/gen_content.py
        delta_row(
            "Sparking gauge charge",
            cf.get("sparkingGaugeChargeSpeed"),
            ct.get("sparkingGaugeChargeSpeed"),
        )
        delta_row(
            "Pre-Sparking gauge decay",
            cf.get("preSparkingGaugeDecreaseSpeed"),
            ct.get("preSparkingGaugeDecreaseSpeed"),
            "/s",
        )
```

  but `characters.json` has **no** `sparkingGaugeChargeSpeed` or
  `preSparkingGaugeDecreaseSpeed` keys — `parse_data.py:333` emits the sparking field as
  **`sparkingDrainPerSec`**. `delta_row` (gen_content.py:614-616) returns early when
  either side is `None`, so both rows are **always** dropped.
- **Repro (probe `a8_transform_probe.py`):** `sparkingGaugeChargeSpeed`/
  `preSparkingGaugeDecreaseSpeed` present in `characters.json` = **False/False**;
  transformation pages rendering a "Sparking gauge charge" row = **0 / 164**;
  "Pre-Sparking gauge decay" row = **0 / 164**.
- **Impact:** dead code masquerading as a feature; the promised sparking-gauge before→after
  delta never appears on any transformation page.
- **Fix:** use the real key (`sparkingDrainPerSec`) and add a parser field for the
  charge-speed if a charge delta is actually intended; otherwise delete the two calls.

### M3 — `best_damage` can surface a melee number as the headline "damage" and drop the move's chip/hits; multi-bullet moves collapse to one bullet

- **File:** `scripts/gen_content.py:160-176`
- **Problem:** it takes `max(beamPower, power)` across bullets, then if any
  `combatives.meleePowers` value exceeds it, **overrides** `dmg` and sets `chip=None`,
  `hits=None`:

```171:176:scripts/gen_content.py
        melee = [p for p in (move.get("combatives") or {}).get("meleePowers", []) if p]
        if melee and (dmg is None or max(melee) > dmg):
            dmg = max(melee)
            chip = None
            hits = None
        return dmg, chip, hits
```

  Mixing per-action melee `Power` with beam projectile `Power`/`BeamPower` means a heavy
  melee startup value can become the displayed "damage" of a beam super, discarding the
  beam's datamined chip and multi-hit. For a multi-bullet move only the single strongest
  bullet's dmg/chip/hits is kept.
- **Repro (probe `a8_bestdmg.py`):**
  - `0031_01` *Raging Masenko*: beam dmg **500** / chip **100** → overridden by melee
    **10,500**, chip+hits dropped.
  - `0022_62` *God Shine Attack*: beam dmg **600** / chip **96** → overridden by melee
    **3,900**, chip dropped.
  - 3 moves have >1 datamined bullet, collapsed to the max bullet only.
- **Impact:** headline damage/chip on those pages misrepresents the move; low volume but
  it is presented as `[datamined]`.
- **Fix:** keep beam vs melee as separate fields (e.g. `beamDamage` + `meleeDamage`), or
  do not null `chip`/`hits` when a melee value wins.

---

## LOW

### L1 — `playable = bool(e)` is a proxy ("matched a research DP row"); sw_a/sw_b S/W only merge into already-enriched cids
- **File:** `scripts/gen_content.py:301` ; merge at `:109-125`
- `playable` = "this cid has any merged enrichment entry" = "build_enrichment matched it to
  a row in research/02". Currently exactly **208/208** (probe `a8_gen_probe.py`: enrich=208,
  playable:true=208, 0 enrich cids missing from chars, 0 unnamed). **But** a genuinely
  playable fighter absent from the research DP table would be marked `playable:false`
  (dropped from the roster), and a system/NPC cid that fuzzy-matched a DP row would be
  marked playable. Also the sw_a/sw_b loop (`:113 if cid in enrich`) only *updates*
  existing enrich cids — a fighter present in `sw_*.json` but **not** in
  `enrichment/characters.json` would have its strengths/weaknesses/how-to-fight silently
  dropped (0 today: sw_a 120 + sw_b 88 = 208, all in enrich). Fragile coupling; consider an
  intrinsic flag (e.g. `hasNumeric`/roster table) for playability.

### L2 — Slug-collision suffixing is correct, but two fighters share a display name; the suffixed page is unreachable by name
- **File:** `scripts/gen_content.py:154-158`
- The `-{cid}` suffix prevents file overwrite (good, no data loss). But probe
  `a8_gen_probe.py`/`a8_bestdmg.py` show `Goku (Super)` = {`goku-super` (0000_40),
  `goku-super-0000-44` (0000_44, `fullName:null`)} and `Vegeta (Super)` =
  {`vegeta-super` (0020_60), `vegeta-super-0020-64` (0020_64, `fullName:null`)}. Both
  members carry the identical `name`, so `[[Goku (Super)]]`/autolink always resolve to
  the first (0000_40); the suffixed page is reachable only by its literal slug. Worth a
  distinguishing display name (the underlying data has none for 0000_44/0020_64).

### L3 — search-index title regex breaks on names containing a quote
- **File:** `scripts/gen_content.py:845-848` (`fm_field`), used at `:859`
- `…:\s*"?([^"\n]+)"?\s*$` stops the value at the first `"`. For the JSON-escaped name
  `"\"No Hard Feelings\" Hit"` the match fails and the builder falls back to `f.stem`.
  Probe `a8_gen_probe.py`: search entry `/blasts/no-hard-feelings-hit-super` has
  `t="no-hard-feelings-hit-super"` (slug, not the real title). 1 page affected.
  `int(float(fields['hp']))` (`:872`) is a latent `ValueError` if `hp` were ever
  non-numeric — safe today (hp is always an int for characters). Hrefs are unique by
  construction, so the missing dedup is harmless (audit_v4 confirms 0 dup hrefs).

### L4 — `parse_data` swallows Combatives parse failures silently
- **File:** `scripts/parse_data.py:201-204` (`try: load(f) / except Exception: continue`)
- Probe `a8_parse_probe.py`: **0/212** Combatives files fail today, so no data is lost
  now — but a future malformed/renamed file would drop that character's entire melee
  override set (`Power`/`ArmorBreakLevel`/…) with **no warning**. Log the exception and
  count, don't `continue` blindly.

### L5 — Revert heuristic could mislabel a free forward transform as a "revert" and drop it
- **File:** `scripts/parse_data.py:386-389`
  (`resolved_kind = "revert" if kind=="transform" and stock==0 and same_base else kind`)
- Probe `a8_parse_probe.py`: 43 reverts, **0** with a higher target form-code, **0**
  crossing base id — correct for current data. The risk is structural: the rule assumes
  *free + same base = backward*. A future free same-base power-up (auto/passive transform)
  would be tagged `revert` and excluded from `transformsTo` and from page generation. Use
  the actual change direction rather than "free + same base".

### L6 — Redundant (and crash-prone) gender extraction
- **File:** `scripts/parse_data.py:368-372`
- `story.get("Gender") or rec.get("StorySettingParameter", {}).get("Gender")` — the second
  operand is identical to the first (since `story = rec.get("StorySettingParameter") or {}`)
  and would raise `AttributeError` if `StorySettingParameter` were explicit `null`
  (`.get(...,{})` returns `None`, not `{}`, when the key exists with a null value). Probe
  `a8_misc_probe.py`: 294 dicts, 0 null → no crash today. Drop the dead second operand.

### L7 — `zCounterType` ternary crashes on a present-but-null `SuperZCounterType`
- **File:** `scripts/parse_data.py:292-297`
- `(asset.get("BlastSkillParamData") or {}).get("SuperZCounterType", "").split("::")` — if
  the key is present with value `null`, `.get(...,"")` returns `None` → `None.split` →
  crash. Probe `a8_gen_probe.py`: **0** null values today (always `EKorat…::Repel/Erase`),
  so safe now. Guard with `(… .get("SuperZCounterType") or "")`.

### L8 — Transformation double slug-collision is dropped silently; 1 edge lost to a missing name
- **File:** `scripts/gen_content.py:544-548`
- On a second slug collision the loop does `continue` (page silently skipped). Probe
  `a8_transform_probe.py`: 0 double-collisions today. Separately, 1 non-revert edge
  (`0003_51 → 0000_43`, Goku SSGSS) is dropped because the source cid is unnamed
  (`fromName=None`) — minor, but it is silent.

---

## NIT

- **N1 — Hardcoded absolute paths** in every script (`parse_data.py:32-33`,
  `gen_content.py:20`, `fix_links.py:6`, `build_enrichment.py:31-34`, `audit*.py:8-9`):
  `C:\vaults\sparking_zero` is baked in. By design (per CLAUDE.md) but non-portable;
  derive from `Path(__file__).resolve().parents[1]`.
- **N2 — audit_v4 weak checks:** the skill-cost cross-check (`audit_v4.py:143-145`) only
  matches blast1 moves that emit a `skillCost` line — **141 of 416** blast1 moves
  (probe `a8_gen_probe.py`); the other 275 are uncovered. The HP-tier-count check
  (`:114-117`) only emits a `note`, never an `issue`, and didn't match the page wording
  ("does not show counts pattern") — effectively disabled.
- **N3 — fix_links suffix guessing:** `resolve()` (`fix_links.py:22-29`) maps a bare name to
  `-super` before `-ultimate` and returns the first hit, so `[[kamehameha]]` is always
  "fixed" to the super even when the ultimate was meant. `len(hits) >= 1` is just `if hits`.
- **N4 — Style:** `gen_content.py` reuses the name `cats` for an inner `Counter`
  (`:361`) and an outer `defaultdict(list)` (`:757`); `build_enrichment.py` matching is
  order-dependent and two branches (`:430-432`) assign a cid without checking `used_ids`,
  so a cid could be enriched twice (last write wins) — static observation, not reproduced.

---

## Verified-OK (checked, no bug — reported to bound the audit)

- **`yml()`/`scalar()` falsy handling is correct** (`gen_content.py:50-52,72-80`): only
  `None`/empty-list/empty-dict are dropped; **`0`, `False`, `""` are preserved**
  (`0`→`0`, `False`→`false`, `""`→`""`). All string paths go through `scalar()` →
  `json.dumps`, so `:`, `#`, leading specials, embedded quotes and newlines are correctly
  escaped and round-trip through the YAML reader.
- **`audit_v3` userCount is NOT off-by-one** (`audit_v3.py:161-170`): the capture group
  `((?:  - .*\n)+)` excludes the `users:` header line, so `len(splitlines())` == user count.
- **`parse_data` field mappings are correct** (probe `a8_parse_probe.py`, 10/10 spot-check):
  `Life→hp`, `SPChargeSpeed→kiChargeSpeed` (0 for androids, e.g. Android 13 = 0.0),
  `SPAutoRecoverySpeed→kiAutoRecovery`, `InitialSP→initialKi`, `BlastStock→maxSkillStock`,
  `SparkingModeGaugeDecreaseSpeed→sparkingDrainPerSec` (2,800), `BulletNum→kiBlastShots`.
- **`props(entry)` is safe** (`parse_data.py:41-44`): all masterdata top-level values are
  non-empty lists (probe `a8_parse_probe.py`), and the `if not entry` guard handles
  empty/None; `entry[0]` never crashes in current data.

---

## Slugify-drift link-breakage — quantified summary (deliverable §1)

| Metric | Value | Probe |
|---|---|---|
| Page display-names where `slugify(name) ≠ normalizeSlug(name)` | **419 / 1153** | a8_slug_drift |
| — by cause | parens 239, comma 203, non-ascii 192, `!` 32, `.` 26, `'` 25, `&` 14, `/` 5, `:` 3 | a8_slug_drift |
| Character pages unreachable via `[[exact display name]]` | **127 / 245** (parens 100, comma 71, `.` 6, é 1) | a8_final_probe |
| Pages reachable via `[[name]]` (whole corpus) | **304 / 1153** | a8_slug_drift |
| `[[name]]` that resolves to the WRONG page | **1** (`Energy Blast` → `/glossary#ki-blast`) | a8_final_probe |
| Accent dropped in a real slug | `Rosé` → `…-ros` (é deleted) | a8_slug_drift |
| **Live** dead cross-links from the `\|` mechanism (H1) | **58 / 58** blast siblings | a8_sibling_scan |
| Genuinely-broken links *today* (slug-form targets, `\` stripped) | **1** (`super-17`, intentional) → drift is LATENT | a8_final_probe |

**Bottom line on §1:** two distinct mechanisms break wikilinks. (a) The **`\|` backslash**
issue (H1) is *live* and user-visible — 58 dead blast cross-links — because `markdown.ts`'s
regex keeps the backslash and the `autolink` fallback can't recover a non-page-name label
on its own page. (b) The **punctuation/accent drift** (M1) between `slugify` and
`normalizeSlug` is *latent* (authors wrote slug-form targets, and `autolink` covers
plain-text mentions) but leaves 127 character pages — and effectively the whole
blast/transformation corpus — unreachable the moment anyone writes `[[Display Name]]`, and
already mis-routes `[[Energy Blast]]`. Both are invisible to `audit*.py` (H2).

## Probe inventory (all read-only, under `audit/`)
- `a8_slug_drift.py` — slugify vs normalizeSlug divergence, reachability, real-link scan
- `a8_parse_probe.py` — Combatives load test, field-mapping spot check, revert heuristic, props shapes
- `a8_gen_probe.py` — playable/enrich/sw merge, search-index titles, blast1 skillCost coverage, zCounterType nulls, dup-name collisions
- `a8_bestdmg.py` — collision cids + best_damage chip/hit loss
- `a8_transform_probe.py` — transform slug-collision drops + dead stat-delta fields
- `a8_misc_probe.py` — gender-null crash risk, cooldown `—s`, missing-name edge
- `a8_sibling_scan.py` — counts dead vs linked blast sibling cross-links in built HTML
- `a8_final_probe.py` — wrong-target, pure-punctuation character count, latency confirmation
