"use client";

import { useMemo, useState } from "react";
import Link from "next/link";

export type BlastRow = {
  name: string;
  slug: string;
  cls: "super" | "ultimate";
  users: number;
  costs: number[];
  category: string | null;
  maxDamage: number | null;
};

const fmt = (n: number) => n.toLocaleString("en-US");

export function BlastsTable({ rows }: { rows: BlastRow[] }) {
  const [q, setQ] = useState("");
  const [cls, setCls] = useState<"all" | "super" | "ultimate">("all");
  const [cat, setCat] = useState("all");
  const [sort, setSort] = useState<"name" | "users" | "damage">("name");

  const cats = useMemo(
    () => [...new Set(rows.map((r) => r.category).filter((x): x is string => !!x))].sort(),
    [rows],
  );

  const filtered = useMemo(() => {
    const ql = q.trim().toLowerCase();
    const out = rows.filter(
      (r) =>
        (cls === "all" || r.cls === cls) &&
        (cat === "all" || r.category === cat) &&
        (!ql || r.name.toLowerCase().includes(ql)),
    );
    out.sort((a, b) => {
      if (sort === "users") return b.users - a.users || a.name.localeCompare(b.name);
      if (sort === "damage") return (b.maxDamage ?? -1) - (a.maxDamage ?? -1) || a.name.localeCompare(b.name);
      return a.name.localeCompare(b.name);
    });
    return out;
  }, [rows, q, cls, cat, sort]);

  const sel = "rounded-lg border border-border bg-surface-2 px-2 py-1.5 text-xs text-ink outline-none focus:border-ki/60";

  return (
    <div className="space-y-3">
      <div className="flex flex-wrap items-center gap-2">
        <input value={q} onChange={(e) => setQ(e.target.value)} placeholder={`Filter ${rows.length} attacks…`} className={`${sel} w-56`} />
        <select value={cls} onChange={(e) => setCls(e.target.value as typeof cls)} className={sel}>
          <option value="all">Supers + Ultimates</option>
          <option value="super">Supers only</option>
          <option value="ultimate">Ultimates only</option>
        </select>
        <select value={cat} onChange={(e) => setCat(e.target.value)} className={sel}>
          <option value="all">Any category</option>
          {cats.map((c) => (
            <option key={c}>{c}</option>
          ))}
        </select>
        <select value={sort} onChange={(e) => setSort(e.target.value as typeof sort)} className={sel}>
          <option value="name">Sort: name</option>
          <option value="users">Sort: most users</option>
          <option value="damage">Sort: datamined power</option>
        </select>
        <span className="ml-auto text-xs tabular-nums text-muted">{filtered.length} shown</span>
      </div>
      <div className="overflow-x-auto rounded-xl border border-border">
        <table className="w-full min-w-[640px] text-sm" data-sortable-self>
          <thead className="bg-surface-2 text-left text-xs uppercase tracking-wide text-muted">
            <tr>
              <th className="px-3 py-2">Attack</th>
              <th className="px-3 py-2">Class</th>
              <th className="px-3 py-2">Category</th>
              <th className="px-3 py-2 text-right">Users</th>
              <th className="px-3 py-2 text-right">Ki cost(s)</th>
              <th className="px-3 py-2 text-right">Power</th>
            </tr>
          </thead>
          <tbody>
            {filtered.map((b) => (
              <tr key={b.slug} className="border-t border-border hover:bg-surface-2/50">
                <td className="px-3 py-2">
                  <Link href={`/blasts/${b.slug}`} className="font-medium text-ki hover:underline">
                    {b.name}
                  </Link>
                </td>
                <td className="px-3 py-2">
                  <span className={b.cls === "ultimate" ? "text-aura" : "text-muted"}>{b.cls}</span>
                </td>
                <td className="px-3 py-2 text-muted">{b.category ?? "—"}</td>
                <td className="px-3 py-2 text-right tabular-nums">{b.users}</td>
                <td className="px-3 py-2 text-right tabular-nums">
                  {b.costs.length ? b.costs.map(fmt).join(" / ") : "—"}
                </td>
                <td className="px-3 py-2 text-right tabular-nums">{b.maxDamage != null ? fmt(b.maxDamage) : "—"}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
