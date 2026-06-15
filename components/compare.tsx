"use client";

import { useState } from "react";
import Link from "next/link";

export type CompareChar = {
  name: string;
  slug: string;
  dp: number | null;
  hp: number | null;
  kiCharge: number | null;
  kiRecovery: number | null;
  initialKi: number | null;
  drain: number | null;
  stocksMax: number | null;
  tier?: string;
  playstyle?: string;
  classes: string[];
  era: string;
  source: string;
  moves: { name: string; type: string; kiCost: number | null; skillCost: number | null }[];
};

const fmt = (n: number | null | undefined) => (n == null ? "—" : n.toLocaleString("en-US"));

function Cell({ a, b, val, higherBetter = true }: { a: number | null; b: number | null; val: number | null; higherBetter?: boolean }) {
  let cls = "";
  if (a != null && b != null && a !== b && val != null) {
    const best = higherBetter ? Math.max(a, b) : Math.min(a, b);
    cls = val === best ? "text-good font-semibold" : "text-muted";
  }
  return <td className={`px-4 py-2 text-right tabular-nums ${cls}`}>{fmt(val)}</td>;
}

export function CompareTool({ chars }: { chars: CompareChar[] }) {
  const [a, setA] = useState("goku-z-early");
  const [b, setB] = useState("vegeta-z-scouter");
  const ca = chars.find((c) => c.slug === a) ?? chars[0];
  const cb = chars.find((c) => c.slug === b) ?? chars[1];

  const sel =
    "w-full max-w-sm rounded-lg border border-border bg-surface-2 px-3 py-2 text-sm text-ink outline-none focus:border-ki/60";

  const numRows: { label: string; ka: keyof CompareChar; higher: boolean }[] = [
    { label: "DP cost", ka: "dp", higher: false },
    { label: "HP", ka: "hp", higher: true },
    { label: "Ki charge speed", ka: "kiCharge", higher: true },
    { label: "Ki auto-recovery /s", ka: "kiRecovery", higher: true },
    { label: "Starting ki", ka: "initialKi", higher: true },
    { label: "Max skill stocks", ka: "stocksMax", higher: true },
    { label: "Sparking! drain /s", ka: "drain", higher: false },
  ];

  const kit = (c: CompareChar) => (
    <ul className="space-y-1 text-sm">
      {c.moves.map((m, i) => (
        <li key={i} className="flex justify-between gap-3">
          <span>
            <span className="mr-1.5 text-[10px] uppercase text-muted">{m.type}</span>
            {m.name}
          </span>
          <span className="shrink-0 tabular-nums text-muted">
            {m.kiCost != null ? `${fmt(m.kiCost)} ki` : m.skillCost != null ? `${fmt(m.skillCost)} st` : ""}
          </span>
        </li>
      ))}
    </ul>
  );

  return (
    <div className="space-y-6">
      <div className="grid gap-4 sm:grid-cols-2">
        {[
          { v: a, set: setA, c: ca },
          { v: b, set: setB, c: cb },
        ].map(({ v, set, c }, i) => (
          <div key={i} className="space-y-2">
            <select value={v} onChange={(e) => set(e.target.value)} className={sel}>
              {chars.map((ch) => (
                <option key={ch.slug} value={ch.slug}>
                  {ch.name} {ch.dp != null ? `(DP ${ch.dp})` : ""}
                </option>
              ))}
            </select>
            <div className="flex flex-wrap items-center gap-2 text-sm">
              <Link href={`/characters/${c.slug}`} className="font-semibold text-ki hover:underline">
                {c.name}
              </Link>
              {c.tier && <span className="rounded border border-aura/40 bg-aura/10 px-1.5 text-xs text-aura">{c.tier}-tier</span>}
              {c.playstyle && <span className="text-xs text-muted">{c.playstyle}</span>}
            </div>
          </div>
        ))}
      </div>

      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full text-sm" data-sortable-self>
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-4 py-2">Parameter</th>
              <th className="px-4 py-2 text-right">{ca.name}</th>
              <th className="px-4 py-2 text-right">{cb.name}</th>
            </tr>
          </thead>
          <tbody>
            {numRows.map((r) => {
              const va = ca[r.ka] as number | null;
              const vb = cb[r.ka] as number | null;
              return (
                <tr key={r.label} className="border-t border-border">
                  <td className="px-4 py-2 text-muted">{r.label}</td>
                  <Cell a={va} b={vb} val={va} higherBetter={r.higher} />
                  <Cell a={va} b={vb} val={vb} higherBetter={r.higher} />
                </tr>
              );
            })}
            <tr className="border-t border-border">
              <td className="px-4 py-2 text-muted">Era / Source</td>
              <td className="px-4 py-2 text-right text-xs">{ca.era} · {ca.source}</td>
              <td className="px-4 py-2 text-right text-xs">{cb.era} · {cb.source}</td>
            </tr>
            <tr className="border-t border-border">
              <td className="px-4 py-2 text-muted">Classes</td>
              <td className="px-4 py-2 text-right text-xs">{ca.classes.join(", ") || "—"}</td>
              <td className="px-4 py-2 text-right text-xs">{cb.classes.join(", ") || "—"}</td>
            </tr>
          </tbody>
        </table>
      </div>

      <div className="grid gap-4 sm:grid-cols-2">
        <div className="rounded-xl border border-border bg-surface p-4">
          <h3 className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted">{ca.name} — kit</h3>
          {kit(ca)}
        </div>
        <div className="rounded-xl border border-border bg-surface p-4">
          <h3 className="mb-2 text-xs font-semibold uppercase tracking-wider text-muted">{cb.name} — kit</h3>
          {kit(cb)}
        </div>
      </div>
      <p className="text-xs text-muted">
        Green = better value (lower DP, higher everything else). Damage is per-move (blueprint
        data), so kits list datamined costs.
      </p>
    </div>
  );
}
