# Agent 02 — Blasts Data Accuracy & Integrity Audit

**Scope:** all 453 `content/blasts/*.md` (282 supers + 171 ultimates).
**Date:** 2026-06-15 · **Auditor:** Audit Agent 2/10 · **Mode:** read-only (no wiki content/data/code modified).
**Source of truth:** `data-mined/blast_index.json` (parsed) → `data-mined/raw/masterdata/BulletSetting/BulletParam.json`, `Combatives/<cid>.json`, `Common.json`, `BlastSkill.json`, `BlastUltimate.json`, `OperationGuide.json`; cross-referenced against `data-mined/characters.json` and `content/characters/*.md`.

**Method:** I wrote three read-only probes under `audit/` and ran them with `python`:
- `a2_probe.py` — re-derives the *expected* page (frontmatter + body) for every blast directly from `blast_index.json` using a faithful re-implementation of `gen_content.py`'s logic (`slugify`, `best_damage`, user sort, tag/`Ki Required` stripping, category = most-common, sibling rule), then diffs against the on-disk `.md`. Also traces every page damage value back to raw, and cross-checks blast users ↔ character movesets.
- `a2_trace.py` / `a2_trace2.py` — trace each of the 83 page-level damage claims to the exact raw `BulletParam`/`Combatives` entry (precise cid via the page `characterSlug`); verify a kiCost sample against raw `ExpendEnergy`.
- `a2_stats.py` / `a2_query.py` — aggregate stats and finding breakdowns.

---

## Verdict / Severity counts

