import { isStale } from "@/lib/version";

/** Format a percentage modifier: 25 -> "+25%", -20 -> "-20%", 0 -> "—". */
export function fmtPct(n: number): string {
  if (n === 0) return "—";
  return `${n > 0 ? "+" : ""}${n}%`;
}

const tierStyles: Record<string, string> = {
  S: "bg-aura/20 text-aura border-aura/40",
  A: "bg-ki/20 text-ki border-ki/40",
  B: "bg-time/20 text-time border-time/40",
  C: "bg-surface-2 text-muted border-border",
  situational: "bg-surface-2 text-muted border-border",
};

export function TierBadge({ tier }: { tier?: string }) {
  if (!tier) return null;
  const cls = tierStyles[tier] ?? tierStyles.C;
  return (
    <span className={`inline-block rounded border px-1.5 py-0.5 text-xs font-medium ${cls}`}>
      {tier === "situational" ? "Situational" : `${tier}-tier`}
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
