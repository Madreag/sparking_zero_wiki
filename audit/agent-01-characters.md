# Agent 01 — Characters: Data Accuracy & Integrity Audit

**Scope:** all 245 `content/characters/*.md` (208 playable + 37 system/NPC).
**Date:** 2026-06-15 · **Corpus version:** v2.2 (2026-05-26 update) · **Method:** read-only.
**Source of truth (priority):** `data-mined/raw/masterdata/*.json` → `data-mined/characters.json`
→ `data-mined/enrichment/{characters,sw_a,sw_b}.json`. Online sources NOT trusted for numbers.

**Probes (all read-only, written by this agent, runnable with `python`):**
`audit/a1_probe.py` (full field-by-field page↔data diff), `audit/a1_probe2.py` (dropped
moves / distributions), `audit/a1_probe3.py` (prose-number vs frontmatter), `audit/a1_probe4.py`
(hpInherited ambiguity), `audit/a1_trace.py` (16-cid raw→json→page trace). Machine output cached
in `audit/a1_out.json`.

---

## TL;DR

**The datamined numbers are accurate.** Across **3,675 numeric field comparisons, 245 movesets,
163 transform edges, and 16 hand-traced cids to raw `Numeric.json`, I found ZERO incorrect
datamined values.** Every HP / ki-economy / skill-gauge / move-cost / damage figure on every page
equals `characters.json`, which equals the raw `Numeric.json`/`BulletSetting`/`Combatives`. There
are **no BLOCKERs and no fabricated numbers.**

The findings are about **provenance honesty, missing data, and two fighters whose supers were
silently dropped** — not about wrong numbers.

| Severity | Count | Headline |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 2 | (1) `confidence: "datamined"` stamped on all 245 pages incl. community DP/tier/S-W; (2) Krillin & Frost render **zero Blast 2 supers** |
| MEDIUM | 3 | (3) 20 playable fusions/giants show **no HP**; (4) Gohan Beast inherits wrong HP + "null HP" prose; (5) stale HP sanity-anchor in CLAUDE/PLAN/README |
| LOW | 1 | (6) 83 strengths/weaknesses bullets reused verbatim across unrelated fighters |
| NIT | 2 | (7) `kiBlastShots: 999` literal on 22 fighters; (8) duplicate display names on 2 non-playable stubs |

---

## Coverage summary

| Check | What was compared | Volume | Mismatches |
|---|---|---|---|
| 1. Numeric frontmatter | hp, kiChargeSpeed, kiAutoRecovery(+Limit), initialKi, max/initialSkillStock, sparkingDrainPerSec, kiBlastShots vs `characters.json` | 1,960 top-level + 1,715 skillGaugeGains = **3,675** | **0** |
| 2. Moveset fidelity | blast1/blast2/ultimate name·kiCost·damage·hits·skillCost vs supers[]/ultimate/s1Skills[] | 245 movesets; 412 supers, 416 S1, 619 super+ult ki-cost rows; 83 datamined-damage rows | **0** page↔data mismatches (but see HIGH-2: 4 real supers dropped upstream) |
| 3. transformsTo | target·targetSlug·cost·kind vs formChanges+fusions; targetSlug resolves to a real page | 96 pages, **163 edges** | **0** dangling/missing slugs; **0** cost/kind errors |
| 4. DP | present on all playable; plausible range | 208 playable | **0** missing, **0** out-of-range (range 1–10). Provenance honesty → HIGH-1 |
| 5. playable count | enumerate playable vs system/NPC | 208 playable / 37 non-playable | **0** misclassified |
| 6. hpInherited | resolved-HP + inherited flag vs sibling forms | 245 (4 inherited) | **0** flag errors vs generator; 1 questionable heuristic result (MEDIUM-4) |
| 7. Raw trace | raw `Numeric.json`/`CharacterData.json` → `characters.json` → page | **16 cids** | **0** — all faithful |
| 8. S/W prose | duplication + numbers-vs-moveset | 100 recovery + 64 charge + 224 HP + DP claims | **0** numeric contradictions; 83 verbatim-duplicate groups (LOW-6) |
| 9. sparkingDrain | =2,800 uniform; never described as a vanish cost | 245 | **0** non-2800; **0** vanish-cost mislabels |

