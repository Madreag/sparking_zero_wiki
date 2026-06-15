---
slug: "sonic-sway"
name: "Sonic Sway"
category: "defense"
input: "Frame-perfect Super Perception against an incoming Rush attack"
values:
  - label: "Trigger"
    value: "frame-perfect Super Perception vs a Rush"
    patch: "current"
    tag: "official"
  - label: "Cost"
    value: "ki only (inherits Super Perception's melee cost; no skill stock vs a rush)"
    patch: "current"
    tag: "community"
  - label: "Effect"
    value: "dodge + counter, and drains the attacker's ki"
    patch: "current"
    tag: "official"
  - label: "Beats"
    value: "Rush strings only (not blasts, not throws)"
    patch: "current"
    tag: "community"
counters:
  - "Rush strings"
  - "Vanishing Assault into rush pressure"
counteredBy:
  - "Throws"
  - "Blasts (it is a melee read)"
  - "Mistimed input (whiffs into the rush)"
summary: "A frame-perfect upgrade of Super Perception versus a Rush: instead of a normal deflect you sway the rush, counter, AND drain the attacker's ki. It is a reward layer on top of Perception — same input, tighter timing, bigger payoff — and only applies to rush melee, not blasts or throws."
asOfVersion: "v2.2 (2026-05-26 update)"
asOfDate: "2026-05-26"
lastVerified: "2026-06-10"
confidence: "community"
sources:
  - "research/04-mechanics-frame-data.md (§3.2 Perception — Sonic Sway row)"
  - "Bandai Namco official patch notes / in-game tutorial (Sonic Sway as frame-perfect Super Perception result)"
---
Sonic Sway is the **frame-perfect payoff** on [[perception|Super Perception]]. When you land a Super Perception against a **Rush** attack on the exact frame, instead of an ordinary deflect your character **sways the rush, counters, and drains the attacker's ki**. Same input as Perception — just a tighter window and a bigger reward.

## The numbers

- **Trigger:** a **frame-perfect Super Perception vs a Rush**. It is not a separate button; it is the best-case outcome of the Perception read against melee.
- **Cost:** because it comes out of a melee Perception read, it costs **ki only** (no skill stock vs a rush) — the same as a normal melee Perception, which is **not** itself officially numbered. The exact ki figure is unpublished.
- **Effect:** dodge + counter **plus an opponent ki drain**, which is the part that distinguishes it from a plain deflect — you don't just avoid the rush, you set the opponent's ki economy back.

## Who has it / what it dodges

- **Universal** — Sonic Sway is a property of the **Super Perception** system, not a character-specific skill, so any fighter with access to Perception can trigger it. (Contrast with auto-dodge *skills* like [[afterimage-strike]] or Wild Sense, which only specific characters equip.)
- **Dodges rush melee only.** It does **not** apply to blasts (those go through the standard 2-stock blast Perception) and does **not** beat [[throws|throws]], which ignore the read entirely.

## Interactions

- Sonic Sway rides on Perception, so every Perception nerf applies to it: it **cannot** be triggered during guard stun (Apr 21, 2025 →), and its activation ki cost has risen with the Apr 2025 and May 2026 Perception passes.
- It overlaps with [[super-counter|Super Counter]] as an answer to rush pressure, but where Super Counter is **free** and reverses position, Sonic Sway costs **ki**, demands a **Super** Perception read, and pays out with a **ki drain** on the attacker.
