# Agent 04 — Mechanics + Glossary + Datamine-Rule Honesty

**Scope:** all 22 `content/mechanics/*.md` + 30 `content/glossary/*.md` (52 files, every one read in full).
**Mandate:** datamine-confidence honesty (the vanish/2,800 rule, DP=community, partial-damage rule) and combat-logic consistency.
**Source of truth:** `data-mined/system_constants.json`, `data-mined/characters.json`, `data-mined/raw/masterdata/Numeric.json` (verified with `audit/a4_probe.py`, `a4_pursuit.py`, `a4_struct.py`).
**Date:** 2026-06-15 · build state assumed green (1144 pages). **No content/data/code modified.**

## Headline

- The **non-negotiable "2,800 is never a vanish cost" rule is VIOLATED** in two in-scope glossary pages (`z-counter.md`, `vanish-war.md`) and one out-of-scope guide. They cite **`data-mined/characters.json (vanishKiCost 2800)`** as a source. Verified: **`vanishKiCost` does not exist in `characters.json` at all**, and **`2800` is the Sparking!-mode drain** (`sparkingDrainPerSec`, uniform across all 208). This is the exact launch-usmap mislabel the codex was built to prevent. **BLOCKER.**
- A cluster of **`datamined`-tagged numbers are factually wrong against our own datamine**: "ki-drain androids start +2 stocks" (real value **1**, in 5 pages), "max skill stocks 4–5 / Cell·Piccolo 5" (real values **4/6/7, no 5**), and two mutually-contradictory pursuit-limit claims ("6 uniform" vs "4/6/7") where the real field is **`pursuitBaseLimit` = 1–4 (mode 2)**.
- A second cluster **mislabels community frame-data / lab numbers as `datamined`** (rush-5 ~2,460, charge speed ~1.3/s, sparking-gauge 7.0/10.5, guard-break 1 bar, several glossary pages at `confidence: datamined`).
- **Combat-logic / defensive-RPS reciprocity is sound** (CHECK 6/8): no "X is both blockable and unblockable" contradictions; throws correctly beat every reactive option; giants throw-immune both ways.
- **The DP pages agree** (CHECK 4) and correctly keep per-character DP out of `datamined`; the only DP issues are confidence-level (`confirmed` vs `community`) and an *honestly-flagged* team-size 3-vs-5 ambiguity.
- **The 2,800/s Sparking drain is correct in the datamine** (`sparkingDrainDistribution` = 2800×208) but **is never stated on any mechanics/glossary page** — `sparking-mode.md` omits it. So the only narrative uses of "2,800" in the corpus are the *wrong* vanish-cost citations.

---

## A. CONFIDENCE-VIOLATIONS TABLE (lead deliverable)

Severity: **BLOCKER** = repeats the bug the rules forbid · **HIGH** = `datamined` tag on a value our datamine refutes · **MEDIUM** = community/inferred value tagged `datamined`/`official`/`confirmed` · **LOW/NIT** = minor.