Field-level numeric accuracy is therefore **100%** against the datamine. The corpus's "numbers-first"
promise is met for the data it has; the gaps below are about data it *lacks* or *mis-labels*.

---

## Findings (severity-ranked)

### HIGH-1 — `confidence: "datamined"` is hardcoded on all 245 character pages, but every playable page also carries community-sourced DP, tier, era, and the entire strengths/weaknesses layer
**Where:** `scripts/gen_content.py:310` (`"confidence": "datamined",`) → every `content/characters/*.md:confidence`.
**Evidence (the contradiction is self-documented on the page):** all **208/208** playable pages
simultaneously have a `dp:` value, `confidence: "datamined"`, **and** list
`"research/02-roster-dp-dlc.md (Game8/Fandom DP tables)"` in `sources`. Example —
`content/characters/goku-z-early.md:7` `dp: 4`, line `78` `confidence: "datamined"`, line `81`
the Game8/Fandom DP source. Same pattern on `android-13.md`, `frost.md`, `krillin.md`, etc.
**Why it's wrong:** the project's own rules are explicit and emphatic —
> "DP cost is not in the game files — community-sourced … Tag it `community`, never `datamined`." (`CLAUDE.md:43`)
> "Cite confidence honestly. `datamined` only for values straight from game files." (`CLAUDE.md:88`)

The page leads with DP (a community number) and is dominated by community/agent content
(`era`, `tier`, `classes`, `playstyle`, `strengths`, `weaknesses`, `howToFight`, `summary`), yet
the single page-level provenance stamp claims `datamined`. This is the exact "honesty tension" the
audit calls out, and it is **systemic** (the same `confidence: "datamined"` hardcode also stamps
blasts/skills/transformations/stages/shop — flag for Agents 2/3/10).
**Recommended fix (generator):** in `gen_content.py`, stop hardcoding `"datamined"` for the
character front-matter. Options, best first: (a) set page `confidence` to `community` (the schema
default) because the page mixes datamined stats with community DP/tier/S-W; (b) keep `datamined`
only for the stat block and add an explicit per-field/inline note that DP, tier, era and S/W are
`community`; (c) at minimum, never emit `datamined` on a page whose `sources` include a
`research/*` community brief. Note: the **numbers themselves are correct** — this is purely a
mislabeled provenance, but it is a labeled-as-truth overclaim the rules forbid.

---

### HIGH-2 — Krillin and Frost display **zero Blast 2 supers**, though each has two datamined 30,000-ki supers
**Where:** `content/characters/krillin.md:24-44` (moveset = S2 Afterimage Strike, S1 Solar Flare,
ULT Chain Destructo Disc — **no `blast2`**); `content/characters/frost.md:25-41` (S2 Welcome to My
World, S1 Explosive Wave, ULT Chaos Ball — **no `blast2`**).
**Root cause (traced to raw):** in `characters.json`, both `0050_00` and `0881_00` have two
`supers[]` entries with `kiCost: 30000` and datamined categories (Krillin: `None`/`Simultaneous
Fire`; Frost: `Beam`/`Rush`) **but `name: null`**. The raw `BlastSkill1/2_<cid>` assets *exist*,
but the locres keys `ST_BLASTSKILL_<cid>_actSPM1/SPM2` are missing (verified in `a1_trace.py`:
`asset_present=True, locres_name=None`). `gen_content.py:203-205`
(`for s in c["supers"]: if not s["name"]: continue`) then silently drops every nameless super, so
both fighters lose their entire Blast 2 tier from the structured moveset.
**Reader-visible inconsistency:** `frost.md:47` strengths claim *"Two 30,000-ki supers (one
speed-impact at 15,000 trigger)"* and `frost.md:54` summary says *"twin 30k-ki supers"* — but the
moveset shows none. Krillin's signature Destructo Disc super is likewise absent (only the ultimate
"Chain Destructo Disc" survives).
**Scope:** exactly 4 dropped super entries across 2 playable fighters (full list from
`a1_probe2.py §A`). No ultimates affected; no other fighter has 0 supers.
**Recommended fix:** (a) **parser/generator** — when a super/ult has a real asset + `kiCost`/
`category` but no resolved name, emit a fallback label (e.g. category-derived `"Beam Super (SPM1)"`
or the asset key) instead of dropping it, so the datamined ki cost/category still render; and/or
(b) **enrichment** — backfill the 4 names (community-known: Krillin = Destructo Disc / Scattering
Energy Wave; Frost = Chaos Strike / similar) tagged `community`; (c) add a parser warning that lists
"named asset present, locres name missing" so this gap is visible at parse time.

