import { isStale } from "@/lib/version";

/** Format a percentage modifier: 25 -> "+25%", -20 -> "-20%", 0 -> "—". */
export function fmtPct(n: number): string {
  if (n === 0) return "—";
  return `${n > 0 ? "+" : ""}${n}%`;
}

// Single source of truth for tier colours (Z is the apex band, above S). Reused by
// the roster table, compare tool, meta board and detail pages so the scale is consistent.
export const TIER_TONE: Record<string, string> = {
  Z: "border-aura/70 bg-aura/25 text-aura ring-1 ring-inset ring-aura/30",
  S: "border-aura/50 bg-aura/15 text-aura",
  A: "border-ki/50 bg-ki/15 text-ki",
  B: "border-time/50 bg-time/15 text-time",
  C: "border-border bg-surface-2 text-muted",
  D: "border-danger/30 bg-danger/10 text-danger",
  unranked: "border-border bg-surface-2 text-muted",
  situational: "border-border bg-surface-2 text-muted",
};

export function tierTone(tier?: string): string {
  return TIER_TONE[tier ?? ""] ?? TIER_TONE.C;
}

/** Tier rank for sorting (Z best → D worst; unranked/missing last). */
export const TIER_RANK: Record<string, number> = {
  Z: 0,
  S: 1,
  A: 2,
  B: 3,
  C: 4,
  D: 5,
};

const tierLabels: Record<string, string> = {
  situational: "Situational",
  unranked: "Unranked",
};

export function TierBadge({ tier, mode }: { tier?: string; mode?: "Singles" | "DP" }) {
  if (!tier) return null;
  const label = tierLabels[tier] ?? `${tier}-tier`;
  return (
    <span
      className={`inline-flex items-center gap-1 rounded border px-1.5 py-0.5 text-xs font-medium ${tierTone(tier)}`}
    >
      {mode && <span className="text-[9px] font-semibold uppercase tracking-wide opacity-70">{mode}</span>}
      {label}
    </span>
  );
}

/** A small "community" / "datamined" provenance marker for an individual value. */
export function ProvenanceTag({ kind }: { kind: "community" | "datamined" | "official" }) {
  const tone =
    kind === "datamined"
      ? "text-ki/90"
      : kind === "official"
        ? "text-good/90"
        : "text-muted";
  const title =
    kind === "datamined"
      ? "Straight from the game files"
      : kind === "official"
        ? "From official patch notes"
        : "Community-sourced — not in the game files; see sources";
  return (
    <span
      title={title}
      className={`rounded bg-surface-2 px-1 py-px text-[9px] font-medium uppercase tracking-wide ${tone}`}
    >
      {kind}
    </span>
  );
}

const confLabel: Record<string, string> = {
  confirmed: "Confirmed",
  datamined: "Datamined",
  community: "Community",
  unverified: "Unverified",
};

export function ConfidenceBadge({ confidence }: { confidence?: string }) {
  if (!confidence) return null;
  return (
    <span className="inline-block rounded border border-border bg-surface-2 px-1.5 py-0.5 text-xs text-muted">
      {confLabel[confidence] ?? confidence}
    </span>
  );
}

const STAT_TONES: Record<string, string> = {
  good: "text-good",
  bad: "text-danger",
  ki: "text-ki",
  aura: "text-aura",
  time: "text-time",
  muted: "text-ink",
};

/** Tone for a +/- percentage: positive = good, negative = danger. */
export function pctTone(n: number): string {
  return n > 0 ? "good" : n < 0 ? "bad" : "muted";
}

/** A prominent row of key numeric facts shown at the top of a detail page. */
export function StatStrip({
  items,
}: {
  items: { label: string; value: string | number | null | undefined; tone?: string }[];
}) {
  const shown = items.filter((i) => i.value != null && i.value !== "" && i.value !== "—");
  if (!shown.length) return null;
  return (
    <div className="flex flex-wrap gap-x-6 gap-y-3 rounded-xl border border-border bg-surface-2/50 px-4 py-3">
      {shown.map((i, idx) => (
        <div key={idx}>
          <div className="text-[10px] font-medium uppercase tracking-wider text-muted">
            {i.label}
          </div>
          <div
            className={`text-lg font-semibold tabular-nums ${STAT_TONES[i.tone ?? "muted"] ?? STAT_TONES.muted}`}
          >
            {i.value}
          </div>
        </div>
      ))}
    </div>
  );
}

export function VerifiedBadge({ lastVerified }: { lastVerified?: string }) {
  if (!lastVerified) return <span className="text-xs text-danger">unverified</span>;
  const stale = isStale(lastVerified);
  return (
    <span className={`text-xs ${stale ? "text-danger" : "text-good"}`}>
      {stale ? "⚠ " : "✓ "}
      {lastVerified}
    </span>
  );
}