| # | Sev | File:line | Exact quote | Rule broken | Fix |
|---|-----|-----------|-------------|-------------|-----|
| 1 | **BLOCKER** | `glossary/z-counter.md:16` | `- "data-mined/characters.json (vanishKiCost 2800)"` | Vanish cost is **not datamined**; `vanishKiCost` field **does not exist**; **2,800 = Sparking drain, never a vanish cost**. | Delete the source line. Body already says "community-measured… not in the parameter tables" — keep that. |
| 2 | **BLOCKER** | `glossary/vanish-war.md:16` | `- "data-mined/characters.json (vanishKiCost 2800)"` | Same as #1. | Delete the source line. |
| 3 | **HIGH** | `glossary/z-counter.md:4` & `:16` | def: "≈half a ki bar (community-measured)" **vs** source "(vanishKiCost 2800)" | Internal contradiction: body says not-datamined, source claims datamined 2,800. | Body is correct; remove the contradictory datamined source. |
| 4 | **HIGH** | `mechanics/vanishing-assault.md:7-10` | `label: "Ki cost"` / `value: "small (modest base…)"` / `tag: "datamined"` | Vanish-family cost is **not datamined**. Body line 48 itself says *"No exact value is datamined or community-measured."* | Change `tag` to `community`. |
| 5 | **HIGH** | `mechanics/vanishing-assault.md:11-14` | `label: "'Dragon Assault' item reduction"` / `value: "−16.5% ki cost"` / `tag: "datamined"` | A −16.5% reduction of a base that is *not* datamined cannot itself be a datamined cost figure. | Tag `community` (or `official` if the item % is from notes), and stop implying a datamined base. |
| 6 | **HIGH** | `mechanics/skill-count.md:11-14` | `value: "character-specific, typically 4–5 (Cell/Piccolo 5; many 4; Yajirobe raised 5→6)"` / `tag: "datamined"` | **Datamine refutes it.** `maxSkillStockDistribution` = **4 (67) / 6 (68) / 7 (1, Babidi)** — *no value 5 exists*. Perfect Cell = **6**, Piccolo-fused-with-Kami = **6**. | "typically **4 or 6** (Babidi 7); no character has 5." |
| 7 | **HIGH** | `mechanics/skill-count.md:15-18` | `value: "usually 0; androids +1, ki-drain androids +2; 'Secret Measures' item +1"` / `tag: "datamined"` | **Datamine refutes "+2".** `system_constants.json` lists **Android 19 and Dr. Gero under `initialSkillStock`=1**; both character pages = `initialSkillStock: 1`. | All androids **+1**. Remove the "+2 ki-drain" claim. |
| 8 | **HIGH** | `mechanics/ki-and-charging.md:27-30` | `label: "Android starting skill stocks"` / `value: "+1 (infinite-ki) / +2 (ki-drain)"` / `tag: "datamined"` | Same "+2" error (datamine = 1). Body line 77 repeats it. | All androids **+1**. |
| 9 | **HIGH** | `mechanics/android-class.md:19-22` | `label: "Starting skill stocks (ki-drain)"` / `value: "+2 (Android 19, Dr. Gero)"` / `tag: "datamined"` | Same "+2" error (datamine = 1). Summary + body line 67 repeat it. | All androids **+1**. |
| 10 | **HIGH** | `glossary/android-class.md:13` + `:4`/`:17` | `confidence: "datamined"` … "ki-drain Androids (19, Dr. Gero) **start +2 stock**" | `datamined`-confidence page stating a datamine-refuted fact (real = 1). | Fix to +1; this page is community frame-data, not datamined. |
| 11 | **HIGH** | `glossary/skill-count.md:14` + `:4`/`:19` | `confidence: "datamined"` … "typically 4-5 (**Cell/Piccolo 5**…); ki-drain Androids (19, Dr. Gero) **start +2**" | `datamined`-confidence page carrying **two** datamine-refuted facts (#6, #7). | Correct both numbers; downgrade confidence. |
| 12 | **HIGH** | `mechanics/lightning-attack-pursuit.md:7-10` (val `:8`) | `value: "6 per combo (datamined PursuitLimitLightningAttack = 6)"` / `tag: "datamined"` | `PursuitLimitLightningAttack` in `Numeric.json` = **0**; the real pursuit cap `pursuitBaseLimit` (characters.json) = **1/2/3/4 (mode 2)**. "6" is a third-party value, not in our files. | Re-cite `pursuitBaseLimit` (mostly 2, +2 at Sparking); fix the value. |
| 13 | **HIGH** | `glossary/lightning-attack.md:12-14` + `:4` | `confidence: "datamined"` … source `"characters.json (pursuitLimitLightning: 4 / 6 / outlier 7)"` | **Field doesn't exist.** `characters.json` has `pursuitBaseLimit` (1–4), not `pursuitLimitLightning`. The "4/6/7, Babidi 7" pattern is **`maxSkillStock`** — a conflation. Also **contradicts #12** (uniform 6 vs variable 4/6/7). | Rewrite against `pursuitBaseLimit`; remove the invented field. |
| 14 | **MEDIUM** | `mechanics/ki-and-charging.md:15-18` | `value: "~1.3 / sec standard (Cell 1.32, Roshi 1.47, Vegeta 1.54)"` / `tag: "datamined"` | Datamined `kiChargeSpeed` = **6/7/8** (Cell 6, Roshi 7, Vegeta 7–8). The ~1.3 figures aren't in our datamine; sourced to a third-party wiki (line 61). | Tag `community`, or show the real `kiChargeSpeed` and explain the conversion. |
| 15 | **MEDIUM** | `mechanics/health-and-damage.md:27-34` | `"Rush 1st hit ~390"`, `"Rush 5-hit string ~2,460 (≈2,289 into armor)"` / `tag: "datamined"` | Class-default/aggregate melee + armor-reduction labs are **community** (rules: "class-default damage and frame data are community labs, not datamined"). Sourced to `research/04`, not a damage table. | Tag `community` (keep specific named-move blast values as `datamined`). |
| 16 | **MEDIUM** | `mechanics/smash-and-rush.md:11-13` | `"Rush 5-hit damage ~2,460 (≈2,289 into armor)"` / `tag: "datamined"` | Same community-lab figure as #15, duplicated. | Tag `community`. |
| 17 | **MEDIUM** | `mechanics/super-armor.md:7-18` | `"4–5 Smash/Rush-Chain hits"`, `"~2,289 (≈7% less…)"`, `"−12% defense"` / `tag: "datamined"` | "4–5 hits to break" + rush-5 are community labs (sourced `research/04` + third-party). Item existence is datamined; the *measured thresholds* are not. | Tag the measured thresholds `community`. |
| 18 | **MEDIUM** | `mechanics/giant-class.md:15-18` | `"Rush 5-hit into giant ~2,289 (≈7% less than ~2,460…)"` / `tag: "datamined"` | Same community rush-5 lab figure (4th occurrence). | Tag `community`. |
| 19 | **MEDIUM** | `glossary/super-armor.md:13` | `confidence: "datamined"` (4–5 hits, −12%, ~2,289 — all `research/04`) | Community frame/lab data tagged `datamined` confidence. | Downgrade to `community`. |
| 20 | **MEDIUM** | `glossary/smash-attack.md:13` | `confidence: "datamined"` (~2,275 / ~2,460 melee aggregates, `research/04` only) | Community lab aggregates tagged `datamined`. | Downgrade to `community`. |
| 21 | **MEDIUM** | `glossary/giant-class.md:13` | `confidence: "datamined"` (2-bar Z-Burst, 4–5 stagger) | Core numbers are community (mechanic page tags Z-Burst `community`). | Downgrade to `community`. |
| 22 | **MEDIUM** | `mechanics/revenge-counter.md:7-10` | `value: "2 skill stocks (some launch guides said 1)"` / `tag: "official"` | Body line 54: cost *"has never been resolved by an official numeric note."* Self-contradiction. | Tag `community`. |
| 23 | **MEDIUM** | `mechanics/guard-and-chip.md:11-14` | `"Guard-break ki damage (base) 1 ki bar"` / `tag: "datamined"` | Body line 63 says it's **inferred** from the Mind Breaker item, not directly datamined. ("Chip damage… by default" `datamined` is likewise an inference.) | Tag `community`/inferred for the baseline; keep item % as datamined. |
| 24 | **MEDIUM** | `mechanics/sparking-mode.md:7-14` | `"Sparking gauge charge speed 7.0/sec"` + `"Pre-Sparking decay 10.5/sec"` / `tag: "datamined"`; source `"system_constants.json + sparkingzerometa.com"` | Neither value is in our `system_constants.json` (no such field); 7.0 collides suspiciously with `kiChargeSpeed` mode 7.0. Third-party-sourced. | Verify against raw or tag `community`; don't imply `system_constants.json`. |
| 25 | **MEDIUM** | `mechanics/lightning-attack-pursuit.md:32` & similar | sources cited as `"data-mined/sparkingzerometa.com datamine (…)"` (also `ki-and-charging.md:61`, `skill-count.md:67`, `super-armor.md:38`, `sparking-mode.md:58`) | Prefixing a **third-party wiki** with `data-mined/` conflates community corroboration with our own datamine. | Cite `data-mined/raw/...` when ours; otherwise label `community (sparkingzerometa.com)`. |
| 26 | **LOW** | `glossary/dp.md:13`, `glossary/dp-gap.md:13` | `confidence: "confirmed"` | DP is a community value per project rule; the parallel `mechanics/dp-system.md` correctly uses `community`. `confirmed` over-states certainty. | Use `community` for consistency. |
| 27 | **LOW** | `mechanics/dp-system.md:19-22` | `"'Big Impact' item: +500 at 1 DP diff, +250 per extra DP"` / `tag: "datamined"` | Built on per-character DP (community); sourced `research/04`. Item params *may* be datamined but the DP-gap math is community. | Tag `community` unless the item effect is shown in raw. |
| 28 | **NIT** | `mechanics/health-and-damage.md:39-42` vs `:100` | values: `"15,000–19,620 base"` vs body `"15,000 base / 19,638 Boosted"` | 19,620 (presented as a base range top) ≠ 19,638 (a Boosted value). | Reconcile the two ultimate numbers. |

---

## B. RULE-BY-RULE RESULTS

### CHECK 1 — Vanish / Z-Counter (the priority check)
- **`vanish-z-counter.md` (mechanic): CLEAN.** Every vanish-cost figure is `tag: community`; body explicitly states "`vanishKiCost` is `null`… there is no per-character datamine number" and "**not** a datamined value." `confidence: community`. (Minor: the field is actually *absent*, not "null"; cosmetic.)
- **`z-counter.md` (glossary): VIOLATION #1/#3.** Definition/body are honest ("≈half a ki bar (community-measured)… the cost is not in the parameter tables"), but `sources:` line 16 cites **`vanishKiCost 2800`** — directly contradicting its own body and breaking the 2,800 rule.
- **`vanish-war.md` (glossary): VIOLATION #2.** Same `vanishKiCost 2800` source line; body again says "not stored in the parameter tables."
- **`vanishing-assault.md` (mechanic): VIOLATION #4/#5.** Ki-cost rows tagged `datamined` though body says the value is *not* datamined. (`glossary/vanishing-assault.md` is correctly `community`.)
- **`sparking-mode.md` / `glossary`:** no "2,800" misuse; but see #24 (7.0/10.5 datamined-but-not-in-our-files) and the gap below.
- **`super-counter.md` / `perception.md`:** **CLEAN on vanish honesty.** Super-counter window `~2 frames` correctly `community`; perception costs correctly tied to patch notes (`official`).
- **No page uses "2,800" as a vanish cost in prose** — but the *only* appearances of "2800" in `content/` outside character frontmatter are the three erroneous `vanishKiCost 2800` source lines (#1, #2, and the out-of-scope guide below). Searched corpus-wide.

> **Cross-scope (NOT my 52 files, flag for Agent 6/Guides):** `content/guides/beginner-numbers-guide.md:11` — `sources: - "data-mined/characters.json (vanishKiCost 2800, ultimate kiCost 50000, …)"`. Same BLOCKER-class mislabel; the `vanishKiCost 2800` token must be removed.

### CHECK 2 — `numericValue.tag` honesty across all mechanics `values[]`
Enumerated every value in all 22 mechanic pages. Over-claimed `datamined` tags: #4, #5, #6, #7, #8, #9, #12, #14, #15, #16, #17, #18, #23, #24, #27 (and `official` over-claim #22). **Correctly tagged** examples worth noting (good practice): all movement ki costs in `z-burst-dash.md`/`dragon-dash.md` (`community`); super-counter window (`community`); skill-count auto-regen (`community`); `fusion-and-potara.md` (genuinely datamined from `CharacterData` — stock cost 3–5, HpRecovery 0, AddMaxHP 0, 5.0s cooldown, 38 records — **a model of correct `datamined` usage**); HP tiers in `health-and-damage.md` (datamined, and correct).

### CHECK 3 — Sparking drain 2,800/s
- **Datamine confirmed:** `system_constants.json` `sparkingDrainDistribution` = **2800.0 × 208 (uniform)**; character frontmatter `sparkingDrainPerSec: 2800 × 208`. Anchor holds.
- **Gap:** `sparking-mode.md` and `instant-sparking.md` **never state the 2,800/s drain.** `sparking-mode.md` lists gauge *charge* 7.0/s and *pre-Sparking decay* 10.5/s (#24) but not the in-Sparking drain that defines duration. Given the rule's whole point, the canonical 2,800/s belongs on `sparking-mode.md` — its absence (while 2,800 surfaces *wrongly* as a vanish cost) is a structural weakness. **MEDIUM.**

### CHECK 4 — DP system (mechanics vs game-modes vs glossary)
- Slug collision `dp-system` resolves to `mechanics/` by priority (confirmed against `lib/content.ts` order). 
- **The two `dp-system` pages AGREE** on everything both state: scale 1–10, budget 15, selectable 10/15/20 (May 26 2026, persists), auto-reflect DP7+, DP-scaling widened, DP1 = Mr. Satan, DP10 = 5 (Beerus/Whis/Vegito SSGSS/Gogeta Super SSGSS/Gogeta GT SS4). No contradictions. `mechanics/dp-system.md` is simply terser (omits team size).
- **Per-character DP correctly NOT datamined** anywhere (mechanics `dp-system.md` `confidence: community`; per-character DP "lives in roster data"). Rule satisfied.
- **Team size:** the requested "5" is present but contested **honestly** — `game-modes/dp-system.md:55-66` documents a source conflict (Versus "up to 5" vs ranked "3"), `glossary/dp.md` says "3-5", `mechanics/dp-system.md` omits it. Not a contradiction (it's transparently flagged) but an unresolved ambiguity. **LOW.**
- DP glossary confidence over-claim: #26. "Big Impact" datamined tag: #27.

### CHECK 5 — HP / energy anchors
- **`health-and-damage.md` HP tiers EXACT MATCH** to `system_constants.json` `hpDistribution`: 30k→9, 35k→14, 40k→147, 45k→16. ✓ (Raw character files show 9/15/150/16 because they include extra forms/NPCs beyond the 186-fighter `hpDistribution` population; the page correctly cites the system-constants numbers.) **PASS.**
- **`ki-and-charging.md`:** "10,000 energy = 1 bar / 5 bars / 50,000 full" consistent and body honestly calls the bar↔energy bridge "datamine-inferred, not officially published" (line 85) — yet the `Energy per ki bar` value is tagged `datamined` (minor tension, LOW). Charge-speed numbers are the real problem (#14).
- **`guard-and-chip.md`:** numbers are item-inferred and the body says so honestly; the `datamined` tags on inferred baselines over-claim (#23).
- Ultimate cost "50,000 universal" / supers "20,000–40,000" consistent with `initialKi`/`initialSkillStock` distributions and CLAUDE anchors. ✓ (numeric nit #28).

### CHECK 6 — `counters[]` / `counteredBy[]` reciprocity
- **Note:** these arrays hold **descriptive prose**, not slugs (e.g. `"Throws (cannot be vanished)"`), so literal slug-existence/reciprocity checks don't apply; evaluated semantically.
- **Defensive RPS is internally consistent:** throws appear in `counteredBy` of `vanish-z-counter`, `super-counter`, `perception`, `sonic-sway`, `guard-and-chip` — and `throws.md` reciprocally claims it beats guard and "cannot be Vanished or Super Countered." ✓
- **Giants throw-immune** reciprocal: `throws.md` counteredBy "Giants (throw-immune)" ↔ `giant-class.md` counters "throw-immune." ✓
- **Perception/Super-Counter vs Afterimage** reciprocal with `glossary/afterimage-strike.md` ("ends… Super Counter or Perception"). ✓
- Only asymmetry: `revenge-counter.md` does not list throws in `counteredBy` — **semantically fine** (RC is a mid-combo break; throws aren't its answer). **No logical contradictions found.**

### CHECK 7 — Glossary ↔ mechanics consistency
- **Contradiction (HIGH #12/#13):** pursuit limit — `mechanics/lightning-attack-pursuit.md` says **uniform 6**; `glossary/lightning-attack.md` says **variable 4/6/7**. Both `datamined`, both wrong (real `pursuitBaseLimit` 1–4).
- **Contradiction (HIGH #6/#7/#11):** `glossary/skill-count.md` mirrors the false max-stock-5 and android-+2 claims from `mechanics/skill-count.md`.
- **Minor date discrepancies (LOW):**
  - Perception Smash/Rush follow-up 1→2: `mechanics/perception.md` attributes it to **Apr 21 2025** (re-locked May 2026); `glossary/perception.md` says **"since May 26 2026."**
  - Senzu 5→6 + Yajirobe start: `glossary/senzu-bean.md` says **Oct 2024**; `mechanics/skill-count.md` changeHistory says **Sep 22 2025**. (Also "first balance patch (Oct 2024)" conflicts with the Dec 11 2024 "first Free Update" framing used elsewhere.)
- **Consistent pairs (good):** sparking-mode, super-counter, instant-sparking, z-burst-dash, dragon-dash, sonic-sway, revenge-counter (value), unblockable, throws — numbers and definitions align.

### CHECK 8 — Internal logic / contradictions
- No "unblockable yet blockable" or mutually-exclusive-property contradictions found. `unblockable.md` ↔ `guard-and-chip.md` ↔ `smash-and-rush.md` agree (auto-evasion now evades many unblockables; Cell Max Max Bomb the holdout).
- `sparking-mode.md` buff-list vs May-2026 defense-down window is a stated tradeoff, not a contradiction.
- The substantive issues are the datamine factual errors above, not prose self-contradiction.

---

## C. Confidence-tag inventory (page-level)

- **Glossary `confidence: datamined`** (4): `skill-count` ❌(#11), `android-class` ❌(#10), `giant-class` ⚠(#21), `super-armor` ⚠(#19), plus `smash-attack` ❌(#20), `ki-blast` ⚠(partly OK — 999 shots is datamined), `lightning-attack` ❌(#13). → most should be `community`.
- **Glossary `confidence: confirmed`** (8): dp, dp-gap, sparking-mode, perception, super-counter→no(community), instant-sparking, revenge-counter, sonic-sway, unblockable, singles, senzu-bean, shenron-wish, whiff-punish→no(community), what-if-route, world-library, rush-chain, afterimage-strike, ki-sickness. DP ones flagged (#26); rest acceptable for established mechanics.
- **`community`** (correct, good): z-counter, vanish-war, vanishing-assault, z-burst-dash, dragon-dash, whiff-punish (glossary); all 22 mechanics except `fusion-and-potara` (`datamined`, correctly).

---

## D. Probes (read-only, under `audit/`)
- `a4_probe.py` — character-frontmatter distributions + system_constants cross-check (max/initial stock, kiChargeSpeed, drain, HP).
- `a4_pursuit.py` — `Numeric.json` PursuitLimit* value distributions.
- `a4_struct.py` — `characters.json` structure + `pursuitBaseLimit` distribution (1/2/3/4) confirming no `pursuitLimitLightning` / no `vanishKiCost` fields.

---

## E. Summary counts

- Files audited: **52 / 52** (22 mechanics + 30 glossary). 
- **BLOCKER: 2** · **HIGH: 11** · **MEDIUM: 14** · **LOW/NIT: 4** (+1 cross-scope guide BLOCKER-class flag).
- Distinct datamine factual errors (value contradicts our files): **3** (android +2 → 1; max-stock 5 → none/6; pursuit 6 & 4/6/7 → `pursuitBaseLimit` 1–4) spread across **8 pages**.
- "community-as-datamined" tag over-claims: ~**12** value rows + **5** glossary `confidence:datamined` pages.
- Combat-logic contradictions: **0** prose; **1** cross-page numeric contradiction (pursuit).