---

### MEDIUM-3 — 20 playable fusions/giants render **no HP at all** (numbers-first gap on marquee fighters)
**Where:** front-matter has no `hp:` line on these 20 playable pages:
`gogeta-super` (0110_00), `gogeta-super-super-saiyan` (0110_01), `gogeta-gt-super-saiyan-4`
(0110_02), `gogeta-super-super-saiyan-god-super-saiyan` (0110_03), `super-gogeta-z` (0110_04),
`vegito` (0100_00), `super-vegito` (0100_01), `vegito-super-saiyan-god-super-saiyan` (0100_02),
`kefla` (0920_00), `kefla-super-saiyan` (0920_01), `kefla-super-saiyan-2` (0920_02),
`cell-max` (3040_00), `hirudegarn` (0670_00), `janemba` (0650_00), `jiren-full-power` (0931_00),
`toppo-god-of-destruction` (0941_00), `anilaza` (1500_00), `great-ape-baby-gt` (0681_00),
`lord-slug-giant-form` (0591_00), `orange-piccolo-giant-form` (3012_00).
**Root cause (traced to raw):** the raw `Numeric_<cid>` asset **omits `Life`** for these fighters
(verified for Kefla/Cell Max/Hirudegarn/Gogeta/Vegito in `a1_trace.py` — `Life=None`, while
SPChargeSpeed/SparkingModeGaugeDecreaseSpeed are present). `gen_content.py`'s HP fallback
(`resolved_hp`, lines 139-145) can't inherit because **no** form in the baseId group has a `Life`
either. The parser is faithful (null in, null out); this is a genuine datamine gap — the game
likely resolves fusion/giant HP at runtime.
**Why it matters:** these include the most-picked fighters in the game (Gogeta, Vegito, Kefla) and
every giant. The prime directive is "every page leads with numbers"; here the headline number is
blank. Not a *correctness* error (no wrong value shown), hence MEDIUM not HIGH.
**Recommended fix:** add community HP to `enrichment/characters.json` for these 20 cids (tag
`community`; in-game/community value is 40,000 for the fusions, larger for giants), **or** have
`gen_content.py` print an explicit "HP not serialized for fusions/giants (runtime-inherited)" note
in the body instead of an empty stat.

---

### MEDIUM-4 — Gohan Beast inherits the **wrong** sibling HP (35,000) and its prose says "null HP"
**Where:** `content/characters/gohan-beast.md` → `hp: 35000`, `hpInherited: true`.
**Evidence:** `gohan-beast` is `3000_03` with `data.hp = null`. `resolved_hp` inherits from the
**lowest-formCode** sibling because `groups[...]` is sorted by formCode (`gen_content.py:135`,
returned at `142-144`). Siblings: `3000_00`/`3000_01` Gohan (Super Hero) = **35,000**, `3000_02`
Ultimate Gohan = **40,000**. Gohan Beast **transforms from Ultimate Gohan (40,000)**, so inheriting
the base form's 35,000 is the less-defensible guess for the franchise's strongest Gohan form.
Compounding it, the enrichment `summary` says *"giant-ish (null HP)"* — which contradicts the
displayed `hp: 35000`. (Gohan Beast is a top-meta pick: its own summary cites "#10 Singles, #1 DP".)
**Recommended fix:** in `resolved_hp`, prefer the HP of the **transform-source form** (or the
highest-HP sibling) rather than the lowest formCode; or enrich `3000_03` HP explicitly; and fix the
"null HP" wording in `sw_*`/enrichment now that a value is shown. Only 4 pages use `hpInherited`
(the other 3 — `goku-super-ultra-instinct`, plus non-playable stubs `goku-super-0000-44`,
`vegeta-super-0020-64` — inherit unambiguously from all-40,000 siblings).

---

