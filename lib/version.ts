/**
 * Single source of truth for "what patch are we documenting".
 *
 * Sparking! ZERO ships balance patches every few months and numbers move every
 * time (damage values, counter windows, skill costs). Every entity carries
 * `lastVerified`/`asOfVersion`, and the UI flags anything stale relative to this.
 */
export const CURRENT_VERSION = {
  patch: "v2.2 (2026-05-26 update)",
  era: "Season 1 complete — Hero of Justice + DAIMA 1/2 + Shallot",
  releaseDate: "2026-05-26",
  rosterSlots: 208,
  dpBudget: 15,
  teamSizeMax: 5,
  rankedSeason: "Season 0 — ends 2026-06-30",
  rankCount: 26,
  nextContent: "Season 2 'Super Limit-Breaking NEO' — Summer 2026 (30+ fighters, Chain Blast, Sparking! Boost)",
} as const;

/** Entities not re-verified within this many days are surfaced as "may be outdated". */
export const STALE_AFTER_DAYS = 240;

export function daysSince(dateISO?: string): number | null {
  if (!dateISO) return null;
  const then = new Date(dateISO).getTime();
  if (Number.isNaN(then)) return null;
  return Math.floor((Date.now() - then) / 86_400_000);
}

export function isStale(lastVerified?: string): boolean {
  const d = daysSince(lastVerified);
  return d === null ? true : d > STALE_AFTER_DAYS;
}
