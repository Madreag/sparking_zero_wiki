# Agent 03 — Skills + Transformations Data Accuracy

**Scope:** 146 `content/skills/*.md` + 164 `content/transformations/*.md`
**Date:** 2026-06-15 · **Method:** read-only cross-check of every page against the datamine
(`data-mined/raw/masterdata/{CharacterData,BlastForte}.json` → parsed `*.json` → `enrichment/*.json`),
replicating `gen_content.py` logic and re-deriving values from the raw layer.
**Probes (reproducible, read-only):** `audit/a3_tf_probe.py`, `audit/a3_tf_probe2.py`,
`audit/a3_skills_probe.py`, `audit/a3_skills_probe2.py` (raw outputs in `audit/a3_*_out.txt`).

> **Headline:** Both generated collections are in **excellent** shape. There are **no BLOCKER/HIGH**
> page bugs. The pipeline is internally consistent (raw == parsed == rendered) for stat deltas,
> moveset diffs, costs, HP rules, DP, partners, and link integrity. Findings are one wrong
> enrichment user-list (`Fury`), one frontmatter consistency gap (`fury` userCount), a
> **documentation** claim that contradicts the shipped data (the "HpRecovery: 0" heal-removal rule),
> and a cosmetic trailing-space name.

## Severity counts
| Severity | Count |
|---|---|
| BLOCKER | 0 |
| HIGH | 0 |
| MEDIUM | 2 |
| LOW | 1 |
| NIT | 2 |

---

## Coverage / verification stats

**Transformations (164 pages)**
- 164/164 pages matched to a non-revert edge; **0** orphan pages, **0** edges dropped by slug collision.
- Raw `CharacterData.json` (228 form/fusion/Potara edges) vs parsed `transformations.json` (208 edges):
  **0 field mismatches** on `hpRecovery`/`consumeBlastStock`/`addMaxHp`/`coolTimeSec`/`kind`. The 20
  raw-only edges are all `S_`-prefixed story-duplicate source slots that resolve to pages that already
  exist via the playable source — correctly excluded.
- `statChanges` recomputed from `characters.json` for **all 164** pages → **0 mismatches**.
- Moveset-diff table recomputed (`kit()`) for **all 164** pages → **0 mismatches**.
- `cost`, `hpRule`, body "HP recovery on change", `dpFrom`/`dpTo`, `kind`, partners → **0 mismatches**.
- **0 revert edges leaked**; **0 dead body wikilinks**.
- HP-recovery split: **137 pages heal 0**, **27 pages heal >0** (5,000–10,000) — every positive value
  raw-confirmed. **31 transforms** carry a max-HP delta (independently recomputed; Bojack +5,000 + 30 more).

**Skills (146 pages)**
- Catalog: 170 entries → **146 unique valid names → 146 pages** (1:1).
- Parsed `s1Skills` cost+flags vs **raw `BlastForte.json` `ExpendBlastStock`/guard flags**: **417 (char,slot)
  pairs checked → 0 mismatches.**
- `skillCost` provenance: **73 datamined-single**, **5 enrichment-only (labelled `community`)**,
  **68 null/class-default ("—")**. **0** skills claim a *datamined* cost that is actually a class default.
- `effect` provenance: **0 fabricated** (every effect traces to `enrichment.effect` or datamined OperationGuide desc).
- `tier`: **0 invalid**, **0 mismatched**. `confidence`: **0 dishonest** (no `datamined` label without datamined substance).
- Per-user "Datamined users & stock costs" tables vs `characters.json`: match on all 146 (the 2 flagged
  rows are a probe-side strip artifact = NIT #2 below).
- 2 skills with 0 datamined users (`Cloak Ki`, `Fury`) — handling reviewed individually below.

---

## MEDIUM

### M1 — `Fury` lists two users that the datamine contradicts (no character has this skill)
**File:** `content/skills/fury.md:5-7` · **Source of the bad data:** `data-mined/enrichment/skills.json:527-534`

The page asserts:

```5:7:content/skills/fury.md
users:
  - "Gohan (Teen)"
  - "Gohan (Adult)"
```
But **no character in the datamine has a Blast Forte named "Fury"** (`skill_users["Fury"] == []`; the
only `*Fury` skill in `s1Skills` is **"Maiden's Fury"** on Ribrianne/Kakunsa/Roasie). The two named
users provably run different skills:

| Character | Datamined S1 / S2 (`characters.json` + char page) | Has "Fury"? |
|---|---|---|
| Gohan (Teen) `0031_00` | Wild Sense (S1) · Full-Power Charge (S2) | **No** |
| Gohan (Adult) `0032_00` | Wild Sense (S1) · Full-Power Charge (S2) | **No** |

Confirmed cross-collection: `content/characters/gohan-teen.md:33,36` lists `Full-Power Charge` and
`Wild Sense`, **not** `Fury`; the string `Fury` appears in **zero** character pages. Per the audit
ground rule (game files beat Game8/Fandom for factual claims), the user list is wrong. The page is
`confidence: community`, which softens but does not excuse a factual user attribution contradicted by
the source of truth.

**Recommended fix:** in `enrichment/skills.json` remove the `users` array for `Fury` (or correct it to
the real owner if one exists in a future roster). With no datamined users, the generator will then emit
the standard "no current roster user (story/legacy entry)" body like `Cloak Ki` does.

### M2 — Documentation rule "HpRecovery: 0 on transforms" contradicts the shipped data (content is correct)
**Docs:** `CLAUDE.md:46`, `PLAN.md:58` · **Data:** `data-mined/transformations.json`, raw `CharacterData.json`

The repo states as a confirmed datamine fact that the May-26-2026 heal-removal shipped `HpRecovery: 0`
"on transforms." The **post-patch** extract (Steam build 22517964, dumped 2026-06-05 — i.e. *after* the
May 26 update) shows this is **only partially true**: **27 of 208 parsed edges** (and 30/228 raw, incl.
reverts) still heal **5,000–10,000 HP**. The heal-removal hit the repeatable Super-Saiyan *toggles*
(those are 0) but **not** the one-way cinematic form changes (Frieza/Cell forms, Broly LSSJ, Cooler,
Bojack, Android 13, Lord Slug, Jiren, Toppo, Gohan SH→Ultimate→Beast, Orange Piccolo, Great Ape Vegeta,
Syn→Omega Shenron, Fused Zamasu, Kale Berserk, UI -Sign-→UI, Giant Gomah).

**The transformation pages are CORRECT.** Specifically re: the task's spot target — **Bojack → Full-Power
Bojack shows 5,000 and that is genuine, not stale**:
- Page `content/transformations/bojack-to-full-power-bojack.md:9,26` → `HP recovery on change: 5,000`
- `data-mined/transformations.json` (`0630_00→0631_00`) → `"hpRecovery": 5000.0`
- raw `CharacterData_0630_00.BattleAssets.FormChange.HpRecovery` → `5000.0` (probe: `[OK]`)

**Recommended fix:** reword both docs from a blanket "HpRecovery: 0 on transforms" to the accurate
"HpRecovery 0 on Super-Saiyan-style toggle transforms; one-way cinematic form changes retained 5k–10k
heals (27/208 edges)." No content change needed. *(Docs are Agents 4/5/6's primary scope; flagged here
because the task explicitly asked me to verify the heal-removal and the Bojack value.)*