### MEDIUM-5 — Stale HP sanity-anchor counts in CLAUDE.md / PLAN.md / audit README
**Where:** `CLAUDE.md:45`, `PLAN.md:90`, `audit/README.md:14` all state HP tiers
**"30/35/40/45k = 9 / 14 / 147 / 16 fighters"**.
**Evidence (current data):** actual **playable** distribution is **30k:9 / 35k:15 / 40k:148 /
45k:16** (188 fighters with HP), per `a1_probe2.py §F`. The anchor is off by +1 at 35k and +1 at
40k, and — more importantly — it implies *every* fighter falls in one of the four tiers, hiding the
**20 playable fighters with no datamined HP** (MEDIUM-3). The audit README is the shared ground
truth for all 10 agents, so a wrong anchor can cause other agents to mis-flag.
**Recommended fix:** update the three docs to "9 / 15 / 148 / 16 (188 with HP; 20 fusions/giants
have no serialized HP)".

---

### LOW-6 — 83 strengths/weaknesses/howToFight bullets are reused verbatim across unrelated fighters
**Where:** `enrichment/sw_a.json` + `sw_b.json` → `strengths`/`weaknesses`/`howToFight` on many pages.
**Evidence (`a1_probe.py` dup analysis, top groups):**
- "No heal/regen — fixed effective durability once committed" — **53** fighters
- "No auto-dodge/evasion skill — active defense is Super Counter only" — **50**
- "Average 1,750 recovery, no teleport" — 18 · "No transform path — fixed kit…" — 18
- "Explosive Wave knockback/ki-shield reset" — 21 · "Super Kamehameha (30,000-ki super)" — 14 · …
**Important — I verified these are factually CONSISTENT, not wrong:** every reused bullet that
names a move (Kamehameha, Wild Sense, Solar Flare, Afterimage Strike, …) was checked against that
fighter's actual kit → **0 fighters claim a move they lack** (`a1_probe2.py §E`; the one apparent
hit, `goku-z-mid` "Kamehameha", is a substring of its real "x20 Kaioken Kamehameha"). Every reused
bullet carrying a hard number (1,750 recovery, 8.0 charge, 35,000 HP, DP, ki costs — 388 numeric
claims) matches that fighter's own frontmatter → **0 contradictions** (`a1_probe3.py`). So this is an
**editorial/quality** issue (generic, repetitive prose; brittle if a fighter is rebalanced), not a
data error. Severity LOW for that reason.
**Recommended fix (optional):** treat these as explicit derived tags generated from the stat block
at gen time (so they auto-update), or diversify wording. No urgent action.

---

### NIT-7 — `kiBlastShots: 999` shown as a literal on 22 fighters
**Where:** 22 pages incl. most Vegeta forms, Toppo (0940/0941), Gamma 1/2 (3020/3030), Vegeta
Mini/DAIMA. **Faithful** to raw `Numeric.BulletNum: 999` (verified Gamma 1 / Vegeta DAIMA in
`a1_trace.py`). 999 reads as the game's "uncapped / continuous volley" sentinel.
**Recommended fix (optional):** render 999 as "∞ (continuous)" with a note rather than a bare
"999", to avoid looking like a data glitch.

### NIT-8 — Two non-playable stubs duplicate real fighters' display names
**Where:** `goku-super-0000-44.md` "Goku (Super)" and `vegeta-super-0020-64.md` "Vegeta (Super)"
are empty stubs (`hasNumeric=False`, no moveset) sharing names with the real playable
`goku-super` (0000_40) / `vegeta-super` (0020_60). Correctly non-playable and slug-disambiguated
(no link collision), but the duplicate human-readable names can confuse search. Low/no action.

---

## Check-by-check detail

**Check 1 (numeric frontmatter) — PASS, 0/3,675.** Every `hp, kiChargeSpeed, kiAutoRecovery,
kiAutoRecoveryLimit, initialKi, maxSkillStock, initialSkillStock, sparkingDrainPerSec, kiBlastShots`
and all 7 `skillGaugeGains` entries equal `characters.json[cid]`. The generator copies these
straight through; `None` values are correctly omitted (e.g. `android-13.md` legitimately has no
`maxSkillStock` because raw `BlastStock=null`, only `InitialBlastStock=2`).