| Severity | Count | Summary |
|---|---|---|
| BLOCKER | 0 | — |
| HIGH | 2 | Slug collisions silently **drop 2 pages and orphan 8 fighters'** supers |
| MEDIUM | 9 | 8 cross-collection holes (same root cause as HIGH) + 1 multi-hit "power" interpretation ambiguity |
| LOW | 54 | 52 "projectile/beam values" wording on melee-derived damage + 1 cross-char Combatives key + 1 stray `\r` in a tag |
| NIT / informational | 2 classes | 49 verified-correct 40 k-ki supers (brief's "10/20/30k" heuristic is incomplete); 82 pages legitimately have no datamined category |

**Headline (honesty):** **0 honesty violations.** All **83** user-level "Datamined power" claims (across **80** pages) trace to a real per-character `BulletParam` override (29) or `Combatives` Power override (54) — none inherit a class default while asserting datamined damage. Every per-tag `*[datamined]*` label traces to an `OperationGuide`-derived tag; none are invented. `Ki Required` is stripped from every page (0 occurrences). All 58 sibling cross-links resolve to existing pages.

---

## Coverage stats

| Metric | Value |
|---|---|
| Blast pages on disk | 453 (282 super / 171 ultimate) |
| `blast_index.json` entries | 455 |
| Expected pages after dedup | 453 ✓ (matches disk; 0 missing, 0 orphan) |
| **Slug-collision-dropped blasts** | **2** (→ HIGH) |
| Total user rows compared | 611 |
| User rows w/ field mismatch vs `blast_index` | **0** |
| Page `category` mismatches (most-common rule) | **0** |
| Pages asserting datamined damage | 80 |
| User-level damage claims | 83 |
| ↳ traced to raw override | **83 / 83 (100%)** — 54 Combatives, 29 BulletParam |
| ↳ honesty violations (claim damage, raw = default) | **0** |
| Cross-collection: blast-user → char-page missing the move | **0** |
| Cross-collection: char move → no blast page / not a user | **8** (all from the 2 dropped pages) |
| kiCost sample verified vs raw `ExpendEnergy` | 16/16 exact (incl. 40 k supers + 50 k ults) |
| Pages w/ multi-hit / chip / category | 17 / 28 / 371 |
| `Ki Required` tag occurrences | 0 ✓ |

---

## HIGH findings

### H1 — Slug collisions silently drop blast pages and orphan 8 fighters' supers
**Slugs:** `full-power-energy-blast-volley-super`, `high-speed-rush-super`
**Where:** `scripts/gen_content.py:338-342`

```338:342:scripts/gen_content.py
    for b in blasts:
        s = f"{slugify(b['name'])}-{b['class']}"
        if s in bslugs:
            continue
        bslugs.add(s)
```

`slugify` (`gen_content.py:37-41`) maps both spaces and hyphens to `-`, so two distinct in-game names collide on one slug and the **second entry is `continue`-dropped entirely** — its users vanish from the wiki and the surviving page under-reports its roster:

| Kept page (name) | Users shown | Dropped variant (name) | Orphaned users (lost) |
|---|---|---|---|
| `full-power-energy-blast-volley-super` — "Full Power Energy Blast Volley" | **1** (Piccolo (Super Hero)) | "Full-Power Energy Blast Volley" | **7**: Goku (GT)×2, Gohan (Adult), Guldo, Kale, Roasie, Vegeta (Mini) |
| `high-speed-rush-super` — "High Speed Rush" | 8 | "High-Speed Rush" | **1**: Gohan (Super Hero) |

Evidence (`data-mined/blast_index.json`, two separate `(name, class=super)` keys differing only by a hyphen). These are near-certainly the **same move** with inconsistent localization punctuation. Net effect: `full-power-energy-blast-volley-super` claims **1 user when the true count is 8**, and 8 fighters have a Blast 2 that appears on **no** blast page.

**Recommended fix (generator-level):** group `blast_index` by slug *before* writing and **merge** colliding entries' `users[]` into one page (dedupe users by `charId`), instead of dropping. Equivalent alternative: normalize punctuation when building the `(name, class)` key in `parse_data.py:577/597` so the hyphen/space variants fold into one `blast_index` entry. Do **not** suffix-disambiguate — that would create two near-duplicate pages for one move.

---

## MEDIUM findings

### M1 — 8 character pages list a Blast 2 with no corresponding blast page / user entry
**Slugs (character pages):** `gohan-adult-super-saiyan`, `goku-gt-super-saiyan`, `goku-gt-super-saiyan-3`, `guldo`, `kale`, `roasie`, `vegeta-mini-super-saiyan` (all `blast2: "Full-Power Energy Blast Volley"`); `gohan-super-hero` (`blast2: "High-Speed Rush"`).

This is the downstream symptom of **H1**: the cross-collection invariant "a blast's `users[]` = exactly the set of characters whose moveset lists that move" breaks for these 8. Their character pages render a super that links to nothing (the slug `full-power-energy-blast-volley-super` resolves to a page that doesn't list them). Fixing H1 (merge on slug collision) resolves all 8 automatically. No separate fix needed.

### M2 — Multi-hit "Datamined power" is a single raw tick value shown without per-hit/total clarification
**Where:** `scripts/gen_content.py:409-413` + `:160-176` (`best_damage`)
**Examples (page vs raw):**
- `maximum-flasher-super` (Vegeta Z-Early `0020_11`): page **"Datamined power: 4,560"** + `hits: 9`; raw `BulletParam_0020_11_actSPM1_BEAM_bi` `BeamPower=4560, CollisionRevibeNum=9`.
- `kamehameha-super` (`0000_00`): page 4,560 + `hits: 4`; raw `BeamPower=4560, Revibe=4`.

`best_damage` reports the single largest `BeamPower`/`Power` of one projectile, while `hits` is that projectile's `CollisionRevibeNum`. The body simultaneously states *"typical Beam supers land ~4,000–6,000 **total**"* (`:420-423`). If `BeamPower` is per-revibe, a 9-hit beam's total is ~9× the printed number; if it's already a total, the hit count is decorative. The page doesn't disambiguate, so a numbers-first reader can misread the headline damage by up to ~Nx. The value is faithfully datamined (not fabricated), so this is clarity/accuracy, not honesty.
**Recommended fix:** label the figure explicitly (e.g. "BeamPower 4,560 per hit × 9" or "per-tick") and gate the generic "~4,000–6,000 total" sentence so it isn't printed alongside a multi-hit per-tick value.

---

## LOW findings

### L1 — "projectile/beam values" wording printed on 52 melee/Combatives-derived damage pages
**Where:** `scripts/gen_content.py:410-413` and `:420-423`
54 of 83 damage claims come from `Combatives` **Power** (melee/contact), not a projectile, yet the body labels every value *"projectile/beam values vs 40,000-HP standard cast"*. Misleading for Rush and many Fire/Explosive ults. Examples:
- `wolf-fang-fist-super` — d=6,700 ← `Combatives_0060_00_actSPM2HD1P Power=6700` (Rush).
- `final-explosion-ultimate` — d=16,000 ← `Combatives_0020_40_actULTHD1P` (Explosive Wave).
- `spirit-bomb-ultimate` — d=13,000 ← `Combatives_0002_30_actULTHD1P` (Fire).
- `big-bang-attack-ultimate` — d=12,000 ← `Combatives_0020_11_actULTHD1P` (Fire).

**Recommended fix:** have `best_damage` return a source flag (`bullet` vs `melee`) and switch the wording to "contact/melee values" when the damage came from `Combatives`. (Full list of 52 slugs in `audit/a2_findings.json`, check=`wording`.)

### L2 — Cross-character Combatives key feeds one ultimate's damage
**Slug:** `point-blank-kamehameha-ultimate` (Goku (Super) UI-Sign, file cid `0000_50`)
The winning melee Power (8,000) comes from key **`Combatives_0050_00_actULTHD1P`** *inside* `Combatives/0000_50.json`. The parser attributes by file-stem cid (`parse_data.py:200,258-268`), so the embedded `0050_00` is treated as `0000_50`'s. It is the only such case among all 83 damage rows, and the value does live in this character's own asset file, so it is most likely a retained source-name artifact rather than a wrong number — but it warrants an in-game spot-check. **Fix (optional):** assert the embedded cid in the Combatives key equals the file cid in `parse_data.py`, log mismatches.

### L3 — Stray carriage return left in a datamined tag
**Slug:** `body-change-ultimate` (frontmatter `tags[4]`)
The Body Change body-swap restriction tag is stored as `"...you cannot use\r Transformation, ..."` — a literal `\r`. `guide_decode` normalizes `\n` but not `\r` (`parse_data.py:131`: `txt.replace("\n", " ").strip()`).
**Fix:** `txt.replace("\n", " ").replace("\r", "").strip()` (or `re.sub(r"\s+", " ", txt)`).

---

## NIT / informational (verified NOT errors)

### N1 — 49 super-user rows at 40,000 ki are a legitimate datamined 4th tier
The brief's "supers cluster at 10/20/30k" flagged 49 rows at 40,000 ki (e.g. `final-kamehameha-super`, `blaster-meteor-super`, `death-storm-super`, `gigantic-crash-super`, `explosive-flash-super`, …). I verified a sample against raw: **all match `BlastSkill*.ExpendEnergy` exactly.**

| Move / user | cid/slot | page ki | raw `ExpendEnergy` |
|---|---|---|---|
| Final Kamehameha / Super Vegito | `0100_01`/SPM2 | 40,000 | 40,000 ✓ |
| Blaster Meteor / Broly (Super) | `0555_00`/SPM2 | 40,000 | 40,000 ✓ |
| Death Storm / Frieza (Z) | `0151_00`/SPM2 | 40,000 | 40,000 ✓ |

40,000 ki = 4 bars is a real super tier; **not** an error. The audit heuristic should read "10/20/30/40k supers, 50k ults." Ultimates: all sampled = 50,000 ✓.

### N2 — 82 pages carry no `category`; this is honest source sparsity
`OperationGuide` has no `BLAST_CATEGORY` record for those (cid, slot)s, so the generator emits none rather than inventing one (e.g. `super-kamehameha-super`, `full-power-energy-blast-volley-super`). Page-level category distribution: Rush 166, Fire 77, Beam 56, Continuous Fire 21, Explosive Wave 18, Simultaneous Fire 14, Short-range energy attack 11, others 8.

---

## Damage honesty — 24 traced blasts (page value ↔ exact raw entry)

All values below were re-derived from raw and **match the page exactly**. `B`=BulletParam (beam/projectile), `C`=Combatives (melee/contact).

| Blast (slug) | User / cid·slot | Page d / chip / hits | Raw source → value | Cat |
|---|---|---|---|---|
| `kamehameha-super` | Goku (Teen) `0002_50`·SPM1 | 4,560 / 1,140 / 4 | **B** `..._actSPM1_SSG` BeamPower 4560, BeamShave 1140, Revibe 4 | Beam |
| `final-flash-super` | Future Trunks `0080_31`·SPM2 | 4,560 / 1,140 / 4 | **B** `..._actSPM2_BEAM_bi` BeamPower 4560 (>Power 1710) | Beam |
| `final-kamehameha-super` | Super Vegito `0100_01`·SPM2 | 5,360 / 1,340 / 4 | **B** `..._actSPM2_SSG` BeamPower 5360 | — |
| `maximum-flasher-super` | Vegeta Z-E `0020_11`·SPM1 | 4,560 / 1,140 / 9 | **B** `..._actSPM1_BEAM_bi` BeamPower 4560, Revibe 9 | Beam |
| `special-beam-cannon-ultimate` | Piccolo `0040_00`·ULT | 9,600 / 3,840 / 5 | **B** `..._actULT_BEAM_pen` BeamPower 9600, BeamShave 3840, Revibe 5 | Rush |
| `planet-geyser-ultimate` | Dr. Wheelo `0570_00`·ULT | 750 / 250 / — | **B** `..._actULT_B_BOM` BeamPower 750, BeamShave 250 | Beam |
| `photon-strike-super` | Dr. Wheelo `0570_00`·SPM1 | 1,900 / 380 / 4 | **B** `..._HUGE_BEAM_s3` Power 1900, BeamShave 380, Revibe 4 | Fire |
| `stardust-blaster-super` | Gogeta (S) `0110_03`·SPM1 | 5,700 / 1,140 / 2 | **B** `..._actSPM1` Power 5700, Revibe 2 | Fire |
| `tri-beam-super` | Tien `0070_00`·SPM2 | 5,700 / 1,140 / 2 | **B** `..._actSPM2` Power 5700 | Fire |
| `death-saucer-super` | Frieza (Z) `0154_00`·SPM1 | 1,000 / 1,200 / 2 | **B** `..._actSPM1_hom` Power 1000, BeamShave 1200, Revibe 2 | Fire |
| `assault-rain-super` | Super Buu `0172_00`·SPM1 | 500 / 100 / 11 | **B** `..._actSPM1` Power 500, Revibe 11 | Simultaneous Fire |
| `chou-makouhou-barrage-super` | Great Ape Vegeta `0023_00`·SPM2 | 2,234 / 447 / 4 | **B** `..._HUGE_BULLET_s3` Power 2234, Revibe 4 | Continuous Fire |
| `chain-destructo-disc-ultimate` | Krillin `0050_00`·ULT | 1,000 / 1,500 / — | **B** `..._actULT_SRPSI` Power 1000, Shave 1500 | Continuous Fire |
| `super-ghost-kamikaze-attack-ultimate` | Gotenks `0120_01`·ULT | 2,000 / 212 / — | **B** `..._actULTSI_BLT_unblockable` Power 2000 | Simultaneous Fire |
| `wolf-fang-fist-super` | Yamcha `0060_00`·SPM2 | 6,700 / — / — | **C** `..._actSPM2HD1P` Power 6700 | Rush |
| `charge-super` | Goten `0090_00`·SPM2 | 5,700 / — / — | **C** `..._actSPM2HD1P` Power 5700 | Rush |
| `dynamite-kick-super` | Mr. Satan `0180_00`·SPM1 | 8,500 / — / — | **C** `..._actSPM1HI` Power 8500 | Rush |
| `drain-life-cell-ultimate` | Cell `0160_00`·ULT | 9,270 / — / — | **C** `..._actULTHD1P_2D` Power 9270 | Rush |
| `spirit-bomb-ultimate` | Goku (GT) `0002_30`·ULT | 13,000 / — / — | **C** `..._actULTHD1P` Power 13000 | Fire |
| `big-bang-attack-ultimate` | Vegeta Z-E `0020_11`·ULT | 12,000 / — / — | **C** `..._actULTHD1P` Power 12000 | Fire |
| `final-explosion-ultimate` | Majin Vegeta `0020_40`·ULT | 16,000 / — / — | **C** `..._actULTHD1P` Power 16000 | Explosive Wave |
| `mr-buu-arrives-ultimate` | Mr. Satan `0180_00`·ULT | 16,750 / — / — | **C** `..._actULTHD1P` Power 16750 | Rush |
| `evil-containment-wave-ultimate` | Master Roshi `0140_00`·ULT | 12,500 / — / — | **C** `..._actULTHD1P` Power 12500 | Short-range energy |
| `revenge-death-ball-ultimate` | Super Baby 2 (GT) `0680_02`·ULT | 11,000 / — / — | **C** `..._actULTHD1P` Power 11000 | Fire |

Note the `best_damage` rules hold throughout: beams correctly take `max(BeamPower, Power)`; **melee-derived rows correctly drop `chip`/`hits` to `—`** (`gen_content.py:174-175`); and `hits` only ever equals a real `CollisionRevibeNum`.

---

## Checks performed (all 8 brief items) — status

1. **users[] vs blast_index** — 611 rows, **0 field mismatches** (character, slug, kiCost, triggerKiCost, damage, chip, hits, category, tags, notes/slot all match). ✓
2. **category = most-common among users** — **0 mismatches** across 453 pages. ✓
3. **Datamined-damage honesty** — 83/83 trace to real overrides, **0 violations**; tags trace to `OperationGuide`; no invented `[datamined]`. ✓
4. **Cross-collection** — user→char: 0 missing; char→blast: 8 missing, **all** caused by H1's 2 dropped pages. ✓ (quantified)
5. **Sibling cross-link** — 58 links, all targets exist, all are same-name/other-class. ✓
6. **kiCost sanity** — supers 10/20/30/**40**k, ults 50k; 16/16 sample verified vs raw `ExpendEnergy`. ✓
7. **slug/dedup** — 2 collisions found (H1); `-super`/`-ultimate` suffixing otherwise correct; `Ki Required` stripped everywhere (0 hits). ✓
8. **hits/chip rules** — `hits` only from `CollisionRevibeNum`; melee-derived damage correctly drops `hits`/`chip` (0 violations after tie-case verification). ✓

## Artifacts (under `audit/`, read-only probes)
`a2_probe.py` (main cross-check), `a2_trace.py`/`a2_trace2.py` (raw damage + kiCost trace), `a2_stats.py`, `a2_query.py`, and machine-readable `a2_findings.json`.
