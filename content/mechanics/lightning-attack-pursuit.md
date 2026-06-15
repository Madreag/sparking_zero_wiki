---
slug: "lightning-attack-pursuit"
name: "Lightning Attack & Pursuit"
category: "offense"
input: "Pursue a knocked-away opponent to continue the combo; chase/pursuit attacks extend a launched string"
values:
  - label: "Pursuit limit (pursuitBaseLimit)"
    value: "1–4 per combo (most fighters 2; +2 while Sparking)"
    patch: "current (datamine)"
    tag: "datamined"
  - label: "Use"
    value: "chase a launched/knocked-away foe to keep the combo going"
    patch: "current"
    tag: "official"
  - label: "Wall/ground slam follow-up"
    value: "Chase attacks continue a slam combo (adds follow-up damage)"
    patch: "current"
    tag: "official"
counters:
  - "Extends combos on a launched opponent"
  - "Converts wall/ground slams into continued damage"
counteredBy:
  - "Pursuit cap (pursuitBaseLimit, typically 2 per combo; +2 while Sparking)"
  - "Combo scaling (each chase hit returns less)"
  - "Vanish / tech on the chase"
summary: "The chase mechanic that extends combos on a launched or knocked-away opponent. The datamined pursuit cap is pursuitBaseLimit — 1–4 per combo (most fighters 2), rising +2 while Sparking — the ceiling on how many times you can re-chase before the combo must end. (Numeric.json's PursuitLimitLightningAttack reads 0, so there is no datamined '6' cap.) Chase attacks also continue wall/ground-slam combos. Subject to combo scaling, so each additional pursuit hit returns less."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "data-mined/characters.json (pursuitBaseLimit 1–4, mode 2; pursuitAddAtSparking +2)"
  - "research/04-mechanics-frame-data.md (§1.5 combo scaling; §9 Chase attacks continue slam combos)"
  - "Bandai Namco official patch notes / in-game tutorial (Chase / Pursuit attacks)"
---
Lightning Attack and Pursuit are the **chase** tools that extend a combo after you've launched or knocked the opponent away. Instead of letting a launcher end the string, you **pursue** the flying body and keep hitting.

## The numbers

- **Pursuit limit: 1–4 per combo (most fighters 2).** The datamined cap is **`pursuitBaseLimit`** (characters.json): values run **1 / 2 / 3 / 4** with **2 the mode**, and it **rises by +2 while [[sparking-mode|Sparking]]** (`pursuitAddAtSparking` = 2). This is the ceiling that keeps chase loops from running forever. The old "**6**" figure was a third-party value: `Numeric.json`'s `PursuitLimitLightningAttack` actually reads **0**, and the "**4/6/7**" pattern quoted elsewhere is really [[skill-count|max skill stock]] (a conflation), not a pursuit field.
- **Wall / ground slams:** **Chase** attacks continue a slam combo, adding follow-up damage when you knock the opponent into terrain (see [[health-and-damage|health & damage]] and the stage-slam interactions).

## Interactions

- **Combo scaling applies.** Every pursuit hit is still subject to the aggressive diminishing-returns curve, so the **last** Lightning Attack in a chain does far less than the first — chasing all the way to the cap is not always optimal damage. See [[health-and-damage|combo scaling]].
- The opponent can **tech or [[vanish-z-counter|Vanish]]** out of the chase at the appropriate window, so pursuit is not guaranteed for every rep against a competent defender.
- Pursuit interacts with the **[[smash-and-rush|rush/smash chain]]** routing — you typically launch off a Smash, then convert with Lightning Attack pursuits before a finisher (a Rush Super or Ultimate), keeping the combo short enough that scaling doesn't eat the [[health-and-damage|finisher]].