**Check 2 (moveset) — PASS for page↔data, 0 mismatches.** Names, ki costs, datamined damage
(`best_damage` from `bullets`/`combatives`), hits, and S1 skillCosts all match. Datamined damage is
present on 83/619 super+ult rows; the rest correctly show no damage (inherit class defaults). No
fabricated damage anywhere. Example: `goku-z-early.md` Kamehameha `damage: 4560, hits: 4, chip
1,140` == raw bullet `beamPower 4560 / multiHit 4 / beamChip 1140`. The only defect is **upstream**
(HIGH-2: 4 nameless supers dropped before the moveset is built).

**Check 3 (transformsTo) — PASS, 163 edges, 0 problems.** No missing/`#`-rendering `targetSlug`,
no dangling slug (all resolve to a real character file), no cost or kind mismatch vs
`formChanges`+`fusions`. Spot-traced to raw `CharacterData`: Android 13→Fusion A13 (FormChange,
cost 2, HpRecovery 5000), Kefla→SSJ/SSJ2 (cost 1/2), Vegito→Super Vegito/SSGSS (cost 1/2) — all
faithful. `revert` edges are correctly excluded.

**Check 4 (DP) — present & in range; provenance dishonest (HIGH-1).** 208/208 playable have `dp`
(range 1–10, distribution 1:1 2:10 3:16 4:26 5:42 6:40 7:38 8:23 9:7 10:5). 0 non-playable carry
DP. No out-of-range values.

**Check 5 (playable count) — PASS, exactly 208 playable / 37 non-playable.** `playable` is
`bool(enrichment_entry)` (`gen_content.py:301`). The 37 non-playable were each verified to be empty
system/NPC stubs (`hasNumeric=False`, no moveset, no transforms): 33 in the 8xxx range (narration,
narration-with-voice, all-members, option, opponent, you, ally, enemy, status, shenron, porunga,
super-shenron, bulma(+super), chi-chi(+super), kami-first-gen, not-used[Fortuneteller Baba],
announcer, king-kai, dende-kid, dende-youth, namek-village-elder, elder-kai, zen-oh,
grand-minister, pilaf, shu, mai, oolong, supreme-kai, belmod, videl-super) plus `champa` (1000_00),
`kadan` (7111_00), and the two duplicate stubs `goku-super-0000-44` / `vegeta-super-0020-64`. **No
real fighter is wrongly excluded** — every excluded entry has no Numeric/moveset data.

**Check 6 (hpInherited) — PASS vs generator; 1 questionable heuristic.** Only 4 pages inherit HP;
3 are unambiguous. Gohan Beast is the exception (MEDIUM-4). Separately, 20 playable fighters have
no HP to inherit (MEDIUM-3). HP distribution on pages matches the 4-tier model exactly.

**Check 7 (raw trace) — PASS, 16/16 cids faithful.** Raw `Numeric.json` → `characters.json` →
page, every field OK:

| cid | slug | era / source | raw Life | SPChg | SPAutoRec | InitSP | BlastStk/Init | SparkDrain | BulletNum |
|---|---|---|---|---|---|---|---|---|---|
| 0000_00 | goku-z-early | Z / Base | 40000 | 7 | 1750 | — | 6 / — | 2800 | 5 |
| 0620_00 | android-13 | Movie / Base | 40000 | 0 | 1800 | 30000 | — / 2 | 2800 | 4 |
| 0790_00 | whis | Super / Base | 45000 | 5.5 | 2250 | 30000 | 6 / — | 2800 | 18 |
| 3050_00 | goku-mini | DAIMA / Pre-order | 40000 | 7 | 1750 | — | — / — | 2800 | 5 |
| 3100_03 | vegeta-daima-ssj3 | DAIMA / DAIMA Pack 2 | 40000 | 8 | 1500 | 10000 | — / — | 2800 | 999 |
| 3140_00 | majin-duu | DAIMA / DAIMA Pack 2 | 40000 | 7 | 1750 | — | 4 / — | 2800 | 6 |
| 0700_01 | omega-shenron-gt | GT / Base | 45000 | 7 | 1750 | 40000 | 6 / — | 2800 | 9 |
| 0680_00 | baby-vegeta-gt | GT / Base | 40000 | 7 | 1750 | — | — / — | 2800 | 4 |
| 0920_00 | kefla | Super / Base (fusion) | **null** | 7 | 1750 | — | — / — | 2800 | null |
| 3040_00 | cell-max | Movie / Heroes of Justice (giant) | **null** | 8 | 1500 | 40000 | — / — | 2800 | 4 |
| 0670_00 | hirudegarn | Movie / Base (giant) | **null** | 8 | 1500 | 40000 | — / — | 2800 | 3 |
| 3020_00 | gamma-1 | Movie / Heroes of Justice (DLC) | 40000 | 0 | 2000 | 30000 | 4 / 1 | 2800 | 999 |
| 0050_00 | krillin | Z / Base | 35000 | 7 | 1750 | 10000 | 4 / — | 2800 | 5 |
| 0881_00 | frost | Super / Base | 40000 | 7 | 1750 | — | 6 / — | 2800 | 8 |
| 0110_00 | gogeta-super | Movie / Pre-order (fusion) | **null** | 7 | 1750 | — | — / — | 2800 | null |
| 0100_00 | vegito | Z / Base (fusion) | **null** | 7 | 1750 | — | — / — | 2800 | null |

