# Sparking! ZERO Wiki — Full Audit (2026-06-15)

Parallel 10-agent audit. Each agent writes `audit/agent-NN-<topic>.md` with severity-ranked
findings (BLOCKER / HIGH / MEDIUM / LOW / NIT), each finding citing `file:line`, the evidence
(quote the source-of-truth value vs the page value), and a recommended fix.

## Ground rules (all agents)
- **Source of truth = the game's datamine**, in this order: `data-mined/raw/` (CUE4Parse extract)
  → `data-mined/*.json` (parsed) → `data-mined/enrichment/*.json` (overlays). **Do NOT trust online
  sources** (Game8/Fandom/Reddit) for numeric facts; the game files win. Online sources may only
  corroborate explicitly community-sourced values (DP, vanish cost).
- Critical datamine rules: vanish/Z-Counter cost is **NOT datamined** (community ≈½ bar); Sparking!
  drain = **2,800/s** uniform (not a vanish cost); DP is **community**, not datamined; HP tiers
  30/35/40/45k (counts 9/14/147/16); 10,000 ki = 1 bar, supers ~30k, ults ~50k.
- Generated collections (characters, blasts, skills, transformations, stages, shop) come from
  `scripts/gen_content.py` — fixes belong in the parser/generator/enrichment, NOT hand-edits.
- **Do NOT modify any content/data/code file. Only write your own report under `audit/`.**
- **Do NOT run** `npm run build`, `gen_content.py`, `parse_data.py`, `fix_links.py`,
  `build_enrichment.py` (mutating/heavy, will clobber parallel agents). You MAY run
  `python scripts/audit.py|audit_v3.py|audit_v4.py` (read-only) and read `.next/server/app/*.html`
  (build already green: 1144 pages).
- Windows PowerShell mangles `$`/backslash one-liners — prefer Read/Glob/Grep tools; if you need a
  probe, write a Python script under `audit/` and run it with `python`.

## Assignments
1. Characters data accuracy & integrity
2. Blasts data accuracy & integrity
3. Skills + Transformations data accuracy
4. Mechanics + Glossary + datamine-rule honesty
5. Patches + DLC + Episode-Battles + Game-modes
6. Guides + Research + Meta tier consistency
7. Link integrity & built-HTML graph
8. Python code review (scripts/)
9. TypeScript/Next.js code review (lib/, app/, components/)
10. Cross-cutting frontmatter/schema integrity + rendered-output QA + numeric sanity
