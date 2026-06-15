"use client";

import { useMemo, useState } from "react";
import Link from "next/link";

export type RosterRow = {
  name: string;
  slug: string;
  dp: number | null;
  hp: number | null;
  kiCharge: number | null;
  kiRecovery: number | null;
  stocksInit: number | null;
  stocksMax: number | null;
  era: string;
  source: string;
  tier?: string;
  classes: string[];
  playstyle?: string;
  ult?: string;
  ultKi?: number | null;
  playable: boolean;
};

const fmt = (n: number | null | undefined) => (n == null ? "—" : n.toLocaleString("en-US"));

function dpTone(dp: number | null) {
  if (dp == null) return "border-border bg-surface-2 text-muted";
  if (dp <= 4) return "border-good/50 bg-good/10 text-good";
  if (dp <= 7) return "border-ki/50 bg-ki/10 text-ki";
  return "border-aura/50 bg-aura/15 text-aura";
}

const tierTone: Record<string, string> = {
  S: "border-aura/50 bg-aura/15 text-aura",
  A: "border-ki/50 bg-ki/10 text-ki",
  B: "border-time/50 bg-time/10 text-time",
  C: "border-border bg-surface-2 text-muted",
  D: "border-border bg-surface-2 text-muted",
};

type SortKey =
  | "name"
  | "dp"
  | "hp"
  | "tier"
  | "kiCharge"
  | "kiRecovery"
  | "stocks"
  | "era"
  | "source"
  | "playstyle"
  | "ult";

const tierRank: Record<string, number> = { S: 0, A: 1, B: 2, C: 3, D: 4 };

