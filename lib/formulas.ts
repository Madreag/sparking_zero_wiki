/** Number formatting + derived-stat helpers. Numbers-first: every page leans on these. */

/** 12345 -> "12,345" */
export function fmtNum(n: number | null | undefined): string {
  if (n == null) return "—";
  return n.toLocaleString("en-US");
}

/** Format a percentage modifier: 25 -> "+25%", -20 -> "-20%", 0 -> "—". */
export function fmtPct(n: number): string {
  if (n === 0) return "—";
  return `${n > 0 ? "+" : ""}${n}%`;
}

/** Old -> new as a signed percent change: (2358, 2052) -> "-13.0%". */
export function pctChange(oldVal: number, newVal: number): string {
  if (!oldVal) return "—";
  const d = ((newVal - oldVal) / oldVal) * 100;
  return `${d > 0 ? "+" : ""}${d.toFixed(1)}%`;
}

/** Damage per ki BAR spent (10,000 energy = 1 bar; ultimates cost ~5 bars, supers ~2-3). */
export function dmgPerKi(damage?: number | null, kiCost?: number | null): number | null {
  if (!damage || !kiCost) return null;
  return Math.round(damage / (kiCost / 10000));
}

/** Damage per DP — the core team-builder value metric. */
export function dmgPerDp(damage?: number | null, dp?: number | null): number | null {
  if (!damage || !dp) return null;
  return Math.round(damage / dp);
}

/** HP per DP — tankiness value metric. */
export function hpPerDp(hp?: number | null, dp?: number | null): number | null {
  if (!hp || !dp) return null;
  return Math.round(hp / dp);
}
