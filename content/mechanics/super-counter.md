---
slug: "super-counter"
name: "Super Counter"
category: "defense"
input: "↑ + Rush Attack at the exact moment an attack connects (repeatable while being comboed)"
values:
  - label: "Input window"
    value: "~2 frames (≈33 ms at 60fps)"
    patch: "current (re-tested post-May 26, 2026)"
    tag: "community"
  - label: "Cost"
    value: "0 (free)"
    tag: "official"
  - label: "Whiff lockout"
    value: "Extended lockout after a failed attempt"
    patch: "added Jan 20, 2025"
    tag: "official"
  - label: "Ki recovery during attempt"
    value: "0 (ki gain disabled during Super Counter)"
    patch: "added May 26, 2026"
    tag: "official"
counters:
  - "Rush combos (front)"
  - "Vanishing Assault pressure"
counteredBy:
  - "Throws"
  - "Delayed/staggered strings"
  - "Ki blasts at range"
summary: "The universal free escape from front rush pressure: up + rush attack on the exact frame a hit lands. The window is community-measured at roughly 2 frames, and two patches have nerfed attempt-spam (whiff lockout Jan 2025, no ki gain during attempts May 2026)."
changeHistory:
  - version: "v1.x (Jan 20, 2025)"
    date: "2025-01-20"
    change: "Failed Super Counter attempts now incur a longer lockout before the next attempt (anti-mash)."
  - version: "May 26, 2026 update"
    date: "2026-05-26"
    change: "Ki no longer recovers while attempting Super Counters; mash-fishing now has a real resource cost."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (community frame tests, r/SparkingZero + GameFAQs labbing)"
  - "Bandai Namco official patch notes (Jan 20, 2025; May 26, 2026)"
---
Super Counter is Sparking! ZERO's universal defensive answer: while taking rush-string hits from the front, input **↑ + Rush Attack** on the exact frame a hit connects to instantly reverse positions at **zero cost**.

## The numbers

- **Window:** community frame-tests place the success window at **~2 frames (≈33 ms)**; a minority of labbers argue up to 4 frames depending on move hit-stop. No official value has ever been published. Measured on current patch; earlier measurements (launch era) found the same window, so the *window itself* has not been patched.
- **Cost:** free — no ki, no skill stocks. This is why it defines high-rank play: it is the only escape that costs nothing.
- **Anti-spam nerfs (quantified by patch):**
  - **Jan 20, 2025** — failed attempts trigger a **longer lockout** before you can attempt again (mashing ↑+square during a combo now whiffs entire strings).
  - **May 26, 2026** — **ki gain is disabled** during attempt frames, so fishing for Super Counters bleeds your ki economy versus charging.

## Interactions

- Works against front rush pressure and [[vanishing-assault|Vanishing Assault]] follow-ups; does **not** beat throws or true ranged ki pressure.
- After the May 26, 2026 update, [[afterimage-strike]] ends early when the user is Super Countered — the counter is now also the answer to evasion-skill stalling.
- In Singles (post-June 23, 2025 split), standardized HP pools make the free escape proportionally stronger; in DP it competes with [[revenge-counter|Revenge Counter]] (2 skill stocks) as the comeback tool.