export function RosterTable({ rows }: { rows: RosterRow[] }) {
  const [q, setQ] = useState("");
  const [era, setEra] = useState("all");
  const [source, setSource] = useState("all");
  const [tier, setTier] = useState("all");
  const [cls, setCls] = useState("all");
  const [showStory, setShowStory] = useState(false);
  const [sort, setSort] = useState<SortKey>("name");
  const [dir, setDir] = useState(1);

  const eras = useMemo(
    () => [...new Set(rows.filter((r) => r.playable).map((r) => r.era))].sort(),
    [rows],
  );
  const classes = useMemo(() => [...new Set(rows.flatMap((r) => r.classes))].sort(), [rows]);

  const filtered = useMemo(() => {
    const ql = q.trim().toLowerCase();
    const out = rows.filter((r) => {
      if (!showStory && !r.playable) return false;
      if (
        ql &&
        !r.name.toLowerCase().includes(ql) &&
        !(r.ult ?? "").toLowerCase().includes(ql) &&
        !(r.playstyle ?? "").toLowerCase().includes(ql)
      )
        return false;
      if (era !== "all" && r.era !== era) return false;
      if (source !== "all" && (source === "Base" ? r.source !== "Base" : r.source === "Base")) return false;
      if (tier !== "all" && r.tier !== tier) return false;
      if (cls !== "all" && !r.classes.includes(cls)) return false;
      return true;
    });
    const numKey = (r: RosterRow, k: SortKey): number | null =>
      k === "dp" ? r.dp : k === "hp" ? r.hp : k === "kiCharge" ? r.kiCharge : k === "kiRecovery" ? r.kiRecovery : k === "stocks" ? r.stocksMax : null;
    out.sort((a, b) => {
      let v = 0;
      if (sort === "name") v = a.name.localeCompare(b.name);
      else if (sort === "tier") v = (tierRank[a.tier ?? ""] ?? 9) - (tierRank[b.tier ?? ""] ?? 9);
      else if (sort === "era") v = a.era.localeCompare(b.era);
      else if (sort === "source") v = a.source.localeCompare(b.source);
      else if (sort === "playstyle") v = (a.playstyle ?? "˜").localeCompare(b.playstyle ?? "˜");
      else if (sort === "ult") v = (a.ult ?? "˜").localeCompare(b.ult ?? "˜");
      else {
        const na = numKey(a, sort);
        const nb = numKey(b, sort);
        v = (na ?? (dir === 1 ? Infinity : -Infinity)) - (nb ?? (dir === 1 ? Infinity : -Infinity));
      }
      return v * dir || a.name.localeCompare(b.name);
    });
    return out;
  }, [rows, q, era, source, tier, cls, showStory, sort, dir]);

  const header = (label: string, key: SortKey, right = false) => (
    <th
      key={key}
      className={`cursor-pointer select-none whitespace-nowrap px-3 py-2 ${right ? "text-right" : "text-left"} hover:text-ink`}
      title="Click to sort"
      onClick={() => {
        if (sort === key) setDir(-dir);
        else {
          setSort(key);
          setDir(1);
        }
      }}
    >
      {label} {sort === key ? <span className="text-aura">{dir === 1 ? "▲" : "▼"}</span> : ""}
    </th>
  );

  const sel =
    "rounded-lg border border-border bg-surface-2 px-2 py-1.5 text-xs text-ink outline-none focus:border-ki/60";

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center gap-2">
        <input
          value={q}
          onChange={(e) => setQ(e.target.value)}
          placeholder={`Filter ${rows.filter((r) => r.playable).length} fighters…`}
          className={`${sel} w-56`}
        />
        <select value={era} onChange={(e) => setEra(e.target.value)} className={sel}>
          <option value="all">All eras</option>
          {eras.map((e) => (
            <option key={e}>{e}</option>
          ))}
        </select>
        <select value={source} onChange={(e) => setSource(e.target.value)} className={sel}>
          <option value="all">Base + DLC</option>
          <option value="Base">Base only</option>
          <option value="DLC">DLC only</option>
        </select>
        <select value={tier} onChange={(e) => setTier(e.target.value)} className={sel}>
          <option value="all">Any tier</option>
          {["S", "A", "B", "C", "D"].map((t) => (
            <option key={t}>{t}</option>
          ))}
        </select>
        <select value={cls} onChange={(e) => setCls(e.target.value)} className={sel}>
          <option value="all">Any class</option>
          {classes.map((c) => (
            <option key={c}>{c}</option>
          ))}
        </select>
        <label className="flex items-center gap-1.5 text-xs text-muted">
          <input type="checkbox" checked={showStory} onChange={(e) => setShowStory(e.target.checked)} />
          include story-only
        </label>
        <span className="ml-auto text-xs tabular-nums text-muted">{filtered.length} shown</span>
      </div>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[1080px] text-sm" data-sortable-self>
          <thead className="bg-surface-2 text-xs uppercase tracking-wide text-muted">
            <tr>
              {header("Fighter", "name")}
              {header("DP", "dp", true)}
              {header("HP", "hp", true)}
              {header("Ki charge", "kiCharge", true)}
              {header("Ki rec /s", "kiRecovery", true)}
              {header("Stocks", "stocks", true)}
              {header("Tier", "tier")}
              {header("Playstyle", "playstyle")}
              {header("Ultimate", "ult")}
              {header("Source", "source")}
            </tr>
          </thead>
          <tbody>
            {filtered.map((r) => (
              <tr key={r.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/characters/${r.slug}`} className="font-medium text-ki hover:underline">
                    {r.name}
                  </Link>
                  {!r.playable && <span className="ml-2 text-[10px] uppercase text-muted">story</span>}
                  {r.classes.length > 0 && (
                    <span className="ml-2 text-[10px] uppercase text-time">{r.classes.join(" · ")}</span>
                  )}
                </td>
                <td className="px-3 py-2 text-right">
                  <span
                    className={`inline-block min-w-7 rounded border px-1.5 py-0.5 text-center text-xs font-semibold tabular-nums ${dpTone(r.dp)}`}
                  >
                    {r.dp ?? "—"}
                  </span>
                </td>
                <td className="px-3 py-2 text-right tabular-nums">{fmt(r.hp)}</td>
                <td className="px-3 py-2 text-right tabular-nums">{fmt(r.kiCharge)}</td>
                <td className="px-3 py-2 text-right tabular-nums">{fmt(r.kiRecovery)}</td>
                <td className="px-3 py-2 text-right tabular-nums">{r.stocksInit != null || r.stocksMax != null ? `${r.stocksInit ?? "·"}/${r.stocksMax ?? "·"}` : "—"}</td>
                <td className="px-3 py-2">
                  {r.tier ? (
                    <span className={`inline-block rounded border px-1.5 py-0.5 text-xs font-medium ${tierTone[r.tier] ?? tierTone.C}`}>
                      {r.tier}
                    </span>
                  ) : (
                    <span className="text-muted">—</span>
                  )}
                </td>
                <td className="px-3 py-2 text-muted">{r.playstyle ?? "—"}</td>
                <td className="px-3 py-2 text-muted">
                  {r.ult ?? "—"}
                  {r.ultKi != null && <span className="tabular-nums"> · {fmt(r.ultKi)} ki</span>}
                </td>
                <td className="px-3 py-2">
                  {r.source === "Base" ? <span className="text-good">Base</span> : <span className="text-aura">{r.source}</span>}
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