---

## LOW

### L1 — `fury` frontmatter: `users[]` populated but `userCount` omitted; `audit_v3` can't catch it
**File:** `content/skills/fury.md:5-7` (no `userCount` key)

Because `Fury` has 0 *datamined* users, the generator falls back to the enrichment `users` list, but sets
`"userCount": len(users) or None` where `users` is the *datamined* list (empty) → **`userCount` is dropped
while `users[]` still shows 2 entries** (`gen_content.py:477-478`). This is the only userCount/len(users)
inconsistency in all 146 skills (every other page is exact — the off-by-one concern is otherwise clean).

It also exposes a **gap in `audit_v3.py:160-170`**: section I only fires `if uc and n` — when `userCount`
is absent it is skipped, so this page passes QA silently. (The `audit_v3` userCount check is *correct for
present values* but blind to the omitted-count-with-users case.)

**Recommended fix:** resolving M1 (drop Fury's enrichment users) makes this disappear. Independently,
change the generator to `"userCount": len(front_users)` (count whatever ends up in `users[]`), and tighten
`audit_v3` section I to also flag `users present & userCount missing`.

---

## NIT

### N1 — Trailing space in character name "Super Gogeta (Z) " leaks into labels
**Root:** `data-mined/characters.json` `0110_04.fullName == "Super Gogeta (Z) "` (only such name in the dataset)
**Propagates to:** `content/characters/super-gogeta-z.md:3`, skill pages
`content/skills/im-the-one-who-will-defeat-you.md:6,26` and `content/skills/immovable-stance.md` (user
rows + frontmatter), and the Super Gogeta fusion transformation pages.

The wikilink target (slug before the `\|`) is fine, so links resolve; only the **visible label** carries a
stray trailing space (`[[super-gogeta-z\|Super Gogeta (Z) ]]`). Purely cosmetic.

**Recommended fix:** `.strip()` `name`/`fullName` in `parse_data.py` (`name_of`) so the locres trailing
space is trimmed at the source; regen.

### N2 — (probe note, not a page bug) per-user table "mismatch" on the two Super Gogeta rows
The `a3_skills_probe.py` `user_table` check reports 2 rows differing only by the N1 trailing space; this is
a probe-side `.strip()` asymmetry, **not** a page defect. Documented so it isn't re-triaged as real.

---

## Things explicitly verified as CORRECT (no action)
- **Bojack +5,000 HP delta and HP recovery** — genuine post-patch data (M2). 30 other HP deltas
  independently recomputed and matched (Gotenks fusions +10,000, Master Roshi ±10,000, Broly +5,000,
  Cooler +5,000, Fused Zamasu +5,000, etc.).
- **All transformation costs** = `consumeBlastStock`; **hpRule** strings (incl. `addMaxHp`, `cooldown`,
  `no HP recovery after 2nd use`) match the data verbatim.
- **DP from/to** (`dpFrom`/`dpTo`) = `enrichment/characters.json` `dp` for both endpoints, all 164 pages.
- **Fusion/Potara partners** present, resolve to real characters, and are listed; **revert edges fully
  excluded**; `kind` ∈ {transform, fusion} only.
- **Skill costs**: the 5 enrichment-sourced costs (`Explosive Wave`, `Wild Sense`, `False Courage`,
  `Solar Flare`, `All I Need Is Five Seconds!`) correctly carry `confidence: community` because their
  datamined users have no serialized `ExpendBlastStock` (class default). The 73 datamined-single costs all
  match raw `BlastForte` `ExpendBlastStock` exactly.
- **`Cloak Ki`** (0 users) handled correctly: story/legacy note, `confidence: community`, no fabricated count.
- **Skill effects**: none fabricated; datamined OperationGuide descriptions render in the "In-game
  description *[datamined]*" block and are kept distinct from community effect prose (e.g. `kaioken.md`).
