"use client";

import { useState } from "react";
import Link from "next/link";

type TierEntry = { name: string; slug: string; score?: number };
type TierBand = { tier: string; entries: TierEntry[] };
type Counter = { slug: string; name: string; beats: string[]; losesTo: string[]; why: string };

const TIER_STYLE: Record<string, { bar: string; chip: string }> = {
  Z: { bar: "bg-aura text-void", chip: "border-aura/50 bg-aura/10 hover:bg-aura/20" },
  S: { bar: "bg-ki text-void", chip: "border-ki/50 bg-ki/10 hover:bg-ki/20" },
  A: { bar: "bg-time text-void", chip: "border-time/50 bg-time/10 hover:bg-time/20" },
  B: { bar: "bg-surface-2 text-ink", chip: "border-border bg-surface-2 hover:bg-border" },
  C: { bar: "bg-surface-2 text-muted", chip: "border-border bg-surface-2 hover:bg-border" },
  D: { bar: "bg-surface-2 text-muted", chip: "border-border bg-surface/60 hover:bg-border" },
};

export function MetaBoard({
  singles,
  dp,
  counters,
  nameOf,
}: {
  singles: TierBand[];
  dp: TierBand[];
  counters: Counter[];
  nameOf: Record<string, string>;
}) {
  const [tab, setTab] = useState<"singles" | "dp">("singles");
  const bands = tab === "singles" ? singles : dp;

  return (
    <div className="space-y-8">
      <div className="flex gap-2">
        {(["singles", "dp"] as const).map((t) => (
          <button
            key={t}
            onClick={() => setTab(t)}
            className={`rounded-lg border px-4 py-2 text-sm font-medium transition-colors ${
              tab === t
                ? "border-ki/60 bg-ki/15 text-ki"
                : "border-border bg-surface-2 text-muted hover:text-ink"
            }`}
          >
            {t === "singles" ? "Singles (raw power)" : "DP Battle (value per DP)"}
          </button>
        ))}
      </div>

      <div className="space-y-2">
        {bands.map((band) => {
          const st = TIER_STYLE[band.tier] ?? TIER_STYLE.C;
          return (
            <div key={band.tier} className="flex overflow-hidden rounded-xl border border-border">
              <div className={`flex w-14 shrink-0 items-center justify-center text-2xl font-black ${st.bar}`}>
                {band.tier}
              </div>
              <div className="flex flex-wrap gap-1.5 bg-surface p-2.5">
                {band.entries.map((e) => (
                  <Link
                    key={e.slug}
                    href={`/characters/${e.slug}`}
                    className={`rounded-lg border px-2 py-1 text-xs transition-colors ${st.chip}`}
                  >
                    {e.name}
                    {e.score != null && (
                      <span className="ml-1 tabular-nums text-muted">{e.score.toFixed(1)}</span>
                    )}
                  </Link>
                ))}
              </div>
            </div>
          );
        })}
      </div>

      {tab === "singles" && counters.length > 0 && (
        <section className="space-y-2">
          <h2 className="text-lg font-semibold">Counter-pick cheat sheet (top picks)</h2>
          <div className="overflow-x-auto rounded-xl border border-border">
            <table data-sortable-self className="w-full min-w-[760px] text-sm">
              <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
                <tr>
                  <th className="px-3 py-2">Pick</th>
                  <th className="px-3 py-2">Beats</th>
                  <th className="px-3 py-2">Loses to</th>
                  <th className="px-3 py-2">Why</th>
                </tr>
              </thead>
              <tbody>
                {counters.map((c) => (
                  <tr key={c.slug} className="border-t border-border align-top">
                    <td className="px-3 py-2">
                      <Link href={`/characters/${c.slug}`} className="font-medium text-ki hover:underline">
                        {c.name}
                      </Link>
                    </td>
                    <td className="px-3 py-2">
                      <span className="flex flex-wrap gap-1">
                        {c.beats.map((s) => (
                          <Link key={s} href={`/characters/${s}`} className="rounded border border-good/40 bg-good/10 px-1.5 py-0.5 text-xs text-good hover:bg-good/20">
                            {nameOf[s] ?? s}
                          </Link>
                        ))}
                      </span>
                    </td>
                    <td className="px-3 py-2">
                      <span className="flex flex-wrap gap-1">
                        {c.losesTo.map((s) => (
                          <Link key={s} href={`/characters/${s}`} className="rounded border border-danger/40 bg-danger/10 px-1.5 py-0.5 text-xs text-danger hover:bg-danger/20">
                            {nameOf[s] ?? s}
                          </Link>
                        ))}
                      </span>
                    </td>
                    <td className="px-3 py-2 text-xs text-muted">{c.why}</td>
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
        </section>
      )}
    </div>
  );
}