(`—` = field absent in raw → correctly omitted from page. `null` Life = MEDIUM-3.)

**Check 8 (S/W prose) — duplication (LOW-6); 0 numeric contradictions.** After allowing datamined
trigger ki costs, **0** real "wrong-number" claims remain (the 52 first-pass hits were all the
legitimate "15,000-ki on combo trigger" discount, present in the data as `triggerKiCost`). 0 named
moves missing from a fighter's kit; 0 prose stat numbers disagree with frontmatter; 0 own-DP
mismatches (the 9 apparent DP hits all reference the DP7 auto-reflect threshold, a transform
target's DP, or a meta points figure like "DP 33.9k").

**Check 9 (sparkingDrain) — PASS.** Every fighter with a value has exactly **2,800** (0 deviations);
the 20 null-HP fusions/giants still have 2,800. **0** pages describe 2,800 (or any value) as a
vanish/Z-Counter cost — the datamine rule is fully respected in character content.

---

## Hand-traced cids (raw → parsed → page), all verified faithful
`0000_00` Goku (Z-Early), `0620_00` Android 13, `0790_00` Whis, `3050_00` Goku (Mini)/DAIMA-DLC,
`3100_03` Vegeta (DAIMA) SSJ3/DLC, `3140_00` Majin Duu/DAIMA-DLC, `0700_01` Omega Shenron/GT,
`0680_00` Baby Vegeta/GT, `0920_00` Kefla (fusion), `3040_00` Cell Max (giant)/DLC, `0670_00`
Hirudegarn (giant), `3020_00` Gamma 1 (DLC), `0050_00` Krillin, `0881_00` Frost, `0110_00` Gogeta
(Super) (fusion), `0100_00` Vegito (fusion). Values in the Check-7 table; verbatim raw vs json vs
page comparison in `audit/a1_trace.py` output.

---

## Recommended fixes — ranked, all in parser/generator/enrichment (never hand-edit pages)
1. **HIGH-1:** `gen_content.py:310` — stop hardcoding `confidence: "datamined"`; emit `community`
   for character pages (or split per-field provenance). Mirror across blasts/skills/transformations.
2. **HIGH-2:** `gen_content.py:203-205` + `parse_data.py:277-282` — don't drop supers with a real
   asset+kiCost but null name; emit a category-derived fallback name and/or enrich the 4 names
   (Krillin ×2, Frost ×2). Add a parser warning for "asset present, locres name missing".
3. **MEDIUM-3:** enrich HP (community) for the 20 fusions/giants, or print an explicit
   "HP runtime-inherited / not serialized" note in the body.
4. **MEDIUM-4:** `resolved_hp` (`gen_content.py:135,142-144`) — inherit from the transform-source /
   highest-HP sibling, not the lowest formCode; fix Gohan Beast's "null HP" prose.
5. **MEDIUM-5:** update HP anchor to 9/15/148/16 in `CLAUDE.md:45`, `PLAN.md:90`, `audit/README.md:14`.
6. **LOW-6 / NITs:** optional polish (derive S/W tags from stats; render 999 as "continuous").
