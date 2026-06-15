"use client";

import { useMemo, useState } from "react";
import Link from "next/link";

export type Badge = { label: string; tone: string; group: string };
export type DnaRow = {
  name: string;
  slug: string;
  dp: number | null;
  tier?: string;
  badges: Badge[];
};

const TONE: Record<string, string> = {
  good: "border-good/50 bg-good/10 text-good",
  bad: "border-danger/50 bg-danger/10 text-danger",
  ki: "border-ki/50 bg-ki/10 text-ki",
  aura: "border-aura/50 bg-aura/15 text-aura",
  time: "border-time/50 bg-time/10 text-time",
  muted: "border-border bg-surface-2 text-muted",
};

export function DnaExplorer({ rows, groups }: { rows: DnaRow[]; groups: string[] }) {
  const [q, setQ] = useState("");
  const [active, setActive] = useState<string[]>([]);
  const [standardOnly, setStandardOnly] = useState(false);

  const toggle = (g: string) =>
    setActive((a) => (a.includes(g) ? a.filter((x) => x !== g) : [...a, g]));

  const filtered = useMemo(() => {
    const ql = q.trim().toLowerCase();
    return rows.filter((r) => {
      if (ql && !r.name.toLowerCase().includes(ql)) return false;
      if (standardOnly) return r.badges.length === 0;
      if (active.length && !active.every((g) => r.badges.some((b) => b.group === g)))
        return false;
      return true;
    });
  }, [rows, q, active, standardOnly]);

  const sel =
    "rounded-lg border border-border bg-surface-2 px-2 py-1.5 text-xs text-ink outline-none focus:border-ki/60";

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center gap-2">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder={`Filter ${rows.length} fighters…`}
          className={`${sel} w-52`}
        />
        {groups.map((g) => (
          <button
            key={g}
            onClick={() => toggle(g)}
            className={`rounded-lg border px-2 py-1 text-xs transition-colors ${
              active.includes(g)
                ? "border-ki/60 bg-ki/15 text-ki"
                : "border-border bg-surface-2 text-muted hover:text-ink"
            }`}
          >
            {g}
          </button>
        ))}
        <label className="flex items-center gap-1.5 text-xs text-muted">
          <input
            type="checkbox"
            checked={standardOnly}
            onChange={(e) => setStandardOnly(e.target.checked)}
          />
          pure standard chassis only
        </label>
        <span className="ml-auto text-xs tabular-nums text-muted">{filtered.length} shown</span>
      </div>

      <div className="grid gap-2">
        {filtered.map((r) => (
          <div
            key={r.slug}
            className="flex flex-wrap items-center gap-2 rounded-xl border border-border bg-surface px-3 py-2"
          >
            <Link
              href={`/characters/${r.slug}`}
              className="w-64 shrink-0 truncate font-medium text-ki hover:underline"
            >
              {r.name}
            </Link>
            {r.dp != null && (
              <span className="shrink-0 rounded border border-border bg-surface-2 px-1.5 py-0.5 text-[11px] tabular-nums text-muted">
                DP {r.dp}
              </span>
            )}
            {r.tier && (
              <span className="shrink-0 rounded border border-aura/40 bg-aura/10 px-1.5 py-0.5 text-[11px] text-aura">
                {r.tier}
              </span>
            )}
            {r.badges.length === 0 ? (
              <span className="text-xs text-muted">standard chassis — no deviations</span>
            ) : (
              r.badges.map((b, i) => (
                <span
                  key={i}
                  className={`rounded border px-1.5 py-0.5 text-[11px] ${TONE[b.tone] ?? TONE.muted}`}
                >
                  {b.label}
                </span>
              ))
            )}
          </div>
        ))}
      </div>
    </div>
  );
}
